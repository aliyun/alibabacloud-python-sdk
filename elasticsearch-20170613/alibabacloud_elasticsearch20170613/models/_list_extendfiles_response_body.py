# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class ListExtendfilesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.ListExtendfilesResponseBodyResult] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The returned result.
        self.result = result

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListExtendfilesResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        return self

class ListExtendfilesResponseBodyResult(DaraModel):
    def __init__(
        self,
        file_path: str = None,
        file_size: int = None,
        name: str = None,
        source_type: str = None,
    ):
        # The path of the driver file.
        self.file_path = file_path
        # The size of the driver file.
        self.file_size = file_size
        # The name of the driver file.
        self.name = name
        # The source type.
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_path is not None:
            result['filePath'] = self.file_path

        if self.file_size is not None:
            result['fileSize'] = self.file_size

        if self.name is not None:
            result['name'] = self.name

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filePath') is not None:
            self.file_path = m.get('filePath')

        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        return self

