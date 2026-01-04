# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class GetApplicationAdvancedConfigResponseBody(DaraModel):
    def __init__(
        self,
        application_advanced_config: main_models.GetApplicationAdvancedConfigResponseBodyApplicationAdvancedConfig = None,
        request_id: str = None,
    ):
        self.application_advanced_config = application_advanced_config
        self.request_id = request_id

    def validate(self):
        if self.application_advanced_config:
            self.application_advanced_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_advanced_config is not None:
            result['ApplicationAdvancedConfig'] = self.application_advanced_config.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationAdvancedConfig') is not None:
            temp_model = main_models.GetApplicationAdvancedConfigResponseBodyApplicationAdvancedConfig()
            self.application_advanced_config = temp_model.from_map(m.get('ApplicationAdvancedConfig'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetApplicationAdvancedConfigResponseBodyApplicationAdvancedConfig(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        instance_id: str = None,
        scim_server_advanced_config: main_models.GetApplicationAdvancedConfigResponseBodyApplicationAdvancedConfigScimServerAdvancedConfig = None,
    ):
        # IDaaS EIAM 应用Id
        self.application_id = application_id
        # IDaaS EIAM 实例Id
        self.instance_id = instance_id
        # Scim Server 高阶配置
        self.scim_server_advanced_config = scim_server_advanced_config

    def validate(self):
        if self.scim_server_advanced_config:
            self.scim_server_advanced_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.scim_server_advanced_config is not None:
            result['ScimServerAdvancedConfig'] = self.scim_server_advanced_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ScimServerAdvancedConfig') is not None:
            temp_model = main_models.GetApplicationAdvancedConfigResponseBodyApplicationAdvancedConfigScimServerAdvancedConfig()
            self.scim_server_advanced_config = temp_model.from_map(m.get('ScimServerAdvancedConfig'))

        return self

class GetApplicationAdvancedConfigResponseBodyApplicationAdvancedConfigScimServerAdvancedConfig(DaraModel):
    def __init__(
        self,
        supported_user_custom_field_ids: List[str] = None,
        user_custom_field_namespace: str = None,
    ):
        # 支持的用户自定义字段ID列表。
        self.supported_user_custom_field_ids = supported_user_custom_field_ids
        # 用户扩展字段的命名空间。
        self.user_custom_field_namespace = user_custom_field_namespace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.supported_user_custom_field_ids is not None:
            result['SupportedUserCustomFieldIds'] = self.supported_user_custom_field_ids

        if self.user_custom_field_namespace is not None:
            result['UserCustomFieldNamespace'] = self.user_custom_field_namespace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SupportedUserCustomFieldIds') is not None:
            self.supported_user_custom_field_ids = m.get('SupportedUserCustomFieldIds')

        if m.get('UserCustomFieldNamespace') is not None:
            self.user_custom_field_namespace = m.get('UserCustomFieldNamespace')

        return self

