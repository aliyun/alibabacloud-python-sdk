# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class ListTargetsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListTargetsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned response code. Valid values:
        # 
        # *   Success: The request is successful.
        # *   Other codes: The request failed. For a list of error codes, see Error codes.
        self.code = code
        # The returned data.
        self.data = data
        # The returned error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true
        # *   false
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
            temp_model = main_models.ListTargetsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListTargetsResponseBodyData(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        targets: List[main_models.ListTargetsResponseBodyDataTargets] = None,
        total: int = None,
    ):
        # If excess return values exist, this parameter is returned.
        self.next_token = next_token
        # The event targets.
        self.targets = targets
        # The total number of entries.
        self.total = total

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
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['Targets'] = []
        if self.targets is not None:
            for k1 in self.targets:
                result['Targets'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.targets = []
        if m.get('Targets') is not None:
            for k1 in m.get('Targets'):
                temp_model = main_models.ListTargetsResponseBodyDataTargets()
                self.targets.append(temp_model.from_map(k1))

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListTargetsResponseBodyDataTargets(DaraModel):
    def __init__(
        self,
        concurrent_config: main_models.ListTargetsResponseBodyDataTargetsConcurrentConfig = None,
        endpoint: str = None,
        errors_tolerance: str = None,
        event_bus_name: str = None,
        id: str = None,
        param_list: List[main_models.ListTargetsResponseBodyDataTargetsParamList] = None,
        rule_name: str = None,
        type: str = None,
    ):
        # The concurrency configuration.
        self.concurrent_config = concurrent_config
        # The endpoint of the event target.
        self.endpoint = endpoint
        # The fault tolerance policy. Valid values: ALL and NONE. 
        # 
        # - **ALL**: Fault tolerance is allowed. If an error occurs in an event, event processing is not blocked. If the event fails to be sent after the maximum number of retries specified by the retry policy is reached, the event is delivered to the dead-letter queue or discarded based on your configurations. 
        # - **NONE**: Fault tolerance is not allowed. If an error occurs in an event and the event fails to be sent after the maximum number of retries specified by the retry policy is reached, event processing is blocked.
        self.errors_tolerance = errors_tolerance
        # The name of the event bus.
        self.event_bus_name = event_bus_name
        # The ID of the event target.
        self.id = id
        # The parameters that are configured for the event target.
        self.param_list = param_list
        # The name of the event rule.
        self.rule_name = rule_name
        # The type of the event target. For more information, see [Event target parameters](https://help.aliyun.com/document_detail/183698.html).
        self.type = type

    def validate(self):
        if self.concurrent_config:
            self.concurrent_config.validate()
        if self.param_list:
            for v1 in self.param_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.concurrent_config is not None:
            result['ConcurrentConfig'] = self.concurrent_config.to_map()

        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.errors_tolerance is not None:
            result['ErrorsTolerance'] = self.errors_tolerance

        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name

        if self.id is not None:
            result['Id'] = self.id

        result['ParamList'] = []
        if self.param_list is not None:
            for k1 in self.param_list:
                result['ParamList'].append(k1.to_map() if k1 else None)

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConcurrentConfig') is not None:
            temp_model = main_models.ListTargetsResponseBodyDataTargetsConcurrentConfig()
            self.concurrent_config = temp_model.from_map(m.get('ConcurrentConfig'))

        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('ErrorsTolerance') is not None:
            self.errors_tolerance = m.get('ErrorsTolerance')

        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        self.param_list = []
        if m.get('ParamList') is not None:
            for k1 in m.get('ParamList'):
                temp_model = main_models.ListTargetsResponseBodyDataTargetsParamList()
                self.param_list.append(temp_model.from_map(k1))

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListTargetsResponseBodyDataTargetsParamList(DaraModel):
    def __init__(
        self,
        form: str = None,
        resource_key: str = None,
        template: str = None,
        value: str = None,
    ):
        # The format that is used by the event target parameter.
        self.form = form
        # The resource parameter of the event target.
        self.resource_key = resource_key
        # The template that is used by the event target parameter.
        self.template = template
        # The value of the event target parameter.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.resource_key is not None:
            result['ResourceKey'] = self.resource_key

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('ResourceKey') is not None:
            self.resource_key = m.get('ResourceKey')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListTargetsResponseBodyDataTargetsConcurrentConfig(DaraModel):
    def __init__(
        self,
        concurrency: int = None,
    ):
        # The maximum number of concurrent events allowed in the event target.
        self.concurrency = concurrency

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.concurrency is not None:
            result['Concurrency'] = self.concurrency

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Concurrency') is not None:
            self.concurrency = m.get('Concurrency')

        return self

