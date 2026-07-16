# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDdosEventListRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        ddos_region_id: str = None,
        instance_id: str = None,
        instance_type: str = None,
        internet_ip: str = None,
        page_size: int = None,
        query_days: int = None,
    ):
        # The number of the page to return for a paged query. Default value: **1**.
        self.current_page = current_page
        # The region ID of the asset that is assigned a public IP address.
        # 
        # > Call [DescribeRegions](https://help.aliyun.com/document_detail/353250.html) to query all region IDs.
        # 
        # This parameter is required.
        self.ddos_region_id = ddos_region_id
        # The ID of the instance for the asset that is assigned a public IP address.
        # 
        # > Call [DescribeInstance](https://help.aliyun.com/document_detail/354191.html) to query the IDs of the ECS, SLB, and EIP instances that belong to your Alibaba Cloud account.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The instance type of the asset that is assigned a public IP address. Valid values:
        # 
        # - **ecs**: an Elastic Compute Service (ECS) instance.
        # 
        # - **slb**: a Server Load Balancer (SLB) instance.
        # 
        # - **eip**: an elastic IP address (EIP) instance.
        # 
        # - **ipv6**: an IPv6 Gateway instance.
        # 
        # - **swas**: a simple application server instance.
        # 
        # - **waf**: a dedicated Web Application Firewall (WAF) instance.
        # 
        # - **ga_basic**: a Global Accelerator instance.
        # 
        # This parameter is required.
        self.instance_type = instance_type
        # The IP address of the asset that is assigned a public IP address.
        self.internet_ip = internet_ip
        # The number of attack events to return on each page for a paged query. Default value: **10**.
        self.page_size = page_size
        # The number of days to query backwards from the current time. Default value: 7.
        self.query_days = query_days

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.ddos_region_id is not None:
            result['DdosRegionId'] = self.ddos_region_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.query_days is not None:
            result['QueryDays'] = self.query_days

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('DdosRegionId') is not None:
            self.ddos_region_id = m.get('DdosRegionId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('QueryDays') is not None:
            self.query_days = m.get('QueryDays')

        return self

