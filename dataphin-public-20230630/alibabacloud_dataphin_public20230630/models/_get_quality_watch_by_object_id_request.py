# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetQualityWatchByObjectIdRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        watch_object_id: str = None,
        watch_type: str = None,
    ):
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.watch_object_id = watch_object_id
        # This parameter is required.
        self.watch_type = watch_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.watch_object_id is not None:
            result['WatchObjectId'] = self.watch_object_id

        if self.watch_type is not None:
            result['WatchType'] = self.watch_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('WatchObjectId') is not None:
            self.watch_object_id = m.get('WatchObjectId')

        if m.get('WatchType') is not None:
            self.watch_type = m.get('WatchType')

        return self

