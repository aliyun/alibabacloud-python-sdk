# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class ListDocumentCollectionsResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        items: main_models.ListDocumentCollectionsResponseBodyItems = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
    ):
        # The total number of entries returned.
        self.count = count
        # The queried document collections.
        self.items = items
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **success**
        # *   **fail**
        self.status = status

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.items is not None:
            result['Items'] = self.items.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Items') is not None:
            temp_model = main_models.ListDocumentCollectionsResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class ListDocumentCollectionsResponseBodyItems(DaraModel):
    def __init__(
        self,
        collection_list: List[main_models.ListDocumentCollectionsResponseBodyItemsCollectionList] = None,
    ):
        self.collection_list = collection_list

    def validate(self):
        if self.collection_list:
            for v1 in self.collection_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CollectionList'] = []
        if self.collection_list is not None:
            for k1 in self.collection_list:
                result['CollectionList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.collection_list = []
        if m.get('CollectionList') is not None:
            for k1 in m.get('CollectionList'):
                temp_model = main_models.ListDocumentCollectionsResponseBodyItemsCollectionList()
                self.collection_list.append(temp_model.from_map(k1))

        return self

class ListDocumentCollectionsResponseBodyItemsCollectionList(DaraModel):
    def __init__(
        self,
        collection_name: str = None,
        dimension: int = None,
        embedding_model: str = None,
        full_text_retrieval_fields: str = None,
        metadata: str = None,
        metrics: str = None,
        parser: str = None,
    ):
        # The name of the document collection.
        self.collection_name = collection_name
        # The number of vector dimensions.
        self.dimension = dimension
        # The name of the vector algorithm.
        self.embedding_model = embedding_model
        # The fields that are used for full-text search. Multiple fields are separated by commas (,).
        self.full_text_retrieval_fields = full_text_retrieval_fields
        # The metadata.
        self.metadata = metadata
        # The vector similarity algorithm.
        self.metrics = metrics
        # The analyzer that is used for full-text search.
        self.parser = parser

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.collection_name is not None:
            result['CollectionName'] = self.collection_name

        if self.dimension is not None:
            result['Dimension'] = self.dimension

        if self.embedding_model is not None:
            result['EmbeddingModel'] = self.embedding_model

        if self.full_text_retrieval_fields is not None:
            result['FullTextRetrievalFields'] = self.full_text_retrieval_fields

        if self.metadata is not None:
            result['Metadata'] = self.metadata

        if self.metrics is not None:
            result['Metrics'] = self.metrics

        if self.parser is not None:
            result['Parser'] = self.parser

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CollectionName') is not None:
            self.collection_name = m.get('CollectionName')

        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')

        if m.get('EmbeddingModel') is not None:
            self.embedding_model = m.get('EmbeddingModel')

        if m.get('FullTextRetrievalFields') is not None:
            self.full_text_retrieval_fields = m.get('FullTextRetrievalFields')

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        if m.get('Metrics') is not None:
            self.metrics = m.get('Metrics')

        if m.get('Parser') is not None:
            self.parser = m.get('Parser')

        return self

