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
        # The ID of the application.
        # 
        # >  The ID can be up to 64 characters in length and can contain letters, digits, underscores (_), and hyphens (-).
        # 
        # This parameter is required.
        self.app_id = app_id
        # The page number.
        self.page_no = page_no
        # The number of entries per page. Valid values: 1 to 100.
        # 
        # >  If you do not specify TaskId, you must specify PageSize and PageNo. Then, the parameters of all stream relay tasks for the specified application are returned in pages.
        self.page_size = page_size
        # The task ID.
        # 
        # > 
        # 
        # *   The ID can be up to 55 characters in length and can contain letters, digits, underscores (_), and hyphens (-).
        # 
        # *   If you specify TaskId, the parameters of the specified tasks are returned.
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

