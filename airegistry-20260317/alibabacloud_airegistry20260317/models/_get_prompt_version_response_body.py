# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_airegistry20260317 import models as main_models
from darabonba.model import DaraModel

class GetPromptVersionResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetPromptVersionResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetPromptVersionResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetPromptVersionResponseBodyData(DaraModel):
    def __init__(
        self,
        commit_msg: str = None,
        gmt_modified: int = None,
        md_5: str = None,
        prompt_key: str = None,
        src_user: str = None,
        status: str = None,
        template: str = None,
        variables: List[main_models.GetPromptVersionResponseBodyDataVariables] = None,
        version: str = None,
    ):
        self.commit_msg = commit_msg
        self.gmt_modified = gmt_modified
        self.md_5 = md_5
        self.prompt_key = prompt_key
        self.src_user = src_user
        self.status = status
        self.template = template
        self.variables = variables
        self.version = version

    def validate(self):
        if self.variables:
            for v1 in self.variables:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.commit_msg is not None:
            result['CommitMsg'] = self.commit_msg

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.md_5 is not None:
            result['Md5'] = self.md_5

        if self.prompt_key is not None:
            result['PromptKey'] = self.prompt_key

        if self.src_user is not None:
            result['SrcUser'] = self.src_user

        if self.status is not None:
            result['Status'] = self.status

        if self.template is not None:
            result['Template'] = self.template

        result['Variables'] = []
        if self.variables is not None:
            for k1 in self.variables:
                result['Variables'].append(k1.to_map() if k1 else None)

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommitMsg') is not None:
            self.commit_msg = m.get('CommitMsg')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')

        if m.get('PromptKey') is not None:
            self.prompt_key = m.get('PromptKey')

        if m.get('SrcUser') is not None:
            self.src_user = m.get('SrcUser')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        self.variables = []
        if m.get('Variables') is not None:
            for k1 in m.get('Variables'):
                temp_model = main_models.GetPromptVersionResponseBodyDataVariables()
                self.variables.append(temp_model.from_map(k1))

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class GetPromptVersionResponseBodyDataVariables(DaraModel):
    def __init__(
        self,
        default_value: str = None,
        description: str = None,
        name: str = None,
    ):
        self.default_value = default_value
        self.description = description
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

