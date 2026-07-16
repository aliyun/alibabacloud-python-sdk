# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitIndexAddDocumentsJobShrinkRequest(DaraModel):
    def __init__(
        self,
        category_ids_shrink: str = None,
        chunk_mode: str = None,
        chunk_size: int = None,
        document_ids_shrink: str = None,
        enable_headers: bool = None,
        extra_shrink: str = None,
        index_id: str = None,
        overlap_size: int = None,
        separator: str = None,
        source_type: str = None,
    ):
        # A list of category IDs.
        self.category_ids_shrink = category_ids_shrink
        # <props="china">
        # 
        # The custom chunking mode. This setting applies only to the documents added in the current job. For more information, see [knowledge base](https://help.aliyun.com/document_detail/2807740.html). Valid values (you can specify only one value):
        # 
        # - **length**: Splits the text by a fixed length. The chunking strictly follows the specified `ChunkSize` and `OverlapSize`. If you do not specify these parameters, the system uses the default values: a `ChunkSize` of 500 and an `OverlapSize` of 100. This mode ignores the `Separator` parameter.
        # 
        # - **page**: Splits the text by page. If `ChunkSize` is specified, its value is also applied during chunking. If `ChunkSize` is not set, a default value of 500 is used. This mode ignores the `OverlapSize` and `Separator` parameters.
        # 
        # - **h1**: Splits the text by level-1 headings. If `ChunkSize` is specified, its value is also applied during chunking. If `ChunkSize` is not set, a default value of 500 is used. This mode ignores the `OverlapSize` and `Separator` parameters.
        # 
        # - **h2**: Splits the text by level-2 headings. If `ChunkSize` is specified, its value is also applied during chunking. If `ChunkSize` is not set, a default value of 500 is used. This mode ignores the `OverlapSize` and `Separator` parameters.
        # 
        # - **regex**: Splits the text by using a regular expression. The `Separator` parameter is required for this mode. If `ChunkSize` is specified, its value is also applied during chunking. If `ChunkSize` is not set, a default value of 500 is used. This mode ignores the `OverlapSize` parameter.
        # 
        # If this parameter is not set, intelligent chunking is used by default.
        # 
        # 
        # 
        # <props="intl">
        # 
        # > This parameter is not available. Do not specify it.
        self.chunk_mode = chunk_mode
        # <props="china">
        # 
        # The chunk size. Specifies the maximum number of characters for each text chunk. This setting applies only to the documents added in the current job. If a text segment exceeds this size, the behavior depends on the chunking mode:
        # 
        # - **Intelligent chunking** (if `ChunkMode` is not set): The text may be truncated.
        # 
        # - **Custom chunking** (if `ChunkMode` is set): The text is forcibly split.
        # 
        # The value must be in the range of [1, 6000]. Defaults to 500 if not specified.
        # 
        # For more information, see [knowledge base](https://help.aliyun.com/document_detail/2807740.html).
        # 
        # > If you specify a `ChunkSize` less than 100, you must also specify the `OverlapSize` parameter. You can also omit both parameters to use the system defaults.
        # 
        # 
        # 
        # <props="intl">
        # 
        # > This parameter is not available. Do not specify it.
        self.chunk_size = chunk_size
        # A list of file IDs.
        self.document_ids_shrink = document_ids_shrink
        # Specifies whether to include Excel file headers. If set to `true`, the knowledge base treats the first row of all .xlsx and .xls files as the header and automatically prepends it to each text chunk (data row). This prevents the large language model (LLM) from misinterpreting the header as a regular data row.
        # 
        # > Enable this parameter only if all imported documents are Excel files that contain a header.
        # 
        # Valid values:
        # 
        # - true: Enabled.
        # 
        # - false: Disabled.
        # 
        # Default value: false.
        self.enable_headers = enable_headers
        self.extra_shrink = extra_shrink
        # The knowledge base ID. This is the `Data.Id` returned by the **CreateIndex** API.
        # 
        # This parameter is required.
        self.index_id = index_id
        # <props="china">
        # 
        # Specifies the number of overlapping characters between adjacent text chunks. This setting applies only to the documents added in the current job. For more information, see [knowledge base](https://help.aliyun.com/document_detail/2807740.html). The value must be in the range of [0, 1024].
        # 
        # Defaults to 100 if not specified.
        # 
        # > The value of `OverlapSize` must be less than the value of `ChunkSize`. Otherwise, the chunking process may fail.
        # 
        # 
        # 
        # <props="intl">
        # 
        # > This parameter is not available. Do not specify it.
        self.overlap_size = overlap_size
        # <props="china">
        # 
        # The separator for chunking. This parameter is used only when `ChunkMode` is set to **regex**. You can specify a single regular expression (multiple expressions are not supported) to split the file into smaller text chunks. For more information, see [knowledge base](https://help.aliyun.com/document_detail/2807740.html).
        # 
        # When you use intelligent chunking (when `ChunkMode` is not specified), leave this parameter empty.
        # 
        # 
        # 
        # <props="intl">
        # 
        # > This parameter is not available. Do not specify it.
        self.separator = separator
        # The type of the data source. Valid values:
        # 
        # - DATA_CENTER_CATEGORY: Imports all documents from specified categories in <props="china">[application data](https://bailian.console.aliyun.com/?tab=app#/data-center)<props="intl">[application data](https://modelstudio.console.alibabacloud.com/?tab=app#/data-center). You can import documents from multiple categories.
        # 
        # - DATA_CENTER_FILE: Imports specified files from <props="china">[application data](https://bailian.console.aliyun.com/?tab=app#/data-center)<props="intl">[application data](https://modelstudio.console.alibabacloud.com/?tab=app#/data-center). You can import multiple files.
        # 
        # > If you set this parameter to `DATA_CENTER_CATEGORY`, you must specify the `CategoryIds` parameter. If you set this parameter to `DATA_CENTER_FILE`, you must specify the `DocumentIds` parameter.
        # 
        # This parameter is required.
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_ids_shrink is not None:
            result['CategoryIds'] = self.category_ids_shrink

        if self.chunk_mode is not None:
            result['ChunkMode'] = self.chunk_mode

        if self.chunk_size is not None:
            result['ChunkSize'] = self.chunk_size

        if self.document_ids_shrink is not None:
            result['DocumentIds'] = self.document_ids_shrink

        if self.enable_headers is not None:
            result['EnableHeaders'] = self.enable_headers

        if self.extra_shrink is not None:
            result['Extra'] = self.extra_shrink

        if self.index_id is not None:
            result['IndexId'] = self.index_id

        if self.overlap_size is not None:
            result['OverlapSize'] = self.overlap_size

        if self.separator is not None:
            result['Separator'] = self.separator

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryIds') is not None:
            self.category_ids_shrink = m.get('CategoryIds')

        if m.get('ChunkMode') is not None:
            self.chunk_mode = m.get('ChunkMode')

        if m.get('ChunkSize') is not None:
            self.chunk_size = m.get('ChunkSize')

        if m.get('DocumentIds') is not None:
            self.document_ids_shrink = m.get('DocumentIds')

        if m.get('EnableHeaders') is not None:
            self.enable_headers = m.get('EnableHeaders')

        if m.get('Extra') is not None:
            self.extra_shrink = m.get('Extra')

        if m.get('IndexId') is not None:
            self.index_id = m.get('IndexId')

        if m.get('OverlapSize') is not None:
            self.overlap_size = m.get('OverlapSize')

        if m.get('Separator') is not None:
            self.separator = m.get('Separator')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        return self

