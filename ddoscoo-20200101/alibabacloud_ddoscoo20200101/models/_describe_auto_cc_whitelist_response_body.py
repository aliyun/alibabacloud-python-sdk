# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeAutoCcWhitelistResponseBody(DaraModel):
    def __init__(
        self,
        auto_cc_whitelist: List[main_models.DescribeAutoCcWhitelistResponseBodyAutoCcWhitelist] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # An array that consists of details of the IP address in the whitelist of the instance.
        self.auto_cc_whitelist = auto_cc_whitelist
        # The ID of the request.
        self.request_id = request_id
        # The total number of returned IP addresses in the whitelist.
        self.total_count = total_count

    def validate(self):
        if self.auto_cc_whitelist:
            for v1 in self.auto_cc_whitelist:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AutoCcWhitelist'] = []
        if self.auto_cc_whitelist is not None:
            for k1 in self.auto_cc_whitelist:
                result['AutoCcWhitelist'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.auto_cc_whitelist = []
        if m.get('AutoCcWhitelist') is not None:
            for k1 in m.get('AutoCcWhitelist'):
                temp_model = main_models.DescribeAutoCcWhitelistResponseBodyAutoCcWhitelist()
                self.auto_cc_whitelist.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeAutoCcWhitelistResponseBodyAutoCcWhitelist(DaraModel):
    def __init__(
        self,
        dest_ip: str = None,
        end_time: int = None,
        source_ip: str = None,
        type: str = None,
    ):
        # The IP address of the instance.
        self.dest_ip = dest_ip
        # The validity period of the IP address in the whitelist. Unit: seconds. **0** indicates that the IP address in the whitelist never expires.
        self.end_time = end_time
        # The IP addresses that is contained in the IP address whitelist.
        self.source_ip = source_ip
        # The mode of how an IP address is added to the whitelist. Valid values:
        # 
        # *   **manual**: manually added
        # *   **auto**: automatically added
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dest_ip is not None:
            result['DestIp'] = self.dest_ip

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestIp') is not None:
            self.dest_ip = m.get('DestIp')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

