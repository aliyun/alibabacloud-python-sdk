# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateGeneralConfigRequest(DaraModel):
    def __init__(
        self,
        config_key: str = None,
        config_value: str = None,
        workspace_id: str = None,
    ):
        # Unique identifier of the configuration item. Supported keys include the following:
        # 
        # - MiaoSou text search threshold (double): searchGenerate.searchTextMinScore
        # 
        # - MiaoSou image search threshold (double): searchGenerate.searchImageMinScore
        # 
        # - MiaoSou video search threshold (double): searchGenerate.searchVideoMinScore
        # 
        # - MiaoSou audio search threshold (double): searchGenerate.searchAudioMinScore
        # 
        # - MiaoSou Q\\&A search general answer summary prompt template (string): searchGenerate.sumQaAgentPrompt
        # 
        # - MiaoSou Q\\&A search general answer summary prompt template with text and images (string): searchGenerate.sumQaAgentVlPrompt
        # 
        # - MiaoSou Q\\&A search deep answer summary prompt template (string): searchGenerate.sumQaEnhanceAgentPrompt
        # 
        # - MiaoSou Q\\&A search deep answer summary prompt template with text and images (string): searchGenerate.sumQaEnhanceAgentVlPrompt
        # 
        # This parameter is required.
        self.config_key = config_key
        # Value of the configuration item
        # 
        # This parameter is required.
        self.config_value = config_value
        # Unique identifier of the Model Studio workspace. [Get the workspace ID](https://help.aliyun.com/document_detail/2782167.html)
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

