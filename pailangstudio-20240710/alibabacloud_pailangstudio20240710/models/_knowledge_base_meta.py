# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pailangstudio20240710 import models as main_models
from darabonba.model import DaraModel

class KnowledgeBaseMeta(DaraModel):
    def __init__(
        self,
        chunk_attachment: List[main_models.KnowledgeBaseMetaChunkAttachment] = None,
        chunk_content: str = None,
        chunk_end: int = None,
        chunk_id: str = None,
        chunk_sequence: int = None,
        chunk_size: int = None,
        chunk_start: int = None,
        chunk_status: str = None,
        download_url: str = None,
        file_content_type: str = None,
        file_create_time: str = None,
        file_meta_data: str = None,
        file_meta_id: str = None,
        file_name: str = None,
        file_size: int = None,
        file_status: str = None,
        file_type: str = None,
        file_update_time: str = None,
        file_uri: str = None,
        meta_data: main_models.KnowledgeBaseMetaMetaData = None,
        thumbnail_url: str = None,
    ):
        self.chunk_attachment = chunk_attachment
        self.chunk_content = chunk_content
        self.chunk_end = chunk_end
        self.chunk_id = chunk_id
        self.chunk_sequence = chunk_sequence
        self.chunk_size = chunk_size
        self.chunk_start = chunk_start
        self.chunk_status = chunk_status
        self.download_url = download_url
        self.file_content_type = file_content_type
        self.file_create_time = file_create_time
        self.file_meta_data = file_meta_data
        self.file_meta_id = file_meta_id
        self.file_name = file_name
        self.file_size = file_size
        self.file_status = file_status
        self.file_type = file_type
        self.file_update_time = file_update_time
        self.file_uri = file_uri
        self.meta_data = meta_data
        self.thumbnail_url = thumbnail_url

    def validate(self):
        if self.chunk_attachment:
            for v1 in self.chunk_attachment:
                 if v1:
                    v1.validate()
        if self.meta_data:
            self.meta_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ChunkAttachment'] = []
        if self.chunk_attachment is not None:
            for k1 in self.chunk_attachment:
                result['ChunkAttachment'].append(k1.to_map() if k1 else None)

        if self.chunk_content is not None:
            result['ChunkContent'] = self.chunk_content

        if self.chunk_end is not None:
            result['ChunkEnd'] = self.chunk_end

        if self.chunk_id is not None:
            result['ChunkId'] = self.chunk_id

        if self.chunk_sequence is not None:
            result['ChunkSequence'] = self.chunk_sequence

        if self.chunk_size is not None:
            result['ChunkSize'] = self.chunk_size

        if self.chunk_start is not None:
            result['ChunkStart'] = self.chunk_start

        if self.chunk_status is not None:
            result['ChunkStatus'] = self.chunk_status

        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url

        if self.file_content_type is not None:
            result['FileContentType'] = self.file_content_type

        if self.file_create_time is not None:
            result['FileCreateTime'] = self.file_create_time

        if self.file_meta_data is not None:
            result['FileMetaData'] = self.file_meta_data

        if self.file_meta_id is not None:
            result['FileMetaId'] = self.file_meta_id

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_size is not None:
            result['FileSize'] = self.file_size

        if self.file_status is not None:
            result['FileStatus'] = self.file_status

        if self.file_type is not None:
            result['FileType'] = self.file_type

        if self.file_update_time is not None:
            result['FileUpdateTime'] = self.file_update_time

        if self.file_uri is not None:
            result['FileUri'] = self.file_uri

        if self.meta_data is not None:
            result['MetaData'] = self.meta_data.to_map()

        if self.thumbnail_url is not None:
            result['ThumbnailUrl'] = self.thumbnail_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.chunk_attachment = []
        if m.get('ChunkAttachment') is not None:
            for k1 in m.get('ChunkAttachment'):
                temp_model = main_models.KnowledgeBaseMetaChunkAttachment()
                self.chunk_attachment.append(temp_model.from_map(k1))

        if m.get('ChunkContent') is not None:
            self.chunk_content = m.get('ChunkContent')

        if m.get('ChunkEnd') is not None:
            self.chunk_end = m.get('ChunkEnd')

        if m.get('ChunkId') is not None:
            self.chunk_id = m.get('ChunkId')

        if m.get('ChunkSequence') is not None:
            self.chunk_sequence = m.get('ChunkSequence')

        if m.get('ChunkSize') is not None:
            self.chunk_size = m.get('ChunkSize')

        if m.get('ChunkStart') is not None:
            self.chunk_start = m.get('ChunkStart')

        if m.get('ChunkStatus') is not None:
            self.chunk_status = m.get('ChunkStatus')

        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')

        if m.get('FileContentType') is not None:
            self.file_content_type = m.get('FileContentType')

        if m.get('FileCreateTime') is not None:
            self.file_create_time = m.get('FileCreateTime')

        if m.get('FileMetaData') is not None:
            self.file_meta_data = m.get('FileMetaData')

        if m.get('FileMetaId') is not None:
            self.file_meta_id = m.get('FileMetaId')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')

        if m.get('FileStatus') is not None:
            self.file_status = m.get('FileStatus')

        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')

        if m.get('FileUpdateTime') is not None:
            self.file_update_time = m.get('FileUpdateTime')

        if m.get('FileUri') is not None:
            self.file_uri = m.get('FileUri')

        if m.get('MetaData') is not None:
            temp_model = main_models.KnowledgeBaseMetaMetaData()
            self.meta_data = temp_model.from_map(m.get('MetaData'))

        if m.get('ThumbnailUrl') is not None:
            self.thumbnail_url = m.get('ThumbnailUrl')

        return self

class KnowledgeBaseMetaMetaData(DaraModel):
    def __init__(
        self,
        file_meta_id: str = None,
        file_name: str = None,
        file_uri: str = None,
    ):
        self.file_meta_id = file_meta_id
        self.file_name = file_name
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

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_uri is not None:
            result['FileUri'] = self.file_uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileMetaId') is not None:
            self.file_meta_id = m.get('FileMetaId')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileUri') is not None:
            self.file_uri = m.get('FileUri')

        return self

class KnowledgeBaseMetaChunkAttachment(DaraModel):
    def __init__(
        self,
        download_url: str = None,
        placeholder_id: str = None,
        type: str = None,
        uri: str = None,
    ):
        self.download_url = download_url
        self.placeholder_id = placeholder_id
        self.type = type
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url

        if self.placeholder_id is not None:
            result['PlaceholderId'] = self.placeholder_id

        if self.type is not None:
            result['Type'] = self.type

        if self.uri is not None:
            result['Uri'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')

        if m.get('PlaceholderId') is not None:
            self.placeholder_id = m.get('PlaceholderId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Uri') is not None:
            self.uri = m.get('Uri')

        return self

