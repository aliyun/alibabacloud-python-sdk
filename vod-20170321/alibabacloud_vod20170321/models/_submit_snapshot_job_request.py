# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SubmitSnapshotJobRequest(DaraModel):
    def __init__(
        self,
        count: int = None,
        height: str = None,
        interval: int = None,
        reference_id: str = None,
        snapshot_template_id: str = None,
        specified_offset_time: int = None,
        specified_offset_times: List[int] = None,
        sprite_snapshot_config: str = None,
        user_data: str = None,
        video_id: str = None,
        width: str = None,
    ):
        # The maximum number of snapshots. Default value: **1**.
        self.count = count
        # The height of each snapshot. Valid values: `[8,4096]`. By default, the height of the video source is used. Unit: pixels.
        self.height = height
        # The snapshot interval. The value must be **greater than or equal to 0**.
        # 
        # *   Unit: seconds.
        # *   Default value: **1**.
        # *   If you set this parameter to **0**, snapshots are captured at even intervals based on the video duration divided by the value of the Count parameter.
        self.interval = interval
        self.reference_id = reference_id
        # The ID of the snapshot template.
        # 
        # *   We recommend that you create a snapshot template before you specify the template ID. For more information about how to create a snapshot template, see [AddVodTemplate](https://help.aliyun.com/document_detail/99406.html).
        # *   If you set the SnapshotTemplateId parameter, all the other request parameters except the Action and VideoId parameters are ignored.
        self.snapshot_template_id = snapshot_template_id
        # The point in time when the first snapshot is captured.
        # 
        # *   Unit: milliseconds.
        # *   Default value: **0**.
        self.specified_offset_time = specified_offset_time
        # The playback positions at which you want to capture snapshots. Unit: milliseconds. You can specify up to 30 playback positions in a request.
        self.specified_offset_times = specified_offset_times
        # The sprite snapshot configuration. If you set this parameter, sprite snapshots are generated. For more information, see [SpriteSnapshotConfig](https://help.aliyun.com/document_detail/86952.html).
        self.sprite_snapshot_config = sprite_snapshot_config
        # The custom configurations including the configuration of transparent data transmission and callback configurations. The value must be a JSON string. For more information, see [UserData](https://help.aliyun.com/document_detail/86952.html).
        # 
        # >  To use the message callback feature, you must specify an HTTP callback URL and the callback events in the ApsaraVideo VOD console. Otherwise, the callback settings do not take effect.
        self.user_data = user_data
        # The ID of the video. You can use one of the following methods to obtain the ID:
        # 
        # *   After you upload a video in the ApsaraVideo VOD console, you can log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com) and choose **Media Files** > **Audio/Video** to view the ID of the video.
        # *   Obtain the video ID from the response to the [CreateUploadVideo](https://help.aliyun.com/document_detail/55407.html) operation that you called to obtain the upload URL and credential.
        # *   Obtain the video ID from the response to the [SearchMedia](https://help.aliyun.com/document_detail/86044.html) operation that you called to query media information after the audio or video file is uploaded.
        self.video_id = video_id
        # The width of each snapshot. Valid values: `[8,4096]`. By default, the width of the video source is used. Unit: pixels.
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

        if self.specified_offset_times is not None:
            result['SpecifiedOffsetTimes'] = self.specified_offset_times

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
            self.specified_offset_times = m.get('SpecifiedOffsetTimes')

        if m.get('SpriteSnapshotConfig') is not None:
            self.sprite_snapshot_config = m.get('SpriteSnapshotConfig')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

