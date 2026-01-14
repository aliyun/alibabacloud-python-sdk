# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_websitebuild20250429 import models as main_models
from darabonba.model import DaraModel

class GetUserTmpIdentityForPartnerResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetUserTmpIdentityForPartnerResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_msg = error_msg
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetUserTmpIdentityForPartnerResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetUserTmpIdentityForPartnerResponseBodyData(DaraModel):
    def __init__(
        self,
        credentials: main_models.GetUserTmpIdentityForPartnerResponseBodyDataCredentials = None,
        has_custom_role_auth: bool = None,
    ):
        self.credentials = credentials
        self.has_custom_role_auth = has_custom_role_auth

    def validate(self):
        if self.credentials:
            self.credentials.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credentials is not None:
            result['Credentials'] = self.credentials.to_map()

        if self.has_custom_role_auth is not None:
            result['HasCustomRoleAuth'] = self.has_custom_role_auth

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Credentials') is not None:
            temp_model = main_models.GetUserTmpIdentityForPartnerResponseBodyDataCredentials()
            self.credentials = temp_model.from_map(m.get('Credentials'))

        if m.get('HasCustomRoleAuth') is not None:
            self.has_custom_role_auth = m.get('HasCustomRoleAuth')

        return self

class GetUserTmpIdentityForPartnerResponseBodyDataCredentials(DaraModel):
    def __init__(
        self,
        encrypted_access_key_id: str = None,
        encrypted_access_key_secret: str = None,
        encrypted_security_token: str = None,
        expiration: str = None,
    ):
        self.encrypted_access_key_id = encrypted_access_key_id
        self.encrypted_access_key_secret = encrypted_access_key_secret
        self.encrypted_security_token = encrypted_security_token
        self.expiration = expiration

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.encrypted_access_key_id is not None:
            result['EncryptedAccessKeyId'] = self.encrypted_access_key_id

        if self.encrypted_access_key_secret is not None:
            result['EncryptedAccessKeySecret'] = self.encrypted_access_key_secret

        if self.encrypted_security_token is not None:
            result['EncryptedSecurityToken'] = self.encrypted_security_token

        if self.expiration is not None:
            result['Expiration'] = self.expiration

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncryptedAccessKeyId') is not None:
            self.encrypted_access_key_id = m.get('EncryptedAccessKeyId')

        if m.get('EncryptedAccessKeySecret') is not None:
            self.encrypted_access_key_secret = m.get('EncryptedAccessKeySecret')

        if m.get('EncryptedSecurityToken') is not None:
            self.encrypted_security_token = m.get('EncryptedSecurityToken')

        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')

        return self

