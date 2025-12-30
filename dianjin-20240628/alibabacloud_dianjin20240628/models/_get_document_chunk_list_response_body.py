# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_dianjin20240628 import models as main_models
from darabonba.model import DaraModel

class GetDocumentChunkListResponseBody(DaraModel):
    def __init__(
        self,
        cost: int = None,
        data: main_models.GetDocumentChunkListResponseBodyData = None,
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
            temp_model = main_models.GetDocumentChunkListResponseBodyData()
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

class GetDocumentChunkListResponseBodyData(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        records: List[main_models.GetDocumentChunkListResponseBodyDataRecords] = None,
        total_pages: int = None,
        total_records: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.records = records
        self.total_pages = total_pages
        self.total_records = total_records

    def validate(self):
        if self.records:
            for v1 in self.records:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['currentPage'] = self.current_page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        result['records'] = []
        if self.records is not None:
            for k1 in self.records:
                result['records'].append(k1.to_map() if k1 else None)

        if self.total_pages is not None:
            result['totalPages'] = self.total_pages

        if self.total_records is not None:
            result['totalRecords'] = self.total_records

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        self.records = []
        if m.get('records') is not None:
            for k1 in m.get('records'):
                temp_model = main_models.GetDocumentChunkListResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k1))

        if m.get('totalPages') is not None:
            self.total_pages = m.get('totalPages')

        if m.get('totalRecords') is not None:
            self.total_records = m.get('totalRecords')

        return self

class GetDocumentChunkListResponseBodyDataRecords(DaraModel):
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
        pos: List[main_models.GetDocumentChunkListResponseBodyDataRecordsPos] = None,
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
                temp_model = main_models.GetDocumentChunkListResponseBodyDataRecordsPos()
                self.pos.append(temp_model.from_map(k1))

        if m.get('preChunkId') is not None:
            self.pre_chunk_id = m.get('preChunkId')

        if m.get('score') is not None:
            self.score = m.get('score')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class GetDocumentChunkListResponseBodyDataRecordsPos(DaraModel):
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

