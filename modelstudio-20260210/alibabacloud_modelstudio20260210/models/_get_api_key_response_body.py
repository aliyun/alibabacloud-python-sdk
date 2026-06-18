# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_modelstudio20260210 import models as main_models
from darabonba.model import DaraModel

class GetApiKeyResponseBody(DaraModel):
    def __init__(
        self,
        api_key: main_models.GetApiKeyResponseBodyApiKey = None,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The API key information.
        self.api_key = api_key
        # The response status code.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The response message.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # - true: The request was successful.
        # - false: The request failed.
        self.success = success

    def validate(self):
        if self.api_key:
            self.api_key.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['apiKey'] = self.api_key.to_map()

        if self.code is not None:
            result['code'] = self.code

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
        if m.get('apiKey') is not None:
            temp_model = main_models.GetApiKeyResponseBodyApiKey()
            self.api_key = temp_model.from_map(m.get('apiKey'))

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class GetApiKeyResponseBodyApiKey(DaraModel):
    def __init__(
        self,
        api_key_id: int = None,
        api_key_value: str = None,
        auth: main_models.GetApiKeyResponseBodyApiKeyAuth = None,
        created_by: str = None,
        description: str = None,
        disabled: int = None,
        gmt_create: int = None,
        workspace_id: str = None,
    ):
        # API Key ID。
        self.api_key_id = api_key_id
        # The value of the API key.
        self.api_key_value = api_key_value
        # The permission settings.
        self.auth = auth
        # The creator.
        self.created_by = created_by
        # The description.
        self.description = description
        # Indicates whether the API key is disabled. Valid values:
        # 
        # - **0**: Active.
        # - **1**: Disabled.
        self.disabled = disabled
        # The creation time.
        self.gmt_create = gmt_create
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        if self.auth:
            self.auth.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key_id is not None:
            result['apiKeyId'] = self.api_key_id

        if self.api_key_value is not None:
            result['apiKeyValue'] = self.api_key_value

        if self.auth is not None:
            result['auth'] = self.auth.to_map()

        if self.created_by is not None:
            result['createdBy'] = self.created_by

        if self.description is not None:
            result['description'] = self.description

        if self.disabled is not None:
            result['disabled'] = self.disabled

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiKeyId') is not None:
            self.api_key_id = m.get('apiKeyId')

        if m.get('apiKeyValue') is not None:
            self.api_key_value = m.get('apiKeyValue')

        if m.get('auth') is not None:
            temp_model = main_models.GetApiKeyResponseBodyApiKeyAuth()
            self.auth = temp_model.from_map(m.get('auth'))

        if m.get('createdBy') is not None:
            self.created_by = m.get('createdBy')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('disabled') is not None:
            self.disabled = m.get('disabled')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

class GetApiKeyResponseBodyApiKeyAuth(DaraModel):
    def __init__(
        self,
        access_ips: List[str] = None,
        type: str = None,
    ):
        # The IP address whitelist.
        self.access_ips = access_ips
        # The permission type. Valid values: All: all permissions. Custom: custom permissions.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_ips is not None:
            result['accessIps'] = self.access_ips

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessIps') is not None:
            self.access_ips = m.get('accessIps')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

