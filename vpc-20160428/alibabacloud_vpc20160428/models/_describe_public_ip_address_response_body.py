# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribePublicIpAddressResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        public_ip_address: List[str] = None,
        region_id: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The status code.
        self.code = code
        # The response message.
        self.message = message
        # The page number of the list.
        self.page_number = page_number
        # The number of entries per page in a paged query.
        self.page_size = page_size
        # The range of public IP addresses in a virtual private cloud (VPC) in the specified region.
        self.public_ip_address = public_ip_address
        # The region ID of the public IP address.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
        # Indicates whether the query was successful. Valid values:
        # 
        # - **true**: The query was successful.
        # 
        # - **false**: The query failed.
        self.success = success
        # The total number of entries in the list.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.public_ip_address is not None:
            result['PublicIpAddress'] = self.public_ip_address

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PublicIpAddress') is not None:
            self.public_ip_address = m.get('PublicIpAddress')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

