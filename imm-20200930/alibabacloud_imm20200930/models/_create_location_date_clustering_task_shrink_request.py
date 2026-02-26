# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateLocationDateClusteringTaskShrinkRequest(DaraModel):
    def __init__(
        self,
        dataset_name: str = None,
        date_options_shrink: str = None,
        location_options_shrink: str = None,
        notification_shrink: str = None,
        project_name: str = None,
        tags_shrink: str = None,
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
        self.date_options_shrink = date_options_shrink
        # The geolocation configurations for clustering.
        # 
        # >  Adjusting these configurations affects existing spatiotemporal clusters for the dataset.
        # 
        # This parameter is required.
        self.location_options_shrink = location_options_shrink
        # The notification settings. For information about the asynchronous notification format, see [Asynchronous message examples](https://help.aliyun.com/document_detail/2743997.html).
        self.notification_shrink = notification_shrink
        # The name of the project.[](~~478153~~)
        # 
        # This parameter is required.
        self.project_name = project_name
        # The custom tags. You can search for or filter asynchronous tasks by custom tag.
        self.tags_shrink = tags_shrink
        # The custom information, which is returned in an asynchronous notification and facilitates notification management. The maximum length of the value is 2,048 bytes.
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name

        if self.date_options_shrink is not None:
            result['DateOptions'] = self.date_options_shrink

        if self.location_options_shrink is not None:
            result['LocationOptions'] = self.location_options_shrink

        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        if m.get('DateOptions') is not None:
            self.date_options_shrink = m.get('DateOptions')

        if m.get('LocationOptions') is not None:
            self.location_options_shrink = m.get('LocationOptions')

        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

