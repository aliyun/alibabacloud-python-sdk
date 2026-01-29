# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpgradeResourcePackageRequest(DaraModel):
    def __init__(
        self,
        effective_date: str = None,
        instance_id: str = None,
        owner_id: int = None,
        specification: str = None,
    ):
        # The time when the resource plan takes effect. If you leave this parameter empty, the resource plan immediately takes effect by default.
        # 
        # Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.effective_date = effective_date
        # The ID of the resource plan.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_id = owner_id
        # The specifications to which you want to upgrade the resource plan.
        self.specification = specification

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.effective_date is not None:
            result['EffectiveDate'] = self.effective_date

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.specification is not None:
            result['Specification'] = self.specification

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EffectiveDate') is not None:
            self.effective_date = m.get('EffectiveDate')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Specification') is not None:
            self.specification = m.get('Specification')

        return self

