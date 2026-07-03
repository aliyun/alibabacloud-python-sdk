# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListVendorsRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        role_for: int = None,
        vendor_ids: List[str] = None,
        vendor_name: str = None,
        vendor_type: str = None,
    ):
        # The language of the response message. Valid values:
        # 
        # - **zh** (default): Chinese.
        # 
        # - **en**: English.
        self.lang = lang
        # The maximum number of entries to return for this request.
        self.max_results = max_results
        # The token that is used to retrieve the next page of results. If this is your first query or if no next page exists, you do not need to specify this parameter. If a next page exists, set the value to the NextToken value that is returned in the last response.
        self.next_token = next_token
        # The region where the Data Management center for threat analysis is located. Select a region for the Management Hub based on the region where your asset resides. Valid values:
        # 
        # - cn-hangzhou: Your asset is in the Chinese mainland.
        # 
        # - ap-southeast-1: Your asset is outside China.
        self.region_id = region_id
        # The user ID of a member. An administrator can use this ID to switch to the member\\"s perspective.
        self.role_for = role_for
        # A list of vendors.
        self.vendor_ids = vendor_ids
        # The vendor name.
        self.vendor_name = vendor_name
        # The vendor type. Valid values:
        # 
        # - preset
        # 
        # - custom
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

        if self.vendor_ids is not None:
            result['VendorIds'] = self.vendor_ids

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
            self.vendor_ids = m.get('VendorIds')

        if m.get('VendorName') is not None:
            self.vendor_name = m.get('VendorName')

        if m.get('VendorType') is not None:
            self.vendor_type = m.get('VendorType')

        return self

