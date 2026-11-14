# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sandbox20260820 import models as main_models
from darabonba.model import DaraModel

class PublicWarmPoolConfig(DaraModel):
    def __init__(
        self,
        capacity_policy: main_models.WarmPoolCapacityPolicy = None,
        deleting: bool = None,
        team_id: str = None,
        template_id: str = None,
    ):
        # The warm pool capacity policy, which includes the base target capacity and optional scheduling rules.
        self.capacity_policy = capacity_policy
        # Indicates whether the warm pool is being deleted.
        self.deleting = deleting
        # The team ID.
        self.team_id = team_id
        # The template ID, which specifies the template associated with the warm pool.
        self.template_id = template_id

    def validate(self):
        if self.capacity_policy:
            self.capacity_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.capacity_policy is not None:
            result['capacityPolicy'] = self.capacity_policy.to_map()

        if self.deleting is not None:
            result['deleting'] = self.deleting

        if self.team_id is not None:
            result['teamID'] = self.team_id

        if self.template_id is not None:
            result['templateID'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('capacityPolicy') is not None:
            temp_model = main_models.WarmPoolCapacityPolicy()
            self.capacity_policy = temp_model.from_map(m.get('capacityPolicy'))

        if m.get('deleting') is not None:
            self.deleting = m.get('deleting')

        if m.get('teamID') is not None:
            self.team_id = m.get('teamID')

        if m.get('templateID') is not None:
            self.template_id = m.get('templateID')

        return self

