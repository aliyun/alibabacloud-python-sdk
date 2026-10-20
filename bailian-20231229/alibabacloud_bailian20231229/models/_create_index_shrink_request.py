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
        description: str = None,
        document_ids_shrink: str = None,
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
        table_ids_shrink: str = None,
        channel_type: str = None,
        chunk_mode: str = None,
        connect_id: str = None,
        database: str = None,
        datasource_code: str = None,
        enable_headers: bool = None,
        knowledge_scene: str = None,
        knowledge_type: str = None,
        meta_extract_columns_shrink: str = None,
        pipeline_commercial_cu: int = None,
        pipeline_commercial_type: str = None,
        pipeline_retrieve_rate_limit_strategy: str = None,
        table: str = None,
    ):
        # You can import files synchronously when you create a knowledge base. Here, you can import all files under a specified category by specifying the category ID. We recommend that you import no more than 500 files. If you have remaining files, you can call the **SubmitIndexAddDocumentsJob** operation to continue importing them later.
        self.category_ids_shrink = category_ids_shrink
        # <props="china">
        # 
        # The chunk size, which is the maximum number of characters in each text chunk. If the text exceeds this length:
        # 
        # - **Intelligent chunking** (chunkMode is not specified): The text is highly likely to be truncated.
        # - **Custom chunking** (chunkMode is specified): The text is forcibly truncated.
        # 
        # 
        # 
        # <props="intl">
        # The chunk size, which is the maximum number of characters in each text chunk. If the text exceeds this length, it is highly likely to be truncated.
        # 
        # 
        # 
        # Valid values: [1, 6000]. Default value: 500.
        # 
        # > If you set ChunkSize to a value less than 100, you must also set OverlapSize. You can also leave these two parameters unspecified, and the system uses the default values.
        self.chunk_size = chunk_size
        # <props="china">
        # The structure of the data table, such as column names and types.
        # 
        # 
        # <props="intl">
        # 
        # > This parameter is not available. Do not pass this parameter.
        # >
        self.columns_shrink = columns_shrink
        # > This parameter is not available. Do not pass this parameter.
        # >
        self.create_index_type = create_index_type
        # The description of the knowledge base. The description must be 0 to 200 characters in length and can contain English and Chinese characters.
        # Default value: empty.
        self.description = description
        # You can import files synchronously when you create a knowledge base. Here, you can specify the list of files to be imported by passing file IDs. We recommend that you import no more than 10,000 files. If you have remaining files, you can call the **SubmitIndexAddDocumentsJob** operation to continue importing them later.
        self.document_ids_shrink = document_ids_shrink
        # <props="china">
        # 
        # The embedding model used by the knowledge base. The embedding model is used to transform the original input prompt and knowledge text into numerical vectors for similarity comparison. Compared with the text-embedding-v3 model, the text-embedding-v4 model is comprehensively upgraded in terms of language support, code snippet vectorization effect, and selection of vector dimensions, and is suitable for most scenarios. For more information, refer to [Quantization](https://help.aliyun.com/document_detail/2842587.html). Valid values:
        # - text-embedding-v4
        # - text-embedding-v3
        # 
        # Default value: empty. In this case, the text-embedding-v3 model is used.
        # 
        # 
        # 
        # 
        # <props="intl">
        # 
        # The embedding model used by the knowledge base. The embedding model is used to transform the original input prompt and knowledge text into numerical vectors for similarity comparison. The default text-embedding-v2 model (which cannot be changed at the moment) supports not only Chinese and English but also multiple other languages, and performs normalization on the vector results. For more information, refer to [Quantization](https://help.aliyun.com/document_detail/2842587.html). Valid values:
        # - text-embedding-v2
        # 
        # Default value: empty. In this case, the text-embedding-v2 model is used.
        self.embedding_model_name = embedding_model_name
        # Specifies whether to enable multi-turn conversation rewriting. Valid values:
        # 
        # - true: enabled.
        # - false: disabled.
        # 
        # Default value: true.
        self.enable_rewrite = enable_rewrite
        # The name of the knowledge base. The name must be 1 to 20 characters in length and can contain Chinese characters, English letters, digits, underscores (_), hyphens (-), periods (.), and colons (:).
        # 
        # This parameter is required.
        self.name = name
        # The chunk overlap size, which indicates the number of overlapping characters between the current text chunk and the previous text chunk. Valid values: [0, 1024].
        # 
        # Default value: 100.
        # > OverlapSize must be less than ChunkSize. Otherwise, chunking exceptions occur.
        self.overlap_size = overlap_size
        # <props="intl">This parameter is not available. Do not specify this parameter.
        # 
        # <props="china">Provides a natural language instruction to fine-tune the behavior of the reranking model.
        # <notice>This parameter takes effect only when rerank_mode is set to "custom".</notice>
        self.rerank_instruct = rerank_instruct
        # The similarity threshold. Only text chunks with a similarity score greater than this value are recalled. This parameter is used to filter the text chunks returned by the reranking model. Valid values: [0.01, 1.00].
        # 
        # Default value: 0.01.
        self.rerank_min_score = rerank_min_score
        # <props="china">
        # Specifies the instruction intervention mode of the reranking model to determine its scoring preference. Valid values:
        # 
        # - **qa**: question answering mode. This is the default value. The model tends to assign higher scores to candidates that can directly answer the query. We recommend that you use this mode in question answering scenarios.
        # 
        # - **similar**: similarity mode. The model tends to assign higher scores to candidates that are highly consistent with the query content. We recommend that you use this mode in matching and retrieval scenarios.
        # 
        # - **custom**: custom mode. The ranking behavior of the model is determined by the instruction in the rerank_instruct parameter.
        # 
        # 
        # 
        # <props="intl">This parameter is not available. Do not specify this parameter.
        self.rerank_mode = rerank_mode
        # The reranking model used by the knowledge base. The reranking model is a scoring system external to the knowledge base. It calculates the similarity score between the user\\"s question and each text chunk in the knowledge base, sorts the chunks in descending order of the scores, and returns the top K text chunks with the highest scores. Valid values:
        # 
        # 
        # <props="china">
        # 
        # - qwen3-rerank-hybrid: qwen3-rerank (hybrid) reranking.
        # - qwen3-rerank: qwen3-rerank reranking.
        # - gte-rerank-hybrid: gte-rerank (hybrid) reranking.
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
        # Default value: empty. In this case, qwen3-rerank is used.
        # > If you only need semantic reranking, you can use qwen3-rerank. If you need both semantic reranking and text matching features to ensure relevance, use qwen3-rerank-hybrid.
        # >
        # 
        # 
        # 
        # 
        # <props="intl">
        # 
        # Default value: empty. In this case, gte-rerank-hybrid is used.
        # > If you only need semantic reranking, you can use gte-rerank. If you need both semantic reranking and text matching features to ensure relevance, use gte-rerank-hybrid.
        # >
        # 
        # 
        # 
        # 
        # 
        # <props="china">
        # 
        # > gte-rerank-hybrid and gte-rerank will stop receiving updates and are not recommended.
        # >
        self.rerank_model_name = rerank_model_name
        # <props="china">
        # 
        # The sentence separator. This parameter takes effect only when chunkMode is set to **regex**. In other modes, this parameter does not take effect even if it is passed. You can pass a regular expression (multiple regular expressions are not supported) to split the file into small text chunks.
        # 
        # When you use intelligent chunking (chunkMode is not specified), leave this parameter empty.
        # 
        # 
        # 
        # 
        # <props="intl">
        # 
        # > This parameter is not available. Do not pass this parameter.
        self.separator = separator
        # The ID of the AnalyticDB for PostgreSQL instance. This parameter is required only when SinkType is set to ADB. Go to the [AnalyticDB for PostgreSQL Instance List](https://gpdbnext.console.aliyun.com/gpdb/list) page to obtain the ID.
        self.sink_instance_id = sink_instance_id
        # The region where the AnalyticDB for PostgreSQL instance resides. This parameter is required only when SinkType is set to ADB. You can call the <props="china">[DescribeRegions](https://www.alibabacloud.com/help/en/analyticdb-for-postgresql/developer-reference/api-gpdb-2016-05-03-describeregions)<props="intl">[DescribeRegions](https://www.alibabacloud.com/help/zh/analyticdb/analyticdb-for-postgresql/developer-reference/api-gpdb-2016-05-03-describeregions?spm=a2c63.p38356.0.i3) operation to obtain the region list.
        self.sink_region = sink_region
        # The vector storage type of the knowledge base. For more information, refer to [Knowledge base](https://help.aliyun.com/document_detail/2807740.html). Valid values:
        # - BUILT_IN: stores vector data in Alibaba Cloud Model Studio.
        # - ADB: AnalyticDB for PostgreSQL database. If you need advanced features such as managing, auditing, and monitoring the database, select ADB.
        # > If you have not used ADB storage in Alibaba Cloud Model Studio, go to the <props="china">[Create Knowledge Base](https://bailian.console.aliyun.com/#/knowledge-base/create)<props="intl">[Create Knowledge Base](https://bailian.console.alibabacloud.com/#/knowledge-base/create) page, select ADB-PG as the vector storage type, and complete the authorization as prompted. If you pass ADB, you must specify the SinkInstanceId and SinkRegion parameters.
        # 
        # This parameter is required.
        self.sink_type = sink_type
        # >Notice: This parameter is required in the latest SDK version. Otherwise, an error is reported when you call the SubmitIndexJob operation: Required parameter(data_sources) missing or invalid.</notice>
        # 
        # The source of the imported data. Valid values:
        # - DATA_CENTER_CATEGORY: the category type. This value indicates that all files under a specified category in <props="china">[Application Data](https://bailian.console.aliyun.com/?tab=app#/data-center)<props="intl">[Application Data](https://modelstudio.console.alibabacloud.com/?tab=app#/data-center) are imported. You can import multiple categories at a time.
        # - DATA_CENTER_FILE: the file type. This value indicates that specified files in <props="china">[Application Data](https://bailian.console.aliyun.com/?tab=app#/data-center)<props="intl">[Application Data](https://modelstudio.console.alibabacloud.com/?tab=app#/data-center) are imported. You can import multiple files at a time.
        # 
        # > If you set this parameter to DATA_CENTER_CATEGORY, you must specify the CategoryIds parameter. If you set this parameter to DATA_CENTER_FILE, you must specify the DocumentIds parameter.
        # >
        # 
        # > To create an empty knowledge base, you can use an empty category that contains no files: set this parameter to DATA_CENTER_CATEGORY and set CategoryIds to the ID of the empty category.
        # >
        self.source_type = source_type
        # The type of the knowledge base.
        # 
        # **Valid values**:
        # 
        # - unstructured: a knowledge base for document search or audio and video. The default use scenario for the document search type is basic document question answering. <props="china">To create a knowledge base for other scenarios, you must also pass the knowledgeType and knowledgeScene parameters.
        # 
        # <props="china">
        # 
        # - structured: a knowledge base for data querying or image question answering.
        # 
        # 
        # 
        # > Note that the type of a knowledge base cannot be changed after it is created.
        # >
        # 
        # This parameter is required.
        self.structure_type = structure_type
        # <props="china">
        # 
        # You can obtain the ID by clicking the ID icon next to the table name on the Tables tab of the Table Connector in [Data Connection](https://bailian.console.aliyun.com/cn-beijing?tab=app#/connector/list). If the list contains multiple IDs, only the first one is used.
        # 
        # 
        # 
        # 
        # <props="intl">
        # 
        # > This parameter is not available. Do not pass this parameter.
        # >
        self.table_ids_shrink = table_ids_shrink
        self.channel_type = channel_type
        # <props="china">
        # 
        # Enables custom chunking and specifies the chunking strategy. For more information, refer to [Knowledge base](https://help.aliyun.com/document_detail/2807740.html).
        # 
        # Valid values (you cannot pass multiple values at a time):
        # 
        # - **length**: chunks by length. The text is strictly chunked according to the ChunkSize and OverlapSize you specify. If you do not pass these two parameters, the system uses the default values (ChunkSize is 500 and OverlapSize is 100). Chunking by length does not support Separator (it does not take effect even if passed).
        # - **page**: chunks by page. If ChunkSize is specified, it is considered during chunking (if not passed, the default value 500 is used). Chunking by page does not support OverlapSize and Separator (they do not take effect even if passed).
        # - **h1**: chunks by level-1 heading. If ChunkSize is specified, it is considered during chunking (if not passed, the default value 500 is used). Chunking by level-1 heading does not support OverlapSize and Separator (they do not take effect even if passed).
        # - **h2**: chunks by level-2 heading. If ChunkSize is specified, it is considered during chunking (if not passed, the default value 500 is used). Chunking by level-2 heading does not support OverlapSize and Separator (they do not take effect even if passed).
        # - **regex**: chunks by regular expression. In this case, you must specify the Separator parameter. If ChunkSize is specified, it is considered during chunking (if not passed, the default value 500 is used). Chunking by regular expression does not support OverlapSize (it does not take effect even if passed).
        # 
        # Default value: empty. In this case, intelligent chunking is used.
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
        # Specifies whether to use the first row of all .xlsx and .xls files as the header and concatenate it to each text chunk to prevent the large language model from mistakenly treating the header as a normal data row.
        # 
        # 
        # > Enable this feature only when all imported files are in .xlsx or .xls format and contain headers. Otherwise, do not enable it.
        # >
        # 
        # Valid values:
        # - true: enabled.
        # - false: disabled.
        # 
        # Default value: false.
        self.enable_headers = enable_headers
        self.knowledge_scene = knowledge_scene
        # <props="china">
        # The specific knowledge type, which is used to further specify the type of data processed by the knowledge base.
        # <notice>This parameter must be provided or omitted together with knowledgeScene. It cannot be set separately. If both are omitted, the system uses the default configurations based on structureType.</notice>
        # 
        # **Settings** constraints: The value of this parameter must match the structureType you select and determines the active values for knowledgeScene.
        # 
        # **Valid values**:
        # - document: document search. Must be used with structureType: unstructured.
        # - table: data querying. Must be used with structureType: structured.
        # - image: image question answering. Must be used with structureType: structured.
        # - multimedia: audio and video search. Must be used with structureType: unstructured.
        # 
        # 
        # 
        # 
        # <props="intl">This parameter is not available. Do not pass this parameter.
        self.knowledge_type = knowledge_type
        # The metadata extraction configuration. Metadata is a series of additional attributes related to the content of unstructured data. These attributes are integrated into text chunks in the form of key-value pairs. For more information, refer to [Knowledge base](https://help.aliyun.com/document_detail/2807740.html).
        self.meta_extract_columns_shrink = meta_extract_columns_shrink
        # <props="china">The number of RCUs for the knowledge base. This parameter is required only when pipelineCommercialType is set to enterprise. Valid values: [1, 200].
        # 
        # 
        # <props="intl">
        # 
        # > This parameter is not available. Do not pass this parameter.
        # >
        self.pipeline_commercial_cu = pipeline_commercial_cu
        # <props="china">
        # 
        # The [edition](https://help.aliyun.com/document_detail/2997110.html) of the knowledge base. Valid values:
        # - standard: Standard Edition
        # - enterprise: Ultimate Edition
        # 
        # 
        # 
        # <props="intl">
        # 
        # > This parameter is not available. Do not pass this parameter.
        # >
        self.pipeline_commercial_type = pipeline_commercial_type
        # <props="china">The throttling handling strategy for the knowledge base dependency link. This parameter is required only when pipelineCommercialType is set to enterprise.
        # Valid values:
        # downgrade: downgrade processing (switches to lightweight link retrieval).
        # Default value: downgrade.
        # 
        # 
        # <props="intl">
        # 
        # > This parameter is not available. Do not pass this parameter.
        # >
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

        if self.table_ids_shrink is not None:
            result['TableIds'] = self.table_ids_shrink

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
            self.table_ids_shrink = m.get('TableIds')

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

