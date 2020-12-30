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
        assumed_role_id: str = None,
        arn: str = None,
    ):
        self.assumed_role_id = assumed_role_id
        self.arn = arn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.assumed_role_id is not None:
            result['AssumedRoleId'] = self.assumed_role_id
        if self.arn is not None:
            result['Arn'] = self.arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssumedRoleId') is not None:
            self.assumed_role_id = m.get('AssumedRoleId')
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        return self


class AssumeRoleResponseBodyCredentials(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        expiration: str = None,
        access_key_secret: str = None,
        access_key_id: str = None,
    ):
        self.security_token = security_token
        self.expiration = expiration
        self.access_key_secret = access_key_secret
        self.access_key_id = access_key_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.expiration is not None:
            result['Expiration'] = self.expiration
        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')
        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        return self


class AssumeRoleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        assumed_role_user: AssumeRoleResponseBodyAssumedRoleUser = None,
        credentials: AssumeRoleResponseBodyCredentials = None,
    ):
        self.request_id = request_id
        self.assumed_role_user = assumed_role_user
        self.credentials = credentials

    def validate(self):
        if self.assumed_role_user:
            self.assumed_role_user.validate()
        if self.credentials:
            self.credentials.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.assumed_role_user is not None:
            result['AssumedRoleUser'] = self.assumed_role_user.to_map()
        if self.credentials is not None:
            result['Credentials'] = self.credentials.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AssumedRoleUser') is not None:
            temp_model = AssumeRoleResponseBodyAssumedRoleUser()
            self.assumed_role_user = temp_model.from_map(m['AssumedRoleUser'])
        if m.get('Credentials') is not None:
            temp_model = AssumeRoleResponseBodyCredentials()
            self.credentials = temp_model.from_map(m['Credentials'])
        return self


class AssumeRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AssumeRoleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AssumeRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssumeRoleWithSAMLRequest(TeaModel):
    def __init__(
        self,
        samlprovider_arn: str = None,
        role_arn: str = None,
        samlassertion: str = None,
        policy: str = None,
        duration_seconds: int = None,
    ):
        self.samlprovider_arn = samlprovider_arn
        self.role_arn = role_arn
        self.samlassertion = samlassertion
        self.policy = policy
        self.duration_seconds = duration_seconds

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.samlprovider_arn is not None:
            result['SAMLProviderArn'] = self.samlprovider_arn
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        if self.samlassertion is not None:
            result['SAMLAssertion'] = self.samlassertion
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.duration_seconds is not None:
            result['DurationSeconds'] = self.duration_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SAMLProviderArn') is not None:
            self.samlprovider_arn = m.get('SAMLProviderArn')
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        if m.get('SAMLAssertion') is not None:
            self.samlassertion = m.get('SAMLAssertion')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('DurationSeconds') is not None:
            self.duration_seconds = m.get('DurationSeconds')
        return self


class AssumeRoleWithSAMLResponseBodySAMLAssertionInfo(TeaModel):
    def __init__(
        self,
        subject_type: str = None,
        subject: str = None,
        issuer: str = None,
        recipient: str = None,
    ):
        self.subject_type = subject_type
        self.subject = subject
        self.issuer = issuer
        self.recipient = recipient

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.subject_type is not None:
            result['SubjectType'] = self.subject_type
        if self.subject is not None:
            result['Subject'] = self.subject
        if self.issuer is not None:
            result['Issuer'] = self.issuer
        if self.recipient is not None:
            result['Recipient'] = self.recipient
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubjectType') is not None:
            self.subject_type = m.get('SubjectType')
        if m.get('Subject') is not None:
            self.subject = m.get('Subject')
        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')
        if m.get('Recipient') is not None:
            self.recipient = m.get('Recipient')
        return self


class AssumeRoleWithSAMLResponseBodyAssumedRoleUser(TeaModel):
    def __init__(
        self,
        assumed_role_id: str = None,
        arn: str = None,
    ):
        self.assumed_role_id = assumed_role_id
        self.arn = arn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.assumed_role_id is not None:
            result['AssumedRoleId'] = self.assumed_role_id
        if self.arn is not None:
            result['Arn'] = self.arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssumedRoleId') is not None:
            self.assumed_role_id = m.get('AssumedRoleId')
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        return self


class AssumeRoleWithSAMLResponseBodyCredentials(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        expiration: str = None,
        access_key_secret: str = None,
        access_key_id: str = None,
    ):
        self.security_token = security_token
        self.expiration = expiration
        self.access_key_secret = access_key_secret
        self.access_key_id = access_key_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.expiration is not None:
            result['Expiration'] = self.expiration
        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')
        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        return self


class AssumeRoleWithSAMLResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        samlassertion_info: AssumeRoleWithSAMLResponseBodySAMLAssertionInfo = None,
        assumed_role_user: AssumeRoleWithSAMLResponseBodyAssumedRoleUser = None,
        credentials: AssumeRoleWithSAMLResponseBodyCredentials = None,
    ):
        self.request_id = request_id
        self.samlassertion_info = samlassertion_info
        self.assumed_role_user = assumed_role_user
        self.credentials = credentials

    def validate(self):
        if self.samlassertion_info:
            self.samlassertion_info.validate()
        if self.assumed_role_user:
            self.assumed_role_user.validate()
        if self.credentials:
            self.credentials.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.samlassertion_info is not None:
            result['SAMLAssertionInfo'] = self.samlassertion_info.to_map()
        if self.assumed_role_user is not None:
            result['AssumedRoleUser'] = self.assumed_role_user.to_map()
        if self.credentials is not None:
            result['Credentials'] = self.credentials.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SAMLAssertionInfo') is not None:
            temp_model = AssumeRoleWithSAMLResponseBodySAMLAssertionInfo()
            self.samlassertion_info = temp_model.from_map(m['SAMLAssertionInfo'])
        if m.get('AssumedRoleUser') is not None:
            temp_model = AssumeRoleWithSAMLResponseBodyAssumedRoleUser()
            self.assumed_role_user = temp_model.from_map(m['AssumedRoleUser'])
        if m.get('Credentials') is not None:
            temp_model = AssumeRoleWithSAMLResponseBodyCredentials()
            self.credentials = temp_model.from_map(m['Credentials'])
        return self


class AssumeRoleWithSAMLResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AssumeRoleWithSAMLResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AssumeRoleWithSAMLResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCallerIdentityResponseBody(TeaModel):
    def __init__(
        self,
        identity_type: str = None,
        account_id: str = None,
        request_id: str = None,
        principal_id: str = None,
        user_id: str = None,
        arn: str = None,
        role_id: str = None,
    ):
        self.identity_type = identity_type
        self.account_id = account_id
        self.request_id = request_id
        self.principal_id = principal_id
        self.user_id = user_id
        self.arn = arn
        self.role_id = role_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.identity_type is not None:
            result['IdentityType'] = self.identity_type
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.principal_id is not None:
            result['PrincipalId'] = self.principal_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdentityType') is not None:
            self.identity_type = m.get('IdentityType')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PrincipalId') is not None:
            self.principal_id = m.get('PrincipalId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        return self


class GetCallerIdentityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetCallerIdentityResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetCallerIdentityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


