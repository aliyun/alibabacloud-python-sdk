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
        # The request ID.
        self.request_id = request_id
        # The upload URL.
        # 
        # > The upload URL returned by this operation is a Base64-encoded value. When you use an SDK or API to upload media assets, you must Base64-decode the value before use. Only uploads by using the native OSS SDK or OSS API require you to parse UploadAddress.
        self.upload_address = upload_address
        # The upload credential.
        # 
        # > The upload credential returned by this operation is a Base64-encoded value. When you use an SDK or API to upload media assets, you must Base64-decode the value before use. Only uploads by using the native OSS SDK or OSS API require you to parse UploadAuth.
        self.upload_auth = upload_auth
        # The audio or video ID. This ID can be used as a request parameter for media asset management, media processing, and content moderation operations.
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

