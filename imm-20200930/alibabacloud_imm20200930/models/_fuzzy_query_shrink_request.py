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
        # The name of the dataset. For more information about how to obtain the dataset name, see [Create a dataset](https://help.aliyun.com/document_detail/478160.html).
        # 
        # This parameter is required.
        self.dataset_name = dataset_name
        # The maximum number of files to return. Valid values: 0 to 200.
        # 
        # If you do not set this parameter or set it to 0, the default value is 100.
        self.max_results = max_results
        # The token used for pagination when the total number of files exceeds the value of MaxResults.
        # 
        # The list of file information is returned in lexicographical order starting from NextToken.
        # 
        # Set this parameter to empty when you call this operation for the first time.
        self.next_token = next_token
        # The sort order of the sort fields. Valid values:
        # 
        # - asc: Ascending order.
        # 
        # - desc: Descending order. This is the default value.
        # 
        # > - You can separate multiple sort orders with commas (,), such as asc,desc.
        # > - The number of sort orders cannot exceed the number of sort fields. That is, the number of elements in the Order parameter must be less than or equal to the number of elements in the Sort parameter. For example, if Sort is set to Size,Filename, Order can be set to desc or asc.
        # > - If the number of sort orders is less than the number of sort fields, the default sort order for the unspecified fields is asc. For example, if Sort is set to Size,Filename and Order is set to asc, the default sort order for Filename is asc, which means ascending order.
        self.order = order
        # The name of the project. For more information about how to obtain the project name, see [Create a project](https://help.aliyun.com/document_detail/478153.html).
        # 
        # This parameter is required.
        self.project_name = project_name
        # The string used for the query. The string cannot exceed 1 MB in size.
        # 
        # This parameter is required.
        self.query = query
        # The list of fields by which to sort the results. For more information, see the [list of supported fields and operators](https://help.aliyun.com/document_detail/2743991.html).
        # 
        # - You can separate multiple sort fields with commas (,), such as `Size,Filename`.
        # 
        # - You can specify up to 5 sort fields.
        # 
        # - The order of the sort fields determines the sorting priority.
        self.sort = sort
        # Specifies the fields to return. Only the values of the specified fields are returned instead of all existing metadata fields. You can use this parameter to reduce the size of the returned struct.
        # 
        # If you do not specify this parameter or leave it empty, all fields are returned.
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

