# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class ListCredentialsResponseBody(DaraModel):
    def __init__(
        self,
        credentials: List[main_models.ListCredentialsResponseBodyCredentials] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # A list of credentials.
        self.credentials = credentials
        # The maximum number of entries to return per page.
        self.max_results = max_results
        # The token used to retrieve the next page of results. If this parameter is not returned, it indicates all results have been returned.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.credentials:
            for v1 in self.credentials:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Credentials'] = []
        if self.credentials is not None:
            for k1 in self.credentials:
                result['Credentials'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.credentials = []
        if m.get('Credentials') is not None:
            for k1 in m.get('Credentials'):
                temp_model = main_models.ListCredentialsResponseBodyCredentials()
                self.credentials.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListCredentialsResponseBodyCredentials(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        credential_content: main_models.ListCredentialsResponseBodyCredentialsCredentialContent = None,
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
        # The time the credential was created, provided as a Unix timestamp in milliseconds.
        self.create_time = create_time
        # The content of the credential.
        self.credential_content = credential_content
        # The creation type of the credential. Valid values:
        # 
        # - `system_init`: Created by the system.
        # 
        # - `user_custom`: Created by a user.
        self.credential_creation_type = credential_creation_type
        self.credential_external_id = credential_external_id
        # The ID of the credential.
        self.credential_id = credential_id
        # The identifier of the credential.
        self.credential_identifier = credential_identifier
        # The name of the credential.
        self.credential_name = credential_name
        # The use case label for the credential. Valid values:
        # 
        # - `llm`: A large language model.
        # 
        # - `saas`: A third-party SaaS service.
        self.credential_scenario_label = credential_scenario_label
        self.credential_sharing_scope = credential_sharing_scope
        # The ID of the credential\\"s subject.
        self.credential_subject_id = credential_subject_id
        # The type of the credential\\"s subject. Valid value:
        # 
        # - `authentication_token_provider`: An authentication token provider.
        self.credential_subject_type = credential_subject_type
        # The type of the credential. Valid values:
        # 
        # - `api_key`: An API key.
        # 
        # - `oauth_client`: An OAuth client.
        self.credential_type = credential_type
        # The description of the credential.
        self.description = description
        self.exclusive_user_id = exclusive_user_id
        # The ID of the EIAM instance.
        self.instance_id = instance_id
        # The status of the credential. Valid values:
        # 
        # - `enabled`: The credential is enabled.
        # 
        # - `disabled`: The credential is disabled.
        self.status = status
        # The time the credential was last updated, provided as a Unix timestamp in milliseconds.
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

        if self.credential_external_id is not None:
            result['CredentialExternalId'] = self.credential_external_id

        if self.credential_id is not None:
            result['CredentialId'] = self.credential_id

        if self.credential_identifier is not None:
            result['CredentialIdentifier'] = self.credential_identifier

        if self.credential_name is not None:
            result['CredentialName'] = self.credential_name

        if self.credential_scenario_label is not None:
            result['CredentialScenarioLabel'] = self.credential_scenario_label

        if self.credential_sharing_scope is not None:
            result['CredentialSharingScope'] = self.credential_sharing_scope

        if self.credential_subject_id is not None:
            result['CredentialSubjectId'] = self.credential_subject_id

        if self.credential_subject_type is not None:
            result['CredentialSubjectType'] = self.credential_subject_type

        if self.credential_type is not None:
            result['CredentialType'] = self.credential_type

        if self.description is not None:
            result['Description'] = self.description

        if self.exclusive_user_id is not None:
            result['ExclusiveUserId'] = self.exclusive_user_id

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
            temp_model = main_models.ListCredentialsResponseBodyCredentialsCredentialContent()
            self.credential_content = temp_model.from_map(m.get('CredentialContent'))

        if m.get('CredentialCreationType') is not None:
            self.credential_creation_type = m.get('CredentialCreationType')

        if m.get('CredentialExternalId') is not None:
            self.credential_external_id = m.get('CredentialExternalId')

        if m.get('CredentialId') is not None:
            self.credential_id = m.get('CredentialId')

        if m.get('CredentialIdentifier') is not None:
            self.credential_identifier = m.get('CredentialIdentifier')

        if m.get('CredentialName') is not None:
            self.credential_name = m.get('CredentialName')

        if m.get('CredentialScenarioLabel') is not None:
            self.credential_scenario_label = m.get('CredentialScenarioLabel')

        if m.get('CredentialSharingScope') is not None:
            self.credential_sharing_scope = m.get('CredentialSharingScope')

        if m.get('CredentialSubjectId') is not None:
            self.credential_subject_id = m.get('CredentialSubjectId')

        if m.get('CredentialSubjectType') is not None:
            self.credential_subject_type = m.get('CredentialSubjectType')

        if m.get('CredentialType') is not None:
            self.credential_type = m.get('CredentialType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExclusiveUserId') is not None:
            self.exclusive_user_id = m.get('ExclusiveUserId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class ListCredentialsResponseBodyCredentialsCredentialContent(DaraModel):
    def __init__(
        self,
        oauth_client_content: main_models.ListCredentialsResponseBodyCredentialsCredentialContentOAuthClientContent = None,
    ):
        # The content of an OAuth client credential.
        self.oauth_client_content = oauth_client_content

    def validate(self):
        if self.oauth_client_content:
            self.oauth_client_content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.oauth_client_content is not None:
            result['OAuthClientContent'] = self.oauth_client_content.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OAuthClientContent') is not None:
            temp_model = main_models.ListCredentialsResponseBodyCredentialsCredentialContentOAuthClientContent()
            self.oauth_client_content = temp_model.from_map(m.get('OAuthClientContent'))

        return self

class ListCredentialsResponseBodyCredentialsCredentialContentOAuthClientContent(DaraModel):
    def __init__(
        self,
        client_id: str = None,
    ):
        # The client ID of the OAuth client.
        self.client_id = client_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_id is not None:
            result['ClientId'] = self.client_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        return self

