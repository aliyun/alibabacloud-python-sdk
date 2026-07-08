# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateGeneralConfigRequest(DaraModel):
    def __init__(
        self,
        config_key: str = None,
        config_value: str = None,
        workspace_id: str = None,
    ):
        # The unique identifier of the configuration item. The following configurations are supported:
        # 
        # - Text search threshold for data sources (double): \\`searchGenerate.searchTextMinScore\\`
        # 
        # - Image search threshold for data sources (double): \\`searchGenerate.searchImageMinScore\\`
        # 
        # - Video search threshold for data sources (double): \\`searchGenerate.searchVideoMinScore\\`
        # 
        # - Audio search threshold for data sources (double): \\`searchGenerate.searchAudioMinScore\\`
        # 
        # - Plain text prompt template for answer summarization in general Q\\&A search (string): \\`searchGenerate.sumQaAgentPrompt\\`
        # 
        # - Text and image prompt template for answer summarization in general Q\\&A search (string): \\`searchGenerate.sumQaAgentVlPrompt\\`
        # 
        # - Plain text prompt template for answer summarization in enhanced Q\\&A search (string): \\`searchGenerate.sumQaEnhanceAgentPrompt\\`
        # 
        # - Text and image prompt template for answer summarization in enhanced Q\\&A search (string): \\`searchGenerate.sumQaEnhanceAgentVlPrompt\\`
        # 
        # This parameter is required.
        self.config_key = config_key
        # The value of the configuration item.
        # 
        # This parameter is required.
        self.config_value = config_value
        # The unique identifier of the Model Studio workspace. For more information, see [Get a workspaceId](https://help.aliyun.com/document_detail/2782167.html).
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_key is not None:
            result['ConfigKey'] = self.config_key

        if self.config_value is not None:
            result['ConfigValue'] = self.config_value

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigKey') is not None:
            self.config_key = m.get('ConfigKey')

        if m.get('ConfigValue') is not None:
            self.config_value = m.get('ConfigValue')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

