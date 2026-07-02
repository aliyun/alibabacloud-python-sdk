# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sddp20190103 import models as main_models
from darabonba.model import DaraModel

class DescribeDataMaskingTasksResponseBody(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        items: List[main_models.DescribeDataMaskingTasksResponseBodyItems] = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.current_page = current_page
        # A list of data masking tasks.
        self.items = items
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeDataMaskingTasksResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDataMaskingTasksResponseBodyItems(DaraModel):
    def __init__(
        self,
        dst_member_account: int = None,
        dst_path: str = None,
        dst_type: int = None,
        dst_type_code: str = None,
        gmt_create: int = None,
        has_unfinish_process: bool = None,
        id: int = None,
        original_table: bool = None,
        owner: str = None,
        run_count: int = None,
        src_member_account: int = None,
        src_path: str = None,
        src_type: int = None,
        src_type_code: str = None,
        status: int = None,
        task_id: str = None,
        task_name: str = None,
        trigger_type: int = None,
    ):
        # The member account that the data masking destination belongs to.
        self.dst_member_account = dst_member_account
        # The destination path.
        self.dst_path = dst_path
        # The product that the destination data source belongs to. Valid values:
        # 
        # - **1**: MaxCompute.
        # 
        # - **2**: OSS.
        # 
        # - **3**: ADS.
        # 
        # - **4**: OTS.
        # 
        # - **5**: RDS.
        # 
        # - **6**: SELF_DB.
        self.dst_type = dst_type
        # The type of the destination product. Valid values:
        # 
        # - **MaxCompute**.
        # 
        # - **OSS**.
        # 
        # - **ADS**.
        # 
        # - **OTS**.
        # 
        # - **RDS**.
        # 
        # - **SELF_DB**.
        self.dst_type_code = dst_type_code
        # The time when the task was created. The value is a UNIX timestamp. Unit: milliseconds.
        self.gmt_create = gmt_create
        # Indicates whether the task is running.
        self.has_unfinish_process = has_unfinish_process
        # The numerical ID of the task.
        self.id = id
        # Indicates whether the source table is masked.
        self.original_table = original_table
        # The creator of the task.
        self.owner = owner
        # The number of executions.
        self.run_count = run_count
        # The member account that the data masking source belongs to.
        self.src_member_account = src_member_account
        # The source path.
        self.src_path = src_path
        # The type of the source product. Valid values:
        # 
        # - **1**: MaxCompute.
        # 
        # - **2**: OSS.
        # 
        # - **3**: ADS.
        # 
        # - **4**: OTS.
        # 
        # - **5**: RDS.
        # 
        # - **6**: SELF_DB.
        self.src_type = src_type
        # The type of the source product. Valid values:
        # 
        # - **MaxCompute**.
        # 
        # - **OSS**.
        # 
        # - **ADS**.
        # 
        # - **OTS**.
        # 
        # - **RDS**.
        # 
        # - **SELF_DB**.
        self.src_type_code = src_type_code
        # The status of the task. Valid values:
        # 
        # - **0**: Disabled.
        # 
        # - **1**: Enabled.
        self.status = status
        # The string ID of the task.
        self.task_id = task_id
        # The name of the task.
        self.task_name = task_name
        # The execution method of the task. Valid values:
        # 
        # - **1**: Manual.
        # 
        # - **2**: Scheduled.
        # 
        # - **3**: Manual and scheduled.
        self.trigger_type = trigger_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dst_member_account is not None:
            result['DstMemberAccount'] = self.dst_member_account

        if self.dst_path is not None:
            result['DstPath'] = self.dst_path

        if self.dst_type is not None:
            result['DstType'] = self.dst_type

        if self.dst_type_code is not None:
            result['DstTypeCode'] = self.dst_type_code

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.has_unfinish_process is not None:
            result['HasUnfinishProcess'] = self.has_unfinish_process

        if self.id is not None:
            result['Id'] = self.id

        if self.original_table is not None:
            result['OriginalTable'] = self.original_table

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.run_count is not None:
            result['RunCount'] = self.run_count

        if self.src_member_account is not None:
            result['SrcMemberAccount'] = self.src_member_account

        if self.src_path is not None:
            result['SrcPath'] = self.src_path

        if self.src_type is not None:
            result['SrcType'] = self.src_type

        if self.src_type_code is not None:
            result['SrcTypeCode'] = self.src_type_code

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DstMemberAccount') is not None:
            self.dst_member_account = m.get('DstMemberAccount')

        if m.get('DstPath') is not None:
            self.dst_path = m.get('DstPath')

        if m.get('DstType') is not None:
            self.dst_type = m.get('DstType')

        if m.get('DstTypeCode') is not None:
            self.dst_type_code = m.get('DstTypeCode')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('HasUnfinishProcess') is not None:
            self.has_unfinish_process = m.get('HasUnfinishProcess')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('OriginalTable') is not None:
            self.original_table = m.get('OriginalTable')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('RunCount') is not None:
            self.run_count = m.get('RunCount')

        if m.get('SrcMemberAccount') is not None:
            self.src_member_account = m.get('SrcMemberAccount')

        if m.get('SrcPath') is not None:
            self.src_path = m.get('SrcPath')

        if m.get('SrcType') is not None:
            self.src_type = m.get('SrcType')

        if m.get('SrcTypeCode') is not None:
            self.src_type_code = m.get('SrcTypeCode')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')

        return self

