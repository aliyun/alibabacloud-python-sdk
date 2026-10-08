# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ContextualRetrievalShrinkRequest(DaraModel):
    def __init__(
        self,
        dataset_name: str = None,
        messages_shrink: str = None,
        project_name: str = None,
        recall_only: bool = None,
        smart_cluster_ids_shrink: str = None,
    ):
        # The dataset used for retrieval.
        # 
        # This parameter is required.
        self.dataset_name = dataset_name
        # The conversation history and tool calling history. The latest message is at the end (index n-1), and the oldest message is at the beginning (index 0). The messages must be in user-assistant pairs, with a total count of 2*n+1, and the length of the latest question cannot exceed 1,000 characters. The conversation history is limited to 100 messages.
        # 
        # This parameter is required.
        self.messages_shrink = messages_shrink
        # The name of the project. For more information about how to obtain the project name, see [Create a project](https://www.alibabacloud.com/help/en/imm/getting-started/create-a-project-1).
        # 
        # This parameter is required.
        self.project_name = project_name
        # Specifies whether to enable only the recall process (embedding search). If this parameter is set to true, the returned data is not reranked, which allows you to customize the reranking process. Default value: false.
        self.recall_only = recall_only
        # The list of smart cluster IDs, which are used to retrieve files within specific smart clusters.
        self.smart_cluster_ids_shrink = smart_cluster_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name

        if self.messages_shrink is not None:
            result['Messages'] = self.messages_shrink

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.recall_only is not None:
            result['RecallOnly'] = self.recall_only

        if self.smart_cluster_ids_shrink is not None:
            result['SmartClusterIds'] = self.smart_cluster_ids_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        if m.get('Messages') is not None:
            self.messages_shrink = m.get('Messages')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('RecallOnly') is not None:
            self.recall_only = m.get('RecallOnly')

        if m.get('SmartClusterIds') is not None:
            self.smart_cluster_ids_shrink = m.get('SmartClusterIds')

        return self

