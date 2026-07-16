# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class ModifyUserAlarmConfigShrinkRequest(DaraModel):
    def __init__(
        self,
        alarm_config: List[main_models.ModifyUserAlarmConfigShrinkRequestAlarmConfig] = None,
        alarm_lang: str = None,
        contact_config_shrink: str = None,
        lang: str = None,
        source_ip: str = None,
        use_default_contact: int = None,
    ):
        # Alert configuration.
        # 
        # This parameter is required.
        self.alarm_config = alarm_config
        # Language for message notifications.
        self.alarm_lang = alarm_lang
        # Contact configuration.
        self.contact_config_shrink = contact_config_shrink
        # Language used for requests and responses.
        self.lang = lang
        # Source IP address of the requester.
        self.source_ip = source_ip
        # Use default contact method.
        self.use_default_contact = use_default_contact

    def validate(self):
        if self.alarm_config:
            for v1 in self.alarm_config:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AlarmConfig'] = []
        if self.alarm_config is not None:
            for k1 in self.alarm_config:
                result['AlarmConfig'].append(k1.to_map() if k1 else None)

        if self.alarm_lang is not None:
            result['AlarmLang'] = self.alarm_lang

        if self.contact_config_shrink is not None:
            result['ContactConfig'] = self.contact_config_shrink

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.use_default_contact is not None:
            result['UseDefaultContact'] = self.use_default_contact

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alarm_config = []
        if m.get('AlarmConfig') is not None:
            for k1 in m.get('AlarmConfig'):
                temp_model = main_models.ModifyUserAlarmConfigShrinkRequestAlarmConfig()
                self.alarm_config.append(temp_model.from_map(k1))

        if m.get('AlarmLang') is not None:
            self.alarm_lang = m.get('AlarmLang')

        if m.get('ContactConfig') is not None:
            self.contact_config_shrink = m.get('ContactConfig')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('UseDefaultContact') is not None:
            self.use_default_contact = m.get('UseDefaultContact')

        return self

class ModifyUserAlarmConfigShrinkRequestAlarmConfig(DaraModel):
    def __init__(
        self,
        alarm_hour: str = None,
        alarm_notify: str = None,
        alarm_period: str = None,
        alarm_type: str = None,
        alarm_value: str = None,
        alarm_week_day: str = None,
    ):
        # Hour for alert notifications.
        self.alarm_hour = alarm_hour
        # Notification method.
        self.alarm_notify = alarm_notify
        # Alert period.
        self.alarm_period = alarm_period
        # Alarm metric.
        self.alarm_type = alarm_type
        # Alert notification message.
        self.alarm_value = alarm_value
        # Day of the week for alert notifications.
        self.alarm_week_day = alarm_week_day

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_hour is not None:
            result['AlarmHour'] = self.alarm_hour

        if self.alarm_notify is not None:
            result['AlarmNotify'] = self.alarm_notify

        if self.alarm_period is not None:
            result['AlarmPeriod'] = self.alarm_period

        if self.alarm_type is not None:
            result['AlarmType'] = self.alarm_type

        if self.alarm_value is not None:
            result['AlarmValue'] = self.alarm_value

        if self.alarm_week_day is not None:
            result['AlarmWeekDay'] = self.alarm_week_day

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmHour') is not None:
            self.alarm_hour = m.get('AlarmHour')

        if m.get('AlarmNotify') is not None:
            self.alarm_notify = m.get('AlarmNotify')

        if m.get('AlarmPeriod') is not None:
            self.alarm_period = m.get('AlarmPeriod')

        if m.get('AlarmType') is not None:
            self.alarm_type = m.get('AlarmType')

        if m.get('AlarmValue') is not None:
            self.alarm_value = m.get('AlarmValue')

        if m.get('AlarmWeekDay') is not None:
            self.alarm_week_day = m.get('AlarmWeekDay')

        return self

