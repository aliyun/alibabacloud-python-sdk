# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetResourcePriceRequest(DaraModel):
    def __init__(
        self,
        amount: int = None,
        app_instance_type: str = None,
        biz_region_id: str = None,
        charge_type: str = None,
        node_instance_type: str = None,
        period: int = None,
        period_unit: str = None,
        product_type: str = None,
    ):
        # The quantity of resources to purchase.
        # 
        # This parameter is required.
        self.amount = amount
        # The ID of the session instance type to purchase. You can call the `ListAppInstanceType` operation to obtain the ID.
        # 
        # Either AppInstanceType or NodeInstanceType must have a value. If both have values, NodeInstanceType is used.
        self.app_instance_type = app_instance_type
        # The region ID of the delivery group. For more information about supported regions, see [Limits](https://help.aliyun.com/document_detail/426036.html).
        # 
        # This parameter is required.
        self.biz_region_id = biz_region_id
        # The billing method.
        # 
        # This parameter is required.
        self.charge_type = charge_type
        # The ID of the resource instance type to purchase. You can call the [ListNodeInstanceType](https://help.aliyun.com/document_detail/428502.html) operation to obtain the ID.
        # 
        # Either AppInstanceType or NodeInstanceType must have a value. If both have values, NodeInstanceType is used.
        self.node_instance_type = node_instance_type
        # The numeric part of the purchase duration. This parameter is used together with PeriodUnit to specify the complete purchase duration.
        # 
        # This parameter is required.
        self.period = period
        # The unit part of the purchase duration. This parameter is used together with Period to specify the complete purchase duration. The following combinations of Period and PeriodUnit are supported:
        # 
        # - 1 Week (1 week)
        # - 1 Month (1 month)
        # - 2 Month (2 months)
        # - 3 Month (3 months)
        # - 6 Month (6 months)
        # - 1 Year (1 year)
        # - 2 Year (2 years)
        # - 3 Year (3 years)
        # 
        # > This parameter is case-sensitive. For example, `Week` is valid, but `week` is invalid. If the request parameters do not match the supported combinations, such as `2 Week`, the API call succeeds but an error occurs during the order placement stage.
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
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.app_instance_type is not None:
            result['AppInstanceType'] = self.app_instance_type

        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.node_instance_type is not None:
            result['NodeInstanceType'] = self.node_instance_type

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('AppInstanceType') is not None:
            self.app_instance_type = m.get('AppInstanceType')

        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('NodeInstanceType') is not None:
            self.node_instance_type = m.get('NodeInstanceType')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        return self

