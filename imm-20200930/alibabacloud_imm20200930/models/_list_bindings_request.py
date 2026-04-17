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
        # The name of the dataset.[](~~478160~~)
        self.dataset_name = dataset_name
        # *   The maximum number of bindings to return. Valid values: 0 to 200.
        # *   If you do not specify this parameter or set the parameter to 0, the default value of 100 is used.
        self.max_results = max_results
        self.name = name
        # *   The pagination token that is used in the next request to retrieve a new page of results if the total number of results exceeds the value of the MaxResults parameter.
        # *   The next call to the operation returns results lexicographically after the NextToken parameter value.
        # *   You do not need to specify this parameter in your initial request.
        self.next_token = next_token
        # The name of the project.[](~~478153~~)
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

