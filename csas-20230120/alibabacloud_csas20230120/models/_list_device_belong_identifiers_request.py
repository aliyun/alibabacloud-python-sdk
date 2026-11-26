# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListDeviceBelongIdentifiersRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        identifier_ids: List[str] = None,
        identifier_type: str = None,
        identifier_values: List[str] = None,
        max_results: int = None,
        next_token: str = None,
        page_size: int = None,
    ):
        # The current page number. Valid values: 1 to 2147483647.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The list of record IDs to query. You can specify 1 to 100 positive integer decimal strings at a time. If this parameter is specified along with other filter parameters, the records that meet all the conditions are returned.
        self.identifier_ids = identifier_ids
        # The identifier type. MAC indicates the MAC address of the network interface controller (NIC), SystemSN indicates the system serial number, and BIOSSN indicates the BIOS serial number. This parameter is required when IdentifierValues is specified.
        self.identifier_type = identifier_type
        # The list of identifier values for exact match. You can specify 1 to 100 items at a time, and each item can contain 1 to 128 characters. You must specify IdentifierType at the same time. Records that match any value in the array are returned. MAC addresses are uniformly converted to the lowercase colon-separated format. System serial numbers and BIOS serial numbers are case-sensitive and space-sensitive.
        self.identifier_values = identifier_values
        # A reserved pagination parameter. This value is not used in the current version. Use PageSize to specify the number of entries per page.
        self.max_results = max_results
        # A reserved pagination cursor. This value is not used in the current version. Use CurrentPage to specify the page number.
        self.next_token = next_token
        # The maximum number of records to return per page. Valid values: 1 to 1000.
        # 
        # This parameter is required.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.identifier_ids is not None:
            result['IdentifierIds'] = self.identifier_ids

        if self.identifier_type is not None:
            result['IdentifierType'] = self.identifier_type

        if self.identifier_values is not None:
            result['IdentifierValues'] = self.identifier_values

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('IdentifierIds') is not None:
            self.identifier_ids = m.get('IdentifierIds')

        if m.get('IdentifierType') is not None:
            self.identifier_type = m.get('IdentifierType')

        if m.get('IdentifierValues') is not None:
            self.identifier_values = m.get('IdentifierValues')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

