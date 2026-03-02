# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetLastDeploymentConfigRequest(DaraModel):
    def __init__(
        self,
        service_group_id: int = None,
    ):
        # This parameter is required.
        self.service_group_id = service_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.service_group_id is not None:
            result['serviceGroupId'] = self.service_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('serviceGroupId') is not None:
            self.service_group_id = m.get('serviceGroupId')

        return self

