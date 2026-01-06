# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDatasetFileMetasStatisticsRequest(DaraModel):
    def __init__(
        self,
        aggregate_by: str = None,
        dataset_version: str = None,
        max_results: int = None,
        workspace_id: str = None,
    ):
        # Aggregates statistics based on the specified metadata field. The value is not case-sensitive. If not specified, the total number of dataset file metadata will be returned, instead of aggregation lists. Valid values:
        # 
        # *   filedir: the directory path of the file
        # *   file_type: the file type
        # *   tags.user: user-defined tag
        # *   tags.user-delete-ai-tags: algorithm tags deleted by the user
        # *   tags.ai: algorithm tags (aggregated by all tagging tasks)
        # *   tags.all: algorithm tags and user-defined tags (excluding alogorithm tags deleted by the user)
        self.aggregate_by = aggregate_by
        # The dataset version.
        # 
        # This parameter is required.
        self.dataset_version = dataset_version
        # The maximum number of results to be returned from a single query when the NextToken parameter is used in the query. Valid values: 1 to 100. Default value: 10.
        self.max_results = max_results
        # The workspace ID. You can call [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html) to obtain the workspace ID.
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
        if self.aggregate_by is not None:
            result['AggregateBy'] = self.aggregate_by

        if self.dataset_version is not None:
            result['DatasetVersion'] = self.dataset_version

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregateBy') is not None:
            self.aggregate_by = m.get('AggregateBy')

        if m.get('DatasetVersion') is not None:
            self.dataset_version = m.get('DatasetVersion')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

