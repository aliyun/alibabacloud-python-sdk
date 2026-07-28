# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class ListPublicIpAddressPoolsRequest(DaraModel):
    def __init__(
        self,
        dry_run: bool = None,
        isp: str = None,
        max_results: int = None,
        name: str = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        public_ip_address_pool_ids: List[str] = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_protection_enabled: bool = None,
        status: str = None,
        tags: List[main_models.ListPublicIpAddressPoolsRequestTags] = None,
    ):
        # Specifies whether to perform a dry run. Valid values:
        # - **true**: performs a dry run without querying available IP address pool information. The system checks whether the required parameters are specified, whether the request format is valid, and whether business restrictions are met. If the check fails, the corresponding error is returned. If the check succeeds, the error code `DryRunOperation` is returned.
        # - **false** (default): performs a dry run and sends the request. If the check succeeds, an HTTP 2xx status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The line type. Valid values:
        # 
        # - **BGP** (default): BGP (multi-ISP) line.
        # 
        # - **BGP_PRO**: BGP (multi-ISP) Pro line.
        # 
        # For more information about BGP (multi-ISP) lines and BGP (multi-ISP) Pro lines, see [EIP line types](https://help.aliyun.com/document_detail/32321.html).
        # 
        # If you are a whitelist user of single-ISP bandwidth, you can also select the following types:
        # - **ChinaTelecom**: China Telecom
        # - **ChinaUnicom**: China Unicom
        # - **ChinaMobile**: China Mobile
        # - **ChinaTelecom_L2**: China Telecom L2
        # - **ChinaUnicom_L2**: China Unicom L2
        # - **ChinaMobile_L2**: China Mobile L2
        # 
        # If you are a China (Hangzhou) Finance Cloud user, this field is required. Set the value to **BGP_FinanceCloud**.
        self.isp = isp
        # The maximum number of entries to return in this request. Valid values: **10** to **100**. Default value: **10**.
        self.max_results = max_results
        # The name of the IP address pool instance.
        # 
        # The name must be 0 to 128 characters in length and cannot start with `http://` or `https://`.
        self.name = name
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # - You do not need to specify this parameter for the first request or if no subsequent request is to be sent.
        # - If a subsequent request is to be sent, set the value to the NextToken value returned in the previous API call.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The list of IP address pool instance IDs.
        # 
        # You can specify up to 100 IP address pool instance IDs.
        self.public_ip_address_pool_ids = public_ip_address_pool_ids
        # The region ID of the IP address pool that you want to query.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to obtain the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the IP address pool belongs.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Specifies whether to enable Anti-DDoS (Enhanced). Valid values:
        # - **false**: disabled.
        # - **true**: enabled.
        self.security_protection_enabled = security_protection_enabled
        # The instance status of the IPAM pool. Valid values:
        # - **Created**: active.
        # - **Deleting**: being deleted.
        # - **Modifying**: being modified.
        self.status = status
        # The list of tags.
        self.tags = tags

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
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.isp is not None:
            result['Isp'] = self.isp

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.name is not None:
            result['Name'] = self.name

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.public_ip_address_pool_ids is not None:
            result['PublicIpAddressPoolIds'] = self.public_ip_address_pool_ids

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.security_protection_enabled is not None:
            result['SecurityProtectionEnabled'] = self.security_protection_enabled

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('Isp') is not None:
            self.isp = m.get('Isp')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PublicIpAddressPoolIds') is not None:
            self.public_ip_address_pool_ids = m.get('PublicIpAddressPoolIds')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecurityProtectionEnabled') is not None:
            self.security_protection_enabled = m.get('SecurityProtectionEnabled')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListPublicIpAddressPoolsRequestTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class ListPublicIpAddressPoolsRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the resource. You can specify up to 20 tag keys. The tag key cannot be an empty string.
        # 
        # A tag key can be up to 128 characters in length and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        self.key = key
        # The tag value of the resource. You can specify up to 20 tag values. The tag value can be an empty string.
        # 
        # The tag value can be up to 128 characters in length and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
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

