# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class ListChunksResponseBody(DaraModel):
    def __init__(
        self,
        chunks: main_models.ListChunksResponseBodyChunks = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        self.chunks = chunks
        self.page_number = page_number
        self.page_record_count = page_record_count
        self.request_id = request_id
        self.total_record_count = total_record_count

    def validate(self):
        if self.chunks:
            self.chunks.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chunks is not None:
            result['Chunks'] = self.chunks.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Chunks') is not None:
            temp_model = main_models.ListChunksResponseBodyChunks()
            self.chunks = temp_model.from_map(m.get('Chunks'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class ListChunksResponseBodyChunks(DaraModel):
    def __init__(
        self,
        chunks: List[main_models.ListChunksResponseBodyChunksChunks] = None,
    ):
        self.chunks = chunks

    def validate(self):
        if self.chunks:
            for v1 in self.chunks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['chunks'] = []
        if self.chunks is not None:
            for k1 in self.chunks:
                result['chunks'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.chunks = []
        if m.get('chunks') is not None:
            for k1 in m.get('chunks'):
                temp_model = main_models.ListChunksResponseBodyChunksChunks()
                self.chunks.append(temp_model.from_map(k1))

        return self

class ListChunksResponseBodyChunksChunks(DaraModel):
    def __init__(
        self,
        content: str = None,
        file_name: str = None,
        id: str = None,
        loader_metadata: str = None,
        metadata: Dict[str, Any] = None,
        page_index: int = None,
        vector: main_models.ListChunksResponseBodyChunksChunksVector = None,
    ):
        self.content = content
        self.file_name = file_name
        self.id = id
        self.loader_metadata = loader_metadata
        self.metadata = metadata
        self.page_index = page_index
        self.vector = vector

    def validate(self):
        if self.vector:
            self.vector.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.id is not None:
            result['Id'] = self.id

        if self.loader_metadata is not None:
            result['LoaderMetadata'] = self.loader_metadata

        if self.metadata is not None:
            result['Metadata'] = self.metadata

        if self.page_index is not None:
            result['PageIndex'] = self.page_index

        if self.vector is not None:
            result['Vector'] = self.vector.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LoaderMetadata') is not None:
            self.loader_metadata = m.get('LoaderMetadata')

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')

        if m.get('Vector') is not None:
            temp_model = main_models.ListChunksResponseBodyChunksChunksVector()
            self.vector = temp_model.from_map(m.get('Vector'))

        return self

class ListChunksResponseBodyChunksChunksVector(DaraModel):
    def __init__(
        self,
        vector: List[float] = None,
    ):
        self.vector = vector

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.vector is not None:
            result['vector'] = self.vector

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('vector') is not None:
            self.vector = m.get('vector')

        return self

