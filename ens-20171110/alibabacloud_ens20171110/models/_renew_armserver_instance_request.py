# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RenewARMServerInstanceRequest(DaraModel):
    def __init__(
        self,
        auto_renew: bool = None,
        instance_id: str = None,
        period: int = None,
        period_unit: str = None,
    ):
        # Specifies whether to enable auto-renewal. Valid values:
        # 
        # - **true**: Auto-renewal is enabled.
        # - **false**: Auto-renewal is not enabled. This is the default value.
        self.auto_renew = auto_renew
        # The ID of the server instance to be renewed.
        # 
        # Pass the ServerId (with the cas- prefix) returned by DescribeARMServerInstances, not the InstanceId (with the aic- prefix) in AICInstances.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The renewal period. By default, the instance is renewed on a monthly basis. Valid values: 1, 2, 3, 4, 5, 6, 7, 8, 9, and 12.
        # 
        # This parameter is required.
        self.period = period
        # The unit of the renewal period. Valid values:
        # - Month (default)
        # - Year
        # 
        # This parameter is required.
        self.period_unit = period_unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        return self

