# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PolicyDetailInfo(DaraModel):
    def __init__(
        self,
        class_id: str = None,
        class_name: str = None,
        config: str = None,
        description: str = None,
        name: str = None,
        policy_id: str = None,
    ):
        self.class_id = class_id
        self.class_name = class_name
        self.config = config
        self.description = description
        self.name = name
        self.policy_id = policy_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.class_id is not None:
            result['classId'] = self.class_id

        if self.class_name is not None:
            result['className'] = self.class_name

        if self.config is not None:
            result['config'] = self.config

        if self.description is not None:
            result['description'] = self.description

        if self.name is not None:
            result['name'] = self.name

        if self.policy_id is not None:
            result['policyId'] = self.policy_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('classId') is not None:
            self.class_id = m.get('classId')

        if m.get('className') is not None:
            self.class_name = m.get('className')

        if m.get('config') is not None:
            self.config = m.get('config')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('policyId') is not None:
            self.policy_id = m.get('policyId')

        return self

