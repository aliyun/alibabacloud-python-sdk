# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sts20150401 import models as main_models
from darabonba.model import DaraModel

class AssumeRoleWithSAMLResponseBody(DaraModel):
    def __init__(
        self,
        assumed_role_user: main_models.AssumeRoleWithSAMLResponseBodyAssumedRoleUser = None,
        credentials: main_models.AssumeRoleWithSAMLResponseBodyCredentials = None,
        request_id: str = None,
        samlassertion_info: main_models.AssumeRoleWithSAMLResponseBodySAMLAssertionInfo = None,
        source_identity: str = None,
    ):
        # The temporary identity that you use to assume the RAM role.
        self.assumed_role_user = assumed_role_user
        # The STS credentials.
        self.credentials = credentials
        # The ID of the request.
        self.request_id = request_id
        # The information in the SAML assertion.
        self.samlassertion_info = samlassertion_info
        self.source_identity = source_identity

    def validate(self):
        if self.assumed_role_user:
            self.assumed_role_user.validate()
        if self.credentials:
            self.credentials.validate()
        if self.samlassertion_info:
            self.samlassertion_info.validate()

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

        if self.samlassertion_info is not None:
            result['SAMLAssertionInfo'] = self.samlassertion_info.to_map()

        if self.source_identity is not None:
            result['SourceIdentity'] = self.source_identity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssumedRoleUser') is not None:
            temp_model = main_models.AssumeRoleWithSAMLResponseBodyAssumedRoleUser()
            self.assumed_role_user = temp_model.from_map(m.get('AssumedRoleUser'))

        if m.get('Credentials') is not None:
            temp_model = main_models.AssumeRoleWithSAMLResponseBodyCredentials()
            self.credentials = temp_model.from_map(m.get('Credentials'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SAMLAssertionInfo') is not None:
            temp_model = main_models.AssumeRoleWithSAMLResponseBodySAMLAssertionInfo()
            self.samlassertion_info = temp_model.from_map(m.get('SAMLAssertionInfo'))

        if m.get('SourceIdentity') is not None:
            self.source_identity = m.get('SourceIdentity')

        return self

class AssumeRoleWithSAMLResponseBodySAMLAssertionInfo(DaraModel):
    def __init__(
        self,
        issuer: str = None,
        recipient: str = None,
        subject: str = None,
        subject_type: str = None,
    ):
        # The value in the `Issuer` element in the SAML assertion.
        self.issuer = issuer
        # The `Recipient` attribute of the SubjectConfirmationData sub-element. SubjectConfirmationData is a sub-element of the `Subject` element in the SAML assertion.
        self.recipient = recipient
        # The value in the NameID sub-element of the `Subject` element in the SAML assertion.
        self.subject = subject
        # The Format attribute of the `NameID` element in the SAML assertion. If the Format attribute is prefixed with `urn:oasis:names:tc:SAML:2.0:nameid-format:`, the prefix is not included in the value of this parameter. For example, if the value of the Format attribute is urn:oasis:names:tc:SAML:2.0:nameid-format:persistent/transient, the value of this parameter is `persistent/transient`.
        self.subject_type = subject_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class AssumeRoleWithSAMLResponseBodyCredentials(DaraModel):
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

class AssumeRoleWithSAMLResponseBodyAssumedRoleUser(DaraModel):
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

