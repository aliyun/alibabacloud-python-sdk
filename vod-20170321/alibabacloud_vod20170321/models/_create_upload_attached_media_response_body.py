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
        # The URL of the auxiliary media asset file. The URL is an Object Storage Service (OSS) URL and does not contain the information used for URL signing.
        # 
        # You can use specify this value for the `FileUrl` parameter when you call the [AddWatermark](~~AddWatermark~~) operation to create a watermark template.
        self.file_url = file_url
        # The ID of the auxiliary media asset.
        self.media_id = media_id
        # The URL of the auxiliary media asset.
        # 
        # If a domain name for Alibaba Cloud CDN is specified, a CDN URL is returned. Otherwise, an OSS URL is returned.
        # 
        # >  If you enable the URL signing feature of ApsaraVideo VOD, you may be unable to access the returned URL of the auxiliary media asset by using a browser and the HTTP status code 403 may be returned. To resolve this issue, you can disable the [URL signing](https://help.aliyun.com/document_detail/86090.html) feature or [generate a signed URL](https://help.aliyun.com/document_detail/57007.html).
        self.media_url = media_url
        # The ID of the request.
        self.request_id = request_id
        # The upload URL.
        # 
        # >  The upload URL returned by this operation is Base64-encoded. Before you can use an SDK or an API operation to upload a media asset based on the upload URL, you must decode the upload URL by using the Base64 algorithm. You must parse the upload URL only if you use native OSS SDKs or OSS API for uploads.
        self.upload_address = upload_address
        # The upload credential.
        # 
        # >  The upload credential returned by this operation is Base64-encoded. Before you can use an SDK or an API operation to upload a media asset based on the upload credential, you must decode the upload credential by using the Base64 algorithm. You must parse the upload credential only if you use native OSS SDKs or OSS API for uploads.
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

