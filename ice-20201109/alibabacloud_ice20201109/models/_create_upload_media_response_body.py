# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateUploadMediaResponseBody(DaraModel):
    def __init__(
        self,
        file_url: str = None,
        media_id: str = None,
        media_url: str = None,
        request_id: str = None,
        upload_address: str = None,
        upload_auth: str = None,
    ):
        # The OSS URL of the file, without authentication parameters.
        self.file_url = file_url
        # The ID of the media asset.
        self.media_id = media_id
        # The URL of the media asset.
        # 
        # > This will be a CDN URL if a CDN domain is configured, or an OSS URL otherwise. If you receive a 403 error when accessing this URL in a browser, it is likely because URL authentication is enabled for the VOD domain. To resolve this, either disable URL authentication or generate a signed URL for access.
        self.media_url = media_url
        # The ID of the request.
        self.request_id = request_id
        # The upload address.
        # 
        # > The returned upload address is Base64-encoded and must be decoded before use. You only need to manually decode this address if you are using a native OSS SDK or an OSS API to perform the upload.
        self.upload_address = upload_address
        # The upload credential.
        # 
        # > The returned upload credential is Base64-encoded and must be decoded before use. You only need to manually decode this credential if you are using a native OSS SDK or an OSS API to perform the upload.
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

