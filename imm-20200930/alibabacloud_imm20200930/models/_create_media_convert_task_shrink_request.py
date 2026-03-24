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
        # When performing media concatenation, the index of the primary media file (which provides the default transcoding parameters for `Video` and `Audio`, including resolution, frame rate, etc.) in the concatenation list. The default value is 0 (aligning with the first media file in the concatenation list).
        self.alignment_index = alignment_index
        # **If there are no special requirements, please leave this blank.**
        # 
        # Chain authorization configuration. For more information, see [Using Chain Authorization to Access Other Entity Resources](https://help.aliyun.com/document_detail/465340.html).
        self.credential_config_shrink = credential_config_shrink
        # Notification configuration. For details, click Notification. The format of asynchronous notification messages can be found in [Asynchronous Notification Message Format](https://help.aliyun.com/document_detail/2743997.html).
        self.notification_shrink = notification_shrink
        # The name of the project. For how to obtain it, see [Creating a Project](https://help.aliyun.com/document_detail/478153.html).
        # 
        # This parameter is required.
        self.project_name = project_name
        # A list of media files. If the list contains more than one element, it indicates that the Concat (concatenation) function is enabled. The Concat order follows the sequence of the input video file URIs.
        # 
        # This parameter is required.
        self.sources_shrink = sources_shrink
        # Custom tags used for searching and filtering asynchronous tasks.
        self.tags_shrink = tags_shrink
        self.target_groups_shrink = target_groups_shrink
        # List of media processing tasks, supporting multiple task configurations.
        self.targets_shrink = targets_shrink
        # User-defined information that will be returned in asynchronous message notifications, used for convenient association and processing within your system. The maximum length is 2048 bytes.
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

