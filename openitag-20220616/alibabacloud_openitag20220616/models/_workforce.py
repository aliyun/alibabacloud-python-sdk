# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_openitag20220616 import models as main_models
from darabonba.model import DaraModel

class Workforce(DaraModel):
    def __init__(
        self,
        node_type: str = None,
        users: List[main_models.SimpleUser] = None,
        work_node_id: int = None,
    ):
        # Node name.  
        # Valid values include: SAMPLING, CHECK, MARK.
        self.node_type = node_type
        # List of user information
        self.users = users
        # Node ID
        self.work_node_id = work_node_id

    def validate(self):
        if self.users:
            for v1 in self.users:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node_type is not None:
            result['NodeType'] = self.node_type

        result['Users'] = []
        if self.users is not None:
            for k1 in self.users:
                result['Users'].append(k1.to_map() if k1 else None)

        if self.work_node_id is not None:
            result['WorkNodeId'] = self.work_node_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        self.users = []
        if m.get('Users') is not None:
            for k1 in m.get('Users'):
                temp_model = main_models.SimpleUser()
                self.users.append(temp_model.from_map(k1))

        if m.get('WorkNodeId') is not None:
            self.work_node_id = m.get('WorkNodeId')

        return self

