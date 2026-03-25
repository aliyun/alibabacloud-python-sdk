# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_maas20260318 import models as main_models
from darabonba.model import DaraModel

class CreateApiKeyResponseBody(DaraModel):
    def __init__(
        self,
        api_key: main_models.CreateApiKeyResponseBodyApiKey = None,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # API Key。
        self.api_key = api_key
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
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
            temp_model = main_models.CreateApiKeyResponseBodyApiKey()
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



class CreateApiKeyResponseBodyApiKey(DaraModel):
    def __init__(
        self,
        api_key_id: int = None,
        api_key_value: str = None,
        creator: str = None,
        description: str = None,
        gmt_create: int = None,
        workspace_id: str = None,
    ):
        # API Key ID。
        self.api_key_id = api_key_id
        # API Key Value。
        self.api_key_value = api_key_value
        self.creator = creator
        self.description = description
        self.gmt_create = gmt_create
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key_id is not None:
            result['apiKeyId'] = self.api_key_id

        if self.api_key_value is not None:
            result['apiKeyValue'] = self.api_key_value

        if self.creator is not None:
            result['creator'] = self.creator

        if self.description is not None:
            result['description'] = self.description

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

        if m.get('creator') is not None:
            self.creator = m.get('creator')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

