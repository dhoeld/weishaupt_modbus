"""Select."""

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import TYPES
from .hpconst import DEVICELISTS
from .entities import build_entity_list
from .coordinator import MyCoordinator


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Select entry setup."""
    _modbus_api = config_entry.runtime_data

    entries = []

    for _useless, device in enumerate(DEVICELISTS):
        coordinator = MyCoordinator(hass, _modbus_api, device, config_entry)
        await coordinator.async_config_entry_first_refresh()

        entries = await build_entity_list(
            entries, config_entry, device, TYPES.SELECT, coordinator
        )

    async_add_entities(
        entries,
        update_before_add=True,
    )
