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
        # Specifies whether to forcibly delete the source file. Valid values:
        # 
        # *   **false** (default)
        # *   **true**
        # 
        # >  If a video is uploaded without transcoding or is asynchronously transcoded, the source file of the video is used for original-quality playback. By default, the source file of the video cannot be deleted. To forcibly delete the mezzanine file, set this parameter to **true**.
        self.force = force
        self.reference_ids = reference_ids
        # The IDs of audio or video files whose source files that you want to delete. You can specify up to 20 IDs. Separate multiple IDs with commas (,). You can use one of the following methods to obtain the ID:
        # 
        # *   After you upload a video in the [ApsaraVideo VOD console](https://vod.console.aliyun.com), you can log on to the ApsaraVideo VOD console and choose **Media Files** > **Audio/Video** to view the ID of the video.
        # *   Obtain the value of VideoId from the response to the [CreateUploadVideo](https://help.aliyun.com/document_detail/55407.html) operation that you called to obtain the upload URL and credential.
        # *   Obtain the value of VideoId from the response to the [SearchMedia](https://help.aliyun.com/document_detail/86044.html) operation that you called to query media information after the audio or video file is uploaded.
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

