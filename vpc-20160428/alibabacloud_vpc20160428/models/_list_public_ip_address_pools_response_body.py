# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class ListPublicIpAddressPoolsResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        public_ip_address_pool_list: List[main_models.ListPublicIpAddressPoolsResponseBodyPublicIpAddressPoolList] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # - If **NextToken** is empty, no subsequent request is to be sent.
        # - If **NextToken** is returned, the value indicates the token for the next query.
        self.next_token = next_token
        # The list of IP address pool instances.
        self.public_ip_address_pool_list = public_ip_address_pool_list
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned under the current request conditions.
        self.total_count = total_count

    def validate(self):
        if self.public_ip_address_pool_list:
            for v1 in self.public_ip_address_pool_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['PublicIpAddressPoolList'] = []
        if self.public_ip_address_pool_list is not None:
            for k1 in self.public_ip_address_pool_list:
                result['PublicIpAddressPoolList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.public_ip_address_pool_list = []
        if m.get('PublicIpAddressPoolList') is not None:
            for k1 in m.get('PublicIpAddressPoolList'):
                temp_model = main_models.ListPublicIpAddressPoolsResponseBodyPublicIpAddressPoolList()
                self.public_ip_address_pool_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListPublicIpAddressPoolsResponseBodyPublicIpAddressPoolList(DaraModel):
    def __init__(
        self,
        biz_type: str = None,
        business_status: str = None,
        creation_time: str = None,
        description: str = None,
        ip_address_remaining: bool = None,
        isp: str = None,
        name: str = None,
        owner_id: int = None,
        public_ip_address_pool_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        security_protection_types: List[str] = None,
        share_type: str = None,
        status: str = None,
        tags: List[main_models.ListPublicIpAddressPoolsResponseBodyPublicIpAddressPoolListTags] = None,
        total_ip_num: int = None,
        used_ip_num: int = None,
        user_type: str = None,
        zones: List[str] = None,
    ):
        # The business type of the IP address pool.
        # - **CloudBox**: CloudBox. Only CloudBox users support this type.
        # - **Default** (default): default, indicating a non-special type.
        self.biz_type = biz_type
        # The business status of the IP address pool instance.
        # 
        # - **Normal**: normal.
        # - **FinancialLocked**: locked.
        self.business_status = business_status
        # The creation time, in the format of `YYYY-MM-DDThh:mm:ssZ`.
        self.creation_time = creation_time
        # The description of the IP address pool instance.
        self.description = description
        # Indicates whether idle IP addresses are available.
        # - **true**: yes.
        # - **false**: no.
        self.ip_address_remaining = ip_address_remaining
        # The line type.
        # 
        # - **BGP**: BGP (multi-ISP) line.
        # 
        # - **BGP_PRO**: BGP (multi-ISP) Pro line.
        # 
        # For more information about BGP (multi-ISP) lines and BGP (multi-ISP) Pro lines, see [EIP line types](https://help.aliyun.com/document_detail/32321.html).
        # 
        # If you are a whitelist user of single-ISP bandwidth, the returned type may also be:
        # - **ChinaTelecom**: China Telecom
        # - **ChinaUnicom**: China Unicom
        # - **ChinaMobile**: China Mobile
        # - **ChinaTelecom_L2**: China Telecom L2
        # - **ChinaUnicom_L2**: China Unicom L2
        # - **ChinaMobile_L2**: China Mobile L2
        # 
        # If you are a China (Hangzhou) Finance Cloud user, **BGP_FinanceCloud** is returned.
        self.isp = isp
        # The name of the IP address pool instance.
        self.name = name
        # The Alibaba Cloud account to which the IP address pool belongs.
        self.owner_id = owner_id
        # The instance ID of the IP address pool.
        self.public_ip_address_pool_id = public_ip_address_pool_id
        # The region ID of the IP address pool.
        self.region_id = region_id
        # The ID of the resource group to which the IP address pool belongs.
        self.resource_group_id = resource_group_id
        # The security protection level.
        # 
        # - If this parameter is empty, the default value is Anti-DDoS Basic.
        # 
        # - If the value is **AntiDDoS_Enhanced**, it indicates Anti-DDoS (Enhanced).
        self.security_protection_types = security_protection_types
        # The sharing type of the IP address pool.
        # 
        # - **Shared**: The IP address pool is a shared IP address pool.
        # - Empty: The IP address pool is not a shared IP address pool.
        self.share_type = share_type
        # The instance status of the IPAM pool.
        # - **Created**: active.
        # - **Deleting**: being deleted.
        # - **Modifying**: being modified.
        self.status = status
        # The list of tags.
        self.tags = tags
        # The total number of available IP addresses in the public IP address pool.
        self.total_ip_num = total_ip_num
        # The number of used IP addresses in the public IP address pool.
        self.used_ip_num = used_ip_num
        # The type of the user. Valid values:
        # - **admin**: administrator. An administrator can delete, modify, and query IP address pools, and allocate elastic IP addresses (EIPs) from IP address pools.
        # - **user**: regular user. A regular user can only allocate EIPs from IP address pools and query IP address pools, but cannot modify or delete IP address pools.
        self.user_type = user_type
        # The zones of the IP address pool.
        # This parameter is returned only when the business type of the IP address pool is CloudBox.
        self.zones = zones

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.business_status is not None:
            result['BusinessStatus'] = self.business_status

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.ip_address_remaining is not None:
            result['IpAddressRemaining'] = self.ip_address_remaining

        if self.isp is not None:
            result['Isp'] = self.isp

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.public_ip_address_pool_id is not None:
            result['PublicIpAddressPoolId'] = self.public_ip_address_pool_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.security_protection_types is not None:
            result['SecurityProtectionTypes'] = self.security_protection_types

        if self.share_type is not None:
            result['ShareType'] = self.share_type

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.total_ip_num is not None:
            result['TotalIpNum'] = self.total_ip_num

        if self.used_ip_num is not None:
            result['UsedIpNum'] = self.used_ip_num

        if self.user_type is not None:
            result['UserType'] = self.user_type

        if self.zones is not None:
            result['Zones'] = self.zones

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('BusinessStatus') is not None:
            self.business_status = m.get('BusinessStatus')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('IpAddressRemaining') is not None:
            self.ip_address_remaining = m.get('IpAddressRemaining')

        if m.get('Isp') is not None:
            self.isp = m.get('Isp')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PublicIpAddressPoolId') is not None:
            self.public_ip_address_pool_id = m.get('PublicIpAddressPoolId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SecurityProtectionTypes') is not None:
            self.security_protection_types = m.get('SecurityProtectionTypes')

        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListPublicIpAddressPoolsResponseBodyPublicIpAddressPoolListTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TotalIpNum') is not None:
            self.total_ip_num = m.get('TotalIpNum')

        if m.get('UsedIpNum') is not None:
            self.used_ip_num = m.get('UsedIpNum')

        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')

        if m.get('Zones') is not None:
            self.zones = m.get('Zones')

        return self

class ListPublicIpAddressPoolsResponseBodyPublicIpAddressPoolListTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

