# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListVendorsShrinkRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        role_for: int = None,
        vendor_ids_shrink: str = None,
        vendor_name: str = None,
        vendor_type: str = None,
    ):
        self.lang = lang
        self.max_results = max_results
        self.next_token = next_token
        self.region_id = region_id
        self.role_for = role_for
        self.vendor_ids_shrink = vendor_ids_shrink
        self.vendor_name = vendor_name
        self.vendor_type = vendor_type

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

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        if self.vendor_ids_shrink is not None:
            result['VendorIds'] = self.vendor_ids_shrink

        if self.vendor_name is not None:
            result['VendorName'] = self.vendor_name

        if self.vendor_type is not None:
            result['VendorType'] = self.vendor_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('VendorIds') is not None:
            self.vendor_ids_shrink = m.get('VendorIds')

        if m.get('VendorName') is not None:
            self.vendor_name = m.get('VendorName')

        if m.get('VendorType') is not None:
            self.vendor_type = m.get('VendorType')

        return self

