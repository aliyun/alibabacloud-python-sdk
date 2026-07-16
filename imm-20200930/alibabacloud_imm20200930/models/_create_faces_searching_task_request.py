# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class CreateFacesSearchingTaskRequest(DaraModel):
    def __init__(
        self,
        dataset_name: str = None,
        max_result: int = None,
        notification: main_models.Notification = None,
        project_name: str = None,
        sources: List[main_models.CreateFacesSearchingTaskRequestSources] = None,
        user_data: str = None,
    ):
        # The name of the dataset. For more information, see [Create a dataset](https://help.aliyun.com/document_detail/478160.html).
        # 
        # This parameter is required.
        self.dataset_name = dataset_name
        # The number of most similar faces to return. Valid values: 0 to 100. Default value: 5.
        self.max_result = max_result
        # The notification configuration. For more information about the format of asynchronous notification messages, see [Asynchronous notification message format](https://help.aliyun.com/document_detail/2743997.html).
        self.notification = notification
        # The name of the project. For more information, see [Create a project](https://help.aliyun.com/document_detail/478153.html).
        # 
        # This parameter is required.
        self.project_name = project_name
        # A list of images.
        self.sources = sources
        # Custom user information. This information is returned in the asynchronous notification message to help you associate the message with your system. The maximum length is 2048 bytes.
        self.user_data = user_data

    def validate(self):
        if self.notification:
            self.notification.validate()
        if self.sources:
            for v1 in self.sources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name

        if self.max_result is not None:
            result['MaxResult'] = self.max_result

        if self.notification is not None:
            result['Notification'] = self.notification.to_map()

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        result['Sources'] = []
        if self.sources is not None:
            for k1 in self.sources:
                result['Sources'].append(k1.to_map() if k1 else None)

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
            temp_model = main_models.Notification()
            self.notification = temp_model.from_map(m.get('Notification'))

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        self.sources = []
        if m.get('Sources') is not None:
            for k1 in m.get('Sources'):
                temp_model = main_models.CreateFacesSearchingTaskRequestSources()
                self.sources.append(temp_model.from_map(k1))

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class CreateFacesSearchingTaskRequestSources(DaraModel):
    def __init__(
        self,
        uri: str = None,
    ):
        # The OSS URI of the image.
        # 
        # The OSS URI must follow the format oss\\://${Bucket}/${Object}. `${Bucket}` is the name of the OSS bucket in the same region as the current project. `${Object}` is the full path of the file, including the file name extension.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.uri is not None:
            result['URI'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('URI') is not None:
            self.uri = m.get('URI')

        return self

