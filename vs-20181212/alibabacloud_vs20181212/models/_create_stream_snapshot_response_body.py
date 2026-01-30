# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateStreamSnapshotResponseBody(DaraModel):
    def __init__(
        self,
        format: str = None,
        height: int = None,
        id: str = None,
        oss_bucket: str = None,
        oss_endpoint: str = None,
        oss_object: str = None,
        request_id: str = None,
        timestamp: int = None,
        url: str = None,
        width: int = None,
    ):
        self.format = format
        self.height = height
        self.id = id
        self.oss_bucket = oss_bucket
        self.oss_endpoint = oss_endpoint
        self.oss_object = oss_object
        self.request_id = request_id
        self.timestamp = timestamp
        self.url = url
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.format is not None:
            result['Format'] = self.format

        if self.height is not None:
            result['Height'] = self.height

        if self.id is not None:
            result['Id'] = self.id

        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket

        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint

        if self.oss_object is not None:
            result['OssObject'] = self.oss_object

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        if self.url is not None:
            result['Url'] = self.url

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Format') is not None:
            self.format = m.get('Format')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')

        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')

        if m.get('OssObject') is not None:
            self.oss_object = m.get('OssObject')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

