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
        # The name of the dataset. To get the dataset name, see [Create a dataset](https://help.aliyun.com/document_detail/478160.html).
        # 
        # This parameter is required.
        self.dataset_name = dataset_name
        # The file to be indexed, in JSON format. For more information, see the struct definition.
        # 
        # This parameter is required.
        self.file_shrink = file_shrink
        # The message notification configuration. For more information, see Notification. For the format of the asynchronous notification message, see the Metadata Indexing section in [Asynchronous notification message formats](https://help.aliyun.com/document_detail/2743997.html).
        self.notification_shrink = notification_shrink
        # The name of the project. To get the project name, see [Create a project](https://help.aliyun.com/document_detail/478153.html).
        # 
        # This parameter is required.
        self.project_name = project_name
        # Custom information that is returned in the asynchronous notification message. This helps you associate the notification with your services. The maximum length is 2048 bytes.
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

