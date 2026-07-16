# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AutoRenewInstanceParam(DaraModel):
    def __init__(
        self,
        auto_renew: str = None,
        auto_renew_duration: str = None,
        auto_renew_duration_unit: str = None,
        instance_id: str = None,
    ):
        self.auto_renew = auto_renew
        self.auto_renew_duration = auto_renew_duration
        self.auto_renew_duration_unit = auto_renew_duration_unit
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.auto_renew_duration is not None:
            result['AutoRenewDuration'] = self.auto_renew_duration

        if self.auto_renew_duration_unit is not None:
            result['AutoRenewDurationUnit'] = self.auto_renew_duration_unit

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('AutoRenewDuration') is not None:
            self.auto_renew_duration = m.get('AutoRenewDuration')

        if m.get('AutoRenewDurationUnit') is not None:
            self.auto_renew_duration_unit = m.get('AutoRenewDurationUnit')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

