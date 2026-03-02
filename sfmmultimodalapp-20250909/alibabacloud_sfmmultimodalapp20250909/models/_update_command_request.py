# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sfmmultimodalapp20250909 import models as main_models
from darabonba.model import DaraModel

class UpdateCommandRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        domain_code: str = None,
        domain_name: str = None,
        tool_description: str = None,
        tool_examples: List[main_models.UpdateCommandRequestToolExamples] = None,
        tool_id: str = None,
        tool_name: str = None,
        tool_params: List[main_models.UpdateCommandRequestToolParams] = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.domain_code = domain_code
        self.domain_name = domain_name
        # This parameter is required.
        self.tool_description = tool_description
        self.tool_examples = tool_examples
        # This parameter is required.
        self.tool_id = tool_id
        # This parameter is required.
        self.tool_name = tool_name
        self.tool_params = tool_params
        self.workspace_id = workspace_id

    def validate(self):
        if self.tool_examples:
            for v1 in self.tool_examples:
                 if v1:
                    v1.validate()
        if self.tool_params:
            for v1 in self.tool_params:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.domain_code is not None:
            result['DomainCode'] = self.domain_code

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.tool_description is not None:
            result['ToolDescription'] = self.tool_description

        result['ToolExamples'] = []
        if self.tool_examples is not None:
            for k1 in self.tool_examples:
                result['ToolExamples'].append(k1.to_map() if k1 else None)

        if self.tool_id is not None:
            result['ToolId'] = self.tool_id

        if self.tool_name is not None:
            result['ToolName'] = self.tool_name

        result['ToolParams'] = []
        if self.tool_params is not None:
            for k1 in self.tool_params:
                result['ToolParams'].append(k1.to_map() if k1 else None)

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('DomainCode') is not None:
            self.domain_code = m.get('DomainCode')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('ToolDescription') is not None:
            self.tool_description = m.get('ToolDescription')

        self.tool_examples = []
        if m.get('ToolExamples') is not None:
            for k1 in m.get('ToolExamples'):
                temp_model = main_models.UpdateCommandRequestToolExamples()
                self.tool_examples.append(temp_model.from_map(k1))

        if m.get('ToolId') is not None:
            self.tool_id = m.get('ToolId')

        if m.get('ToolName') is not None:
            self.tool_name = m.get('ToolName')

        self.tool_params = []
        if m.get('ToolParams') is not None:
            for k1 in m.get('ToolParams'):
                temp_model = main_models.UpdateCommandRequestToolParams()
                self.tool_params.append(temp_model.from_map(k1))

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class UpdateCommandRequestToolParams(DaraModel):
    def __init__(
        self,
        param_desc: str = None,
        param_example: str = None,
        param_name: str = None,
    ):
        self.param_desc = param_desc
        self.param_example = param_example
        self.param_name = param_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.param_desc is not None:
            result['ParamDesc'] = self.param_desc

        if self.param_example is not None:
            result['ParamExample'] = self.param_example

        if self.param_name is not None:
            result['ParamName'] = self.param_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParamDesc') is not None:
            self.param_desc = m.get('ParamDesc')

        if m.get('ParamExample') is not None:
            self.param_example = m.get('ParamExample')

        if m.get('ParamName') is not None:
            self.param_name = m.get('ParamName')

        return self

class UpdateCommandRequestToolExamples(DaraModel):
    def __init__(
        self,
        query: str = None,
    ):
        self.query = query

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.query is not None:
            result['Query'] = self.query

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Query') is not None:
            self.query = m.get('Query')

        return self

