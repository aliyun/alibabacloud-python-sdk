# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiworkspace20210204 import models as main_models
from darabonba.model import DaraModel

class ListDatasetFileMetasResponseBody(DaraModel):
    def __init__(
        self,
        dataset_file_metas: List[main_models.DatasetFileMeta] = None,
        dataset_id: str = None,
        dataset_version: str = None,
        max_results: int = None,
        next_token: str = None,
        page_size: int = None,
        total_count: int = None,
        workspace_id: str = None,
    ):
        # The metadata records of the dataset files.
        self.dataset_file_metas = dataset_file_metas
        # The dataset ID.
        self.dataset_id = dataset_id
        # The dataset version.
        self.dataset_version = dataset_version
        self.max_results = max_results
        # The pagination token. If the number of results exceeds the maximum number of entries allowed per page, a pagination token is returned. This token can be used as an input parameter to obtain the next page of results. If all results are obtained, no token is returned.
        self.next_token = next_token
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        if self.dataset_file_metas:
            for v1 in self.dataset_file_metas:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DatasetFileMetas'] = []
        if self.dataset_file_metas is not None:
            for k1 in self.dataset_file_metas:
                result['DatasetFileMetas'].append(k1.to_map() if k1 else None)

        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id

        if self.dataset_version is not None:
            result['DatasetVersion'] = self.dataset_version

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dataset_file_metas = []
        if m.get('DatasetFileMetas') is not None:
            for k1 in m.get('DatasetFileMetas'):
                temp_model = main_models.DatasetFileMeta()
                self.dataset_file_metas.append(temp_model.from_map(k1))

        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')

        if m.get('DatasetVersion') is not None:
            self.dataset_version = m.get('DatasetVersion')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

