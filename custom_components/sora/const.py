"""Constants for the Sora integration."""
from __future__ import annotations

from typing import Final, TypedDict

from homeassistant.components.sensor import (
    ATTR_STATE_CLASS,
    SensorStateClass,
    SensorDeviceClass

)

from homeassistant.const import (
    ATTR_DEVICE_CLASS,
    ATTR_ICON,
    PERCENTAGE,
    TEMP_CELSIUS,
    TEMP_FAHRENHEIT,
    PRESSURE_MBAR,
    CONCENTRATION_PARTS_PER_BILLION,
    CONCENTRATION_PARTS_PER_MILLION,
    CONCENTRATION_MICROGRAMS_PER_CUBIC_METER
)

API_IMPERIAL: Final = "Imperial"
API_METRIC: Final = "Metric"
ATTR_ENABLED: Final = "enabled"
ATTR_LABEL: Final = "label"
ATTR_UNIT_IMPERIAL: Final = "unit_imperial"
ATTR_UNIT_METRIC: Final = "unit_metric"
MANUFACTURER: Final = "AthliOS, Inc."
NAME: Final = "Sora"
ATTRIBUTION: Final = "Data from Sora"
DOMAIN: Final = "sora"
MODEL: Final = "Model"
MODEL_PRO: Final = "Pro"
MODEL_MINI: Final = "Mini"
MODEL_v2: Final = "Sora v2"

CONF_RATE: Final = "rate"


API = {
    "protocol": "http",
    "System": "/webapi/v1/Horizon/System/View",
    "Device": "/webapi/v1/Horizon/Device/DataType",
}


SENSOR_TYPES: Final[dict[str, SensorDescription]] = {
    "Temperature": {
        ATTR_DEVICE_CLASS: SensorDeviceClass.TEMPERATURE,
        ATTR_ICON: None,
        ATTR_LABEL: "Temperature",
        ATTR_UNIT_METRIC: TEMP_CELSIUS,
        ATTR_UNIT_IMPERIAL: TEMP_FAHRENHEIT,
        ATTR_ENABLED: True,
        ATTR_STATE_CLASS: SensorStateClass.MEASUREMENT,
    },
    "Humidity": {
        ATTR_DEVICE_CLASS: SensorDeviceClass.HUMIDITY,
        ATTR_ICON: None,
        ATTR_LABEL: "Humidity",
        ATTR_UNIT_METRIC: PERCENTAGE,
        ATTR_UNIT_IMPERIAL: PERCENTAGE,
        ATTR_ENABLED: True,
        ATTR_STATE_CLASS: SensorStateClass.MEASUREMENT,
    },
    "AbsolutePressure": {
        ATTR_DEVICE_CLASS: SensorDeviceClass.PRESSURE,
        ATTR_ICON: None,
        ATTR_LABEL: "Absolute Pressure",
        ATTR_UNIT_METRIC: PRESSURE_MBAR,
        ATTR_UNIT_IMPERIAL: PRESSURE_MBAR,
        ATTR_ENABLED: True,
        ATTR_STATE_CLASS: SensorStateClass.MEASUREMENT,
    },
    "TVOC": {
        ATTR_DEVICE_CLASS: None,
        ATTR_ICON: "mdi:flask-outline",
        ATTR_LABEL: "TVOC",
        ATTR_UNIT_METRIC: CONCENTRATION_PARTS_PER_BILLION,
        ATTR_UNIT_IMPERIAL: CONCENTRATION_PARTS_PER_BILLION,
        ATTR_ENABLED: True,
        ATTR_STATE_CLASS: SensorStateClass.MEASUREMENT,
    },
    "CO2": {
        ATTR_DEVICE_CLASS: SensorDeviceClass.CO2,
        ATTR_ICON: None,
        ATTR_LABEL: "CO2",
        ATTR_UNIT_METRIC: CONCENTRATION_PARTS_PER_MILLION,
        ATTR_UNIT_IMPERIAL: CONCENTRATION_PARTS_PER_MILLION,
        ATTR_ENABLED: True,
        ATTR_STATE_CLASS: SensorStateClass.MEASUREMENT,
    },


    'CO': {
        ATTR_DEVICE_CLASS: SensorDeviceClass.CO,
        ATTR_ICON: None,
        ATTR_LABEL: "CO",
        ATTR_UNIT_METRIC: CONCENTRATION_PARTS_PER_BILLION,
        ATTR_UNIT_IMPERIAL: CONCENTRATION_PARTS_PER_BILLION,
        ATTR_ENABLED: True,
        ATTR_STATE_CLASS: SensorStateClass.MEASUREMENT,
    },
    'NH3': {
        ATTR_DEVICE_CLASS: None,
        ATTR_ICON: "mdi:chemical-weapon",
        ATTR_LABEL: "Ammonia",
        ATTR_UNIT_METRIC: CONCENTRATION_PARTS_PER_BILLION,
        ATTR_UNIT_IMPERIAL: CONCENTRATION_PARTS_PER_BILLION,
        ATTR_ENABLED: True,
        ATTR_STATE_CLASS: SensorStateClass.MEASUREMENT,
    },
    'NO2': {
        ATTR_DEVICE_CLASS: None,
        ATTR_ICON: "mdi:gas-cylinder",
        ATTR_LABEL: "Nitrogen",
        ATTR_UNIT_METRIC: CONCENTRATION_PARTS_PER_MILLION,
        ATTR_UNIT_IMPERIAL: CONCENTRATION_PARTS_PER_MILLION,
        ATTR_ENABLED: True,
        ATTR_STATE_CLASS: SensorStateClass.MEASUREMENT,
    },
    'C3H8': {
        ATTR_DEVICE_CLASS: None,
        ATTR_ICON: "mdi:tailwind",
        ATTR_LABEL: "Propane",
        ATTR_UNIT_METRIC: CONCENTRATION_PARTS_PER_MILLION,
        ATTR_UNIT_IMPERIAL: CONCENTRATION_PARTS_PER_MILLION,
        ATTR_ENABLED: True,
        ATTR_STATE_CLASS: SensorStateClass.MEASUREMENT,
    },
    'C4H10': {
        ATTR_DEVICE_CLASS: None,
        ATTR_ICON: "mdi:tailwind",
        ATTR_LABEL: "Butane",
        ATTR_UNIT_METRIC: CONCENTRATION_PARTS_PER_MILLION,
        ATTR_UNIT_IMPERIAL: CONCENTRATION_PARTS_PER_MILLION,
        ATTR_ENABLED: True,
        ATTR_STATE_CLASS: SensorStateClass.MEASUREMENT,
    },
    'CH4': {
        ATTR_DEVICE_CLASS: None,
        ATTR_ICON: "mdi:tailwind",
        ATTR_LABEL: "Methane",
        ATTR_UNIT_METRIC: CONCENTRATION_PARTS_PER_MILLION,
        ATTR_UNIT_IMPERIAL: CONCENTRATION_PARTS_PER_MILLION,
        ATTR_ENABLED: True,
        ATTR_STATE_CLASS: SensorStateClass.MEASUREMENT,
    },
    'H2': {
        ATTR_DEVICE_CLASS: None,
        ATTR_ICON: "mdi:balloon",
        ATTR_LABEL: "Hydrogen",
        ATTR_UNIT_METRIC: CONCENTRATION_PARTS_PER_MILLION,
        ATTR_UNIT_IMPERIAL: CONCENTRATION_PARTS_PER_MILLION,
        ATTR_ENABLED: True,
        ATTR_STATE_CLASS: SensorStateClass.MEASUREMENT,
    },
    'C2H5OH': {
        ATTR_DEVICE_CLASS: None,
        ATTR_ICON: "mdi:glass-cocktail",
        ATTR_LABEL: "Ethanol",
        ATTR_UNIT_METRIC: CONCENTRATION_PARTS_PER_MILLION,
        ATTR_UNIT_IMPERIAL: CONCENTRATION_PARTS_PER_MILLION,
        ATTR_ENABLED: True,
        ATTR_STATE_CLASS: SensorStateClass.MEASUREMENT,
    },

    'P0P3': {
        ATTR_DEVICE_CLASS: None,
        ATTR_ICON: "mdi:chart-bubble",
        ATTR_LABEL: "Particulate 0.3",
        ATTR_UNIT_METRIC: CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
        ATTR_UNIT_IMPERIAL: CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
        ATTR_ENABLED: True,
        ATTR_STATE_CLASS: SensorStateClass.MEASUREMENT,
    },
    'P0P5': {
        ATTR_DEVICE_CLASS: None,
        ATTR_ICON: "mdi:chart-bubble",
        ATTR_LABEL: "Particulate 0.5",
        ATTR_UNIT_METRIC: CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
        ATTR_UNIT_IMPERIAL: CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
        ATTR_ENABLED: True,
        ATTR_STATE_CLASS: SensorStateClass.MEASUREMENT,
    },
    'P1': {
        ATTR_DEVICE_CLASS: None,
        ATTR_ICON: "mdi:chart-bubble",
        ATTR_LABEL: "Particulate 1",
        ATTR_UNIT_METRIC: CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
        ATTR_UNIT_IMPERIAL: CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
        ATTR_ENABLED: True,
        ATTR_STATE_CLASS: SensorStateClass.MEASUREMENT,
    },
    'P2P5': {
        ATTR_DEVICE_CLASS: None,
        ATTR_ICON: "mdi:chart-bubble",
        ATTR_LABEL: "Particulate 2.5",
        ATTR_UNIT_METRIC: CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
        ATTR_UNIT_IMPERIAL: CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
        ATTR_ENABLED: True,
        ATTR_STATE_CLASS: SensorStateClass.MEASUREMENT,
    },
    'P5': {
        ATTR_DEVICE_CLASS: None,
        ATTR_ICON: "mdi:chart-bubble",
        ATTR_LABEL: "Particulate 5",
        ATTR_UNIT_METRIC: CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
        ATTR_UNIT_IMPERIAL: CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
        ATTR_ENABLED: True,
        ATTR_STATE_CLASS: SensorStateClass.MEASUREMENT,
    },
    'P10': {
        ATTR_DEVICE_CLASS: None,
        ATTR_ICON: "mdi:chart-bubble",
        ATTR_LABEL: "Particulate 10",
        ATTR_UNIT_METRIC: CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
        ATTR_UNIT_IMPERIAL: CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
        ATTR_ENABLED: True,
        ATTR_STATE_CLASS: SensorStateClass.MEASUREMENT,
    },

}


class SensorDescription(TypedDict, total=False):
    """Sensor description class."""

    device_class: str | None
    icon: str | None
    label: str
    unit_metric: str | None
    unit_imperial: str | None
    enabled: bool
    state_class: str | None