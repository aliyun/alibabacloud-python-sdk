# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class CreateFigureClustersMergingTaskRequest(DaraModel):
    def __init__(
        self,
        dataset_name: str = None,
        from_: str = None,
        froms: List[str] = None,
        notification: main_models.Notification = None,
        project_name: str = None,
        tags: Dict[str, Any] = None,
        to: str = None,
        user_data: str = None,
    ):
        # The name of the dataset. For more information, see [Create a dataset](https://help.aliyun.com/document_detail/478160.html).
        # 
        # This parameter is required.
        self.dataset_name = dataset_name
        # The ID of the source group. You must specify either From or Froms, but not both.
        self.from_ = from_
        # The IDs of source clustering groups. You must specify either From or Froms, but not both. You can specify up to 100 task IDs.
        self.froms = froms
        # The notification settings. For information about the asynchronous notification format, see [Asynchronous message examples](https://help.aliyun.com/document_detail/2743997.html).
        self.notification = notification
        # The name of the project. For more information, see [CreateProject](https://help.aliyun.com/document_detail/478153.html).
        # 
        # This parameter is required.
        self.project_name = project_name
        # The custom tags, which can be used to search for and filter asynchronous tasks.
        self.tags = tags
        # The ID of the destination clustering group.
        # 
        # This parameter is required.
        self.to = to
        # The custom data, which is returned in an asynchronous notification and facilitates notification management. The maximum length is 2,048 bytes.
        self.user_data = user_data

    def validate(self):
        if self.notification:
            self.notification.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name

        if self.from_ is not None:
            result['From'] = self.from_

        if self.froms is not None:
            result['Froms'] = self.froms

        if self.notification is not None:
            result['Notification'] = self.notification.to_map()

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.to is not None:
            result['To'] = self.to

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('Froms') is not None:
            self.froms = m.get('Froms')

        if m.get('Notification') is not None:
            temp_model = main_models.Notification()
            self.notification = temp_model.from_map(m.get('Notification'))

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('To') is not None:
            self.to = m.get('To')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

