# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_maas20260318 import models as main_models
from darabonba.model import DaraModel

class ListApiKeysResponseBody(DaraModel):
    def __init__(
        self,
        api_keys: List[main_models.ListApiKeysResponseBodyApiKeys] = None,
        code: str = None,
        http_status_code: int = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # API Key。
        self.api_keys = api_keys
        self.code = code
        self.http_status_code = http_status_code
        self.max_results = max_results
        self.message = message
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.api_keys:
            for v1 in self.api_keys:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['apiKeys'] = []
        if self.api_keys is not None:
            for k1 in self.api_keys:
                result['apiKeys'].append(k1.to_map() if k1 else None)

        if self.code is not None:
            result['code'] = self.code

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.message is not None:
            result['message'] = self.message

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_keys = []
        if m.get('apiKeys') is not None:
            for k1 in m.get('apiKeys'):
                temp_model = main_models.ListApiKeysResponseBodyApiKeys()
                self.api_keys.append(temp_model.from_map(k1))

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListApiKeysResponseBodyApiKeys(DaraModel):
    def __init__(
        self,
        api_key_id: int = None,
        api_key_value: str = None,
        creator: str = None,
        description: str = None,
        gmt_create: int = None,
        is_blocked: int = None,
        workspace_id: str = None,
    ):
        # API Key ID。
        self.api_key_id = api_key_id
        # API Key Value。
        self.api_key_value = api_key_value
        self.creator = creator
        self.description = description
        self.gmt_create = gmt_create
        self.is_blocked = is_blocked
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

        if self.is_blocked is not None:
            result['isBlocked'] = self.is_blocked

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

        if m.get('isBlocked') is not None:
            self.is_blocked = m.get('isBlocked')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

