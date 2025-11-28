# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class DescribeCollectionResponseBody(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        dimension: int = None,
        full_text_retrieval_fields: str = None,
        message: str = None,
        metadata: Dict[str, str] = None,
        metrics: str = None,
        namespace: str = None,
        parser: str = None,
        region_id: str = None,
        request_id: str = None,
        sparse_vector_metrics: str = None,
        status: str = None,
        support_sparse: bool = None,
    ):
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        # The number of vector dimensions.
        self.dimension = dimension
        # The fields that are used for full-text search. Multiple fields are separated by commas (,).
        self.full_text_retrieval_fields = full_text_retrieval_fields
        # The returned message.
        self.message = message
        # The metadata of vector data, which is a JSON string in the MAP format. The key specifies the field name, and the value specifies the data type.
        # 
        # **
        # 
        # **Warning** Reserved fields such as id, vector, and to_tsvector cannot be used.
        self.metadata = metadata
        # The distance metrics.
        self.metrics = metrics
        # The name of the namespace.
        self.namespace = namespace
        # The analyzer that is used for full-text search.
        self.parser = parser
        # The region ID of the instance.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
        # The method that is used to create sparse vector indexes.
        self.sparse_vector_metrics = sparse_vector_metrics
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **success**
        # *   **fail**
        self.status = status
        # Indicates whether sparse vectors are supported.
        self.support_sparse = support_sparse

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dimension is not None:
            result['Dimension'] = self.dimension

        if self.full_text_retrieval_fields is not None:
            result['FullTextRetrievalFields'] = self.full_text_retrieval_fields

        if self.message is not None:
            result['Message'] = self.message

        if self.metadata is not None:
            result['Metadata'] = self.metadata

        if self.metrics is not None:
            result['Metrics'] = self.metrics

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.parser is not None:
            result['Parser'] = self.parser

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sparse_vector_metrics is not None:
            result['SparseVectorMetrics'] = self.sparse_vector_metrics

        if self.status is not None:
            result['Status'] = self.status

        if self.support_sparse is not None:
            result['SupportSparse'] = self.support_sparse

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')

        if m.get('FullTextRetrievalFields') is not None:
            self.full_text_retrieval_fields = m.get('FullTextRetrievalFields')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        if m.get('Metrics') is not None:
            self.metrics = m.get('Metrics')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('Parser') is not None:
            self.parser = m.get('Parser')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SparseVectorMetrics') is not None:
            self.sparse_vector_metrics = m.get('SparseVectorMetrics')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SupportSparse') is not None:
            self.support_sparse = m.get('SupportSparse')

        return self

