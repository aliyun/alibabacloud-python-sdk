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
        # The error code.
        self.code = code
        # The business data field.
        self.data = data
        # The error message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # The status code returned.
        self.status = status
        # Indicates whether the operation was successful. Valid values:
        # - true: The operation was successful.
        # - false: The operation failed.
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
        origin_file_download_url: str = None,
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
        # The ID of the file.
        self.file_id = file_id
        # The name of the file.
        self.file_name = file_name
        # The file type, which is the file extension. Valid values: pdf, docx, doc, txt, md, pptx, ppt, xlsx, xls, html, png, jpg, jpeg, bmp, and gif.
        self.file_type = file_type
        # The download URL of the source file.
        self.origin_file_download_url = origin_file_download_url
        # The cause of the parsing failure.
        self.parse_error_message = parse_error_message
        # The download URL of the file parsing result.
        self.parse_result_download_url = parse_result_download_url
        # The type of the parser used to parse the file. Valid values:
        # - DASHSCOPE_DOCMIND: the default document parser.
        self.parser = parser
        # The size of the file, in bytes.
        self.size_in_bytes = size_in_bytes
        # <props="china">
        # 
        # The status of a file used for a document knowledge base (type: UNSTRUCTURED). Valid values:
        # 
        # 
        # 
        # <props="intl">
        # 
        # The status of a file used for an unstructured knowledge base (type: UNSTRUCTURED). Valid values:
        # 
        # 
        # 
        # 
        # - INIT: to be parsed.
        # - IN_PARSE_QUEUE: queuing for parsing.
        # - PARSING: parsing.
        # - PARSE_SUCCESS: parsed.
        # <note>You can import a document into a knowledge base only after its status changes to PARSE_SUCCESS.</note>
        # - PARSE_FAILED: parsing failed.
        # 
        # <props="china">
        # The status of a file used for [session interaction](https://www.alibabacloud.com/help/en/model-studio/user-guide/file-interaction) in an agent application (type: SESSION_FILE). Valid values:
        # 
        # - INIT: to be parsed.
        # - IN_PARSE_QUEUE: queuing for parsing.
        # - PARSING: parsing.
        # - PARSE_SUCCESS: parsed.
        # - PARSE_FAILED: parsing failed.
        # - SAFE_CHECKING: undergoing security check.
        # - SAFE_CHECK_FAILED: security check failed.
        # - INDEX_BUILDING: building index.
        # - INDEX_BUILD_SUCCESS: index built.
        # - INDEX_BUILDING_FAILED: index building failed.
        # - INDEX_DELETED: file index deleted.
        # - FILE_IS_READY: file ready.
        # <note>You can perform Q&A only after the status changes to FILE_IS_READY.</note>
        # - FILE_EXPIRED: file expired.
        # <note>The file is valid only for the current session of the user. After the user closes the session, the file expires. The maximum validity period is 7 days. Long-term storage is not supported.</note>
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

        if self.origin_file_download_url is not None:
            result['OriginFileDownloadUrl'] = self.origin_file_download_url

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

        if m.get('OriginFileDownloadUrl') is not None:
            self.origin_file_download_url = m.get('OriginFileDownloadUrl')

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

