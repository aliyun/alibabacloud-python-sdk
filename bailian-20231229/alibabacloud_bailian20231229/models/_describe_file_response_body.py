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
        # The status code.
        self.code = code
        # The returned data fields.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The HTTP status code.
        self.status = status
        # Indications whether the API call is successful. Valid values:
        # 
        # *   true
        # *   false
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
        parser: str = None,
        size_in_bytes: int = None,
        status: str = None,
        tags: List[str] = None,
    ):
        # The ID of the category to which the document belongs.
        self.category_id = category_id
        # The timestamp when the document was uploaded to Model Studio. Format: yyyy-MM-dd HH:mm:ss. Time zone: UTC + 8.
        self.create_time = create_time
        # The primary key ID of the document.
        self.file_id = file_id
        # The name of the document.
        self.file_name = file_name
        # The file type of the document. The value is an extension. Valid values: pdf, docx, doc, txt, md, pptx, and ppt.
        self.file_type = file_type
        # The parser that is used to parse the document. Valid value:
        # 
        # *   DASHSCOPE_DOCMIND: The default document parser.
        self.parser = parser
        # The size of the document. Unit: bytes.
        self.size_in_bytes = size_in_bytes
        # The status of the document. Valid values:
        # 
        # *   INIT: pending parsing.
        # *   PARSING
        # *   PARSE_SUCCESS
        # *   PARSE_FAILED
        self.status = status
        # The tags that are associated with the document. A document can be associated with multiple tags.
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

        if m.get('Parser') is not None:
            self.parser = m.get('Parser')

        if m.get('SizeInBytes') is not None:
            self.size_in_bytes = m.get('SizeInBytes')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        return self

