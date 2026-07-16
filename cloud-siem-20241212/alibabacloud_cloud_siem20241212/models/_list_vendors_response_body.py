# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20241212 import models as main_models
from darabonba.model import DaraModel

class ListVendorsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
        vendors: List[main_models.ListVendorsResponseBodyVendors] = None,
    ):
        # The maximum number of entries returned for this request.
        self.max_results = max_results
        # The token that is used to retrieve the next page of results. If this is your first query or if no next page exists, you do not need to specify this parameter. If a next page exists, set the value to the NextToken value that is returned in the last response.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The total number of records.
        self.total_count = total_count
        # The vendors.
        self.vendors = vendors

    def validate(self):
        if self.vendors:
            for v1 in self.vendors:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['Vendors'] = []
        if self.vendors is not None:
            for k1 in self.vendors:
                result['Vendors'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.vendors = []
        if m.get('Vendors') is not None:
            for k1 in m.get('Vendors'):
                temp_model = main_models.ListVendorsResponseBodyVendors()
                self.vendors.append(temp_model.from_map(k1))

        return self

class ListVendorsResponseBodyVendors(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        update_time: int = None,
        vendor_id: str = None,
        vendor_name: str = None,
        vendor_type: str = None,
    ):
        # The creation time.
        self.create_time = create_time
        # The update time.
        self.update_time = update_time
        # The vendor ID.
        self.vendor_id = vendor_id
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
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.vendor_id is not None:
            result['VendorId'] = self.vendor_id

        if self.vendor_name is not None:
            result['VendorName'] = self.vendor_name

        if self.vendor_type is not None:
            result['VendorType'] = self.vendor_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('VendorId') is not None:
            self.vendor_id = m.get('VendorId')

        if m.get('VendorName') is not None:
            self.vendor_name = m.get('VendorName')

        if m.get('VendorType') is not None:
            self.vendor_type = m.get('VendorType')

        return self

