# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FuzzyQueryShrinkRequest(DaraModel):
    def __init__(
        self,
        dataset_name: str = None,
        max_results: int = None,
        next_token: str = None,
        order: str = None,
        project_name: str = None,
        query: str = None,
        sort: str = None,
        with_fields_shrink: str = None,
    ):
        # The name of the dataset. You can obtain the name of the dataset from the response of the [CreateDataset](https://help.aliyun.com/document_detail/478160.html) operation.
        # 
        # This parameter is required.
        self.dataset_name = dataset_name
        # The maximum number of entries to return. Valid values: 0 to 200.
        # 
        # Default value: 100.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. If the total number of files is greater than the value of MaxResults, you must specify NextToken.
        # 
        # The file information is returned in alphabetical order starting from the value of NextToken.
        # 
        # You do not need to specify this parameter for the first request.
        self.next_token = next_token
        # The sorting method. Valid values:
        # 
        # *   asc: ascending order.
        # *   desc (default): descending order.
        # 
        # > 
        # 
        # *   Separate multiple sorting methods with commas (,). Example: asc,desc.
        # 
        # *   The number of values for Order must be less than or equal to the number of values for Sort. For example, if you set Sort to Size,Filename, you can set Order only to desc or asc.
        # 
        # *   If the number of values for Order is less than the number of values for Sort, the unsorted fields are default to the value of asc. For example, if you set Sort to Size,Filename and Order to asc, the Filename field is default to the value of asc.
        self.order = order
        # The name of the project. You can obtain the name of the project from the response of the [CreateProject](https://help.aliyun.com/document_detail/478153.html) operation.
        # 
        # This parameter is required.
        self.project_name = project_name
        # The query content. The value can be up to 1 MB in size.
        # 
        # This parameter is required.
        self.query = query
        # The sort fields. For more information, see [Supported fields and operators](https://help.aliyun.com/document_detail/2743991.html).
        # 
        # *   Separate multiple sort fields with commas (,). Example: `Size,Filename`.
        # *   You can specify up to five sort fields.
        # *   The priority order of sorting is determined based on the order of the sort fields.
        self.sort = sort
        # The fields that you want to include in the response. To help reduce the size of the response, include only necessary metadata fields.
        # 
        # If you do not specify this parameter or set the value to null, all existing metadata fields are returned.
        self.with_fields_shrink = with_fields_shrink

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

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.order is not None:
            result['Order'] = self.order

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.query is not None:
            result['Query'] = self.query

        if self.sort is not None:
            result['Sort'] = self.sort

        if self.with_fields_shrink is not None:
            result['WithFields'] = self.with_fields_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
            self.query = m.get('Query')

        if m.get('Sort') is not None:
            self.sort = m.get('Sort')

        if m.get('WithFields') is not None:
            self.with_fields_shrink = m.get('WithFields')

        return self

