# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class MaintenanceWindow(DaraModel):
    def __init__(
        self,
        duration: str = None,
        enable: bool = None,
        exclusions: List[main_models.MaintenanceWindowExclusions] = None,
        maintenance_time: str = None,
        recurrence: str = None,
        weekly_period: str = None,
    ):
        # The maintenance duration. Valid values: 1 to 24. Unit: hours.
        # 
        # Default value: 3h.
        self.duration = duration
        # Specifies whether to enable the maintenance window. Valid values:
        # - `true`: Enables the maintenance window.
        # - `false`: Does not enable the maintenance window.
        # 
        # Default value: `false`.
        self.enable = enable
        # The list of exclusions for the maintenance window. A maximum of 10 exclusions are supported. Exclusions take precedence over the maintenance window. If an active exclusion covers an O&M type, the O&M operation is not performed even if the current time is within the maintenance window. If multiple exclusions are active at the same time, the union of the exclusions is applied. The total number of NoOperations and NoUpgrades exclusions cannot exceed 3. Only one-time periods are supported. Periodic configurations are not supported.
        self.exclusions = exclusions
        # The start time of the maintenance window. The time must be in the RFC 3339 standard format.
        self.maintenance_time = maintenance_time
        # The recurrence rule for the maintenance window, defined by using the RFC 5545 Recurrence Rule syntax. Only FREQ=WEEKLY is supported. COUNT and UNTIL are not supported.
        self.recurrence = recurrence
        # The weekly maintenance period. Separate multiple values with commas (,). Valid values: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, and Sunday.
        # 
        # Default value: `Thursday`.
        self.weekly_period = weekly_period

    def validate(self):
        if self.exclusions:
            for v1 in self.exclusions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['duration'] = self.duration

        if self.enable is not None:
            result['enable'] = self.enable

        result['exclusions'] = []
        if self.exclusions is not None:
            for k1 in self.exclusions:
                result['exclusions'].append(k1.to_map() if k1 else None)

        if self.maintenance_time is not None:
            result['maintenance_time'] = self.maintenance_time

        if self.recurrence is not None:
            result['recurrence'] = self.recurrence

        if self.weekly_period is not None:
            result['weekly_period'] = self.weekly_period

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('duration') is not None:
            self.duration = m.get('duration')

        if m.get('enable') is not None:
            self.enable = m.get('enable')

        self.exclusions = []
        if m.get('exclusions') is not None:
            for k1 in m.get('exclusions'):
                temp_model = main_models.MaintenanceWindowExclusions()
                self.exclusions.append(temp_model.from_map(k1))

        if m.get('maintenance_time') is not None:
            self.maintenance_time = m.get('maintenance_time')

        if m.get('recurrence') is not None:
            self.recurrence = m.get('recurrence')

        if m.get('weekly_period') is not None:
            self.weekly_period = m.get('weekly_period')

        return self

class MaintenanceWindowExclusions(DaraModel):
    def __init__(
        self,
        description: str = None,
        end_time: str = None,
        name: str = None,
        scope: str = None,
        start_time: str = None,
    ):
        # The description of the exclusion. The description can be up to 128 characters in length and does not support 4-byte characters such as emojis.
        self.description = description
        # The end time of the exclusion. The time must be in the RFC 3339 standard format, later than the start_time, and later than the current time. Maximum duration for a single exclusion: 30 days for NoOperations, NoUpgrades, and NoCVEPatch, and 180 days for NoMinorUpgrades.
        self.end_time = end_time
        # The name of the exclusion. The name must be 1 to 63 characters in length and can contain digits, underscores (_), and hyphens (-). It must start with an uppercase or lowercase letter, a Chinese character, or a digit. The name must be unique within the same maintenance window. If you do not specify this parameter, a default name in the format of exclusion-{random string} is generated.
        self.name = name
        # The scope of the exclusion, which specifies the proactive O&M types that are prohibited during this time period. Valid values (case-sensitive):
        # - NoOperations: Prohibits all proactive O&M operations, including cluster upgrades, component upgrades, CVE patching, and OS image updates.
        # - NoUpgrades: Prohibits cluster upgrades and component upgrades, but still allows CVE patching and responses to scheduled ECS events.
        # - NoMinorUpgrades: Prohibits only minor version upgrades for clusters, but still allows patch upgrades, component upgrades, and CVE patching.
        # - NoCVEPatch: Prohibits automatic CVE patching.
        self.scope = scope
        # The start time of the exclusion. The time must be in the RFC 3339 standard format and use the same time zone offset as the end_time and maintenance_time.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.end_time is not None:
            result['end_time'] = self.end_time

        if self.name is not None:
            result['name'] = self.name

        if self.scope is not None:
            result['scope'] = self.scope

        if self.start_time is not None:
            result['start_time'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('end_time') is not None:
            self.end_time = m.get('end_time')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('scope') is not None:
            self.scope = m.get('scope')

        if m.get('start_time') is not None:
            self.start_time = m.get('start_time')

        return self

