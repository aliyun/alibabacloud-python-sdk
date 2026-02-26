# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class IndexFileMetaShrinkRequest(DaraModel):
    def __init__(
        self,
        dataset_name: str = None,
        file_shrink: str = None,
        notification_shrink: str = None,
        project_name: str = None,
        user_data: str = None,
    ):
        # The name of the dataset. You can obtain the name of the dataset from the response of the [CreateDataset](https://help.aliyun.com/document_detail/478160.html) operation.
        # 
        # This parameter is required.
        self.dataset_name = dataset_name
        # The file for which you want to create a metadata index. The value must be in the JSON format.
        # 
        # This parameter is required.
        self.file_shrink = file_shrink
        # The notification settings. For information about the asynchronous notification format, see [Asynchronous message examples](https://help.aliyun.com/document_detail/2743997.html).
        self.notification_shrink = notification_shrink
        # The name of the project. You can obtain the name of the project from the response of the [CreateProject](https://help.aliyun.com/document_detail/478153.html) operation.
        # 
        # This parameter is required.
        self.project_name = project_name
        # The custom user information, which is returned in an asynchronous notification. The maximum length of a notification is 2048 bytes.
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

        if self.file_shrink is not None:
            result['File'] = self.file_shrink

        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        if m.get('File') is not None:
            self.file_shrink = m.get('File')

        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

