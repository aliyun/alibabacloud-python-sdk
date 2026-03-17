# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bailiancontrol20240816 import models as main_models
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
        api_key_value: str = None,
        apikey_id: str = None,
        auth_set_model: main_models.GetApiKeyResponseBodyApiKeyAuthSetModel = None,
        blocked: str = None,
        create_time: int = None,
        creator: str = None,
        description: str = None,
        expire_time: int = None,
        ext_data: str = None,
        parent_uid: str = None,
        uid: str = None,
        workspace_id: str = None,
    ):
        self.api_key_value = api_key_value
        self.apikey_id = apikey_id
        self.auth_set_model = auth_set_model
        self.blocked = blocked
        self.create_time = create_time
        self.creator = creator
        self.description = description
        self.expire_time = expire_time
        self.ext_data = ext_data
        self.parent_uid = parent_uid
        self.uid = uid
        self.workspace_id = workspace_id

    def validate(self):
        if self.auth_set_model:
            self.auth_set_model.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key_value is not None:
            result['apiKeyValue'] = self.api_key_value

        if self.apikey_id is not None:
            result['apikeyId'] = self.apikey_id

        if self.auth_set_model is not None:
            result['authSetModel'] = self.auth_set_model.to_map()

        if self.blocked is not None:
            result['blocked'] = self.blocked

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.creator is not None:
            result['creator'] = self.creator

        if self.description is not None:
            result['description'] = self.description

        if self.expire_time is not None:
            result['expireTime'] = self.expire_time

        if self.ext_data is not None:
            result['extData'] = self.ext_data

        if self.parent_uid is not None:
            result['parentUid'] = self.parent_uid

        if self.uid is not None:
            result['uid'] = self.uid

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiKeyValue') is not None:
            self.api_key_value = m.get('apiKeyValue')

        if m.get('apikeyId') is not None:
            self.apikey_id = m.get('apikeyId')

        if m.get('authSetModel') is not None:
            temp_model = main_models.GetApiKeyResponseBodyApiKeyAuthSetModel()
            self.auth_set_model = temp_model.from_map(m.get('authSetModel'))

        if m.get('blocked') is not None:
            self.blocked = m.get('blocked')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('creator') is not None:
            self.creator = m.get('creator')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')

        if m.get('extData') is not None:
            self.ext_data = m.get('extData')

        if m.get('parentUid') is not None:
            self.parent_uid = m.get('parentUid')

        if m.get('uid') is not None:
            self.uid = m.get('uid')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

class GetApiKeyResponseBodyApiKeyAuthSetModel(DaraModel):
    def __init__(
        self,
        access_ips: List[str] = None,
        auth_app_structure: main_models.GetApiKeyResponseBodyApiKeyAuthSetModelAuthAppStructure = None,
        auth_model_structure: main_models.GetApiKeyResponseBodyApiKeyAuthSetModelAuthModelStructure = None,
        auth_set_mode: str = None,
    ):
        self.access_ips = access_ips
        self.auth_app_structure = auth_app_structure
        self.auth_model_structure = auth_model_structure
        self.auth_set_mode = auth_set_mode

    def validate(self):
        if self.auth_app_structure:
            self.auth_app_structure.validate()
        if self.auth_model_structure:
            self.auth_model_structure.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_ips is not None:
            result['accessIps'] = self.access_ips

        if self.auth_app_structure is not None:
            result['authAppStructure'] = self.auth_app_structure.to_map()

        if self.auth_model_structure is not None:
            result['authModelStructure'] = self.auth_model_structure.to_map()

        if self.auth_set_mode is not None:
            result['authSetMode'] = self.auth_set_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessIps') is not None:
            self.access_ips = m.get('accessIps')

        if m.get('authAppStructure') is not None:
            temp_model = main_models.GetApiKeyResponseBodyApiKeyAuthSetModelAuthAppStructure()
            self.auth_app_structure = temp_model.from_map(m.get('authAppStructure'))

        if m.get('authModelStructure') is not None:
            temp_model = main_models.GetApiKeyResponseBodyApiKeyAuthSetModelAuthModelStructure()
            self.auth_model_structure = temp_model.from_map(m.get('authModelStructure'))

        if m.get('authSetMode') is not None:
            self.auth_set_mode = m.get('authSetMode')

        return self

class GetApiKeyResponseBodyApiKeyAuthSetModelAuthModelStructure(DaraModel):
    def __init__(
        self,
        define_models: List[str] = None,
        deployments: List[str] = None,
        is_allow_access_all_models: bool = None,
        models: List[str] = None,
    ):
        self.define_models = define_models
        self.deployments = deployments
        self.is_allow_access_all_models = is_allow_access_all_models
        self.models = models

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.define_models is not None:
            result['defineModels'] = self.define_models

        if self.deployments is not None:
            result['deployments'] = self.deployments

        if self.is_allow_access_all_models is not None:
            result['isAllowAccessAllModels'] = self.is_allow_access_all_models

        if self.models is not None:
            result['models'] = self.models

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('defineModels') is not None:
            self.define_models = m.get('defineModels')

        if m.get('deployments') is not None:
            self.deployments = m.get('deployments')

        if m.get('isAllowAccessAllModels') is not None:
            self.is_allow_access_all_models = m.get('isAllowAccessAllModels')

        if m.get('models') is not None:
            self.models = m.get('models')

        return self



class GetApiKeyResponseBodyApiKeyAuthSetModelAuthAppStructure(DaraModel):
    def __init__(
        self,
        agents: List[str] = None,
        high_code_apps: List[str] = None,
        is_allow_access_all_apps: bool = None,
        workflows: List[str] = None,
    ):
        self.agents = agents
        self.high_code_apps = high_code_apps
        self.is_allow_access_all_apps = is_allow_access_all_apps
        self.workflows = workflows

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agents is not None:
            result['agents'] = self.agents

        if self.high_code_apps is not None:
            result['highCodeApps'] = self.high_code_apps

        if self.is_allow_access_all_apps is not None:
            result['isAllowAccessAllApps'] = self.is_allow_access_all_apps

        if self.workflows is not None:
            result['workflows'] = self.workflows

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agents') is not None:
            self.agents = m.get('agents')

        if m.get('highCodeApps') is not None:
            self.high_code_apps = m.get('highCodeApps')

        if m.get('isAllowAccessAllApps') is not None:
            self.is_allow_access_all_apps = m.get('isAllowAccessAllApps')

        if m.get('workflows') is not None:
            self.workflows = m.get('workflows')

        return self

