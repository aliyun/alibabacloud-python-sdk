# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteGatewaySecurityGroupRuleRequest(DaraModel):
    def __init__(
        self,
        cascading_delete: bool = None,
    ):
        # Whether to cascade delete the security group rules.
        self.cascading_delete = cascading_delete

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cascading_delete is not None:
            result['cascadingDelete'] = self.cascading_delete

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cascadingDelete') is not None:
            self.cascading_delete = m.get('cascadingDelete')

        return self

