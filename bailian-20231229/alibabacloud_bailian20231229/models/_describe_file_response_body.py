# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bailian20231229 import models as main_models
from darabonba.model import DaraModel

class DescribeFileResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeFileResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        # The error status code.
        self.code = code
        # The data field of the operation.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The status code returned by the operation.
        self.status = status
        # Indicates whether the call was successful. Valid values:
        # - true: Successful.
        # - false: Failed.
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
            temp_model = main_models.DescribeFileResponseBodyData()
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

class DescribeFileResponseBodyData(DaraModel):
    def __init__(
        self,
        category_id: str = None,
        create_time: str = None,
        file_id: str = None,
        file_name: str = None,
        file_type: str = None,
        parse_error_message: str = None,
        parse_result_download_url: str = None,
        parser: str = None,
        size_in_bytes: int = None,
        status: str = None,
        tags: List[str] = None,
    ):
        # The ID of the category to which the file belongs.
        self.category_id = category_id
        # The timestamp when the file was added to Model Studio. Format: yyyy-MM-dd HH:mm:ss. Time zone: UTC+8.
        self.create_time = create_time
        # The file ID.
        self.file_id = file_id
        # The file name.
        self.file_name = file_name
        # The file type (extension). Valid values: pdf, docx, doc, txt, md, pptx, ppt, xlsx, xls, html, png, jpg, jpeg, bmp, and gif.
        self.file_type = file_type
        self.parse_error_message = parse_error_message
        self.parse_result_download_url = parse_result_download_url
        # The parser type used to parse the file. Valid values:
        # - DASHSCOPE_DOCMIND: the default document parser.
        self.parser = parser
        # The file size, in bytes.
        self.size_in_bytes = size_in_bytes
        # <props="china">
        # 
        # For files used in document-based knowledge bases (type: UNSTRUCTURED), valid values:
        # 
        # 
        # 
        # <props="intl">
        # 
        # For files used in unstructured knowledge bases (type: UNSTRUCTURED), valid values:
        # 
        # 
        # 
        # 
        # - INIT: pending parsing.
        # - IN_PARSE_QUEUE: queued for parsing.
        # - PARSING: being parsed.
        # - PARSE_SUCCESS: parsing completed.
        # <note>The document can be imported into a knowledge base only after the status changes to PARSE_SUCCESS.</note>
        # - PARSE_FAILED: parsing failed.
        # 
        # <props="china">
        # For files used in agent application [session interaction](https://www.alibabacloud.com/help/en/model-studio/user-guide/file-interaction) (type: SESSION_FILE), valid values:
        # 
        # - INIT: pending parsing.
        # - IN_PARSE_QUEUE: queued for parsing.
        # - PARSING: being parsed.
        # - PARSE_SUCCESS: parsing completed.
        # - PARSE_FAILED: parsing failed.
        # - SAFE_CHECKING: security check in progress.
        # - SAFE_CHECK_FAILED: security check failed.
        # - INDEX_BUILDING: index being built.
        # - INDEX_BUILD_SUCCESS: index built.
        # - INDEX_BUILDING_FAILED: index building failed.
        # - INDEX_DELETED: file index deleted.
        # - FILE_IS_READY: file is ready.
        # <note>Q&A can proceed only after the status changes to FILE_IS_READY.</note>
        # - FILE_EXPIRED: file expired.
        # <note>The file is valid only for the current user session. After the user closes the session, the file expires (maximum validity period: 7 days). Long-term retention is not supported.</note>
        # .
        self.status = status
        # The list of tags associated with the file. A file can be associated with multiple tags.
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_type is not None:
            result['FileType'] = self.file_type

        if self.parse_error_message is not None:
            result['ParseErrorMessage'] = self.parse_error_message

        if self.parse_result_download_url is not None:
            result['ParseResultDownloadUrl'] = self.parse_result_download_url

        if self.parser is not None:
            result['Parser'] = self.parser

        if self.size_in_bytes is not None:
            result['SizeInBytes'] = self.size_in_bytes

        if self.status is not None:
            result['Status'] = self.status

        if self.tags is not None:
            result['Tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')

        if m.get('ParseErrorMessage') is not None:
            self.parse_error_message = m.get('ParseErrorMessage')

        if m.get('ParseResultDownloadUrl') is not None:
            self.parse_result_download_url = m.get('ParseResultDownloadUrl')

        if m.get('Parser') is not None:
            self.parser = m.get('Parser')

        if m.get('SizeInBytes') is not None:
            self.size_in_bytes = m.get('SizeInBytes')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        return self

