# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import BinaryIO

from darabonba.model import DaraModel

class SubmitConvertPdfToMarkdownJobAdvanceRequest(DaraModel):
    def __init__(
        self,
        file_name: str = None,
        file_url_object: BinaryIO = None,
        oss_bucket: str = None,
        oss_endpoint: str = None,
    ):
        self.file_name = file_name
        self.file_url_object = file_url_object
        self.oss_bucket = oss_bucket
        self.oss_endpoint = oss_endpoint

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_url_object is not None:
            result['FileUrl'] = self.file_url_object

        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket

        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileUrl') is not None:
            self.file_url_object = m.get('FileUrl')

        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')

        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')

        return self

