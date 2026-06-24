# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetResourceRenewPriceRequest(DaraModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        period: int = None,
        period_unit: str = None,
        product_type: str = None,
    ):
        # The delivery group ID. You can call the [ListAppInstanceGroup](https://help.aliyun.com/document_detail/428506.html) operation to obtain the ID.
        # 
        # This parameter is required.
        self.app_instance_group_id = app_instance_group_id
        # The numeric part of the purchase duration. This parameter is used together with PeriodUnit to specify the complete purchase duration.
        # 
        # This parameter is required.
        self.period = period
        # The unit part of the purchase duration. This parameter is used together with Period to specify the complete purchase duration. Valid combinations of Period and PeriodUnit:
        # 
        # - 1 Week
        # - 1 Month
        # - 2 Month
        # - 3 Month
        # - 6 Month
        # - 1 Year
        # - 2 Year
        # - 3 Year
        # 
        # > This parameter is case-sensitive. For example, `Week` is valid, but `week` is invalid. If the request parameters do not match the combinations listed above, such as `2 Week`, the call to this operation succeeds, but an error occurs during the order placement phase.
        # 
        # This parameter is required.
        self.period_unit = period_unit
        # The product type.
        # 
        # This parameter is required.
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        return self

