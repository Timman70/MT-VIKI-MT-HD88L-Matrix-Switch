from homeassistant import config_entries
import voluptuous as vol
from .const import DOMAIN

class MatrixSwitchConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            ip_address = user_input["ip_address"]
            await self.async_set_unique_id(ip_address)
            self._abort_if_unique_id_configured()
            return self.async_create_entry(title="MT-HD88L Matrix", data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("ip_address"): str
            }),
            errors=errors
        )
