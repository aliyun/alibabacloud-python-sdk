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
        self.code = code
        # The returned data.
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.status = status
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
        # The list of documents in the category.
        self.file_list = file_list
        self.has_next = has_next
        self.max_results = max_results
        self.next_token = next_token
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
        parser: str = None,
        size_in_bytes: int = None,
        status: str = None,
        tags: List[str] = None,
    ):
        self.category_id = category_id
        self.create_time = create_time
        # The document ID, which is the `FileId` parameter returned by the [AddFile](~~AddFile~~) operation. To view the ID, click the icon next to the file name on the [Data Management](https://bailian.console.alibabacloud.com/#/data-center) page.
        self.file_id = file_id
        self.file_name = file_name
        self.file_type = file_type
        self.parser = parser
        self.size_in_bytes = size_in_bytes
        self.status = status
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

