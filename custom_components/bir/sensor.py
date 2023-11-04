"""Sensor platform for BIR."""
import datetime
from homeassistant.components.sensor import SensorEntity

from .const import DAYS, DEFAULT_NAME, DOMAIN, ICON, ICON_OPEN, SENSOR
from .entity import IntegrationBIREntity


async def async_setup_entry(hass, entry, async_add_devices):
    """Setup sensor platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_devices(
        [
            IntegrationBIRSensor(coordinator, entry),
            IntegrationBIRSensorNext(coordinator, entry),
            IntegrationBIRSensorNextRelative(coordinator, entry),
        ]
    )


class IntegrationBIRSensor(IntegrationBIREntity, SensorEntity):
    """BIR Sensor class."""

    @property
    def name(self):
        """Return the name of the sensor."""
        return f"{DEFAULT_NAME}_{SENSOR}"

    @property
    def native_value(self):
        """Return the native value of the sensor."""
        return self.coordinator.data.get("delivery_dates")

    @property
    def icon(self):
        """Return the icon of the sensor."""
        if datetime.date.today() == self._next_delivery:
            return ICON_OPEN
        return ICON


class IntegrationBIRSensorNext(IntegrationBIREntity, SensorEntity):
    """BIR Sensor class."""

    @property
    def unique_id(self):
        """Return a unique ID to use for this entity."""
        return f"{self.config_entry.entry_id}-next"

    @property
    def name(self):
        """Return the name of the sensor."""
        return f"{DEFAULT_NAME}_{SENSOR}_next"

    @property
    def native_value(self):
        """Return the native value of the sensor."""
        return self._next_delivery.strftime("%Y-%m-%d")

    @property
    def icon(self):
        """Return the icon of the sensor."""
        if datetime.date.today() == self._next_delivery:
            return ICON_OPEN
        return ICON


class IntegrationBIRSensorNextRelative(IntegrationBIREntity, SensorEntity):
    """BIR Sensor class."""

    @property
    def unique_id(self):
        """Return a unique ID to use for this entity."""
        return f"{self.config_entry.entry_id}-next-relative"

    @property
    def name(self):
        """Return the name of the sensor."""
        return f"{DEFAULT_NAME}_{SENSOR}_next_relative"

    @property
    def native_value(self):
        """Return the native value of the sensor."""
        today = datetime.date.today()
        if today == self._next_delivery:
            return "I dag"
        if (today + datetime.timedelta(days=1)) == self._next_delivery:
            return "I morgen"
        return DAYS[self._next_delivery.strftime("%w")]

    @property
    def icon(self):
        """Return the icon of the sensor."""
        if datetime.date.today() == self._next_delivery:
            return ICON_OPEN
        return ICON
