# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifySupabaseProjectSecurityIpsRequest(DaraModel):
    def __init__(
        self,
        project_id: str = None,
        region_id: str = None,
        security_iplist: str = None,
    ):
        # The Supabase project ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The region ID of the cluster.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/86912.html) operation to query the most recent region list.
        self.region_id = region_id
        # A comma-separated list of IP addresses and CIDR blocks to set as the whitelist. You can specify up to 1,000 entries. Supported formats:
        # 
        # *   Single IP: 10.23.12.24
        # *   CIDR Block: 10.23.12.0/24 (the prefix`/24` indicates the length must be between 1 and 32)``
        # 
        # This parameter is required.
        self.security_iplist = security_iplist

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')

        return self

