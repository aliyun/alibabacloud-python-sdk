# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTaskFlowInstanceRequest(DaraModel):
    def __init__(
        self,
        dag_id: int = None,
        page_index: int = None,
        page_size: int = None,
        start_time_begin: str = None,
        start_time_end: str = None,
        status: int = None,
        tid: int = None,
        trigger_type: int = None,
        use_biz_date: bool = None,
    ):
        # The ID of the task flow. You can call the [ListTaskFlow](https://help.aliyun.com/document_detail/424565.html) or [ListLhTaskFlowAndScenario](https://help.aliyun.com/document_detail/426672.html) operation to obtain the ID of the task flow.
        # 
        # This parameter is required.
        self.dag_id = dag_id
        # The number of the page to return.
        # 
        # This parameter is required.
        self.page_index = page_index
        # The number of entries to return on each page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The beginning of the time range to query the execution records of the task flow. Specify the time in the yyyy-MM-DD format.
        self.start_time_begin = start_time_begin
        # The end of the time range to query the execution records of the task flow. Specify the time in the yyyy-MM-DD format.
        self.start_time_end = start_time_end
        # The running status of the task node. Valid values:
        # 
        # - **0**: Waiting for scheduling
        # 
        # - **1**: Running
        # 
        # - **2**: Suspend
        # 
        # - **3**: Failed to run
        # 
        # - **4**: Run successfully
        # 
        # - **5**: Completed
        self.status = status
        # The ID of the tenant. You can call the [GetUserActiveTenant](https://help.aliyun.com/document_detail/198073.html) or [ListUserTenants](https://help.aliyun.com/document_detail/198074.html) operation to obtain the tenant ID.
        self.tid = tid
        # The mode in which the task flow is triggered. Valid values:
        # 
        # *   **0**: The task flow is automatically triggered based on periodic scheduling.
        # *   **1**: The task flow is manually triggered.
        self.trigger_type = trigger_type
        # Adjust filter conditions:
        # 
        # - true: StartTimeBegin and StartTimeEnd are the time range for filtering services.
        # 
        # - false: StartTimeBegin and StartTimeEnd are the time range for the task to run.
        self.use_biz_date = use_biz_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dag_id is not None:
            result['DagId'] = self.dag_id

        if self.page_index is not None:
            result['PageIndex'] = self.page_index

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_time_begin is not None:
            result['StartTimeBegin'] = self.start_time_begin

        if self.start_time_end is not None:
            result['StartTimeEnd'] = self.start_time_end

        if self.status is not None:
            result['Status'] = self.status

        if self.tid is not None:
            result['Tid'] = self.tid

        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type

        if self.use_biz_date is not None:
            result['UseBizDate'] = self.use_biz_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DagId') is not None:
            self.dag_id = m.get('DagId')

        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartTimeBegin') is not None:
            self.start_time_begin = m.get('StartTimeBegin')

        if m.get('StartTimeEnd') is not None:
            self.start_time_end = m.get('StartTimeEnd')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')

        if m.get('UseBizDate') is not None:
            self.use_biz_date = m.get('UseBizDate')

        return self

