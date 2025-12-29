# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateApplicationShrinkRequest(DaraModel):
    def __init__(
        self,
        alarm_config_shrink: str = None,
        delete_alarm_rules_before_update: bool = None,
        description: str = None,
        name: str = None,
        region_id: str = None,
        tags_shrink: str = None,
    ):
        # The configurations of application alerts.
        self.alarm_config_shrink = alarm_config_shrink
        # Specifies whether to delete existing alert rules before applying the alert template. Default value: false.
        self.delete_alarm_rules_before_update = delete_alarm_rules_before_update
        # The description to be updated for the application.
        self.description = description
        # The application name.
        # 
        # This parameter is required.
        self.name = name
        # The region ID. Set the value to cn-hangzhou.
        self.region_id = region_id
        # The tags.
        self.tags_shrink = tags_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_config_shrink is not None:
            result['AlarmConfig'] = self.alarm_config_shrink

        if self.delete_alarm_rules_before_update is not None:
            result['DeleteAlarmRulesBeforeUpdate'] = self.delete_alarm_rules_before_update

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmConfig') is not None:
            self.alarm_config_shrink = m.get('AlarmConfig')

        if m.get('DeleteAlarmRulesBeforeUpdate') is not None:
            self.delete_alarm_rules_before_update = m.get('DeleteAlarmRulesBeforeUpdate')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')

        return self

