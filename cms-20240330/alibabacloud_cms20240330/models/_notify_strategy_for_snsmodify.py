# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class NotifyStrategyForSNSModify(DaraModel):
    def __init__(
        self,
        custom_template_entries: List[main_models.NotifyStrategyForSNSModifyCustomTemplateEntries] = None,
        description: str = None,
        enable_incident_management: bool = None,
        grouping_setting: main_models.NotifyStrategyForSNSModifyGroupingSetting = None,
        ignore_restored_notification: bool = None,
        routes: List[main_models.NotifyStrategyForSNSModifyRoutes] = None,
    ):
        self.custom_template_entries = custom_template_entries
        self.description = description
        self.enable_incident_management = enable_incident_management
        # This parameter is required.
        self.grouping_setting = grouping_setting
        self.ignore_restored_notification = ignore_restored_notification
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

        if self.enable_incident_management is not None:
            result['enableIncidentManagement'] = self.enable_incident_management

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
                temp_model = main_models.NotifyStrategyForSNSModifyCustomTemplateEntries()
                self.custom_template_entries.append(temp_model.from_map(k1))

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('enableIncidentManagement') is not None:
            self.enable_incident_management = m.get('enableIncidentManagement')

        if m.get('groupingSetting') is not None:
            temp_model = main_models.NotifyStrategyForSNSModifyGroupingSetting()
            self.grouping_setting = temp_model.from_map(m.get('groupingSetting'))

        if m.get('ignoreRestoredNotification') is not None:
            self.ignore_restored_notification = m.get('ignoreRestoredNotification')

        self.routes = []
        if m.get('routes') is not None:
            for k1 in m.get('routes'):
                temp_model = main_models.NotifyStrategyForSNSModifyRoutes()
                self.routes.append(temp_model.from_map(k1))

        return self

class NotifyStrategyForSNSModifyRoutes(DaraModel):
    def __init__(
        self,
        channels: List[main_models.NotifyStrategyForSNSModifyRoutesChannels] = None,
        digital_employee_name: str = None,
        effect_time_range: main_models.NotifyStrategyForSNSModifyRoutesEffectTimeRange = None,
        enable_rca: bool = None,
        filter_setting: main_models.NotifyStrategyForSNSModifyRoutesFilterSetting = None,
        severities: List[str] = None,
    ):
        self.channels = channels
        self.digital_employee_name = digital_employee_name
        # The effective period settings for notifications. Defines on which days and during which time range the system sends notifications.
        self.effect_time_range = effect_time_range
        self.enable_rca = enable_rca
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
                temp_model = main_models.NotifyStrategyForSNSModifyRoutesChannels()
                self.channels.append(temp_model.from_map(k1))

        if m.get('digitalEmployeeName') is not None:
            self.digital_employee_name = m.get('digitalEmployeeName')

        if m.get('effectTimeRange') is not None:
            temp_model = main_models.NotifyStrategyForSNSModifyRoutesEffectTimeRange()
            self.effect_time_range = temp_model.from_map(m.get('effectTimeRange'))

        if m.get('enableRca') is not None:
            self.enable_rca = m.get('enableRca')

        if m.get('filterSetting') is not None:
            temp_model = main_models.NotifyStrategyForSNSModifyRoutesFilterSetting()
            self.filter_setting = temp_model.from_map(m.get('filterSetting'))

        if m.get('severities') is not None:
            self.severities = m.get('severities')

        return self

class NotifyStrategyForSNSModifyRoutesFilterSetting(DaraModel):
    def __init__(
        self,
        conditions: List[main_models.NotifyStrategyForSNSModifyRoutesFilterSettingConditions] = None,
        expression: str = None,
        relation: str = None,
    ):
        self.conditions = conditions
        self.expression = expression
        self.relation = relation

    def validate(self):
        if self.conditions:
            for v1 in self.conditions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['conditions'] = []
        if self.conditions is not None:
            for k1 in self.conditions:
                result['conditions'].append(k1.to_map() if k1 else None)

        if self.expression is not None:
            result['expression'] = self.expression

        if self.relation is not None:
            result['relation'] = self.relation

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conditions = []
        if m.get('conditions') is not None:
            for k1 in m.get('conditions'):
                temp_model = main_models.NotifyStrategyForSNSModifyRoutesFilterSettingConditions()
                self.conditions.append(temp_model.from_map(k1))

        if m.get('expression') is not None:
            self.expression = m.get('expression')

        if m.get('relation') is not None:
            self.relation = m.get('relation')

        return self

class NotifyStrategyForSNSModifyRoutesFilterSettingConditions(DaraModel):
    def __init__(
        self,
        field: str = None,
        op: str = None,
        value: str = None,
    ):
        self.field = field
        self.op = op
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field is not None:
            result['field'] = self.field

        if self.op is not None:
            result['op'] = self.op

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('field') is not None:
            self.field = m.get('field')

        if m.get('op') is not None:
            self.op = m.get('op')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class NotifyStrategyForSNSModifyRoutesEffectTimeRange(DaraModel):
    def __init__(
        self,
        day_in_week: List[int] = None,
        end_time_in_minute: int = None,
        start_time_in_minute: int = None,
        time_zone: str = None,
    ):
        # The days of the week on which the setting takes effect. Array element values range from 0 to 6 (0 = Sunday, 1 = Monday, 2 = Tuesday, ... 6 = Saturday). Note: The value 7 is not supported. The maximum value is 6. Example for all days: [0,1,2,3,4,5,6]. Example for weekdays only: [1,2,3,4,5].
        self.day_in_week = day_in_week
        # The end time of the day, expressed as the number of minutes from 00:00. Valid values: 0 to 1439 (23 × 60 + 59 = 1439, which represents 23:59).
        self.end_time_in_minute = end_time_in_minute
        # The start time of the day, expressed as the number of minutes from 00:00. Valid values: 0 to 1439 (0 represents 00:00).
        self.start_time_in_minute = start_time_in_minute
        # The IANA time zone identifier, such as Asia/Shanghai or America/Los_Angeles.
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

class NotifyStrategyForSNSModifyRoutesChannels(DaraModel):
    def __init__(
        self,
        channel_type: str = None,
        enabled_sub_channels: List[str] = None,
        receivers: List[str] = None,
    ):
        # The notification channel type. The value must be one of the following uppercase enum values: DING (DingTalk chatbot), WEIXIN (WeCom chatbot), FEISHU (Lark chatbot), SLACK, TEAMS, WEBHOOK (custom webhook), CONTACT (contact, requires enabledSubChannels to specify sub-channels), GROUP (contact group), DUTY (on-call schedule), or DING_COOL_APP (DingTalk Cool App). Note: Lowercase values such as EMAIL or SMS are not supported. To send email, text message, or voice notifications, set channelType to CONTACT and specify EMAIL, SMS, or VOICE in enabledSubChannels.
        # 
        # This parameter is required.
        self.channel_type = channel_type
        # Required only when channelType is CONTACT, GROUP, or DUTY. Valid values: EMAIL (email), SMS (text message), VOICE (voice call), DING (DingTalk work notification), WEIXIN (WeCom message), FEISHU (Lark message), and WEBHOOK. For example, to notify a contact by email and text message, set channelType to CONTACT and enabledSubChannels to ["EMAIL","SMS"]. This field is not required for other channelType values such as WEBHOOK or DING.
        self.enabled_sub_channels = enabled_sub_channels
        # The list of receiver identifiers. For the WEBHOOK type, specify the webhook UUID. For DING, WEIXIN, or FEISHU, specify the chatbot UUID. For CONTACT, specify the contact ID. For GROUP, specify the contact group ID. For DUTY, specify the on-call schedule UUID. At least one element is required.
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

class NotifyStrategyForSNSModifyGroupingSetting(DaraModel):
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

class NotifyStrategyForSNSModifyCustomTemplateEntries(DaraModel):
    def __init__(
        self,
        target_type: str = None,
        template_uuid: str = None,
    ):
        self.target_type = target_type
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

