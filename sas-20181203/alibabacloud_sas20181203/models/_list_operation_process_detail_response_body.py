# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListOperationProcessDetailResponseBody(DaraModel):
    def __init__(
        self,
        page_info: main_models.ListOperationProcessDetailResponseBodyPageInfo = None,
        process_details: List[main_models.ListOperationProcessDetailResponseBodyProcessDetails] = None,
        request_id: str = None,
    ):
        # The pagination information.
        self.page_info = page_info
        # The information about the operation subtasks.
        self.process_details = process_details
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.process_details:
            for v1 in self.process_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        result['ProcessDetails'] = []
        if self.process_details is not None:
            for k1 in self.process_details:
                result['ProcessDetails'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = main_models.ListOperationProcessDetailResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        self.process_details = []
        if m.get('ProcessDetails') is not None:
            for k1 in m.get('ProcessDetails'):
                temp_model = main_models.ListOperationProcessDetailResponseBodyProcessDetails()
                self.process_details.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListOperationProcessDetailResponseBodyProcessDetails(DaraModel):
    def __init__(
        self,
        asset_sub_type: int = None,
        asset_type: int = None,
        asset_vendor: int = None,
        checks: List[main_models.ListOperationProcessDetailResponseBodyProcessDetailsChecks] = None,
        create_time: int = None,
        detail_task_id: str = None,
        end_time: int = None,
        start_time: int = None,
        status_code: int = None,
        task_id: str = None,
    ):
        # The subtype of the asset associated with the operation subtask.
        self.asset_sub_type = asset_sub_type
        # The type of the asset associated with the operation subtask.
        self.asset_type = asset_type
        # The vendor of the asset associated with the operation subtask.
        self.asset_vendor = asset_vendor
        # The check items associated with the operation subtask.
        self.checks = checks
        # The timestamp when the task was created. Unit: milliseconds.
        self.create_time = create_time
        # The ID of the operation subtask.
        self.detail_task_id = detail_task_id
        # The end timestamp of the operation subtask. Unit: milliseconds.
        self.end_time = end_time
        # The start timestamp of the operation subtask. Unit: milliseconds.
        self.start_time = start_time
        # The subtask status code. Enumerated values:
        # 
        # *   0: not started.
        # *   1: running.
        # *   2: successful.
        # *   3: times out.
        # *   4: failed.
        self.status_code = status_code
        # The ID of the operation subtask.
        self.task_id = task_id

    def validate(self):
        if self.checks:
            for v1 in self.checks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_sub_type is not None:
            result['AssetSubType'] = self.asset_sub_type

        if self.asset_type is not None:
            result['AssetType'] = self.asset_type

        if self.asset_vendor is not None:
            result['AssetVendor'] = self.asset_vendor

        result['Checks'] = []
        if self.checks is not None:
            for k1 in self.checks:
                result['Checks'].append(k1.to_map() if k1 else None)

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.detail_task_id is not None:
            result['DetailTaskId'] = self.detail_task_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status_code is not None:
            result['StatusCode'] = self.status_code

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetSubType') is not None:
            self.asset_sub_type = m.get('AssetSubType')

        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')

        if m.get('AssetVendor') is not None:
            self.asset_vendor = m.get('AssetVendor')

        self.checks = []
        if m.get('Checks') is not None:
            for k1 in m.get('Checks'):
                temp_model = main_models.ListOperationProcessDetailResponseBodyProcessDetailsChecks()
                self.checks.append(temp_model.from_map(k1))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DetailTaskId') is not None:
            self.detail_task_id = m.get('DetailTaskId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

class ListOperationProcessDetailResponseBodyProcessDetailsChecks(DaraModel):
    def __init__(
        self,
        check_id: int = None,
        check_show_name: str = None,
    ):
        # The ID of the check item associated with the operation subtask.
        self.check_id = check_id
        # The name of the check item associated with the operation subtask.
        self.check_show_name = check_show_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_id is not None:
            result['CheckId'] = self.check_id

        if self.check_show_name is not None:
            result['CheckShowName'] = self.check_show_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')

        if m.get('CheckShowName') is not None:
            self.check_show_name = m.get('CheckShowName')

        return self

class ListOperationProcessDetailResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of entries returned on the current page.
        self.count = count
        # The page number.
        self.current_page = current_page
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

