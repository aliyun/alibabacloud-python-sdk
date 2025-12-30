# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class ListTransferFileDownloadUrlResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        urls: List[main_models.ListTransferFileDownloadUrlResponseBodyUrls] = None,
    ):
        self.request_id = request_id
        self.urls = urls

    def validate(self):
        if self.urls:
            for v1 in self.urls:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Urls'] = []
        if self.urls is not None:
            for k1 in self.urls:
                result['Urls'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.urls = []
        if m.get('Urls') is not None:
            for k1 in m.get('Urls'):
                temp_model = main_models.ListTransferFileDownloadUrlResponseBodyUrls()
                self.urls.append(temp_model.from_map(k1))

        return self

class ListTransferFileDownloadUrlResponseBodyUrls(DaraModel):
    def __init__(
        self,
        file_id: str = None,
        file_name: str = None,
        status: str = None,
        url: str = None,
    ):
        self.file_id = file_id
        self.file_name = file_name
        self.status = status
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.status is not None:
            result['Status'] = self.status

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

