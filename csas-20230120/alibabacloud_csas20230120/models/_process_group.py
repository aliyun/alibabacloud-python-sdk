# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class ProcessGroup(DaraModel):
    def __init__(
        self,
        description: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        name: str = None,
        process_group_id: str = None,
        processes: List[main_models.ProcessItem] = None,
    ):
        self.description = description
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.name = name
        self.process_group_id = process_group_id
        self.processes = processes

    def validate(self):
        if self.processes:
            for v1 in self.processes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.name is not None:
            result['Name'] = self.name

        if self.process_group_id is not None:
            result['ProcessGroupId'] = self.process_group_id

        result['Processes'] = []
        if self.processes is not None:
            for k1 in self.processes:
                result['Processes'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProcessGroupId') is not None:
            self.process_group_id = m.get('ProcessGroupId')

        self.processes = []
        if m.get('Processes') is not None:
            for k1 in m.get('Processes'):
                temp_model = main_models.ProcessItem()
                self.processes.append(temp_model.from_map(k1))

        return self

