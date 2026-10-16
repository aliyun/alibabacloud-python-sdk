# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class CreateCredentialRequest(DaraModel):
    def __init__(
        self,
        body: main_models.CreateCredentialRequestBody = None,
        client_token: str = None,
    ):
        # The request body for creating a credential.
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
            temp_model = main_models.CreateCredentialRequestBody()
            self.body = temp_model.from_map(m.get('body'))

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        return self

class CreateCredentialRequestBody(DaraModel):
    def __init__(
        self,
        credential_metadata: str = None,
        credential_type: str = None,
        description: str = None,
        name: str = None,
        resource_refs: List[main_models.CreateCredentialRequestBodyResourceRefs] = None,
        resource_scope: str = None,
    ):
        # The credential content, which is a JSON string. If credentialType is apiKey, this parameter can only contain the apiKey field, and the value cannot be empty. After the credential is written, only desensitized queries are supported.
        # 
        # This parameter is required.
        self.credential_metadata = credential_metadata
        # The credential type. Currently, only apiKey is supported.
        # 
        # This parameter is required.
        self.credential_type = credential_type
        # The description of the credential. The description can be up to 256 characters in length.
        self.description = description
        # The name of the credential. The name must be unique within the workspace, can only contain letters, digits, periods, underscores, and hyphens, and must be 3 to 128 characters in length. Runtime reserved names cannot be used.
        # 
        # This parameter is required.
        self.name = name
        # If resourceScope is SPECIFIED, this parameter must be a non-empty array. Each item must contain resourceType and resourceId. resourceName is optional.
        self.resource_refs = resource_refs
        # The application scope of the credential resource. A value of ALL indicates all resources. A value of SPECIFIED indicates that the credential is applied only to the resources specified by resourceRefs.
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

        if self.credential_type is not None:
            result['credentialType'] = self.credential_type

        if self.description is not None:
            result['description'] = self.description

        if self.name is not None:
            result['name'] = self.name

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

        if m.get('credentialType') is not None:
            self.credential_type = m.get('credentialType')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('name') is not None:
            self.name = m.get('name')

        self.resource_refs = []
        if m.get('resourceRefs') is not None:
            for k1 in m.get('resourceRefs'):
                temp_model = main_models.CreateCredentialRequestBodyResourceRefs()
                self.resource_refs.append(temp_model.from_map(k1))

        if m.get('resourceScope') is not None:
            self.resource_scope = m.get('resourceScope')

        return self

class CreateCredentialRequestBodyResourceRefs(DaraModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
    ):
        # The unique identifier of the resource.
        self.resource_id = resource_id
        # The name of the resource. This parameter is empty if the resource is deleted.
        self.resource_name = resource_name
        # The type of the resource, such as agent.
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

