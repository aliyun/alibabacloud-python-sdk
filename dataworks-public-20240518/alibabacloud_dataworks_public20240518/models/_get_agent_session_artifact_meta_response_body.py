# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class GetAgentSessionArtifactMetaResponseBody(DaraModel):
    def __init__(
        self,
        json_rpc_response: main_models.GetAgentSessionArtifactMetaResponseBodyJsonRpcResponse = None,
        request_id: str = None,
    ):
        self.json_rpc_response = json_rpc_response
        self.request_id = request_id

    def validate(self):
        if self.json_rpc_response:
            self.json_rpc_response.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.json_rpc_response is not None:
            result['JsonRpcResponse'] = self.json_rpc_response.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JsonRpcResponse') is not None:
            temp_model = main_models.GetAgentSessionArtifactMetaResponseBodyJsonRpcResponse()
            self.json_rpc_response = temp_model.from_map(m.get('JsonRpcResponse'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetAgentSessionArtifactMetaResponseBodyJsonRpcResponse(DaraModel):
    def __init__(
        self,
        id: str = None,
        jsonrpc: str = None,
        result: main_models.GetAgentSessionArtifactMetaResponseBodyJsonRpcResponseResult = None,
    ):
        self.id = id
        self.jsonrpc = jsonrpc
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.jsonrpc is not None:
            result['Jsonrpc'] = self.jsonrpc

        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Jsonrpc') is not None:
            self.jsonrpc = m.get('Jsonrpc')

        if m.get('Result') is not None:
            temp_model = main_models.GetAgentSessionArtifactMetaResponseBodyJsonRpcResponseResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class GetAgentSessionArtifactMetaResponseBodyJsonRpcResponseResult(DaraModel):
    def __init__(
        self,
        artifact_content: str = None,
        artifact_name: str = None,
        artifact_path: str = None,
    ):
        self.artifact_content = artifact_content
        self.artifact_name = artifact_name
        self.artifact_path = artifact_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.artifact_content is not None:
            result['ArtifactContent'] = self.artifact_content

        if self.artifact_name is not None:
            result['ArtifactName'] = self.artifact_name

        if self.artifact_path is not None:
            result['ArtifactPath'] = self.artifact_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactContent') is not None:
            self.artifact_content = m.get('ArtifactContent')

        if m.get('ArtifactName') is not None:
            self.artifact_name = m.get('ArtifactName')

        if m.get('ArtifactPath') is not None:
            self.artifact_path = m.get('ArtifactPath')

        return self

