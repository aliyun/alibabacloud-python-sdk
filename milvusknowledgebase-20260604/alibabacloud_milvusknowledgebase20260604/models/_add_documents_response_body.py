# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_milvusknowledgebase20260604 import models as main_models
from darabonba.model import DaraModel

class AddDocumentsResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        data: main_models.AddDocumentsResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details of the permission verification failure.
        self.access_denied_detail = access_denied_detail
        # The status code.
        self.code = code
        # The response data.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The response message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['accessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessDeniedDetail') is not None:
            self.access_denied_detail = m.get('accessDeniedDetail')

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.AddDocumentsResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class AddDocumentsResponseBodyData(DaraModel):
    def __init__(
        self,
        documents: List[main_models.AddDocumentsResponseBodyDataDocuments] = None,
        errors: List[str] = None,
    ):
        # The list of documents.
        self.documents = documents
        # The list of errors.
        self.errors = errors

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
        result['documents'] = []
        if self.documents is not None:
            for k1 in self.documents:
                result['documents'].append(k1.to_map() if k1 else None)

        if self.errors is not None:
            result['errors'] = self.errors

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.documents = []
        if m.get('documents') is not None:
            for k1 in m.get('documents'):
                temp_model = main_models.AddDocumentsResponseBodyDataDocuments()
                self.documents.append(temp_model.from_map(k1))

        if m.get('errors') is not None:
            self.errors = m.get('errors')

        return self

class AddDocumentsResponseBodyDataDocuments(DaraModel):
    def __init__(
        self,
        chunk_count: int = None,
        chunk_method: str = None,
        dataset_id: str = None,
        id: str = None,
        location: str = None,
        name: str = None,
        progress: float = None,
        run: str = None,
        size: int = None,
        suffix: str = None,
        thumbnail: str = None,
        token_count: int = None,
    ):
        # The chunk count.
        self.chunk_count = chunk_count
        # The chunk method.
        self.chunk_method = chunk_method
        # The ID of the knowledge base.
        self.dataset_id = dataset_id
        # The document ID.
        self.id = id
        # The object path.
        self.location = location
        # The name of the document.
        self.name = name
        # The processing progress.
        self.progress = progress
        # The processing status.
        self.run = run
        # The size of the file.
        self.size = size
        # The file extension.
        self.suffix = suffix
        # The thumbnail.
        self.thumbnail = thumbnail
        # The token count.
        self.token_count = token_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chunk_count is not None:
            result['chunkCount'] = self.chunk_count

        if self.chunk_method is not None:
            result['chunkMethod'] = self.chunk_method

        if self.dataset_id is not None:
            result['datasetId'] = self.dataset_id

        if self.id is not None:
            result['id'] = self.id

        if self.location is not None:
            result['location'] = self.location

        if self.name is not None:
            result['name'] = self.name

        if self.progress is not None:
            result['progress'] = self.progress

        if self.run is not None:
            result['run'] = self.run

        if self.size is not None:
            result['size'] = self.size

        if self.suffix is not None:
            result['suffix'] = self.suffix

        if self.thumbnail is not None:
            result['thumbnail'] = self.thumbnail

        if self.token_count is not None:
            result['tokenCount'] = self.token_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chunkCount') is not None:
            self.chunk_count = m.get('chunkCount')

        if m.get('chunkMethod') is not None:
            self.chunk_method = m.get('chunkMethod')

        if m.get('datasetId') is not None:
            self.dataset_id = m.get('datasetId')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('location') is not None:
            self.location = m.get('location')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('progress') is not None:
            self.progress = m.get('progress')

        if m.get('run') is not None:
            self.run = m.get('run')

        if m.get('size') is not None:
            self.size = m.get('size')

        if m.get('suffix') is not None:
            self.suffix = m.get('suffix')

        if m.get('thumbnail') is not None:
            self.thumbnail = m.get('thumbnail')

        if m.get('tokenCount') is not None:
            self.token_count = m.get('tokenCount')

        return self

