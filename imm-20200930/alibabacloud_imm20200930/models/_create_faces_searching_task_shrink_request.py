# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateFacesSearchingTaskShrinkRequest(DaraModel):
    def __init__(
        self,
        dataset_name: str = None,
        max_result: int = None,
        notification_shrink: str = None,
        project_name: str = None,
        sources_shrink: str = None,
        user_data: str = None,
    ):
        # The name of the dataset.[](~~478160~~)
        # 
        # This parameter is required.
        self.dataset_name = dataset_name
        # The number of the most similar faces that you want to return. Valid values: 1 to 100. Default value: 5.
        self.max_result = max_result
        # The notification settings. For information about the asynchronous notification format, see [Asynchronous message examples](https://help.aliyun.com/document_detail/2743997.html).
        self.notification_shrink = notification_shrink
        # The name of the project.[](~~478153~~)
        # 
        # This parameter is required.
        self.project_name = project_name
        # The images.
        self.sources_shrink = sources_shrink
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

        if self.max_result is not None:
            result['MaxResult'] = self.max_result

        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.sources_shrink is not None:
            result['Sources'] = self.sources_shrink

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        if m.get('MaxResult') is not None:
            self.max_result = m.get('MaxResult')

        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('Sources') is not None:
            self.sources_shrink = m.get('Sources')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

