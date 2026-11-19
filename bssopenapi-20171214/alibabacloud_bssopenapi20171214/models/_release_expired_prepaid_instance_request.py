# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReleaseExpiredPrepaidInstanceRequest(DaraModel):
    def __init__(
        self,
        instance_ids: str = None,
        product_code: str = None,
        product_type: str = None,
    ):
        # The instance IDs. Separate multiple IDs with commas. You can specify up to 20 IDs.
        # 
        # This parameter is required.
        self.instance_ids = instance_ids
        # The product code. You can call the **QueryProductList** operation to query the product code.
        # 
        # This parameter is required.
        self.product_code = product_code
        # The product type.
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        return self

