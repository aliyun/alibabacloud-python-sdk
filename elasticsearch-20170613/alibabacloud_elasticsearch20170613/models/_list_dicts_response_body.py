# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class ListDictsResponseBody(DaraModel):
    def __init__(
        self,
        headers: main_models.ListDictsResponseBodyHeaders = None,
        request_id: str = None,
        result: List[main_models.ListDictsResponseBodyResult] = None,
    ):
        # The header of the response.
        self.headers = headers
        # The ID of the request.
        self.request_id = request_id
        # The returned result.
        self.result = result

    def validate(self):
        if self.headers:
            self.headers.validate()
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.headers is not None:
            result['Headers'] = self.headers.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Headers') is not None:
            temp_model = main_models.ListDictsResponseBodyHeaders()
            self.headers = temp_model.from_map(m.get('Headers'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListDictsResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        return self

class ListDictsResponseBodyResult(DaraModel):
    def __init__(
        self,
        download_url: str = None,
        file_size: int = None,
        name: str = None,
        source_type: str = None,
        type: str = None,
    ):
        # The link that is used to download the dictionary over the Internet. The link is valid for 90s.
        self.download_url = download_url
        # The size of the dictionary file. Unit: byte.
        self.file_size = file_size
        # The name of the dictionary file.
        self.name = name
        # The source type.
        self.source_type = source_type
        # The type of the IK dictionary. Valid values:
        # 
        # *   MAIN: main dictionary
        # *   STOP: stopword list
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.download_url is not None:
            result['downloadUrl'] = self.download_url

        if self.file_size is not None:
            result['fileSize'] = self.file_size

        if self.name is not None:
            result['name'] = self.name

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('downloadUrl') is not None:
            self.download_url = m.get('downloadUrl')

        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class ListDictsResponseBodyHeaders(DaraModel):
    def __init__(
        self,
        x_total_count: int = None,
    ):
        # The total number of entries returned.
        self.x_total_count = x_total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.x_total_count is not None:
            result['X-Total-Count'] = self.x_total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X-Total-Count') is not None:
            self.x_total_count = m.get('X-Total-Count')

        return self

