# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class BatchIndexFileMetaRequest(DaraModel):
    def __init__(
        self,
        dataset_name: str = None,
        files: List[main_models.InputFile] = None,
        notification: main_models.Notification = None,
        project_name: str = None,
        user_data: str = None,
    ):
        # The dataset name. For more information about how to obtain the dataset name, see [Create a dataset](https://help.aliyun.com/document_detail/478160.html).
        # 
        # This parameter is required.
        self.dataset_name = dataset_name
        # A list of OSS files. This is an array in JSON format that can contain up to 100 files.
        # 
        # This parameter is required.
        self.files = files
        # The notification configuration. For more information, click Notification. For the format of asynchronous notification messages, see the metadata indexing section in [Asynchronous notification message formats](https://help.aliyun.com/document_detail/2743997.html).
        self.notification = notification
        # The project name. For more information about how to obtain the project name, see [Create a project](https://help.aliyun.com/document_detail/478153.html).
        # 
        # This parameter is required.
        self.project_name = project_name
        # Custom user data. This parameter takes effect only when you specify an MNS configuration for the Notification parameter. The data is returned in the asynchronous notification message, which you can use to associate the message with your services. The maximum length is 2048 bytes.
        self.user_data = user_data

    def validate(self):
        if self.files:
            for v1 in self.files:
                 if v1:
                    v1.validate()
        if self.notification:
            self.notification.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name

        result['Files'] = []
        if self.files is not None:
            for k1 in self.files:
                result['Files'].append(k1.to_map() if k1 else None)

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

        self.files = []
        if m.get('Files') is not None:
            for k1 in m.get('Files'):
                temp_model = main_models.InputFile()
                self.files.append(temp_model.from_map(k1))

        if m.get('Notification') is not None:
            temp_model = main_models.Notification()
            self.notification = temp_model.from_map(m.get('Notification'))

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

