# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_amqp_open20191212 import models as main_models
from darabonba.model import DaraModel

class ListDownStreamBindingsResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.ListDownStreamBindingsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code. The status code 200 indicates that the request is successful.
        self.code = code
        # The returned data.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful.
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
            temp_model = main_models.ListDownStreamBindingsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListDownStreamBindingsResponseBodyData(DaraModel):
    def __init__(
        self,
        bindings: List[main_models.ListDownStreamBindingsResponseBodyDataBindings] = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # The bindings.
        self.bindings = bindings
        # The maximum number of entries returned.
        self.max_results = max_results
        # The token that marks the end of the current returned page. If this parameter is empty, all data is retrieved.
        self.next_token = next_token

    def validate(self):
        if self.bindings:
            for v1 in self.bindings:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Bindings'] = []
        if self.bindings is not None:
            for k1 in self.bindings:
                result['Bindings'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bindings = []
        if m.get('Bindings') is not None:
            for k1 in m.get('Bindings'):
                temp_model = main_models.ListDownStreamBindingsResponseBodyDataBindings()
                self.bindings.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

class ListDownStreamBindingsResponseBodyDataBindings(DaraModel):
    def __init__(
        self,
        argument: str = None,
        binding_key: str = None,
        binding_type: str = None,
        destination_name: str = None,
        source_exchange: str = None,
    ):
        # The x-match attribute. Valid values:
        # 
        # *   **all:** A headers exchange routes a message to a queue only if all binding attributes of the queue except for x-match match the headers attributes of the message. This value is the default value.
        # *   **any:** A headers exchange routes a message to a queue if one or more binding attributes of the queue except for x-match match the headers attributes of the message.
        # 
        # This parameter is available only for headers exchanges.
        self.argument = argument
        # The binding key.
        # 
        # *   If the source exchange is not a topic exchange, the binding key must meet the following conventions:
        # 
        #     *   The binding key can contain only letters, digits, hyphens (-), underscores (_), periods (.), forward slashes (/), and at signs (@).
        #     *   The binding key must be 1 to 255 characters in length.
        # 
        # *   If the source exchange is a topic exchange, the binding key must meet the following conventions:
        # 
        #     *   The binding key can contain letters, digits, hyphens (-), underscores (_), periods (.), number signs (#), forward slashes (/), and at signs (@).
        #     *   The binding key cannot start or end with a period (.). If a binding key starts with a number sign (#) or an asterisk (\\*), the number sign (#) or asterisk (\\*) must be followed by a period (.). If the binding key ends with a number sign (#) or an asterisk (\\*), the number sign (#) or asterisk (\\*) must be preceded by a period (.). If a number sign (#) or an asterisk (\\*) is used in the middle of a binding key, the number sign (#) or asterisk (\\*) must be preceded and followed by a period (.).
        #     *   The binding key must be 1 to 255 characters in length.
        self.binding_key = binding_key
        # The type of the object to which the source exchange is bound. Valid values:
        # 
        # *   **QUEUE**
        # *   **EXCHANGE**
        self.binding_type = binding_type
        # The name of the object to which the source exchange is bound.
        self.destination_name = destination_name
        # The name of the source exchange.
        self.source_exchange = source_exchange

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.argument is not None:
            result['Argument'] = self.argument

        if self.binding_key is not None:
            result['BindingKey'] = self.binding_key

        if self.binding_type is not None:
            result['BindingType'] = self.binding_type

        if self.destination_name is not None:
            result['DestinationName'] = self.destination_name

        if self.source_exchange is not None:
            result['SourceExchange'] = self.source_exchange

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Argument') is not None:
            self.argument = m.get('Argument')

        if m.get('BindingKey') is not None:
            self.binding_key = m.get('BindingKey')

        if m.get('BindingType') is not None:
            self.binding_type = m.get('BindingType')

        if m.get('DestinationName') is not None:
            self.destination_name = m.get('DestinationName')

        if m.get('SourceExchange') is not None:
            self.source_exchange = m.get('SourceExchange')

        return self

