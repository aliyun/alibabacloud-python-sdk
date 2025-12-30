# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class ListRecognitionLibsResponseBody(DaraModel):
    def __init__(
        self,
        libs: main_models.ListRecognitionLibsResponseBodyLibs = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The recognition libraries.
        self.libs = libs
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.libs:
            self.libs.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.libs is not None:
            result['Libs'] = self.libs.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Libs') is not None:
            temp_model = main_models.ListRecognitionLibsResponseBodyLibs()
            self.libs = temp_model.from_map(m.get('Libs'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListRecognitionLibsResponseBodyLibs(DaraModel):
    def __init__(
        self,
        lib: List[main_models.ListRecognitionLibsResponseBodyLibsLib] = None,
    ):
        self.lib = lib

    def validate(self):
        if self.lib:
            for v1 in self.lib:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Lib'] = []
        if self.lib is not None:
            for k1 in self.lib:
                result['Lib'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.lib = []
        if m.get('Lib') is not None:
            for k1 in m.get('Lib'):
                temp_model = main_models.ListRecognitionLibsResponseBodyLibsLib()
                self.lib.append(temp_model.from_map(k1))

        return self

class ListRecognitionLibsResponseBodyLibsLib(DaraModel):
    def __init__(
        self,
        lib_description: str = None,
        lib_id: str = None,
        lib_name: str = None,
    ):
        # The description of the recognition library.
        self.lib_description = lib_description
        # The ID of the recognition library.
        self.lib_id = lib_id
        # The name of the recognition library.
        self.lib_name = lib_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lib_description is not None:
            result['LibDescription'] = self.lib_description

        if self.lib_id is not None:
            result['LibId'] = self.lib_id

        if self.lib_name is not None:
            result['LibName'] = self.lib_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LibDescription') is not None:
            self.lib_description = m.get('LibDescription')

        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')

        if m.get('LibName') is not None:
            self.lib_name = m.get('LibName')

        return self

