# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListBatchTasksResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        page_result: main_models.ListBatchTasksResponseBodyPageResult = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.page_result = page_result
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.page_result:
            self.page_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.page_result is not None:
            result['PageResult'] = self.page_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageResult') is not None:
            temp_model = main_models.ListBatchTasksResponseBodyPageResult()
            self.page_result = temp_model.from_map(m.get('PageResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListBatchTasksResponseBodyPageResult(DaraModel):
    def __init__(
        self,
        count: int = None,
        page: int = None,
        page_size: int = None,
        result_data: List[main_models.ListBatchTasksResponseBodyPageResultResultData] = None,
    ):
        self.count = count
        self.page = page
        self.page_size = page_size
        self.result_data = result_data

    def validate(self):
        if self.result_data:
            for v1 in self.result_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.page is not None:
            result['Page'] = self.page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['ResultData'] = []
        if self.result_data is not None:
            for k1 in self.result_data:
                result['ResultData'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.result_data = []
        if m.get('ResultData') is not None:
            for k1 in m.get('ResultData'):
                temp_model = main_models.ListBatchTasksResponseBodyPageResultResultData()
                self.result_data.append(temp_model.from_map(k1))

        return self

class ListBatchTasksResponseBodyPageResultResultData(DaraModel):
    def __init__(
        self,
        description: str = None,
        directory: str = None,
        file_id: int = None,
        last_submit_status: str = None,
        last_version: int = None,
        name: str = None,
        node_id: str = None,
        node_name: str = None,
        node_output_name_list: List[str] = None,
        node_type: int = None,
        operator_type: int = None,
        owner_name: str = None,
        owner_user_id: str = None,
        published: bool = None,
        released: bool = None,
        status: str = None,
    ):
        self.description = description
        self.directory = directory
        self.file_id = file_id
        self.last_submit_status = last_submit_status
        self.last_version = last_version
        self.name = name
        self.node_id = node_id
        self.node_name = node_name
        self.node_output_name_list = node_output_name_list
        self.node_type = node_type
        self.operator_type = operator_type
        self.owner_name = owner_name
        self.owner_user_id = owner_user_id
        self.published = published
        self.released = released
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.directory is not None:
            result['Directory'] = self.directory

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.last_submit_status is not None:
            result['LastSubmitStatus'] = self.last_submit_status

        if self.last_version is not None:
            result['LastVersion'] = self.last_version

        if self.name is not None:
            result['Name'] = self.name

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.node_output_name_list is not None:
            result['NodeOutputNameList'] = self.node_output_name_list

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.operator_type is not None:
            result['OperatorType'] = self.operator_type

        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name

        if self.owner_user_id is not None:
            result['OwnerUserId'] = self.owner_user_id

        if self.published is not None:
            result['Published'] = self.published

        if self.released is not None:
            result['Released'] = self.released

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Directory') is not None:
            self.directory = m.get('Directory')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('LastSubmitStatus') is not None:
            self.last_submit_status = m.get('LastSubmitStatus')

        if m.get('LastVersion') is not None:
            self.last_version = m.get('LastVersion')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('NodeOutputNameList') is not None:
            self.node_output_name_list = m.get('NodeOutputNameList')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')

        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')

        if m.get('OwnerUserId') is not None:
            self.owner_user_id = m.get('OwnerUserId')

        if m.get('Published') is not None:
            self.published = m.get('Published')

        if m.get('Released') is not None:
            self.released = m.get('Released')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

