# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListRtcMPUTaskDetailRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        page_no: int = None,
        page_size: int = None,
        task_id: str = None,
    ):
        # The application ID.
        # > The application ID consists of uppercase and lowercase letters, digits, underscores, and hyphens (-), with a maximum of 64 characters.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The page number.
        # > If you do not specify a task ID, you must specify the PageSize and PageNo parameters. In this case, the paged query results of all stream mixing and relaying tasks under the specified application ID are returned.
        self.page_no = page_no
        # The number of records per page. Valid values: 1 to 100.
        # > If you do not specify a task ID, you must specify the PageSize and PageNo parameters. In this case, the paged query results of all stream mixing and relaying tasks under the specified application ID are returned.
        self.page_size = page_size
        # The task ID.
        # 
        # 
        # >- The task ID consists of uppercase and lowercase letters, digits, underscores, and hyphens (-), with a maximum of 55 characters.
        # - If you specify a task ID, the query is performed based on the task ID first, and the result contains the parameter details of the stream mixing and relaying task with the specified task ID.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

