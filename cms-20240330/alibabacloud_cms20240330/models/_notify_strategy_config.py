# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class NotifyStrategyConfig(DaraModel):
    def __init__(
        self,
        custom_template_entries: List[main_models.NotifyStrategyConfigCustomTemplateEntries] = None,
        description: str = None,
        grouping_setting: main_models.NotifyStrategyConfigGroupingSetting = None,
        ignore_restored_notification: bool = None,
        routes: List[main_models.NotifyStrategyConfigRoutes] = None,
    ):
        # The list of custom notification templates.
        self.custom_template_entries = custom_template_entries
        # The description of the notification policy.
        self.description = description
        # The noise reduction settings.
        # 
        # This parameter is required.
        self.grouping_setting = grouping_setting
        # Specifies whether to ignore notifications for recovery events. A value of true indicates that recovery notifications are not sent.
        self.ignore_restored_notification = ignore_restored_notification
        # The list of notification channel routing settings.
        # 
        # This parameter is required.
        self.routes = routes

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
        result['customTemplateEntries'] = []
        if self.custom_template_entries is not None:
            for k1 in self.custom_template_entries:
                result['customTemplateEntries'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['description'] = self.description

        if self.grouping_setting is not None:
            result['groupingSetting'] = self.grouping_setting.to_map()

        if self.ignore_restored_notification is not None:
            result['ignoreRestoredNotification'] = self.ignore_restored_notification

        result['routes'] = []
        if self.routes is not None:
            for k1 in self.routes:
                result['routes'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.custom_template_entries = []
        if m.get('customTemplateEntries') is not None:
            for k1 in m.get('customTemplateEntries'):
                temp_model = main_models.NotifyStrategyConfigCustomTemplateEntries()
                self.custom_template_entries.append(temp_model.from_map(k1))

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('groupingSetting') is not None:
            temp_model = main_models.NotifyStrategyConfigGroupingSetting()
            self.grouping_setting = temp_model.from_map(m.get('groupingSetting'))

        if m.get('ignoreRestoredNotification') is not None:
            self.ignore_restored_notification = m.get('ignoreRestoredNotification')

        self.routes = []
        if m.get('routes') is not None:
            for k1 in m.get('routes'):
                temp_model = main_models.NotifyStrategyConfigRoutes()
                self.routes.append(temp_model.from_map(k1))

        return self

class NotifyStrategyConfigRoutes(DaraModel):
    def __init__(
        self,
        channels: List[main_models.NotifyStrategyConfigRoutesChannels] = None,
        digital_employee_name: str = None,
        effect_time_range: main_models.NotifyStrategyConfigRoutesEffectTimeRange = None,
        enable_rca: bool = None,
        filter_setting: main_models.FilterSetting = None,
    ):
        # The list of notification channels.
        self.channels = channels
        # The digital employee name. Required when enableRca is set to true.
        self.digital_employee_name = digital_employee_name
        # The effective time range.
        self.effect_time_range = effect_time_range
        # Specifies whether to enable Root Cause Analysis (RCA).
        self.enable_rca = enable_rca
        # The route-level event filter conditions.
        self.filter_setting = filter_setting

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.channels = []
        if m.get('channels') is not None:
            for k1 in m.get('channels'):
                temp_model = main_models.NotifyStrategyConfigRoutesChannels()
                self.channels.append(temp_model.from_map(k1))

        if m.get('digitalEmployeeName') is not None:
            self.digital_employee_name = m.get('digitalEmployeeName')

        if m.get('effectTimeRange') is not None:
            temp_model = main_models.NotifyStrategyConfigRoutesEffectTimeRange()
            self.effect_time_range = temp_model.from_map(m.get('effectTimeRange'))

        if m.get('enableRca') is not None:
            self.enable_rca = m.get('enableRca')

        if m.get('filterSetting') is not None:
            temp_model = main_models.FilterSetting()
            self.filter_setting = temp_model.from_map(m.get('filterSetting'))

        return self

class NotifyStrategyConfigRoutesEffectTimeRange(DaraModel):
    def __init__(
        self,
        day_in_week: List[int] = None,
        end_time_in_minute: int = None,
        start_time_in_minute: int = None,
        time_zone: str = None,
    ):
        # The effective days. Valid values: 0 to 6 (0 = Sunday, 6 = Saturday). The value 7 is not supported.
        self.day_in_week = day_in_week
        # The end time of the day in minutes. Valid values: 0 to 1439.
        self.end_time_in_minute = end_time_in_minute
        # The start time of the day in minutes. Valid values: 0 to 1438.
        self.start_time_in_minute = start_time_in_minute
        # The IANA time zone identifier.
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

class NotifyStrategyConfigRoutesChannels(DaraModel):
    def __init__(
        self,
        channel_type: str = None,
        enabled_sub_channels: List[str] = None,
        receivers: List[str] = None,
    ):
        # The channel type. Valid values: DING, WEIXIN, FEISHU, SLACK, TEAMS, WEBHOOK, CONTACT, GROUP, DUTY, and DING_COOL_APP. Lowercase values are not supported. For email, text message, or phone call notifications, use CONTACT with enabledSubChannels.
        # 
        # This parameter is required.
        self.channel_type = channel_type
        # Required only for CONTACT, GROUP, or DUTY. The sub-channel types in uppercase. Valid values: EMAIL, SMS, VOICE, DING, WEIXIN, FEISHU, and WEBHOOK.
        self.enabled_sub_channels = enabled_sub_channels
        # The list of receiver identifiers. At least one receiver is required. Specify a webhook UUID for WEBHOOK, a robot UUID for chatbots, or a contact ID for CONTACT.
        # 
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

class NotifyStrategyConfigGroupingSetting(DaraModel):
    def __init__(
        self,
        grouping_keys: List[str] = None,
        period_min: int = None,
        silence_sec: int = None,
        times: int = None,
    ):
        # The event fields by which events are grouped. Events in the same group are merged into a single notification. An empty array indicates no grouping.
        self.grouping_keys = grouping_keys
        # This parameter does not take effect for this operation. You do not need to set this parameter.
        self.period_min = period_min
        # This parameter does not take effect for this operation. You do not need to set this parameter.
        self.silence_sec = silence_sec
        # This parameter does not take effect for this operation. You do not need to set this parameter.
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

class NotifyStrategyConfigCustomTemplateEntries(DaraModel):
    def __init__(
        self,
        template_uuid: str = None,
    ):
        # The UUID of the notification template.
        self.template_uuid = template_uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.template_uuid is not None:
            result['templateUuid'] = self.template_uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('templateUuid') is not None:
            self.template_uuid = m.get('templateUuid')

        return self

