# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBInstancePayTypeRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        pay_type: str = None,
        period: str = None,
        used_time: int = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The billing method of the instance. Valid values:
        # 
        # *   Postpaid: pay-as-you-go.
        # *   Prepaid: subscription.
        # 
        # This parameter is required.
        self.pay_type = pay_type
        # The unit of the subscription duration. Valid values:
        # 
        # *   Month
        # *   Year
        # 
        # This parameter must be specified only when PayType is set to Prepaid.
        self.period = period
        # The subscription duration.
        # 
        # *   Valid values when Period is set to Month: 1 to 9.
        # *   Valid values when Period is set to Year: 1 to 3.
        # 
        # This parameter must be specified only when PayType is set to Prepaid.
        self.used_time = used_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.period is not None:
            result['Period'] = self.period

        if self.used_time is not None:
            result['UsedTime'] = self.used_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')

        return self

