# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eiam_developerapi20220225 import models as main_models
from darabonba.model import DaraModel

class CreateUserExclusiveCredentialRequest(DaraModel):
    def __init__(
        self,
        credential_content: main_models.CreateUserExclusiveCredentialRequestCredentialContent = None,
        credential_external_id: str = None,
        credential_identifier: str = None,
        credential_name: str = None,
        credential_scenario_label: str = None,
        credential_type: str = None,
        description: str = None,
        return_ciphertext: bool = None,
    ):
        # The credential content.
        # 
        # This parameter is required.
        self.credential_content = credential_content
        self.credential_external_id = credential_external_id
        # The credential identifier.
        # 
        # This parameter is required.
        self.credential_identifier = credential_identifier
        # The credential name.
        # 
        # This parameter is required.
        self.credential_name = credential_name
        # The scenarios label of the credential. Valid values:
        # - llm: large language model.
        # - saas: third-party SaaS service.
        self.credential_scenario_label = credential_scenario_label
        # The credential type. Valid values:
        # - api_key: API Key authentication credential.
        # - oauth_client: OAuth client authentication credential.
        # 
        # This parameter is required.
        self.credential_type = credential_type
        # The credential description.
        self.description = description
        self.return_ciphertext = return_ciphertext

    def validate(self):
        if self.credential_content:
            self.credential_content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credential_content is not None:
            result['credentialContent'] = self.credential_content.to_map()

        if self.credential_external_id is not None:
            result['credentialExternalId'] = self.credential_external_id

        if self.credential_identifier is not None:
            result['credentialIdentifier'] = self.credential_identifier

        if self.credential_name is not None:
            result['credentialName'] = self.credential_name

        if self.credential_scenario_label is not None:
            result['credentialScenarioLabel'] = self.credential_scenario_label

        if self.credential_type is not None:
            result['credentialType'] = self.credential_type

        if self.description is not None:
            result['description'] = self.description

        if self.return_ciphertext is not None:
            result['returnCiphertext'] = self.return_ciphertext

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('credentialContent') is not None:
            temp_model = main_models.CreateUserExclusiveCredentialRequestCredentialContent()
            self.credential_content = temp_model.from_map(m.get('credentialContent'))

        if m.get('credentialExternalId') is not None:
            self.credential_external_id = m.get('credentialExternalId')

        if m.get('credentialIdentifier') is not None:
            self.credential_identifier = m.get('credentialIdentifier')

        if m.get('credentialName') is not None:
            self.credential_name = m.get('credentialName')

        if m.get('credentialScenarioLabel') is not None:
            self.credential_scenario_label = m.get('credentialScenarioLabel')

        if m.get('credentialType') is not None:
            self.credential_type = m.get('credentialType')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('returnCiphertext') is not None:
            self.return_ciphertext = m.get('returnCiphertext')

        return self

class CreateUserExclusiveCredentialRequestCredentialContent(DaraModel):
    def __init__(
        self,
        api_key_content: main_models.CreateUserExclusiveCredentialRequestCredentialContentApiKeyContent = None,
    ):
        # The credential content for the API Key credential type.
        self.api_key_content = api_key_content

    def validate(self):
        if self.api_key_content:
            self.api_key_content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key_content is not None:
            result['apiKeyContent'] = self.api_key_content.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiKeyContent') is not None:
            temp_model = main_models.CreateUserExclusiveCredentialRequestCredentialContentApiKeyContent()
            self.api_key_content = temp_model.from_map(m.get('apiKeyContent'))

        return self

class CreateUserExclusiveCredentialRequestCredentialContentApiKeyContent(DaraModel):
    def __init__(
        self,
        api_key: str = None,
    ):
        # The value of the API Key.
        # 
        # This parameter is required.
        self.api_key = api_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['apiKey'] = self.api_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiKey') is not None:
            self.api_key = m.get('apiKey')

        return self

