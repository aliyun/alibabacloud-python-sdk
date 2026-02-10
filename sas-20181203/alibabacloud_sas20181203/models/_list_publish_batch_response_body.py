# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListPublishBatchResponseBody(DaraModel):
    def __init__(
        self,
        batch_list: List[main_models.ListPublishBatchResponseBodyBatchList] = None,
        page_info: main_models.ListPublishBatchResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # The information about the release batches.
        self.batch_list = batch_list
        # The page information.
        self.page_info = page_info
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.batch_list:
            for v1 in self.batch_list:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BatchList'] = []
        if self.batch_list is not None:
            for k1 in self.batch_list:
                result['BatchList'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.batch_list = []
        if m.get('BatchList') is not None:
            for k1 in m.get('BatchList'):
                temp_model = main_models.ListPublishBatchResponseBodyBatchList()
                self.batch_list.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.ListPublishBatchResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListPublishBatchResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The page number.
        self.current_page = current_page
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListPublishBatchResponseBodyBatchList(DaraModel):
    def __init__(
        self,
        batch_id: int = None,
        batch_interval: int = None,
        batch_name: str = None,
        batch_no: int = None,
        batch_process: int = None,
        batch_total: int = None,
        operation_base: int = None,
        status: int = None,
        version: str = None,
    ):
        # The ID of the release batch.
        self.batch_id = batch_id
        # The interval between two release batches. Unit: hours.
        self.batch_interval = batch_interval
        # The name of the release batch.
        self.batch_name = batch_name
        # The current batch number during a batch release.
        self.batch_no = batch_no
        # The progress of the release batch. This parameter indicates the number of servers that are upgraded in the release batch.
        self.batch_process = batch_process
        # The total number of batches.
        self.batch_total = batch_total
        # The asset selection dimension. Valid values:
        # 
        # *   **0**: instance.
        # *   **1**: machine group.
        # *   **2**: Virtual Private Cloud (VPC) ID.
        self.operation_base = operation_base
        # The publish status of the Security Center agent. Valid values:
        # 
        # *   **0**: not started.
        # *   **1**: publishing.
        # *   **2**: published.
        # *   **3**: publish suspended.
        # *   **4**: forcibly upgrading.
        self.status = status
        # The destination version of the Security Center agent.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_id is not None:
            result['BatchId'] = self.batch_id

        if self.batch_interval is not None:
            result['BatchInterval'] = self.batch_interval

        if self.batch_name is not None:
            result['BatchName'] = self.batch_name

        if self.batch_no is not None:
            result['BatchNo'] = self.batch_no

        if self.batch_process is not None:
            result['BatchProcess'] = self.batch_process

        if self.batch_total is not None:
            result['BatchTotal'] = self.batch_total

        if self.operation_base is not None:
            result['OperationBase'] = self.operation_base

        if self.status is not None:
            result['Status'] = self.status

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')

        if m.get('BatchInterval') is not None:
            self.batch_interval = m.get('BatchInterval')

        if m.get('BatchName') is not None:
            self.batch_name = m.get('BatchName')

        if m.get('BatchNo') is not None:
            self.batch_no = m.get('BatchNo')

        if m.get('BatchProcess') is not None:
            self.batch_process = m.get('BatchProcess')

        if m.get('BatchTotal') is not None:
            self.batch_total = m.get('BatchTotal')

        if m.get('OperationBase') is not None:
            self.operation_base = m.get('OperationBase')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

