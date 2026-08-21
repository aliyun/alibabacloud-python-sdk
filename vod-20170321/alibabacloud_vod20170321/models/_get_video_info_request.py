# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetVideoInfoRequest(DaraModel):
    def __init__(
        self,
        reference_id: str = None,
        video_id: str = None,
    ):
        # The custom ID. Only lowercase letters, uppercase letters, digits, hyphens, and underscores are supported. The length is 6 to 64 characters. The ID is unique at the user level.
        self.reference_id = reference_id
        # The audio or video ID. Only one audio or video ID is supported. You can obtain the ID by using one of the following methods:
        # - For videos uploaded through the console, log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com) and choose **Media Files** > **Audio/Video** to view the audio or video ID.
        # - Obtain the audio or video ID from the value of the VideoId response parameter when you call the [CreateUploadVideo](https://help.aliyun.com/document_detail/55407.html) operation to obtain the upload URL and credential.
        # - After the audio or video file is uploaded, call the [SearchMedia](https://help.aliyun.com/document_detail/86044.html) operation to query the audio or video ID, which is the value of the VideoId response parameter.
        self.video_id = video_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.reference_id is not None:
            result['ReferenceId'] = self.reference_id

        if self.video_id is not None:
            result['VideoId'] = self.video_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReferenceId') is not None:
            self.reference_id = m.get('ReferenceId')

        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')

        return self

