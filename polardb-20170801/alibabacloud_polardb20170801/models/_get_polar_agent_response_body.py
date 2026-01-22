# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class GetPolarAgentResponseBody(DaraModel):
    def __init__(
        self,
        content: str = None,
        function_call: List[main_models.GetPolarAgentResponseBodyFunctionCall] = None,
        product: str = None,
        query_id: str = None,
        reasoning_content: str = None,
        request_id: str = None,
        session_id: str = None,
        ui_function_call: List[main_models.GetPolarAgentResponseBodyUiFunctionCall] = None,
    ):
        # Id of the request
        self.content = content
        self.function_call = function_call
        self.product = product
        self.query_id = query_id
        self.reasoning_content = reasoning_content
        self.request_id = request_id
        self.session_id = session_id
        self.ui_function_call = ui_function_call

    def validate(self):
        if self.function_call:
            for v1 in self.function_call:
                 if v1:
                    v1.validate()
        if self.ui_function_call:
            for v1 in self.ui_function_call:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        result['FunctionCall'] = []
        if self.function_call is not None:
            for k1 in self.function_call:
                result['FunctionCall'].append(k1.to_map() if k1 else None)

        if self.product is not None:
            result['Product'] = self.product

        if self.query_id is not None:
            result['QueryId'] = self.query_id

        if self.reasoning_content is not None:
            result['ReasoningContent'] = self.reasoning_content

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        result['UiFunctionCall'] = []
        if self.ui_function_call is not None:
            for k1 in self.ui_function_call:
                result['UiFunctionCall'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        self.function_call = []
        if m.get('FunctionCall') is not None:
            for k1 in m.get('FunctionCall'):
                temp_model = main_models.GetPolarAgentResponseBodyFunctionCall()
                self.function_call.append(temp_model.from_map(k1))

        if m.get('Product') is not None:
            self.product = m.get('Product')

        if m.get('QueryId') is not None:
            self.query_id = m.get('QueryId')

        if m.get('ReasoningContent') is not None:
            self.reasoning_content = m.get('ReasoningContent')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        self.ui_function_call = []
        if m.get('UiFunctionCall') is not None:
            for k1 in m.get('UiFunctionCall'):
                temp_model = main_models.GetPolarAgentResponseBodyUiFunctionCall()
                self.ui_function_call.append(temp_model.from_map(k1))

        return self

class GetPolarAgentResponseBodyUiFunctionCall(DaraModel):
    def __init__(
        self,
        args_text: str = None,
        tool_name: str = None,
    ):
        # xxx
        self.args_text = args_text
        self.tool_name = tool_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.args_text is not None:
            result['ArgsText'] = self.args_text

        if self.tool_name is not None:
            result['ToolName'] = self.tool_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArgsText') is not None:
            self.args_text = m.get('ArgsText')

        if m.get('ToolName') is not None:
            self.tool_name = m.get('ToolName')

        return self

class GetPolarAgentResponseBodyFunctionCall(DaraModel):
    def __init__(
        self,
        arguments: str = None,
        id: str = None,
        name: str = None,
        status: str = None,
    ):
        self.arguments = arguments
        self.id = id
        self.name = name
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arguments is not None:
            result['Arguments'] = self.arguments

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arguments') is not None:
            self.arguments = m.get('Arguments')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

