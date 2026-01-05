# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateProvisionedProductPlanResponseBody(DaraModel):
    def __init__(
        self,
        plan_id: str = None,
        provisioned_product_id: str = None,
        request_id: str = None,
    ):
        # The plan ID.
        self.plan_id = plan_id
        # The product instance ID.
        self.provisioned_product_id = provisioned_product_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id

        if self.provisioned_product_id is not None:
            result['ProvisionedProductId'] = self.provisioned_product_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')

        if m.get('ProvisionedProductId') is not None:
            self.provisioned_product_id = m.get('ProvisionedProductId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

