# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateInstanceBindingsOfNumberRequest(DaraModel):
    def __init__(
        self,
        instance_ids: List[str] = None,
        number: str = None,
        tenant_id: str = None,
    ):
        # The list of instance IDs.
        self.instance_ids = instance_ids
        # The bound number.
        # 
        # This parameter is required.
        self.number = number
        # The tenant ID.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.number is not None:
            result['Number'] = self.number

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('Number') is not None:
            self.number = m.get('Number')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        return self

