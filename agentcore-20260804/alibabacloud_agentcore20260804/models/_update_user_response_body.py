# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class UpdateUserResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.UpdateUserResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
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
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.UpdateUserResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class UpdateUserResponseBodyData(DaraModel):
    def __init__(
        self,
        agent_core_user_id: str = None,
        auth_method: str = None,
        created_at: str = None,
        display_name: str = None,
        email: str = None,
        name: str = None,
        note: str = None,
        region_id: str = None,
        status: str = None,
        updated_at: str = None,
        workspace_id: str = None,
    ):
        self.agent_core_user_id = agent_core_user_id
        self.auth_method = auth_method
        self.created_at = created_at
        self.display_name = display_name
        self.email = email
        self.name = name
        self.note = note
        self.region_id = region_id
        self.status = status
        self.updated_at = updated_at
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_core_user_id is not None:
            result['agentCoreUserId'] = self.agent_core_user_id

        if self.auth_method is not None:
            result['authMethod'] = self.auth_method

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.email is not None:
            result['email'] = self.email

        if self.name is not None:
            result['name'] = self.name

        if self.note is not None:
            result['note'] = self.note

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.status is not None:
            result['status'] = self.status

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentCoreUserId') is not None:
            self.agent_core_user_id = m.get('agentCoreUserId')

        if m.get('authMethod') is not None:
            self.auth_method = m.get('authMethod')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('email') is not None:
            self.email = m.get('email')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('note') is not None:
            self.note = m.get('note')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

