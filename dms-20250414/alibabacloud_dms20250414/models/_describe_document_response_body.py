# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dms20250414 import models as main_models
from darabonba.model import DaraModel

class DescribeDocumentResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeDocumentResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details of the document.
        self.data = data
        # The error code returned when the request fails.
        self.error_code = error_code
        # The error message returned when the request fails.
        self.error_message = error_message
        # The unique request ID. Provide this ID for troubleshooting if an error occurs.
        self.request_id = request_id
        # Indicates whether the request succeeded. Valid values:
        # 
        # - **true**: The request succeeded.
        # 
        # - **false**: The request failed.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeDocumentResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeDocumentResponseBodyData(DaraModel):
    def __init__(
        self,
        description: str = None,
        docs_count: int = None,
        document_loader_name: str = None,
        file_ext: str = None,
        file_size: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        kb_uuid: str = None,
        keywords: str = None,
        name: str = None,
        state: int = None,
        summary: str = None,
        text_splitter_name: str = None,
    ):
        # The description of the document.
        self.description = description
        # The number of chunks.
        self.docs_count = docs_count
        # The name of the document loader.
        self.document_loader_name = document_loader_name
        # The file extension of the document.
        self.file_ext = file_ext
        # The size of the document in bytes.
        self.file_size = file_size
        # The creation time of the document, in UTC.
        self.gmt_create = gmt_create
        # The last modification time of the document, in UTC.
        self.gmt_modified = gmt_modified
        # The ID of the knowledge base.
        self.kb_uuid = kb_uuid
        # The keywords of the document.
        self.keywords = keywords
        # The name of the document.
        self.name = name
        # The document state. Possible values are:
        # 
        # - **0**: Parsing complete.
        # 
        # - **-1**: Not parsed.
        # 
        # - **-2**: Parsing in progress.
        # 
        # - **-3**: Parsing failed.
        # 
        # - **-4**: Parsing canceled.
        self.state = state
        # The summary of the document.
        self.summary = summary
        # The name of the text splitter.
        self.text_splitter_name = text_splitter_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.docs_count is not None:
            result['DocsCount'] = self.docs_count

        if self.document_loader_name is not None:
            result['DocumentLoaderName'] = self.document_loader_name

        if self.file_ext is not None:
            result['FileExt'] = self.file_ext

        if self.file_size is not None:
            result['FileSize'] = self.file_size

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.kb_uuid is not None:
            result['KbUuid'] = self.kb_uuid

        if self.keywords is not None:
            result['Keywords'] = self.keywords

        if self.name is not None:
            result['Name'] = self.name

        if self.state is not None:
            result['State'] = self.state

        if self.summary is not None:
            result['Summary'] = self.summary

        if self.text_splitter_name is not None:
            result['TextSplitterName'] = self.text_splitter_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DocsCount') is not None:
            self.docs_count = m.get('DocsCount')

        if m.get('DocumentLoaderName') is not None:
            self.document_loader_name = m.get('DocumentLoaderName')

        if m.get('FileExt') is not None:
            self.file_ext = m.get('FileExt')

        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('KbUuid') is not None:
            self.kb_uuid = m.get('KbUuid')

        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('TextSplitterName') is not None:
            self.text_splitter_name = m.get('TextSplitterName')

        return self

