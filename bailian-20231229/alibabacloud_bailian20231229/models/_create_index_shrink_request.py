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
        # You can import files when you create a knowledge base. Specify category IDs to import all files under the corresponding categories. We recommend importing no more than 10,000 files. If you have more files, you can call the **SubmitIndexAddDocumentsJob** operation to import them later.
        self.category_ids_shrink = category_ids_shrink
        # <props="china">
        # 
        # The chunk size, which is the maximum number of characters for each text chunk. If this length is exceeded:
        # 
        # - **Smart chunking** (the \\`chunkMode\\` parameter is not specified): The text is likely to be truncated.
        # 
        # - **Custom chunking** (the \\`chunkMode\\` parameter is specified): The text is forcibly truncated.
        # 
        # 
        # 
        # <props="intl">
        # 
        # The chunk size, which is the maximum number of characters for each text chunk. If this length is exceeded, the text is likely to be truncated.
        # 
        # 
        # 
        # The value must be between 1 and 6000. If you do not specify this parameter, the default value 500 is used.
        # 
        # > If you set \\`ChunkSize\\` to a value less than 100, you must also set \\`OverlapSize\\`. You can also leave both parameters unspecified, and the system will use the default values.
        self.chunk_size = chunk_size
        # <props="china">
        # 
        # The structure of the data table (column names, types, etc.).
        # 
        # 
        # 
        # <props="intl">
        # 
        # > This parameter is not yet available. Do not specify it.
        self.columns_shrink = columns_shrink
        # > This parameter is not yet available. Do not specify it.
        self.create_index_type = create_index_type
        # The description of the knowledge base. The description can be 0 to 1,000 English or Chinese characters in length.
        # The default value is empty.
        self.description = description
        # You can import files when you create a knowledge base. Specify a list of files to import by providing their IDs. We recommend importing no more than 10,000 files. If you have more files, you can call the **SubmitIndexAddDocumentsJob** operation to import them later.
        self.document_ids_shrink = document_ids_shrink
        # <props="china">
        # 
        # The vector model used by the knowledge base. A vector model converts the original input prompt and knowledge text into numerical vectors to compare their similarity. The text-embedding-v4 model is a comprehensive upgrade over the text-embedding-v3 model in terms of language support, vectorization of code snippets, and vector dimension selection. It is suitable for most scenarios. For more information, see [Vectorization](https://help.aliyun.com/document_detail/2842587.html). Valid values:
        # 
        # - text-embedding-v4
        # 
        # - text-embedding-v3
        # 
        # If you do not specify this parameter, \\`text-embedding-v3\\` is used.
        # 
        # 
        # 
        # <props="intl">
        # 
        # - The vector model used by the knowledge base. A vector model converts the original input prompt and knowledge text into numerical vectors to compare their similarity. The default text-embedding-v2 model (which cannot be changed for now) supports both Chinese and English, along with multiple other languages, and normalizes the vector results. For more information, see [Vectorization](https://help.aliyun.com/document_detail/2842587.html). Valid values:
        # 
        # 
        # 
        # 
        # - text-embedding-v2
        # 
        # If you do not specify this parameter, \\`text-embedding-v2\\` is used.
        self.embedding_model_name = embedding_model_name
        # Specifies whether to enable multi-turn conversation rewriting. Valid values:
        # 
        # - true: Enabled.
        # 
        # - false: Disabled.
        # 
        # If you do not specify this parameter, this feature is enabled by default.
        self.enable_rewrite = enable_rewrite
        # The name of the knowledge base. The name can be 1 to 20 characters in length and can contain Chinese characters, letters, digits, underscores (_), hyphens (-), periods (.), and colons (:).
        # 
        # This parameter is required.
        self.name = name
        # The overlap size, which is the number of overlapping characters between the current text chunk and the previous one. The value must be between 0 and 1024.
        # 
        # If you do not specify this parameter, the default value 100 is used.
        # 
        # > \\`OverlapSize\\` must be smaller than \\`ChunkSize\\`. Otherwise, chunking errors will occur.
        self.overlap_size = overlap_size
        # The name of the database. This parameter is required when creating a data query knowledge base.
        # 
        # The database must exist in the data source specified by \\`datasourceCode\\`.
        self.rerank_instruct = rerank_instruct
        # The similarity threshold. Only text chunks with a similarity score greater than this value are recalled. This is used to filter the text chunks returned by the reranking model. The value must be between 0.01 and 1.00.
        # 
        # If you do not specify this parameter, the default value 0.01 is used.
        self.rerank_min_score = rerank_min_score
        # The name of the data table. This parameter is required when creating a data query knowledge base.
        # 
        # The data table must exist in the data source specified by \\`connectId\\` or \\`datasourceCode\\`.
        self.rerank_mode = rerank_mode
        # The reranking model used by the knowledge base. The reranking model is an external scoring system that calculates a similarity score between the user\\"s question and each text chunk in the knowledge base, sorts them in descending order, and returns the top K text chunks. Valid values:
        # 
        # <props="china">
        # 
        # - qwen3-rerank-hybrid: qwen3-rerank (hybrid) reranking.
        # 
        # - qwen3-rerank: qwen3-rerank reranking.
        # 
        # - gte-rerank-hybrid: gte-rerank (hybrid) reranking.
        # 
        # - gte-rerank: gte-rerank reranking.
        # 
        # 
        # 
        # <props="intl">
        # 
        # - gte-rerank-hybrid: Official reranking.
        # 
        # - gte-rerank: gte-rerank reranking.
        # 
        # 
        # 
        # <props="china">
        # 
        # If you do not specify this parameter, \\`qwen3-rerank\\` is used.
        # 
        # > Use \\`qwen3-rerank\\` if you only need semantic sorting. Use \\`qwen3-rerank-hybrid\\` if you need both semantic sorting and text-matching features to ensure relevance.
        # 
        # 
        # 
        # <props="intl">
        # 
        # If you do not specify this parameter, \\`gte-rerank-hybrid\\` is used.
        # 
        # > Use \\`gte-rerank\\` if you only need semantic sorting. Use \\`gte-rerank-hybrid\\` if you need both semantic sorting and text-matching features to ensure relevance.
        # 
        # 
        # 
        # <props="china">
        # 
        # > The \\`gte-rerank-hybrid\\` and \\`gte-rerank\\` models are no longer updated and are not recommended.
        self.rerank_model_name = rerank_model_name
        # <props="china">
        # 
        # The sentence separator. This parameter takes effect only when \\`chunkMode\\` is set to **regex**. It is ignored in other modes, even if specified. You can enter a regular expression (multiple expressions are not supported) to split the file into smaller text chunks.
        # 
        # For smart chunking (the \\`chunkMode\\` parameter is not specified), you can leave this parameter empty.
        # 
        # 
        # 
        # <props="intl">
        # 
        # > This parameter is not yet available. Do not specify it.
        self.separator = separator
        # The ID of the AnalyticDB for PostgreSQL instance. This parameter is required only when \\`SinkType\\` is set to ADB. Go to the [AnalyticDB for PostgreSQL instance list](https://gpdbnext.console.aliyun.com/gpdb/list) page to obtain this ID.
        self.sink_instance_id = sink_instance_id
        # The region where the AnalyticDB for PostgreSQL instance is located. This parameter is required only when \\`SinkType\\` is set to ADB. You can call the <props="intl">[DescribeRegions ](https://www.alibabacloud.com/help/zh/analyticdb/analyticdb-for-postgresql/developer-reference/api-gpdb-2016-05-03-describeregions?spm=a2c63.p38356.0.i3)operation to obtain a list of regions.
        self.sink_region = sink_region
        # The storage class for the knowledge base vectors. For more information, see [Knowledge bases](https://help.aliyun.com/document_detail/2807740.html). Valid values:
        # 
        # - BUILT_IN: Hosts the vector data on the Alibaba Cloud Model Studio platform.
        # 
        # - ADB: AnalyticDB for PostgreSQL. We recommend choosing ADB if you need advanced features such as database management, auditing, and monitoring.
        # 
        # > If you have not used ADB storage on Alibaba Cloud Model Studio, go to the <props="intl">[Create Knowledge Base](https://bailian.console.alibabacloud.com/#/knowledge-base/create) page, set the vector storage class to ADB-PG, and follow the on-screen instructions to grant the required permissions. If you set this parameter to ADB, you must specify the \\`SinkInstanceId\\` and \\`SinkRegion\\` parameters.
        # 
        # This parameter is required.
        self.sink_type = sink_type
        # >Notice: 
        # 
        # In the latest SDK version, this parameter is required. Otherwise, calling the SubmitIndexJob operation will result in the error: Required parameter(data_sources) missing or invalid.
        # 
        # 
        # 
        # The source of the imported data. Valid values:
        # 
        # - DATA_CENTER_CATEGORY: Category type. Imports all files under the specified categories in <props="intl">[Application Data](https://modelstudio.console.alibabacloud.com/?tab=app#/data-center). You can import multiple categories at the same time.
        # 
        # - DATA_CENTER_FILE: File type. Imports the specified files from <props="intl">[Application Data](https://modelstudio.console.alibabacloud.com/?tab=app#/data-center). You can import multiple files at the same time.
        # 
        # > If you set this parameter to DATA_CENTER_CATEGORY, you must specify the \\`CategoryIds\\` parameter. If you set this parameter to DATA_CENTER_FILE, you must specify the \\`DocumentIds\\` parameter.
        # 
        # > To create an empty knowledge base, use an empty category that contains no files. Set this parameter to DATA_CENTER_CATEGORY and specify the ID of the empty category for \\`CategoryIds\\`.
        self.source_type = source_type
        # The type of the knowledge base.
        # 
        # **Valid values**:
        # 
        # - unstructured: A knowledge base for document search, audio, or video. The default scenario for document search is basic document Q\\&A.
        # 
        # <props="china">
        # 
        # - structured: A knowledge base for data query or image Q\\&A.
        # 
        # 
        # 
        # 
        # > The type of a knowledge base cannot be changed after it is created.
        # 
        # This parameter is required.
        self.structure_type = structure_type
        # <props="china">
        # 
        # Obtain the table ID on the Tables tab of the table connector in Data Connections by clicking the ID icon next to the table name. If the list contains multiple IDs, only the first one is used.
        # 
        # 
        # 
        # <props="intl">
        # 
        # > This parameter is not yet available. Do not specify it.
        self.table_ids_shrink = table_ids_shrink
        self.channel_type = channel_type
        # <props="china">
        # 
        # Enables custom chunking and specifies the chunking policy. For more information, see [Knowledge bases](https://help.aliyun.com/document_detail/2807740.html).
        # 
        # Possible values (only one value can be specified at a time):
        # 
        # - **length**: Chunks by length. The text is strictly chunked according to the \\`ChunkSize\\` and \\`OverlapSize\\` you specify. If you do not specify these two parameters, the system uses the default values (\\`ChunkSize\\` is 500, \\`OverlapSize\\` is 100). Chunking by length does not support \\`Separator\\` (it is ignored even if specified).
        # 
        # - **page**: Chunks by page. If \\`ChunkSize\\` is specified, it is also considered during chunking (if not specified, the default value 500 is used). Chunking by page does not support \\`OverlapSize\\` or \\`Separator\\` (they are ignored even if specified).
        # 
        # - **h1**: Chunks by level-1 heading. If \\`ChunkSize\\` is specified, it is also considered during chunking (if not specified, the default value 500 is used). Chunking by level-1 heading does not support \\`OverlapSize\\` or \\`Separator\\` (they are ignored even if specified).
        # 
        # - **h2**: Chunks by level-2 heading. If \\`ChunkSize\\` is specified, it is also considered during chunking (if not specified, the default value 500 is used). Chunking by level-2 heading does not support \\`OverlapSize\\` or \\`Separator\\` (they are ignored even if specified).
        # 
        # - **regex**: Chunks by regular expression. You must specify the \\`Separator\\` parameter. If \\`ChunkSize\\` is specified, it is also considered during chunking (if not specified, the default value 500 is used). Chunking by regular expression does not support \\`OverlapSize\\` (it is ignored even if specified).
        # 
        # If you do not specify this parameter, smart chunking is used by default.
        # 
        # 
        # 
        # <props="intl">
        # 
        # > This parameter is not yet available. Do not specify it.
        self.chunk_mode = chunk_mode
        self.connect_id = connect_id
        self.database = database
        self.datasource_code = datasource_code
        # Specifies whether to treat the first row of all .xlsx and .xls files as the table header and append it to each text chunk. This prevents the LLM from treating the header as a regular data row.
        # 
        # > We recommend enabling this feature only when all imported files are in .xlsx or .xls format and contain a header. Otherwise, do not enable it.
        # 
        # Valid values:
        # 
        # - true: Enabled.
        # 
        # - false: Disabled.
        # 
        # If you do not specify this parameter, this feature is disabled by default.
        self.enable_headers = enable_headers
        self.knowledge_scene = knowledge_scene
        # The data source code. This parameter is required when creating a data query knowledge base and is used with \\`table\\` and \\`database\\`.
        # 
        # <props="china">
        # 
        # We recommend using the new \\`connectId\\` parameter, which you can obtain from the data connector card on the [Data Connections](https://modelstudio.console.alibabacloud.com/?tab=app#/connector/list) page. This parameter is still compatible but will no longer be maintained in the future.
        # 
        # 
        # 
        # > - This operation does not support associating custom databases. Use the Alibaba Cloud Model Studio console to create them.
        self.knowledge_type = knowledge_type
        # The metadata extraction configuration. Metadata is a series of additional attributes related to unstructured data content. These attributes are integrated into text chunks as key-value pairs. For more information, see [Knowledge bases](https://help.aliyun.com/document_detail/2807740.html).
        self.meta_extract_columns_shrink = meta_extract_columns_shrink
        # <props="china">
        # 
        # The number of RCUs for the knowledge base. This parameter is required only when \\`pipelineCommercialType\\` is set to \\`enterprise\\`. The value must be between 1 and 200.
        # 
        # 
        # 
        # <props="intl">
        # 
        # > This parameter is not yet available. Do not specify it.
        self.pipeline_commercial_cu = pipeline_commercial_cu
        # <props="china">
        # 
        # The [edition type](https://help.aliyun.com/document_detail/2997110.html) of the knowledge base. Valid values:
        # 
        # - standard: Standard Edition
        # 
        # - enterprise: Ultimate Edition
        # 
        # 
        # 
        # <props="intl">
        # 
        # > This parameter is not yet available. Do not specify it.
        self.pipeline_commercial_type = pipeline_commercial_type
        # <props="china">
        # 
        # The rate limiting policy for the knowledge base dependency chain. This parameter is required only when \\`pipelineCommercialType\\` is set to \\`enterprise\\`.
        # Value:
        # downgrade: Degrades the service (switches to using a lightweight retrieval chain).
        # If you do not specify this parameter, the default value \\`downgrade\\` is used.
        # 
        # 
        # 
        # <props="intl">
        # 
        # > This parameter is not yet available. Do not specify it.
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

