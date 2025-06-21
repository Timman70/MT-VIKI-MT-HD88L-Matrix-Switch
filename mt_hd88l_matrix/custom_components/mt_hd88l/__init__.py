# Credit: timcloud
from .const import DOMAIN

PLATFORMS = ["button"]

async def async_setup_entry(hass, entry):
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = entry.data
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True

async def async_unload_entry(hass, entry):
    await hass.config_entries.async_forward_entry_unloads(entry, PLATFORMS)
    hass.data[DOMAIN].pop(entry.entry_id)
    return True
