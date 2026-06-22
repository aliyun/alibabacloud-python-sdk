# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCycleTaskListRequest(DaraModel):
    def __init__(
        self,
        config_id: str = None,
        current_page: int = None,
        page_size: int = None,
        task_name: str = None,
        task_type: str = None,
    ):
        # The ID of the configuration.
        # >Call the [CreateCycleTask](~~CreateCycleTask~~) operation to obtain this parameter.
        self.config_id = config_id
        # The page number of the current page when using paging.
        self.current_page = current_page
        # The maximum number of entries per page when using paging. Default value: 20.
        self.page_size = page_size
        # The node name. Valid values:
        # - **VIRUS_VUL_SCHEDULE_SCAN**: virus scan.
        # - **IMAGE_SCAN**: image scan.
        # - **EMG_VUL_SCHEDULE_SCAN**: emergency vulnerability scanning.
        self.task_name = task_name
        # The node type. Valid values:
        # - **VIRUS_VUL_SCHEDULE_SCAN**: virus scan.
        # - **IMAGE_SCAN**: image scan.
        # - **EMG_VUL_SCHEDULE_SCAN**: emergency vulnerability scanning.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

