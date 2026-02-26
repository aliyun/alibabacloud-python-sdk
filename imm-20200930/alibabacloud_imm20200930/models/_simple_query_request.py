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
        # The aggregations.
        # 
        # >  If you perform an aggregate query, the aggregation returned in the response contains only statistical results, not the actual metadata.
        self.aggregations = aggregations
        # The name of the dataset.[](~~478160~~)
        # 
        # This parameter is required.
        self.dataset_name = dataset_name
        # *   If the Aggregations parameter is not specified, this parameter specifies the maximum number of files that can be returned. Valid values: 1 to 100.
        # *   If the Aggregations parameter is specified, this parameter specifies the maximum number of aggregation groups that can be returned. Valid values: 0 to 2000.
        # *   If you do not specify this parameter or set the parameter to 0, the default value of 100 is used.
        self.max_results = max_results
        # The pagination token is used in the next request to retrieve a new page of results if the total number of results exceeds the value of the MaxResults parameter.
        # 
        # The next call to the operation returns results lexicographically after the NextToken parameter value.
        # 
        # You do not need to specify this parameter in your initial request.
        self.next_token = next_token
        # The sort order. Valid values:
        # 
        # *   asc: sorts the results in ascending order.
        # *   desc: sorts the results in descending order. This is the default value.
        # 
        # *   You can specify multiple sort orders that are separated by commas. Example: asc,desc.
        # 
        # *   The number of elements in the Order parameter must be less than or equal to the number of elements in the Sort parameter. For example, if the value of the Sort parameter is Size,Filename, you can set the Order parameter to desc,asc.
        # 
        # *   If the number of sort orders is less than the number of sort fields, the sort fields for which no sorting orders are explicitly specified use the asc order by default. For example, if you set Sort to Size,Filename and Order to asc, the Filename field defaults to the value of asc.
        self.order = order
        # The name of the project.[](~~478153~~)
        # 
        # This parameter is required.
        self.project_name = project_name
        # The query conditions.
        self.query = query
        # The sort fields. For more information, see [Supported fields and operators](https://help.aliyun.com/document_detail/2743991.html).
        # 
        # > 
        # 
        # *   If you specify multiple sort fields, separate them with commas (,), as in Size,Filename.
        # 
        # *   You can specify up to five sort fields.
        # 
        # *   The order of the sort fields determines their precedence in the sorting process.
        self.sort = sort
        # The fields that you want to include in the response. You can use this parameter to reduce the size of the response.
        # 
        # If you do not specify this parameter or leave this parameter empty, the operation returns all metadata fields.
        self.with_fields = with_fields
        # Specifies whether to return the total number of hits. Valid values:
        # 
        # *   true
        # *   false
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
        # The operator.
        # 
        # Enumerated values:
        # 
        # *   average: calculates the average number.
        # *   min: finds the minimum value.
        # *   max: finds the maximum value.
        # *   count: counts the number of results.
        # *   distinct: counts the number of distinct results.
        # *   sum: calculates the sum of all matching results..
        # *   group: counts the number of results by group. The results are sorted by the count number in descending order.
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

