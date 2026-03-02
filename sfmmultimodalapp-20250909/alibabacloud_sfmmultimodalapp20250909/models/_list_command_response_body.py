# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sfmmultimodalapp20250909 import models as main_models
from darabonba.model import DaraModel

class ListCommandResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        tool_info_list: List[main_models.ListCommandResponseBodyToolInfoList] = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.tool_info_list = tool_info_list
        self.total_count = total_count

    def validate(self):
        if self.tool_info_list:
            for v1 in self.tool_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ToolInfoList'] = []
        if self.tool_info_list is not None:
            for k1 in self.tool_info_list:
                result['ToolInfoList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.tool_info_list = []
        if m.get('ToolInfoList') is not None:
            for k1 in m.get('ToolInfoList'):
                temp_model = main_models.ListCommandResponseBodyToolInfoList()
                self.tool_info_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListCommandResponseBodyToolInfoList(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        create_user_id: str = None,
        create_user_name: str = None,
        description: str = None,
        domain_code: str = None,
        domain_name: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        modify_user_id: str = None,
        modify_user_name: str = None,
        tool_examples: List[main_models.ListCommandResponseBodyToolInfoListToolExamples] = None,
        tool_id: str = None,
        tool_name: str = None,
        tool_params: List[main_models.ListCommandResponseBodyToolInfoListToolParams] = None,
    ):
        self.app_id = app_id
        self.create_user_id = create_user_id
        self.create_user_name = create_user_name
        self.description = description
        self.domain_code = domain_code
        self.domain_name = domain_name
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.modify_user_id = modify_user_id
        self.modify_user_name = modify_user_name
        self.tool_examples = tool_examples
        self.tool_id = tool_id
        self.tool_name = tool_name
        self.tool_params = tool_params

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

        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id

        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name

        if self.description is not None:
            result['Description'] = self.description

        if self.domain_code is not None:
            result['DomainCode'] = self.domain_code

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.modify_user_id is not None:
            result['ModifyUserId'] = self.modify_user_id

        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')

        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DomainCode') is not None:
            self.domain_code = m.get('DomainCode')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('ModifyUserId') is not None:
            self.modify_user_id = m.get('ModifyUserId')

        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')

        self.tool_examples = []
        if m.get('ToolExamples') is not None:
            for k1 in m.get('ToolExamples'):
                temp_model = main_models.ListCommandResponseBodyToolInfoListToolExamples()
                self.tool_examples.append(temp_model.from_map(k1))

        if m.get('ToolId') is not None:
            self.tool_id = m.get('ToolId')

        if m.get('ToolName') is not None:
            self.tool_name = m.get('ToolName')

        self.tool_params = []
        if m.get('ToolParams') is not None:
            for k1 in m.get('ToolParams'):
                temp_model = main_models.ListCommandResponseBodyToolInfoListToolParams()
                self.tool_params.append(temp_model.from_map(k1))

        return self

class ListCommandResponseBodyToolInfoListToolParams(DaraModel):
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

class ListCommandResponseBodyToolInfoListToolExamples(DaraModel):
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

