# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_pailangstudio20240710 import models as main_models
from darabonba.model import DaraModel

class ListKnowledgeBaseChunksRequest(DaraModel):
    def __init__(
        self,
        chunk_status: str = None,
        meta_data: main_models.ListKnowledgeBaseChunksRequestMetaData = None,
        page_number: int = None,
        page_size: int = None,
        version_name: str = None,
    ):
        self.chunk_status = chunk_status
        self.meta_data = meta_data
        self.page_number = page_number
        self.page_size = page_size
        self.version_name = version_name

    def validate(self):
        if self.meta_data:
            self.meta_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chunk_status is not None:
            result['ChunkStatus'] = self.chunk_status

        if self.meta_data is not None:
            result['MetaData'] = self.meta_data.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.version_name is not None:
            result['VersionName'] = self.version_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChunkStatus') is not None:
            self.chunk_status = m.get('ChunkStatus')

        if m.get('MetaData') is not None:
            temp_model = main_models.ListKnowledgeBaseChunksRequestMetaData()
            self.meta_data = temp_model.from_map(m.get('MetaData'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')

        return self

class ListKnowledgeBaseChunksRequestMetaData(DaraModel):
    def __init__(
        self,
        file_meta_id: str = None,
        file_uri: str = None,
    ):
        # 文件元数据ID
        self.file_meta_id = file_meta_id
        # 文件地址
        self.file_uri = file_uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_meta_id is not None:
            result['FileMetaId'] = self.file_meta_id

        if self.file_uri is not None:
            result['FileUri'] = self.file_uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileMetaId') is not None:
            self.file_meta_id = m.get('FileMetaId')

        if m.get('FileUri') is not None:
            self.file_uri = m.get('FileUri')

        return self

