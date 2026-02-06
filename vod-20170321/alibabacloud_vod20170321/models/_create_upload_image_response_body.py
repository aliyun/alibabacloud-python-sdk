# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateUploadImageResponseBody(DaraModel):
    def __init__(
        self,
        file_url: str = None,
        image_id: str = None,
        image_url: str = None,
        request_id: str = None,
        upload_address: str = None,
        upload_auth: str = None,
    ):
        # The OSS URL of the file. The URL does not contain the information used for URL signing. You can specify FileUrl when you call the [AddWatermark](https://help.aliyun.com/document_detail/98617.html) operation.
        self.file_url = file_url
        # The ID of the image file.
        self.image_id = image_id
        # The URL of the image.
        # 
        # > If the returned URL is inaccessible from a browser and the HTTP 403 status code is returned, the URL signing feature in ApsaraVideo VOD is enabled. To resolve this issue, you can disable the [URL signing](https://help.aliyun.com/document_detail/86090.html) feature or [generate a signed URL](https://help.aliyun.com/document_detail/57007.html).
        self.image_url = image_url
        # The ID of the request.
        self.request_id = request_id
        # The upload URL.
        # 
        # > The returned upload URL is a Base64-encoded URL. You must decode the Base64-encoded URL before you use an SDK or call an API operation to upload auxiliary media assets. You need to parse UploadAddress only if you use the OSS SDK or call an OSS API operation to upload auxiliary media assets.
        self.upload_address = upload_address
        # The upload credential.
        # 
        # > The returned upload credential is a Base64-encoded value. You must decode the Base64-encoded credential before you use an SDK or call an API operation to upload auxiliary media assets. You need to parse UploadAuth only if you use the OSS SDK or call an OSS API operation to upload auxiliary media assets.
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

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_url is not None:
            result['ImageURL'] = self.image_url

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

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UploadAddress') is not None:
            self.upload_address = m.get('UploadAddress')

        if m.get('UploadAuth') is not None:
            self.upload_auth = m.get('UploadAuth')

        return self

