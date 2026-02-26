# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class ContextualRetrievalRequest(DaraModel):
    def __init__(
        self,
        dataset_name: str = None,
        messages: List[main_models.ContextualMessage] = None,
        project_name: str = None,
        recall_only: bool = None,
        smart_cluster_ids: List[str] = None,
    ):
        # The dataset.
        # 
        # This parameter is required.
        self.dataset_name = dataset_name
        # The conversation or tool invocation history. The latest message is at the end of the list (with an index number of n-1), whereas the earliest message is at the beginning of the list (with an index number of 0). Historical messages must be provided in user-assistant pairs. The maximum number of messages that you can specify is 2\\*n+1. The current question cannot exceed 1,000 characters in length. The maximum number of historical messages allowed is 100.
        # 
        # This parameter is required.
        self.messages = messages
        # The name of the project. For more information, see [CreateProject](https://help.aliyun.com/zh/imm/getting-started/create-a-project-1?spm=a2c4g.11186623.help-menu-search-62354.d_0).
        # 
        # This parameter is required.
        self.project_name = project_name
        # Indicates whether to enable recall-only (embedding-based search). If you set this parameter to true, returned results have not been re-ranked and can be ranked in custom order. Default value: false.
        self.recall_only = recall_only
        # The IDs of clusters from which results are retrieved.
        self.smart_cluster_ids = smart_cluster_ids

    def validate(self):
        if self.messages:
            for v1 in self.messages:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name

        result['Messages'] = []
        if self.messages is not None:
            for k1 in self.messages:
                result['Messages'].append(k1.to_map() if k1 else None)

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.recall_only is not None:
            result['RecallOnly'] = self.recall_only

        if self.smart_cluster_ids is not None:
            result['SmartClusterIds'] = self.smart_cluster_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        self.messages = []
        if m.get('Messages') is not None:
            for k1 in m.get('Messages'):
                temp_model = main_models.ContextualMessage()
                self.messages.append(temp_model.from_map(k1))

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('RecallOnly') is not None:
            self.recall_only = m.get('RecallOnly')

        if m.get('SmartClusterIds') is not None:
            self.smart_cluster_ids = m.get('SmartClusterIds')

        return self

