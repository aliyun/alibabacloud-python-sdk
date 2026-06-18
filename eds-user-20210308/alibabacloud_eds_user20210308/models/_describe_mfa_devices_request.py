# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeMfaDevicesRequest(DaraModel):
    def __init__(
        self,
        ad_domain: str = None,
        business_channel: str = None,
        end_user_ids: List[str] = None,
        filter: str = None,
        max_results: int = None,
        next_token: str = None,
        serial_numbers: List[str] = None,
    ):
        # The AD domain name.
        self.ad_domain = ad_domain
        # The business channel.
        self.business_channel = business_channel
        # An array of end user usernames.
        self.end_user_ids = end_user_ids
        self.filter = filter
        # The maximum number of results to return per page. Valid range: 1–500.<br>Default value: 100.<br>
        self.max_results = max_results
        # The token for the next page of results. This value is the `NextToken` returned from a previous call.
        self.next_token = next_token
        # An array of serial numbers for virtual MFA devices.
        self.serial_numbers = serial_numbers

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ad_domain is not None:
            result['AdDomain'] = self.ad_domain

        if self.business_channel is not None:
            result['BusinessChannel'] = self.business_channel

        if self.end_user_ids is not None:
            result['EndUserIds'] = self.end_user_ids

        if self.filter is not None:
            result['Filter'] = self.filter

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.serial_numbers is not None:
            result['SerialNumbers'] = self.serial_numbers

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdDomain') is not None:
            self.ad_domain = m.get('AdDomain')

        if m.get('BusinessChannel') is not None:
            self.business_channel = m.get('BusinessChannel')

        if m.get('EndUserIds') is not None:
            self.end_user_ids = m.get('EndUserIds')

        if m.get('Filter') is not None:
            self.filter = m.get('Filter')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('SerialNumbers') is not None:
            self.serial_numbers = m.get('SerialNumbers')

        return self

