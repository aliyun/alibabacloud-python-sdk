# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SimpleQueryShrinkRequest(DaraModel):
    def __init__(
        self,
        aggregations_shrink: str = None,
        dataset_name: str = None,
        max_results: int = None,
        next_token: str = None,
        order: str = None,
        project_name: str = None,
        query_shrink: str = None,
        sort: str = None,
        with_fields_shrink: str = None,
        without_total_hits: bool = None,
    ):
        # The list of aggregation field information.
        # >Notice: When you use an aggregation query, only the aggregation results are returned, and the list of matched metadata is not returned.</notice>
        self.aggregations_shrink = aggregations_shrink
        # The name of the dataset. For more information about how to obtain the dataset name, see [Create a dataset](https://help.aliyun.com/document_detail/478160.html).
        # 
        # This parameter is required.
        self.dataset_name = dataset_name
        # - When you perform a query for files without specifying the Aggregations parameter, this parameter specifies the maximum number of files to return. Valid values: 0 to 100.
        # 
        # - When you specify the Aggregations parameter for aggregation statistics, this parameter specifies the maximum number of groups to return. Valid values: 0 to 2000.
        # 
        # - If you do not specify this parameter or set it to 0, the default value is 100.
        self.max_results = max_results
        # The token used for pagination when the total number of files exceeds the value of MaxResults.
        # 
        # The list of files is returned in lexicographical order starting from NextToken.
        # 
        # Set this parameter to empty when you call this operation for the first time.
        self.next_token = next_token
        # The sort order of the sort fields. Valid values:
        # 
        # - asc: ascending order
        # 
        # - desc: descending order (default)
        # >- You can separate multiple sort orders with commas (,), for example, asc,desc.
        # > - The number of sort orders cannot exceed the number of sort fields. That is, the number of elements in the Order parameter must be less than or equal to the number of elements in the Sort parameter. For example, if Sort is set to Size,Filename, Order can be set to "asc,desc".
        # > - If the number of sort orders is less than the number of sort fields, the default sort order for the unspecified fields is desc. For example, if Sort is set to Size,Filename and Order is set to asc, the default sort order for Filename is desc, which means descending order.
        self.order = order
        # The name of the project. For more information about how to obtain the project name, see [Create a project](https://help.aliyun.com/document_detail/478153.html).
        # 
        # This parameter is required.
        self.project_name = project_name
        # The simple query conditions. Click the link on the left to view details.
        self.query_shrink = query_shrink
        # The list of sort fields. For more information, see [Supported fields and operators](https://help.aliyun.com/document_detail/2743991.html).
        # > - You can separate multiple sort fields with commas (,), for example, Size,Filename.
        # > - You can specify a maximum of 5 sort fields.
        # > - The order of the sort fields determines the sorting priority.
        self.sort = sort
        # Specifies the specific fields to return instead of all existing metadata fields. This can be used to reduce the size of the returned struct.
        # 
        # If you do not specify this parameter or leave it empty, all fields are returned.
        self.with_fields_shrink = with_fields_shrink
        # Specifies whether to return the total number of matched records. Valid values:
        # - true: The TotalHits field is not returned.
        # - false: The TotalHits field is returned.
        self.without_total_hits = without_total_hits

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aggregations_shrink is not None:
            result['Aggregations'] = self.aggregations_shrink

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

        if self.query_shrink is not None:
            result['Query'] = self.query_shrink

        if self.sort is not None:
            result['Sort'] = self.sort

        if self.with_fields_shrink is not None:
            result['WithFields'] = self.with_fields_shrink

        if self.without_total_hits is not None:
            result['WithoutTotalHits'] = self.without_total_hits

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Aggregations') is not None:
            self.aggregations_shrink = m.get('Aggregations')

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

        if m.get('Query') is not None:
            self.query_shrink = m.get('Query')

        if m.get('Sort') is not None:
            self.sort = m.get('Sort')

        if m.get('WithFields') is not None:
            self.with_fields_shrink = m.get('WithFields')

        if m.get('WithoutTotalHits') is not None:
            self.without_total_hits = m.get('WithoutTotalHits')

        return self

