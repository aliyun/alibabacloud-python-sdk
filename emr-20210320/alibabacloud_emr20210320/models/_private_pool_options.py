# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class PrivatePoolOptions(DaraModel):
    def __init__(
        self,
        match_criteria: str = None,
        private_pool_ids: List[str] = None,
    ):
        # The type of private pool that you want to use to start ECS instances. A private pool is generated when an elasticity assurance or a capacity reservation takes effect. You can select a private pool for starting ECS instances. Valid values: Open, Target, and None. If you set the parameter to Open, the system selects an open private pool to start instances. If no matching open private pools exist, the resources in the public pool are used. In this case, you do not need to specify the ID of the private pool. If you set the parameter to Target, the resources in the specified private pool are used to start ECS instances. If the specified private pool does not exist, ECS instances cannot be started. You must specify the ID of the private pool when you set the parameter to Target. If you set the parameter to None, the resources in private pools are not used to start instances. Default value: None.
        self.match_criteria = match_criteria
        # The IDs of the private pools.
        self.private_pool_ids = private_pool_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.match_criteria is not None:
            result['MatchCriteria'] = self.match_criteria

        if self.private_pool_ids is not None:
            result['PrivatePoolIds'] = self.private_pool_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MatchCriteria') is not None:
            self.match_criteria = m.get('MatchCriteria')

        if m.get('PrivatePoolIds') is not None:
            self.private_pool_ids = m.get('PrivatePoolIds')

        return self

