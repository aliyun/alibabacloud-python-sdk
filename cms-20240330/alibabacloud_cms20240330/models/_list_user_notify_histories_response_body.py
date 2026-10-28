# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class ListUserNotifyHistoriesResponseBody(DaraModel):
    def __init__(
        self,
        history_list: List[main_models.ListUserNotifyHistoriesResponseBodyHistoryList] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total: int = None,
    ):
        # The notification history list.
        self.history_list = history_list
        # The maximum number of entries returned by this request.
        self.max_results = max_results
        # The pagination token for the next page. It is an opaque string generated and encrypted by the server. An empty value indicates that no more data is available.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of notification history entries that meet the query conditions.
        self.total = total

    def validate(self):
        if self.history_list:
            for v1 in self.history_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['historyList'] = []
        if self.history_list is not None:
            for k1 in self.history_list:
                result['historyList'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.history_list = []
        if m.get('historyList') is not None:
            for k1 in m.get('historyList'):
                temp_model = main_models.ListUserNotifyHistoriesResponseBodyHistoryList()
                self.history_list.append(temp_model.from_map(k1))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListUserNotifyHistoriesResponseBodyHistoryList(DaraModel):
    def __init__(
        self,
        channel: str = None,
        contacts: str = None,
        groups: str = None,
        incident_id: str = None,
        job_id: str = None,
        no_channel: bool = None,
        notify_strategy_id: str = None,
        notify_strategy_name: str = None,
        receiver: str = None,
        result: str = None,
        rule_id: str = None,
        rule_name: str = None,
        send_type: str = None,
        severity: str = None,
        status: str = None,
        subscription_id: str = None,
        subscription_name: str = None,
        success: bool = None,
        timestamp: int = None,
        user_id: str = None,
    ):
        # The notification channel. The valid values are the same as those of the `channel` request parameter.
        self.channel = channel
        # The list of contacts. Multiple contacts are separated by commas.
        self.contacts = contacts
        # The list of contact groups. Multiple contact groups are separated by commas.
        self.groups = groups
        # The incident ID.
        self.incident_id = incident_id
        # The notification job ID.
        self.job_id = job_id
        # Indicates whether the notification record has no actual delivery channel. Valid values:
        # - true: The notification record has no actual delivery channel, and the notifyResult is NO_CHANNEL.
        # - false: The notification record has an actual delivery channel.
        self.no_channel = no_channel
        # The notification policy ID.
        self.notify_strategy_id = notify_strategy_id
        # The notification policy name.
        self.notify_strategy_name = notify_strategy_name
        # The recipient address, such as a phone number, email address, or webhook URL, depending on the notification channel.
        self.receiver = receiver
        # The notification delivery result details. This is the raw response content returned by the channel, such as the API response from a DingTalk or Lark bot.
        self.result = result
        # The alert rule ID.
        self.rule_id = rule_id
        # The alert rule name.
        self.rule_name = rule_name
        # The notification delivery type. Valid values:
        # - SUBSCRIBE: subscription notifications
        # - DIRECT: direct event notifications
        # - ITSM: ticket or action notifications
        self.send_type = send_type
        # The alert severity. Valid values:
        # - CRITICAL: critical
        # - ERROR: error
        # - WARNING: warning
        # - INFO: information
        self.severity = severity
        # The incident status. Valid values:
        # - TRIGGERED: triggered
        # - RESOLVED: resolved
        # - ACK: acknowledged
        # - ESCALATED: escalated
        # - MANUAL_RESOLVED: manually resolved
        # - TIMEOUT: automatically resolved due to timeout
        # - RETRIGGERED: retriggered
        # - PARTIAL_RESOLVED: partially resolved
        # - INVALID: invalid
        self.status = status
        # The subscription ID.
        self.subscription_id = subscription_id
        # The subscription name.
        self.subscription_name = subscription_name
        # Indicates whether the notification was delivered successfully. Valid values:
        # - true: The notification was delivered successfully.
        # - false: The notification delivery failed.
        self.success = success
        # The time when the notification record was generated. The value is a UNIX timestamp in seconds.
        self.timestamp = timestamp
        # The Alibaba Cloud account ID to which the notification record belongs.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel is not None:
            result['channel'] = self.channel

        if self.contacts is not None:
            result['contacts'] = self.contacts

        if self.groups is not None:
            result['groups'] = self.groups

        if self.incident_id is not None:
            result['incidentId'] = self.incident_id

        if self.job_id is not None:
            result['jobId'] = self.job_id

        if self.no_channel is not None:
            result['noChannel'] = self.no_channel

        if self.notify_strategy_id is not None:
            result['notifyStrategyId'] = self.notify_strategy_id

        if self.notify_strategy_name is not None:
            result['notifyStrategyName'] = self.notify_strategy_name

        if self.receiver is not None:
            result['receiver'] = self.receiver

        if self.result is not None:
            result['result'] = self.result

        if self.rule_id is not None:
            result['ruleId'] = self.rule_id

        if self.rule_name is not None:
            result['ruleName'] = self.rule_name

        if self.send_type is not None:
            result['sendType'] = self.send_type

        if self.severity is not None:
            result['severity'] = self.severity

        if self.status is not None:
            result['status'] = self.status

        if self.subscription_id is not None:
            result['subscriptionId'] = self.subscription_id

        if self.subscription_name is not None:
            result['subscriptionName'] = self.subscription_name

        if self.success is not None:
            result['success'] = self.success

        if self.timestamp is not None:
            result['timestamp'] = self.timestamp

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channel') is not None:
            self.channel = m.get('channel')

        if m.get('contacts') is not None:
            self.contacts = m.get('contacts')

        if m.get('groups') is not None:
            self.groups = m.get('groups')

        if m.get('incidentId') is not None:
            self.incident_id = m.get('incidentId')

        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')

        if m.get('noChannel') is not None:
            self.no_channel = m.get('noChannel')

        if m.get('notifyStrategyId') is not None:
            self.notify_strategy_id = m.get('notifyStrategyId')

        if m.get('notifyStrategyName') is not None:
            self.notify_strategy_name = m.get('notifyStrategyName')

        if m.get('receiver') is not None:
            self.receiver = m.get('receiver')

        if m.get('result') is not None:
            self.result = m.get('result')

        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')

        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')

        if m.get('sendType') is not None:
            self.send_type = m.get('sendType')

        if m.get('severity') is not None:
            self.severity = m.get('severity')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('subscriptionId') is not None:
            self.subscription_id = m.get('subscriptionId')

        if m.get('subscriptionName') is not None:
            self.subscription_name = m.get('subscriptionName')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

