# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateIndexShrinkRequest(DaraModel):
    def __init__(
        self,
        category_ids_shrink: str = None,
        chunk_size: int = None,
        columns_shrink: str = None,
        create_index_type: str = None,
        data_source_shrink: str = None,
        description: str = None,
        document_ids_shrink: str = None,
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
        table_ids_shrink: str = None,
        chunk_mode: str = None,
        database: str = None,
        datasource_code: str = None,
        enable_headers: bool = None,
        meta_extract_columns_shrink: str = None,
        pipeline_commercial_cu: int = None,
        pipeline_commercial_type: str = None,
        pipeline_retrieve_rate_limit_strategy: str = None,
        table: str = None,
    ):
        # The files to imported to the knowledge base. Specify the category IDs. All files under the categories will be imported (up to 10,000 files). To add more files later, call **SubmitIndexAddDocumentsJob**.
        self.category_ids_shrink = category_ids_shrink
        # The chunk size, which is the maximum number of characters in each chunk. Text exceeding this length may be truncated.
        # 
        # Valid values: 1 to 6000. Default value: 500.
        # 
        # > If `ChunkSize` is set to a value less than 100, `OverlapSize` is required. Or, if you do not pass these two parameters, the system uses the default values of the two.
        self.chunk_size = chunk_size
        self.columns_shrink = columns_shrink
        # > This parameter is not available. Do not specify this parameter.
        self.create_index_type = create_index_type
        # >  This parameter is not available. Do not specify this parameter.
        self.data_source_shrink = data_source_shrink
        # The description of the knowledge base. The description must be 0 to 1,000 characters in length. This parameter is empty by default.
        self.description = description
        # The files to imported to the knowledge base. Specify the file IDs to import (up to 10,000 files). To add more files later, call **SubmitIndexAddDocumentsJob**.
        self.document_ids_shrink = document_ids_shrink
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
        self.table_ids_shrink = table_ids_shrink
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
        self.meta_extract_columns_shrink = meta_extract_columns_shrink
        self.pipeline_commercial_cu = pipeline_commercial_cu
        self.pipeline_commercial_type = pipeline_commercial_type
        self.pipeline_retrieve_rate_limit_strategy = pipeline_retrieve_rate_limit_strategy
        self.table = table

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_ids_shrink is not None:
            result['CategoryIds'] = self.category_ids_shrink

        if self.chunk_size is not None:
            result['ChunkSize'] = self.chunk_size

        if self.columns_shrink is not None:
            result['Columns'] = self.columns_shrink

        if self.create_index_type is not None:
            result['CreateIndexType'] = self.create_index_type

        if self.data_source_shrink is not None:
            result['DataSource'] = self.data_source_shrink

        if self.description is not None:
            result['Description'] = self.description

        if self.document_ids_shrink is not None:
            result['DocumentIds'] = self.document_ids_shrink

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

        if self.table_ids_shrink is not None:
            result['TableIds'] = self.table_ids_shrink

        if self.chunk_mode is not None:
            result['chunkMode'] = self.chunk_mode

        if self.database is not None:
            result['database'] = self.database

        if self.datasource_code is not None:
            result['datasourceCode'] = self.datasource_code

        if self.enable_headers is not None:
            result['enableHeaders'] = self.enable_headers

        if self.meta_extract_columns_shrink is not None:
            result['metaExtractColumns'] = self.meta_extract_columns_shrink

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
            self.category_ids_shrink = m.get('CategoryIds')

        if m.get('ChunkSize') is not None:
            self.chunk_size = m.get('ChunkSize')

        if m.get('Columns') is not None:
            self.columns_shrink = m.get('Columns')

        if m.get('CreateIndexType') is not None:
            self.create_index_type = m.get('CreateIndexType')

        if m.get('DataSource') is not None:
            self.data_source_shrink = m.get('DataSource')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DocumentIds') is not None:
            self.document_ids_shrink = m.get('DocumentIds')

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
            self.table_ids_shrink = m.get('TableIds')

        if m.get('chunkMode') is not None:
            self.chunk_mode = m.get('chunkMode')

        if m.get('database') is not None:
            self.database = m.get('database')

        if m.get('datasourceCode') is not None:
            self.datasource_code = m.get('datasourceCode')

        if m.get('enableHeaders') is not None:
            self.enable_headers = m.get('enableHeaders')

        if m.get('metaExtractColumns') is not None:
            self.meta_extract_columns_shrink = m.get('metaExtractColumns')

        if m.get('pipelineCommercialCu') is not None:
            self.pipeline_commercial_cu = m.get('pipelineCommercialCu')

        if m.get('pipelineCommercialType') is not None:
            self.pipeline_commercial_type = m.get('pipelineCommercialType')

        if m.get('pipelineRetrieveRateLimitStrategy') is not None:
            self.pipeline_retrieve_rate_limit_strategy = m.get('pipelineRetrieveRateLimitStrategy')

        if m.get('table') is not None:
            self.table = m.get('table')

        return self

