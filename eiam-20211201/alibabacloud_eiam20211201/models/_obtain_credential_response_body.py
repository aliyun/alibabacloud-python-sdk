# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class ObtainCredentialResponseBody(DaraModel):
    def __init__(
        self,
        credential: main_models.ObtainCredentialResponseBodyCredential = None,
        request_id: str = None,
    ):
        self.credential = credential
        self.request_id = request_id

    def validate(self):
        if self.credential:
            self.credential.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credential is not None:
            result['Credential'] = self.credential.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Credential') is not None:
            temp_model = main_models.ObtainCredentialResponseBodyCredential()
            self.credential = temp_model.from_map(m.get('Credential'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ObtainCredentialResponseBodyCredential(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        credential_content: main_models.ObtainCredentialResponseBodyCredentialCredentialContent = None,
        credential_creation_type: str = None,
        credential_id: str = None,
        credential_identifier: str = None,
        credential_name: str = None,
        credential_scenario_label: str = None,
        credential_subject_id: str = None,
        credential_subject_type: str = None,
        credential_type: str = None,
        description: str = None,
        instance_id: str = None,
        status: str = None,
        update_time: int = None,
    ):
        # 云角色创建时间
        self.create_time = create_time
        # 凭据的内容。
        self.credential_content = credential_content
        # 凭据的创建类型。
        self.credential_creation_type = credential_creation_type
        # 凭据ID。
        self.credential_id = credential_id
        # 凭据标识
        self.credential_identifier = credential_identifier
        # 凭据名称
        self.credential_name = credential_name
        # 凭据的使用场景标签。
        self.credential_scenario_label = credential_scenario_label
        # 凭据所属的主体ID。
        self.credential_subject_id = credential_subject_id
        # 凭据所属的主体类型。
        self.credential_subject_type = credential_subject_type
        # 凭据类型。
        self.credential_type = credential_type
        # 描述
        self.description = description
        # EIAM实例ID。
        self.instance_id = instance_id
        # 凭据状态
        self.status = status
        # 云角色更新时间
        self.update_time = update_time

    def validate(self):
        if self.credential_content:
            self.credential_content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.credential_content is not None:
            result['CredentialContent'] = self.credential_content.to_map()

        if self.credential_creation_type is not None:
            result['CredentialCreationType'] = self.credential_creation_type

        if self.credential_id is not None:
            result['CredentialId'] = self.credential_id

        if self.credential_identifier is not None:
            result['CredentialIdentifier'] = self.credential_identifier

        if self.credential_name is not None:
            result['CredentialName'] = self.credential_name

        if self.credential_scenario_label is not None:
            result['CredentialScenarioLabel'] = self.credential_scenario_label

        if self.credential_subject_id is not None:
            result['CredentialSubjectId'] = self.credential_subject_id

        if self.credential_subject_type is not None:
            result['CredentialSubjectType'] = self.credential_subject_type

        if self.credential_type is not None:
            result['CredentialType'] = self.credential_type

        if self.description is not None:
            result['Description'] = self.description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CredentialContent') is not None:
            temp_model = main_models.ObtainCredentialResponseBodyCredentialCredentialContent()
            self.credential_content = temp_model.from_map(m.get('CredentialContent'))

        if m.get('CredentialCreationType') is not None:
            self.credential_creation_type = m.get('CredentialCreationType')

        if m.get('CredentialId') is not None:
            self.credential_id = m.get('CredentialId')

        if m.get('CredentialIdentifier') is not None:
            self.credential_identifier = m.get('CredentialIdentifier')

        if m.get('CredentialName') is not None:
            self.credential_name = m.get('CredentialName')

        if m.get('CredentialScenarioLabel') is not None:
            self.credential_scenario_label = m.get('CredentialScenarioLabel')

        if m.get('CredentialSubjectId') is not None:
            self.credential_subject_id = m.get('CredentialSubjectId')

        if m.get('CredentialSubjectType') is not None:
            self.credential_subject_type = m.get('CredentialSubjectType')

        if m.get('CredentialType') is not None:
            self.credential_type = m.get('CredentialType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class ObtainCredentialResponseBodyCredentialCredentialContent(DaraModel):
    def __init__(
        self,
        api_key_content: main_models.ObtainCredentialResponseBodyCredentialCredentialContentApiKeyContent = None,
        oauth_client_content: main_models.ObtainCredentialResponseBodyCredentialCredentialContentOAuthClientContent = None,
    ):
        self.api_key_content = api_key_content
        # OAuth客户端认证凭证类型的凭据内容。
        self.oauth_client_content = oauth_client_content

    def validate(self):
        if self.api_key_content:
            self.api_key_content.validate()
        if self.oauth_client_content:
            self.oauth_client_content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key_content is not None:
            result['ApiKeyContent'] = self.api_key_content.to_map()

        if self.oauth_client_content is not None:
            result['OAuthClientContent'] = self.oauth_client_content.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKeyContent') is not None:
            temp_model = main_models.ObtainCredentialResponseBodyCredentialCredentialContentApiKeyContent()
            self.api_key_content = temp_model.from_map(m.get('ApiKeyContent'))

        if m.get('OAuthClientContent') is not None:
            temp_model = main_models.ObtainCredentialResponseBodyCredentialCredentialContentOAuthClientContent()
            self.oauth_client_content = temp_model.from_map(m.get('OAuthClientContent'))

        return self

class ObtainCredentialResponseBodyCredentialCredentialContentOAuthClientContent(DaraModel):
    def __init__(
        self,
        client_id: str = None,
        client_secret: str = None,
    ):
        # OAuth协议的client_id
        self.client_id = client_id
        self.client_secret = client_secret

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.client_secret is not None:
            result['ClientSecret'] = self.client_secret

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('ClientSecret') is not None:
            self.client_secret = m.get('ClientSecret')

        return self

class ObtainCredentialResponseBodyCredentialCredentialContentApiKeyContent(DaraModel):
    def __init__(
        self,
        api_key: str = None,
    ):
        self.api_key = api_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['ApiKey'] = self.api_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')

        return self

