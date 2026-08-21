# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteMultipartUploadRequest(DaraModel):
    def __init__(
        self,
        media_id: str = None,
        media_type: str = None,
        owner_account: str = None,
    ):
        # The media ID, which is the audio or video ID (VideoId). You can obtain the ID by using the following methods:
        # - For audio or video files uploaded through the console, log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com) and choose **Media Files** > **Audio/Video** to view the audio or video ID.
        # - When you call the [CreateUploadVideo](https://help.aliyun.com/document_detail/55407.html) operation to obtain the upload URL and credential, the audio or video ID is the value of the VideoId response parameter.
        # - After the audio or video file is uploaded, you can call the [SearchMedia](https://help.aliyun.com/document_detail/86044.html) operation to query the audio or video ID, which is the value of the VideoId response parameter.
        # 
        # This parameter is required.
        self.media_id = media_id
        # The media type. Set the value to **video** (audio/video).
        # 
        # This parameter is required.
        self.media_type = media_type
        self.owner_account = owner_account

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.media_type is not None:
            result['MediaType'] = self.media_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        return self

