# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeQuaraFileDownloadInfoResponseBody(DaraModel):
    def __init__(
        self,
        download_url: str = None,
        md_5: str = None,
        path: str = None,
        quara_file_id: int = None,
        request_id: str = None,
        tag: str = None,
        uuid: str = None,
    ):
        # The URL that is used to download the file. The URL is valid for five minutes.
        self.download_url = download_url
        # The MD5 hash value of the quarantined file.
        self.md_5 = md_5
        # The file path.
        self.path = path
        # The ID of the quarantined file.
        self.quara_file_id = quara_file_id
        # The ID of the request.
        self.request_id = request_id
        # The tag that is added to the related alert.
        self.tag = tag
        # The UUID of the server.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url

        if self.md_5 is not None:
            result['Md5'] = self.md_5

        if self.path is not None:
            result['Path'] = self.path

        if self.quara_file_id is not None:
            result['QuaraFileId'] = self.quara_file_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.tag is not None:
            result['Tag'] = self.tag

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')

        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('QuaraFileId') is not None:
            self.quara_file_id = m.get('QuaraFileId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

