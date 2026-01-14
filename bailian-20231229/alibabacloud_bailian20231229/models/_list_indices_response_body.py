# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bailian20231229 import models as main_models
from darabonba.model import DaraModel

class ListIndicesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListIndicesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        # HTTP status code
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The HTTP status code returned.
        self.status = status
        # Indications whether the API call is successful. Valid values:
        # 
        # *   true
        # *   false
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

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ListIndicesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListIndicesResponseBodyData(DaraModel):
    def __init__(
        self,
        indices: List[main_models.ListIndicesResponseBodyDataIndices] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The list of knowledge bases.
        self.indices = indices
        # The specified page number.
        self.page_number = page_number
        # The specified number of documents on each page.
        self.page_size = page_size
        # The total number of knowledge bases returned.
        self.total_count = total_count

    def validate(self):
        if self.indices:
            for v1 in self.indices:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Indices'] = []
        if self.indices is not None:
            for k1 in self.indices:
                result['Indices'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.indices = []
        if m.get('Indices') is not None:
            for k1 in m.get('Indices'):
                temp_model = main_models.ListIndicesResponseBodyDataIndices()
                self.indices.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListIndicesResponseBodyDataIndices(DaraModel):
    def __init__(
        self,
        chunk_size: int = None,
        confg_model: str = None,
        description: str = None,
        document_ids: List[str] = None,
        embedding_model_name: str = None,
        enable_rewrite: bool = None,
        id: str = None,
        name: str = None,
        overlap_size: int = None,
        rerank_min_score: str = None,
        rerank_model_name: str = None,
        separator: str = None,
        sink_instance_id: str = None,
        sink_region: str = None,
        sink_type: str = None,
        source_type: str = None,
        structure_type: str = None,
    ):
        # The estimated length of chunks. Valid values: [1-2048].
        self.chunk_size = chunk_size
        self.confg_model = confg_model
        # The description of the knowledge base.
        self.description = description
        # The list of the primary key IDs of the documents.
        self.document_ids = document_ids
        # The name of the embedding model. Valid values:
        # 
        # *   text-embedding-v2
        self.embedding_model_name = embedding_model_name
        self.enable_rewrite = enable_rewrite
        # The primary key ID of the knowledge base, which is the `Data.Id` parameter returned by the [CreateIndex](https://www.alibabacloud.com/help/en/model-studio/developer-reference/api-bailian-2023-12-29-createindex) operation.
        self.id = id
        # The name of the knowledge base.
        self.name = name
        # The overlap length. Valid values: [0-1024].
        self.overlap_size = overlap_size
        # Similarity Threshold Valid values: [0.01-1.00].
        self.rerank_min_score = rerank_min_score
        # The name of the rank model. Valid values:
        # 
        # *   gte-rerank-hybrid
        # *   gte-rerank
        self.rerank_model_name = rerank_model_name
        # The clause identifier. Separate multiple clause identifiers with |. Valid values:
        # 
        # *   \\n: line break
        # *   ，: Chinese comma
        # *   ,: English comma
        # *   。 : Chinese full stop
        # *   .: English full stop
        # *   ！ : Chinese exclamation point
        # *   ! : English exclamation point
        # *   ；: Chinese semicolon
        # *   ;: English semicolon
        # *   ？ : Chinese question mark
        # *   ?: English question mark
        self.separator = separator
        # The ID of the vector storage instance.
        self.sink_instance_id = sink_instance_id
        # The region of the vector storage instance.
        self.sink_region = sink_region
        # The vector storage type of the knowledge base. Valid values:
        # 
        # *   ES: Built-in vector database.
        # *   BUILT_IN: Built-in vector database.
        # *   ADB: AnalyticDB for PostgreSQL database.
        self.sink_type = sink_type
        # The data type of [Data Management](https://bailian.console.aliyun.com/#/data-center). For unstructured knowledge base, possible values:
        # 
        # *   DATA_CENTER_CATEGORY: The category type.
        # *   DATA_CENTER_FILE: The document type.
        # 
        # For structured knowledge base, possible values:
        # 
        # *   DATA_CENTER_STRUCTURED_TABLE: The data table type.
        self.source_type = source_type
        # The vector storage type of the knowledge base. Valid values:
        # 
        # *   UNSTRUCTURED
        self.structure_type = structure_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chunk_size is not None:
            result['ChunkSize'] = self.chunk_size

        if self.confg_model is not None:
            result['ConfgModel'] = self.confg_model

        if self.description is not None:
            result['Description'] = self.description

        if self.document_ids is not None:
            result['DocumentIds'] = self.document_ids

        if self.embedding_model_name is not None:
            result['EmbeddingModelName'] = self.embedding_model_name

        if self.enable_rewrite is not None:
            result['EnableRewrite'] = self.enable_rewrite

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.overlap_size is not None:
            result['OverlapSize'] = self.overlap_size

        if self.rerank_min_score is not None:
            result['RerankMinScore'] = self.rerank_min_score

        if self.rerank_model_name is not None:
            result['RerankModelName'] = self.rerank_model_name

        if self.separator is not None:
            result['Separator'] = self.separator

        if self.sink_instance_id is not None:
            result['SinkInstanceId'] = self.sink_instance_id

        if self.sink_region is not None:
            result['SinkRegion'] = self.sink_region

        if self.sink_type is not None:
            result['SinkType'] = self.sink_type

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.structure_type is not None:
            result['StructureType'] = self.structure_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChunkSize') is not None:
            self.chunk_size = m.get('ChunkSize')

        if m.get('ConfgModel') is not None:
            self.confg_model = m.get('ConfgModel')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DocumentIds') is not None:
            self.document_ids = m.get('DocumentIds')

        if m.get('EmbeddingModelName') is not None:
            self.embedding_model_name = m.get('EmbeddingModelName')

        if m.get('EnableRewrite') is not None:
            self.enable_rewrite = m.get('EnableRewrite')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OverlapSize') is not None:
            self.overlap_size = m.get('OverlapSize')

        if m.get('RerankMinScore') is not None:
            self.rerank_min_score = m.get('RerankMinScore')

        if m.get('RerankModelName') is not None:
            self.rerank_model_name = m.get('RerankModelName')

        if m.get('Separator') is not None:
            self.separator = m.get('Separator')

        if m.get('SinkInstanceId') is not None:
            self.sink_instance_id = m.get('SinkInstanceId')

        if m.get('SinkRegion') is not None:
            self.sink_region = m.get('SinkRegion')

        if m.get('SinkType') is not None:
            self.sink_type = m.get('SinkType')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('StructureType') is not None:
            self.structure_type = m.get('StructureType')

        return self

