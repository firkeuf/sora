
"""Platform for sensor integration."""
from homeassistant.const import ATTR_ATTRIBUTION, ATTR_DEVICE_CLASS, ATTR_ICON, CONF_NAME
from homeassistant.components.sensor import ATTR_STATE_CLASS, SensorEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from homeassistant.helpers.typing import StateType
from homeassistant.helpers.entity import DeviceInfo

import logging

from .const import (
    DOMAIN,
    SENSOR_TYPES,
    ATTR_LABEL,
    ATTRIBUTION,
    ATTR_UNIT_IMPERIAL,
    ATTR_UNIT_METRIC,
    MANUFACTURER,
    MODEL,
    ATTR_ENABLED
)
from . import SoraDataUpdateCoordinator


_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass, entry, async_add_entities) -> None:
    name: str = entry.data[CONF_NAME]
    coordinator: SoraDataUpdateCoordinator = hass.data[DOMAIN][entry.entry_id]
    sensors: list[SoraSensor] = []
    for sensor in SENSOR_TYPES:
        sensors.append(SoraSensor(name, sensor, coordinator))
    async_add_entities(sensors)


class SoraSensor(CoordinatorEntity, SensorEntity):
    """Representation of a Sensor."""
    coordinator: SoraDataUpdateCoordinator

    def __init__( self, name: str, kind: str, coordinator: SoraDataUpdateCoordinator) -> None:
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._sensor_data = coordinator.data
        self._description = SENSOR_TYPES[kind]
        self._name = name
        self.kind = kind
        self._device_class = None
        self._attrs = {ATTR_ATTRIBUTION: ATTRIBUTION}
        self._attr_state_class = self._description.get(ATTR_STATE_CLASS)


    @property
    def name(self) -> str:
        """Return the name."""
        return f"{self._name} {self._description[ATTR_LABEL]}"

    @property
    def state(self) -> StateType:
        """Return the state of the entity."""
        if not self.coordinator.is_metric and self.kind == "Temperature":
            return float(self.coordinator.data.get(self.kind)) * 1.8 + 32
        return self.coordinator.data.get(self.kind)

    @property
    def device_class(self):
        return self._description[ATTR_DEVICE_CLASS]

    @property
    def icon(self):
        """Return the icon."""
        return self._description[ATTR_ICON]

    @property
    def unique_id(self) -> str:
        """Return a unique_id for this entity."""
        return f"{self.coordinator.config_entry.data.get('sora_id')}-{self.kind}".lower()

    @property
    def unit_of_measurement(self):
        """Return the unit the value is expressed in."""
        if self.coordinator.is_metric:
            return self._description[ATTR_UNIT_METRIC]
        return self._description[ATTR_UNIT_IMPERIAL]

    @property
    def device_info(self) -> DeviceInfo:
        """Return the device info."""
        return {
            "identifiers": {(DOMAIN, self.coordinator.config_entry.unique_id)},
            "name": f"{self.coordinator.config_entry.data.get(CONF_NAME)}",
            "manufacturer": MANUFACTURER,
            "model": self._sensor_data.get(MODEL),
            "entry_type": "service",
        }

    @property
    def entity_registry_enabled_default(self) -> bool:
        """Return if the entity should be enabled when first added to the entity registry."""
        if not self.coordinator.data.get(self.kind):
            return False
        return self._description[ATTR_ENABLED]