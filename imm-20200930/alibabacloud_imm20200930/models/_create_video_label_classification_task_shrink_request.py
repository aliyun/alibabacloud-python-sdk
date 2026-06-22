# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateVideoLabelClassificationTaskShrinkRequest(DaraModel):
    def __init__(
        self,
        credential_config_shrink: str = None,
        notification_shrink: str = None,
        project_name: str = None,
        source_uri: str = None,
        tags_shrink: str = None,
        user_data: str = None,
    ):
        # **If you do not have special requirements, leave this parameter empty.**
        # 
        # The chained authorization configuration. This parameter is not required. For more information, see [Use chained authorization to access resources of other entities](https://help.aliyun.com/document_detail/465340.html).
        self.credential_config_shrink = credential_config_shrink
        # The message notification configuration. For more information, click Notification. For more information about the format of asynchronous notification messages, see [Asynchronous notification message format](https://help.aliyun.com/document_detail/2743997.html).
        self.notification_shrink = notification_shrink
        # The project name. For more information about how to obtain the project name, see [Create a project](https://help.aliyun.com/document_detail/478153.html).
        # 
        # This parameter is required.
        self.project_name = project_name
        # The Object Storage Service (OSS) URI of the video.
        # 
        # The OSS URI must follow the format oss\\://${Bucket}/${Object}. ${Bucket} is the name of the OSS bucket that is in the same region as the current project. ${Object} is the full path of the file, including the file name extension.
        # 
        # This parameter is required.
        self.source_uri = source_uri
        # Custom tags that you can use to search for and filter asynchronous tasks.
        self.tags_shrink = tags_shrink
        # Custom information. This information is returned in the asynchronous notification message. You can use this information to associate the notification message with your services. The maximum length is 2,048 bytes.
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink

        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri

        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')

        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')

        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

