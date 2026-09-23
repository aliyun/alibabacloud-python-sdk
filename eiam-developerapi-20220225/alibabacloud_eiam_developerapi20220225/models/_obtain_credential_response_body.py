# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eiam_developerapi20220225 import models as main_models
from darabonba.model import DaraModel

class ObtainCredentialResponseBody(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        credential_content: main_models.ObtainCredentialResponseBodyCredentialContent = None,
        credential_creation_type: str = None,
        credential_external_id: str = None,
        credential_id: str = None,
        credential_identifier: str = None,
        credential_name: str = None,
        credential_scenario_label: str = None,
        credential_sharing_scope: str = None,
        credential_subject_id: str = None,
        credential_subject_type: str = None,
        credential_type: str = None,
        description: str = None,
        exclusive_user_id: str = None,
        instance_id: str = None,
        status: str = None,
        update_time: int = None,
    ):
        # The creation time, in UNIX timestamp format. Unit: milliseconds.
        self.create_time = create_time
        # The credential content.
        self.credential_content = credential_content
        # The creation type of the credential. Valid values:
        # - system_init: Created by the system.
        # - user_custom: Created by the user.
        self.credential_creation_type = credential_creation_type
        # The external unique identifier of the credential.
        self.credential_external_id = credential_external_id
        # The credential ID.
        self.credential_id = credential_id
        # The credential identifier.
        self.credential_identifier = credential_identifier
        # The credential name.
        self.credential_name = credential_name
        # The Scenarios label of the credential. Valid values:
        # - llm: Large language model.
        # - saas: Third-party SaaS service.
        self.credential_scenario_label = credential_scenario_label
        # The credential sharing scope.
        self.credential_sharing_scope = credential_sharing_scope
        # The subject ID that the credential belongs to.
        self.credential_subject_id = credential_subject_id
        # The subject type that the credential belongs to. Valid values:
        # - authentication_token_provider: Authentication token provider.
        self.credential_subject_type = credential_subject_type
        # The credential type. Valid values:
        # - api_key: API Key authentication credential.
        # - oauth_client: OAuth client authentication credential.
        self.credential_type = credential_type
        # The credential description.
        self.description = description
        # The exclusive account ID of the credential.
        self.exclusive_user_id = exclusive_user_id
        # The EIAM instance ID.
        self.instance_id = instance_id
        # The credential status. Valid values:
        # - enabled: Enabled.
        # - disabled: Disabled.
        self.status = status
        # The update time, in UNIX timestamp format. Unit: milliseconds.
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
            result['createTime'] = self.create_time

        if self.credential_content is not None:
            result['credentialContent'] = self.credential_content.to_map()

        if self.credential_creation_type is not None:
            result['credentialCreationType'] = self.credential_creation_type

        if self.credential_external_id is not None:
            result['credentialExternalId'] = self.credential_external_id

        if self.credential_id is not None:
            result['credentialId'] = self.credential_id

        if self.credential_identifier is not None:
            result['credentialIdentifier'] = self.credential_identifier

        if self.credential_name is not None:
            result['credentialName'] = self.credential_name

        if self.credential_scenario_label is not None:
            result['credentialScenarioLabel'] = self.credential_scenario_label

        if self.credential_sharing_scope is not None:
            result['credentialSharingScope'] = self.credential_sharing_scope

        if self.credential_subject_id is not None:
            result['credentialSubjectId'] = self.credential_subject_id

        if self.credential_subject_type is not None:
            result['credentialSubjectType'] = self.credential_subject_type

        if self.credential_type is not None:
            result['credentialType'] = self.credential_type

        if self.description is not None:
            result['description'] = self.description

        if self.exclusive_user_id is not None:
            result['exclusiveUserId'] = self.exclusive_user_id

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.status is not None:
            result['status'] = self.status

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('credentialContent') is not None:
            temp_model = main_models.ObtainCredentialResponseBodyCredentialContent()
            self.credential_content = temp_model.from_map(m.get('credentialContent'))

        if m.get('credentialCreationType') is not None:
            self.credential_creation_type = m.get('credentialCreationType')

        if m.get('credentialExternalId') is not None:
            self.credential_external_id = m.get('credentialExternalId')

        if m.get('credentialId') is not None:
            self.credential_id = m.get('credentialId')

        if m.get('credentialIdentifier') is not None:
            self.credential_identifier = m.get('credentialIdentifier')

        if m.get('credentialName') is not None:
            self.credential_name = m.get('credentialName')

        if m.get('credentialScenarioLabel') is not None:
            self.credential_scenario_label = m.get('credentialScenarioLabel')

        if m.get('credentialSharingScope') is not None:
            self.credential_sharing_scope = m.get('credentialSharingScope')

        if m.get('credentialSubjectId') is not None:
            self.credential_subject_id = m.get('credentialSubjectId')

        if m.get('credentialSubjectType') is not None:
            self.credential_subject_type = m.get('credentialSubjectType')

        if m.get('credentialType') is not None:
            self.credential_type = m.get('credentialType')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('exclusiveUserId') is not None:
            self.exclusive_user_id = m.get('exclusiveUserId')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        return self

class ObtainCredentialResponseBodyCredentialContent(DaraModel):
    def __init__(
        self,
        api_key_content: main_models.ObtainCredentialResponseBodyCredentialContentApiKeyContent = None,
        oauth_client_content: main_models.ObtainCredentialResponseBodyCredentialContentOauthClientContent = None,
    ):
        # The credential content of the API Key credential type.
        self.api_key_content = api_key_content
        # The credential content of the OAuth client authentication credential type.
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
            result['apiKeyContent'] = self.api_key_content.to_map()

        if self.oauth_client_content is not None:
            result['oauthClientContent'] = self.oauth_client_content.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiKeyContent') is not None:
            temp_model = main_models.ObtainCredentialResponseBodyCredentialContentApiKeyContent()
            self.api_key_content = temp_model.from_map(m.get('apiKeyContent'))

        if m.get('oauthClientContent') is not None:
            temp_model = main_models.ObtainCredentialResponseBodyCredentialContentOauthClientContent()
            self.oauth_client_content = temp_model.from_map(m.get('oauthClientContent'))

        return self

class ObtainCredentialResponseBodyCredentialContentOauthClientContent(DaraModel):
    def __init__(
        self,
        client_id: str = None,
        client_secret: str = None,
    ):
        # The client_id of the OAuth protocol.
        self.client_id = client_id
        # The client_secret of the OAuth protocol.
        self.client_secret = client_secret

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_id is not None:
            result['clientId'] = self.client_id

        if self.client_secret is not None:
            result['clientSecret'] = self.client_secret

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientId') is not None:
            self.client_id = m.get('clientId')

        if m.get('clientSecret') is not None:
            self.client_secret = m.get('clientSecret')

        return self

class ObtainCredentialResponseBodyCredentialContentApiKeyContent(DaraModel):
    def __init__(
        self,
        api_key: str = None,
    ):
        # The value of the API Key.
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

