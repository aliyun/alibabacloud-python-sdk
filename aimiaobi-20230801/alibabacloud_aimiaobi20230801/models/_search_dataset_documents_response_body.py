# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class SearchDatasetDocumentsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.SearchDatasetDocumentsResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.SearchDatasetDocumentsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class SearchDatasetDocumentsResponseBodyData(DaraModel):
    def __init__(
        self,
        documents: List[main_models.SearchDatasetDocumentsResponseBodyDataDocuments] = None,
    ):
        self.documents = documents

    def validate(self):
        if self.documents:
            for v1 in self.documents:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Documents'] = []
        if self.documents is not None:
            for k1 in self.documents:
                result['Documents'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.documents = []
        if m.get('Documents') is not None:
            for k1 in m.get('Documents'):
                temp_model = main_models.SearchDatasetDocumentsResponseBodyDataDocuments()
                self.documents.append(temp_model.from_map(k1))

        return self

class SearchDatasetDocumentsResponseBodyDataDocuments(DaraModel):
    def __init__(
        self,
        category_uuid: str = None,
        chunk: str = None,
        chunk_infos: List[main_models.SearchDatasetDocumentsResponseBodyDataDocumentsChunkInfos] = None,
        content: str = None,
        doc_id: str = None,
        doc_type: str = None,
        doc_uuid: str = None,
        extend_1: str = None,
        extend_2: str = None,
        extend_3: str = None,
        pub_time: str = None,
        score: float = None,
        search_source: str = None,
        search_source_name: str = None,
        search_source_type: str = None,
        source_from: str = None,
        summary: str = None,
        tags: List[str] = None,
        title: str = None,
        url: str = None,
    ):
        self.category_uuid = category_uuid
        self.chunk = chunk
        self.chunk_infos = chunk_infos
        self.content = content
        self.doc_id = doc_id
        self.doc_type = doc_type
        self.doc_uuid = doc_uuid
        self.extend_1 = extend_1
        self.extend_2 = extend_2
        self.extend_3 = extend_3
        self.pub_time = pub_time
        self.score = score
        self.search_source = search_source
        self.search_source_name = search_source_name
        self.search_source_type = search_source_type
        self.source_from = source_from
        self.summary = summary
        self.tags = tags
        self.title = title
        self.url = url

    def validate(self):
        if self.chunk_infos:
            for v1 in self.chunk_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_uuid is not None:
            result['CategoryUuid'] = self.category_uuid

        if self.chunk is not None:
            result['Chunk'] = self.chunk

        result['ChunkInfos'] = []
        if self.chunk_infos is not None:
            for k1 in self.chunk_infos:
                result['ChunkInfos'].append(k1.to_map() if k1 else None)

        if self.content is not None:
            result['Content'] = self.content

        if self.doc_id is not None:
            result['DocId'] = self.doc_id

        if self.doc_type is not None:
            result['DocType'] = self.doc_type

        if self.doc_uuid is not None:
            result['DocUuid'] = self.doc_uuid

        if self.extend_1 is not None:
            result['Extend1'] = self.extend_1

        if self.extend_2 is not None:
            result['Extend2'] = self.extend_2

        if self.extend_3 is not None:
            result['Extend3'] = self.extend_3

        if self.pub_time is not None:
            result['PubTime'] = self.pub_time

        if self.score is not None:
            result['Score'] = self.score

        if self.search_source is not None:
            result['SearchSource'] = self.search_source

        if self.search_source_name is not None:
            result['SearchSourceName'] = self.search_source_name

        if self.search_source_type is not None:
            result['SearchSourceType'] = self.search_source_type

        if self.source_from is not None:
            result['SourceFrom'] = self.source_from

        if self.summary is not None:
            result['Summary'] = self.summary

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.title is not None:
            result['Title'] = self.title

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryUuid') is not None:
            self.category_uuid = m.get('CategoryUuid')

        if m.get('Chunk') is not None:
            self.chunk = m.get('Chunk')

        self.chunk_infos = []
        if m.get('ChunkInfos') is not None:
            for k1 in m.get('ChunkInfos'):
                temp_model = main_models.SearchDatasetDocumentsResponseBodyDataDocumentsChunkInfos()
                self.chunk_infos.append(temp_model.from_map(k1))

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('DocId') is not None:
            self.doc_id = m.get('DocId')

        if m.get('DocType') is not None:
            self.doc_type = m.get('DocType')

        if m.get('DocUuid') is not None:
            self.doc_uuid = m.get('DocUuid')

        if m.get('Extend1') is not None:
            self.extend_1 = m.get('Extend1')

        if m.get('Extend2') is not None:
            self.extend_2 = m.get('Extend2')

        if m.get('Extend3') is not None:
            self.extend_3 = m.get('Extend3')

        if m.get('PubTime') is not None:
            self.pub_time = m.get('PubTime')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('SearchSource') is not None:
            self.search_source = m.get('SearchSource')

        if m.get('SearchSourceName') is not None:
            self.search_source_name = m.get('SearchSourceName')

        if m.get('SearchSourceType') is not None:
            self.search_source_type = m.get('SearchSourceType')

        if m.get('SourceFrom') is not None:
            self.source_from = m.get('SourceFrom')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class SearchDatasetDocumentsResponseBodyDataDocumentsChunkInfos(DaraModel):
    def __init__(
        self,
        chunk: str = None,
        score: float = None,
    ):
        self.chunk = chunk
        self.score = score

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chunk is not None:
            result['Chunk'] = self.chunk

        if self.score is not None:
            result['Score'] = self.score

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Chunk') is not None:
            self.chunk = m.get('Chunk')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        return self

