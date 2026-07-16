# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateFigureClustersMergingTaskShrinkRequest(DaraModel):
    def __init__(
        self,
        dataset_name: str = None,
        from_: str = None,
        froms_shrink: str = None,
        notification_shrink: str = None,
        project_name: str = None,
        tags_shrink: str = None,
        to: str = None,
        user_data: str = None,
    ):
        # The name of the dataset. For more information, see [Create a dataset](https://help.aliyun.com/document_detail/478160.html).
        # 
        # This parameter is required.
        self.dataset_name = dataset_name
        # The ID of the source clustering group. You must specify a value for either \\`From\\` or \\`Froms\\`. You cannot specify values for both parameters.
        self.from_ = from_
        # A list of the IDs of the source clustering groups. You must specify a value for either \\`From\\` or \\`Froms\\`. You cannot specify values for both parameters. The list can contain up to 100 IDs.
        self.froms_shrink = froms_shrink
        # The configuration of the notification message. For more information, click Notification. For more information about the format of an asynchronous notification message, see [Asynchronous notification messages](https://help.aliyun.com/document_detail/2743997.html).
        self.notification_shrink = notification_shrink
        # The name of the project. For more information, see [Create a project](https://help.aliyun.com/document_detail/478153.html).
        # 
        # This parameter is required.
        self.project_name = project_name
        # The custom tags. You can use custom tags to search for and filter asynchronous tasks.
        self.tags_shrink = tags_shrink
        # The ID of the destination clustering group.
        # 
        # This parameter is required.
        self.to = to
        # The custom information. This information is returned in the asynchronous notification message to help you associate the message with your system. The value can be up to 2,048 bytes in length.
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

        if self.from_ is not None:
            result['From'] = self.from_

        if self.froms_shrink is not None:
            result['Froms'] = self.froms_shrink

        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink

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
            self.froms_shrink = m.get('Froms')

        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')

        if m.get('To') is not None:
            self.to = m.get('To')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

