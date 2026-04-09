# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eiam_developerapi20220225 import models as main_models
from darabonba.model import DaraModel

class CreateUserExclusiveCredentialRequest(DaraModel):
    def __init__(
        self,
        credential_content: main_models.CreateUserExclusiveCredentialRequestCredentialContent = None,
        credential_identifier: str = None,
        credential_name: str = None,
        credential_scenario_label: str = None,
        credential_type: str = None,
        description: str = None,
    ):
        # This parameter is required.
        self.credential_content = credential_content
        # This parameter is required.
        self.credential_identifier = credential_identifier
        # This parameter is required.
        self.credential_name = credential_name
        self.credential_scenario_label = credential_scenario_label
        # This parameter is required.
        self.credential_type = credential_type
        self.description = description

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('credentialContent') is not None:
            temp_model = main_models.CreateUserExclusiveCredentialRequestCredentialContent()
            self.credential_content = temp_model.from_map(m.get('credentialContent'))

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

        return self

class CreateUserExclusiveCredentialRequestCredentialContent(DaraModel):
    def __init__(
        self,
        api_key_content: main_models.CreateUserExclusiveCredentialRequestCredentialContentApiKeyContent = None,
    ):
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

