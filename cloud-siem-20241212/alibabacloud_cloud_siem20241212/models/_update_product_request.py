# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateProductRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        product_id: str = None,
        product_name: str = None,
        region_id: str = None,
        role_for: int = None,
        vendor_name: str = None,
    ):
        self.lang = lang
        self.product_id = product_id
        self.product_name = product_name
        self.region_id = region_id
        self.role_for = role_for
        self.vendor_name = vendor_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.product_name is not None:
            result['ProductName'] = self.product_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        if self.vendor_name is not None:
            result['VendorName'] = self.vendor_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('VendorName') is not None:
            self.vendor_name = m.get('VendorName')

        return self

