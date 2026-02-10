# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVpcHoneyPotListRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        honey_pot_existence: bool = None,
        page_size: int = None,
        vpc_id: str = None,
        vpc_name: str = None,
        vpc_region_id: str = None,
    ):
        # The number of the page to return.
        self.current_page = current_page
        # Specifies whether the cloud honeypot feature is enabled for the VPCs. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.honey_pot_existence = honey_pot_existence
        # The number of entries to return on each page. Default value: 20. If you leave this parameter empty, 20 entries are returned on each page.
        # 
        # > We recommend that you do not leave this parameter empty.
        self.page_size = page_size
        # The ID of the VPC on which the honeypot is deployed.
        # 
        # > You can call the [DescribeVpcList](~~DescribeVpcList~~) operation to query the IDs of VPCs.
        self.vpc_id = vpc_id
        # The name of the VPC.
        # 
        # > You can call the [DescribeVpcList](~~DescribeVpcList~~) operation to query the names of VPCs.
        self.vpc_name = vpc_name
        # The region ID of the VPC.
        # 
        # > You can call the [DescribeVpcList](~~DescribeVpcList~~) operation to query the region IDs of VPCs.
        self.vpc_region_id = vpc_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.honey_pot_existence is not None:
            result['HoneyPotExistence'] = self.honey_pot_existence

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name

        if self.vpc_region_id is not None:
            result['VpcRegionId'] = self.vpc_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('HoneyPotExistence') is not None:
            self.honey_pot_existence = m.get('HoneyPotExistence')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')

        if m.get('VpcRegionId') is not None:
            self.vpc_region_id = m.get('VpcRegionId')

        return self

