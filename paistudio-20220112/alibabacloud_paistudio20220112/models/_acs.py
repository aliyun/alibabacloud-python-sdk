# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ACS(DaraModel):
    def __init__(
        self,
        acsquota_id: str = None,
        associated_products: List[str] = None,
    ):
        self.acsquota_id = acsquota_id
        self.associated_products = associated_products

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acsquota_id is not None:
            result['ACSQuotaId'] = self.acsquota_id

        if self.associated_products is not None:
            result['AssociatedProducts'] = self.associated_products

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ACSQuotaId') is not None:
            self.acsquota_id = m.get('ACSQuotaId')

        if m.get('AssociatedProducts') is not None:
            self.associated_products = m.get('AssociatedProducts')

        return self

