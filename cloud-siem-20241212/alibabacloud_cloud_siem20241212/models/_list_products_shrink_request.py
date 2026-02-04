# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListProductsShrinkRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        max_results: int = None,
        next_token: str = None,
        product_ids_shrink: str = None,
        product_name: str = None,
        product_type: str = None,
        region_id: str = None,
        role_for: int = None,
        vendor_id: str = None,
    ):
        self.lang = lang
        self.max_results = max_results
        self.next_token = next_token
        self.product_ids_shrink = product_ids_shrink
        self.product_name = product_name
        self.product_type = product_type
        self.region_id = region_id
        self.role_for = role_for
        self.vendor_id = vendor_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.product_ids_shrink is not None:
            result['ProductIds'] = self.product_ids_shrink

        if self.product_name is not None:
            result['ProductName'] = self.product_name

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        if self.vendor_id is not None:
            result['VendorId'] = self.vendor_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ProductIds') is not None:
            self.product_ids_shrink = m.get('ProductIds')

        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('VendorId') is not None:
            self.vendor_id = m.get('VendorId')

        return self

