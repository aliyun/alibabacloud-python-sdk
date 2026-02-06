# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateUploadVideoResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        upload_address: str = None,
        upload_auth: str = None,
        video_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The upload URL.
        # 
        # > The returned upload URL is a Base64-encoded URL. You must decode the Base64-encoded URL before you use an SDK or call an API operation to upload media files. You need to parse UploadAddress only if you use the Object Storage Service (OSS) SDK or call an OSS API operation to upload media files.
        self.upload_address = upload_address
        # The upload credential.
        # 
        # > The returned upload credential is a Base64-encoded value. You must decode the Base64-encoded credential before you use an SDK or call an API operation to upload media files. You need to parse UploadAuth only if you use the OSS SDK or call an OSS API operation to upload media files.
        self.upload_auth = upload_auth
        # The ID of the audio or video file. VideoId can be used as a request parameter when you call an operation for media asset management, media processing, or media review.
        self.video_id = video_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.upload_address is not None:
            result['UploadAddress'] = self.upload_address

        if self.upload_auth is not None:
            result['UploadAuth'] = self.upload_auth

        if self.video_id is not None:
            result['VideoId'] = self.video_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UploadAddress') is not None:
            self.upload_address = m.get('UploadAddress')

        if m.get('UploadAuth') is not None:
            self.upload_auth = m.get('UploadAuth')

        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')

        return self

