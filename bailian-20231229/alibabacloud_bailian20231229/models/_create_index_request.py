# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bailian20231229 import models as main_models
from darabonba.model import DaraModel

class CreateIndexRequest(DaraModel):
    def __init__(
        self,
        category_ids: List[str] = None,
        chunk_size: int = None,
        columns: List[main_models.CreateIndexRequestColumns] = None,
        create_index_type: str = None,
        data_source: main_models.CreateIndexRequestDataSource = None,
        description: str = None,
        document_ids: List[str] = None,
        embedding_model_name: str = None,
        enable_rewrite: bool = None,
        name: str = None,
        overlap_size: int = None,
        rerank_min_score: float = None,
        rerank_model_name: str = None,
        separator: str = None,
        sink_instance_id: str = None,
        sink_region: str = None,
        sink_type: str = None,
        source_type: str = None,
        structure_type: str = None,
        table_ids: List[str] = None,
        chunk_mode: str = None,
        database: str = None,
        datasource_code: str = None,
        enable_headers: bool = None,
        meta_extract_columns: List[main_models.CreateIndexRequestMetaExtractColumns] = None,
        pipeline_commercial_cu: int = None,
        pipeline_commercial_type: str = None,
        pipeline_retrieve_rate_limit_strategy: str = None,
        table: str = None,
    ):
        # The files to imported to the knowledge base. Specify the category IDs. All files under the categories will be imported (up to 10,000 files). To add more files later, call **SubmitIndexAddDocumentsJob**.
        self.category_ids = category_ids
        # The chunk size, which is the maximum number of characters in each chunk. Text exceeding this length may be truncated.
        # 
        # Valid values: 1 to 6000. Default value: 500.
        # 
        # > If `ChunkSize` is set to a value less than 100, `OverlapSize` is required. Or, if you do not pass these two parameters, the system uses the default values of the two.
        self.chunk_size = chunk_size
        self.columns = columns
        # > This parameter is not available. Do not specify this parameter.
        self.create_index_type = create_index_type
        # >  This parameter is not available. Do not specify this parameter.
        self.data_source = data_source
        # The description of the knowledge base. The description must be 0 to 1,000 characters in length. This parameter is empty by default.
        self.description = description
        # The files to imported to the knowledge base. Specify the file IDs to import (up to 10,000 files). To add more files later, call **SubmitIndexAddDocumentsJob**.
        self.document_ids = document_ids
        # The embedding model used in the knowledge base. The embedding model converts the original input prompt and knowledge text into numerical embeddings for similarity comparison. The default and only model available is text-embedding-v2. It supports multiple languages including Chinese and English and normalizes the embedding results. For more information, see [Embedding](https://help.aliyun.com/document_detail/2842587.html). Valid values:
        # 
        # *   text-embedding-v2
        # 
        # The default value is null, which means using text-embedding-v2.
        self.embedding_model_name = embedding_model_name
        # Whether to enable rewriting for multi-turn conversations. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: true.
        self.enable_rewrite = enable_rewrite
        # The name of the knowledge base. The name must be 1 to 20 characters in length, and can contain Chinese characters, letters, digits, underscores (_), hyphens (-), periods (.), and colons (:).
        # 
        # This parameter is required.
        self.name = name
        # The overlap size, which is the number of overlapping characters between two consecutive chunks. Valid values: 0 to 1024.
        # 
        # Default value: 100.
        # 
        # > `OverlapSize` must be less than `ChunkSize`. Otherwise, chunking errors may occur.
        self.overlap_size = overlap_size
        # The similarity threshold. Only chunks with a similarity score higher than this value can be recalled. This parameter is used to filter chunks returned by the re-rank model. Valid values: 0.01 to 1.00.
        # 
        # Default value: 0.01.
        self.rerank_min_score = rerank_min_score
        # The re-ranking model used in the knowledge base. The re-rank model is a scoring system outside the knowledge base. It calculates the similarity score of the query and text chunks in the knowledge base and ranks them in descending order. Then, the model returns the top K chunks with the highest scores. Valid values:
        # 
        # *   gte-rerank-hybrid
        # *   gte-rerank
        # 
        # The default value is empty, which means using gte-rerank-hybrid.
        # 
        # > If you need only semantic ranking, we recommend gte-rerank. If you need both semantic ranking and text matching features to ensure relevance, we recommend gte-rerank-hybrid.
        self.rerank_model_name = rerank_model_name
        # > This parameter is not available. Do not specify this parameter.
        self.separator = separator
        # The ID of the AnalyticDB for PostgreSQL instance. Required only when `SinkType` is set to ADB. Get the ID on the [Instances](https://gpdbnext.console.aliyun.com/gpdb/list) page of AnalyticDB for PostgreSQL.
        self.sink_instance_id = sink_instance_id
        # The region of the AnalyticDB for PostgreSQL instance. Required only when `SinkType` is set to ADB. Call [DescribeRegions](https://www.alibabacloud.com/help/zh/analyticdb/analyticdb-for-postgresql/developer-reference/api-gpdb-2016-05-03-describeregions?spm=a2c63.p38356.0.i3) to obtain the region list.
        self.sink_region = sink_region
        # The vector storage type of the knowledge base. For more information, see [Knowledge base](https://help.aliyun.com/document_detail/2807740.html). Valid values:
        # 
        # *   BUILT_IN: The vector data is hosted by Alibaba Cloud Model Studio.
        # *   ADB: AnalyticDB for PostgreSQL database. If you need advanced features, such as managing, auditing, and monitoring, we recommend ADB.
        # 
        # > If you have not used AnalyticDB for AnalyticDB in Model Studio before, go to the [Create Knowledge Base](https://bailian.console.alibabacloud.com/#/knowledge-base/create) page, select ADB-PG as Vector Storage Type, and follow the instructions to grant permissions. If you specify ADB, the `SinkInstanceId` and `SinkRegion` parameters are required.
        # 
        # This parameter is required.
        self.sink_type = sink_type
        # > This parameter is required in the latest version of the SDK. Otherwise, when you call SubmitIndexJob, an error will occur: Required parameter(data_sources) missing or invalid.
        # 
        # The source of the imported data. Valid values:
        # 
        # *   DATA_CENTER_CATEGORY: The category type, that is to import all files in one or more specified categories in [Application Data](https://modelstudio.console.alibabacloud.com/?tab=app#/data-center).
        # *   DATA_CENTER_FILE: The file type, that is to import one or more specified files in [Application Data](https://modelstudio.console.alibabacloud.com/?tab=app#/data-center).
        # 
        # > If set to DATA_CENTER_CATEGORY, `CategoryIds` is required. If set to DATA_CENTER_FILE, `DocumentIds` is required.
        # 
        # > To create an empty knowledge base, you can use an empty category with no files: Set this parameter to DATA_CENTER_CATEGORY, and `CategoryIds` to the ID of an empty category.
        self.source_type = source_type
        # The type of the knowledge base. Valid values:
        # 
        # *   unstructured: The document search type.
        # 
        # > After you create a knowledge base, its type cannot be changed. This operation does not support data query and image Q\\&A types. Use the console instead.
        # 
        # This parameter is required.
        self.structure_type = structure_type
        # > This parameter is not available. Do not specify this parameter.
        self.table_ids = table_ids
        # > This parameter is not available. Do not specify this parameter.
        self.chunk_mode = chunk_mode
        self.database = database
        self.datasource_code = datasource_code
        # Whether to treat the first row of all .xlsx and .xls files as headers and concatenate them into each text chunk. This prevents the models from mistakenly interpreting headers as regular data rows.
        # 
        # > Enable this feature only when all imported files are in .xlsx or .xls format and contain headers. Otherwise, leave it disabled.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        self.enable_headers = enable_headers
        # The metadata extraction configurations. Metadata refers to a set of additional attributes associated with unstructured data, which are integrated into text chunks in key-value pairs. For more information, see [Knowledge base](https://help.aliyun.com/document_detail/2807740.html).
        self.meta_extract_columns = meta_extract_columns
        self.pipeline_commercial_cu = pipeline_commercial_cu
        self.pipeline_commercial_type = pipeline_commercial_type
        self.pipeline_retrieve_rate_limit_strategy = pipeline_retrieve_rate_limit_strategy
        self.table = table

    def validate(self):
        if self.columns:
            for v1 in self.columns:
                 if v1:
                    v1.validate()
        if self.data_source:
            self.data_source.validate()
        if self.meta_extract_columns:
            for v1 in self.meta_extract_columns:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_ids is not None:
            result['CategoryIds'] = self.category_ids

        if self.chunk_size is not None:
            result['ChunkSize'] = self.chunk_size

        result['Columns'] = []
        if self.columns is not None:
            for k1 in self.columns:
                result['Columns'].append(k1.to_map() if k1 else None)

        if self.create_index_type is not None:
            result['CreateIndexType'] = self.create_index_type

        if self.data_source is not None:
            result['DataSource'] = self.data_source.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.document_ids is not None:
            result['DocumentIds'] = self.document_ids

        if self.embedding_model_name is not None:
            result['EmbeddingModelName'] = self.embedding_model_name

        if self.enable_rewrite is not None:
            result['EnableRewrite'] = self.enable_rewrite

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

        if self.table_ids is not None:
            result['TableIds'] = self.table_ids

        if self.chunk_mode is not None:
            result['chunkMode'] = self.chunk_mode

        if self.database is not None:
            result['database'] = self.database

        if self.datasource_code is not None:
            result['datasourceCode'] = self.datasource_code

        if self.enable_headers is not None:
            result['enableHeaders'] = self.enable_headers

        result['metaExtractColumns'] = []
        if self.meta_extract_columns is not None:
            for k1 in self.meta_extract_columns:
                result['metaExtractColumns'].append(k1.to_map() if k1 else None)

        if self.pipeline_commercial_cu is not None:
            result['pipelineCommercialCu'] = self.pipeline_commercial_cu

        if self.pipeline_commercial_type is not None:
            result['pipelineCommercialType'] = self.pipeline_commercial_type

        if self.pipeline_retrieve_rate_limit_strategy is not None:
            result['pipelineRetrieveRateLimitStrategy'] = self.pipeline_retrieve_rate_limit_strategy

        if self.table is not None:
            result['table'] = self.table

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryIds') is not None:
            self.category_ids = m.get('CategoryIds')

        if m.get('ChunkSize') is not None:
            self.chunk_size = m.get('ChunkSize')

        self.columns = []
        if m.get('Columns') is not None:
            for k1 in m.get('Columns'):
                temp_model = main_models.CreateIndexRequestColumns()
                self.columns.append(temp_model.from_map(k1))

        if m.get('CreateIndexType') is not None:
            self.create_index_type = m.get('CreateIndexType')

        if m.get('DataSource') is not None:
            temp_model = main_models.CreateIndexRequestDataSource()
            self.data_source = temp_model.from_map(m.get('DataSource'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DocumentIds') is not None:
            self.document_ids = m.get('DocumentIds')

        if m.get('EmbeddingModelName') is not None:
            self.embedding_model_name = m.get('EmbeddingModelName')

        if m.get('EnableRewrite') is not None:
            self.enable_rewrite = m.get('EnableRewrite')

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

        if m.get('TableIds') is not None:
            self.table_ids = m.get('TableIds')

        if m.get('chunkMode') is not None:
            self.chunk_mode = m.get('chunkMode')

        if m.get('database') is not None:
            self.database = m.get('database')

        if m.get('datasourceCode') is not None:
            self.datasource_code = m.get('datasourceCode')

        if m.get('enableHeaders') is not None:
            self.enable_headers = m.get('enableHeaders')

        self.meta_extract_columns = []
        if m.get('metaExtractColumns') is not None:
            for k1 in m.get('metaExtractColumns'):
                temp_model = main_models.CreateIndexRequestMetaExtractColumns()
                self.meta_extract_columns.append(temp_model.from_map(k1))

        if m.get('pipelineCommercialCu') is not None:
            self.pipeline_commercial_cu = m.get('pipelineCommercialCu')

        if m.get('pipelineCommercialType') is not None:
            self.pipeline_commercial_type = m.get('pipelineCommercialType')

        if m.get('pipelineRetrieveRateLimitStrategy') is not None:
            self.pipeline_retrieve_rate_limit_strategy = m.get('pipelineRetrieveRateLimitStrategy')

        if m.get('table') is not None:
            self.table = m.get('table')

        return self

class CreateIndexRequestMetaExtractColumns(DaraModel):
    def __init__(
        self,
        desc: str = None,
        enable_llm: bool = None,
        enable_search: bool = None,
        key: str = None,
        type: str = None,
        value: str = None,
    ):
        # The description of the metadata field. The description must be 0 to 1,000 characters in length, and can contain Chinese characters, letters, digits, underscores (_), hyphens (-), periods (.), and colons (:). This parameter is left empty by default.
        self.desc = desc
        # When set to true, the key and value of this metadata filed will participate in the generation process of the model, together with the chunk. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        self.enable_llm = enable_llm
        # When set to true, the key and value of this metadata filed will participate in the knowledge base retrieval, together with the chunk. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        self.enable_search = enable_search
        # The metadata key. It must be 1 to 50 characters in length and must be English letters or underscores. If you specify this parameter, the `Value` and `Type` parameters are required.
        self.key = key
        # The type of the metadata field. Valid values:
        # 
        # *   constant
        # *   variable
        # *   custom_prompt
        # *   regular
        # *   keywords
        # 
        # Enumerated value:
        # 
        # *   constant: constant extraction.
        # *   keywords: keyword extraction.
        # *   custom_prompt: LLM.
        # *   variable: variable extraction.
        # *   regular: regular expression.
        self.type = type
        # The metadata value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desc is not None:
            result['Desc'] = self.desc

        if self.enable_llm is not None:
            result['EnableLlm'] = self.enable_llm

        if self.enable_search is not None:
            result['EnableSearch'] = self.enable_search

        if self.key is not None:
            result['Key'] = self.key

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

        if m.get('EnableLlm') is not None:
            self.enable_llm = m.get('EnableLlm')

        if m.get('EnableSearch') is not None:
            self.enable_search = m.get('EnableSearch')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateIndexRequestDataSource(DaraModel):
    def __init__(
        self,
        credential_id: str = None,
        credential_key: str = None,
        database: str = None,
        endpoint: str = None,
        is_private_link: bool = None,
        region: str = None,
        sub_path: str = None,
        sub_type: str = None,
        table: str = None,
        type: str = None,
    ):
        # >  This parameter is not available. Do not specify this parameter.
        self.credential_id = credential_id
        # >  This parameter is not available. Do not specify this parameter.
        self.credential_key = credential_key
        # >  This parameter is not available. Do not specify this parameter.
        self.database = database
        # >  This parameter is not available. Do not specify this parameter.
        self.endpoint = endpoint
        # >  This parameter is not available. Do not specify this parameter.
        self.is_private_link = is_private_link
        # >  This parameter is not available. Do not specify this parameter.
        self.region = region
        # >  This parameter is not available. Do not specify this parameter.
        self.sub_path = sub_path
        # >  This parameter is not available. Do not specify this parameter.
        self.sub_type = sub_type
        # >  This parameter is not available. Do not specify this parameter.
        self.table = table
        # >  This parameter is not available. Do not specify this parameter.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credential_id is not None:
            result['CredentialId'] = self.credential_id

        if self.credential_key is not None:
            result['CredentialKey'] = self.credential_key

        if self.database is not None:
            result['Database'] = self.database

        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.is_private_link is not None:
            result['IsPrivateLink'] = self.is_private_link

        if self.region is not None:
            result['Region'] = self.region

        if self.sub_path is not None:
            result['SubPath'] = self.sub_path

        if self.sub_type is not None:
            result['SubType'] = self.sub_type

        if self.table is not None:
            result['Table'] = self.table

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialId') is not None:
            self.credential_id = m.get('CredentialId')

        if m.get('CredentialKey') is not None:
            self.credential_key = m.get('CredentialKey')

        if m.get('Database') is not None:
            self.database = m.get('Database')

        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('IsPrivateLink') is not None:
            self.is_private_link = m.get('IsPrivateLink')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('SubPath') is not None:
            self.sub_path = m.get('SubPath')

        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')

        if m.get('Table') is not None:
            self.table = m.get('Table')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class CreateIndexRequestColumns(DaraModel):
    def __init__(
        self,
        column: str = None,
        is_recall: bool = None,
        is_search: bool = None,
        name: str = None,
        type: str = None,
    ):
        self.column = column
        self.is_recall = is_recall
        self.is_search = is_search
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column is not None:
            result['Column'] = self.column

        if self.is_recall is not None:
            result['IsRecall'] = self.is_recall

        if self.is_search is not None:
            result['IsSearch'] = self.is_search

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Column') is not None:
            self.column = m.get('Column')

        if m.get('IsRecall') is not None:
            self.is_recall = m.get('IsRecall')

        if m.get('IsSearch') is not None:
            self.is_search = m.get('IsSearch')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

