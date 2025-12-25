# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class NotifyStrategyForModify(DaraModel):
    def __init__(
        self,
        auto_recover_seconds: int = None,
        custom_template_entries: List[main_models.NotifyStrategyForModifyCustomTemplateEntries] = None,
        description: str = None,
        enable_incident_management: bool = None,
        escalation_id: List[str] = None,
        filter_setting: main_models.FilterSetting = None,
        grouping_setting: main_models.NotifyStrategyForModifyGroupingSetting = None,
        ignore_restored_notification: bool = None,
        notify_strategy_name: str = None,
        pushing_setting: main_models.NotifyStrategyForModifyPushingSetting = None,
        repeat_notify_setting: main_models.NotifyStrategyForModifyRepeatNotifySetting = None,
        routes: List[main_models.NotifyStrategyForModifyRoutes] = None,
        workspace_filter_setting: main_models.WorkspaceFilterSetting = None,
    ):
        self.auto_recover_seconds = auto_recover_seconds
        self.custom_template_entries = custom_template_entries
        self.description = description
        self.enable_incident_management = enable_incident_management
        self.escalation_id = escalation_id
        self.filter_setting = filter_setting
        # This parameter is required.
        self.grouping_setting = grouping_setting
        self.ignore_restored_notification = ignore_restored_notification
        # This parameter is required.
        self.notify_strategy_name = notify_strategy_name
        self.pushing_setting = pushing_setting
        self.repeat_notify_setting = repeat_notify_setting
        # This parameter is required.
        self.routes = routes
        self.workspace_filter_setting = workspace_filter_setting

    def validate(self):
        if self.custom_template_entries:
            for v1 in self.custom_template_entries:
                 if v1:
                    v1.validate()
        if self.filter_setting:
            self.filter_setting.validate()
        if self.grouping_setting:
            self.grouping_setting.validate()
        if self.pushing_setting:
            self.pushing_setting.validate()
        if self.repeat_notify_setting:
            self.repeat_notify_setting.validate()
        if self.routes:
            for v1 in self.routes:
                 if v1:
                    v1.validate()
        if self.workspace_filter_setting:
            self.workspace_filter_setting.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_recover_seconds is not None:
            result['autoRecoverSeconds'] = self.auto_recover_seconds

        result['customTemplateEntries'] = []
        if self.custom_template_entries is not None:
            for k1 in self.custom_template_entries:
                result['customTemplateEntries'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['description'] = self.description

        if self.enable_incident_management is not None:
            result['enableIncidentManagement'] = self.enable_incident_management

        if self.escalation_id is not None:
            result['escalationId'] = self.escalation_id

        if self.filter_setting is not None:
            result['filterSetting'] = self.filter_setting.to_map()

        if self.grouping_setting is not None:
            result['groupingSetting'] = self.grouping_setting.to_map()

        if self.ignore_restored_notification is not None:
            result['ignoreRestoredNotification'] = self.ignore_restored_notification

        if self.notify_strategy_name is not None:
            result['notifyStrategyName'] = self.notify_strategy_name

        if self.pushing_setting is not None:
            result['pushingSetting'] = self.pushing_setting.to_map()

        if self.repeat_notify_setting is not None:
            result['repeatNotifySetting'] = self.repeat_notify_setting.to_map()

        result['routes'] = []
        if self.routes is not None:
            for k1 in self.routes:
                result['routes'].append(k1.to_map() if k1 else None)

        if self.workspace_filter_setting is not None:
            result['workspaceFilterSetting'] = self.workspace_filter_setting.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoRecoverSeconds') is not None:
            self.auto_recover_seconds = m.get('autoRecoverSeconds')

        self.custom_template_entries = []
        if m.get('customTemplateEntries') is not None:
            for k1 in m.get('customTemplateEntries'):
                temp_model = main_models.NotifyStrategyForModifyCustomTemplateEntries()
                self.custom_template_entries.append(temp_model.from_map(k1))

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('enableIncidentManagement') is not None:
            self.enable_incident_management = m.get('enableIncidentManagement')

        if m.get('escalationId') is not None:
            self.escalation_id = m.get('escalationId')

        if m.get('filterSetting') is not None:
            temp_model = main_models.FilterSetting()
            self.filter_setting = temp_model.from_map(m.get('filterSetting'))

        if m.get('groupingSetting') is not None:
            temp_model = main_models.NotifyStrategyForModifyGroupingSetting()
            self.grouping_setting = temp_model.from_map(m.get('groupingSetting'))

        if m.get('ignoreRestoredNotification') is not None:
            self.ignore_restored_notification = m.get('ignoreRestoredNotification')

        if m.get('notifyStrategyName') is not None:
            self.notify_strategy_name = m.get('notifyStrategyName')

        if m.get('pushingSetting') is not None:
            temp_model = main_models.NotifyStrategyForModifyPushingSetting()
            self.pushing_setting = temp_model.from_map(m.get('pushingSetting'))

        if m.get('repeatNotifySetting') is not None:
            temp_model = main_models.NotifyStrategyForModifyRepeatNotifySetting()
            self.repeat_notify_setting = temp_model.from_map(m.get('repeatNotifySetting'))

        self.routes = []
        if m.get('routes') is not None:
            for k1 in m.get('routes'):
                temp_model = main_models.NotifyStrategyForModifyRoutes()
                self.routes.append(temp_model.from_map(k1))

        if m.get('workspaceFilterSetting') is not None:
            temp_model = main_models.WorkspaceFilterSetting()
            self.workspace_filter_setting = temp_model.from_map(m.get('workspaceFilterSetting'))

        return self

class NotifyStrategyForModifyRoutes(DaraModel):
    def __init__(
        self,
        channels: List[main_models.NotifyStrategyForModifyRoutesChannels] = None,
        effect_time_range: main_models.NotifyStrategyForModifyRoutesEffectTimeRange = None,
        filter_setting: main_models.FilterSetting = None,
        severities: List[str] = None,
    ):
        self.channels = channels
        self.effect_time_range = effect_time_range
        self.filter_setting = filter_setting
        self.severities = severities

    def validate(self):
        if self.channels:
            for v1 in self.channels:
                 if v1:
                    v1.validate()
        if self.effect_time_range:
            self.effect_time_range.validate()
        if self.filter_setting:
            self.filter_setting.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['channels'] = []
        if self.channels is not None:
            for k1 in self.channels:
                result['channels'].append(k1.to_map() if k1 else None)

        if self.effect_time_range is not None:
            result['effectTimeRange'] = self.effect_time_range.to_map()

        if self.filter_setting is not None:
            result['filterSetting'] = self.filter_setting.to_map()

        if self.severities is not None:
            result['severities'] = self.severities

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.channels = []
        if m.get('channels') is not None:
            for k1 in m.get('channels'):
                temp_model = main_models.NotifyStrategyForModifyRoutesChannels()
                self.channels.append(temp_model.from_map(k1))

        if m.get('effectTimeRange') is not None:
            temp_model = main_models.NotifyStrategyForModifyRoutesEffectTimeRange()
            self.effect_time_range = temp_model.from_map(m.get('effectTimeRange'))

        if m.get('filterSetting') is not None:
            temp_model = main_models.FilterSetting()
            self.filter_setting = temp_model.from_map(m.get('filterSetting'))

        if m.get('severities') is not None:
            self.severities = m.get('severities')

        return self

class NotifyStrategyForModifyRoutesEffectTimeRange(DaraModel):
    def __init__(
        self,
        day_in_week: List[int] = None,
        end_time_in_minute: int = None,
        start_time_in_minute: int = None,
        time_zone: str = None,
    ):
        self.day_in_week = day_in_week
        self.end_time_in_minute = end_time_in_minute
        self.start_time_in_minute = start_time_in_minute
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.day_in_week is not None:
            result['dayInWeek'] = self.day_in_week

        if self.end_time_in_minute is not None:
            result['endTimeInMinute'] = self.end_time_in_minute

        if self.start_time_in_minute is not None:
            result['startTimeInMinute'] = self.start_time_in_minute

        if self.time_zone is not None:
            result['timeZone'] = self.time_zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dayInWeek') is not None:
            self.day_in_week = m.get('dayInWeek')

        if m.get('endTimeInMinute') is not None:
            self.end_time_in_minute = m.get('endTimeInMinute')

        if m.get('startTimeInMinute') is not None:
            self.start_time_in_minute = m.get('startTimeInMinute')

        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')

        return self

class NotifyStrategyForModifyRoutesChannels(DaraModel):
    def __init__(
        self,
        channel_type: str = None,
        enabled_sub_channels: List[str] = None,
        receivers: List[str] = None,
    ):
        # This parameter is required.
        self.channel_type = channel_type
        self.enabled_sub_channels = enabled_sub_channels
        # This parameter is required.
        self.receivers = receivers

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_type is not None:
            result['channelType'] = self.channel_type

        if self.enabled_sub_channels is not None:
            result['enabledSubChannels'] = self.enabled_sub_channels

        if self.receivers is not None:
            result['receivers'] = self.receivers

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channelType') is not None:
            self.channel_type = m.get('channelType')

        if m.get('enabledSubChannels') is not None:
            self.enabled_sub_channels = m.get('enabledSubChannels')

        if m.get('receivers') is not None:
            self.receivers = m.get('receivers')

        return self

class NotifyStrategyForModifyRepeatNotifySetting(DaraModel):
    def __init__(
        self,
        end_incident_state: str = None,
        repeat_interval: int = None,
    ):
        self.end_incident_state = end_incident_state
        self.repeat_interval = repeat_interval

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_incident_state is not None:
            result['endIncidentState'] = self.end_incident_state

        if self.repeat_interval is not None:
            result['repeatInterval'] = self.repeat_interval

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endIncidentState') is not None:
            self.end_incident_state = m.get('endIncidentState')

        if m.get('repeatInterval') is not None:
            self.repeat_interval = m.get('repeatInterval')

        return self

class NotifyStrategyForModifyPushingSetting(DaraModel):
    def __init__(
        self,
        alert_action_ids: List[str] = None,
        restore_action_ids: List[str] = None,
        template_uuid: str = None,
    ):
        self.alert_action_ids = alert_action_ids
        self.restore_action_ids = restore_action_ids
        self.template_uuid = template_uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_action_ids is not None:
            result['alertActionIds'] = self.alert_action_ids

        if self.restore_action_ids is not None:
            result['restoreActionIds'] = self.restore_action_ids

        if self.template_uuid is not None:
            result['templateUuid'] = self.template_uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alertActionIds') is not None:
            self.alert_action_ids = m.get('alertActionIds')

        if m.get('restoreActionIds') is not None:
            self.restore_action_ids = m.get('restoreActionIds')

        if m.get('templateUuid') is not None:
            self.template_uuid = m.get('templateUuid')

        return self

class NotifyStrategyForModifyGroupingSetting(DaraModel):
    def __init__(
        self,
        grouping_keys: List[str] = None,
        period_min: int = None,
        silence_sec: int = None,
        times: int = None,
    ):
        self.grouping_keys = grouping_keys
        self.period_min = period_min
        self.silence_sec = silence_sec
        self.times = times

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.grouping_keys is not None:
            result['groupingKeys'] = self.grouping_keys

        if self.period_min is not None:
            result['periodMin'] = self.period_min

        if self.silence_sec is not None:
            result['silenceSec'] = self.silence_sec

        if self.times is not None:
            result['times'] = self.times

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupingKeys') is not None:
            self.grouping_keys = m.get('groupingKeys')

        if m.get('periodMin') is not None:
            self.period_min = m.get('periodMin')

        if m.get('silenceSec') is not None:
            self.silence_sec = m.get('silenceSec')

        if m.get('times') is not None:
            self.times = m.get('times')

        return self

class NotifyStrategyForModifyCustomTemplateEntries(DaraModel):
    def __init__(
        self,
        target_type: str = None,
        template_uuid: str = None,
    ):
        # This parameter is required.
        self.target_type = target_type
        # This parameter is required.
        self.template_uuid = template_uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.target_type is not None:
            result['targetType'] = self.target_type

        if self.template_uuid is not None:
            result['templateUuid'] = self.template_uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('targetType') is not None:
            self.target_type = m.get('targetType')

        if m.get('templateUuid') is not None:
            self.template_uuid = m.get('templateUuid')

        return self

