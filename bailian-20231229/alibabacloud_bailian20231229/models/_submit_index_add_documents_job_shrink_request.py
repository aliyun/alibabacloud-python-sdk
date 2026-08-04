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
        # The list of category IDs.
        self.category_ids_shrink = category_ids_shrink
        # <props="china">
        # Enables custom chunking (applies only to files appended in this request). For more information, see [Knowledge base](https://help.aliyun.com/document_detail/2807740.html). Valid values (only one value can be specified at a time):
        # 
        # - **length**: chunk by length. Strictly chunks according to the specified `ChunkSize` and `OverlapSize`. If these two parameters are not specified, the system uses default values (`ChunkSize` of 500 and `OverlapSize` of 100). Chunking by length does not support `Separator` (even if specified, it does not take effect).
        # - **page**: chunk by page. If `ChunkSize` is specified, it is also considered during chunking (if not specified, the default value of 500 is used). Chunking by page does not support `OverlapSize` or `Separator` (even if specified, they do not take effect).
        # - **h1**~**h5**: chunk by headings at the corresponding level (`h1` is the first-level heading, and so on, with support up to `h5` fifth-level heading). If `ChunkSize` is specified, it is also considered during chunking (if not specified, the default value of 500 is used). Chunking by heading does not support `OverlapSize` or `Separator` (even if specified, they do not take effect).
        # - **regex**: chunk by regular expression. The `Separator` parameter must be specified. If `ChunkSize` is specified, it is also considered during chunking (if not specified, the default value of 500 is used). Chunking by regex does not support `OverlapSize` (even if specified, it does not take effect).
        # 
        # Default value: empty, which uses intelligent chunking.
        # 
        # 
        # 
        # 
        # <props="intl">
        # 
        # > This parameter is not yet available. Do not specify this parameter.
        self.chunk_mode = chunk_mode
        # <props="china">
        # The chunk length, which is the maximum number of characters per text chunk (applies only to files appended in this request). When this length is exceeded:
        # 
        # - **Intelligent chunking** (without specifying `chunkMode`): the text is likely to be truncated.
        # - **Custom chunking** (with `chunkMode` specified): the text is forcibly split.
        # 
        # Valid values: 1 to 6000. If this parameter is not specified, the default value of 500 is used.
        # 
        # For more information, see [Knowledge base](https://help.aliyun.com/document_detail/2807740.html).
        # 
        # > If you specify `ChunkSize` with a value less than 100, you must also specify `OverlapSize`. You can also leave both parameters unspecified (the system uses default values).
        # 
        # 
        # 
        # <props="intl">
        # 
        # > This parameter is not yet available. Do not specify this parameter.
        self.chunk_size = chunk_size
        # The list of file IDs.
        self.document_ids_shrink = document_ids_shrink
        # Specifies whether to enable header assembly for Excel files. When enabled, the knowledge base treats the first row of all xlsx and xls files as headers and automatically appends them to each text chunk (data row), preventing the large language model from treating headers as regular data rows.
        # 
        # 
        # > Enable this feature only when all imported files are in xlsx or xls format and contain headers. Otherwise, leave it disabled.
        # >
        # 
        # Valid values:
        # - true: Enabled.
        # - false: Disabled.
        # 
        # Default value: false.
        self.enable_headers = enable_headers
        self.extra_shrink = extra_shrink
        # The knowledge base ID, which is the `Data.Id` returned by the **CreateIndex** operation.
        # 
        # This parameter is required.
        self.index_id = index_id
        # <props="china">
        # The chunk overlap length (applies only to files appended in this request). It indicates the number of overlapping characters between the current text chunk and the previous text chunk. For more information, see [Knowledge base](https://help.aliyun.com/document_detail/2807740.html). Valid values: 0 to 1024.
        # 
        # If this parameter is not specified, the default value of 100 is used.
        # > The value of `OverlapSize` must be less than the value of `ChunkSize`. Otherwise, chunking exceptions may occur.
        # 
        # 
        # 
        # <props="intl">
        # 
        # > This parameter is not yet available. Do not specify this parameter.
        self.overlap_size = overlap_size
        # <props="china">
        # The sentence separator, which takes effect only when `chunkMode` is set to **regex** (otherwise, it does not take effect even if specified). You can specify a regular expression (only one is supported) to split the file into small text chunks. For more information, see [Knowledge base](https://help.aliyun.com/document_detail/2807740.html).
        # 
        # When using intelligent chunking (without specifying `chunkMode`), keep the default empty value.
        # 
        # 
        # 
        # <props="intl">
        # 
        # > This parameter is not yet available. Do not specify this parameter.
        self.separator = separator
        # The data source type. Valid values:
        # - DATA_CENTER_CATEGORY: category type. Imports all documents under specified categories in <props="china">[Application Data](https://bailian.console.aliyun.com/?tab=app#/data-center)<props="intl">[Application Data](https://modelstudio.console.alibabacloud.com/?tab=app#/data-center). Multiple categories are supported.
        # - DATA_CENTER_FILE: document type. Imports specified files from <props="china">[Application Data](https://bailian.console.aliyun.com/?tab=app#/data-center)<props="intl">[Application Data](https://modelstudio.console.alibabacloud.com/?tab=app#/data-center). Multiple files are supported.
        # 
        # > If this parameter is set to DATA_CENTER_CATEGORY, you must specify the `CategoryIds` parameter. If this parameter is set to DATA_CENTER_FILE, you must specify the `DocumentIds` parameter.
        # >
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

