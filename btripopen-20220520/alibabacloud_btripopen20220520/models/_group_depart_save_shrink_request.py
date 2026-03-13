# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GroupDepartSaveShrinkRequest(DaraModel):
    def __init__(
        self,
        dept_name: str = None,
        manager_ids: str = None,
        outer_dept_id: str = None,
        outer_dept_pid: str = None,
        status: int = None,
        sub_corp_id_list_shrink: str = None,
        sync_group: bool = None,
    ):
        # This parameter is required.
        self.dept_name = dept_name
        self.manager_ids = manager_ids
        # This parameter is required.
        self.outer_dept_id = outer_dept_id
        self.outer_dept_pid = outer_dept_pid
        # This parameter is required.
        self.status = status
        self.sub_corp_id_list_shrink = sub_corp_id_list_shrink
        self.sync_group = sync_group

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dept_name is not None:
            result['dept_name'] = self.dept_name

        if self.manager_ids is not None:
            result['manager_ids'] = self.manager_ids

        if self.outer_dept_id is not None:
            result['outer_dept_id'] = self.outer_dept_id

        if self.outer_dept_pid is not None:
            result['outer_dept_pid'] = self.outer_dept_pid

        if self.status is not None:
            result['status'] = self.status

        if self.sub_corp_id_list_shrink is not None:
            result['sub_corp_id_list'] = self.sub_corp_id_list_shrink

        if self.sync_group is not None:
            result['sync_group'] = self.sync_group

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dept_name') is not None:
            self.dept_name = m.get('dept_name')

        if m.get('manager_ids') is not None:
            self.manager_ids = m.get('manager_ids')

        if m.get('outer_dept_id') is not None:
            self.outer_dept_id = m.get('outer_dept_id')

        if m.get('outer_dept_pid') is not None:
            self.outer_dept_pid = m.get('outer_dept_pid')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('sub_corp_id_list') is not None:
            self.sub_corp_id_list_shrink = m.get('sub_corp_id_list')

        if m.get('sync_group') is not None:
            self.sync_group = m.get('sync_group')

        return self

