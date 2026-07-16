# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateMediaConvertTaskShrinkRequest(DaraModel):
    def __init__(
        self,
        alignment_index: int = None,
        credential_config_shrink: str = None,
        notification_shrink: str = None,
        project_name: str = None,
        sources_shrink: str = None,
        tags_shrink: str = None,
        target_groups_shrink: str = None,
        targets_shrink: str = None,
        user_data: str = None,
    ):
        # When concatenating media files, this specifies the index of the primary file in the Sources list. The default transcoding parameters (such as resolution and frame rate from the `Video` and `Audio` objects) are taken from this primary file. The default index is 0.
        self.alignment_index = alignment_index
        # **You can leave this parameter empty if you do not have special requirements.**
        # 
        # The chained authorization configuration. For more information, see [Use chained authorization to access resources of other entities](https://help.aliyun.com/document_detail/465340.html).
        self.credential_config_shrink = credential_config_shrink
        # The message notification settings. For more information, click Notification. For information about the format of asynchronous notifications, see [Asynchronous notification format](https://help.aliyun.com/document_detail/2743997.html).
        self.notification_shrink = notification_shrink
        # The name of the project. For more information about how to obtain the project name, see [Create a project](https://help.aliyun.com/document_detail/478153.html).
        # 
        # This parameter is required.
        self.project_name = project_name
        # A list of media files. If you provide more than one file, they are concatenated in the order of their URIs.
        # 
        # This parameter is required.
        self.sources_shrink = sources_shrink
        # Custom tags for searching and filtering asynchronous tasks.
        self.tags_shrink = tags_shrink
        # A list of media packaging tasks to convert and package the input media into HLS outputs. Each TargetGroup corresponds to one HLS master playlist.
        self.target_groups_shrink = target_groups_shrink
        # A list of media processing tasks.
        self.targets_shrink = targets_shrink
        # The custom user data. This data is returned in the asynchronous notification, allowing you to associate the notification with your internal system. The maximum length is 2,048 bytes.
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alignment_index is not None:
            result['AlignmentIndex'] = self.alignment_index

        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink

        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.sources_shrink is not None:
            result['Sources'] = self.sources_shrink

        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink

        if self.target_groups_shrink is not None:
            result['TargetGroups'] = self.target_groups_shrink

        if self.targets_shrink is not None:
            result['Targets'] = self.targets_shrink

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlignmentIndex') is not None:
            self.alignment_index = m.get('AlignmentIndex')

        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')

        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('Sources') is not None:
            self.sources_shrink = m.get('Sources')

        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')

        if m.get('TargetGroups') is not None:
            self.target_groups_shrink = m.get('TargetGroups')

        if m.get('Targets') is not None:
            self.targets_shrink = m.get('Targets')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

