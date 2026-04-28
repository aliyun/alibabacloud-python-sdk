# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class CssPurchase(DaraModel):
    def __init__(
        self,
        charge_type: str = None,
        commodity_code: str = None,
        end_date: int = None,
        gmt_create: int = None,
        instance_components: List[main_models.CssInstanceComponent] = None,
        instance_id: str = None,
        order_type: str = None,
        purchase_params: Dict[str, str] = None,
        start_date: int = None,
    ):
        self.charge_type = charge_type
        self.commodity_code = commodity_code
        self.end_date = end_date
        self.gmt_create = gmt_create
        self.instance_components = instance_components
        self.instance_id = instance_id
        self.order_type = order_type
        self.purchase_params = purchase_params
        self.start_date = start_date

    def validate(self):
        if self.instance_components:
            for v1 in self.instance_components:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type

        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code

        if self.end_date is not None:
            result['endDate'] = self.end_date

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        result['instanceComponents'] = []
        if self.instance_components is not None:
            for k1 in self.instance_components:
                result['instanceComponents'].append(k1.to_map() if k1 else None)

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.order_type is not None:
            result['orderType'] = self.order_type

        if self.purchase_params is not None:
            result['purchaseParams'] = self.purchase_params

        if self.start_date is not None:
            result['startDate'] = self.start_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')

        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')

        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        self.instance_components = []
        if m.get('instanceComponents') is not None:
            for k1 in m.get('instanceComponents'):
                temp_model = main_models.CssInstanceComponent()
                self.instance_components.append(temp_model.from_map(k1))

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('orderType') is not None:
            self.order_type = m.get('orderType')

        if m.get('purchaseParams') is not None:
            self.purchase_params = m.get('purchaseParams')

        if m.get('startDate') is not None:
            self.start_date = m.get('startDate')

        return self

