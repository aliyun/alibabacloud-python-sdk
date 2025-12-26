# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paistudio20220112 import models as main_models
from darabonba.model import DaraModel

class ListResourceGroupMachineGroupsResponseBody(DaraModel):
    def __init__(
        self,
        machine_groups: List[main_models.MachineGroup] = None,
        request_id: str = None,
        total_count: str = None,
    ):
        self.machine_groups = machine_groups
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.machine_groups:
            for v1 in self.machine_groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MachineGroups'] = []
        if self.machine_groups is not None:
            for k1 in self.machine_groups:
                result['MachineGroups'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.machine_groups = []
        if m.get('MachineGroups') is not None:
            for k1 in m.get('MachineGroups'):
                temp_model = main_models.MachineGroup()
                self.machine_groups.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

