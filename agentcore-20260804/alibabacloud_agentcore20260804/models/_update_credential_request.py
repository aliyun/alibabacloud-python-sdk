# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class UpdateCredentialRequest(DaraModel):
    def __init__(
        self,
        body: main_models.UpdateCredentialRequestBody = None,
        client_token: str = None,
    ):
        # The request body for updating the credential.
        self.body = body
        # Not supported.
        self.client_token = client_token

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body.to_map()

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = main_models.UpdateCredentialRequestBody()
            self.body = temp_model.from_map(m.get('body'))

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        return self

class UpdateCredentialRequestBody(DaraModel):
    def __init__(
        self,
        credential_metadata: str = None,
        description: str = None,
        resource_refs: List[main_models.UpdateCredentialRequestBodyResourceRefs] = None,
        resource_scope: str = None,
    ):
        # The new credential content, which is a JSON string. If credentialType is apiKey, this parameter can only contain the apiKey field, and the value cannot be empty. You must specify at least one of credentialMetadata and description.
        self.credential_metadata = credential_metadata
        # The new credential description, which can be up to 256 characters in length. You must specify at least one of credentialMetadata and description.
        self.description = description
        # If resourceScope is SPECIFIED, this parameter must be a non-empty array. Each item must include resourceType and resourceId. resourceName is optional.
        self.resource_refs = resource_refs
        # The application scope of the credential resources. A value of ALL indicates all resources. A value of SPECIFIED indicates only the resources specified by resourceRefs.
        self.resource_scope = resource_scope

    def validate(self):
        if self.resource_refs:
            for v1 in self.resource_refs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credential_metadata is not None:
            result['credentialMetadata'] = self.credential_metadata

        if self.description is not None:
            result['description'] = self.description

        result['resourceRefs'] = []
        if self.resource_refs is not None:
            for k1 in self.resource_refs:
                result['resourceRefs'].append(k1.to_map() if k1 else None)

        if self.resource_scope is not None:
            result['resourceScope'] = self.resource_scope

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('credentialMetadata') is not None:
            self.credential_metadata = m.get('credentialMetadata')

        if m.get('description') is not None:
            self.description = m.get('description')

        self.resource_refs = []
        if m.get('resourceRefs') is not None:
            for k1 in m.get('resourceRefs'):
                temp_model = main_models.UpdateCredentialRequestBodyResourceRefs()
                self.resource_refs.append(temp_model.from_map(k1))

        if m.get('resourceScope') is not None:
            self.resource_scope = m.get('resourceScope')

        return self

class UpdateCredentialRequestBodyResourceRefs(DaraModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
    ):
        # The unique identifier of the resource.
        self.resource_id = resource_id
        # The resource name. This parameter is empty if the resource is deleted.
        self.resource_name = resource_name
        # The resource type, such as agent.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id

        if self.resource_name is not None:
            result['resourceName'] = self.resource_name

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')

        if m.get('resourceName') is not None:
            self.resource_name = m.get('resourceName')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        return self

