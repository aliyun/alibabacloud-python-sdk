# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryFigureClustersShrinkRequest(DaraModel):
    def __init__(
        self,
        create_time_range_shrink: str = None,
        custom_labels: str = None,
        dataset_name: str = None,
        max_results: int = None,
        next_token: str = None,
        order: str = None,
        project_name: str = None,
        sort: str = None,
        update_time_range_shrink: str = None,
        with_total_count: bool = None,
    ):
        # The time range during which the face clusters were created.
        self.create_time_range_shrink = create_time_range_shrink
        # The query conditions for custom labels.
        self.custom_labels = custom_labels
        # The name of the dataset. For more information about how to obtain the dataset name, see [Create a dataset](https://help.aliyun.com/document_detail/478160.html).
        # 
        # This parameter is required.
        self.dataset_name = dataset_name
        # The maximum number of data records to return in this call. Valid values: 0 to 100. If this parameter is not specified or is set to 0, the default value 100 is used.
        self.max_results = max_results
        # The pagination token. If this parameter is left empty or set to None, the query starts from the beginning.
        self.next_token = next_token
        # The sort order. Default value: asc.
        self.order = order
        # The name of the project. For more information about how to obtain the project name, see [Create a project](https://help.aliyun.com/document_detail/478153.html).
        # 
        # This parameter is required.
        self.project_name = project_name
        # The field used for sorting. By default, this parameter is left empty, which indicates that the results are sorted by cluster ID.
        self.sort = sort
        # The time range during which the face clusters were updated.
        self.update_time_range_shrink = update_time_range_shrink
        # Specifies whether to return the total number of face clusters that meet the current query conditions. Default value: false, which indicates that the total number of clusters is not returned.
        self.with_total_count = with_total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time_range_shrink is not None:
            result['CreateTimeRange'] = self.create_time_range_shrink

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

        if self.update_time_range_shrink is not None:
            result['UpdateTimeRange'] = self.update_time_range_shrink

        if self.with_total_count is not None:
            result['WithTotalCount'] = self.with_total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTimeRange') is not None:
            self.create_time_range_shrink = m.get('CreateTimeRange')

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

        if m.get('UpdateTimeRange') is not None:
            self.update_time_range_shrink = m.get('UpdateTimeRange')

        if m.get('WithTotalCount') is not None:
            self.with_total_count = m.get('WithTotalCount')

        return self

