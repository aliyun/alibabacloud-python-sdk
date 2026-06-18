# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bailian20231229 import models as main_models
from darabonba.model import DaraModel

class ListFileResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListFileResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        # The error code.
        self.code = code
        # The data field returned by the operation.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The status code returned by the operation.
        self.status = status
        # Indicates whether the operation was successful. Valid values:
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
            temp_model = main_models.ListFileResponseBodyData()
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

class ListFileResponseBodyData(DaraModel):
    def __init__(
        self,
        file_list: List[main_models.ListFileResponseBodyDataFileList] = None,
        has_next: bool = None,
        max_results: int = None,
        next_token: str = None,
        total_count: int = None,
    ):
        # The list of files in the category.
        self.file_list = file_list
        # Indicates whether there is a next page of category data that matches the query conditions. Valid values:
        # - true: Yes.
        # - false: No.
        self.has_next = has_next
        # The number of entries per page for paging.
        self.max_results = max_results
        # The pagination token returned by this call.
        self.next_token = next_token
        # The total number of entries in the returned results.
        self.total_count = total_count

    def validate(self):
        if self.file_list:
            for v1 in self.file_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FileList'] = []
        if self.file_list is not None:
            for k1 in self.file_list:
                result['FileList'].append(k1.to_map() if k1 else None)

        if self.has_next is not None:
            result['HasNext'] = self.has_next

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.file_list = []
        if m.get('FileList') is not None:
            for k1 in m.get('FileList'):
                temp_model = main_models.ListFileResponseBodyDataFileList()
                self.file_list.append(temp_model.from_map(k1))

        if m.get('HasNext') is not None:
            self.has_next = m.get('HasNext')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListFileResponseBodyDataFileList(DaraModel):
    def __init__(
        self,
        category_id: str = None,
        create_time: str = None,
        file_id: str = None,
        file_name: str = None,
        file_type: str = None,
        parse_error_message: str = None,
        parser: str = None,
        size_in_bytes: int = None,
        status: str = None,
        tags: List[str] = None,
    ):
        # The ID of the category to which the file belongs.
        self.category_id = category_id
        # The timestamp when the file was added to Alibaba Cloud Model Studio. Format: yyyy-MM-dd HH:mm:ss. Time zone: UTC+8.
        self.create_time = create_time
        # The file ID, which is the `FileId` returned by the **AddFile** operation. You can also obtain it on the <props="china">[Application Data](https://bailian.console.aliyun.com/?tab=app#/data-center)<props="intl">[Application Data](https://modelstudio.console.alibabacloud.com/?tab=app#/data-center) page by clicking the icon next to the file name.
        self.file_id = file_id
        # The file name.
        self.file_name = file_name
        # The file format type. Valid values: pdf, docx, doc, txt, md, pptx, ppt, xlsx, xls, html, png, jpg, jpeg, bmp, and gif.
        self.file_type = file_type
        self.parse_error_message = parse_error_message
        # The document parser. Valid values:
        # - DASHSCOPE_DOCMIND: Alibaba Cloud intelligent document parsing.
        self.parser = parser
        # The file size in bytes.
        self.size_in_bytes = size_in_bytes
        # The file parsing status. Valid values:
        # - INIT: Initialization state, waiting to be scheduled.
        # - PARSING: Parsing in progress.
        # - PARSE_SUCCESS: Parsing completed.
        # - PARSE_FAILED: Parsing failed.
        self.status = status
        # The list of tags associated with the file. A document can be associated with multiple tags.
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

        if m.get('Parser') is not None:
            self.parser = m.get('Parser')

        if m.get('SizeInBytes') is not None:
            self.size_in_bytes = m.get('SizeInBytes')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        return self

