# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_amqp_open20191212 import models as main_models
from darabonba.model import DaraModel

class ListExchangeUpStreamBindingsResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.ListExchangeUpStreamBindingsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The return code. A value of 200 indicates that the call is successful.
        self.code = code
        # The returned data.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call was successful.
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
            temp_model = main_models.ListExchangeUpStreamBindingsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListExchangeUpStreamBindingsResponseBodyData(DaraModel):
    def __init__(
        self,
        bindings: List[main_models.ListExchangeUpStreamBindingsResponseBodyDataBindings] = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # The bindings.
        self.bindings = bindings
        # The maximum number of results returned.
        self.max_results = max_results
        # The token that indicates the position where the current query ends. An empty value indicates that all data has been read.
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
                temp_model = main_models.ListExchangeUpStreamBindingsResponseBodyDataBindings()
                self.bindings.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

class ListExchangeUpStreamBindingsResponseBodyDataBindings(DaraModel):
    def __init__(
        self,
        argument: str = None,
        binding_key: str = None,
        binding_type: str = None,
        destination_name: str = None,
        source_exchange: str = None,
    ):
        # The x-match property. Valid values:
        # 
        # - **all**: The default value. All key-value pairs in the message header must match.
        # 
        # - **any**: At least one key-value pair in the message header must match.
        # 
        # This parameter is valid only for headers exchanges. It is invalid for other types of exchanges.
        self.argument = argument
        # The binding key.
        # 
        # - If the source exchange is not a topic exchange:
        # 
        #   - The key can contain only letters, digits, hyphens (-), underscores (_), periods (.), forward slashes (/), and at signs (@).
        # 
        #   - The key must be 1 to 255 characters in length.
        # 
        # - If the source exchange is a topic exchange:
        # 
        #   - The key can contain letters, digits, hyphens (-), underscores (_), periods (.), number signs (#), forward slashes (/), and at signs (@).
        # 
        #   - The key cannot start or end with a period (.). A number sign (#) or an asterisk (\\*) must be preceded by a period if it is not at the start of the key. It must be followed by a period if it is not at the end of the key.
        # 
        #   - The key must be 1 to 255 characters in length.
        self.binding_key = binding_key
        # The type of the destination object. Valid values:
        # 
        # - **QUEUE**
        # 
        # - **EXCHANGE**
        self.binding_type = binding_type
        # The destination name.
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

