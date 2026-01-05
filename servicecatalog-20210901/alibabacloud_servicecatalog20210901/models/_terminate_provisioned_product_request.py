# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TerminateProvisionedProductRequest(DaraModel):
    def __init__(
        self,
        provisioned_product_id: str = None,
    ):
        # The ID of the product instance.
        # 
        # This parameter is required.
        self.provisioned_product_id = provisioned_product_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.provisioned_product_id is not None:
            result['ProvisionedProductId'] = self.provisioned_product_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProvisionedProductId') is not None:
            self.provisioned_product_id = m.get('ProvisionedProductId')

        return self

