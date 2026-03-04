# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateYikeAssetUploadResponseBody(DaraModel):
    def __init__(
        self,
        file_url: str = None,
        request_id: str = None,
        upload_address: str = None,
        upload_auth: str = None,
    ):
        self.file_url = file_url
        self.request_id = request_id
        self.upload_address = upload_address
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

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UploadAddress') is not None:
            self.upload_address = m.get('UploadAddress')

        if m.get('UploadAuth') is not None:
            self.upload_auth = m.get('UploadAuth')

        return self

