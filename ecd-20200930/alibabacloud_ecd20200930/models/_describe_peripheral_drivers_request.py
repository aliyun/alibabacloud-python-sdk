# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribePeripheralDriversRequest(DaraModel):
    def __init__(
        self,
        brand: str = None,
        device_type: str = None,
        driver_ids: List[str] = None,
        filter: str = None,
        max_results: int = None,
        next_token: str = None,
        owner_type: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The brand identifier. Exact match is used. The value depends on the actual configuration and is not a fixed enumeration. If this parameter is not specified, drivers of all brands are returned. The example value is provided to illustrate the format only.
        self.brand = brand
        # The device type identifier. Exact match is used. The value depends on the actual configuration. For example, printer indicates a printer. If this parameter is not specified, drivers of all device types are returned.
        self.device_type = device_type
        # The list of driver IDs. If this parameter is not specified or an empty array is passed in, no filtering by driver ID is applied. Only drivers that are visible to the current account and match the specified IDs are returned. IDs that do not match any driver do not produce corresponding records.
        self.driver_ids = driver_ids
        # The search keyword. The keyword is matched against the driver ID, brand identifier, driver name, description, device type, or brand display name. A hit on any field qualifies the driver. The wildcard % matches any number of characters, and _ matches a single character. If this parameter is not specified, no keyword filtering is applied.
        self.filter = filter
        # Reserved parameter. This parameter does not participate in queries or pagination. Do not specify this parameter. Use PageSize to set the number of entries per page. The example value 20 is provided only to illustrate the integer type. It is not the default value of this parameter and does not take effect if specified.
        self.max_results = max_results
        # Reserved parameter. Token-based pagination is not supported. Do not specify this parameter. Use PageNumber to specify the page number. The example value token-for-format-only is provided only to illustrate the string type and is not a usable pagination token.
        self.next_token = next_token
        # The driver ownership. Valid values:
        # - WUYING: Wuying official driver.
        # - CUSTOMER: Custom driver of the current account.
        # 
        # If this parameter is not specified, both types of drivers are queried.
        self.owner_type = owner_type
        # The page number. Start from 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 500. Default value: 20.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.brand is not None:
            result['Brand'] = self.brand

        if self.device_type is not None:
            result['DeviceType'] = self.device_type

        if self.driver_ids is not None:
            result['DriverIds'] = self.driver_ids

        if self.filter is not None:
            result['Filter'] = self.filter

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.owner_type is not None:
            result['OwnerType'] = self.owner_type

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Brand') is not None:
            self.brand = m.get('Brand')

        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')

        if m.get('DriverIds') is not None:
            self.driver_ids = m.get('DriverIds')

        if m.get('Filter') is not None:
            self.filter = m.get('Filter')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OwnerType') is not None:
            self.owner_type = m.get('OwnerType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

