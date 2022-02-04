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
    hass.config_entries.async_setup_platforms(entry, PLATFORMS)
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
        self.is_metric = hass.config.units.is_metric
        _LOGGER.debug("Data will be update every %s", update_interval)
        super().__init__(hass, _LOGGER, name=DOMAIN, update_interval=update_interval)

    async def _async_update_data(self) -> dict[str, Any]:
        """Update data via library."""
        host = self.config_entry.data.get('host')
        response = await async_get(self.hass, host, API['Device'], API['protocol'])
        result = {}
        result.update({k:v for e in response.get('General') for (k,v) in e.items()})
        result.update({k:v for e in response.get('Averages') for (k,v) in e.items()})

        if result.get('Model') == 'Pro':
            result.update({'C2H5OH': max(response.get('C2H5OH')[0].popitem()[1], response.get('C2H5OH')[1].popitem()[1])})
            result.update({k:v for e in response.get('Misc') for (k,v) in e.items()})
            result.update({'CO': response.get('CO')[0].popitem()[1]})
            result.update({'NH3': response.get('NH3')[0].popitem()[1]})
            result.update({'NO2': response.get('NO2')[0].popitem()[1]})
            result.update({'C3H8': response.get('C3H8')[0].popitem()[1]})
            result.update({'C4H10': response.get('C4H10')[0].popitem()[1]})
            result.update({'CH4': response.get('CH4')[0].popitem()[1]})
            result.update({'H2': response.get('H2')[0].popitem()[1]})
            result.update({'P0P3': mean([float(response.get('ParticulateTenthLiterAir')[0].get('Ap3')),
                                         float(response.get('ParticulateTenthLiterAir')[1].get('Bp3'))])})
            result.update({'P0P5': mean([float(response.get('ParticulateTenthLiterAir')[0].get('Ap5')),
                                         float(response.get('ParticulateTenthLiterAir')[1].get('Bp5'))])})
            result.update({'P1': mean([float(response.get('ParticulateTenthLiterAir')[0].get('A1')),
                                       float(response.get('ParticulateTenthLiterAir')[1].get('B1'))])})
            result.update({'P5': mean([float(response.get('ParticulateTenthLiterAir')[0].get('A5')),
                                       float(response.get('ParticulateTenthLiterAir')[1].get('B5'))])})
            result.update({'P10': mean([float(response.get('ParticulateTenthLiterAir')[0].get('A10')),
                                        float(response.get('ParticulateTenthLiterAir')[1].get('B10'))])})
            result.update({'P2P5': mean([float(response.get('ParticulateConcentration')[0].get('A2p5')),
                                         float(response.get('ParticulateConcentration')[1].get('B2p5'))])})
        else:
            result.update({'P0P3': response.get('ParticulateTenthLiterAir')[0].get('Ap3')})
            result.update({'P0P5': response.get('ParticulateTenthLiterAir')[0].get('Ap5')})
            result.update({'P1': response.get('ParticulateTenthLiterAir')[0].get('A1')})
            result.update({'P5': response.get('ParticulateTenthLiterAir')[0].get('A5')})
            result.update({'P10': response.get('ParticulateTenthLiterAir')[0].get('A10')})
            result.update({'P2P5': response.get('ParticulateConcentration')[0].get('A2p5')})

        return result
