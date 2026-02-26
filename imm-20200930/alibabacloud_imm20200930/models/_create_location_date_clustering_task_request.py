# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class CreateLocationDateClusteringTaskRequest(DaraModel):
    def __init__(
        self,
        dataset_name: str = None,
        date_options: main_models.CreateLocationDateClusteringTaskRequestDateOptions = None,
        location_options: main_models.CreateLocationDateClusteringTaskRequestLocationOptions = None,
        notification: main_models.Notification = None,
        project_name: str = None,
        tags: Dict[str, Any] = None,
        user_data: str = None,
    ):
        # The name of the dataset.[](~~478160~~)
        # 
        # This parameter is required.
        self.dataset_name = dataset_name
        # The date configurations for clustering.
        # 
        # >  Adjusting these configurations affects existing spatiotemporal clusters for the dataset.
        # 
        # This parameter is required.
        self.date_options = date_options
        # The geolocation configurations for clustering.
        # 
        # >  Adjusting these configurations affects existing spatiotemporal clusters for the dataset.
        # 
        # This parameter is required.
        self.location_options = location_options
        # The notification settings. For information about the asynchronous notification format, see [Asynchronous message examples](https://help.aliyun.com/document_detail/2743997.html).
        self.notification = notification
        # The name of the project.[](~~478153~~)
        # 
        # This parameter is required.
        self.project_name = project_name
        # The custom tags. You can search for or filter asynchronous tasks by custom tag.
        self.tags = tags
        # The custom information, which is returned in an asynchronous notification and facilitates notification management. The maximum length of the value is 2,048 bytes.
        self.user_data = user_data

    def validate(self):
        if self.date_options:
            self.date_options.validate()
        if self.location_options:
            self.location_options.validate()
        if self.notification:
            self.notification.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name

        if self.date_options is not None:
            result['DateOptions'] = self.date_options.to_map()

        if self.location_options is not None:
            result['LocationOptions'] = self.location_options.to_map()

        if self.notification is not None:
            result['Notification'] = self.notification.to_map()

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        if m.get('DateOptions') is not None:
            temp_model = main_models.CreateLocationDateClusteringTaskRequestDateOptions()
            self.date_options = temp_model.from_map(m.get('DateOptions'))

        if m.get('LocationOptions') is not None:
            temp_model = main_models.CreateLocationDateClusteringTaskRequestLocationOptions()
            self.location_options = temp_model.from_map(m.get('LocationOptions'))

        if m.get('Notification') is not None:
            temp_model = main_models.Notification()
            self.notification = temp_model.from_map(m.get('Notification'))

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class CreateLocationDateClusteringTaskRequestLocationOptions(DaraModel):
    def __init__(
        self,
        location_date_cluster_levels: List[str] = None,
    ):
        # The administrative division levels. You can specify multiple administrative division levels.
        # 
        # For example, you uploaded photos that were taken from March 3, 2024 to March 5, 2024 in Hangzhou and photos that were taken from March 6, 2024 to March 8, 2024 in Jiaxing. When you call the operation and set the parameter to `["city", "province"]`, the following spatiotemporal clusters are created from these photos:
        # 
        # *   March 3, 2024 to March 5, 2024, Hangzhou
        # *   March 6, 2024 to March 8, 2024, Jiaxing
        # *   March 3, 2024 to March 8, 2024, Zhejiang
        # 
        # This parameter is required.
        self.location_date_cluster_levels = location_date_cluster_levels

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.location_date_cluster_levels is not None:
            result['LocationDateClusterLevels'] = self.location_date_cluster_levels

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocationDateClusterLevels') is not None:
            self.location_date_cluster_levels = m.get('LocationDateClusterLevels')

        return self

class CreateLocationDateClusteringTaskRequestDateOptions(DaraModel):
    def __init__(
        self,
        gap_days: int = None,
        max_days: int = None,
        min_days: int = None,
    ):
        # The maximum number of days allowed in a gap for a single spatiotemporal cluster. Valid values: 0 to 99999.
        # 
        # For example, if travel photos were produced on March 4, 5, and 7, 2024, but not on Marh 6, 2024, and you set the parameter to 1, IMM considers the travel spanning the date range from March 4, 2024 to March 7, 2024 and includes photos within the data range in the same cluster.````
        # 
        # We recommend that you set the parameter to a value within the range from 0 to 3.
        # 
        # This parameter is required.
        self.gap_days = gap_days
        # The maximum number of days that a single spatiotemporal cluster can span. Valid values: 1 to 99999. IMM does not create a cluster that spans more than the maximum number of days.
        # 
        # For example, if you want to create travel photo clusters, you may want to exclude photos that were taken within 15 consecutive days in the same city, because it is likely that these photos were not taken during a travel. In this case, you can set the parameter to 15 to exclude this time range and location from the clustering task.
        # 
        # This parameter is required.
        self.max_days = max_days
        # The minimum number of days that a single spatiotemporal cluster can span. Valid values: 1 to 99999. IMM does not create a cluster that spans less than the minimum number of days.
        # 
        # For example, if you do not want a one-day tour cluster, you can set the parameter to 2.
        # 
        # This parameter is required.
        self.min_days = min_days

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gap_days is not None:
            result['GapDays'] = self.gap_days

        if self.max_days is not None:
            result['MaxDays'] = self.max_days

        if self.min_days is not None:
            result['MinDays'] = self.min_days

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GapDays') is not None:
            self.gap_days = m.get('GapDays')

        if m.get('MaxDays') is not None:
            self.max_days = m.get('MaxDays')

        if m.get('MinDays') is not None:
            self.min_days = m.get('MinDays')

        return self

