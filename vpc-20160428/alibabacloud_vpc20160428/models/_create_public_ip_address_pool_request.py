# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class CreatePublicIpAddressPoolRequest(DaraModel):
    def __init__(
        self,
        biz_type: str = None,
        client_token: str = None,
        description: str = None,
        dry_run: bool = None,
        isp: str = None,
        name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_protection_types: List[str] = None,
        tag: List[main_models.CreatePublicIpAddressPoolRequestTag] = None,
        zones: List[str] = None,
    ):
        # The business type of the IP address pool. Valid values:
        # - **CloudBox**: CloudBox. Only CloudBox users can select this type.
        # - **Default** (default): indicates that the business type is not a special type.
        self.biz_type = biz_type
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** may be different for each API request.
        self.client_token = client_token
        # The description of the IP address pool instance.
        # 
        # The description must be 0 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # Specifies whether to perform a dry run. Valid values:
        # - **true**: performs a dry run without creating the IP address pool. The system checks the required parameters, request format, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # - **false** (default): performs a dry run and sends the request. If the request passes the dry run, an HTTP 2xx status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The line type. Valid values:
        # 
        # - **BGP** (default): BGP (Multi-ISP) line.
        # 
        # - **BGP_PRO**: BGP (Multi-ISP) Pro line.
        # 
        # For more information about BGP (Multi-ISP) lines and BGP (Multi-ISP) Pro lines, see [EIP line types](https://help.aliyun.com/document_detail/32321.html).
        # 
        # - If you are a whitelist user of single-ISP bandwidth, you can also select the following types:
        #     - **ChinaTelecom**: China Telecom
        #     - **ChinaUnicom**: China Unicom
        #     - **ChinaMobile**: China Mobile
        #     - **ChinaTelecom_L2**: China Telecom L2
        #     - **ChinaUnicom_L2**: China Unicom L2
        #     - **ChinaMobile_L2**: China Mobile L2
        # - If you are a China (Hangzhou) Finance Cloud user, this field is required. Set this parameter to **BGP_FinanceCloud**.
        self.isp = isp
        # The name of the IP address pool instance.
        # 
        # The name must be 0 to 128 characters in length and cannot start with `http://` or `https://`.
        self.name = name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the IP address pool that you want to create.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the IP address pool belongs.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The security protection level.
        # 
        # - If this parameter is left empty, DDoS Protection (Basic) is used by default.
        # 
        # - If this parameter is set to **AntiDDoS_Enhanced**, DDoS Protection (Enhanced) is used.
        self.security_protection_types = security_protection_types
        # The tags of the resource.
        self.tag = tag
        # The zones of the IP address pool.
        # This parameter is required only when **BizType** is set to **CloudBox**, which indicates that the business type of the IP address pool is CloudBox.
        self.zones = zones

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.isp is not None:
            result['Isp'] = self.isp

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.security_protection_types is not None:
            result['SecurityProtectionTypes'] = self.security_protection_types

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.zones is not None:
            result['Zones'] = self.zones

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('Isp') is not None:
            self.isp = m.get('Isp')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecurityProtectionTypes') is not None:
            self.security_protection_types = m.get('SecurityProtectionTypes')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreatePublicIpAddressPoolRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('Zones') is not None:
            self.zones = m.get('Zones')

        return self

class CreatePublicIpAddressPoolRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the resource. You can specify up to 20 tag keys. The tag key cannot be an empty string.
        # 
        # The tag key can be up to 128 characters in length and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
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

