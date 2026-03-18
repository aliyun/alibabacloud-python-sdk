# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aicontent20240611 import models as main_models
from darabonba.model import DaraModel

class ListTextbookAssistantBooksResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListTextbookAssistantBooksResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        # Id of the request
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
        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.err_code is not None:
            result['errCode'] = self.err_code

        if self.err_message is not None:
            result['errMessage'] = self.err_message

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.ListTextbookAssistantBooksResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')

        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class ListTextbookAssistantBooksResponseBodyData(DaraModel):
    def __init__(
        self,
        book_list: List[main_models.ListTextbookAssistantBooksResponseBodyDataBookList] = None,
        pagination_data: main_models.ListTextbookAssistantBooksResponseBodyDataPaginationData = None,
    ):
        self.book_list = book_list
        self.pagination_data = pagination_data

    def validate(self):
        if self.book_list:
            for v1 in self.book_list:
                 if v1:
                    v1.validate()
        if self.pagination_data:
            self.pagination_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['bookList'] = []
        if self.book_list is not None:
            for k1 in self.book_list:
                result['bookList'].append(k1.to_map() if k1 else None)

        if self.pagination_data is not None:
            result['paginationData'] = self.pagination_data.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.book_list = []
        if m.get('bookList') is not None:
            for k1 in m.get('bookList'):
                temp_model = main_models.ListTextbookAssistantBooksResponseBodyDataBookList()
                self.book_list.append(temp_model.from_map(k1))

        if m.get('paginationData') is not None:
            temp_model = main_models.ListTextbookAssistantBooksResponseBodyDataPaginationData()
            self.pagination_data = temp_model.from_map(m.get('paginationData'))

        return self

class ListTextbookAssistantBooksResponseBodyDataPaginationData(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        max_results: int = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.max_results = max_results
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['currentPage'] = self.current_page

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListTextbookAssistantBooksResponseBodyDataBookList(DaraModel):
    def __init__(
        self,
        author: str = None,
        book_id: str = None,
        book_name: str = None,
        cover_image: str = None,
        edition: str = None,
        grade: str = None,
        impression: str = None,
        isbn: str = None,
        publisher: str = None,
        subject: str = None,
        version: str = None,
        volume: str = None,
    ):
        self.author = author
        self.book_id = book_id
        self.book_name = book_name
        self.cover_image = cover_image
        self.edition = edition
        self.grade = grade
        self.impression = impression
        self.isbn = isbn
        self.publisher = publisher
        self.subject = subject
        self.version = version
        self.volume = volume

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.author is not None:
            result['author'] = self.author

        if self.book_id is not None:
            result['bookId'] = self.book_id

        if self.book_name is not None:
            result['bookName'] = self.book_name

        if self.cover_image is not None:
            result['coverImage'] = self.cover_image

        if self.edition is not None:
            result['edition'] = self.edition

        if self.grade is not None:
            result['grade'] = self.grade

        if self.impression is not None:
            result['impression'] = self.impression

        if self.isbn is not None:
            result['isbn'] = self.isbn

        if self.publisher is not None:
            result['publisher'] = self.publisher

        if self.subject is not None:
            result['subject'] = self.subject

        if self.version is not None:
            result['version'] = self.version

        if self.volume is not None:
            result['volume'] = self.volume

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('author') is not None:
            self.author = m.get('author')

        if m.get('bookId') is not None:
            self.book_id = m.get('bookId')

        if m.get('bookName') is not None:
            self.book_name = m.get('bookName')

        if m.get('coverImage') is not None:
            self.cover_image = m.get('coverImage')

        if m.get('edition') is not None:
            self.edition = m.get('edition')

        if m.get('grade') is not None:
            self.grade = m.get('grade')

        if m.get('impression') is not None:
            self.impression = m.get('impression')

        if m.get('isbn') is not None:
            self.isbn = m.get('isbn')

        if m.get('publisher') is not None:
            self.publisher = m.get('publisher')

        if m.get('subject') is not None:
            self.subject = m.get('subject')

        if m.get('version') is not None:
            self.version = m.get('version')

        if m.get('volume') is not None:
            self.volume = m.get('volume')

        return self

