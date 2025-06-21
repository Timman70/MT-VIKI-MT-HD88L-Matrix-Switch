from homeassistant.components.button import ButtonEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.device_registry import DeviceInfo
import requests
from .const import DOMAIN

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback):
    ip_address = entry.data["ip_address"]
    device_id = entry.entry_id
    device_info = DeviceInfo(
        identifiers={(DOMAIN, device_id)},
        name="MT-HD88L Matrix",
        manufacturer="Matrix",
        model="MT-HD88L Matrix"
    )
    entities = []

    for input_ch in range(1, 9):
        for output_ch in range(1, 9):
            name = f"Input {input_ch} → Output {output_ch}"
            unique_id = f"{input_ch}_{output_ch}"
            entities.append(MatrixSwitchButton(name, unique_id, ip_address, input_ch, output_ch, device_info))

    async_add_entities(entities)

class MatrixSwitchButton(ButtonEntity):
    def __init__(self, name, unique_id, ip_address, input_ch, output_ch, device_info):
        self._attr_name = name
        self._attr_unique_id = unique_id
        self._ip = ip_address
        self._input = input_ch
        self._output = output_ch
        self._attr_icon = "mdi:hdmi-port"
        self._attr_device_info = device_info

    def press(self) -> None:
        payload = {"COMMAND": f"SW {self._input} {self._output} "}
        data = {'matrixdata': str(payload).replace("'", '\"')}

        try:
            response = requests.post(
                f"http://{self._ip}/cgi-bin/matrixs.cgi",
                headers={
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Authorization': 'Basic YWRtaW46YWRtaW4='
                },
                data=data,
                timeout=5
            )
            print(f"[MatrixSwitch] Sent: SW {self._input} {self._output}, Status: {response.status_code}, Response: {response.text}")
        except Exception as e:
            print(f"[MatrixSwitch] ERROR sending command: {e}")
