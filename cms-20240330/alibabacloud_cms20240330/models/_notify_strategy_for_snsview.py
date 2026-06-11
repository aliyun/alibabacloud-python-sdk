# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class NotifyStrategyForSNSView(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        custom_template_entries: List[main_models.NotifyStrategyForSNSViewCustomTemplateEntries] = None,
        description: str = None,
        enable: bool = None,
        enable_incident_management: bool = None,
        grouping_setting: main_models.NotifyStrategyForSNSViewGroupingSetting = None,
        ignore_restored_notification: bool = None,
        incident_response_plan_id: str = None,
        mode: str = None,
        notify_strategy_id: str = None,
        notify_strategy_name: str = None,
        routes: List[main_models.NotifyStrategyForSNSViewRoutes] = None,
        sync_from_type: str = None,
        update_time: str = None,
        user_id: str = None,
        workspace: str = None,
    ):
        # The creation time of the notification strategy.
        self.create_time = create_time
        # The list of custom templates.
        self.custom_template_entries = custom_template_entries
        # The description of the notification strategy.
        self.description = description
        # Specifies whether to enable the notification strategy. Valid values: true, false.
        self.enable = enable
        # Specifies whether to enable incident management. Valid values: true, false.
        self.enable_incident_management = enable_incident_management
        # The settings for alert grouping.
        self.grouping_setting = grouping_setting
        # Specifies whether to ignore notifications for restored alerts. Valid values: true, false.
        self.ignore_restored_notification = ignore_restored_notification
        # The ID of the incident response plan.
        self.incident_response_plan_id = incident_response_plan_id
        # The mode of the notification strategy.
        self.mode = mode
        # The ID of the notification strategy.
        self.notify_strategy_id = notify_strategy_id
        # The name of the notification strategy.
        self.notify_strategy_name = notify_strategy_name
        # The list of notification routes.
        self.routes = routes
        # The source from which the strategy is synchronized.
        self.sync_from_type = sync_from_type
        # The last update time of the notification strategy.
        self.update_time = update_time
        # The user ID.
        self.user_id = user_id
        # The workspace to which the notification strategy belongs.
        self.workspace = workspace

    def validate(self):
        if self.custom_template_entries:
            for v1 in self.custom_template_entries:
                 if v1:
                    v1.validate()
        if self.grouping_setting:
            self.grouping_setting.validate()
        if self.routes:
            for v1 in self.routes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        result['customTemplateEntries'] = []
        if self.custom_template_entries is not None:
            for k1 in self.custom_template_entries:
                result['customTemplateEntries'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['description'] = self.description

        if self.enable is not None:
            result['enable'] = self.enable

        if self.enable_incident_management is not None:
            result['enableIncidentManagement'] = self.enable_incident_management

        if self.grouping_setting is not None:
            result['groupingSetting'] = self.grouping_setting.to_map()

        if self.ignore_restored_notification is not None:
            result['ignoreRestoredNotification'] = self.ignore_restored_notification

        if self.incident_response_plan_id is not None:
            result['incidentResponsePlanId'] = self.incident_response_plan_id

        if self.mode is not None:
            result['mode'] = self.mode

        if self.notify_strategy_id is not None:
            result['notifyStrategyId'] = self.notify_strategy_id

        if self.notify_strategy_name is not None:
            result['notifyStrategyName'] = self.notify_strategy_name

        result['routes'] = []
        if self.routes is not None:
            for k1 in self.routes:
                result['routes'].append(k1.to_map() if k1 else None)

        if self.sync_from_type is not None:
            result['syncFromType'] = self.sync_from_type

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        if self.user_id is not None:
            result['userId'] = self.user_id

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        self.custom_template_entries = []
        if m.get('customTemplateEntries') is not None:
            for k1 in m.get('customTemplateEntries'):
                temp_model = main_models.NotifyStrategyForSNSViewCustomTemplateEntries()
                self.custom_template_entries.append(temp_model.from_map(k1))

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('enableIncidentManagement') is not None:
            self.enable_incident_management = m.get('enableIncidentManagement')

        if m.get('groupingSetting') is not None:
            temp_model = main_models.NotifyStrategyForSNSViewGroupingSetting()
            self.grouping_setting = temp_model.from_map(m.get('groupingSetting'))

        if m.get('ignoreRestoredNotification') is not None:
            self.ignore_restored_notification = m.get('ignoreRestoredNotification')

        if m.get('incidentResponsePlanId') is not None:
            self.incident_response_plan_id = m.get('incidentResponsePlanId')

        if m.get('mode') is not None:
            self.mode = m.get('mode')

        if m.get('notifyStrategyId') is not None:
            self.notify_strategy_id = m.get('notifyStrategyId')

        if m.get('notifyStrategyName') is not None:
            self.notify_strategy_name = m.get('notifyStrategyName')

        self.routes = []
        if m.get('routes') is not None:
            for k1 in m.get('routes'):
                temp_model = main_models.NotifyStrategyForSNSViewRoutes()
                self.routes.append(temp_model.from_map(k1))

        if m.get('syncFromType') is not None:
            self.sync_from_type = m.get('syncFromType')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

class NotifyStrategyForSNSViewRoutes(DaraModel):
    def __init__(
        self,
        channels: List[main_models.NotifyStrategyForSNSViewRoutesChannels] = None,
        digital_employee_name: str = None,
        effect_time_range: main_models.NotifyStrategyForSNSViewRoutesEffectTimeRange = None,
        enable_rca: bool = None,
        filter_setting: main_models.FilterSetting = None,
        severities: List[str] = None,
    ):
        # The notification channels for the route.
        self.channels = channels
        # The name of the digital employee assigned to this route.
        self.digital_employee_name = digital_employee_name
        # The time range during which the notification route is active.
        self.effect_time_range = effect_time_range
        # Specifies whether to enable root cause analysis (RCA) for alerts that match this route. Valid values: true, false.
        self.enable_rca = enable_rca
        # The filter settings for the route.
        self.filter_setting = filter_setting
        # The alert severities that trigger this route.
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

        if self.digital_employee_name is not None:
            result['digitalEmployeeName'] = self.digital_employee_name

        if self.effect_time_range is not None:
            result['effectTimeRange'] = self.effect_time_range.to_map()

        if self.enable_rca is not None:
            result['enableRca'] = self.enable_rca

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
                temp_model = main_models.NotifyStrategyForSNSViewRoutesChannels()
                self.channels.append(temp_model.from_map(k1))

        if m.get('digitalEmployeeName') is not None:
            self.digital_employee_name = m.get('digitalEmployeeName')

        if m.get('effectTimeRange') is not None:
            temp_model = main_models.NotifyStrategyForSNSViewRoutesEffectTimeRange()
            self.effect_time_range = temp_model.from_map(m.get('effectTimeRange'))

        if m.get('enableRca') is not None:
            self.enable_rca = m.get('enableRca')

        if m.get('filterSetting') is not None:
            temp_model = main_models.FilterSetting()
            self.filter_setting = temp_model.from_map(m.get('filterSetting'))

        if m.get('severities') is not None:
            self.severities = m.get('severities')

        return self

class NotifyStrategyForSNSViewRoutesEffectTimeRange(DaraModel):
    def __init__(
        self,
        day_in_week: List[int] = None,
        end_time_in_minute: int = None,
        start_time_in_minute: int = None,
        time_zone: str = None,
    ):
        # The days of the week when the route is active.
        self.day_in_week = day_in_week
        # The end time of the active period, specified in minutes from 00:00.
        self.end_time_in_minute = end_time_in_minute
        # The start time of the active period, specified in minutes from 00:00.
        self.start_time_in_minute = start_time_in_minute
        # The time zone for the active period. For example, \\"Asia/Shanghai\\".
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

class NotifyStrategyForSNSViewRoutesChannels(DaraModel):
    def __init__(
        self,
        channel_type: str = None,
        enabled_sub_channels: List[str] = None,
        receivers: List[str] = None,
    ):
        # The type of the notification channel, such as \\"sms\\" or \\"email\\".
        self.channel_type = channel_type
        # The enabled sub-channels.
        self.enabled_sub_channels = enabled_sub_channels
        # The list of receivers for the channel.
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

class NotifyStrategyForSNSViewGroupingSetting(DaraModel):
    def __init__(
        self,
        grouping_keys: List[str] = None,
        period_min: int = None,
        silence_sec: int = None,
        times: int = None,
    ):
        # The keys for grouping alerts.
        self.grouping_keys = grouping_keys
        # The time window in minutes for grouping alerts.
        self.period_min = period_min
        # The silence period in seconds after a notification is sent for a group.
        self.silence_sec = silence_sec
        # The number of times to send notifications for a group.
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

class NotifyStrategyForSNSViewCustomTemplateEntries(DaraModel):
    def __init__(
        self,
        target_type: str = None,
        template_uuid: str = None,
    ):
        # The target type for the custom template.
        self.target_type = target_type
        # The unique identifier (UUID) of the template.
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

