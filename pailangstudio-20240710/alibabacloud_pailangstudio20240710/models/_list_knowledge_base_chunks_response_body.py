# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pailangstudio20240710 import models as main_models
from darabonba.model import DaraModel

class ListKnowledgeBaseChunksResponseBody(DaraModel):
    def __init__(
        self,
        knowledge_base_chunks: List[main_models.ListKnowledgeBaseChunksResponseBodyKnowledgeBaseChunks] = None,
        max_results: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # 切片列表
        self.knowledge_base_chunks = knowledge_base_chunks
        self.max_results = max_results
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.knowledge_base_chunks:
            for v1 in self.knowledge_base_chunks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['KnowledgeBaseChunks'] = []
        if self.knowledge_base_chunks is not None:
            for k1 in self.knowledge_base_chunks:
                result['KnowledgeBaseChunks'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.knowledge_base_chunks = []
        if m.get('KnowledgeBaseChunks') is not None:
            for k1 in m.get('KnowledgeBaseChunks'):
                temp_model = main_models.ListKnowledgeBaseChunksResponseBodyKnowledgeBaseChunks()
                self.knowledge_base_chunks.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListKnowledgeBaseChunksResponseBodyKnowledgeBaseChunks(DaraModel):
    def __init__(
        self,
        chunk_attachment: List[main_models.ListKnowledgeBaseChunksResponseBodyKnowledgeBaseChunksChunkAttachment] = None,
        chunk_content: str = None,
        chunk_end: int = None,
        chunk_sequence: int = None,
        chunk_size: int = None,
        chunk_start: int = None,
        chunk_status: str = None,
        download_url: str = None,
        knowledge_base_chunk_id: str = None,
        knowledge_base_id: str = None,
        meta_data: main_models.ListKnowledgeBaseChunksResponseBodyKnowledgeBaseChunksMetaData = None,
        thumbnail_url: str = None,
        version_name: str = None,
    ):
        # 切片附属信息
        self.chunk_attachment = chunk_attachment
        # 切片内容
        self.chunk_content = chunk_content
        # 切片结束位置
        self.chunk_end = chunk_end
        # 切片顺序
        self.chunk_sequence = chunk_sequence
        # 切片大小
        self.chunk_size = chunk_size
        # 切片起始位置
        self.chunk_start = chunk_start
        # 切片状态
        self.chunk_status = chunk_status
        # 切片下载地址
        self.download_url = download_url
        # 切片ID
        self.knowledge_base_chunk_id = knowledge_base_chunk_id
        # 知识库ID
        self.knowledge_base_id = knowledge_base_id
        # 原始文件信息
        self.meta_data = meta_data
        # 切片缩略图
        self.thumbnail_url = thumbnail_url
        # 知识库版本
        self.version_name = version_name

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

        if self.knowledge_base_chunk_id is not None:
            result['KnowledgeBaseChunkId'] = self.knowledge_base_chunk_id

        if self.knowledge_base_id is not None:
            result['KnowledgeBaseId'] = self.knowledge_base_id

        if self.meta_data is not None:
            result['MetaData'] = self.meta_data.to_map()

        if self.thumbnail_url is not None:
            result['ThumbnailUrl'] = self.thumbnail_url

        if self.version_name is not None:
            result['VersionName'] = self.version_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.chunk_attachment = []
        if m.get('ChunkAttachment') is not None:
            for k1 in m.get('ChunkAttachment'):
                temp_model = main_models.ListKnowledgeBaseChunksResponseBodyKnowledgeBaseChunksChunkAttachment()
                self.chunk_attachment.append(temp_model.from_map(k1))

        if m.get('ChunkContent') is not None:
            self.chunk_content = m.get('ChunkContent')

        if m.get('ChunkEnd') is not None:
            self.chunk_end = m.get('ChunkEnd')

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

        if m.get('KnowledgeBaseChunkId') is not None:
            self.knowledge_base_chunk_id = m.get('KnowledgeBaseChunkId')

        if m.get('KnowledgeBaseId') is not None:
            self.knowledge_base_id = m.get('KnowledgeBaseId')

        if m.get('MetaData') is not None:
            temp_model = main_models.ListKnowledgeBaseChunksResponseBodyKnowledgeBaseChunksMetaData()
            self.meta_data = temp_model.from_map(m.get('MetaData'))

        if m.get('ThumbnailUrl') is not None:
            self.thumbnail_url = m.get('ThumbnailUrl')

        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')

        return self

class ListKnowledgeBaseChunksResponseBodyKnowledgeBaseChunksMetaData(DaraModel):
    def __init__(
        self,
        file_meta_id: str = None,
        file_name: str = None,
        file_uri: str = None,
    ):
        # 文件元数据ID
        self.file_meta_id = file_meta_id
        # 文件名
        self.file_name = file_name
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

class ListKnowledgeBaseChunksResponseBodyKnowledgeBaseChunksChunkAttachment(DaraModel):
    def __init__(
        self,
        download_url: str = None,
        placeholder_id: str = None,
        type: str = None,
        uri: str = None,
    ):
        # 下载地址
        self.download_url = download_url
        # 占位符ID
        self.placeholder_id = placeholder_id
        # 类型
        self.type = type
        # 路径
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

