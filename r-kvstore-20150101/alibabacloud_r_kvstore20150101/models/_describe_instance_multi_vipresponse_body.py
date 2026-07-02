# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_r_kvstore20150101 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceMultiVIPResponseBody(DaraModel):
    def __init__(
        self,
        master_dns: str = None,
        master_dns_record: List[str] = None,
        max_quota: int = None,
        multi_viplist: List[main_models.DescribeInstanceMultiVIPResponseBodyMultiVIPList] = None,
        request_id: str = None,
    ):
        self.master_dns = master_dns
        self.master_dns_record = master_dns_record
        self.max_quota = max_quota
        self.multi_viplist = multi_viplist
        self.request_id = request_id

    def validate(self):
        if self.multi_viplist:
            for v1 in self.multi_viplist:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.master_dns is not None:
            result['MasterDns'] = self.master_dns

        if self.master_dns_record is not None:
            result['MasterDnsRecord'] = self.master_dns_record

        if self.max_quota is not None:
            result['MaxQuota'] = self.max_quota

        result['MultiVIPList'] = []
        if self.multi_viplist is not None:
            for k1 in self.multi_viplist:
                result['MultiVIPList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MasterDns') is not None:
            self.master_dns = m.get('MasterDns')

        if m.get('MasterDnsRecord') is not None:
            self.master_dns_record = m.get('MasterDnsRecord')

        if m.get('MaxQuota') is not None:
            self.max_quota = m.get('MaxQuota')

        self.multi_viplist = []
        if m.get('MultiVIPList') is not None:
            for k1 in m.get('MultiVIPList'):
                temp_model = main_models.DescribeInstanceMultiVIPResponseBodyMultiVIPList()
                self.multi_viplist.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeInstanceMultiVIPResponseBodyMultiVIPList(DaraModel):
    def __init__(
        self,
        connection_string: str = None,
    ):
        self.connection_string = connection_string

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        return self

