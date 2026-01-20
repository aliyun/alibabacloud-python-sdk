# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eiam_developerapi20220225 import models as main_models
from darabonba.model import DaraModel

class ObtainCloudAccountRoleAccessCredentialResponseBody(DaraModel):
    def __init__(
        self,
        cloud_account_id: str = None,
        cloud_account_role_access_credential: main_models.ObtainCloudAccountRoleAccessCredentialResponseBodyCloudAccountRoleAccessCredential = None,
        cloud_account_role_external_id: str = None,
        cloud_account_role_id: str = None,
        cloud_account_role_name: str = None,
        cloud_account_vendor_type: str = None,
    ):
        self.cloud_account_id = cloud_account_id
        self.cloud_account_role_access_credential = cloud_account_role_access_credential
        self.cloud_account_role_external_id = cloud_account_role_external_id
        self.cloud_account_role_id = cloud_account_role_id
        self.cloud_account_role_name = cloud_account_role_name
        self.cloud_account_vendor_type = cloud_account_vendor_type

    def validate(self):
        if self.cloud_account_role_access_credential:
            self.cloud_account_role_access_credential.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cloud_account_id is not None:
            result['cloudAccountId'] = self.cloud_account_id

        if self.cloud_account_role_access_credential is not None:
            result['cloudAccountRoleAccessCredential'] = self.cloud_account_role_access_credential.to_map()

        if self.cloud_account_role_external_id is not None:
            result['cloudAccountRoleExternalId'] = self.cloud_account_role_external_id

        if self.cloud_account_role_id is not None:
            result['cloudAccountRoleId'] = self.cloud_account_role_id

        if self.cloud_account_role_name is not None:
            result['cloudAccountRoleName'] = self.cloud_account_role_name

        if self.cloud_account_vendor_type is not None:
            result['cloudAccountVendorType'] = self.cloud_account_vendor_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cloudAccountId') is not None:
            self.cloud_account_id = m.get('cloudAccountId')

        if m.get('cloudAccountRoleAccessCredential') is not None:
            temp_model = main_models.ObtainCloudAccountRoleAccessCredentialResponseBodyCloudAccountRoleAccessCredential()
            self.cloud_account_role_access_credential = temp_model.from_map(m.get('cloudAccountRoleAccessCredential'))

        if m.get('cloudAccountRoleExternalId') is not None:
            self.cloud_account_role_external_id = m.get('cloudAccountRoleExternalId')

        if m.get('cloudAccountRoleId') is not None:
            self.cloud_account_role_id = m.get('cloudAccountRoleId')

        if m.get('cloudAccountRoleName') is not None:
            self.cloud_account_role_name = m.get('cloudAccountRoleName')

        if m.get('cloudAccountVendorType') is not None:
            self.cloud_account_vendor_type = m.get('cloudAccountVendorType')

        return self

class ObtainCloudAccountRoleAccessCredentialResponseBodyCloudAccountRoleAccessCredential(DaraModel):
    def __init__(
        self,
        access_credential_expires_at: int = None,
        alibaba_cloud_sts_token: main_models.ObtainCloudAccountRoleAccessCredentialResponseBodyCloudAccountRoleAccessCredentialAlibabaCloudStsToken = None,
    ):
        self.access_credential_expires_at = access_credential_expires_at
        self.alibaba_cloud_sts_token = alibaba_cloud_sts_token

    def validate(self):
        if self.alibaba_cloud_sts_token:
            self.alibaba_cloud_sts_token.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_credential_expires_at is not None:
            result['accessCredentialExpiresAt'] = self.access_credential_expires_at

        if self.alibaba_cloud_sts_token is not None:
            result['alibabaCloudStsToken'] = self.alibaba_cloud_sts_token.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessCredentialExpiresAt') is not None:
            self.access_credential_expires_at = m.get('accessCredentialExpiresAt')

        if m.get('alibabaCloudStsToken') is not None:
            temp_model = main_models.ObtainCloudAccountRoleAccessCredentialResponseBodyCloudAccountRoleAccessCredentialAlibabaCloudStsToken()
            self.alibaba_cloud_sts_token = temp_model.from_map(m.get('alibabaCloudStsToken'))

        return self

class ObtainCloudAccountRoleAccessCredentialResponseBodyCloudAccountRoleAccessCredentialAlibabaCloudStsToken(DaraModel):
    def __init__(
        self,
        access_key_id: str = None,
        access_key_secret: str = None,
        expiration: str = None,
        security_token: str = None,
    ):
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret
        self.expiration = expiration
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_key_id is not None:
            result['accessKeyId'] = self.access_key_id

        if self.access_key_secret is not None:
            result['accessKeySecret'] = self.access_key_secret

        if self.expiration is not None:
            result['expiration'] = self.expiration

        if self.security_token is not None:
            result['securityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKeyId') is not None:
            self.access_key_id = m.get('accessKeyId')

        if m.get('accessKeySecret') is not None:
            self.access_key_secret = m.get('accessKeySecret')

        if m.get('expiration') is not None:
            self.expiration = m.get('expiration')

        if m.get('securityToken') is not None:
            self.security_token = m.get('securityToken')

        return self

