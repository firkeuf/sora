"""The Sora integration."""
from __future__ import annotations

from typing import Any, Dict
from datetime import timedelta
from statistics import mean

from homeassistant.config_entries import ConfigEntry, current_entry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .const import DOMAIN, API, CONF_RATE
from .athlios import async_get

import logging


_LOGGER = logging.getLogger(__name__)

PLATFORMS = ["sensor"]


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Sora from a config entry."""
    coordinator = SoraDataUpdateCoordinator(hass)
    await coordinator.async_config_entry_first_refresh()
    entry.async_on_unload(entry.add_update_listener(update_listener))
    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = coordinator
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok


async def update_listener(hass: HomeAssistant, entry: ConfigEntry) -> None:
    """Update listener."""
    await hass.config_entries.async_reload(entry.entry_id)


class SoraDataUpdateCoordinator(DataUpdateCoordinator):
    """Class to manage fetching data from Sora API."""
    def __init__(self, hass: HomeAssistant, ) -> None:
        """Initialize."""
        self.config_entry = current_entry.get()
        update_interval = timedelta(seconds=self.config_entry.data.get(CONF_RATE))
        self.units = hass.config.units
        _LOGGER.debug("Data will be update every %s", update_interval)
        super().__init__(hass, _LOGGER, name=DOMAIN, update_interval=update_interval)

    async def _async_update_data(self) -> dict[str, Any]:
        """Update data via library."""
        host = self.config_entry.data.get('host')
        response = await async_get(self.hass, host, API['Device'], API['protocol'])
        result = {}

        result.update({'Temperature': response.get('Temperature')})
        result.update({'Humidity': response.get('Humidity')})
        result.update({'CO2': response.get('CO2')})
        result.update({'P0P3': response.get('Countp3')})
        result.update({'P0P5': response.get('Countp5')})
        result.update({'P1': response.get('Count1')})
        result.update({'P5': response.get('Count5')})
        result.update({'P10': response.get('Count10')})
        result.update({'P2P5': response.get('Count2p5')})

        return result
