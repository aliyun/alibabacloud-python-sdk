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
        # The aggregations.
        # 
        # >  If you perform an aggregate query, the aggregation returned in the response contains only statistical results, not the actual metadata.
        self.aggregations_shrink = aggregations_shrink
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
        self.query_shrink = query_shrink
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
        self.with_fields_shrink = with_fields_shrink
        # Specifies whether to return the total number of hits. Valid values:
        # 
        # *   true
        # *   false
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

