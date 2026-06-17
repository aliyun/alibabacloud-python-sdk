# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAssetListRequest(DaraModel):
    def __init__(
        self,
        current_page: str = None,
        ip_version: str = None,
        lang: str = None,
        member_uid: int = None,
        new_resource_tag: str = None,
        out_statistic: str = None,
        page_size: str = None,
        region_no: str = None,
        resource_type: str = None,
        search_item: str = None,
        sensitive_status: str = None,
        sg_status: str = None,
        status: str = None,
        type: str = None,
        user_type: str = None,
    ):
        # The page number to return.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The IP version of the asset. Valid values:
        # 
        # - **4** (default): IPv4
        # 
        # - **6**: IPv6
        self.ip_version = ip_version
        # The language of the response. Valid values:
        # 
        # - **zh** (default): Chinese
        # 
        # - **en**: English
        self.lang = lang
        # The UID of the member account.
        self.member_uid = member_uid
        # Filters for assets discovered within a specific time window. Valid values:
        # 
        # - **discovered in 1 hour**: The asset was added within the last hour.
        # 
        # - **discovered in 1 day**: The asset was added within the last day.
        # 
        # - **discovered in 7 days**: The asset was added within the last 7 days.
        self.new_resource_tag = new_resource_tag
        # Specifies whether to query information about outbound traffic.
        self.out_statistic = out_statistic
        # The number of assets to return per page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The region ID of your Cloud Firewall instance.
        # 
        # > For more information about the regions that Cloud Firewall supports, see [Supported regions](https://help.aliyun.com/document_detail/195657.html).
        self.region_no = region_no
        # The asset type. Valid values:
        # 
        # - **BastionHostEgressIP**: The egress IP address of a Bastionhost instance.
        # 
        # - **BastionHostIngressIP**: The ingress IP address of a Bastionhost instance.
        # 
        # - **EcsEIP**: The Elastic IP Address (EIP) of an ECS instance.
        # 
        # - **EcsPublicIP**: The public IP address of an ECS instance.
        # 
        # - **EIP**: An Elastic IP Address (EIP).
        # 
        # - **EniEIP**: The EIP of an elastic network interface (ENI).
        # 
        # - **NatEIP**: The EIP of a NAT Gateway instance.
        # 
        # - **SlbEIP**: The EIP of a Server Load Balancer (SLB) or Classic Load Balancer (CLB) instance.
        # 
        # - **SlbPublicIP**: The public IP address of a Server Load Balancer (SLB) or Classic Load Balancer (CLB) instance.
        # 
        # - **NatPublicIP**: The public IP address of a NAT Gateway instance.
        # 
        # - **HAVIP**: A High-availability Virtual IP (HAVIP).
        # 
        # - **NlbEIP**: The EIP of a Network Load Balancer (NLB) instance.
        # 
        # - **ApiGatewayEIP**: The public IP address of an API Gateway instance.
        # 
        # - **AlbEIP**: The EIP of an Application Load Balancer (ALB) instance.
        # 
        # - **AiGatewayEIP**: The public IP address of an AI Gateway instance.
        # 
        # - **GaEIP**: The EIP of a Global Accelerator (GA) instance.
        # 
        # - **SwasEIP**: The public IP address of a Simple Application Server instance.
        # 
        # - **EcdEIP**: The public IP address of a Wuying instance.
        # 
        # - **BastionHostIP**: The IP address of a Bastionhost instance.
        self.resource_type = resource_type
        # The IP address or instance ID of the asset.
        self.search_item = search_item
        # The status of the data leak detection feature.
        self.sensitive_status = sensitive_status
        # The status of the security group policy. Valid values:
        # 
        # - **pass**: The security group policy is enforced.
        # 
        # - **block**: The security group policy is not enforced.
        # 
        # - **unsupport**: The asset does not support security group policies.
        # 
        # > If you do not specify this parameter, assets are queried regardless of the security group policy status.
        self.sg_status = sg_status
        # The protection status of the asset. Valid values:
        # 
        # - **open**: Protection is enabled.
        # 
        # - **opening**: Protection is being enabled.
        # 
        # - **closed**: Protection is disabled.
        # 
        # - **closing**: Protection is being disabled.
        # 
        # > If you do not specify this parameter, assets are queried regardless of their protection status.
        self.status = status
        # This parameter is deprecated.
        self.type = type
        # The type of the user. Valid values:
        # 
        # - **buy** (default): A user with a paid subscription.
        # 
        # - **free**: A user on the free tier.
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid

        if self.new_resource_tag is not None:
            result['NewResourceTag'] = self.new_resource_tag

        if self.out_statistic is not None:
            result['OutStatistic'] = self.out_statistic

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.search_item is not None:
            result['SearchItem'] = self.search_item

        if self.sensitive_status is not None:
            result['SensitiveStatus'] = self.sensitive_status

        if self.sg_status is not None:
            result['SgStatus'] = self.sg_status

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        if self.user_type is not None:
            result['UserType'] = self.user_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')

        if m.get('NewResourceTag') is not None:
            self.new_resource_tag = m.get('NewResourceTag')

        if m.get('OutStatistic') is not None:
            self.out_statistic = m.get('OutStatistic')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('SearchItem') is not None:
            self.search_item = m.get('SearchItem')

        if m.get('SensitiveStatus') is not None:
            self.sensitive_status = m.get('SensitiveStatus')

        if m.get('SgStatus') is not None:
            self.sg_status = m.get('SgStatus')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')

        return self

