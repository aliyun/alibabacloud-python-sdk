# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateProductRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        product_name: str = None,
        region_id: str = None,
        role_for: int = None,
        vendor_name: str = None,
    ):
        # The language of the response. Valid values:
        # - **zh** (default): Chinese.
        # - **en**: English.
        # Note: This parameter is required in practice. If you do not specify this parameter, the service returns a 400 error: "The specified Lang can not be empty."
        self.lang = lang
        # The product name.
        self.product_name = product_name
        # The region where the threat analysis data management center resides. Specify the management center based on the region of your assets. Valid values:
        # - cn-hangzhou: Your assets reside in the Chinese mainland.
        # - ap-southeast-1: Your assets reside outside China.
        self.region_id = region_id
        # The user ID that the administrator uses to switch to the view of another member.
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

        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('VendorName') is not None:
            self.vendor_name = m.get('VendorName')

        return self

