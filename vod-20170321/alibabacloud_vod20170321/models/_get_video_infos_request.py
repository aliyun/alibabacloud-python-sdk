# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetVideoInfosRequest(DaraModel):
    def __init__(
        self,
        reference_ids: str = None,
        video_ids: str = None,
    ):
        # The list of custom IDs. Separate multiple IDs with commas (,). You can specify a maximum of 20 IDs.
        self.reference_ids = reference_ids
        # The list of audio or video IDs. Separate multiple IDs with commas (,). You can specify a maximum of 20 IDs. You can obtain the audio or video ID by using the following methods:
        # - If the video is uploaded by using the ApsaraVideo VOD console, log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com) and choose **Media Files** > **Audio/Video** to view the audio or video ID.
        # - Obtain the audio or video ID from the value of the VideoId response parameter when you call the [CreateUploadVideo](https://help.aliyun.com/document_detail/55407.html) operation to obtain the upload URL and credential.
        # - After the audio or video file is uploaded, you can call the [SearchMedia](https://help.aliyun.com/document_detail/86044.html) operation to query the audio or video ID, which is the value of the VideoId response parameter.
        self.video_ids = video_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.reference_ids is not None:
            result['ReferenceIds'] = self.reference_ids

        if self.video_ids is not None:
            result['VideoIds'] = self.video_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReferenceIds') is not None:
            self.reference_ids = m.get('ReferenceIds')

        if m.get('VideoIds') is not None:
            self.video_ids = m.get('VideoIds')

        return self

