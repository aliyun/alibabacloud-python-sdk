# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class DepartmentSaveRequest(DaraModel):
    def __init__(
        self,
        depart_list: List[main_models.DepartmentSaveRequestDepartList] = None,
    ):
        self.depart_list = depart_list

    def validate(self):
        if self.depart_list:
            for v1 in self.depart_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['depart_list'] = []
        if self.depart_list is not None:
            for k1 in self.depart_list:
                result['depart_list'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.depart_list = []
        if m.get('depart_list') is not None:
            for k1 in m.get('depart_list'):
                temp_model = main_models.DepartmentSaveRequestDepartList()
                self.depart_list.append(temp_model.from_map(k1))

        return self

class DepartmentSaveRequestDepartList(DaraModel):
    def __init__(
        self,
        depart_id: int = None,
        depart_name: str = None,
        depart_pid: int = None,
        manager_ids: str = None,
        status: int = None,
        third_depart_id: str = None,
        third_depart_pid: str = None,
    ):
        self.depart_id = depart_id
        # This parameter is required.
        self.depart_name = depart_name
        self.depart_pid = depart_pid
        self.manager_ids = manager_ids
        self.status = status
        self.third_depart_id = third_depart_id
        self.third_depart_pid = third_depart_pid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.depart_id is not None:
            result['depart_id'] = self.depart_id

        if self.depart_name is not None:
            result['depart_name'] = self.depart_name

        if self.depart_pid is not None:
            result['depart_pid'] = self.depart_pid

        if self.manager_ids is not None:
            result['manager_ids'] = self.manager_ids

        if self.status is not None:
            result['status'] = self.status

        if self.third_depart_id is not None:
            result['third_depart_id'] = self.third_depart_id

        if self.third_depart_pid is not None:
            result['third_depart_pid'] = self.third_depart_pid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('depart_id') is not None:
            self.depart_id = m.get('depart_id')

        if m.get('depart_name') is not None:
            self.depart_name = m.get('depart_name')

        if m.get('depart_pid') is not None:
            self.depart_pid = m.get('depart_pid')

        if m.get('manager_ids') is not None:
            self.manager_ids = m.get('manager_ids')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('third_depart_id') is not None:
            self.third_depart_id = m.get('third_depart_id')

        if m.get('third_depart_pid') is not None:
            self.third_depart_pid = m.get('third_depart_pid')

        return self

