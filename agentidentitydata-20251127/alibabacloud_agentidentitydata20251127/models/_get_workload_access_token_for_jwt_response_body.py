# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentidentitydata20251127 import models as main_models
from darabonba.model import DaraModel

class GetWorkloadAccessTokenForJWTResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        user_context: main_models.GetWorkloadAccessTokenForJWTResponseBodyUserContext = None,
        workload_access_token: str = None,
        workload_identity_arn: str = None,
    ):
        self.request_id = request_id
        self.user_context = user_context
        self.workload_access_token = workload_access_token
        self.workload_identity_arn = workload_identity_arn

    def validate(self):
        if self.user_context:
            self.user_context.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.user_context is not None:
            result['UserContext'] = self.user_context.to_map()

        if self.workload_access_token is not None:
            result['WorkloadAccessToken'] = self.workload_access_token

        if self.workload_identity_arn is not None:
            result['WorkloadIdentityArn'] = self.workload_identity_arn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UserContext') is not None:
            temp_model = main_models.GetWorkloadAccessTokenForJWTResponseBodyUserContext()
            self.user_context = temp_model.from_map(m.get('UserContext'))

        if m.get('WorkloadAccessToken') is not None:
            self.workload_access_token = m.get('WorkloadAccessToken')

        if m.get('WorkloadIdentityArn') is not None:
            self.workload_identity_arn = m.get('WorkloadIdentityArn')

        return self

class GetWorkloadAccessTokenForJWTResponseBodyUserContext(DaraModel):
    def __init__(
        self,
        jwt_claims: main_models.GetWorkloadAccessTokenForJWTResponseBodyUserContextJwtClaims = None,
    ):
        self.jwt_claims = jwt_claims

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JwtClaims') is not None:
            temp_model = main_models.GetWorkloadAccessTokenForJWTResponseBodyUserContextJwtClaims()
            self.jwt_claims = temp_model.from_map(m.get('JwtClaims'))

        return self

class GetWorkloadAccessTokenForJWTResponseBodyUserContextJwtClaims(DaraModel):
    def __init__(
        self,
        audiences: str = None,
        issuer: str = None,
        jti: str = None,
        subject: str = None,
    ):
        self.audiences = audiences
        self.issuer = issuer
        self.jti = jti
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

        if self.jti is not None:
            result['JTI'] = self.jti

        if self.subject is not None:
            result['Subject'] = self.subject

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Audiences') is not None:
            self.audiences = m.get('Audiences')

        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')

        if m.get('JTI') is not None:
            self.jti = m.get('JTI')

        if m.get('Subject') is not None:
            self.subject = m.get('Subject')

        return self

