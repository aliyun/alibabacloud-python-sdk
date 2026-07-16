# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class IndexFileMetaRequest(DaraModel):
    def __init__(
        self,
        dataset_name: str = None,
        file: main_models.InputFile = None,
        notification: main_models.Notification = None,
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
        self.file = file
        # The message notification configuration. For more information, see Notification. For the format of the asynchronous notification message, see the Metadata Indexing section in [Asynchronous notification message formats](https://help.aliyun.com/document_detail/2743997.html).
        self.notification = notification
        # The name of the project. To get the project name, see [Create a project](https://help.aliyun.com/document_detail/478153.html).
        # 
        # This parameter is required.
        self.project_name = project_name
        # Custom information that is returned in the asynchronous notification message. This helps you associate the notification with your services. The maximum length is 2048 bytes.
        self.user_data = user_data

    def validate(self):
        if self.file:
            self.file.validate()
        if self.notification:
            self.notification.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name

        if self.file is not None:
            result['File'] = self.file.to_map()

        if self.notification is not None:
            result['Notification'] = self.notification.to_map()

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
            temp_model = main_models.InputFile()
            self.file = temp_model.from_map(m.get('File'))

        if m.get('Notification') is not None:
            temp_model = main_models.Notification()
            self.notification = temp_model.from_map(m.get('Notification'))

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

