# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class QueryEventTracesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.QueryEventTracesResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. Valid values:
        # 
        # 200: The request was successful.
        # 
        # Other codes: The request failed. For information about error codes, see Error codes.
        self.code = code
        # The name of the event source.
        self.data = data
        # The error message that is returned if the request failed.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values: true and false.
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.QueryEventTracesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryEventTracesResponseBodyData(DaraModel):
    def __init__(
        self,
        action: str = None,
        action_time: int = None,
        endpoint: str = None,
        event_bus_name: str = None,
        event_id: str = None,
        event_source: str = None,
        notify_latency: str = None,
        notify_status: str = None,
        notify_time: int = None,
        received_time: int = None,
        rule_matching_time: str = None,
        rule_name: str = None,
    ):
        # The type of the event trace. Valid values: PutEvent, FilterEvent, and PushEvent. The value PutEvent indicates that the event was delivered. The value FilterEvent indicates that the event was filtered. The value PushEvent indicates that the event was pushed.
        self.action = action
        # The execution time of the event trace.
        self.action_time = action_time
        # The endpoint of the event target. This parameter is returned only if Action is set to PushEvent.
        self.endpoint = endpoint
        # The name of the event bus.
        self.event_bus_name = event_bus_name
        # The event ID.
        self.event_id = event_id
        # The name of the event source.
        self.event_source = event_source
        # The delay period for which the event was delivered to the event target. This parameter is returned only if Action is set to PushEvent.
        self.notify_latency = notify_latency
        # The delivery status.
        self.notify_status = notify_status
        # The time when the event was delivered to the event target. This parameter is returned only if Action is set to PushEvent.
        self.notify_time = notify_time
        # The time when the event was delivered to the event bus. This parameter is returned only if Action is set to PutEvent.
        self.received_time = received_time
        # The time when the event rule was matched. This parameter is returned only if Action is set to FilterEvent.
        self.rule_matching_time = rule_matching_time
        # The name of the event rule.
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.action_time is not None:
            result['ActionTime'] = self.action_time

        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name

        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.event_source is not None:
            result['EventSource'] = self.event_source

        if self.notify_latency is not None:
            result['NotifyLatency'] = self.notify_latency

        if self.notify_status is not None:
            result['NotifyStatus'] = self.notify_status

        if self.notify_time is not None:
            result['NotifyTime'] = self.notify_time

        if self.received_time is not None:
            result['ReceivedTime'] = self.received_time

        if self.rule_matching_time is not None:
            result['RuleMatchingTime'] = self.rule_matching_time

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('ActionTime') is not None:
            self.action_time = m.get('ActionTime')

        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('EventSource') is not None:
            self.event_source = m.get('EventSource')

        if m.get('NotifyLatency') is not None:
            self.notify_latency = m.get('NotifyLatency')

        if m.get('NotifyStatus') is not None:
            self.notify_status = m.get('NotifyStatus')

        if m.get('NotifyTime') is not None:
            self.notify_time = m.get('NotifyTime')

        if m.get('ReceivedTime') is not None:
            self.received_time = m.get('ReceivedTime')

        if m.get('RuleMatchingTime') is not None:
            self.rule_matching_time = m.get('RuleMatchingTime')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        return self

