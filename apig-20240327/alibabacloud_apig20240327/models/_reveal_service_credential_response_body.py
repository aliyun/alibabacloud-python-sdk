# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class RevealServiceCredentialResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.RevealServiceCredentialResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code. The value is Ok if the request is successful.
        self.code = code
        # The currently active credential data.
        self.data = data
        # The response message. The value is success if the request is successful.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.RevealServiceCredentialResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class RevealServiceCredentialResponseBodyData(DaraModel):
    def __init__(
        self,
        config_revision: str = None,
        credential: main_models.RevealServiceCredentialResponseBodyDataCredential = None,
        credential_type: str = None,
        provider: str = None,
        service_id: str = None,
    ):
        # The current configuration revision. The value is legacy for historical objects.
        self.config_revision = config_revision
        # The credential object of the currently active type. Only the fields corresponding to the credentialType are populated.
        self.credential = credential
        # The currently active credential type. Valid values: apiKey, bedrock, vertex, and kling.
        self.credential_type = credential_type
        # The name of the provider, such as qwen, openai, bedrock, vertex, kling, or pai-eas.
        self.provider = provider
        # The unique ID of the service.
        self.service_id = service_id

    def validate(self):
        if self.credential:
            self.credential.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_revision is not None:
            result['configRevision'] = self.config_revision

        if self.credential is not None:
            result['credential'] = self.credential.to_map()

        if self.credential_type is not None:
            result['credentialType'] = self.credential_type

        if self.provider is not None:
            result['provider'] = self.provider

        if self.service_id is not None:
            result['serviceId'] = self.service_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configRevision') is not None:
            self.config_revision = m.get('configRevision')

        if m.get('credential') is not None:
            temp_model = main_models.RevealServiceCredentialResponseBodyDataCredential()
            self.credential = temp_model.from_map(m.get('credential'))

        if m.get('credentialType') is not None:
            self.credential_type = m.get('credentialType')

        if m.get('provider') is not None:
            self.provider = m.get('provider')

        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')

        return self

class RevealServiceCredentialResponseBodyDataCredential(DaraModel):
    def __init__(
        self,
        api_key_generate_mode: str = None,
        api_key_references: List[str] = None,
        api_keys: List[str] = None,
        aws_access_key: str = None,
        aws_region: str = None,
        aws_secret_key: str = None,
        credential_source: str = None,
        endpoint_mode: str = None,
        kling_access_key: str = None,
        kling_secret_key: str = None,
        vertex_auth_key: str = None,
        vertex_project_id: str = None,
        vertex_region: str = None,
    ):
        # The API key generation mode. Valid values: Custom and Reference. Historical null values are treated as Custom.
        self.api_key_generate_mode = api_key_generate_mode
        # The list of Key Management Service (KMS) reference names. This parameter is returned only in Reference mode. The reference values are not returned.
        self.api_key_references = api_key_references
        # The list of custom API keys. This parameter is returned only when apiKeyGenerateMode is set to Custom. The keys are returned in the original order without deduplication.
        self.api_keys = api_keys
        # The AWS access key ID for Bedrock.
        self.aws_access_key = aws_access_key
        # The AWS region for Bedrock.
        self.aws_region = aws_region
        # The AWS secret access key for Bedrock.
        self.aws_secret_key = aws_secret_key
        # The source of the credential. The value is pai-eas when the credential is backfilled by the PAI-EAS system.
        self.credential_source = credential_source
        # The Bedrock endpoint mode. The value is runtime for historical null values.
        self.endpoint_mode = endpoint_mode
        # The access key ID for Kling.
        self.kling_access_key = kling_access_key
        # The secret access key for Kling.
        self.kling_secret_key = kling_secret_key
        # The original JSON text of the Vertex service account. The text is neither parsed nor reordered.
        self.vertex_auth_key = vertex_auth_key
        # The Vertex project ID.
        self.vertex_project_id = vertex_project_id
        # The region for Vertex.
        self.vertex_region = vertex_region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key_generate_mode is not None:
            result['apiKeyGenerateMode'] = self.api_key_generate_mode

        if self.api_key_references is not None:
            result['apiKeyReferences'] = self.api_key_references

        if self.api_keys is not None:
            result['apiKeys'] = self.api_keys

        if self.aws_access_key is not None:
            result['awsAccessKey'] = self.aws_access_key

        if self.aws_region is not None:
            result['awsRegion'] = self.aws_region

        if self.aws_secret_key is not None:
            result['awsSecretKey'] = self.aws_secret_key

        if self.credential_source is not None:
            result['credentialSource'] = self.credential_source

        if self.endpoint_mode is not None:
            result['endpointMode'] = self.endpoint_mode

        if self.kling_access_key is not None:
            result['klingAccessKey'] = self.kling_access_key

        if self.kling_secret_key is not None:
            result['klingSecretKey'] = self.kling_secret_key

        if self.vertex_auth_key is not None:
            result['vertexAuthKey'] = self.vertex_auth_key

        if self.vertex_project_id is not None:
            result['vertexProjectId'] = self.vertex_project_id

        if self.vertex_region is not None:
            result['vertexRegion'] = self.vertex_region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiKeyGenerateMode') is not None:
            self.api_key_generate_mode = m.get('apiKeyGenerateMode')

        if m.get('apiKeyReferences') is not None:
            self.api_key_references = m.get('apiKeyReferences')

        if m.get('apiKeys') is not None:
            self.api_keys = m.get('apiKeys')

        if m.get('awsAccessKey') is not None:
            self.aws_access_key = m.get('awsAccessKey')

        if m.get('awsRegion') is not None:
            self.aws_region = m.get('awsRegion')

        if m.get('awsSecretKey') is not None:
            self.aws_secret_key = m.get('awsSecretKey')

        if m.get('credentialSource') is not None:
            self.credential_source = m.get('credentialSource')

        if m.get('endpointMode') is not None:
            self.endpoint_mode = m.get('endpointMode')

        if m.get('klingAccessKey') is not None:
            self.kling_access_key = m.get('klingAccessKey')

        if m.get('klingSecretKey') is not None:
            self.kling_secret_key = m.get('klingSecretKey')

        if m.get('vertexAuthKey') is not None:
            self.vertex_auth_key = m.get('vertexAuthKey')

        if m.get('vertexProjectId') is not None:
            self.vertex_project_id = m.get('vertexProjectId')

        if m.get('vertexRegion') is not None:
            self.vertex_region = m.get('vertexRegion')

        return self

