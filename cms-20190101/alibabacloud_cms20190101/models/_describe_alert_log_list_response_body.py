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
        # The list of alert history entries.
        self.alert_log_list = alert_log_list
        # The HTTP status code.
        # 
        # > The status code 200 indicates that the call was successful.
        self.code = code
        # The error message.
        self.message = message
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call was successful. Valid values:
        # 
        # - true: The call was successful.
        # 
        # - false: The call failed.
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
        # The timestamp when the alert was triggered.
        # 
        # Unit: milliseconds.
        self.alert_time = alert_time
        # The details of the matched alert blacklist.
        self.black_list_detail = black_list_detail
        # The name of the matched alert blacklist.
        self.black_list_name = black_list_name
        # The UUID of the matched alert blacklist.
        self.black_list_uuid = black_list_uuid
        # The list of Wangwang IDs of the alert contact.
        self.contact_aliiwwlist = contact_aliiwwlist
        # The list of DingTalk accounts of the alert contact.
        self.contact_ding_list = contact_ding_list
        # The list of alert contact groups.
        self.contact_groups = contact_groups
        # The list of email addresses of the alert contact.
        self.contact_mail_list = contact_mail_list
        # The list of phone numbers of the alert contact.
        self.contact_on_call_list = contact_on_call_list
        # The list of phone numbers that receive text messages of the alert contact.
        self.contact_smslist = contact_smslist
        # The dimensions of the resource for which the alert is triggered.
        self.dimensions = dimensions
        # The list of webhook URLs of DingTalk chatbots for the alert contact.
        self.dingding_webhook_list = dingding_webhook_list
        # The rule that triggers the alert.
        self.escalation = escalation
        # The name of the event.
        self.event_name = event_name
        # The extended information of the alert.
        self.extended_info = extended_info
        # The ID of the application group.
        self.group_id = group_id
        # The name of the application group.
        self.group_name = group_name
        # The ID of the resource.
        self.instance_id = instance_id
        # The name of the resource.
        self.instance_name = instance_name
        # The alert level and notification methods. Valid values:
        # 
        # <props="china">- P2: phone calls, text messages, emails, and DingTalk chatbots.
        # 
        # <props="china">- P3: text messages, emails, and DingTalk chatbots.
        # 
        # <props="china">- P4: emails and DingTalk chatbots.
        # 
        # <props="china">- OK: no alerts.
        # 
        # <props="intl">- P4: emails and DingTalk chatbots.
        # 
        # <props="intl">- OK: no alerts.
        # 
        # <props="partner">- P4: emails and DingTalk chatbots.
        # 
        # <props="partner">- OK: no alerts.
        self.level = level
        # The change of the alert level. Valid values:
        # - `P4->OK`: The alert level changes from P4 to OK, which indicates that the alert is cleared.
        # - `P4->P4`: indicates a P4-level alert.
        self.level_change = level_change
        # The log ID.
        self.log_id = log_id
        # The alert-related information, which is a JSON string.
        self.message = message
        # The name of the metric.
        self.metric_name = metric_name
        # The namespace of the cloud service.
        self.namespace = namespace
        # The cloud service identifier. Valid values:
        # 
        # - For an Alibaba Cloud service, the value is the abbreviation of the cloud service name. Example: ECS.
        # 
        # - For a non-Alibaba Cloud service, the value is in the format of `acs_Product keyword`. Example: acs_networkmonitor.
        self.product = product
        # The ID of the alert rule.
        self.rule_id = rule_id
        # The name of the alert rule.
        self.rule_name = rule_name
        # The details of the alert pushing result.
        self.send_detail = send_detail
        # The list of alert sending results.
        self.send_result_list = send_result_list
        # The alert status. Valid values:
        # - 0: An alert is triggered or cleared.
        # - 1: The current time is not within the effective period of the alert.
        # - 2: The current time is within the channel silence period.
        # - 3: The host is being restarted.
        # - 4: No alerts are sent.
        # 
        # <props="china">When the alert status is 0, an alert is triggered if Level is set to P2, P3, or P4; the alert is cleared if Level is set to OK.
        # <props="intl">When the alert status is 0, an alert is triggered if Level is set to P4; the alert is cleared if Level is set to OK.
        # <props="partner">When the alert status is 0, an alert is triggered if Level is set to P4; the alert is cleared if Level is set to OK.
        self.send_status = send_status
        # The list of URLs that are called back when the alert is triggered.
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
        # The status code returned for the alert callback.
        self.code = code
        # The information returned for the alert callback.
        self.message = message
        # The URL that is called back when the alert is triggered.
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
        # The channel that sends the alert. Valid values:
        # - MAIL: email.
        # - ALIIM: Wangwang.
        # - SMS: text message.
        # - CALL: phone call.
        # - DING: DingTalk chatbot.
        # - Merged: alert combination.
        self.key = key
        # The notification target that corresponds to the alert channel.
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
        # The list of alert pushing results by alert channel.
        self.channel_result_list = channel_result_list
        # The pushing status of the alert information.
        # 
        # - success: The alert was pushed.
        # 
        # - error code: If a configuration error occurs and the pushing list is empty, an error code is displayed.
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
        # The alert pushing channel. Valid values:
        # 
        # - MAIL: email.
        # 
        # - SMS: text message.
        # 
        # - WEBHOOK: alert callback.
        # 
        # - SLS: Log Service.
        # 
        # - ONCALL: phone call.
        # 
        # - FC: Function Compute.
        # 
        # - MNS: Message Service (MNS).
        self.channel = channel
        # The list of alert information results that CloudMonitor sends to the alert channel.
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
        # The status code.
        # 
        # - If `Channel` is set to `WEBHOOK`, the status code is 200 or 500.
        # 
        # - If `Channel` is set to `MAIL`, `SMS`, `SLS`, `ONCALL`, `FC`, or `MNS`, this parameter is unavailable or empty.
        self.code = code
        # The details of the returned result.
        self.detail = detail
        # The request ID returned by calling another cloud service.
        self.request_id = request_id
        # The result of calling the target.
        # 
        # - true: The call was successful.
        # 
        # - false: The call failed.
        self.success = success
        # The list of channel notifications.
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
        # The name of the extension field.
        self.name = name
        # The value of the extension field.
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
        # The description of the rule that triggers the alert.
        # 
        # > The body of the alert rule. An alert rule is triggered when the monitoring data meets the alert conditions.
        self.expression = expression
        # The alert level and notification methods. Valid values:
        # 
        # <props="china">- P2: phone calls, text messages, emails, and DingTalk chatbots.
        # 
        # <props="china">- P3: text messages, emails, and DingTalk chatbots.
        # 
        # <props="china">- P4: emails and DingTalk chatbots.
        # 
        # <props="china">- OK: no alerts.
        # 
        # <props="intl">- P4: emails and DingTalk chatbots.
        # 
        # <props="intl">- OK: no alerts.
        # 
        # <props="partner">- P4: emails and DingTalk chatbots.
        # 
        # <props="partner">- OK: no alerts.
        self.level = level
        # The number of times that the alert is retried.
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
        # The key of the alerting resource.
        self.key = key
        # The value of the alerting resource.
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

