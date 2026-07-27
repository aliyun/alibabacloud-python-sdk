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
        description: str = None,
        document_ids: List[str] = None,
        embedding_model_name: str = None,
        enable_rewrite: bool = None,
        name: str = None,
        overlap_size: int = None,
        rerank_instruct: str = None,
        rerank_min_score: float = None,
        rerank_mode: str = None,
        rerank_model_name: str = None,
        separator: str = None,
        sink_instance_id: str = None,
        sink_region: str = None,
        sink_type: str = None,
        source_type: str = None,
        structure_type: str = None,
        table_ids: List[str] = None,
        channel_type: str = None,
        chunk_mode: str = None,
        connect_id: str = None,
        database: str = None,
        datasource_code: str = None,
        enable_headers: bool = None,
        knowledge_scene: str = None,
        knowledge_type: str = None,
        meta_extract_columns: List[main_models.CreateIndexRequestMetaExtractColumns] = None,
        pipeline_commercial_cu: int = None,
        pipeline_commercial_type: str = None,
        pipeline_retrieve_rate_limit_strategy: str = None,
        table: str = None,
    ):
        # The list of category IDs to import when creating the knowledge base. All files under the specified categories are imported. We recommend importing no more than 500 files. For remaining files, call the **SubmitIndexAddDocumentsJob** operation to continue importing.
        self.category_ids = category_ids
        # <props="china">
        # 
        # The chunk size, which specifies the maximum number of characters per text chunk. When this length is exceeded:
        # 
        # - **Intelligent chunking** (when `chunkMode` is not specified): The text is likely to be truncated.
        # - **Custom chunking** (when `chunkMode` is specified): The text is forcibly truncated.
        # 
        # 
        # 
        # <props="intl">
        # The chunk size, which specifies the maximum number of characters per text chunk. When this length is exceeded, the text is likely to be truncated.
        # 
        # 
        # 
        # Value range: [1-6000]. If not specified, the default value is 500.
        # 
        # > If `ChunkSize` is set to a value less than 100, you must also set `OverlapSize`. You can also leave both parameters unspecified, and the system uses default values.
        self.chunk_size = chunk_size
        # <props="china">
        # The structure of the data table (column names, types, etc.).
        # 
        # 
        # <props="intl">
        # 
        # > This parameter is not available. Do not pass this parameter.
        # >
        self.columns = columns
        # > This parameter is not available. Do not pass this parameter.
        # >
        self.create_index_type = create_index_type
        # The knowledge base description. The description can be up to 1000 characters in length.
        # Default value: empty.
        self.description = description
        # The list of files to import when creating the knowledge base. Specify file IDs here. We recommend importing no more than 10,000 files. For remaining files, call the **SubmitIndexAddDocumentsJob** operation to continue importing.
        self.document_ids = document_ids
        # <props="china">
        # 
        # The embedding model used by the knowledge base. The embedding model transforms the original input prompt and knowledge text into numerical vectors for similarity comparison. The text-embedding-v4 model is a comprehensive upgrade over text-embedding-v3 in terms of language support, code snippet quantization, and vector dimensions selection, and is suitable for most scenarios. For more information, see [Vectorization](https://help.aliyun.com/document_detail/2842587.html). Valid values:
        # - text-embedding-v4
        # - text-embedding-v3
        # 
        # Default value: empty, which uses the text-embedding-v3 model.
        # 
        # 
        # 
        # 
        # <props="intl">
        # 
        # The embedding model used by the knowledge base. The embedding model transforms the original input prompt and knowledge text into numerical vectors for similarity comparison. The default text-embedding-v2 model (cannot be changed) supports Chinese, English, and multiple other languages, and performs normalization on vector results. For more information, see [Vectorization](https://help.aliyun.com/document_detail/2842587.html). Valid values:
        # - text-embedding-v2
        # 
        # Default value: empty, which uses the text-embedding-v2 model.
        self.embedding_model_name = embedding_model_name
        # Specifies whether to enable multi-turn conversation rewriting. Valid values:
        # 
        # - true: Enabled.
        # - false: Disabled.
        # 
        # If not specified, this feature is enabled by default.
        self.enable_rewrite = enable_rewrite
        # The knowledge base name. The name must be 1 to 20 characters in length and can contain Chinese characters, letters, digits, underscores (_), hyphens (-), periods (.), and colons (:).
        # 
        # This parameter is required.
        self.name = name
        # The chunk overlap size, which specifies the number of overlapping characters between the current text chunk and the previous text chunk. Value range: [0-1024].
        # 
        # If not specified, the default value is 100.
        # >`OverlapSize` must be less than `ChunkSize`. Otherwise, chunking exceptions occur.
        self.overlap_size = overlap_size
        # <props="intl">This parameter is not available. Do not pass this parameter.
        # 
        # <props="china">A natural language instruction for fine-grained control of the reranking model\\"s behavior.
        # <notice>This parameter takes effect only when rerank_mode is set to "custom".
        self.rerank_instruct = rerank_instruct
        # The similarity threshold. Only text chunks with similarity scores exceeding this value are recalled. This parameter filters the text chunks returned by the reranking model. Value range: [0.01-1.00].
        # 
        # If not specified, the default value is 0.01.
        self.rerank_min_score = rerank_min_score
        # <props="china">
        # Specifies the instruction intervention mode for the reranking model to determine its scoring preference.
        # 
        # **Valid values:**
        # 
        # - **qa**: (Default) Q&A mode. The model tends to assign higher scores to candidates that directly answer the query. Recommended for Q&A scenarios.
        # 
        # - **similar**: Similarity mode. The model tends to assign higher scores to candidates with high content consistency with the query. Recommended for matching and retrieval scenarios.
        # 
        # - **custom**: Custom mode. The model\\"s ranking behavior is determined by the instruction in the rerank_instruct parameter.
        # 
        # 
        # 
        # <props="intl">This parameter is not available. Do not pass this parameter.
        # [_single.params.RerankMode.enum.similar: 相似模式。]similar: Similarity mode.
        # [_single.params.RerankMode.enum.custom: 自定义模式。]custom: Custom mode.
        # [_single.params.RerankMode.enum.qa:（默认值） 问答模式。]qa: (Default) Q&A mode.
        # [parameters.33.schema.enumValueTitles.similar: 相似模式。]similar: Similarity mode.
        # [parameters.33.schema.enumValueTitles.custom: 自定义模式。]custom: Custom mode.
        # [parameters.33.schema.enumValueTitles.qa:（默认值） 问答模式。]qa: (Default) Q&A mode.
        self.rerank_mode = rerank_mode
        # The reranking model used by the knowledge base. The reranking model is an external scoring system that calculates the similarity score between the user query and each text chunk in the knowledge base, sorts them in descending order, and returns the top K text chunks with the highest scores. Valid values:
        # 
        # 
        # <props="china">
        # 
        # - qwen3-rerank-hybrid: qwen3-rerank(hybrid) reranking.
        # - qwen3-rerank: qwen3-rerank reranking.
        # - gte-rerank-hybrid: gte-rerank(hybrid) reranking.
        # - gte-rerank: gte-rerank reranking.
        # 
        # 
        # 
        # <props="intl">
        # 
        # - gte-rerank-hybrid: official reranking.
        # - gte-rerank: gte-rerank reranking.
        # 
        # 
        # 
        # 
        # 
        # <props="china">
        # 
        # Default value: empty, which uses qwen3-rerank.
        # > If you only need semantic reranking, use `qwen3-rerank`. If you need both semantic reranking and text matching features to ensure relevance, use `qwen3-rerank-hybrid`.
        # >
        # 
        # 
        # 
        # 
        # <props="intl">
        # 
        # Default value: empty, which uses gte-rerank-hybrid.
        # > If you only need semantic reranking, use `gte-rerank`. If you need both semantic reranking and text matching features to ensure relevance, use `gte-rerank-hybrid`.
        # >
        # 
        # 
        # 
        # 
        # 
        # <props="china">
        # 
        # > `gte-rerank-hybrid` and `gte-rerank` will no longer be updated and are not recommended.
        # >
        self.rerank_model_name = rerank_model_name
        # <props="china">
        # 
        # The sentence separator, which takes effect only when `chunkMode`=**regex** (it does not take effect in other modes even if specified). You can pass a single regular expression (multiple expressions are not supported) to split files into small text chunks.
        # 
        # When using intelligent chunking (when `chunkMode` is not specified), keep the default empty value.
        # 
        # 
        # 
        # 
        # <props="intl">
        # 
        # > This parameter is not available. Do not pass this parameter.
        self.separator = separator
        # The AnalyticDB for PostgreSQL instance ID (required only when `SinkType` is set to ADB). Obtain this ID from the [AnalyticDB for PostgreSQL instance list](https://gpdbnext.console.aliyun.com/gpdb/list) page.
        self.sink_instance_id = sink_instance_id
        # The region of the AnalyticDB for PostgreSQL instance (required only when `SinkType` is set to ADB). Call <props="china">[DescribeRegions](https://www.alibabacloud.com/help/en/analyticdb-for-postgresql/developer-reference/api-gpdb-2016-05-03-describeregions)<props="intl">[DescribeRegions](https://www.alibabacloud.com/help/zh/analyticdb/analyticdb-for-postgresql/developer-reference/api-gpdb-2016-05-03-describeregions?spm=a2c63.p38356.0.i3) to obtain the list of regions.
        self.sink_region = sink_region
        # The vector storage type of the knowledge base. For more information, see [Knowledge base](https://help.aliyun.com/document_detail/2807740.html). Valid values:
        # - BUILT_IN: Vector data is hosted on the Alibaba Cloud Model Studio platform.
        # - ADB: AnalyticDB for PostgreSQL database. If you need advanced features such as database management, auditing, and monitoring, select ADB.
        # > If you have not used ADB storage on Alibaba Cloud Model Studio before, go to the <props="china">[Create Knowledge Base](https://bailian.console.aliyun.com/#/knowledge-base/create)<props="intl">[Create Knowledge Base](https://bailian.console.alibabacloud.com/#/knowledge-base/create) page, select ADB-PG as the vector storage type, and complete authorization as prompted. If you pass ADB, you must specify the `SinkInstanceId` and `SinkRegion` parameters.
        # 
        # This parameter is required.
        self.sink_type = sink_type
        # >Notice: This parameter is required in the latest SDK. Otherwise, calling the SubmitIndexJob operation returns an error: Required parameter(data_sources) missing or invalid.
        # 
        # The data source type. Valid values:
        # - DATA_CENTER_CATEGORY: Category type. Imports all files under specified categories in <props="china">[Application Data](https://bailian.console.aliyun.com/?tab=app#/data-center)<props="intl">[Application Data](https://modelstudio.console.alibabacloud.com/?tab=app#/data-center). Multiple categories can be imported simultaneously.
        # - DATA_CENTER_FILE: File type. Imports specified files from <props="china">[Application Data](https://bailian.console.aliyun.com/?tab=app#/data-center)<props="intl">[Application Data](https://modelstudio.console.alibabacloud.com/?tab=app#/data-center). Multiple files can be imported simultaneously.
        # 
        # > If this parameter is set to DATA_CENTER_CATEGORY, you must specify the `CategoryIds` parameter. If this parameter is set to DATA_CENTER_FILE, you must specify the `DocumentIds` parameter.
        # >
        # 
        # > To create an empty knowledge base, use an empty category that contains no files: set this parameter to DATA_CENTER_CATEGORY and pass the empty category ID in `CategoryIds`.
        # >
        self.source_type = source_type
        # The knowledge base type.
        # 
        # **Valid values:**
        # 
        # - unstructured: A document search or audio/video knowledge base. The default scenario for document search type is basic document Q&A. <props="china">To create other scenarios, pass the knowledgeType and knowledgeScene parameters.
        # 
        # <props="china">
        # 
        # - structured: A data query or image-based Q&A knowledge base.
        # 
        # 
        # 
        # > The knowledge base type cannot be changed after creation.
        # >
        # 
        # This parameter is required.
        self.structure_type = structure_type
        # <props="china">
        # 
        # Obtained by clicking the ID icon next to the table name on the Tables tab of [Data Connections](https://bailian.console.aliyun.com/cn-beijing?tab=app#/connector/list) table connector. If the list contains multiple IDs, only the first one is used.
        # 
        # 
        # 
        # 
        # <props="intl">
        # 
        # > This parameter is not available. Do not pass this parameter.
        # >
        self.table_ids = table_ids
        self.channel_type = channel_type
        # <props="china">
        # 
        # Enables custom chunking and specifies the chunking strategy. For more information, see [Knowledge base](https://help.aliyun.com/document_detail/2807740.html).
        # 
        # Valid values (only one value can be passed at a time):
        # 
        # - **length**: Chunk by length. Strictly chunks according to the specified `ChunkSize` and `OverlapSize`. If these two parameters are not passed, the system uses default values (`ChunkSize` of 500 and `OverlapSize` of 100). Chunking by length does not support `Separator` (it does not take effect even if specified).
        # - **page**: Chunk by page. If `ChunkSize` is specified, it is also considered during chunking (if not passed, the default value of 500 is used). Chunking by page does not support `OverlapSize` or `Separator` (they do not take effect even if specified).
        # - **h1**: Chunk by first-level headings. If `ChunkSize` is specified, it is also considered during chunking (if not passed, the default value of 500 is used). Chunking by first-level headings does not support `OverlapSize` or `Separator` (they do not take effect even if specified).
        # - **h2**: Chunk by second-level headings. If `ChunkSize` is specified, it is also considered during chunking (if not passed, the default value of 500 is used). Chunking by second-level headings does not support `OverlapSize` or `Separator` (they do not take effect even if specified).
        # - **regex**: Chunk by regular expression. The `Separator` parameter must be specified. If `ChunkSize` is specified, it is also considered during chunking (if not passed, the default value of 500 is used). Chunking by regular expression does not support `OverlapSize` (it does not take effect even if specified).
        # 
        # If not specified, intelligent chunking is used by default.
        # 
        # 
        # 
        # 
        # <props="intl">
        # 
        # > This parameter is not available. Do not pass this parameter.
        self.chunk_mode = chunk_mode
        self.connect_id = connect_id
        self.database = database
        self.datasource_code = datasource_code
        # Specifies whether to treat the first row of all xlsx and xls files as headers and concatenate them into each text chunk, preventing the large language model from treating headers as regular data rows.
        # 
        # 
        # > Enable this feature only when all imported files are in .xlsx or .xls format and contain headers. Otherwise, do not enable it.
        # >
        # 
        # Valid values:
        # - true: Enabled.
        # - false: Disabled.
        # 
        # If not specified, this feature is disabled by default.
        self.enable_headers = enable_headers
        self.knowledge_scene = knowledge_scene
        # <props="china">
        # The specific knowledge type, which further specifies the type of data processed by the knowledge base.
        # <notice>This parameter and knowledgeScene must be provided together or omitted together. They cannot be set independently. If both are omitted, the system uses default configurations based on structureType.
        # 
        # **Settings constraint**: The value of this parameter must match the selected structureType and determines the active values for knowledgeScene.
        # 
        # **Valid values**:
        # - document: Document search. Must be used with structureType: unstructured.
        # - table: Data query. Must be used with structureType: structured.
        # - image: Image-based Q&A. Must be used with structureType: structured.
        # - multimedia: Audio/video search. Must be used with structureType: unstructured.
        # 
        # 
        # 
        # 
        # <props="intl">This parameter is not available. Do not pass this parameter.
        self.knowledge_type = knowledge_type
        # The metadata extraction configuration. Metadata is a set of additional attributes related to unstructured data content. These attributes are integrated into text chunks as key-value pairs. For more information, see [Knowledge base](https://help.aliyun.com/document_detail/2807740.html).
        self.meta_extract_columns = meta_extract_columns
        # <props="china">The number of RCUs for the knowledge base (required only when pipelineCommercialType is set to enterprise). Value range: [1-200].
        # 
        # 
        # <props="intl">
        # 
        # > This parameter is not available. Do not pass this parameter.
        # >
        self.pipeline_commercial_cu = pipeline_commercial_cu
        # <props="china">
        # 
        # The [specification type](https://help.aliyun.com/document_detail/2997110.html) of the knowledge base. Valid values:
        # - standard: Standard Edition.
        # - enterprise: Ultimate Edition.
        # 
        # 
        # 
        # <props="intl">
        # 
        # > This parameter is not available. Do not pass this parameter.
        # >
        self.pipeline_commercial_type = pipeline_commercial_type
        # <props="china">The rate limiting strategy for knowledge base dependent links (required only when pipelineCommercialType is set to enterprise).
        # Valid values:
        # downgrade: Downgrade processing (switch to lightweight link retrieval).
        # If not specified, the default value is downgrade.
        # 
        # 
        # <props="intl">
        # 
        # > This parameter is not available. Do not pass this parameter.
        # >
        self.pipeline_retrieve_rate_limit_strategy = pipeline_retrieve_rate_limit_strategy
        self.table = table

    def validate(self):
        if self.columns:
            for v1 in self.columns:
                 if v1:
                    v1.validate()
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

        if self.rerank_instruct is not None:
            result['RerankInstruct'] = self.rerank_instruct

        if self.rerank_min_score is not None:
            result['RerankMinScore'] = self.rerank_min_score

        if self.rerank_mode is not None:
            result['RerankMode'] = self.rerank_mode

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

        if self.channel_type is not None:
            result['channelType'] = self.channel_type

        if self.chunk_mode is not None:
            result['chunkMode'] = self.chunk_mode

        if self.connect_id is not None:
            result['connectId'] = self.connect_id

        if self.database is not None:
            result['database'] = self.database

        if self.datasource_code is not None:
            result['datasourceCode'] = self.datasource_code

        if self.enable_headers is not None:
            result['enableHeaders'] = self.enable_headers

        if self.knowledge_scene is not None:
            result['knowledgeScene'] = self.knowledge_scene

        if self.knowledge_type is not None:
            result['knowledgeType'] = self.knowledge_type

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

        if m.get('RerankInstruct') is not None:
            self.rerank_instruct = m.get('RerankInstruct')

        if m.get('RerankMinScore') is not None:
            self.rerank_min_score = m.get('RerankMinScore')

        if m.get('RerankMode') is not None:
            self.rerank_mode = m.get('RerankMode')

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

        if m.get('channelType') is not None:
            self.channel_type = m.get('channelType')

        if m.get('chunkMode') is not None:
            self.chunk_mode = m.get('chunkMode')

        if m.get('connectId') is not None:
            self.connect_id = m.get('connectId')

        if m.get('database') is not None:
            self.database = m.get('database')

        if m.get('datasourceCode') is not None:
            self.datasource_code = m.get('datasourceCode')

        if m.get('enableHeaders') is not None:
            self.enable_headers = m.get('enableHeaders')

        if m.get('knowledgeScene') is not None:
            self.knowledge_scene = m.get('knowledgeScene')

        if m.get('knowledgeType') is not None:
            self.knowledge_type = m.get('knowledgeType')

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
        # The Chinese description of the metadata field. The description can be up to 1000 characters in length and can contain Chinese characters, letters, digits, underscores (_), hyphens (-), periods (.), and colons (:). Default value: empty.
        self.desc = desc
        # Specifies whether this metadata field and its value participate in the large language model\\"s answer generation process along with the text chunk content. Valid values:
        # 
        # - true: Enabled.
        # - false: Disabled.
        # 
        # Default value: false.
        self.enable_llm = enable_llm
        # Specifies whether this metadata field and its value participate in knowledge base retrieval along with the text chunk content. Valid values:
        # 
        # - true: Enabled.
        # - false: Disabled.
        # 
        # Default value: false.
        self.enable_search = enable_search
        # The metadata field. The field must be 1 to 50 characters in length and can contain only letters and underscores. If this parameter is specified, you must also specify the `Value` and `Type` parameters.
        self.key = key
        # The extraction method for the metadata field. Valid values:
        # 
        # - constant: Constant.
        # - variable: Variable.
        # - custom_prompt: Large language model.
        # - regular: Regular expression.
        # - keywords: Keyword search.
        self.type = type
        # The value of the metadata field.
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

class CreateIndexRequestColumns(DaraModel):
    def __init__(
        self,
        column: str = None,
        is_recall: bool = None,
        is_search: bool = None,
        name: str = None,
        type: str = None,
    ):
        # > This parameter is not available. Do not pass this parameter.
        # >
        self.column = column
        # <props="china">
        # 
        # Specifies whether this column participates in model responses. When enabled, the search results of this column are used as input for the large language model to generate answers. Valid values:
        # 
        # - true: Enabled.
        # - false: Disabled.
        # 
        # 
        # 
        # 
        # <props="intl">
        # 
        # > This parameter is not available. Do not pass this parameter.
        # >
        self.is_recall = is_recall
        # <props="china">
        # 
        # Specifies whether this column participates in knowledge base retrieval. When enabled, the knowledge base can search within the data of this column. Valid values:
        # 
        # - true: Enabled.
        # - false: Disabled.
        # 
        # 
        # 
        # 
        # <props="intl">
        # 
        # > This parameter is not available. Do not pass this parameter.
        # >
        self.is_search = is_search
        # <props="china">
        # The field name. Must be consistent with the header of the data table created in Application Data.
        # 
        # 
        # 
        # <props="intl">
        # 
        # > This parameter is not available. Do not pass this parameter.
        # >
        self.name = name
        # <props="china">
        # 
        # The field type. Must be consistent with the header of the data table created in Application Data. Valid values:
        # 
        # - string
        # - double
        # - long
        # - datetime
        # - image_url
        # 
        # 
        # 
        # <props="intl">
        # 
        # > This parameter is not available. Do not pass this parameter.
        # >
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

