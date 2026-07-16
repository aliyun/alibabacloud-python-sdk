# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListBindingsRequest(DaraModel):
    def __init__(
        self,
        dataset_name: str = None,
        max_results: int = None,
        name: str = None,
        next_token: str = None,
        project_name: str = None,
    ):
        # The dataset name. For information about how to obtain the dataset name, see [CreateDataset](https://help.aliyun.com/document_detail/478160.html).
        self.dataset_name = dataset_name
        # - The maximum number of bindings to return. Valid values: 0 to 200.
        # - If this parameter is not set or is set to 0, the default value 100 is used.
        self.max_results = max_results
        # The name of the binding task.
        self.name = name
        # - The pagination token that is used when the total number of bindings exceeds the MaxResults value.
        # - Binding information is returned in alphabetical order starting from the NextToken value.
        # - Leave this parameter empty for the first request.
        self.next_token = next_token
        # The project name. For information about how to obtain the project name, see [CreateProject](https://help.aliyun.com/document_detail/478153.html).
        # 
        # This parameter is required.
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.name is not None:
            result['Name'] = self.name

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        return self

