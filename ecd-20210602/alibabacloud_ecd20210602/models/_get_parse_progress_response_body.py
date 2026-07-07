# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20210602 import models as main_models
from darabonba.model import DaraModel

class GetParseProgressResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetParseProgressResponseBodyData = None,
        request_id: str = None,
    ):
        # The response data object for parsing the skill package.
        self.data = data
        # The request ID.
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
            temp_model = main_models.GetParseProgressResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self



class GetParseProgressResponseBodyData(DaraModel):
    def __init__(
        self,
        description: str = None,
        error_code: str = None,
        error_message: str = None,
        required_env_vars: List[str] = None,
        requires_api_key: bool = None,
        skill_name: str = None,
        slug: str = None,
        status: str = None,
        task_key: str = None,
        version: str = None,
    ):
        self.description = description
        # The error code returned when an execution exception occurs.
        self.error_code = error_code
        # The error message returned when an execution exception occurs.
        self.error_message = error_message
        self.required_env_vars = required_env_vars
        self.requires_api_key = requires_api_key
        # The name in the SKILL.md file.
        self.skill_name = skill_name
        # The skill slug identifier. This is user-defined and unique within the tenant dimension.
        self.slug = slug
        # The task status. Valid values:
        # - PARSING_METADATA: parsing in progress.
        # - COMPLETED: completed.
        # - FAILED: failed.
        self.status = status
        # The task key for parsing the skill package.
        self.task_key = task_key
        # The version number.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.required_env_vars is not None:
            result['RequiredEnvVars'] = self.required_env_vars

        if self.requires_api_key is not None:
            result['RequiresApiKey'] = self.requires_api_key

        if self.skill_name is not None:
            result['SkillName'] = self.skill_name

        if self.slug is not None:
            result['Slug'] = self.slug

        if self.status is not None:
            result['Status'] = self.status

        if self.task_key is not None:
            result['TaskKey'] = self.task_key

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequiredEnvVars') is not None:
            self.required_env_vars = m.get('RequiredEnvVars')

        if m.get('RequiresApiKey') is not None:
            self.requires_api_key = m.get('RequiresApiKey')

        if m.get('SkillName') is not None:
            self.skill_name = m.get('SkillName')

        if m.get('Slug') is not None:
            self.slug = m.get('Slug')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskKey') is not None:
            self.task_key = m.get('TaskKey')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

