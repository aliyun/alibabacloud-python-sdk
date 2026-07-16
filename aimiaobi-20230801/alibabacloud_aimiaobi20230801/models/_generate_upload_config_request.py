# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateUploadConfigRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        file_name: str = None,
        parent_dir: str = None,
    ):
        # The unique identifier of the workspace. For more information, see [AgentKey](https://help.aliyun.com/document_detail/2587494.html).
        # 
        # This parameter is required.
        self.agent_key = agent_key
        # The file name.
        self.file_name = file_name
        # The parent folder.
        # 
        # - materialDocument: The Material Library for AI Writing Assistant.
        # 
        # - datasetUpload: The dataset for AI Search.
        # 
        # - intervenes: Interventions.
        # 
        # - temp: A temporary upload folder. Files in this folder are released periodically.
        # 
        # This parameter is required.
        self.parent_dir = parent_dir

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.parent_dir is not None:
            result['ParentDir'] = self.parent_dir

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('ParentDir') is not None:
            self.parent_dir = m.get('ParentDir')

        return self

