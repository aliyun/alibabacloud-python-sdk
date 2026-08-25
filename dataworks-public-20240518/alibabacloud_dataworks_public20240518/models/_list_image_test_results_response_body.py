# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListImageTestResultsResponseBody(DaraModel):
    def __init__(
        self,
        paging_info: main_models.ListImageTestResultsResponseBodyPagingInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The pagination information.
        self.paging_info = paging_info
        # The request ID, which is used to locate logs and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.paging_info:
            self.paging_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.paging_info is not None:
            result['PagingInfo'] = self.paging_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PagingInfo') is not None:
            temp_model = main_models.ListImageTestResultsResponseBodyPagingInfo()
            self.paging_info = temp_model.from_map(m.get('PagingInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListImageTestResultsResponseBodyPagingInfo(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        test_result_list: List[main_models.ListImageTestResultsResponseBodyPagingInfoTestResultList] = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The list of image test results.
        self.test_result_list = test_result_list
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.test_result_list:
            for v1 in self.test_result_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['TestResultList'] = []
        if self.test_result_list is not None:
            for k1 in self.test_result_list:
                result['TestResultList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.test_result_list = []
        if m.get('TestResultList') is not None:
            for k1 in m.get('TestResultList'):
                temp_model = main_models.ListImageTestResultsResponseBodyPagingInfoTestResultList()
                self.test_result_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListImageTestResultsResponseBodyPagingInfoTestResultList(DaraModel):
    def __init__(
        self,
        image_id: str = None,
        message: str = None,
        operate_time: int = None,
        process_id: str = None,
        publish_stage: str = None,
        resource_group_id: int = None,
        status: str = None,
    ):
        # The image ID.
        self.image_id = image_id
        # The test result message.
        self.message = message
        # The operation time, represented as a 64-bit timestamp.
        self.operate_time = operate_time
        # The process ID.
        self.process_id = process_id
        # The publish stage of the image.
        self.publish_stage = publish_stage
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The status of the test process.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.message is not None:
            result['Message'] = self.message

        if self.operate_time is not None:
            result['OperateTime'] = self.operate_time

        if self.process_id is not None:
            result['ProcessId'] = self.process_id

        if self.publish_stage is not None:
            result['PublishStage'] = self.publish_stage

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('OperateTime') is not None:
            self.operate_time = m.get('OperateTime')

        if m.get('ProcessId') is not None:
            self.process_id = m.get('ProcessId')

        if m.get('PublishStage') is not None:
            self.publish_stage = m.get('PublishStage')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

