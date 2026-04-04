# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any, Dict

from alibabacloud_websitebuild20250429 import models as main_models
from darabonba.model import DaraModel

class CreateAppAssistantAgentResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        allow_retry: bool = None,
        app_name: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_args: List[Any] = None,
        module: main_models.CreateAppAssistantAgentResponseBodyModule = None,
        request_id: str = None,
        root_error_code: str = None,
        root_error_msg: str = None,
        synchro: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.allow_retry = allow_retry
        self.app_name = app_name
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_args = error_args
        self.module = module
        # Id of the request
        self.request_id = request_id
        self.root_error_code = root_error_code
        self.root_error_msg = root_error_msg
        self.synchro = synchro

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.allow_retry is not None:
            result['AllowRetry'] = self.allow_retry

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code

        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message

        if self.error_args is not None:
            result['ErrorArgs'] = self.error_args

        if self.module is not None:
            result['Module'] = self.module.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.root_error_code is not None:
            result['RootErrorCode'] = self.root_error_code

        if self.root_error_msg is not None:
            result['RootErrorMsg'] = self.root_error_msg

        if self.synchro is not None:
            result['Synchro'] = self.synchro

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('AllowRetry') is not None:
            self.allow_retry = m.get('AllowRetry')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

        if m.get('ErrorArgs') is not None:
            self.error_args = m.get('ErrorArgs')

        if m.get('Module') is not None:
            temp_model = main_models.CreateAppAssistantAgentResponseBodyModule()
            self.module = temp_model.from_map(m.get('Module'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RootErrorCode') is not None:
            self.root_error_code = m.get('RootErrorCode')

        if m.get('RootErrorMsg') is not None:
            self.root_error_msg = m.get('RootErrorMsg')

        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')

        return self

class CreateAppAssistantAgentResponseBodyModule(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        agent_name: str = None,
        biz_id: str = None,
        credential: main_models.CreateAppAssistantAgentResponseBodyModuleCredential = None,
        embed_config: main_models.CreateAppAssistantAgentResponseBodyModuleEmbedConfig = None,
        extra_params: Dict[str, str] = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        platform_app_id: str = None,
        platform_type: str = None,
        status: str = None,
        user_id: str = None,
    ):
        self.agent_id = agent_id
        self.agent_name = agent_name
        self.biz_id = biz_id
        self.credential = credential
        self.embed_config = embed_config
        self.extra_params = extra_params
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.platform_app_id = platform_app_id
        self.platform_type = platform_type
        self.status = status
        self.user_id = user_id

    def validate(self):
        if self.credential:
            self.credential.validate()
        if self.embed_config:
            self.embed_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.agent_name is not None:
            result['AgentName'] = self.agent_name

        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.credential is not None:
            result['Credential'] = self.credential.to_map()

        if self.embed_config is not None:
            result['EmbedConfig'] = self.embed_config.to_map()

        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.platform_app_id is not None:
            result['PlatformAppId'] = self.platform_app_id

        if self.platform_type is not None:
            result['PlatformType'] = self.platform_type

        if self.status is not None:
            result['Status'] = self.status

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')

        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('Credential') is not None:
            temp_model = main_models.CreateAppAssistantAgentResponseBodyModuleCredential()
            self.credential = temp_model.from_map(m.get('Credential'))

        if m.get('EmbedConfig') is not None:
            temp_model = main_models.CreateAppAssistantAgentResponseBodyModuleEmbedConfig()
            self.embed_config = temp_model.from_map(m.get('EmbedConfig'))

        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('PlatformAppId') is not None:
            self.platform_app_id = m.get('PlatformAppId')

        if m.get('PlatformType') is not None:
            self.platform_type = m.get('PlatformType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class CreateAppAssistantAgentResponseBodyModuleEmbedConfig(DaraModel):
    def __init__(
        self,
        extra: Dict[str, str] = None,
        raw_script: str = None,
    ):
        self.extra = extra
        self.raw_script = raw_script

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extra is not None:
            result['Extra'] = self.extra

        if self.raw_script is not None:
            result['RawScript'] = self.raw_script

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')

        if m.get('RawScript') is not None:
            self.raw_script = m.get('RawScript')

        return self

class CreateAppAssistantAgentResponseBodyModuleCredential(DaraModel):
    def __init__(
        self,
        extra: Dict[str, str] = None,
        username: str = None,
    ):
        self.extra = extra
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extra is not None:
            result['Extra'] = self.extra

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

