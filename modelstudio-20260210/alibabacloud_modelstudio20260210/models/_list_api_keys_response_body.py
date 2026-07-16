# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_modelstudio20260210 import models as main_models
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
        # The list of API keys.
        self.api_keys = api_keys
        # The response status code.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The number of entries per page.
        self.max_results = max_results
        # The response message.
        self.message = message
        # The token used to retrieve more results. This parameter is not required for the first query. For subsequent queries, use the token obtained from the previous response.
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        # Indicates whether the API call was successful. Valid values:
        # 
        # - true: Successful.
        # - false: Failed.
        self.success = success
        # The total number of records.
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
        auth: main_models.ListApiKeysResponseBodyApiKeysAuth = None,
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
            temp_model = main_models.ListApiKeysResponseBodyApiKeysAuth()
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

class ListApiKeysResponseBodyApiKeysAuth(DaraModel):
    def __init__(
        self,
        access_ips: List[str] = None,
        model_access_scope: main_models.ListApiKeysResponseBodyApiKeysAuthModelAccessScope = None,
        type: str = None,
    ):
        # The IP access whitelist.
        self.access_ips = access_ips
        # The model access scope.
        self.model_access_scope = model_access_scope
        # All: all permissions. Custom: custom permissions.
        self.type = type

    def validate(self):
        if self.model_access_scope:
            self.model_access_scope.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_ips is not None:
            result['accessIps'] = self.access_ips

        if self.model_access_scope is not None:
            result['modelAccessScope'] = self.model_access_scope.to_map()

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessIps') is not None:
            self.access_ips = m.get('accessIps')

        if m.get('modelAccessScope') is not None:
            temp_model = main_models.ListApiKeysResponseBodyApiKeysAuthModelAccessScope()
            self.model_access_scope = temp_model.from_map(m.get('modelAccessScope'))

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class ListApiKeysResponseBodyApiKeysAuthModelAccessScope(DaraModel):
    def __init__(
        self,
        accessible_models: List[str] = None,
        allow_all_models: bool = None,
    ):
        # The list of accessible models.
        self.accessible_models = accessible_models
        # Indicates whether access to all models with inference permissions in the workspace is allowed.
        self.allow_all_models = allow_all_models

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accessible_models is not None:
            result['accessibleModels'] = self.accessible_models

        if self.allow_all_models is not None:
            result['allowAllModels'] = self.allow_all_models

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessibleModels') is not None:
            self.accessible_models = m.get('accessibleModels')

        if m.get('allowAllModels') is not None:
            self.allow_all_models = m.get('allowAllModels')

        return self

