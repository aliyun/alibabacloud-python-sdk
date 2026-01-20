# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetLLMConfigResponseBody(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        base_url: str = None,
        batch_size: int = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        llmconfig_id: str = None,
        max_tokens: int = None,
        model: str = None,
        name: str = None,
        request_id: str = None,
        rps: int = None,
        workspace_id: str = None,
    ):
        self.api_key = api_key
        self.base_url = base_url
        self.batch_size = batch_size
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.llmconfig_id = llmconfig_id
        self.max_tokens = max_tokens
        self.model = model
        self.name = name
        # Id of the request
        self.request_id = request_id
        self.rps = rps
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['ApiKey'] = self.api_key

        if self.base_url is not None:
            result['BaseUrl'] = self.base_url

        if self.batch_size is not None:
            result['BatchSize'] = self.batch_size

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.llmconfig_id is not None:
            result['LLMConfigId'] = self.llmconfig_id

        if self.max_tokens is not None:
            result['MaxTokens'] = self.max_tokens

        if self.model is not None:
            result['Model'] = self.model

        if self.name is not None:
            result['Name'] = self.name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.rps is not None:
            result['Rps'] = self.rps

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')

        if m.get('BaseUrl') is not None:
            self.base_url = m.get('BaseUrl')

        if m.get('BatchSize') is not None:
            self.batch_size = m.get('BatchSize')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('LLMConfigId') is not None:
            self.llmconfig_id = m.get('LLMConfigId')

        if m.get('MaxTokens') is not None:
            self.max_tokens = m.get('MaxTokens')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Rps') is not None:
            self.rps = m.get('Rps')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

