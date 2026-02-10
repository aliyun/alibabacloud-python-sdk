# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDynamicDictResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        file_name: str = None,
        file_size: int = None,
        limit: int = None,
        oss_url: str = None,
        request_id: str = None,
        upload_time: int = None,
    ):
        # The number of weak password rules that are added.
        self.count = count
        # The name of the OSS object that contains custom weak passwords.
        self.file_name = file_name
        # The size of the OSS object. Unit: bytes.
        self.file_size = file_size
        # The maximum number of weak password rules that can be added.
        self.limit = limit
        # The IP address of the Object Storage Service (OSS) object.
        self.oss_url = oss_url
        # The request ID.
        self.request_id = request_id
        # The timestamp when the OSS object was uploaded. Unit: milliseconds.
        self.upload_time = upload_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_size is not None:
            result['FileSize'] = self.file_size

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.oss_url is not None:
            result['OssUrl'] = self.oss_url

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.upload_time is not None:
            result['UploadTime'] = self.upload_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('OssUrl') is not None:
            self.oss_url = m.get('OssUrl')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UploadTime') is not None:
            self.upload_time = m.get('UploadTime')

        return self

