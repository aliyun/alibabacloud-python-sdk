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
        # The page number of the current page in a paginated query.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The IP version of the assets protected by Cloud Firewall. Valid values:
        # 
        # - **4** (default): IPv4.
        # - **6**: IPv6.
        self.ip_version = ip_version
        # The language type of the response. Valid values:
        # 
        # - **zh** (default): Chinese.
        # - **en**: English.
        self.lang = lang
        # The UID of the Cloud Firewall member account.
        self.member_uid = member_uid
        # The time when the asset was discovered. Valid values:
        # - **discovered in 1 hour**: The asset was discovered within 1 hour.
        # - **discovered in 1 day**: The asset was discovered within 1 day.
        # - **discovered in 7 days**: The asset was discovered within 7 days.
        self.new_resource_tag = new_resource_tag
        # Specifies whether to query outbound traffic information.
        self.out_statistic = out_statistic
        # The number of Cloud Firewall-protected assets to display on each page in a paginated query.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The region ID of the Cloud Firewall.
        # 
        # > For more information about regions supported by Cloud Firewall, see [Supported regions](https://help.aliyun.com/document_detail/195657.html).
        self.region_no = region_no
        # The asset type. Valid values:
        # 
        # - **BastionHostEgressIP**: Bastion host egress IP.
        # - **BastionHostIngressIP**: Bastion host ingress IP.
        # - **EcsEIP**: ECS EIP.
        # - **EcsPublicIP**: ECS public IP.
        # - **EIP**: Elastic IP address.
        # - **EniEIP**: Elastic network interface EIP.
        # - **NatEIP**: NAT EIP.
        # - **SlbEIP**: SLB EIP (CLB EIP).
        # - **SlbPublicIP**: SLB public IP (CLB public IP).
        # - **NatPublicIP**: NAT public IP.
        # - **HAVIP**: High-availability virtual IP.
        # - **NlbEIP**: NLB EIP.
        # - **ApiGatewayEIP**: API Gateway public IP.
        # - **AlbEIP**: ALB EIP.
        # - **AiGatewayEIP**: AI Gateway public IP.
        # - **GaEIP**: GA EIP.
        # - **SwasEIP**: Simple Application Server public IP.
        # - **EcdEIP**: Elastic Desktop Service public IP.
        # - **BastionHostIP**: Bastion host IP.
        self.resource_type = resource_type
        # The IP address or instance ID of the asset.
        self.search_item = search_item
        # The status of data leakage detection.
        self.sensitive_status = sensitive_status
        # The security group policy status. Valid values:
        # 
        # - **pass**: Delivered.
        # - **block**: Not delivered.
        # - **unsupport**: Not supported.
        # > If this parameter is not set, all security group policy statuses are queried.
        self.sg_status = sg_status
        # The Cloud Firewall status. Valid values:
        # 
        # - **open**: Protected.
        # - **opening**: Protection enabling.
        # - **closed**: Not protected.
        # - **closing**: Protection disabling.
        # 
        # > If this parameter is not set, all firewall statuses are queried.
        self.status = status
        # This parameter is deprecated.
        self.type = type
        # The user type. Valid values:
        # 
        # - **buy** (default): Paid user.
        # - **free**: Free user.
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

