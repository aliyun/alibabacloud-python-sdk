# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeSyncAssetTaskLogDetailResponseBody(DaraModel):
    def __init__(
        self,
        page_info: main_models.DescribeSyncAssetTaskLogDetailResponseBodyPageInfo = None,
        request_id: str = None,
        task_record_details: List[main_models.DescribeSyncAssetTaskLogDetailResponseBodyTaskRecordDetails] = None,
    ):
        # The pagination information.
        self.page_info = page_info
        # The request ID.
        self.request_id = request_id
        # The details of the tasks.
        self.task_record_details = task_record_details

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.task_record_details:
            for v1 in self.task_record_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['TaskRecordDetails'] = []
        if self.task_record_details is not None:
            for k1 in self.task_record_details:
                result['TaskRecordDetails'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = main_models.DescribeSyncAssetTaskLogDetailResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.task_record_details = []
        if m.get('TaskRecordDetails') is not None:
            for k1 in m.get('TaskRecordDetails'):
                temp_model = main_models.DescribeSyncAssetTaskLogDetailResponseBodyTaskRecordDetails()
                self.task_record_details.append(temp_model.from_map(k1))

        return self

class DescribeSyncAssetTaskLogDetailResponseBodyTaskRecordDetails(DaraModel):
    def __init__(
        self,
        asset_count: int = None,
        idc_region: str = None,
        leaf_task_id: str = None,
        leaf_task_status: str = None,
        task_msg: str = None,
        task_report_time: int = None,
        unprotected_asset_count: int = None,
    ):
        # The total number of assets.
        self.asset_count = asset_count
        # The region of the server in the data center.
        self.idc_region = idc_region
        # The ID of the task.
        self.leaf_task_id = leaf_task_id
        # The status of the task. Valid values:
        # 
        # *   **INIT**: The task is not started.
        # *   **START**: The task is started.
        # *   **MESSAGE_SEND**: The command is sent.
        # *   **SUCCESS**: The task is complete.
        # *   **FAIL**: The task failed.
        # *   **TIMEOUT**: The task timed out.
        self.leaf_task_status = leaf_task_status
        # The description of the task.
        self.task_msg = task_msg
        # The timestamp when the task results were reported.
        self.task_report_time = task_report_time
        # The number of unprotected assets.
        self.unprotected_asset_count = unprotected_asset_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_count is not None:
            result['AssetCount'] = self.asset_count

        if self.idc_region is not None:
            result['IdcRegion'] = self.idc_region

        if self.leaf_task_id is not None:
            result['LeafTaskId'] = self.leaf_task_id

        if self.leaf_task_status is not None:
            result['LeafTaskStatus'] = self.leaf_task_status

        if self.task_msg is not None:
            result['TaskMsg'] = self.task_msg

        if self.task_report_time is not None:
            result['TaskReportTime'] = self.task_report_time

        if self.unprotected_asset_count is not None:
            result['UnprotectedAssetCount'] = self.unprotected_asset_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetCount') is not None:
            self.asset_count = m.get('AssetCount')

        if m.get('IdcRegion') is not None:
            self.idc_region = m.get('IdcRegion')

        if m.get('LeafTaskId') is not None:
            self.leaf_task_id = m.get('LeafTaskId')

        if m.get('LeafTaskStatus') is not None:
            self.leaf_task_status = m.get('LeafTaskStatus')

        if m.get('TaskMsg') is not None:
            self.task_msg = m.get('TaskMsg')

        if m.get('TaskReportTime') is not None:
            self.task_report_time = m.get('TaskReportTime')

        if m.get('UnprotectedAssetCount') is not None:
            self.unprotected_asset_count = m.get('UnprotectedAssetCount')

        return self

class DescribeSyncAssetTaskLogDetailResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of entries on the current page.
        self.count = count
        # The page number.
        self.current_page = current_page
        # The number of entries per page. Default value: 20. If you leave this parameter empty, 20 entries are returned on each page.
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

