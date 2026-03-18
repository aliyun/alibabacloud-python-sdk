# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePackIpListRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        ip: str = None,
        member_uid: str = None,
        page_no: int = None,
        page_size: int = None,
        product_name: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # The ID of the Anti-DDoS Origin instance to query.
        # 
        # >  You can call the [DescribeInstanceList](https://help.aliyun.com/document_detail/118698.html) operation to query the IDs of all Anti-DDoS Origin instances.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The protected IP address to query.
        self.ip = ip
        # The ID of the member.
        self.member_uid = member_uid
        # The number of the page to return.
        # 
        # This parameter is required.
        self.page_no = page_no
        # The number of entries to return on each page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The type of the cloud asset to which the protected IP address to query belongs. Valid values:
        # 
        # *   **ECS**: an Elastic Compute Service (ECS) instance.
        # *   **SLB**: a Classic Load Balancer (CLB) instance, originally called a Server Load Balancer (SLB) instance.
        # *   **EIP**: an elastic IP address (EIP). An Internet-facing Application Load Balancer (ALB) instance uses an EIP. If the IP address belongs to the Internet-facing ALB instance, set this parameter to EIP.
        # *   **WAF**: a Web Application Firewall (WAF) instance.
        self.product_name = product_name
        # The ID of the region where the Anti-DDoS Origin instance resides.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/118703.html) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the resource group to which the Anti-DDoS Origin instance belongs in Resource Management.
        # 
        # If you do not specify this parameter, the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.product_name is not None:
            result['ProductName'] = self.product_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

