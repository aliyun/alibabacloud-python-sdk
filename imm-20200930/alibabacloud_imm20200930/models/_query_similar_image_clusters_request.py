# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QuerySimilarImageClustersRequest(DaraModel):
    def __init__(
        self,
        custom_labels: str = None,
        dataset_name: str = None,
        max_results: int = None,
        next_token: str = None,
        order: str = None,
        project_name: str = None,
        sort: str = None,
    ):
        # The custom tags, which are used to filter tasks.
        self.custom_labels = custom_labels
        # The name of the dataset. For more information, see [Create a dataset](https://help.aliyun.com/document_detail/478160.html).
        # 
        # This parameter is required.
        self.dataset_name = dataset_name
        # The number of entries per page. Value range: 0 to 100. Default value: 100.
        self.max_results = max_results
        # The pagination token.
        # 
        # If the total number of clusters is greater than the value of MaxResults, you must specify this parameter. The next call to the operation returns results lexicographically after the NextToken parameter value.
        # 
        # >  The first time you call this operation in a query, set this parameter to null.
        self.next_token = next_token
        # The sorting order. Valid values:
        # 
        # *   asc: ascending order.
        # *   desc: descending order. This is the default value.
        self.order = order
        # The name of the project. For more information, see [CreateProject](https://help.aliyun.com/document_detail/478153.html).
        # 
        # This parameter is required.
        self.project_name = project_name
        # The sorting field.
        # 
        # *   CreateTime: the time when the clusters were created.
        # *   UpdateTime: the time when the clusters were updated. This is the default value.
        self.sort = sort

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels

        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.order is not None:
            result['Order'] = self.order

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.sort is not None:
            result['Sort'] = self.sort

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')

        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('Sort') is not None:
            self.sort = m.get('Sort')

        return self

