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
        # The language of the response messages. Valid values:
        # - **zh** (default): Chinese.
        # - **en**: English. This parameter is required. If not provided, the service returns a 400 error.
        self.lang = lang
        # The product ID. Only products with ProductType set to custom support updates. System preset products (ProductType set to preset) cannot be modified. Calling this operation on a preset product returns a 403 error. To create a custom product, use the CreateProduct API first. This parameter is the resource identifier for the Update operation and is required. Only custom products can be updated. System preset products cannot be updated.
        self.product_id = product_id
        # The product name.
        self.product_name = product_name
        # The region where the data management center of Cloud Threat Detection and Response (CTDR) is located. Select the management center region based on the region where your assets reside. Valid values:
        # - cn-hangzhou: Assets are located in the Chinese mainland.
        # - ap-southeast-1: Assets are located outside China.
        self.region_id = region_id
        # The user ID that the administrator uses to switch to another member\\"s view.
        self.role_for = role_for
        # The vendor name.
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

