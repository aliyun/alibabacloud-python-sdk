# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sts20150401 import models as main_models
from darabonba.model import DaraModel

class AssumeRoleWithOIDCResponseBody(DaraModel):
    def __init__(
        self,
        assumed_role_user: main_models.AssumeRoleWithOIDCResponseBodyAssumedRoleUser = None,
        credentials: main_models.AssumeRoleWithOIDCResponseBodyCredentials = None,
        oidctoken_info: main_models.AssumeRoleWithOIDCResponseBodyOIDCTokenInfo = None,
        request_id: str = None,
        source_identity: str = None,
    ):
        # The temporary identity that you use to assume the RAM role.
        self.assumed_role_user = assumed_role_user
        # The access credentials.
        self.credentials = credentials
        # The information about the OIDC token.
        self.oidctoken_info = oidctoken_info
        # The ID of the request.
        self.request_id = request_id
        self.source_identity = source_identity

    def validate(self):
        if self.assumed_role_user:
            self.assumed_role_user.validate()
        if self.credentials:
            self.credentials.validate()
        if self.oidctoken_info:
            self.oidctoken_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assumed_role_user is not None:
            result['AssumedRoleUser'] = self.assumed_role_user.to_map()

        if self.credentials is not None:
            result['Credentials'] = self.credentials.to_map()

        if self.oidctoken_info is not None:
            result['OIDCTokenInfo'] = self.oidctoken_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.source_identity is not None:
            result['SourceIdentity'] = self.source_identity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssumedRoleUser') is not None:
            temp_model = main_models.AssumeRoleWithOIDCResponseBodyAssumedRoleUser()
            self.assumed_role_user = temp_model.from_map(m.get('AssumedRoleUser'))

        if m.get('Credentials') is not None:
            temp_model = main_models.AssumeRoleWithOIDCResponseBodyCredentials()
            self.credentials = temp_model.from_map(m.get('Credentials'))

        if m.get('OIDCTokenInfo') is not None:
            temp_model = main_models.AssumeRoleWithOIDCResponseBodyOIDCTokenInfo()
            self.oidctoken_info = temp_model.from_map(m.get('OIDCTokenInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SourceIdentity') is not None:
            self.source_identity = m.get('SourceIdentity')

        return self

class AssumeRoleWithOIDCResponseBodyOIDCTokenInfo(DaraModel):
    def __init__(
        self,
        client_ids: str = None,
        expiration_time: str = None,
        issuance_time: str = None,
        issuer: str = None,
        subject: str = None,
        verification_info: str = None,
    ):
        # The audience. If multiple audiences are returned, the audiences are separated by commas (,).
        # 
        # The audience is represented by the `aud` field in the OIDC Token.
        self.client_ids = client_ids
        # The time when the OIDC token expires.
        self.expiration_time = expiration_time
        # The time when the OIDC token was issued.
        self.issuance_time = issuance_time
        # The URL of the issuer,
        # 
        # which is represented by the `iss` field in the OIDC Token.
        self.issuer = issuer
        # The subject,
        # 
        # which is represented by the `sub` field in the OIDC Token.
        self.subject = subject
        # The verification information about the OIDC token. For more information, see [Manage an OIDC IdP](https://help.aliyun.com/document_detail/327123.html).
        self.verification_info = verification_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_ids is not None:
            result['ClientIds'] = self.client_ids

        if self.expiration_time is not None:
            result['ExpirationTime'] = self.expiration_time

        if self.issuance_time is not None:
            result['IssuanceTime'] = self.issuance_time

        if self.issuer is not None:
            result['Issuer'] = self.issuer

        if self.subject is not None:
            result['Subject'] = self.subject

        if self.verification_info is not None:
            result['VerificationInfo'] = self.verification_info

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIds') is not None:
            self.client_ids = m.get('ClientIds')

        if m.get('ExpirationTime') is not None:
            self.expiration_time = m.get('ExpirationTime')

        if m.get('IssuanceTime') is not None:
            self.issuance_time = m.get('IssuanceTime')

        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')

        if m.get('Subject') is not None:
            self.subject = m.get('Subject')

        if m.get('VerificationInfo') is not None:
            self.verification_info = m.get('VerificationInfo')

        return self

class AssumeRoleWithOIDCResponseBodyCredentials(DaraModel):
    def __init__(
        self,
        access_key_id: str = None,
        access_key_secret: str = None,
        expiration: str = None,
        security_token: str = None,
    ):
        # The AccessKey ID.
        self.access_key_id = access_key_id
        # The AccessKey secret.
        self.access_key_secret = access_key_secret
        # The time when the STS token expires. The time is displayed in UTC.
        self.expiration = expiration
        # The STS token.
        # 
        # > Alibaba Cloud STS does not impose limits on the length of STS tokens. We strongly recommend that you do not specify a maximum length for STS tokens.
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id

        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret

        if self.expiration is not None:
            result['Expiration'] = self.expiration

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')

        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')

        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

class AssumeRoleWithOIDCResponseBodyAssumedRoleUser(DaraModel):
    def __init__(
        self,
        arn: str = None,
        assumed_role_id: str = None,
    ):
        # The ARN of the temporary identity that you use to assume the RAM role.
        self.arn = arn
        # The ID of the temporary identity that you use to assume the RAM role.
        self.assumed_role_id = assumed_role_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arn is not None:
            result['Arn'] = self.arn

        if self.assumed_role_id is not None:
            result['AssumedRoleId'] = self.assumed_role_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')

        if m.get('AssumedRoleId') is not None:
            self.assumed_role_id = m.get('AssumedRoleId')

        return self

