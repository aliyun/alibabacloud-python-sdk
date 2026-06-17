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
        update_db: bool = None,
        update_web: bool = None,
    ):
        # The Supabase instance ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The region ID.
        # 
        # > For more information, see [DescribeRegions](https://help.aliyun.com/document_detail/86912.html) to view available region IDs.
        self.region_id = region_id
        # The list of IP addresses for the whitelist. Up to 1,000 IP addresses are supported. Separate multiple IP addresses with commas. The following formats are supported:
        # 
        # - 10.23.12.24 (IP address)
        # 
        # - 10.23.12.24/24 (A CIDR block, where `/24` indicates the prefix length. The prefix length must be an integer in the range `[1,32]`.)
        # 
        # This parameter is required.
        self.security_iplist = security_iplist
        # Specifies whether to modify the whitelist for database port 5432. The default value is true.
        self.update_db = update_db
        # Specifies whether to modify the whitelist for HTTP port 80 and HTTPS port 443. The default value is true.
        self.update_web = update_web

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

        if self.update_db is not None:
            result['UpdateDb'] = self.update_db

        if self.update_web is not None:
            result['UpdateWeb'] = self.update_web

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')

        if m.get('UpdateDb') is not None:
            self.update_db = m.get('UpdateDb')

        if m.get('UpdateWeb') is not None:
            self.update_web = m.get('UpdateWeb')

        return self

