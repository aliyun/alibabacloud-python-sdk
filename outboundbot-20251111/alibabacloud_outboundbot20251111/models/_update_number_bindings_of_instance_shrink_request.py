# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateNumberBindingsOfInstanceShrinkRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        numbers_shrink: str = None,
        tenant_id: str = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The list of phone numbers.
        self.numbers_shrink = numbers_shrink
        # The tenant ID.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.numbers_shrink is not None:
            result['Numbers'] = self.numbers_shrink

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Numbers') is not None:
            self.numbers_shrink = m.get('Numbers')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        return self

