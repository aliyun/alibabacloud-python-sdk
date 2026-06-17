# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeUserAlarmConfigResponseBody(DaraModel):
    def __init__(
        self,
        alarm_config: List[main_models.DescribeUserAlarmConfigResponseBodyAlarmConfig] = None,
        alarm_lang: str = None,
        contact_config: List[main_models.DescribeUserAlarmConfigResponseBodyContactConfig] = None,
        default_contact: main_models.DescribeUserAlarmConfigResponseBodyDefaultContact = None,
        request_id: str = None,
    ):
        # The alarm configuration.
        self.alarm_config = alarm_config
        # The language of the alarm notifications.
        self.alarm_lang = alarm_lang
        # The contact information.
        self.contact_config = contact_config
        # Information about the default alarm contact.
        self.default_contact = default_contact
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.alarm_config:
            for v1 in self.alarm_config:
                 if v1:
                    v1.validate()
        if self.contact_config:
            for v1 in self.contact_config:
                 if v1:
                    v1.validate()
        if self.default_contact:
            self.default_contact.validate()

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

        result['ContactConfig'] = []
        if self.contact_config is not None:
            for k1 in self.contact_config:
                result['ContactConfig'].append(k1.to_map() if k1 else None)

        if self.default_contact is not None:
            result['DefaultContact'] = self.default_contact.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alarm_config = []
        if m.get('AlarmConfig') is not None:
            for k1 in m.get('AlarmConfig'):
                temp_model = main_models.DescribeUserAlarmConfigResponseBodyAlarmConfig()
                self.alarm_config.append(temp_model.from_map(k1))

        if m.get('AlarmLang') is not None:
            self.alarm_lang = m.get('AlarmLang')

        self.contact_config = []
        if m.get('ContactConfig') is not None:
            for k1 in m.get('ContactConfig'):
                temp_model = main_models.DescribeUserAlarmConfigResponseBodyContactConfig()
                self.contact_config.append(temp_model.from_map(k1))

        if m.get('DefaultContact') is not None:
            temp_model = main_models.DescribeUserAlarmConfigResponseBodyDefaultContact()
            self.default_contact = temp_model.from_map(m.get('DefaultContact'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeUserAlarmConfigResponseBodyDefaultContact(DaraModel):
    def __init__(
        self,
        email: str = None,
        mobile_phone: str = None,
        name: str = None,
        status: str = None,
    ):
        # The email address of the default contact.
        self.email = email
        # The mobile number of the default contact.
        self.mobile_phone = mobile_phone
        # The name of the default contact.
        self.name = name
        # The status. Valid values: **normal** (Normal) and **disable** (Disabled).
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.email is not None:
            result['Email'] = self.email

        if self.mobile_phone is not None:
            result['MobilePhone'] = self.mobile_phone

        if self.name is not None:
            result['Name'] = self.name

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('MobilePhone') is not None:
            self.mobile_phone = m.get('MobilePhone')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeUserAlarmConfigResponseBodyContactConfig(DaraModel):
    def __init__(
        self,
        email: str = None,
        mobile_phone: str = None,
        name: str = None,
        status: int = None,
    ):
        # The email address.
        self.email = email
        # The mobile number.
        self.mobile_phone = mobile_phone
        # The contact name.
        self.name = name
        # The status of the contact. Valid values: **0** (Disabled) and **1** (Enabled).
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.email is not None:
            result['Email'] = self.email

        if self.mobile_phone is not None:
            result['MobilePhone'] = self.mobile_phone

        if self.name is not None:
            result['Name'] = self.name

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('MobilePhone') is not None:
            self.mobile_phone = m.get('MobilePhone')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeUserAlarmConfigResponseBodyAlarmConfig(DaraModel):
    def __init__(
        self,
        alarm_hour: int = None,
        alarm_notify: int = None,
        alarm_period: int = None,
        alarm_type: str = None,
        alarm_value: str = None,
        alarm_week_day: int = None,
    ):
        # The alarm threshold.
        self.alarm_hour = alarm_hour
        # The notification method.
        self.alarm_notify = alarm_notify
        # The alarm period.
        self.alarm_period = alarm_period
        # The alarm type.
        self.alarm_type = alarm_type
        # The value that triggers the alarm.
        self.alarm_value = alarm_value
        # The alarm retry count.
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

