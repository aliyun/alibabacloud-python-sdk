# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeAutoCcBlacklistResponseBody(DaraModel):
    def __init__(
        self,
        auto_cc_blacklist: List[main_models.DescribeAutoCcBlacklistResponseBodyAutoCcBlacklist] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # An array that consists of the details of the IP addresses in the blacklist of the instance.
        self.auto_cc_blacklist = auto_cc_blacklist
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The total number of returned IP addresses in the blacklist.
        self.total_count = total_count

    def validate(self):
        if self.auto_cc_blacklist:
            for v1 in self.auto_cc_blacklist:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AutoCcBlacklist'] = []
        if self.auto_cc_blacklist is not None:
            for k1 in self.auto_cc_blacklist:
                result['AutoCcBlacklist'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.auto_cc_blacklist = []
        if m.get('AutoCcBlacklist') is not None:
            for k1 in m.get('AutoCcBlacklist'):
                temp_model = main_models.DescribeAutoCcBlacklistResponseBodyAutoCcBlacklist()
                self.auto_cc_blacklist.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeAutoCcBlacklistResponseBodyAutoCcBlacklist(DaraModel):
    def __init__(
        self,
        dest_ip: str = None,
        end_time: int = None,
        source_ip: str = None,
        type: str = None,
    ):
        # The IP address of the instance.
        self.dest_ip = dest_ip
        # The validity period of the IP address in the blacklist. The value is a UNIX timestamp. Unit: seconds.
        self.end_time = end_time
        # The IP address in the blacklist.
        self.source_ip = source_ip
        # The mode of how the IP address is added to the blacklist. Valid values:
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

