# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class GetPluginWorkspaceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetPluginWorkspaceResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response status code.
        self.code = code
        # The response data.
        self.data = data
        # The response message.
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
            temp_model = main_models.GetPluginWorkspaceResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetPluginWorkspaceResponseBodyData(DaraModel):
    def __init__(
        self,
        organization_id: str = None,
        pipeline_run_id: str = None,
        repo_id: str = None,
        repo_name: str = None,
        wasm_url: str = None,
        workspace_id: str = None,
    ):
        # The Codeup organization ID.
        self.organization_id = organization_id
        # The ID of the most recent pipeline run. This parameter is not returned if the plugin has never been built.
        self.pipeline_run_id = pipeline_run_id
        # The Codeup repository ID.
        self.repo_id = repo_id
        # The repository name (the English ID of the plugin).
        self.repo_name = repo_name
        # The OSS download URL of the compiled WASM build output. This parameter is returned only when the pipeline status is SUCCESS.
        self.wasm_url = wasm_url
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.organization_id is not None:
            result['organizationId'] = self.organization_id

        if self.pipeline_run_id is not None:
            result['pipelineRunId'] = self.pipeline_run_id

        if self.repo_id is not None:
            result['repoId'] = self.repo_id

        if self.repo_name is not None:
            result['repoName'] = self.repo_name

        if self.wasm_url is not None:
            result['wasmUrl'] = self.wasm_url

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('organizationId') is not None:
            self.organization_id = m.get('organizationId')

        if m.get('pipelineRunId') is not None:
            self.pipeline_run_id = m.get('pipelineRunId')

        if m.get('repoId') is not None:
            self.repo_id = m.get('repoId')

        if m.get('repoName') is not None:
            self.repo_name = m.get('repoName')

        if m.get('wasmUrl') is not None:
            self.wasm_url = m.get('wasmUrl')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

