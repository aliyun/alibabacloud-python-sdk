# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitSnapshotJobShrinkRequest(DaraModel):
    def __init__(
        self,
        count: int = None,
        height: str = None,
        interval: int = None,
        reference_id: str = None,
        snapshot_template_id: str = None,
        specified_offset_time: int = None,
        specified_offset_times_shrink: str = None,
        sprite_snapshot_config: str = None,
        user_data: str = None,
        video_id: str = None,
        width: str = None,
    ):
        # The maximum number of snapshots. Default value: **1**.
        self.count = count
        # The snapshot height. Valid values: `[8,4096]`. Default value: the source video height. Unit: px.
        self.height = height
        # The snapshot interval. The value must be **greater than or equal to 0**.
        # - Unit: seconds.
        # - Default value: **1**.
        # - If Interval is set to **0**, snapshots are evenly captured based on the value of Count and the video duration.
        self.interval = interval
        # The custom ID. Only lowercase letters, uppercase letters, digits, hyphens, and underscores are supported. Length: 6 to 64 characters. The value must be unique at the user level.
        self.reference_id = reference_id
        # The snapshot template ID.
        # - We recommend that you create a snapshot template first and then pass the snapshot template ID. For more information about how to create a snapshot template, see [Add a snapshot template](https://help.aliyun.com/document_detail/99406.html).
        # - If you pass the snapshot template ID, all request parameters except Action and VideoId are ignored.
        self.snapshot_template_id = snapshot_template_id
        # The start time for the snapshot.
        # 
        # - Unit: milliseconds.
        # - Default value: **0**.
        self.specified_offset_time = specified_offset_time
        # The points in time at which snapshots are captured. Unit: milliseconds. You can specify up to 30 points in time at a time.
        self.specified_offset_times_shrink = specified_offset_times_shrink
        # The sprite configuration. If this parameter is not empty, a sprite is generated. For more information about the parameter structure, see [SpriteSnapshotConfig](https://help.aliyun.com/document_detail/86952.html).
        self.sprite_snapshot_config = sprite_snapshot_config
        # The custom settings. Only JSON strings are supported. You can use this parameter to pass through custom data and specify callback URL settings. For more information about the parameter structure, see [UserData](https://help.aliyun.com/document_detail/86952.html).
        # 
        # > To use the message callback in this parameter, configure the HTTP callback URL and select the corresponding callback event types in the console. Otherwise, the callback settings do not take effect.
        self.user_data = user_data
        # The video ID. You can obtain the video ID by using one of the following methods:
        # - For videos uploaded through the console, log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com) and choose **Media Files** > **Audio/Video** to view the video ID.
        # - Obtain the video ID from the value of the VideoId response parameter when you call the [CreateUploadVideo](https://help.aliyun.com/document_detail/55407.html) operation to obtain the upload URL and credential.
        # - After the video is uploaded, call the [SearchMedia](https://help.aliyun.com/document_detail/86044.html) operation to query the video ID, which is the value of the VideoId response parameter.
        self.video_id = video_id
        # The snapshot width. Valid values: `[8,4096]`. Default value: the source video width. Unit: px.
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.height is not None:
            result['Height'] = self.height

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.reference_id is not None:
            result['ReferenceId'] = self.reference_id

        if self.snapshot_template_id is not None:
            result['SnapshotTemplateId'] = self.snapshot_template_id

        if self.specified_offset_time is not None:
            result['SpecifiedOffsetTime'] = self.specified_offset_time

        if self.specified_offset_times_shrink is not None:
            result['SpecifiedOffsetTimes'] = self.specified_offset_times_shrink

        if self.sprite_snapshot_config is not None:
            result['SpriteSnapshotConfig'] = self.sprite_snapshot_config

        if self.user_data is not None:
            result['UserData'] = self.user_data

        if self.video_id is not None:
            result['VideoId'] = self.video_id

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('ReferenceId') is not None:
            self.reference_id = m.get('ReferenceId')

        if m.get('SnapshotTemplateId') is not None:
            self.snapshot_template_id = m.get('SnapshotTemplateId')

        if m.get('SpecifiedOffsetTime') is not None:
            self.specified_offset_time = m.get('SpecifiedOffsetTime')

        if m.get('SpecifiedOffsetTimes') is not None:
            self.specified_offset_times_shrink = m.get('SpecifiedOffsetTimes')

        if m.get('SpriteSnapshotConfig') is not None:
            self.sprite_snapshot_config = m.get('SpriteSnapshotConfig')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

