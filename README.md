# HomeAssistant-BIR
[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg?style=for-the-badge)](https://github.com/sikksakk/HomeAssistant-BIR)

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]][license]

[![Project Maintenance][maintenance-shield]][user_profile]

[![Discord][discord-shield]][discord]

_Component to integrate with [BIR][bir]._

BIR integrasjon som trigger dagen når renovasjonen blir hentet: https://bir.no/adressesoek

**This component will set up the following platforms.**

| Platform | Description         |
| -------- | ------------------- |
| `next_recycle` | Next date for recycle pickup.  |
| `days_until_recycle` | Days left until recycle pickup. |
| `bool_recycle_day` | True if recycle pickup date is tomorrow. |
| `next_waste` | Next date for waste pickup.  |
| `days_until_waste` | Days left until waste pickup. |
| `bool_waste_day` | True if waste pickup date is tomorrow. |

## Installation

### Method 1 (Installation using HACS)

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=sikksakk&repository=HomeAssistant-BIR&category=integration)

### Method 2 (Manual)
Copy contents of custom_components/bir/ to custom_components/bir/ in your Home Assistant config folder.

## Configuration is done in the UI

<!---->

---

[bir]: https://bir.no
[commits-shield]: https://img.shields.io/github/commit-activity/y/sikksakk/HomeAssistant-BIR.svg?style=for-the-badge
[commits]: https://github.com/sikksakk/HomeAssistant-BIR/commits/master
[discord]: https://discord
[discord-shield]: https://img.shields.io/discord/xxxx.svg?style=for-the-badge
[license]: https://github.com/sikksakk/HomeAssistant-BIR/blob/master/LICENSE
[license-shield]: https://img.shields.io/github/license/sikkasakk/HomeAssistant-BIR.svg?style=for-the-badge
[maintenance-shield]: https://img.shields.io/badge/maintainer-%40sikksakk-blue.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/sikksakk/HomeAssistant-BIR.svg?style=for-the-badge
[releases]: https://github.com/sikksakk/HomeAssistant-BIR/releases
[user_profile]: https://github.com/sikksakk