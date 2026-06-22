# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AutoRenewInstance(DaraModel):
    def __init__(
        self,
        auto_renew: bool = None,
        auto_renew_duration: int = None,
        auto_renew_duration_unit: str = None,
        emr_auto_renew_duration: int = None,
        emr_auto_renew_duration_unit: str = None,
        instance_id: str = None,
    ):
        # 自动续费。
        self.auto_renew = auto_renew
        # 自动续费时长。
        self.auto_renew_duration = auto_renew_duration
        # 自动付费时长单位。
        self.auto_renew_duration_unit = auto_renew_duration_unit
        # emr实例自动续费时长。
        self.emr_auto_renew_duration = emr_auto_renew_duration
        # emr实例自动续费时长单位。
        self.emr_auto_renew_duration_unit = emr_auto_renew_duration_unit
        # 节点ID。
        # 
        # This parameter is required.
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

        if self.emr_auto_renew_duration is not None:
            result['EmrAutoRenewDuration'] = self.emr_auto_renew_duration

        if self.emr_auto_renew_duration_unit is not None:
            result['EmrAutoRenewDurationUnit'] = self.emr_auto_renew_duration_unit

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

        if m.get('EmrAutoRenewDuration') is not None:
            self.emr_auto_renew_duration = m.get('EmrAutoRenewDuration')

        if m.get('EmrAutoRenewDurationUnit') is not None:
            self.emr_auto_renew_duration_unit = m.get('EmrAutoRenewDurationUnit')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

