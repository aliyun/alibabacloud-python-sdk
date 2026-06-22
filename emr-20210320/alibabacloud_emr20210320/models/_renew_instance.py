# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RenewInstance(DaraModel):
    def __init__(
        self,
        emr_renew_duration: int = None,
        emr_renew_duration_unit: str = None,
        instance_id: str = None,
        renew_duration: int = None,
        renew_duration_unit: str = None,
    ):
        # emr实例续费时长。
        self.emr_renew_duration = emr_renew_duration
        # emr实例续费时长单位。
        self.emr_renew_duration_unit = emr_renew_duration_unit
        # 节点ID。
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # 续费时长。
        self.renew_duration = renew_duration
        # 付费时长单位。
        self.renew_duration_unit = renew_duration_unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.emr_renew_duration is not None:
            result['EmrRenewDuration'] = self.emr_renew_duration

        if self.emr_renew_duration_unit is not None:
            result['EmrRenewDurationUnit'] = self.emr_renew_duration_unit

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.renew_duration is not None:
            result['RenewDuration'] = self.renew_duration

        if self.renew_duration_unit is not None:
            result['RenewDurationUnit'] = self.renew_duration_unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EmrRenewDuration') is not None:
            self.emr_renew_duration = m.get('EmrRenewDuration')

        if m.get('EmrRenewDurationUnit') is not None:
            self.emr_renew_duration_unit = m.get('EmrRenewDurationUnit')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RenewDuration') is not None:
            self.renew_duration = m.get('RenewDuration')

        if m.get('RenewDurationUnit') is not None:
            self.renew_duration_unit = m.get('RenewDurationUnit')

        return self

