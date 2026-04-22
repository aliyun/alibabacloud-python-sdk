# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListAgentSessionArtifactsResponseBody(DaraModel):
    def __init__(
        self,
        json_rpc_response: main_models.ListAgentSessionArtifactsResponseBodyJsonRpcResponse = None,
        request_id: str = None,
    ):
        self.json_rpc_response = json_rpc_response
        # Id of the request
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
            temp_model = main_models.ListAgentSessionArtifactsResponseBodyJsonRpcResponse()
            self.json_rpc_response = temp_model.from_map(m.get('JsonRpcResponse'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListAgentSessionArtifactsResponseBodyJsonRpcResponse(DaraModel):
    def __init__(
        self,
        id: str = None,
        jsonrpc: str = None,
        result: main_models.ListAgentSessionArtifactsResponseBodyJsonRpcResponseResult = None,
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
            temp_model = main_models.ListAgentSessionArtifactsResponseBodyJsonRpcResponseResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class ListAgentSessionArtifactsResponseBodyJsonRpcResponseResult(DaraModel):
    def __init__(
        self,
        artifacts: List[main_models.ListAgentSessionArtifactsResponseBodyJsonRpcResponseResultArtifacts] = None,
        max_results: int = None,
        next_token: str = None,
    ):
        self.artifacts = artifacts
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        if self.artifacts:
            for v1 in self.artifacts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Artifacts'] = []
        if self.artifacts is not None:
            for k1 in self.artifacts:
                result['Artifacts'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.artifacts = []
        if m.get('Artifacts') is not None:
            for k1 in m.get('Artifacts'):
                temp_model = main_models.ListAgentSessionArtifactsResponseBodyJsonRpcResponseResultArtifacts()
                self.artifacts.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

class ListAgentSessionArtifactsResponseBodyJsonRpcResponseResultArtifacts(DaraModel):
    def __init__(
        self,
        artifact_name: str = None,
        artifact_path: str = None,
        artifact_type: str = None,
    ):
        self.artifact_name = artifact_name
        self.artifact_path = artifact_path
        self.artifact_type = artifact_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.artifact_name is not None:
            result['ArtifactName'] = self.artifact_name

        if self.artifact_path is not None:
            result['ArtifactPath'] = self.artifact_path

        if self.artifact_type is not None:
            result['ArtifactType'] = self.artifact_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactName') is not None:
            self.artifact_name = m.get('ArtifactName')

        if m.get('ArtifactPath') is not None:
            self.artifact_path = m.get('ArtifactPath')

        if m.get('ArtifactType') is not None:
            self.artifact_type = m.get('ArtifactType')

        return self

