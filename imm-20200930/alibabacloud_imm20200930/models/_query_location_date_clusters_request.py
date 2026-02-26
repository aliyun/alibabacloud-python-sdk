# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class QueryLocationDateClustersRequest(DaraModel):
    def __init__(
        self,
        address: main_models.Address = None,
        create_time_range: main_models.TimeRange = None,
        custom_labels: str = None,
        dataset_name: str = None,
        location_date_cluster_end_time_range: main_models.TimeRange = None,
        location_date_cluster_levels: List[str] = None,
        location_date_cluster_start_time_range: main_models.TimeRange = None,
        max_results: int = None,
        next_token: str = None,
        object_id: str = None,
        order: str = None,
        project_name: str = None,
        sort: str = None,
        title: str = None,
        update_time_range: main_models.TimeRange = None,
    ):
        # The address information.
        self.address = address
        # The time range during which the spatiotemporal clusters were generated.
        self.create_time_range = create_time_range
        # The custom labels.
        self.custom_labels = custom_labels
        # The name of the dataset. For information about how to create a dataset, see [CreateDataset](https://help.aliyun.com/document_detail/478160.html).
        # 
        # This parameter is required.
        self.dataset_name = dataset_name
        # The time range during which the latest photo in a cluster was taken.
        self.location_date_cluster_end_time_range = location_date_cluster_end_time_range
        # The container for the administrative division level of the spatiotemporal clusters to be queried.
        self.location_date_cluster_levels = location_date_cluster_levels
        # The time range during which the earliest photo in a cluster was taken.
        self.location_date_cluster_start_time_range = location_date_cluster_start_time_range
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
        self.update_time_range = update_time_range

    def validate(self):
        if self.address:
            self.address.validate()
        if self.create_time_range:
            self.create_time_range.validate()
        if self.location_date_cluster_end_time_range:
            self.location_date_cluster_end_time_range.validate()
        if self.location_date_cluster_start_time_range:
            self.location_date_cluster_start_time_range.validate()
        if self.update_time_range:
            self.update_time_range.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['Address'] = self.address.to_map()

        if self.create_time_range is not None:
            result['CreateTimeRange'] = self.create_time_range.to_map()

        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels

        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name

        if self.location_date_cluster_end_time_range is not None:
            result['LocationDateClusterEndTimeRange'] = self.location_date_cluster_end_time_range.to_map()

        if self.location_date_cluster_levels is not None:
            result['LocationDateClusterLevels'] = self.location_date_cluster_levels

        if self.location_date_cluster_start_time_range is not None:
            result['LocationDateClusterStartTimeRange'] = self.location_date_cluster_start_time_range.to_map()

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

        if self.update_time_range is not None:
            result['UpdateTimeRange'] = self.update_time_range.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            temp_model = main_models.Address()
            self.address = temp_model.from_map(m.get('Address'))

        if m.get('CreateTimeRange') is not None:
            temp_model = main_models.TimeRange()
            self.create_time_range = temp_model.from_map(m.get('CreateTimeRange'))

        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')

        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        if m.get('LocationDateClusterEndTimeRange') is not None:
            temp_model = main_models.TimeRange()
            self.location_date_cluster_end_time_range = temp_model.from_map(m.get('LocationDateClusterEndTimeRange'))

        if m.get('LocationDateClusterLevels') is not None:
            self.location_date_cluster_levels = m.get('LocationDateClusterLevels')

        if m.get('LocationDateClusterStartTimeRange') is not None:
            temp_model = main_models.TimeRange()
            self.location_date_cluster_start_time_range = temp_model.from_map(m.get('LocationDateClusterStartTimeRange'))

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
            temp_model = main_models.TimeRange()
            self.update_time_range = temp_model.from_map(m.get('UpdateTimeRange'))

        return self

