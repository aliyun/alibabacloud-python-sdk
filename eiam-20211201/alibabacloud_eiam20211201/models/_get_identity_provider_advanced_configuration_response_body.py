# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class GetIdentityProviderAdvancedConfigurationResponseBody(DaraModel):
    def __init__(
        self,
        advanced_configuration: main_models.GetIdentityProviderAdvancedConfigurationResponseBodyAdvancedConfiguration = None,
        request_id: str = None,
    ):
        self.advanced_configuration = advanced_configuration
        self.request_id = request_id

    def validate(self):
        if self.advanced_configuration:
            self.advanced_configuration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.advanced_configuration is not None:
            result['AdvancedConfiguration'] = self.advanced_configuration.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdvancedConfiguration') is not None:
            temp_model = main_models.GetIdentityProviderAdvancedConfigurationResponseBodyAdvancedConfiguration()
            self.advanced_configuration = temp_model.from_map(m.get('AdvancedConfiguration'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetIdentityProviderAdvancedConfigurationResponseBodyAdvancedConfiguration(DaraModel):
    def __init__(
        self,
        dingtalk_advanced_config: main_models.GetIdentityProviderAdvancedConfigurationResponseBodyAdvancedConfigurationDingtalkAdvancedConfig = None,
        identity_provider_id: str = None,
        instance_id: str = None,
    ):
        # 钉钉高阶配置
        self.dingtalk_advanced_config = dingtalk_advanced_config
        # IDaaS EIAM 身份提供方ID
        self.identity_provider_id = identity_provider_id
        # IDaaS EIAM 实例Id
        self.instance_id = instance_id

    def validate(self):
        if self.dingtalk_advanced_config:
            self.dingtalk_advanced_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dingtalk_advanced_config is not None:
            result['DingtalkAdvancedConfig'] = self.dingtalk_advanced_config.to_map()

        if self.identity_provider_id is not None:
            result['IdentityProviderId'] = self.identity_provider_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DingtalkAdvancedConfig') is not None:
            temp_model = main_models.GetIdentityProviderAdvancedConfigurationResponseBodyAdvancedConfigurationDingtalkAdvancedConfig()
            self.dingtalk_advanced_config = temp_model.from_map(m.get('DingtalkAdvancedConfig'))

        if m.get('IdentityProviderId') is not None:
            self.identity_provider_id = m.get('IdentityProviderId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

class GetIdentityProviderAdvancedConfigurationResponseBodyAdvancedConfigurationDingtalkAdvancedConfig(DaraModel):
    def __init__(
        self,
        app_key: str = None,
        app_secret: str = None,
    ):
        # IDaaS EIAM 钉钉一方应用的AppKey
        self.app_key = app_key
        # IDaaS EIAM 钉钉一方应用的AppSecret
        self.app_secret = app_secret

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_key is not None:
            result['AppKey'] = self.app_key

        if self.app_secret is not None:
            result['AppSecret'] = self.app_secret

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        if m.get('AppSecret') is not None:
            self.app_secret = m.get('AppSecret')

        return self

