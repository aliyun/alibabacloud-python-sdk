# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListUserNotifyHistoriesRequest(DaraModel):
    def __init__(
        self,
        batch_id: str = None,
        biz_source: str = None,
        channel: str = None,
        channel_category: str = None,
        from_: int = None,
        group: str = None,
        incident_id: str = None,
        include_no_channel: bool = None,
        is_desc: bool = None,
        max_results: int = None,
        next_token: str = None,
        notify_strategy_id: str = None,
        notify_strategy_name: str = None,
        partition_key: str = None,
        receiver: str = None,
        rule_id: str = None,
        rule_name: str = None,
        send_type: str = None,
        severity: str = None,
        subscription_id: str = None,
        subscription_name: str = None,
        success: bool = None,
        to: int = None,
        workspace: str = None,
    ):
        self.batch_id = batch_id
        self.biz_source = biz_source
        self.channel = channel
        self.channel_category = channel_category
        self.from_ = from_
        self.group = group
        self.incident_id = incident_id
        self.include_no_channel = include_no_channel
        self.is_desc = is_desc
        self.max_results = max_results
        self.next_token = next_token
        self.notify_strategy_id = notify_strategy_id
        self.notify_strategy_name = notify_strategy_name
        self.partition_key = partition_key
        self.receiver = receiver
        self.rule_id = rule_id
        self.rule_name = rule_name
        self.send_type = send_type
        self.severity = severity
        self.subscription_id = subscription_id
        self.subscription_name = subscription_name
        self.success = success
        self.to = to
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_id is not None:
            result['batchId'] = self.batch_id

        if self.biz_source is not None:
            result['bizSource'] = self.biz_source

        if self.channel is not None:
            result['channel'] = self.channel

        if self.channel_category is not None:
            result['channelCategory'] = self.channel_category

        if self.from_ is not None:
            result['from'] = self.from_

        if self.group is not None:
            result['group'] = self.group

        if self.incident_id is not None:
            result['incidentId'] = self.incident_id

        if self.include_no_channel is not None:
            result['includeNoChannel'] = self.include_no_channel

        if self.is_desc is not None:
            result['isDesc'] = self.is_desc

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.notify_strategy_id is not None:
            result['notifyStrategyId'] = self.notify_strategy_id

        if self.notify_strategy_name is not None:
            result['notifyStrategyName'] = self.notify_strategy_name

        if self.partition_key is not None:
            result['partitionKey'] = self.partition_key

        if self.receiver is not None:
            result['receiver'] = self.receiver

        if self.rule_id is not None:
            result['ruleId'] = self.rule_id

        if self.rule_name is not None:
            result['ruleName'] = self.rule_name

        if self.send_type is not None:
            result['sendType'] = self.send_type

        if self.severity is not None:
            result['severity'] = self.severity

        if self.subscription_id is not None:
            result['subscriptionId'] = self.subscription_id

        if self.subscription_name is not None:
            result['subscriptionName'] = self.subscription_name

        if self.success is not None:
            result['success'] = self.success

        if self.to is not None:
            result['to'] = self.to

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('batchId') is not None:
            self.batch_id = m.get('batchId')

        if m.get('bizSource') is not None:
            self.biz_source = m.get('bizSource')

        if m.get('channel') is not None:
            self.channel = m.get('channel')

        if m.get('channelCategory') is not None:
            self.channel_category = m.get('channelCategory')

        if m.get('from') is not None:
            self.from_ = m.get('from')

        if m.get('group') is not None:
            self.group = m.get('group')

        if m.get('incidentId') is not None:
            self.incident_id = m.get('incidentId')

        if m.get('includeNoChannel') is not None:
            self.include_no_channel = m.get('includeNoChannel')

        if m.get('isDesc') is not None:
            self.is_desc = m.get('isDesc')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('notifyStrategyId') is not None:
            self.notify_strategy_id = m.get('notifyStrategyId')

        if m.get('notifyStrategyName') is not None:
            self.notify_strategy_name = m.get('notifyStrategyName')

        if m.get('partitionKey') is not None:
            self.partition_key = m.get('partitionKey')

        if m.get('receiver') is not None:
            self.receiver = m.get('receiver')

        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')

        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')

        if m.get('sendType') is not None:
            self.send_type = m.get('sendType')

        if m.get('severity') is not None:
            self.severity = m.get('severity')

        if m.get('subscriptionId') is not None:
            self.subscription_id = m.get('subscriptionId')

        if m.get('subscriptionName') is not None:
            self.subscription_name = m.get('subscriptionName')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('to') is not None:
            self.to = m.get('to')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

