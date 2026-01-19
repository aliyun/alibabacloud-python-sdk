# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class GetCloudAccountResponseBody(DaraModel):
    def __init__(
        self,
        cloud_account: main_models.GetCloudAccountResponseBodyCloudAccount = None,
        request_id: str = None,
    ):
        self.cloud_account = cloud_account
        self.request_id = request_id

    def validate(self):
        if self.cloud_account:
            self.cloud_account.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cloud_account is not None:
            result['CloudAccount'] = self.cloud_account.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudAccount') is not None:
            temp_model = main_models.GetCloudAccountResponseBodyCloudAccount()
            self.cloud_account = temp_model.from_map(m.get('CloudAccount'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetCloudAccountResponseBodyCloudAccount(DaraModel):
    def __init__(
        self,
        cloud_account_external_id: str = None,
        cloud_account_health: str = None,
        cloud_account_health_check_result: main_models.GetCloudAccountResponseBodyCloudAccountCloudAccountHealthCheckResult = None,
        cloud_account_id: str = None,
        cloud_account_name: str = None,
        cloud_account_provider_config: main_models.GetCloudAccountResponseBodyCloudAccountCloudAccountProviderConfig = None,
        cloud_account_provider_name: str = None,
        cloud_account_vendor_type: str = None,
        create_time: int = None,
        description: str = None,
        instance_id: str = None,
        update_time: int = None,
    ):
        # 云账号外部唯一ID
        self.cloud_account_external_id = cloud_account_external_id
        # 云账号状态
        self.cloud_account_health = cloud_account_health
        self.cloud_account_health_check_result = cloud_account_health_check_result
        # 云账号ID
        self.cloud_account_id = cloud_account_id
        # 云账号名称
        self.cloud_account_name = cloud_account_name
        # 云账号提供商配置
        self.cloud_account_provider_config = cloud_account_provider_config
        # 云账号提供商名称
        self.cloud_account_provider_name = cloud_account_provider_name
        # 云账号类别
        self.cloud_account_vendor_type = cloud_account_vendor_type
        self.create_time = create_time
        # 云账号描述
        self.description = description
        # IDaaS EIAM 实例Id
        self.instance_id = instance_id
        self.update_time = update_time

    def validate(self):
        if self.cloud_account_health_check_result:
            self.cloud_account_health_check_result.validate()
        if self.cloud_account_provider_config:
            self.cloud_account_provider_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cloud_account_external_id is not None:
            result['CloudAccountExternalId'] = self.cloud_account_external_id

        if self.cloud_account_health is not None:
            result['CloudAccountHealth'] = self.cloud_account_health

        if self.cloud_account_health_check_result is not None:
            result['CloudAccountHealthCheckResult'] = self.cloud_account_health_check_result.to_map()

        if self.cloud_account_id is not None:
            result['CloudAccountId'] = self.cloud_account_id

        if self.cloud_account_name is not None:
            result['CloudAccountName'] = self.cloud_account_name

        if self.cloud_account_provider_config is not None:
            result['CloudAccountProviderConfig'] = self.cloud_account_provider_config.to_map()

        if self.cloud_account_provider_name is not None:
            result['CloudAccountProviderName'] = self.cloud_account_provider_name

        if self.cloud_account_vendor_type is not None:
            result['CloudAccountVendorType'] = self.cloud_account_vendor_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudAccountExternalId') is not None:
            self.cloud_account_external_id = m.get('CloudAccountExternalId')

        if m.get('CloudAccountHealth') is not None:
            self.cloud_account_health = m.get('CloudAccountHealth')

        if m.get('CloudAccountHealthCheckResult') is not None:
            temp_model = main_models.GetCloudAccountResponseBodyCloudAccountCloudAccountHealthCheckResult()
            self.cloud_account_health_check_result = temp_model.from_map(m.get('CloudAccountHealthCheckResult'))

        if m.get('CloudAccountId') is not None:
            self.cloud_account_id = m.get('CloudAccountId')

        if m.get('CloudAccountName') is not None:
            self.cloud_account_name = m.get('CloudAccountName')

        if m.get('CloudAccountProviderConfig') is not None:
            temp_model = main_models.GetCloudAccountResponseBodyCloudAccountCloudAccountProviderConfig()
            self.cloud_account_provider_config = temp_model.from_map(m.get('CloudAccountProviderConfig'))

        if m.get('CloudAccountProviderName') is not None:
            self.cloud_account_provider_name = m.get('CloudAccountProviderName')

        if m.get('CloudAccountVendorType') is not None:
            self.cloud_account_vendor_type = m.get('CloudAccountVendorType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class GetCloudAccountResponseBodyCloudAccountCloudAccountProviderConfig(DaraModel):
    def __init__(
        self,
        audience: str = None,
        authorization_server_id: str = None,
        issuer: str = None,
        oidc_jwks_endpoint: str = None,
    ):
        # 受众标识
        self.audience = audience
        # 授权服务ID
        self.authorization_server_id = authorization_server_id
        # Issuer。
        self.issuer = issuer
        # 验签公钥端点
        self.oidc_jwks_endpoint = oidc_jwks_endpoint

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audience is not None:
            result['Audience'] = self.audience

        if self.authorization_server_id is not None:
            result['AuthorizationServerId'] = self.authorization_server_id

        if self.issuer is not None:
            result['Issuer'] = self.issuer

        if self.oidc_jwks_endpoint is not None:
            result['OidcJwksEndpoint'] = self.oidc_jwks_endpoint

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Audience') is not None:
            self.audience = m.get('Audience')

        if m.get('AuthorizationServerId') is not None:
            self.authorization_server_id = m.get('AuthorizationServerId')

        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')

        if m.get('OidcJwksEndpoint') is not None:
            self.oidc_jwks_endpoint = m.get('OidcJwksEndpoint')

        return self

class GetCloudAccountResponseBodyCloudAccountCloudAccountHealthCheckResult(DaraModel):
    def __init__(
        self,
        error_reason: main_models.GetCloudAccountResponseBodyCloudAccountCloudAccountHealthCheckResultErrorReason = None,
        last_check_time: int = None,
        result: str = None,
    ):
        self.error_reason = error_reason
        self.last_check_time = last_check_time
        self.result = result

    def validate(self):
        if self.error_reason:
            self.error_reason.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_reason is not None:
            result['ErrorReason'] = self.error_reason.to_map()

        if self.last_check_time is not None:
            result['LastCheckTime'] = self.last_check_time

        if self.result is not None:
            result['Result'] = self.result

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorReason') is not None:
            temp_model = main_models.GetCloudAccountResponseBodyCloudAccountCloudAccountHealthCheckResultErrorReason()
            self.error_reason = temp_model.from_map(m.get('ErrorReason'))

        if m.get('LastCheckTime') is not None:
            self.last_check_time = m.get('LastCheckTime')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        return self

class GetCloudAccountResponseBodyCloudAccountCloudAccountHealthCheckResultErrorReason(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        return self

