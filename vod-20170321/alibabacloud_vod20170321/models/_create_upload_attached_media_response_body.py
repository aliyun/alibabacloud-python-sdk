# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateUploadAttachedMediaResponseBody(DaraModel):
    def __init__(
        self,
        file_url: str = None,
        media_id: str = None,
        media_url: str = None,
        request_id: str = None,
        upload_address: str = None,
        upload_auth: str = None,
    ):
        # The OSS URL of the auxiliary media asset file (without authentication).
        # 
        # When you add an image watermark template, this URL can be used as the request parameter `FileUrl` of the [AddWatermark](~~AddWatermark~~) operation.
        self.file_url = file_url
        # The media asset ID.
        self.media_id = media_id
        # The access URL of the media asset.
        # 
        # If a CDN domain name is configured, a CDN URL is returned. Otherwise, an OSS URL is returned.
        # 
        # > If the returned MediaURL is inaccessible in a browser (403), you have enabled URL authentication for the VOD domain name. You can disable [URL authentication](https://help.aliyun.com/document_detail/86090.html) or [generate an authentication signature](https://help.aliyun.com/document_detail/57007.html) yourself.
        self.media_url = media_url
        # The request ID.
        self.request_id = request_id
        # The upload URL.
        # > The upload URL returned by the operation is a Base64-encoded value. When you use the SDK or API to upload media assets, you must Base64-decode the value before use. Only uploads by using the OSS native SDK or OSS API require you to parse UploadAddress yourself.
        self.upload_address = upload_address
        # The upload credential.
        # 
        # > The upload credential returned by the operation is a Base64-encoded value. When you use the SDK or API to upload media assets, you must Base64-decode the value before use. Only uploads by using the OSS native SDK or OSS API require you to parse UploadAuth yourself.
        self.upload_auth = upload_auth

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_url is not None:
            result['FileURL'] = self.file_url

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.media_url is not None:
            result['MediaURL'] = self.media_url

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.upload_address is not None:
            result['UploadAddress'] = self.upload_address

        if self.upload_auth is not None:
            result['UploadAuth'] = self.upload_auth

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileURL') is not None:
            self.file_url = m.get('FileURL')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('MediaURL') is not None:
            self.media_url = m.get('MediaURL')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UploadAddress') is not None:
            self.upload_address = m.get('UploadAddress')

        if m.get('UploadAuth') is not None:
            self.upload_auth = m.get('UploadAuth')

        return self

