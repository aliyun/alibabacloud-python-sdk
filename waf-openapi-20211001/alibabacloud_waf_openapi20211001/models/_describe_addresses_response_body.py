# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeAddressesResponseBody(DaraModel):
    def __init__(
        self,
        address_list: List[main_models.DescribeAddressesResponseBodyAddressList] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of addresses.
        self.address_list = address_list
        # The number of entries per page for paging. Valid values: 1 to 500. Default value: 20.
        self.max_results = max_results
        # The pagination token for the next page. If a next page exists, this field contains a value.
        # > If this parameter has a return value, a next page exists. You can pass the returned **NextToken** as a request parameter to retrieve the next page of data. Repeat this process until no value is returned, which indicates that all data has been retrieved.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.address_list:
            for v1 in self.address_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AddressList'] = []
        if self.address_list is not None:
            for k1 in self.address_list:
                result['AddressList'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.address_list = []
        if m.get('AddressList') is not None:
            for k1 in m.get('AddressList'):
                temp_model = main_models.DescribeAddressesResponseBodyAddressList()
                self.address_list.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeAddressesResponseBodyAddressList(DaraModel):
    def __init__(
        self,
        address: str = None,
        gmt_modified: int = None,
        rule_id: int = None,
    ):
        # The address.
        self.address = address
        # The most recent modification time of the address. The value is a UNIX timestamp in milliseconds.
        self.gmt_modified = gmt_modified
        # The address book ID.
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['Address'] = self.address

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        return self

