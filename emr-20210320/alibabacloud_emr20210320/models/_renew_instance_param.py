# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RenewInstanceParam(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        renew_duration: int = None,
        renew_duration_unit: str = None,
    ):
        self.instance_id = instance_id
        self.renew_duration = renew_duration
        self.renew_duration_unit = renew_duration_unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.renew_duration is not None:
            result['RenewDuration'] = self.renew_duration

        if self.renew_duration_unit is not None:
            result['RenewDurationUnit'] = self.renew_duration_unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RenewDuration') is not None:
            self.renew_duration = m.get('RenewDuration')

        if m.get('RenewDurationUnit') is not None:
            self.renew_duration_unit = m.get('RenewDurationUnit')

        return self

