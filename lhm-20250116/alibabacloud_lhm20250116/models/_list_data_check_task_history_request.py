# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDataCheckTaskHistoryRequest(DaraModel):
    def __init__(
        self,
        batch_id: int = None,
        check_result: int = None,
        create_end_time: str = None,
        create_start_time: str = None,
        exec_end_time: str = None,
        exec_start_time: str = None,
        exec_status: int = None,
        finish_end_time: str = None,
        finish_start_time: str = None,
        page_index: int = None,
        page_size: int = None,
        task_id: int = None,
    ):
        # The ID of the validation job.
        # 
        # This parameter is required.
        self.batch_id = batch_id
        # Filters by validation result. Valid values:
        # 
        # - 0: No records.
        # - 1: Passed.
        # - 2: Failed.
        self.check_result = check_result
        # The end of the job creation time filter range. Format: YYYY-MM-DD HH:MM:SS.
        self.create_end_time = create_end_time
        # The start of the job creation time filter range. Format: YYYY-MM-DD HH:MM:SS.
        self.create_start_time = create_start_time
        # The end of the execution start time filter range. Format: YYYY-MM-DD HH:MM:SS.
        self.exec_end_time = exec_end_time
        # The start of the execution start time filter range. Format: YYYY-MM-DD HH:MM:SS.
        self.exec_start_time = exec_start_time
        # Filters by execution status. Valid values:
        # 
        # - 0: Pending.
        # - 1: Running.
        # - 2: Stopped.
        # - 3: Failed.
        # - 4: Completed.
        self.exec_status = exec_status
        # The end of the execution end time filter range. Format: YYYY-MM-DD HH:MM:SS.
        self.finish_end_time = finish_end_time
        # The start of the execution end time filter range. Format: YYYY-MM-DD HH:MM:SS.
        self.finish_start_time = finish_start_time
        # The page number of the page to return.
        self.page_index = page_index
        # The maximum number of entries to return per page.
        self.page_size = page_size
        # The ID of the data validation task.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_id is not None:
            result['batchId'] = self.batch_id

        if self.check_result is not None:
            result['checkResult'] = self.check_result

        if self.create_end_time is not None:
            result['createEndTime'] = self.create_end_time

        if self.create_start_time is not None:
            result['createStartTime'] = self.create_start_time

        if self.exec_end_time is not None:
            result['execEndTime'] = self.exec_end_time

        if self.exec_start_time is not None:
            result['execStartTime'] = self.exec_start_time

        if self.exec_status is not None:
            result['execStatus'] = self.exec_status

        if self.finish_end_time is not None:
            result['finishEndTime'] = self.finish_end_time

        if self.finish_start_time is not None:
            result['finishStartTime'] = self.finish_start_time

        if self.page_index is not None:
            result['pageIndex'] = self.page_index

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.task_id is not None:
            result['taskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('batchId') is not None:
            self.batch_id = m.get('batchId')

        if m.get('checkResult') is not None:
            self.check_result = m.get('checkResult')

        if m.get('createEndTime') is not None:
            self.create_end_time = m.get('createEndTime')

        if m.get('createStartTime') is not None:
            self.create_start_time = m.get('createStartTime')

        if m.get('execEndTime') is not None:
            self.exec_end_time = m.get('execEndTime')

        if m.get('execStartTime') is not None:
            self.exec_start_time = m.get('execStartTime')

        if m.get('execStatus') is not None:
            self.exec_status = m.get('execStatus')

        if m.get('finishEndTime') is not None:
            self.finish_end_time = m.get('finishEndTime')

        if m.get('finishStartTime') is not None:
            self.finish_start_time = m.get('finishStartTime')

        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        return self

