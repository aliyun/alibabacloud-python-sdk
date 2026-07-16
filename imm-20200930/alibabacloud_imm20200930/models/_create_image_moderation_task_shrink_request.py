# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateImageModerationTaskShrinkRequest(DaraModel):
    def __init__(
        self,
        credential_config_shrink: str = None,
        interval: int = None,
        max_frames: int = None,
        notification_shrink: str = None,
        project_name: str = None,
        scenes_shrink: str = None,
        source_uri: str = None,
        tags_shrink: str = None,
        user_data: str = None,
    ):
        # The chained authorization configuration. This parameter is optional. For more information, see [Use chained authorization to access resources of other entities](https://help.aliyun.com/document_detail/465340.html).
        self.credential_config_shrink = credential_config_shrink
        # The frame capture frequency. This parameter is used for GIF and long image detection. The default value is 1.
        self.interval = interval
        # The maximum number of frames to capture. This parameter is used for GIF and long image detection. The default value is 1.
        self.max_frames = max_frames
        # The notification configuration. For more information about the format of asynchronous notification messages, see [Asynchronous notification message format](https://help.aliyun.com/document_detail/2743997.html).
        self.notification_shrink = notification_shrink
        # The project name. For more information about how to obtain the project name, see [Create a project](https://help.aliyun.com/document_detail/478153.html).
        # 
        # This parameter is required.
        self.project_name = project_name
        # The image detection scenarios.
        self.scenes_shrink = scenes_shrink
        # The OSS URI of the image.
        # 
        # The URI must follow the `oss://<Bucket>/<Object>` format. `<Bucket>` is the name of the OSS bucket that is in the same region as the project. `<Object>` is the full path of the file, including the file name extension.
        # 
        # This parameter is required.
        self.source_uri = source_uri
        # The custom tags. You can use tags to search for and filter asynchronous tasks.
        self.tags_shrink = tags_shrink
        # The custom information. This information is returned in the asynchronous notification message to help you associate the message with your system. The value can be up to 2,048 bytes long.
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

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.max_frames is not None:
            result['MaxFrames'] = self.max_frames

        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.scenes_shrink is not None:
            result['Scenes'] = self.scenes_shrink

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

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('MaxFrames') is not None:
            self.max_frames = m.get('MaxFrames')

        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('Scenes') is not None:
            self.scenes_shrink = m.get('Scenes')

        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')

        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

