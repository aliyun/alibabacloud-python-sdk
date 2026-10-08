# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class SimpleQueryRequest(DaraModel):
    def __init__(
        self,
        aggregations: List[main_models.SimpleQueryRequestAggregations] = None,
        dataset_name: str = None,
        max_results: int = None,
        next_token: str = None,
        order: str = None,
        project_name: str = None,
        query: main_models.SimpleQuery = None,
        sort: str = None,
        with_fields: List[str] = None,
        without_total_hits: bool = None,
    ):
        # The list of aggregation field information.
        # >Notice: When you use an aggregation query, only the aggregation results are returned, and the list of matched metadata is not returned.</notice>
        self.aggregations = aggregations
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
        self.query = query
        # The list of sort fields. For more information, see [Supported fields and operators](https://help.aliyun.com/document_detail/2743991.html).
        # > - You can separate multiple sort fields with commas (,), for example, Size,Filename.
        # > - You can specify a maximum of 5 sort fields.
        # > - The order of the sort fields determines the sorting priority.
        self.sort = sort
        # Specifies the specific fields to return instead of all existing metadata fields. This can be used to reduce the size of the returned struct.
        # 
        # If you do not specify this parameter or leave it empty, all fields are returned.
        self.with_fields = with_fields
        # Specifies whether to return the total number of matched records. Valid values:
        # - true: The TotalHits field is not returned.
        # - false: The TotalHits field is returned.
        self.without_total_hits = without_total_hits

    def validate(self):
        if self.aggregations:
            for v1 in self.aggregations:
                 if v1:
                    v1.validate()
        if self.query:
            self.query.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Aggregations'] = []
        if self.aggregations is not None:
            for k1 in self.aggregations:
                result['Aggregations'].append(k1.to_map() if k1 else None)

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
            result['Query'] = self.query.to_map()

        if self.sort is not None:
            result['Sort'] = self.sort

        if self.with_fields is not None:
            result['WithFields'] = self.with_fields

        if self.without_total_hits is not None:
            result['WithoutTotalHits'] = self.without_total_hits

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.aggregations = []
        if m.get('Aggregations') is not None:
            for k1 in m.get('Aggregations'):
                temp_model = main_models.SimpleQueryRequestAggregations()
                self.aggregations.append(temp_model.from_map(k1))

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
            temp_model = main_models.SimpleQuery()
            self.query = temp_model.from_map(m.get('Query'))

        if m.get('Sort') is not None:
            self.sort = m.get('Sort')

        if m.get('WithFields') is not None:
            self.with_fields = m.get('WithFields')

        if m.get('WithoutTotalHits') is not None:
            self.without_total_hits = m.get('WithoutTotalHits')

        return self

class SimpleQueryRequestAggregations(DaraModel):
    def __init__(
        self,
        field: str = None,
        operation: str = None,
    ):
        # The name of the field. For more information about supported fields, see [Supported fields and operators](https://help.aliyun.com/document_detail/2743991.html).
        self.field = field
        # The operator for the aggregation field.
        self.operation = operation

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field is not None:
            result['Field'] = self.field

        if self.operation is not None:
            result['Operation'] = self.operation

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Field') is not None:
            self.field = m.get('Field')

        if m.get('Operation') is not None:
            self.operation = m.get('Operation')

        return self

