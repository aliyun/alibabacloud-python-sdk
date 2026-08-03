# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_actiontrail20200706 import models as main_models
from darabonba.model import DaraModel

class GetAccessKeyLastUsedIpsResponseBody(DaraModel):
    def __init__(
        self,
        ips: List[main_models.GetAccessKeyLastUsedIpsResponseBodyIps] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The IP addresses.
        # 
        # This parameter is required.
        self.ips = ips
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        # 
        # This parameter is required.
        self.request_id = request_id

    def validate(self):
        if self.ips:
            for v1 in self.ips:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Ips'] = []
        if self.ips is not None:
            for k1 in self.ips:
                result['Ips'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ips = []
        if m.get('Ips') is not None:
            for k1 in m.get('Ips'):
                temp_model = main_models.GetAccessKeyLastUsedIpsResponseBodyIps()
                self.ips.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetAccessKeyLastUsedIpsResponseBodyIps(DaraModel):
    def __init__(
        self,
        detail: str = None,
        ip: str = None,
        source: str = None,
        used_timestamp: int = None,
    ):
        # The event details.
        self.detail = detail
        # The IP address.
        self.ip = ip
        # The source of the last usage record.
        # 
        # Valid values:
        # 
        # - Internal: Other event
        # 
        # - ManagementEvent: Management event
        # 
        # - DataEvent: Data event
        self.source = source
        # The timestamp when the IP address was used. Unit: milliseconds.
        self.used_timestamp = used_timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.detail is not None:
            result['Detail'] = self.detail

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.source is not None:
            result['Source'] = self.source

        if self.used_timestamp is not None:
            result['UsedTimestamp'] = self.used_timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('UsedTimestamp') is not None:
            self.used_timestamp = m.get('UsedTimestamp')

        return self

