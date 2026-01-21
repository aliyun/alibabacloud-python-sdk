# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeAlertLogListResponseBody(DaraModel):
    def __init__(
        self,
        alert_log_list: List[main_models.DescribeAlertLogListResponseBodyAlertLogList] = None,
        code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The queried alert logs.
        self.alert_log_list = alert_log_list
        # The HTTP status code.
        # 
        # > The status code 200 indicates that the request was successful.
        self.code = code
        # The error message.
        self.message = message
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.alert_log_list:
            for v1 in self.alert_log_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AlertLogList'] = []
        if self.alert_log_list is not None:
            for k1 in self.alert_log_list:
                result['AlertLogList'].append(k1.to_map() if k1 else None)

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alert_log_list = []
        if m.get('AlertLogList') is not None:
            for k1 in m.get('AlertLogList'):
                temp_model = main_models.DescribeAlertLogListResponseBodyAlertLogList()
                self.alert_log_list.append(temp_model.from_map(k1))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeAlertLogListResponseBodyAlertLogList(DaraModel):
    def __init__(
        self,
        alert_time: str = None,
        black_list_detail: str = None,
        black_list_name: str = None,
        black_list_uuid: str = None,
        contact_aliiwwlist: List[str] = None,
        contact_ding_list: List[str] = None,
        contact_groups: List[str] = None,
        contact_mail_list: List[str] = None,
        contact_on_call_list: List[str] = None,
        contact_smslist: List[str] = None,
        dimensions: List[main_models.DescribeAlertLogListResponseBodyAlertLogListDimensions] = None,
        dingding_webhook_list: List[str] = None,
        escalation: main_models.DescribeAlertLogListResponseBodyAlertLogListEscalation = None,
        event_name: str = None,
        extended_info: List[main_models.DescribeAlertLogListResponseBodyAlertLogListExtendedInfo] = None,
        group_id: str = None,
        group_name: str = None,
        instance_id: str = None,
        instance_name: str = None,
        level: str = None,
        level_change: str = None,
        log_id: str = None,
        message: str = None,
        metric_name: str = None,
        namespace: str = None,
        product: str = None,
        rule_id: str = None,
        rule_name: str = None,
        send_detail: main_models.DescribeAlertLogListResponseBodyAlertLogListSendDetail = None,
        send_result_list: List[main_models.DescribeAlertLogListResponseBodyAlertLogListSendResultList] = None,
        send_status: str = None,
        webhook_list: List[main_models.DescribeAlertLogListResponseBodyAlertLogListWebhookList] = None,
    ):
        # The timestamp that was generated when the alert was triggered.
        # 
        # Unit: milliseconds.
        self.alert_time = alert_time
        # The details of the blacklist policy.
        self.black_list_detail = black_list_detail
        # The name of the blacklist policy.
        self.black_list_name = black_list_name
        # The ID of the blacklist policy.
        self.black_list_uuid = black_list_uuid
        self.contact_aliiwwlist = contact_aliiwwlist
        self.contact_ding_list = contact_ding_list
        self.contact_groups = contact_groups
        self.contact_mail_list = contact_mail_list
        self.contact_on_call_list = contact_on_call_list
        self.contact_smslist = contact_smslist
        # The dimensions of the resource that triggered alerts.
        self.dimensions = dimensions
        self.dingding_webhook_list = dingding_webhook_list
        # The alert rule based on which the alert is triggered.
        self.escalation = escalation
        # The event name.
        self.event_name = event_name
        # The extended fields.
        self.extended_info = extended_info
        # The ID of the application group.
        self.group_id = group_id
        # The name of the application group.
        self.group_name = group_name
        # The resource ID.
        self.instance_id = instance_id
        # The resource name.
        self.instance_name = instance_name
        # The alert level and the methods that are used to send alert notifications. Valid values:
        # 
        # *   P4: Alert notifications are sent by using emails and DingTalk chatbots.
        # *   OK: No alert is generated.
        self.level = level
        # Indicates whether the alert level was changed. Valid values:
        # 
        # *   `P4->OK`: The alert level was changed from P4 to OK.
        # *   `P4->P4`: The alert level was still P4.
        self.level_change = level_change
        # The log ID.
        self.log_id = log_id
        # The alert information in a JSON string.
        self.message = message
        # The metric name.
        self.metric_name = metric_name
        # The namespace of the cloud service.
        self.namespace = namespace
        # The identifier of the cloud service. Valid values:
        # 
        # *   If the cloud service is provided by Alibaba Cloud, the abbreviation of the service name is returned. Example: ECS.
        # *   If the cloud service is not provided by Alibaba Cloud, a value in the `acs_Service keyword` format is returned. Example: acs_networkmonitor.
        self.product = product
        # The ID of the alert rule.
        self.rule_id = rule_id
        # The name of the alert rule.
        self.rule_name = rule_name
        # The details about the sending results of alert notifications.
        self.send_detail = send_detail
        # The sending results of alert notifications.
        self.send_result_list = send_result_list
        # The status of the alert. Valid values:
        # 
        # *   0: The alert is triggered or cleared.
        # *   1: The alert is ineffective.
        # *   2: The alert is muted.
        # *   3: The host is restarting.
        # *   4: No alert notification is sent.
        # 
        # If the value of the SendStatus parameter is 0, the value P4 of the Level parameter indicates a triggered alert and the value OK indicates a cleared alert.
        self.send_status = send_status
        # The callback URLs.
        self.webhook_list = webhook_list

    def validate(self):
        if self.dimensions:
            for v1 in self.dimensions:
                 if v1:
                    v1.validate()
        if self.escalation:
            self.escalation.validate()
        if self.extended_info:
            for v1 in self.extended_info:
                 if v1:
                    v1.validate()
        if self.send_detail:
            self.send_detail.validate()
        if self.send_result_list:
            for v1 in self.send_result_list:
                 if v1:
                    v1.validate()
        if self.webhook_list:
            for v1 in self.webhook_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_time is not None:
            result['AlertTime'] = self.alert_time

        if self.black_list_detail is not None:
            result['BlackListDetail'] = self.black_list_detail

        if self.black_list_name is not None:
            result['BlackListName'] = self.black_list_name

        if self.black_list_uuid is not None:
            result['BlackListUUID'] = self.black_list_uuid

        if self.contact_aliiwwlist is not None:
            result['ContactALIIWWList'] = self.contact_aliiwwlist

        if self.contact_ding_list is not None:
            result['ContactDingList'] = self.contact_ding_list

        if self.contact_groups is not None:
            result['ContactGroups'] = self.contact_groups

        if self.contact_mail_list is not None:
            result['ContactMailList'] = self.contact_mail_list

        if self.contact_on_call_list is not None:
            result['ContactOnCallList'] = self.contact_on_call_list

        if self.contact_smslist is not None:
            result['ContactSMSList'] = self.contact_smslist

        result['Dimensions'] = []
        if self.dimensions is not None:
            for k1 in self.dimensions:
                result['Dimensions'].append(k1.to_map() if k1 else None)

        if self.dingding_webhook_list is not None:
            result['DingdingWebhookList'] = self.dingding_webhook_list

        if self.escalation is not None:
            result['Escalation'] = self.escalation.to_map()

        if self.event_name is not None:
            result['EventName'] = self.event_name

        result['ExtendedInfo'] = []
        if self.extended_info is not None:
            for k1 in self.extended_info:
                result['ExtendedInfo'].append(k1.to_map() if k1 else None)

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.level is not None:
            result['Level'] = self.level

        if self.level_change is not None:
            result['LevelChange'] = self.level_change

        if self.log_id is not None:
            result['LogId'] = self.log_id

        if self.message is not None:
            result['Message'] = self.message

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.product is not None:
            result['Product'] = self.product

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.send_detail is not None:
            result['SendDetail'] = self.send_detail.to_map()

        result['SendResultList'] = []
        if self.send_result_list is not None:
            for k1 in self.send_result_list:
                result['SendResultList'].append(k1.to_map() if k1 else None)

        if self.send_status is not None:
            result['SendStatus'] = self.send_status

        result['WebhookList'] = []
        if self.webhook_list is not None:
            for k1 in self.webhook_list:
                result['WebhookList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertTime') is not None:
            self.alert_time = m.get('AlertTime')

        if m.get('BlackListDetail') is not None:
            self.black_list_detail = m.get('BlackListDetail')

        if m.get('BlackListName') is not None:
            self.black_list_name = m.get('BlackListName')

        if m.get('BlackListUUID') is not None:
            self.black_list_uuid = m.get('BlackListUUID')

        if m.get('ContactALIIWWList') is not None:
            self.contact_aliiwwlist = m.get('ContactALIIWWList')

        if m.get('ContactDingList') is not None:
            self.contact_ding_list = m.get('ContactDingList')

        if m.get('ContactGroups') is not None:
            self.contact_groups = m.get('ContactGroups')

        if m.get('ContactMailList') is not None:
            self.contact_mail_list = m.get('ContactMailList')

        if m.get('ContactOnCallList') is not None:
            self.contact_on_call_list = m.get('ContactOnCallList')

        if m.get('ContactSMSList') is not None:
            self.contact_smslist = m.get('ContactSMSList')

        self.dimensions = []
        if m.get('Dimensions') is not None:
            for k1 in m.get('Dimensions'):
                temp_model = main_models.DescribeAlertLogListResponseBodyAlertLogListDimensions()
                self.dimensions.append(temp_model.from_map(k1))

        if m.get('DingdingWebhookList') is not None:
            self.dingding_webhook_list = m.get('DingdingWebhookList')

        if m.get('Escalation') is not None:
            temp_model = main_models.DescribeAlertLogListResponseBodyAlertLogListEscalation()
            self.escalation = temp_model.from_map(m.get('Escalation'))

        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')

        self.extended_info = []
        if m.get('ExtendedInfo') is not None:
            for k1 in m.get('ExtendedInfo'):
                temp_model = main_models.DescribeAlertLogListResponseBodyAlertLogListExtendedInfo()
                self.extended_info.append(temp_model.from_map(k1))

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('LevelChange') is not None:
            self.level_change = m.get('LevelChange')

        if m.get('LogId') is not None:
            self.log_id = m.get('LogId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('Product') is not None:
            self.product = m.get('Product')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('SendDetail') is not None:
            temp_model = main_models.DescribeAlertLogListResponseBodyAlertLogListSendDetail()
            self.send_detail = temp_model.from_map(m.get('SendDetail'))

        self.send_result_list = []
        if m.get('SendResultList') is not None:
            for k1 in m.get('SendResultList'):
                temp_model = main_models.DescribeAlertLogListResponseBodyAlertLogListSendResultList()
                self.send_result_list.append(temp_model.from_map(k1))

        if m.get('SendStatus') is not None:
            self.send_status = m.get('SendStatus')

        self.webhook_list = []
        if m.get('WebhookList') is not None:
            for k1 in m.get('WebhookList'):
                temp_model = main_models.DescribeAlertLogListResponseBodyAlertLogListWebhookList()
                self.webhook_list.append(temp_model.from_map(k1))

        return self

class DescribeAlertLogListResponseBodyAlertLogListWebhookList(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        url: str = None,
    ):
        # The status code of the alert callback.
        self.code = code
        # The message returned for the alert callback.
        self.message = message
        # The callback URL.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

class DescribeAlertLogListResponseBodyAlertLogListSendResultList(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: List[str] = None,
    ):
        # The category of the alert notification method. Valid values:
        # 
        # *   MAIL: email
        # *   ALIIM: TradeManager
        # *   SMS: text message
        # *   CALL: phone call
        # *   DING: DingTalk chatbot
        # *   Merged: alert merging
        self.key = key
        # The notification object corresponding to the alert notification method.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeAlertLogListResponseBodyAlertLogListSendDetail(DaraModel):
    def __init__(
        self,
        channel_result_list: List[main_models.DescribeAlertLogListResponseBodyAlertLogListSendDetailChannelResultList] = None,
        result_code: str = None,
    ):
        # The list of sending results that are categorized by notification method.
        self.channel_result_list = channel_result_list
        # Indicates whether the alert notifications are sent.
        # 
        # *   If the alert notifications are sent, the value "success" is returned.
        # *   If the configuration is invalid, no alert notification is sent and an error code is returned.
        self.result_code = result_code

    def validate(self):
        if self.channel_result_list:
            for v1 in self.channel_result_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ChannelResultList'] = []
        if self.channel_result_list is not None:
            for k1 in self.channel_result_list:
                result['ChannelResultList'].append(k1.to_map() if k1 else None)

        if self.result_code is not None:
            result['ResultCode'] = self.result_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.channel_result_list = []
        if m.get('ChannelResultList') is not None:
            for k1 in m.get('ChannelResultList'):
                temp_model = main_models.DescribeAlertLogListResponseBodyAlertLogListSendDetailChannelResultList()
                self.channel_result_list.append(temp_model.from_map(k1))

        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')

        return self

class DescribeAlertLogListResponseBodyAlertLogListSendDetailChannelResultList(DaraModel):
    def __init__(
        self,
        channel: str = None,
        result_list: List[main_models.DescribeAlertLogListResponseBodyAlertLogListSendDetailChannelResultListResultList] = None,
    ):
        # The method that is used to send alert notifications. Valid values:
        # 
        # *   MAIL: email
        # *   SMS: text message
        # *   WEBHOOK: alert callback
        # *   SLS: Simple Log Service
        # *   ONCALL: phone call
        # *   FC: Function Compute
        # *   MNS: Message Service queue
        self.channel = channel
        # The sending results of alert notifications.
        self.result_list = result_list

    def validate(self):
        if self.result_list:
            for v1 in self.result_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel is not None:
            result['Channel'] = self.channel

        result['ResultList'] = []
        if self.result_list is not None:
            for k1 in self.result_list:
                result['ResultList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')

        self.result_list = []
        if m.get('ResultList') is not None:
            for k1 in m.get('ResultList'):
                temp_model = main_models.DescribeAlertLogListResponseBodyAlertLogListSendDetailChannelResultListResultList()
                self.result_list.append(temp_model.from_map(k1))

        return self

class DescribeAlertLogListResponseBodyAlertLogListSendDetailChannelResultListResultList(DaraModel):
    def __init__(
        self,
        code: str = None,
        detail: str = None,
        request_id: str = None,
        success: bool = None,
        notify_target_list: List[str] = None,
    ):
        # The HTTP status code.
        # 
        # *   If the value of the `Channel` parameter is `WEBHOOK`, the status code is 200 or 500.
        # *   If the value of the `Channel` parameter is `MAIL`, `SMS`, `SLS`, `ONCALL`, `FC`, or `MNS`, this parameter is empty or not returned.
        self.code = code
        # The details of the returned results.
        self.detail = detail
        # The request ID returned when CloudMonitor calls another cloud service.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success
        self.notify_target_list = notify_target_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.detail is not None:
            result['Detail'] = self.detail

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.notify_target_list is not None:
            result['notifyTargetList'] = self.notify_target_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Detail') is not None:
            self.detail = m.get('Detail')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('notifyTargetList') is not None:
            self.notify_target_list = m.get('notifyTargetList')

        return self

class DescribeAlertLogListResponseBodyAlertLogListExtendedInfo(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The name of the extended field.
        self.name = name
        # The value of the extended field.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeAlertLogListResponseBodyAlertLogListEscalation(DaraModel):
    def __init__(
        self,
        expression: str = None,
        level: str = None,
        times: int = None,
    ):
        # The description of the alert rule.
        # 
        # >  The content of the alert rule. This parameter indicates the conditions that trigger an alert.
        self.expression = expression
        # The alert level and the methods that are used to send alert notifications. Valid values:
        # 
        # *   P4: Alert notifications are sent by using emails and DingTalk chatbots.
        # *   OK: No alert is generated.
        self.level = level
        # The consecutive number of times for which the metric value meets the alert condition before an alert is triggered.
        self.times = times

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expression is not None:
            result['Expression'] = self.expression

        if self.level is not None:
            result['Level'] = self.level

        if self.times is not None:
            result['Times'] = self.times

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Times') is not None:
            self.times = m.get('Times')

        return self

class DescribeAlertLogListResponseBodyAlertLogListDimensions(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the dimension.
        self.key = key
        # The value of the dimension.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

