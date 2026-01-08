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
        # The page number. Valid values: 1 to 50.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The IP version of the asset that is protected by Cloud Firewall. Valid values:
        # 
        # *   **4**: IPv4 (default)
        # *   **6**: IPv6
        self.ip_version = ip_version
        # The language of the content within the response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # The UID of the member that is added to Cloud Firewall.
        self.member_uid = member_uid
        # The time when the asset was added. Valid values:
        # 
        # *   **discovered in 1 hour**: within one hour.
        # *   **discovered in 1 day**: within one day.
        # *   **discovered in 7 days**: within seven days.
        self.new_resource_tag = new_resource_tag
        # Whether to query external traffic information.
        self.out_statistic = out_statistic
        # The number of entries per page. Valid values: 1 to 50.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The region ID of your Cloud Firewall.
        # 
        # > For more information about the regions, see [Supported regions](https://help.aliyun.com/document_detail/195657.html).
        self.region_no = region_no
        # The type of the asset. Valid values:
        # 
        # *   **BastionHostEgressIP**: the egress IP address of a bastion host
        # *   **BastionHostIngressIP**: the ingress IP address of a bastion host
        # *   **EcsEIP**: the elastic IP address (EIP) of an Elastic Compute Service (ECS) instance
        # *   **EcsPublicIP**: the public IP address of an ECS instance
        # *   **EIP**: the EIP
        # *   **EniEIP**: the EIP of an elastic network interface (ENI)
        # *   **NatEIP**: the EIP of a NAT gateway
        # *   **SlbEIP**: the EIP of a Server Load Balancer (SLB) instance or a Classic Load Balancer (CLB) instance
        # *   **SlbPublicIP**: the public IP address of an SLB instance or a CLB instance
        # *   **NatPublicIP**: the public IP address of a NAT gateway
        # *   **HAVIP**: the high-availability virtual IP address (HAVIP)
        self.resource_type = resource_type
        # The instance ID or IP address of the asset.
        self.search_item = search_item
        # Data leakage detection activation status.
        self.sensitive_status = sensitive_status
        # The status of the security group policy. Valid values:
        # 
        # *   **pass**: delivered
        # *   **block**: undelivered
        # *   **unsupport**: unsupported
        # 
        # > If you do not specify this parameter, the assets on which security group policies in all states take effect are queried.
        self.sg_status = sg_status
        # The status of the firewall. Valid values:
        # 
        # *   **open**: The firewall is enabled.
        # *   **opening**: The firewall is being enabled.
        # *   **closed**: The firewall is disabled.
        # *   **closing**: The firewall is being disabled.
        # 
        # > If you do not specify this parameter, the assets that are configured for firewalls in all states are queried.
        self.status = status
        # This parameter is deprecated.
        self.type = type
        # The edition of Cloud Firewall. Valid values:
        # 
        # *   **buy**: a paid edition (default)
        # *   **free**: Free Edition
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

