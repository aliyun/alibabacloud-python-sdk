# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDataCheckTaskListRequest(DaraModel):
    def __init__(
        self,
        check_result: int = None,
        check_type: int = None,
        create_end_time: str = None,
        create_start_time: str = None,
        exec_status: int = None,
        is_scheduled: int = None,
        page_index: int = None,
        page_size: int = None,
        task_name: str = None,
        template_name: str = None,
        update_end_time: str = None,
        update_start_time: str = None,
    ):
        # The validation result filter. Valid values:
        # 
        # - 0: no record.
        # - 1: passed.
        # - 2: failed.
        self.check_result = check_result
        # The validation type filter. Valid values:
        # 
        # - 0: row count comparison.
        # - 1: metric comparison.
        # - 2: weak content comparison.
        self.check_type = check_type
        # The end of the creation time range. Format: YYYY-MM-DD HH:MM:SS.
        self.create_end_time = create_end_time
        # The start of the creation time range. Format: YYYY-MM-DD HH:MM:SS.
        self.create_start_time = create_start_time
        # The execution status filter. Valid values:
        # 
        # - 0: pending.
        # - 1: running.
        # - 2: stopped.
        # - 3: failed.
        # - 4: completed.
        self.exec_status = exec_status
        # Specifies whether scheduling is enabled. Valid values:
        # 
        # - 0: disabled.
        # - 1: enabled.
        self.is_scheduled = is_scheduled
        # The page number. Default value: 1.
        self.page_index = page_index
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The task name. Fuzzy match is supported.
        self.task_name = task_name
        # The validation template name. Fuzzy match is supported. The server automatically converts the name into a list of template IDs for filtering.
        self.template_name = template_name
        # The end of the update time range. Format: YYYY-MM-DD HH:MM:SS.
        self.update_end_time = update_end_time
        # The start of the update time range. Format: YYYY-MM-DD HH:MM:SS.
        self.update_start_time = update_start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_result is not None:
            result['checkResult'] = self.check_result

        if self.check_type is not None:
            result['checkType'] = self.check_type

        if self.create_end_time is not None:
            result['createEndTime'] = self.create_end_time

        if self.create_start_time is not None:
            result['createStartTime'] = self.create_start_time

        if self.exec_status is not None:
            result['execStatus'] = self.exec_status

        if self.is_scheduled is not None:
            result['isScheduled'] = self.is_scheduled

        if self.page_index is not None:
            result['pageIndex'] = self.page_index

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.task_name is not None:
            result['taskName'] = self.task_name

        if self.template_name is not None:
            result['templateName'] = self.template_name

        if self.update_end_time is not None:
            result['updateEndTime'] = self.update_end_time

        if self.update_start_time is not None:
            result['updateStartTime'] = self.update_start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('checkResult') is not None:
            self.check_result = m.get('checkResult')

        if m.get('checkType') is not None:
            self.check_type = m.get('checkType')

        if m.get('createEndTime') is not None:
            self.create_end_time = m.get('createEndTime')

        if m.get('createStartTime') is not None:
            self.create_start_time = m.get('createStartTime')

        if m.get('execStatus') is not None:
            self.exec_status = m.get('execStatus')

        if m.get('isScheduled') is not None:
            self.is_scheduled = m.get('isScheduled')

        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('taskName') is not None:
            self.task_name = m.get('taskName')

        if m.get('templateName') is not None:
            self.template_name = m.get('templateName')

        if m.get('updateEndTime') is not None:
            self.update_end_time = m.get('updateEndTime')

        if m.get('updateStartTime') is not None:
            self.update_start_time = m.get('updateStartTime')

        return self

