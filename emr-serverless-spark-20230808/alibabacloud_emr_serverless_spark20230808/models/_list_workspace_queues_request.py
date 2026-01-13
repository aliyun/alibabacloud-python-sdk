# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListWorkspaceQueuesRequest(DaraModel):
    def __init__(
        self,
        environment: str = None,
        region_id: str = None,
    ):
        # The environment type.
        # 
        # Valid values:
        # 
        # *   dev
        # *   production
        self.environment = environment
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.environment is not None:
            result['environment'] = self.environment

        if self.region_id is not None:
            result['regionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('environment') is not None:
            self.environment = m.get('environment')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        return self

