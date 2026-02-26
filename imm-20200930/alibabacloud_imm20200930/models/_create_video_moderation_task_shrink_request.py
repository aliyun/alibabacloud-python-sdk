# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateVideoModerationTaskShrinkRequest(DaraModel):
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
        # The authorization chain settings. For more information, see [Use authorization chains to access resources of other entities](https://help.aliyun.com/document_detail/465340.html).
        self.credential_config_shrink = credential_config_shrink
        # The interval of capturing video frames. Unit: seconds. Valid values: 1 to 600. Default value: 1.
        self.interval = interval
        # The maximum number of frames that can be captured from the video. Valid values: 5 to 3600. Default value: 200.
        self.max_frames = max_frames
        # The notification settings. For information about the asynchronous notification format, see [Asynchronous message examples](https://help.aliyun.com/document_detail/2743997.html).
        self.notification_shrink = notification_shrink
        # The name of the project.[](~~478153~~)
        # 
        # This parameter is required.
        self.project_name = project_name
        # The scenarios of video moderation.
        self.scenes_shrink = scenes_shrink
        # The OSS URI of the video.
        # 
        # Specify the OSS URI in the oss://${Bucket}/${Object} format, where `${Bucket}` is the name of the bucket in the same region as the current project and `${Object}` is the path of the object with the extension included.
        # 
        # This parameter is required.
        self.source_uri = source_uri
        # The custom tags. The custom tags help you retrieve the task.
        self.tags_shrink = tags_shrink
        # The custom information, which is returned in an asynchronous notification and facilitates notification management. The maximum length of the value is 2,048 bytes.
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

