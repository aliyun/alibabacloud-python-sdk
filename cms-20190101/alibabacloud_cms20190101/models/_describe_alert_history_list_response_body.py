# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeAlertHistoryListResponseBody(DaraModel):
    def __init__(
        self,
        alarm_history_list: main_models.DescribeAlertHistoryListResponseBodyAlarmHistoryList = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        total: str = None,
    ):
        # The details of historical alerts.
        self.alarm_history_list = alarm_history_list
        # The status code.
        # 
        # > The status code 200 indicates that the request was successful.
        self.code = code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.alarm_history_list:
            self.alarm_history_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_history_list is not None:
            result['AlarmHistoryList'] = self.alarm_history_list.to_map()

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmHistoryList') is not None:
            temp_model = main_models.DescribeAlertHistoryListResponseBodyAlarmHistoryList()
            self.alarm_history_list = temp_model.from_map(m.get('AlarmHistoryList'))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeAlertHistoryListResponseBodyAlarmHistoryList(DaraModel):
    def __init__(
        self,
        alarm_history: List[main_models.DescribeAlertHistoryListResponseBodyAlarmHistoryListAlarmHistory] = None,
    ):
        self.alarm_history = alarm_history

    def validate(self):
        if self.alarm_history:
            for v1 in self.alarm_history:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AlarmHistory'] = []
        if self.alarm_history is not None:
            for k1 in self.alarm_history:
                result['AlarmHistory'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alarm_history = []
        if m.get('AlarmHistory') is not None:
            for k1 in m.get('AlarmHistory'):
                temp_model = main_models.DescribeAlertHistoryListResponseBodyAlarmHistoryListAlarmHistory()
                self.alarm_history.append(temp_model.from_map(k1))

        return self

class DescribeAlertHistoryListResponseBodyAlarmHistoryListAlarmHistory(DaraModel):
    def __init__(
        self,
        alert_time: int = None,
        contact_aliims: main_models.DescribeAlertHistoryListResponseBodyAlarmHistoryListAlarmHistoryContactALIIMs = None,
        contact_groups: main_models.DescribeAlertHistoryListResponseBodyAlarmHistoryListAlarmHistoryContactGroups = None,
        contact_mails: main_models.DescribeAlertHistoryListResponseBodyAlarmHistoryListAlarmHistoryContactMails = None,
        contact_smses: main_models.DescribeAlertHistoryListResponseBodyAlarmHistoryListAlarmHistoryContactSmses = None,
        contacts: main_models.DescribeAlertHistoryListResponseBodyAlarmHistoryListAlarmHistoryContacts = None,
        dimensions: str = None,
        evaluation_count: int = None,
        expression: str = None,
        group_id: str = None,
        instance_name: str = None,
        last_time: int = None,
        level: str = None,
        metric_name: str = None,
        namespace: str = None,
        rule_id: str = None,
        rule_name: str = None,
        state: str = None,
        status: int = None,
        value: str = None,
        webhooks: str = None,
    ):
        # The timestamp when the alert was triggered. Unit: milliseconds.
        self.alert_time = alert_time
        # The TradeManager IDs of the alert contacts.
        # 
        # > This parameter is valid only on the China site (aliyun.com).
        self.contact_aliims = contact_aliims
        # The alert contact groups.
        self.contact_groups = contact_groups
        # The email addresses of the alert contacts.
        self.contact_mails = contact_mails
        # The mobile numbers of the alert contacts.
        # 
        # > This parameter is valid only on the China site (aliyun.com).
        self.contact_smses = contact_smses
        # The alert contacts that receive alert notifications.
        self.contacts = contacts
        # The resources that are monitored.
        self.dimensions = dimensions
        # The consecutive number of times for which the metric value meets the alert condition before an alert is triggered.
        self.evaluation_count = evaluation_count
        # The expression that is used to trigger alerts.
        self.expression = expression
        # The ID of the application group.
        self.group_id = group_id
        # The instance name.
        self.instance_name = instance_name
        # The duration of the alert. Unit: milliseconds.
        self.last_time = last_time
        # The severity level and notification methods of the alert. Valid values:
        # 
        # *   P4: Alert notifications are sent by using emails and DingTalk chatbots.
        # *   OK: No alert is generated.
        self.level = level
        # The metric name.
        self.metric_name = metric_name
        # The namespace of the cloud service.
        self.namespace = namespace
        # The ID of the alert rule.
        self.rule_id = rule_id
        # The name of the alert rule.
        self.rule_name = rule_name
        # The alert status. Valid values:
        # 
        # *   ALARM: Alerts are triggered.
        # *   OK: No alerts are triggered.
        self.state = state
        # Indicates whether alerts are muted. Valid values:
        # 
        # *   2 (default): Alerts are muted and are not triggered within the mute period, even if the condition specified in the alert rule is met.
        # *   0: Alerts are triggered or cleared.
        # *   1: The alert rule is ineffective.
        self.status = status
        # The threshold of the metric value to trigger or clear an alert.
        self.value = value
        # The callback URL.
        self.webhooks = webhooks

    def validate(self):
        if self.contact_aliims:
            self.contact_aliims.validate()
        if self.contact_groups:
            self.contact_groups.validate()
        if self.contact_mails:
            self.contact_mails.validate()
        if self.contact_smses:
            self.contact_smses.validate()
        if self.contacts:
            self.contacts.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_time is not None:
            result['AlertTime'] = self.alert_time

        if self.contact_aliims is not None:
            result['ContactALIIMs'] = self.contact_aliims.to_map()

        if self.contact_groups is not None:
            result['ContactGroups'] = self.contact_groups.to_map()

        if self.contact_mails is not None:
            result['ContactMails'] = self.contact_mails.to_map()

        if self.contact_smses is not None:
            result['ContactSmses'] = self.contact_smses.to_map()

        if self.contacts is not None:
            result['Contacts'] = self.contacts.to_map()

        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions

        if self.evaluation_count is not None:
            result['EvaluationCount'] = self.evaluation_count

        if self.expression is not None:
            result['Expression'] = self.expression

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.last_time is not None:
            result['LastTime'] = self.last_time

        if self.level is not None:
            result['Level'] = self.level

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.state is not None:
            result['State'] = self.state

        if self.status is not None:
            result['Status'] = self.status

        if self.value is not None:
            result['Value'] = self.value

        if self.webhooks is not None:
            result['Webhooks'] = self.webhooks

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertTime') is not None:
            self.alert_time = m.get('AlertTime')

        if m.get('ContactALIIMs') is not None:
            temp_model = main_models.DescribeAlertHistoryListResponseBodyAlarmHistoryListAlarmHistoryContactALIIMs()
            self.contact_aliims = temp_model.from_map(m.get('ContactALIIMs'))

        if m.get('ContactGroups') is not None:
            temp_model = main_models.DescribeAlertHistoryListResponseBodyAlarmHistoryListAlarmHistoryContactGroups()
            self.contact_groups = temp_model.from_map(m.get('ContactGroups'))

        if m.get('ContactMails') is not None:
            temp_model = main_models.DescribeAlertHistoryListResponseBodyAlarmHistoryListAlarmHistoryContactMails()
            self.contact_mails = temp_model.from_map(m.get('ContactMails'))

        if m.get('ContactSmses') is not None:
            temp_model = main_models.DescribeAlertHistoryListResponseBodyAlarmHistoryListAlarmHistoryContactSmses()
            self.contact_smses = temp_model.from_map(m.get('ContactSmses'))

        if m.get('Contacts') is not None:
            temp_model = main_models.DescribeAlertHistoryListResponseBodyAlarmHistoryListAlarmHistoryContacts()
            self.contacts = temp_model.from_map(m.get('Contacts'))

        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')

        if m.get('EvaluationCount') is not None:
            self.evaluation_count = m.get('EvaluationCount')

        if m.get('Expression') is not None:
            self.expression = m.get('Expression')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('LastTime') is not None:
            self.last_time = m.get('LastTime')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        if m.get('Webhooks') is not None:
            self.webhooks = m.get('Webhooks')

        return self

class DescribeAlertHistoryListResponseBodyAlarmHistoryListAlarmHistoryContacts(DaraModel):
    def __init__(
        self,
        contact: List[str] = None,
    ):
        self.contact = contact

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact is not None:
            result['Contact'] = self.contact

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Contact') is not None:
            self.contact = m.get('Contact')

        return self

class DescribeAlertHistoryListResponseBodyAlarmHistoryListAlarmHistoryContactSmses(DaraModel):
    def __init__(
        self,
        contact_sms: List[str] = None,
    ):
        self.contact_sms = contact_sms

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_sms is not None:
            result['ContactSms'] = self.contact_sms

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactSms') is not None:
            self.contact_sms = m.get('ContactSms')

        return self

class DescribeAlertHistoryListResponseBodyAlarmHistoryListAlarmHistoryContactMails(DaraModel):
    def __init__(
        self,
        contact_mail: List[str] = None,
    ):
        self.contact_mail = contact_mail

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_mail is not None:
            result['ContactMail'] = self.contact_mail

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactMail') is not None:
            self.contact_mail = m.get('ContactMail')

        return self

class DescribeAlertHistoryListResponseBodyAlarmHistoryListAlarmHistoryContactGroups(DaraModel):
    def __init__(
        self,
        contact_group: List[str] = None,
    ):
        self.contact_group = contact_group

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_group is not None:
            result['ContactGroup'] = self.contact_group

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactGroup') is not None:
            self.contact_group = m.get('ContactGroup')

        return self

class DescribeAlertHistoryListResponseBodyAlarmHistoryListAlarmHistoryContactALIIMs(DaraModel):
    def __init__(
        self,
        contact_aliim: List[str] = None,
    ):
        self.contact_aliim = contact_aliim

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_aliim is not None:
            result['ContactALIIM'] = self.contact_aliim

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactALIIM') is not None:
            self.contact_aliim = m.get('ContactALIIM')

        return self

