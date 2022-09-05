# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict


class AssumeRoleRequest(TeaModel):
    def __init__(
        self,
        duration_seconds: int = None,
        policy: str = None,
        role_arn: str = None,
        role_session_name: str = None,
    ):
        self.duration_seconds = duration_seconds
        self.policy = policy
        self.role_arn = role_arn
        self.role_session_name = role_session_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration_seconds is not None:
            result['DurationSeconds'] = self.duration_seconds
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        if self.role_session_name is not None:
            result['RoleSessionName'] = self.role_session_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DurationSeconds') is not None:
            self.duration_seconds = m.get('DurationSeconds')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        if m.get('RoleSessionName') is not None:
            self.role_session_name = m.get('RoleSessionName')
        return self


class AssumeRoleResponseBodyAssumedRoleUser(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class AssumeRoleResponseBodyCredentials(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class AssumeRoleResponseBody(TeaModel):
    def __init__(
        self,
        assumed_role_user: AssumeRoleResponseBodyAssumedRoleUser = None,
        credentials: AssumeRoleResponseBodyCredentials = None,
        request_id: str = None,
    ):
        self.assumed_role_user = assumed_role_user
        self.credentials = credentials
        self.request_id = request_id

    def validate(self):
        if self.assumed_role_user:
            self.assumed_role_user.validate()
        if self.credentials:
            self.credentials.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assumed_role_user is not None:
            result['AssumedRoleUser'] = self.assumed_role_user.to_map()
        if self.credentials is not None:
            result['Credentials'] = self.credentials.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssumedRoleUser') is not None:
            temp_model = AssumeRoleResponseBodyAssumedRoleUser()
            self.assumed_role_user = temp_model.from_map(m['AssumedRoleUser'])
        if m.get('Credentials') is not None:
            temp_model = AssumeRoleResponseBodyCredentials()
            self.credentials = temp_model.from_map(m['Credentials'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AssumeRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AssumeRoleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AssumeRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssumeRoleWithOIDCRequest(TeaModel):
    def __init__(
        self,
        duration_seconds: int = None,
        oidcprovider_arn: str = None,
        oidctoken: str = None,
        policy: str = None,
        role_arn: str = None,
        role_session_name: str = None,
    ):
        self.duration_seconds = duration_seconds
        self.oidcprovider_arn = oidcprovider_arn
        self.oidctoken = oidctoken
        self.policy = policy
        self.role_arn = role_arn
        self.role_session_name = role_session_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration_seconds is not None:
            result['DurationSeconds'] = self.duration_seconds
        if self.oidcprovider_arn is not None:
            result['OIDCProviderArn'] = self.oidcprovider_arn
        if self.oidctoken is not None:
            result['OIDCToken'] = self.oidctoken
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        if self.role_session_name is not None:
            result['RoleSessionName'] = self.role_session_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DurationSeconds') is not None:
            self.duration_seconds = m.get('DurationSeconds')
        if m.get('OIDCProviderArn') is not None:
            self.oidcprovider_arn = m.get('OIDCProviderArn')
        if m.get('OIDCToken') is not None:
            self.oidctoken = m.get('OIDCToken')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        if m.get('RoleSessionName') is not None:
            self.role_session_name = m.get('RoleSessionName')
        return self


class AssumeRoleWithOIDCResponseBodyAssumedRoleUser(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class AssumeRoleWithOIDCResponseBodyCredentials(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class AssumeRoleWithOIDCResponseBodyOIDCTokenInfo(TeaModel):
    def __init__(
        self,
        client_ids: str = None,
        issuer: str = None,
        subject: str = None,
    ):
        self.client_ids = client_ids
        self.issuer = issuer
        self.subject = subject

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_ids is not None:
            result['ClientIds'] = self.client_ids
        if self.issuer is not None:
            result['Issuer'] = self.issuer
        if self.subject is not None:
            result['Subject'] = self.subject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIds') is not None:
            self.client_ids = m.get('ClientIds')
        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')
        if m.get('Subject') is not None:
            self.subject = m.get('Subject')
        return self


class AssumeRoleWithOIDCResponseBody(TeaModel):
    def __init__(
        self,
        assumed_role_user: AssumeRoleWithOIDCResponseBodyAssumedRoleUser = None,
        credentials: AssumeRoleWithOIDCResponseBodyCredentials = None,
        oidctoken_info: AssumeRoleWithOIDCResponseBodyOIDCTokenInfo = None,
        request_id: str = None,
    ):
        self.assumed_role_user = assumed_role_user
        self.credentials = credentials
        self.oidctoken_info = oidctoken_info
        self.request_id = request_id

    def validate(self):
        if self.assumed_role_user:
            self.assumed_role_user.validate()
        if self.credentials:
            self.credentials.validate()
        if self.oidctoken_info:
            self.oidctoken_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assumed_role_user is not None:
            result['AssumedRoleUser'] = self.assumed_role_user.to_map()
        if self.credentials is not None:
            result['Credentials'] = self.credentials.to_map()
        if self.oidctoken_info is not None:
            result['OIDCTokenInfo'] = self.oidctoken_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssumedRoleUser') is not None:
            temp_model = AssumeRoleWithOIDCResponseBodyAssumedRoleUser()
            self.assumed_role_user = temp_model.from_map(m['AssumedRoleUser'])
        if m.get('Credentials') is not None:
            temp_model = AssumeRoleWithOIDCResponseBodyCredentials()
            self.credentials = temp_model.from_map(m['Credentials'])
        if m.get('OIDCTokenInfo') is not None:
            temp_model = AssumeRoleWithOIDCResponseBodyOIDCTokenInfo()
            self.oidctoken_info = temp_model.from_map(m['OIDCTokenInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AssumeRoleWithOIDCResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AssumeRoleWithOIDCResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AssumeRoleWithOIDCResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssumeRoleWithSAMLRequest(TeaModel):
    def __init__(
        self,
        duration_seconds: int = None,
        policy: str = None,
        role_arn: str = None,
        samlassertion: str = None,
        samlprovider_arn: str = None,
    ):
        self.duration_seconds = duration_seconds
        self.policy = policy
        self.role_arn = role_arn
        self.samlassertion = samlassertion
        self.samlprovider_arn = samlprovider_arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration_seconds is not None:
            result['DurationSeconds'] = self.duration_seconds
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        if self.samlassertion is not None:
            result['SAMLAssertion'] = self.samlassertion
        if self.samlprovider_arn is not None:
            result['SAMLProviderArn'] = self.samlprovider_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DurationSeconds') is not None:
            self.duration_seconds = m.get('DurationSeconds')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        if m.get('SAMLAssertion') is not None:
            self.samlassertion = m.get('SAMLAssertion')
        if m.get('SAMLProviderArn') is not None:
            self.samlprovider_arn = m.get('SAMLProviderArn')
        return self


class AssumeRoleWithSAMLResponseBodyAssumedRoleUser(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class AssumeRoleWithSAMLResponseBodyCredentials(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class AssumeRoleWithSAMLResponseBodySAMLAssertionInfo(TeaModel):
    def __init__(
        self,
        issuer: str = None,
        recipient: str = None,
        subject: str = None,
        subject_type: str = None,
    ):
        self.issuer = issuer
        self.recipient = recipient
        self.subject = subject
        self.subject_type = subject_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.issuer is not None:
            result['Issuer'] = self.issuer
        if self.recipient is not None:
            result['Recipient'] = self.recipient
        if self.subject is not None:
            result['Subject'] = self.subject
        if self.subject_type is not None:
            result['SubjectType'] = self.subject_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')
        if m.get('Recipient') is not None:
            self.recipient = m.get('Recipient')
        if m.get('Subject') is not None:
            self.subject = m.get('Subject')
        if m.get('SubjectType') is not None:
            self.subject_type = m.get('SubjectType')
        return self


class AssumeRoleWithSAMLResponseBody(TeaModel):
    def __init__(
        self,
        assumed_role_user: AssumeRoleWithSAMLResponseBodyAssumedRoleUser = None,
        credentials: AssumeRoleWithSAMLResponseBodyCredentials = None,
        request_id: str = None,
        samlassertion_info: AssumeRoleWithSAMLResponseBodySAMLAssertionInfo = None,
    ):
        self.assumed_role_user = assumed_role_user
        self.credentials = credentials
        self.request_id = request_id
        self.samlassertion_info = samlassertion_info

    def validate(self):
        if self.assumed_role_user:
            self.assumed_role_user.validate()
        if self.credentials:
            self.credentials.validate()
        if self.samlassertion_info:
            self.samlassertion_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assumed_role_user is not None:
            result['AssumedRoleUser'] = self.assumed_role_user.to_map()
        if self.credentials is not None:
            result['Credentials'] = self.credentials.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.samlassertion_info is not None:
            result['SAMLAssertionInfo'] = self.samlassertion_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssumedRoleUser') is not None:
            temp_model = AssumeRoleWithSAMLResponseBodyAssumedRoleUser()
            self.assumed_role_user = temp_model.from_map(m['AssumedRoleUser'])
        if m.get('Credentials') is not None:
            temp_model = AssumeRoleWithSAMLResponseBodyCredentials()
            self.credentials = temp_model.from_map(m['Credentials'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SAMLAssertionInfo') is not None:
            temp_model = AssumeRoleWithSAMLResponseBodySAMLAssertionInfo()
            self.samlassertion_info = temp_model.from_map(m['SAMLAssertionInfo'])
        return self


class AssumeRoleWithSAMLResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AssumeRoleWithSAMLResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AssumeRoleWithSAMLResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCallerIdentityResponseBody(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        arn: str = None,
        identity_type: str = None,
        principal_id: str = None,
        request_id: str = None,
        role_id: str = None,
        user_id: str = None,
    ):
        self.account_id = account_id
        self.arn = arn
        self.identity_type = identity_type
        self.principal_id = principal_id
        self.request_id = request_id
        self.role_id = role_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.identity_type is not None:
            result['IdentityType'] = self.identity_type
        if self.principal_id is not None:
            result['PrincipalId'] = self.principal_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('IdentityType') is not None:
            self.identity_type = m.get('IdentityType')
        if m.get('PrincipalId') is not None:
            self.principal_id = m.get('PrincipalId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetCallerIdentityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCallerIdentityResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetCallerIdentityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


