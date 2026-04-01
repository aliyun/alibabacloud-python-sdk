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
        resource_owner_id: int = None,
        used_time: int = None,
    ):
        # The instance ID. You can call the DescribeDBInstances operation to query the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The billing method of the instance. The value is fixed as **Prepaid**, which indicates the subscription billing method.
        # 
        # This parameter is required.
        self.pay_type = pay_type
        # The renewal cycle of the instance.
        # 
        # *   **Year**
        # *   **Month**
        # 
        # This parameter is required.
        self.period = period
        self.resource_owner_id = resource_owner_id
        # The subscription duration of the instance. Valid values:
        # 
        # *   If you set the **Period** parameter to **Year**, the value of the **UsedTime** parameter ranges from 1 to 5.
        # *   If you set the **Period** parameter to **Month**, the value of the **UsedTime** parameter ranges from 1 to 11.
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

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

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

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')

        return self

