# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class ListRulesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListRulesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code.
        # 
        # *   **Success**: The request was successful.
        # *   **Other codes**: The request failed. For more information about error codes, see Error codes.
        self.code = code
        # The returned data.
        self.data = data
        # The error message that is returned if the request failed.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values: true and false.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

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

        if m.get('Data') is not None:
            temp_model = main_models.ListRulesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListRulesResponseBodyData(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        rules: List[main_models.ListRulesResponseBodyDataRules] = None,
        total: int = None,
    ):
        # If excess return values exist, this parameter is returned.
        self.next_token = next_token
        # The event rules.
        self.rules = rules
        # The total number of entries.
        self.total = total

    def validate(self):
        if self.rules:
            for v1 in self.rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.ListRulesResponseBodyDataRules()
                self.rules.append(temp_model.from_map(k1))

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListRulesResponseBodyDataRules(DaraModel):
    def __init__(
        self,
        created_timestamp: int = None,
        description: str = None,
        detail_map: Dict[str, Any] = None,
        event_bus_name: str = None,
        filter_pattern: str = None,
        rule_arn: str = None,
        rule_name: str = None,
        status: str = None,
        targets: List[main_models.ListRulesResponseBodyDataRulesTargets] = None,
    ):
        # The creation timestamp.
        self.created_timestamp = created_timestamp
        # The rule description.
        self.description = description
        # The details of the event rule.
        self.detail_map = detail_map
        # The name of the event bus.
        self.event_bus_name = event_bus_name
        # The event pattern, in JSON format. Valid values:
        # 
        # *   **stringEqual**: Up to five expressions in the map data structure can be specified in each field.
        # *   **stringExpression**: Up to five expressions in the map data structure can be specified in each field.
        self.filter_pattern = filter_pattern
        # The Alibaba Cloud Resource Name (ARN) of the rule.
        self.rule_arn = rule_arn
        # The name of the event rule.
        self.rule_name = rule_name
        # The status of the event rule. Valid values:
        # 
        # *   **ENABLE** (default)
        # *   **DISABLE**
        self.status = status
        # The event targets.
        self.targets = targets

    def validate(self):
        if self.targets:
            for v1 in self.targets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_timestamp is not None:
            result['CreatedTimestamp'] = self.created_timestamp

        if self.description is not None:
            result['Description'] = self.description

        if self.detail_map is not None:
            result['DetailMap'] = self.detail_map

        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name

        if self.filter_pattern is not None:
            result['FilterPattern'] = self.filter_pattern

        if self.rule_arn is not None:
            result['RuleARN'] = self.rule_arn

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.status is not None:
            result['Status'] = self.status

        result['Targets'] = []
        if self.targets is not None:
            for k1 in self.targets:
                result['Targets'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTimestamp') is not None:
            self.created_timestamp = m.get('CreatedTimestamp')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DetailMap') is not None:
            self.detail_map = m.get('DetailMap')

        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')

        if m.get('FilterPattern') is not None:
            self.filter_pattern = m.get('FilterPattern')

        if m.get('RuleARN') is not None:
            self.rule_arn = m.get('RuleARN')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.targets = []
        if m.get('Targets') is not None:
            for k1 in m.get('Targets'):
                temp_model = main_models.ListRulesResponseBodyDataRulesTargets()
                self.targets.append(temp_model.from_map(k1))

        return self

class ListRulesResponseBodyDataRulesTargets(DaraModel):
    def __init__(
        self,
        endpoint: str = None,
        errors_tolerance: str = None,
        id: str = None,
        push_selector: str = None,
        type: str = None,
    ):
        # The endpoint of the event target.
        self.endpoint = endpoint
        # The fault tolerance policy. Valid values:
        # 
        # *   **ALL**: Fault tolerance is allowed. If an error occurs in an event, event processing is not blocked. If the event fails to be sent after the maximum number of retries specified by the retry policy is reached, the event is delivered to the dead-letter queue or discarded based on your configurations.
        # *   **NONE**: Fault tolerance is prohibited. If an error occurs in an event and the event fails to be sent after the maximum number of retries specified by the retry policy is reached, event processing is blocked.
        self.errors_tolerance = errors_tolerance
        # The ID of the custom event target.
        self.id = id
        # The transformer that is used to push events.
        self.push_selector = push_selector
        # The type of the event target. For more information, see [Event target parameters.](https://www.alibabacloud.com/help/en/eventbridge/latest/event-target-parameters)
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.errors_tolerance is not None:
            result['ErrorsTolerance'] = self.errors_tolerance

        if self.id is not None:
            result['Id'] = self.id

        if self.push_selector is not None:
            result['PushSelector'] = self.push_selector

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('ErrorsTolerance') is not None:
            self.errors_tolerance = m.get('ErrorsTolerance')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('PushSelector') is not None:
            self.push_selector = m.get('PushSelector')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

