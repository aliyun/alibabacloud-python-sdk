# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryLocationDateClustersShrinkRequest(DaraModel):
    def __init__(
        self,
        address_shrink: str = None,
        create_time_range_shrink: str = None,
        custom_labels: str = None,
        dataset_name: str = None,
        location_date_cluster_end_time_range_shrink: str = None,
        location_date_cluster_levels_shrink: str = None,
        location_date_cluster_start_time_range_shrink: str = None,
        max_results: int = None,
        next_token: str = None,
        object_id: str = None,
        order: str = None,
        project_name: str = None,
        sort: str = None,
        title: str = None,
        update_time_range_shrink: str = None,
    ):
        # The address information.
        self.address_shrink = address_shrink
        # The time range during which the spatiotemporal clusters were generated.
        self.create_time_range_shrink = create_time_range_shrink
        # The custom labels.
        self.custom_labels = custom_labels
        # The name of the dataset. For information about how to create a dataset, see [CreateDataset](https://help.aliyun.com/document_detail/478160.html).
        # 
        # This parameter is required.
        self.dataset_name = dataset_name
        # The time range during which the latest photo in a cluster was taken.
        self.location_date_cluster_end_time_range_shrink = location_date_cluster_end_time_range_shrink
        # The container for the administrative division level of the spatiotemporal clusters to be queried.
        self.location_date_cluster_levels_shrink = location_date_cluster_levels_shrink
        # The time range during which the earliest photo in a cluster was taken.
        self.location_date_cluster_start_time_range_shrink = location_date_cluster_start_time_range_shrink
        # The number of entries per page. Valid values: [1,100]. Default value: 20.
        self.max_results = max_results
        # The pagination token.
        self.next_token = next_token
        # The ID of the cluster that you want to query. Specify this parameter if you want to query a specific spatiotemporal cluster. Otherwise, leave this parameter empty to query spatiotemporal clusters that meet the specified conditions.
        self.object_id = object_id
        # The order that you use to sort the query results.
        # 
        # Valid values:
        # 
        # *   asc: ascending order. This is the default value.
        # *   desc: descending order.
        self.order = order
        # The name of the project. You can obtain the name of the project from the response of the [CreateProject](https://help.aliyun.com/document_detail/478153.html) operation.
        # 
        # This parameter is required.
        self.project_name = project_name
        # The field that you use to sort the query results.
        # 
        # Valid values:
        # 
        # *   LocationDateClusterEndTime: by the time at which the latest photo in a cluster was taken.
        # *   CreateTime: by the creation time of a spatiotemporal cluster.
        # *   UpdateTime: by the update time of a spatiotemporal cluster.
        # *   LocationDateClusterStartTime: by the time at which the earliest photo in a cluster was taken. This is the default value.
        self.sort = sort
        # The characters that are included in the titles of spatiotemporal clusters to be queried. Matches are found by using fuzzy matching.
        self.title = title
        # The time range during which the spatiotemporal clusters were updated.
        self.update_time_range_shrink = update_time_range_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address_shrink is not None:
            result['Address'] = self.address_shrink

        if self.create_time_range_shrink is not None:
            result['CreateTimeRange'] = self.create_time_range_shrink

        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels

        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name

        if self.location_date_cluster_end_time_range_shrink is not None:
            result['LocationDateClusterEndTimeRange'] = self.location_date_cluster_end_time_range_shrink

        if self.location_date_cluster_levels_shrink is not None:
            result['LocationDateClusterLevels'] = self.location_date_cluster_levels_shrink

        if self.location_date_cluster_start_time_range_shrink is not None:
            result['LocationDateClusterStartTimeRange'] = self.location_date_cluster_start_time_range_shrink

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.object_id is not None:
            result['ObjectId'] = self.object_id

        if self.order is not None:
            result['Order'] = self.order

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.sort is not None:
            result['Sort'] = self.sort

        if self.title is not None:
            result['Title'] = self.title

        if self.update_time_range_shrink is not None:
            result['UpdateTimeRange'] = self.update_time_range_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address_shrink = m.get('Address')

        if m.get('CreateTimeRange') is not None:
            self.create_time_range_shrink = m.get('CreateTimeRange')

        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')

        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        if m.get('LocationDateClusterEndTimeRange') is not None:
            self.location_date_cluster_end_time_range_shrink = m.get('LocationDateClusterEndTimeRange')

        if m.get('LocationDateClusterLevels') is not None:
            self.location_date_cluster_levels_shrink = m.get('LocationDateClusterLevels')

        if m.get('LocationDateClusterStartTimeRange') is not None:
            self.location_date_cluster_start_time_range_shrink = m.get('LocationDateClusterStartTimeRange')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('Sort') is not None:
            self.sort = m.get('Sort')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('UpdateTimeRange') is not None:
            self.update_time_range_shrink = m.get('UpdateTimeRange')

        return self

