# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class CreateCommonBandwidthPackageRequest(DaraModel):
    def __init__(
        self,
        bandwidth: int = None,
        client_token: str = None,
        description: str = None,
        isp: str = None,
        internet_charge_type: str = None,
        name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        ratio: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_protection_types: List[str] = None,
        tag: List[main_models.CreateCommonBandwidthPackageRequestTag] = None,
        zone: str = None,
    ):
        # The peak bandwidth of the Internet Shared Bandwidth instance. Unit: Mbit/s. 
        # 
        # <props="intl"><ph>Default value range: **1** to **1000**. Default value: **1**.</ph>
        # 
        # <props="china">
        # 
        # - If **InternetChargeType** is set to **PayByBandwidth**, which indicates that the billable method of the Internet Shared Bandwidth instance is pay-by-bandwidth, the default value range of **Bandwidth** is **2** to **20000**.
        # - If **InternetChargeType** is set to **PayBy95**, which indicates that the billable method of the Internet Shared Bandwidth instance is pay-by-enhanced-95th-percentile, the default value range of **Bandwidth** is **200** to **20000**.
        # - If **InternetChargeType** is set to **PayByDominantTraffic**, which indicates that the billable method of the Internet Shared Bandwidth instance is pay-by-dominant-traffic, the default value range of **Bandwidth** is **1** to **2000**.
        # 
        #  Default value: **1000**.
        # .
        # 
        # This parameter is required.
        self.bandwidth = bandwidth
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The ClientToken value can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** may be different for each API request.
        self.client_token = client_token
        # The description of the Internet Shared Bandwidth instance.
        # 
        # The description must be 0 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # The line type. Valid values:
        # - **BGP** (default): BGP (multi-ISP) lines. All regions support BGP (multi-ISP) lines.
        # - **BGP_PRO**: BGP (multi-ISP) premium lines. Currently, only the Hong Kong (China), Singapore, Japan (Tokyo), Philippines (Manila), Malaysia (Kuala Lumpur), Indonesia (Jakarta), and Thailand (Bangkok) regions support BGP (multi-ISP) premium Internet Shared Bandwidth instances.
        # 
        # If you are a single-ISP bandwidth whitelist user, you can also select the following types:
        # - **ChinaTelecom**: China Telecom
        # - **ChinaUnicom**: China Unicom
        # - **ChinaMobile**: China Mobile
        # - **ChinaTelecom_L2**: China Telecom L2
        # - **ChinaUnicom_L2**: China Unicom L2
        # - **ChinaMobile_L2**: China Mobile L2
        # 
        # If you are a Finance Cloud user in the China (Hangzhou) region, this parameter is required. Set the value to **BGP_FinanceCloud**.
        self.isp = isp
        # The billable method of the Internet Shared Bandwidth instance. Valid values:
        # <props="intl">**PayByTraffic** (pay-by-data-transfer).
        # 
        # <props="china">
        # 
        # - **PayByBandwidth** (default): pay-by-bandwidth.
        # - **PayBy95**: pay-by-enhanced-95th-percentile.
        # - **PayByDominantTraffic**: pay-by-dominant-traffic.
        # .
        self.internet_charge_type = internet_charge_type
        # The name of the Internet Shared Bandwidth instance.
        # 
        # The name must be 0 to 128 characters in length and cannot start with `http://` or `https://`.
        self.name = name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The minimum bandwidth commitment percentage of the Internet Shared Bandwidth instance. Set the value to **20**.
        # 
        #  <props="china"><ph>This parameter is required when **InternetChargeType** is set to **PayBy95**.</ph>
        # >This parameter is supported only on the China site.
        self.ratio = ratio
        # The region ID of the Internet Shared Bandwidth instance.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The security protection level.
        # 
        # - If you do not set this parameter, Anti-DDoS Origin Basic is used by default.
        # 
        # - If you set this parameter to **AntiDDoS_Enhanced**, Anti-DDoS Origin Enhanced is used.
        # 
        # <props="china"><ph>You can set this parameter when **InternetChargeType** is set to **PayBy95**.</ph>
        # 
        # You can specify up to 10 security protection levels.
        # 
        # > This parameter is deprecated.
        self.security_protection_types = security_protection_types
        # The list of tags for the Internet Shared Bandwidth instance.
        self.tag = tag
        # The zone of the Internet Shared Bandwidth instance.
        # This parameter is required when you create an Internet Shared Bandwidth instance for a CloudBox.
        self.zone = zone

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
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.isp is not None:
            result['ISP'] = self.isp

        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.ratio is not None:
            result['Ratio'] = self.ratio

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

        if self.zone is not None:
            result['Zone'] = self.zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ISP') is not None:
            self.isp = m.get('ISP')

        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Ratio') is not None:
            self.ratio = m.get('Ratio')

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
                temp_model = main_models.CreateCommonBandwidthPackageRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('Zone') is not None:
            self.zone = m.get('Zone')

        return self

class CreateCommonBandwidthPackageRequestTag(DaraModel):
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

