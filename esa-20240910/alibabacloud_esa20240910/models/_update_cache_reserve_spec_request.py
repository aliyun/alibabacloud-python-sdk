# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateCacheReserveSpecRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        charge_type: str = None,
        instance_id: str = None,
        target_quota_gb: int = None,
    ):
        # Automatic payment.
        self.auto_pay = auto_pay
        # Billing type. Valid values:
        # - PREPAY
        # - POSTPAY
        self.charge_type = charge_type
        # Instance ID.
        self.instance_id = instance_id
        # Cache requested size, in GB.
        self.target_quota_gb = target_quota_gb

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.target_quota_gb is not None:
            result['TargetQuotaGb'] = self.target_quota_gb

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('TargetQuotaGb') is not None:
            self.target_quota_gb = m.get('TargetQuotaGb')

        return self

