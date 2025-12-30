# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_dianjin20240628 import models as main_models
from darabonba.model import DaraModel

class RecallDocumentResponseBody(DaraModel):
    def __init__(
        self,
        cost: int = None,
        data: main_models.RecallDocumentResponseBodyData = None,
        data_type: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        time: str = None,
    ):
        self.cost = cost
        self.data = data
        self.data_type = data_type
        self.err_code = err_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.time = time

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cost is not None:
            result['cost'] = self.cost

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.data_type is not None:
            result['dataType'] = self.data_type

        if self.err_code is not None:
            result['errCode'] = self.err_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        if self.time is not None:
            result['time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            self.cost = m.get('cost')

        if m.get('data') is not None:
            temp_model = main_models.RecallDocumentResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')

        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('time') is not None:
            self.time = m.get('time')

        return self

class RecallDocumentResponseBodyData(DaraModel):
    def __init__(
        self,
        chunk_list: List[main_models.RecallDocumentResponseBodyDataChunkList] = None,
        chunk_part_list: List[main_models.RecallDocumentResponseBodyDataChunkPartList] = None,
        chunk_text_list: List[str] = None,
        documents: List[main_models.RecallDocumentResponseBodyDataDocuments] = None,
        embedding_elapsed_ms: int = None,
        text_chunk_list: List[main_models.RecallDocumentResponseBodyDataTextChunkList] = None,
        text_search_elapsed_ms: int = None,
        total_elapsed_ms: int = None,
        vector_chunk_list: List[main_models.RecallDocumentResponseBodyDataVectorChunkList] = None,
        vector_search_elapsed_ms: int = None,
    ):
        self.chunk_list = chunk_list
        self.chunk_part_list = chunk_part_list
        self.chunk_text_list = chunk_text_list
        self.documents = documents
        self.embedding_elapsed_ms = embedding_elapsed_ms
        self.text_chunk_list = text_chunk_list
        self.text_search_elapsed_ms = text_search_elapsed_ms
        self.total_elapsed_ms = total_elapsed_ms
        self.vector_chunk_list = vector_chunk_list
        self.vector_search_elapsed_ms = vector_search_elapsed_ms

    def validate(self):
        if self.chunk_list:
            for v1 in self.chunk_list:
                 if v1:
                    v1.validate()
        if self.chunk_part_list:
            for v1 in self.chunk_part_list:
                 if v1:
                    v1.validate()
        if self.documents:
            for v1 in self.documents:
                 if v1:
                    v1.validate()
        if self.text_chunk_list:
            for v1 in self.text_chunk_list:
                 if v1:
                    v1.validate()
        if self.vector_chunk_list:
            for v1 in self.vector_chunk_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['chunkList'] = []
        if self.chunk_list is not None:
            for k1 in self.chunk_list:
                result['chunkList'].append(k1.to_map() if k1 else None)

        result['chunkPartList'] = []
        if self.chunk_part_list is not None:
            for k1 in self.chunk_part_list:
                result['chunkPartList'].append(k1.to_map() if k1 else None)

        if self.chunk_text_list is not None:
            result['chunkTextList'] = self.chunk_text_list

        result['documents'] = []
        if self.documents is not None:
            for k1 in self.documents:
                result['documents'].append(k1.to_map() if k1 else None)

        if self.embedding_elapsed_ms is not None:
            result['embeddingElapsedMs'] = self.embedding_elapsed_ms

        result['textChunkList'] = []
        if self.text_chunk_list is not None:
            for k1 in self.text_chunk_list:
                result['textChunkList'].append(k1.to_map() if k1 else None)

        if self.text_search_elapsed_ms is not None:
            result['textSearchElapsedMs'] = self.text_search_elapsed_ms

        if self.total_elapsed_ms is not None:
            result['totalElapsedMs'] = self.total_elapsed_ms

        result['vectorChunkList'] = []
        if self.vector_chunk_list is not None:
            for k1 in self.vector_chunk_list:
                result['vectorChunkList'].append(k1.to_map() if k1 else None)

        if self.vector_search_elapsed_ms is not None:
            result['vectorSearchElapsedMs'] = self.vector_search_elapsed_ms

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.chunk_list = []
        if m.get('chunkList') is not None:
            for k1 in m.get('chunkList'):
                temp_model = main_models.RecallDocumentResponseBodyDataChunkList()
                self.chunk_list.append(temp_model.from_map(k1))

        self.chunk_part_list = []
        if m.get('chunkPartList') is not None:
            for k1 in m.get('chunkPartList'):
                temp_model = main_models.RecallDocumentResponseBodyDataChunkPartList()
                self.chunk_part_list.append(temp_model.from_map(k1))

        if m.get('chunkTextList') is not None:
            self.chunk_text_list = m.get('chunkTextList')

        self.documents = []
        if m.get('documents') is not None:
            for k1 in m.get('documents'):
                temp_model = main_models.RecallDocumentResponseBodyDataDocuments()
                self.documents.append(temp_model.from_map(k1))

        if m.get('embeddingElapsedMs') is not None:
            self.embedding_elapsed_ms = m.get('embeddingElapsedMs')

        self.text_chunk_list = []
        if m.get('textChunkList') is not None:
            for k1 in m.get('textChunkList'):
                temp_model = main_models.RecallDocumentResponseBodyDataTextChunkList()
                self.text_chunk_list.append(temp_model.from_map(k1))

        if m.get('textSearchElapsedMs') is not None:
            self.text_search_elapsed_ms = m.get('textSearchElapsedMs')

        if m.get('totalElapsedMs') is not None:
            self.total_elapsed_ms = m.get('totalElapsedMs')

        self.vector_chunk_list = []
        if m.get('vectorChunkList') is not None:
            for k1 in m.get('vectorChunkList'):
                temp_model = main_models.RecallDocumentResponseBodyDataVectorChunkList()
                self.vector_chunk_list.append(temp_model.from_map(k1))

        if m.get('vectorSearchElapsedMs') is not None:
            self.vector_search_elapsed_ms = m.get('vectorSearchElapsedMs')

        return self

class RecallDocumentResponseBodyDataVectorChunkList(DaraModel):
    def __init__(
        self,
        chunk_id: str = None,
        chunk_meta: Dict[str, Any] = None,
        chunk_oss_url: str = None,
        chunk_text: str = None,
        chunk_type: str = None,
        doc_id: str = None,
        file_type: str = None,
        library_id: str = None,
        library_name: str = None,
        next_chunk_id: str = None,
        pos: List[main_models.RecallDocumentResponseBodyDataVectorChunkListPos] = None,
        pre_chunk_id: str = None,
        score: float = None,
        title: str = None,
    ):
        self.chunk_id = chunk_id
        self.chunk_meta = chunk_meta
        self.chunk_oss_url = chunk_oss_url
        self.chunk_text = chunk_text
        self.chunk_type = chunk_type
        self.doc_id = doc_id
        self.file_type = file_type
        self.library_id = library_id
        self.library_name = library_name
        self.next_chunk_id = next_chunk_id
        self.pos = pos
        self.pre_chunk_id = pre_chunk_id
        self.score = score
        self.title = title

    def validate(self):
        if self.pos:
            for v1 in self.pos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chunk_id is not None:
            result['chunkId'] = self.chunk_id

        if self.chunk_meta is not None:
            result['chunkMeta'] = self.chunk_meta

        if self.chunk_oss_url is not None:
            result['chunkOssUrl'] = self.chunk_oss_url

        if self.chunk_text is not None:
            result['chunkText'] = self.chunk_text

        if self.chunk_type is not None:
            result['chunkType'] = self.chunk_type

        if self.doc_id is not None:
            result['docId'] = self.doc_id

        if self.file_type is not None:
            result['fileType'] = self.file_type

        if self.library_id is not None:
            result['libraryId'] = self.library_id

        if self.library_name is not None:
            result['libraryName'] = self.library_name

        if self.next_chunk_id is not None:
            result['nextChunkId'] = self.next_chunk_id

        result['pos'] = []
        if self.pos is not None:
            for k1 in self.pos:
                result['pos'].append(k1.to_map() if k1 else None)

        if self.pre_chunk_id is not None:
            result['preChunkId'] = self.pre_chunk_id

        if self.score is not None:
            result['score'] = self.score

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chunkId') is not None:
            self.chunk_id = m.get('chunkId')

        if m.get('chunkMeta') is not None:
            self.chunk_meta = m.get('chunkMeta')

        if m.get('chunkOssUrl') is not None:
            self.chunk_oss_url = m.get('chunkOssUrl')

        if m.get('chunkText') is not None:
            self.chunk_text = m.get('chunkText')

        if m.get('chunkType') is not None:
            self.chunk_type = m.get('chunkType')

        if m.get('docId') is not None:
            self.doc_id = m.get('docId')

        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')

        if m.get('libraryId') is not None:
            self.library_id = m.get('libraryId')

        if m.get('libraryName') is not None:
            self.library_name = m.get('libraryName')

        if m.get('nextChunkId') is not None:
            self.next_chunk_id = m.get('nextChunkId')

        self.pos = []
        if m.get('pos') is not None:
            for k1 in m.get('pos'):
                temp_model = main_models.RecallDocumentResponseBodyDataVectorChunkListPos()
                self.pos.append(temp_model.from_map(k1))

        if m.get('preChunkId') is not None:
            self.pre_chunk_id = m.get('preChunkId')

        if m.get('score') is not None:
            self.score = m.get('score')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class RecallDocumentResponseBodyDataVectorChunkListPos(DaraModel):
    def __init__(
        self,
        axis_array: List[float] = None,
        page: int = None,
        text_highlight_area: List[int] = None,
    ):
        self.axis_array = axis_array
        self.page = page
        self.text_highlight_area = text_highlight_area

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.axis_array is not None:
            result['axisArray'] = self.axis_array

        if self.page is not None:
            result['page'] = self.page

        if self.text_highlight_area is not None:
            result['textHighlightArea'] = self.text_highlight_area

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('axisArray') is not None:
            self.axis_array = m.get('axisArray')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('textHighlightArea') is not None:
            self.text_highlight_area = m.get('textHighlightArea')

        return self

class RecallDocumentResponseBodyDataTextChunkList(DaraModel):
    def __init__(
        self,
        chunk_id: str = None,
        chunk_meta: Dict[str, Any] = None,
        chunk_oss_url: str = None,
        chunk_text: str = None,
        chunk_type: str = None,
        doc_id: str = None,
        file_type: str = None,
        library_id: str = None,
        library_name: str = None,
        next_chunk_id: str = None,
        pos: List[main_models.RecallDocumentResponseBodyDataTextChunkListPos] = None,
        pre_chunk_id: str = None,
        score: float = None,
        title: str = None,
    ):
        self.chunk_id = chunk_id
        self.chunk_meta = chunk_meta
        self.chunk_oss_url = chunk_oss_url
        self.chunk_text = chunk_text
        self.chunk_type = chunk_type
        self.doc_id = doc_id
        self.file_type = file_type
        self.library_id = library_id
        self.library_name = library_name
        self.next_chunk_id = next_chunk_id
        self.pos = pos
        self.pre_chunk_id = pre_chunk_id
        self.score = score
        self.title = title

    def validate(self):
        if self.pos:
            for v1 in self.pos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chunk_id is not None:
            result['chunkId'] = self.chunk_id

        if self.chunk_meta is not None:
            result['chunkMeta'] = self.chunk_meta

        if self.chunk_oss_url is not None:
            result['chunkOssUrl'] = self.chunk_oss_url

        if self.chunk_text is not None:
            result['chunkText'] = self.chunk_text

        if self.chunk_type is not None:
            result['chunkType'] = self.chunk_type

        if self.doc_id is not None:
            result['docId'] = self.doc_id

        if self.file_type is not None:
            result['fileType'] = self.file_type

        if self.library_id is not None:
            result['libraryId'] = self.library_id

        if self.library_name is not None:
            result['libraryName'] = self.library_name

        if self.next_chunk_id is not None:
            result['nextChunkId'] = self.next_chunk_id

        result['pos'] = []
        if self.pos is not None:
            for k1 in self.pos:
                result['pos'].append(k1.to_map() if k1 else None)

        if self.pre_chunk_id is not None:
            result['preChunkId'] = self.pre_chunk_id

        if self.score is not None:
            result['score'] = self.score

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chunkId') is not None:
            self.chunk_id = m.get('chunkId')

        if m.get('chunkMeta') is not None:
            self.chunk_meta = m.get('chunkMeta')

        if m.get('chunkOssUrl') is not None:
            self.chunk_oss_url = m.get('chunkOssUrl')

        if m.get('chunkText') is not None:
            self.chunk_text = m.get('chunkText')

        if m.get('chunkType') is not None:
            self.chunk_type = m.get('chunkType')

        if m.get('docId') is not None:
            self.doc_id = m.get('docId')

        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')

        if m.get('libraryId') is not None:
            self.library_id = m.get('libraryId')

        if m.get('libraryName') is not None:
            self.library_name = m.get('libraryName')

        if m.get('nextChunkId') is not None:
            self.next_chunk_id = m.get('nextChunkId')

        self.pos = []
        if m.get('pos') is not None:
            for k1 in m.get('pos'):
                temp_model = main_models.RecallDocumentResponseBodyDataTextChunkListPos()
                self.pos.append(temp_model.from_map(k1))

        if m.get('preChunkId') is not None:
            self.pre_chunk_id = m.get('preChunkId')

        if m.get('score') is not None:
            self.score = m.get('score')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class RecallDocumentResponseBodyDataTextChunkListPos(DaraModel):
    def __init__(
        self,
        axis_array: List[float] = None,
        page: int = None,
        text_highlight_area: List[int] = None,
    ):
        self.axis_array = axis_array
        self.page = page
        self.text_highlight_area = text_highlight_area

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.axis_array is not None:
            result['axisArray'] = self.axis_array

        if self.page is not None:
            result['page'] = self.page

        if self.text_highlight_area is not None:
            result['textHighlightArea'] = self.text_highlight_area

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('axisArray') is not None:
            self.axis_array = m.get('axisArray')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('textHighlightArea') is not None:
            self.text_highlight_area = m.get('textHighlightArea')

        return self

class RecallDocumentResponseBodyDataDocuments(DaraModel):
    def __init__(
        self,
        doc_id: str = None,
        document_meta: Dict[str, Any] = None,
        file_type: str = None,
        gmt_create: str = None,
        library_id: str = None,
        title: str = None,
        url: str = None,
    ):
        self.doc_id = doc_id
        self.document_meta = document_meta
        self.file_type = file_type
        self.gmt_create = gmt_create
        self.library_id = library_id
        self.title = title
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.doc_id is not None:
            result['docId'] = self.doc_id

        if self.document_meta is not None:
            result['documentMeta'] = self.document_meta

        if self.file_type is not None:
            result['fileType'] = self.file_type

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.library_id is not None:
            result['libraryId'] = self.library_id

        if self.title is not None:
            result['title'] = self.title

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('docId') is not None:
            self.doc_id = m.get('docId')

        if m.get('documentMeta') is not None:
            self.document_meta = m.get('documentMeta')

        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('libraryId') is not None:
            self.library_id = m.get('libraryId')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

class RecallDocumentResponseBodyDataChunkPartList(DaraModel):
    def __init__(
        self,
        chunk_id: str = None,
        chunk_meta: Dict[str, Any] = None,
        chunk_oss_url: str = None,
        chunk_text: str = None,
        chunk_type: str = None,
        doc_id: str = None,
        file_type: str = None,
        library_id: str = None,
        library_name: str = None,
        next_chunk_id: str = None,
        pos: List[main_models.RecallDocumentResponseBodyDataChunkPartListPos] = None,
        pre_chunk_id: str = None,
        score: float = None,
        title: str = None,
    ):
        self.chunk_id = chunk_id
        self.chunk_meta = chunk_meta
        self.chunk_oss_url = chunk_oss_url
        self.chunk_text = chunk_text
        self.chunk_type = chunk_type
        self.doc_id = doc_id
        self.file_type = file_type
        self.library_id = library_id
        self.library_name = library_name
        self.next_chunk_id = next_chunk_id
        self.pos = pos
        self.pre_chunk_id = pre_chunk_id
        self.score = score
        self.title = title

    def validate(self):
        if self.pos:
            for v1 in self.pos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chunk_id is not None:
            result['chunkId'] = self.chunk_id

        if self.chunk_meta is not None:
            result['chunkMeta'] = self.chunk_meta

        if self.chunk_oss_url is not None:
            result['chunkOssUrl'] = self.chunk_oss_url

        if self.chunk_text is not None:
            result['chunkText'] = self.chunk_text

        if self.chunk_type is not None:
            result['chunkType'] = self.chunk_type

        if self.doc_id is not None:
            result['docId'] = self.doc_id

        if self.file_type is not None:
            result['fileType'] = self.file_type

        if self.library_id is not None:
            result['libraryId'] = self.library_id

        if self.library_name is not None:
            result['libraryName'] = self.library_name

        if self.next_chunk_id is not None:
            result['nextChunkId'] = self.next_chunk_id

        result['pos'] = []
        if self.pos is not None:
            for k1 in self.pos:
                result['pos'].append(k1.to_map() if k1 else None)

        if self.pre_chunk_id is not None:
            result['preChunkId'] = self.pre_chunk_id

        if self.score is not None:
            result['score'] = self.score

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chunkId') is not None:
            self.chunk_id = m.get('chunkId')

        if m.get('chunkMeta') is not None:
            self.chunk_meta = m.get('chunkMeta')

        if m.get('chunkOssUrl') is not None:
            self.chunk_oss_url = m.get('chunkOssUrl')

        if m.get('chunkText') is not None:
            self.chunk_text = m.get('chunkText')

        if m.get('chunkType') is not None:
            self.chunk_type = m.get('chunkType')

        if m.get('docId') is not None:
            self.doc_id = m.get('docId')

        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')

        if m.get('libraryId') is not None:
            self.library_id = m.get('libraryId')

        if m.get('libraryName') is not None:
            self.library_name = m.get('libraryName')

        if m.get('nextChunkId') is not None:
            self.next_chunk_id = m.get('nextChunkId')

        self.pos = []
        if m.get('pos') is not None:
            for k1 in m.get('pos'):
                temp_model = main_models.RecallDocumentResponseBodyDataChunkPartListPos()
                self.pos.append(temp_model.from_map(k1))

        if m.get('preChunkId') is not None:
            self.pre_chunk_id = m.get('preChunkId')

        if m.get('score') is not None:
            self.score = m.get('score')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class RecallDocumentResponseBodyDataChunkPartListPos(DaraModel):
    def __init__(
        self,
        axis_array: List[float] = None,
        page: int = None,
        text_highlight_area: List[int] = None,
    ):
        self.axis_array = axis_array
        self.page = page
        self.text_highlight_area = text_highlight_area

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.axis_array is not None:
            result['axisArray'] = self.axis_array

        if self.page is not None:
            result['page'] = self.page

        if self.text_highlight_area is not None:
            result['textHighlightArea'] = self.text_highlight_area

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('axisArray') is not None:
            self.axis_array = m.get('axisArray')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('textHighlightArea') is not None:
            self.text_highlight_area = m.get('textHighlightArea')

        return self

class RecallDocumentResponseBodyDataChunkList(DaraModel):
    def __init__(
        self,
        chunk_id: str = None,
        chunk_meta: Dict[str, Any] = None,
        chunk_oss_url: str = None,
        chunk_text: str = None,
        chunk_type: str = None,
        doc_id: str = None,
        file_type: str = None,
        library_id: str = None,
        library_name: str = None,
        next_chunk_id: str = None,
        pos: List[main_models.RecallDocumentResponseBodyDataChunkListPos] = None,
        pre_chunk_id: str = None,
        score: float = None,
        title: str = None,
    ):
        self.chunk_id = chunk_id
        self.chunk_meta = chunk_meta
        self.chunk_oss_url = chunk_oss_url
        self.chunk_text = chunk_text
        self.chunk_type = chunk_type
        self.doc_id = doc_id
        self.file_type = file_type
        self.library_id = library_id
        self.library_name = library_name
        self.next_chunk_id = next_chunk_id
        self.pos = pos
        self.pre_chunk_id = pre_chunk_id
        self.score = score
        self.title = title

    def validate(self):
        if self.pos:
            for v1 in self.pos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chunk_id is not None:
            result['chunkId'] = self.chunk_id

        if self.chunk_meta is not None:
            result['chunkMeta'] = self.chunk_meta

        if self.chunk_oss_url is not None:
            result['chunkOssUrl'] = self.chunk_oss_url

        if self.chunk_text is not None:
            result['chunkText'] = self.chunk_text

        if self.chunk_type is not None:
            result['chunkType'] = self.chunk_type

        if self.doc_id is not None:
            result['docId'] = self.doc_id

        if self.file_type is not None:
            result['fileType'] = self.file_type

        if self.library_id is not None:
            result['libraryId'] = self.library_id

        if self.library_name is not None:
            result['libraryName'] = self.library_name

        if self.next_chunk_id is not None:
            result['nextChunkId'] = self.next_chunk_id

        result['pos'] = []
        if self.pos is not None:
            for k1 in self.pos:
                result['pos'].append(k1.to_map() if k1 else None)

        if self.pre_chunk_id is not None:
            result['preChunkId'] = self.pre_chunk_id

        if self.score is not None:
            result['score'] = self.score

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chunkId') is not None:
            self.chunk_id = m.get('chunkId')

        if m.get('chunkMeta') is not None:
            self.chunk_meta = m.get('chunkMeta')

        if m.get('chunkOssUrl') is not None:
            self.chunk_oss_url = m.get('chunkOssUrl')

        if m.get('chunkText') is not None:
            self.chunk_text = m.get('chunkText')

        if m.get('chunkType') is not None:
            self.chunk_type = m.get('chunkType')

        if m.get('docId') is not None:
            self.doc_id = m.get('docId')

        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')

        if m.get('libraryId') is not None:
            self.library_id = m.get('libraryId')

        if m.get('libraryName') is not None:
            self.library_name = m.get('libraryName')

        if m.get('nextChunkId') is not None:
            self.next_chunk_id = m.get('nextChunkId')

        self.pos = []
        if m.get('pos') is not None:
            for k1 in m.get('pos'):
                temp_model = main_models.RecallDocumentResponseBodyDataChunkListPos()
                self.pos.append(temp_model.from_map(k1))

        if m.get('preChunkId') is not None:
            self.pre_chunk_id = m.get('preChunkId')

        if m.get('score') is not None:
            self.score = m.get('score')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class RecallDocumentResponseBodyDataChunkListPos(DaraModel):
    def __init__(
        self,
        axis_array: List[float] = None,
        page: int = None,
        text_highlight_area: List[int] = None,
    ):
        self.axis_array = axis_array
        self.page = page
        self.text_highlight_area = text_highlight_area

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.axis_array is not None:
            result['axisArray'] = self.axis_array

        if self.page is not None:
            result['page'] = self.page

        if self.text_highlight_area is not None:
            result['textHighlightArea'] = self.text_highlight_area

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('axisArray') is not None:
            self.axis_array = m.get('axisArray')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('textHighlightArea') is not None:
            self.text_highlight_area = m.get('textHighlightArea')

        return self

