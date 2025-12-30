# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_dianjin20240628 import models as main_models
from darabonba.model import DaraModel

class GetFilterDocumentListResponseBody(DaraModel):
    def __init__(
        self,
        cost: int = None,
        data: main_models.GetFilterDocumentListResponseBodyData = None,
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
            temp_model = main_models.GetFilterDocumentListResponseBodyData()
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

class GetFilterDocumentListResponseBodyData(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        records: List[main_models.GetFilterDocumentListResponseBodyDataRecords] = None,
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
                temp_model = main_models.GetFilterDocumentListResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k1))

        if m.get('totalPages') is not None:
            self.total_pages = m.get('totalPages')

        if m.get('totalRecords') is not None:
            self.total_records = m.get('totalRecords')

        return self

class GetFilterDocumentListResponseBodyDataRecords(DaraModel):
    def __init__(
        self,
        doc_id: str = None,
        document_meta: Dict[str, Any] = None,
        file_type: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        library_id: str = None,
        status_code: str = None,
        title: str = None,
        url: str = None,
    ):
        self.doc_id = doc_id
        self.document_meta = document_meta
        self.file_type = file_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.library_id = library_id
        self.status_code = status_code
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

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.library_id is not None:
            result['libraryId'] = self.library_id

        if self.status_code is not None:
            result['statusCode'] = self.status_code

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

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('libraryId') is not None:
            self.library_id = m.get('libraryId')

        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

