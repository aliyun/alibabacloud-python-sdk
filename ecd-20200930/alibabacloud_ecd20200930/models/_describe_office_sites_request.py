# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeOfficeSitesRequest(DaraModel):
    def __init__(
        self,
        account_type: str = None,
        max_results: int = None,
        next_token: str = None,
        office_site_id: List[str] = None,
        office_site_type: str = None,
        region_id: str = None,
        security_protection: str = None,
        status: str = None,
        vpc_id: str = None,
    ):
        self.account_type = account_type
        # The number of entries to return on each page.
        # 
        # *   Maximum value: 100.
        # *   Default value: 10.
        self.max_results = max_results
        # The token that determines the start point of the next query.
        self.next_token = next_token
        # The office network IDs. You can specify the IDs of 1 to 100 office networks.
        self.office_site_id = office_site_id
        # The account type of the office network.
        # 
        # Valid values:
        # 
        # *   SIMPLE: convenience account
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   AD_CONNECTOR: enterprise Active Directory (AD) account
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.office_site_type = office_site_type
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The security protection setting of the office network.
        # 
        # Valid values:
        # 
        # *   SASE: SASE is configured.
        # *   OFF: No security protection setting is configured.
        self.security_protection = security_protection
        # The office network status.
        # 
        # Valid values:
        # 
        # *   REGISTERING: The office network is being registered.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   DEREGISTERING: The office network is being deregistered.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   REGISTERED: The office network is registered.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   NEEDCONFIGTRUST: A trust relationship is required for the office network.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   CONFIGTRUSTFAILED: A trust relationship fails to be configured for the office network.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   DEREGISTERED: The office network is deregistered.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   ERROR: One or more configurations of the office network are invalid.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   CONFIGTRUSTING: A trust relationship is being configured for the office network.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   NEEDCONFIGUSER: Users are required for the office network.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.status = status
        # The ID of the virtual private cloud (VPC).
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_type is not None:
            result['AccountType'] = self.account_type

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.office_site_type is not None:
            result['OfficeSiteType'] = self.office_site_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.security_protection is not None:
            result['SecurityProtection'] = self.security_protection

        if self.status is not None:
            result['Status'] = self.status

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('OfficeSiteType') is not None:
            self.office_site_type = m.get('OfficeSiteType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SecurityProtection') is not None:
            self.security_protection = m.get('SecurityProtection')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

