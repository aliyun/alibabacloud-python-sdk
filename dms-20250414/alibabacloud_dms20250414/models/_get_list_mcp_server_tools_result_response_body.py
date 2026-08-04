# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms20250414 import models as main_models
from darabonba.model import DaraModel

class GetListMcpServerToolsResultResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetListMcpServerToolsResultResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The MCP Server connectivity detection result. The business status is distinguished by the State field.
        self.data = data
        # The return code. The value success is returned if the request succeeds. An error code is returned if the request fails.
        self.error_code = error_code
        # The error message returned when a system-level request failure occurs.
        self.error_message = error_message
        # The request ID, which is used to locate this API call.
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
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetListMcpServerToolsResultResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetListMcpServerToolsResultResponseBodyData(DaraModel):
    def __init__(
        self,
        accessible: bool = None,
        state: str = None,
        tools: List[main_models.GetListMcpServerToolsResultResponseBodyDataTools] = None,
    ):
        # Indicates whether the MCP Server is accessible. The value is true only when State is success.
        self.accessible = accessible
        # The detection status. Valid values:
        # - pending: The detection is in progress.
        # - success: The detection succeeded.
        # - failed: The detection failed or timed out.
        # 
        # The top-level Success field can be true in all three business states.
        self.state = state
        # The list of detected MCP tools. A non-empty list is returned only when State is success.
        self.tools = tools

    def validate(self):
        if self.tools:
            for v1 in self.tools:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accessible is not None:
            result['Accessible'] = self.accessible

        if self.state is not None:
            result['State'] = self.state

        result['Tools'] = []
        if self.tools is not None:
            for k1 in self.tools:
                result['Tools'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessible') is not None:
            self.accessible = m.get('Accessible')

        if m.get('State') is not None:
            self.state = m.get('State')

        self.tools = []
        if m.get('Tools') is not None:
            for k1 in m.get('Tools'):
                temp_model = main_models.GetListMcpServerToolsResultResponseBodyDataTools()
                self.tools.append(temp_model.from_map(k1))

        return self

class GetListMcpServerToolsResultResponseBodyDataTools(DaraModel):
    def __init__(
        self,
        description: str = None,
        input_schema: str = None,
        name: str = None,
    ):
        # The description of the MCP tool functionality.
        self.description = description
        # The JSON Schema string of the tool input parameters.
        self.input_schema = input_schema
        # The MCP tool name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.input_schema is not None:
            result['InputSchema'] = self.input_schema

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InputSchema') is not None:
            self.input_schema = m.get('InputSchema')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

