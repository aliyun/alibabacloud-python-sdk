# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentidentitydata20251127 import models as main_models
from darabonba.model import DaraModel

class AssumeRoleForWorkloadIdentityResponseBody(DaraModel):
    def __init__(
        self,
        assumed_role_user: main_models.AssumeRoleForWorkloadIdentityResponseBodyAssumedRoleUser = None,
        credentials: main_models.AssumeRoleForWorkloadIdentityResponseBodyCredentials = None,
        request_id: str = None,
        workload_context_info: main_models.AssumeRoleForWorkloadIdentityResponseBodyWorkloadContextInfo = None,
    ):
        self.assumed_role_user = assumed_role_user
        self.credentials = credentials
        self.request_id = request_id
        self.workload_context_info = workload_context_info

    def validate(self):
        if self.assumed_role_user:
            self.assumed_role_user.validate()
        if self.credentials:
            self.credentials.validate()
        if self.workload_context_info:
            self.workload_context_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assumed_role_user is not None:
            result['AssumedRoleUser'] = self.assumed_role_user.to_map()

        if self.credentials is not None:
            result['Credentials'] = self.credentials.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.workload_context_info is not None:
            result['WorkloadContextInfo'] = self.workload_context_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssumedRoleUser') is not None:
            temp_model = main_models.AssumeRoleForWorkloadIdentityResponseBodyAssumedRoleUser()
            self.assumed_role_user = temp_model.from_map(m.get('AssumedRoleUser'))

        if m.get('Credentials') is not None:
            temp_model = main_models.AssumeRoleForWorkloadIdentityResponseBodyCredentials()
            self.credentials = temp_model.from_map(m.get('Credentials'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('WorkloadContextInfo') is not None:
            temp_model = main_models.AssumeRoleForWorkloadIdentityResponseBodyWorkloadContextInfo()
            self.workload_context_info = temp_model.from_map(m.get('WorkloadContextInfo'))

        return self

class AssumeRoleForWorkloadIdentityResponseBodyWorkloadContextInfo(DaraModel):
    def __init__(
        self,
        user_context: main_models.AssumeRoleForWorkloadIdentityResponseBodyWorkloadContextInfoUserContext = None,
        workload_identity_arn: str = None,
    ):
        self.user_context = user_context
        self.workload_identity_arn = workload_identity_arn

    def validate(self):
        if self.user_context:
            self.user_context.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_context is not None:
            result['UserContext'] = self.user_context.to_map()

        if self.workload_identity_arn is not None:
            result['WorkloadIdentityArn'] = self.workload_identity_arn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserContext') is not None:
            temp_model = main_models.AssumeRoleForWorkloadIdentityResponseBodyWorkloadContextInfoUserContext()
            self.user_context = temp_model.from_map(m.get('UserContext'))

        if m.get('WorkloadIdentityArn') is not None:
            self.workload_identity_arn = m.get('WorkloadIdentityArn')

        return self

class AssumeRoleForWorkloadIdentityResponseBodyWorkloadContextInfoUserContext(DaraModel):
    def __init__(
        self,
        jwt_claims: main_models.AssumeRoleForWorkloadIdentityResponseBodyWorkloadContextInfoUserContextJwtClaims = None,
        user_id: str = None,
    ):
        self.jwt_claims = jwt_claims
        self.user_id = user_id

    def validate(self):
        if self.jwt_claims:
            self.jwt_claims.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.jwt_claims is not None:
            result['JwtClaims'] = self.jwt_claims.to_map()

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JwtClaims') is not None:
            temp_model = main_models.AssumeRoleForWorkloadIdentityResponseBodyWorkloadContextInfoUserContextJwtClaims()
            self.jwt_claims = temp_model.from_map(m.get('JwtClaims'))

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class AssumeRoleForWorkloadIdentityResponseBodyWorkloadContextInfoUserContextJwtClaims(DaraModel):
    def __init__(
        self,
        audiences: str = None,
        issuer: str = None,
        subject: str = None,
    ):
        self.audiences = audiences
        self.issuer = issuer
        self.subject = subject

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audiences is not None:
            result['Audiences'] = self.audiences

        if self.issuer is not None:
            result['Issuer'] = self.issuer

        if self.subject is not None:
            result['Subject'] = self.subject

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Audiences') is not None:
            self.audiences = m.get('Audiences')

        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')

        if m.get('Subject') is not None:
            self.subject = m.get('Subject')

        return self

class AssumeRoleForWorkloadIdentityResponseBodyCredentials(DaraModel):
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



class AssumeRoleForWorkloadIdentityResponseBodyAssumedRoleUser(DaraModel):
    def __init__(
        self,
        arn: str = None,
        assumed_role_id: str = None,
    ):
        self.arn = arn
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

