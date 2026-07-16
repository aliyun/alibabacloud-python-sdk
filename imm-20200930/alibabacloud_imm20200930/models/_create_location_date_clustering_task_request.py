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
        # The dataset name. For more information, see [Create a dataset](https://help.aliyun.com/document_detail/478160.html).
        # 
        # This parameter is required.
        self.dataset_name = dataset_name
        # The date clustering settings.
        # >Notice: Modifying this setting also affects existing spatio-temporal clusters in your `Dataset`.
        # 
        # This parameter is required.
        self.date_options = date_options
        # The location clustering settings.
        # >Notice: Modifying this setting also affects existing spatio-temporal clusters in your `Dataset`.
        # 
        # This parameter is required.
        self.location_options = location_options
        # The message notification configuration. For more information, see Notification. For the format of asynchronous notification messages, see [Asynchronous notification message format](https://help.aliyun.com/document_detail/2743997.html).
        self.notification = notification
        # The project name. For more information, see [Create a project](https://help.aliyun.com/document_detail/478153.html).
        # 
        # This parameter is required.
        self.project_name = project_name
        # Custom tags used to search for and filter asynchronous tasks.
        self.tags = tags
        # Custom information that is returned in the asynchronous notification message. This helps you associate the notification message with your system. The maximum length is 2,048 bytes.
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
        # A list of administrative levels for grouping. You can select multiple levels.
        # 
        # For example, a user uploads photos taken in Hangzhou from March 3 to March 5 and photos taken in Jiaxing from March 6 to March 8. If you set this parameter to `["city", "province"]`, the following spatio-temporal clusters are generated:
        # 
        # - March 3 to March 5, Hangzhou
        # 
        # - March 6 to March 8, Jiaxing
        # 
        # - March 3 to March 8, Zhejiang
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
        # The maximum number of gap days allowed in a single spatio-temporal group. The value must be in the range of 0 to 99,999.
        # 
        # For example, a user has photos from March 4–5 and March 7, but not from March 6. If you assume that the photos from March 4–7 belong to the same trip, set this parameter to `1 day`. This allows the gap of `1 day` on March 6 to be included in the same spatio-temporal cluster.
        # 
        # Set this parameter to a value from 0 to 3.
        # 
        # This parameter is required.
        self.gap_days = gap_days
        # The maximum number of days in a single spatio-temporal group. The value must be in the range of 1 to 99,999. Clusters with more days than this value are not detected or stored.
        # 
        # For example, if a user takes photos in the same location for more than 15 consecutive days, this location might be their residence rather than a travel destination. If you want to exclude this time period and location from the spatio-temporal clusters, set this parameter to 15.
        # 
        # This parameter is required.
        self.max_days = max_days
        # The minimum number of days in a single spatio-temporal group. The value must be in the range of 1 to 99,999. Clusters with fewer days than this value are not detected or stored.
        # 
        # For example, if you do not want to include one-day trips in the generated groups, set this parameter to 2.
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

