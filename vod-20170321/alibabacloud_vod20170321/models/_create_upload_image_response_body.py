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
        # The OSS URL of the image file (without authentication).
        # 
        # When you add an image watermark template, this URL can be used as the `FileUrl` request parameter of the [AddWatermark](~~AddWatermark~~) operation.
        self.file_url = file_url
        # The image ID. This ID can be used as a request parameter for operations such as [GetImageInfo](~~GetImageInfo~~), [GetImageInfos](~~GetImageInfos~~), [UpdateImageInfos](~~UpdateImageInfos~~), and [DeleteImage](~~DeleteImage~~).
        self.image_id = image_id
        # The access URL of the image.
        # > If the returned ImageURL is inaccessible in a browser (403 error), URL authentication is enabled for your VOD domain name. Disable [URL authentication](https://help.aliyun.com/document_detail/86090.html) or [generate a signed URL](https://help.aliyun.com/document_detail/57007.html).
        self.image_url = image_url
        # The request ID.
        self.request_id = request_id
        # The upload URL.
        # 
        # > The upload URL returned by this operation is a Base64-encoded value. When you use an SDK or API to upload media assets, decode the value in Base64 before use. Only uploads by using the OSS native SDK or OSS API require you to parse UploadAddress.
        self.upload_address = upload_address
        # The upload credential.
        # > The upload credential returned by this operation is a Base64-encoded value. When you use an SDK or API to upload media assets, decode the value in Base64 before use. Only uploads by using the OSS native SDK or OSS API require you to parse UploadAuth.
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

