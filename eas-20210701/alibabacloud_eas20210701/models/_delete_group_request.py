# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteGroupRequest(DaraModel):
    def __init__(
        self,
        cascade_delete: str = None,
    ):
        # Specifies whether to perform a cascade delete. If enabled, deleting the service group automatically deletes all services within the service group. This feature is disabled by default.
        self.cascade_delete = cascade_delete

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cascade_delete is not None:
            result['CascadeDelete'] = self.cascade_delete

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CascadeDelete') is not None:
            self.cascade_delete = m.get('CascadeDelete')

        return self

