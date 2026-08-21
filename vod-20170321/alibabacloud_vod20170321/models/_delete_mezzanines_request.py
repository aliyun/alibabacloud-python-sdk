# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteMezzaninesRequest(DaraModel):
    def __init__(
        self,
        force: bool = None,
        reference_ids: str = None,
        video_ids: str = None,
    ):
        # Specifies whether to force delete the source file. Valid values:
        # - **false** (default): No.
        # - **true**: Yes.
        # 
        # > If the video transcoding pattern is set to no transcoding or asynchronous transcoding, the source file is used as the original stream for playback and cannot be deleted by default. To force delete the source file of such a video, go to Settings and set this parameter to **true**.
        self.force = force
        # The list of custom IDs. Specify one or more custom IDs separated by commas (,). A maximum of 20 IDs are supported.
        self.reference_ids = reference_ids
        # The list of audio or video IDs whose source files you want to delete. You can specify a maximum of 20 IDs at a time. Separate multiple IDs with commas (,). You can obtain the IDs by using the following methods:
        # - For audio or video files uploaded through the console, log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com) and choose **Media Files** > **Audio/Video** to view the audio or video IDs.
        # - When you call the [CreateUploadVideo](https://help.aliyun.com/document_detail/55407.html) operation to obtain the upload URL and credential, the audio or video ID is the value of the VideoId response parameter.
        # - After the audio or video file is uploaded, you can call the [SearchMedia](https://help.aliyun.com/document_detail/86044.html) operation to query the audio or video ID, which is the value of the VideoId response parameter.
        self.video_ids = video_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.force is not None:
            result['Force'] = self.force

        if self.reference_ids is not None:
            result['ReferenceIds'] = self.reference_ids

        if self.video_ids is not None:
            result['VideoIds'] = self.video_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Force') is not None:
            self.force = m.get('Force')

        if m.get('ReferenceIds') is not None:
            self.reference_ids = m.get('ReferenceIds')

        if m.get('VideoIds') is not None:
            self.video_ids = m.get('VideoIds')

        return self

