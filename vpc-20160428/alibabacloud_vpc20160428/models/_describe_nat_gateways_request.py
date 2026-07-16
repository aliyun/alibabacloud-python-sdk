# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DescribeNatGatewaysRequest(DaraModel):
    def __init__(
        self,
        availability_mode: str = None,
        dry_run: bool = None,
        instance_charge_type: str = None,
        name: str = None,
        nat_gateway_id: str = None,
        nat_type: str = None,
        network_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        spec: str = None,
        status: str = None,
        tag: List[main_models.DescribeNatGatewaysRequestTag] = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        self.availability_mode = availability_mode
        # Specifies whether to perform a dry run. Valid values:
        # 
        # - **true**: performs a dry run without querying resource status. The check items include whether the AccessKey pair is valid, whether the RAM user is authorized, and whether required parameters are specified. If the check fails, the corresponding error is returned. If the check succeeds, the error code `DryRunOperation` is returned.
        # 
        # - **false** (default): performs a normal request. After the check succeeds, a 2xx HTTP status code is returned and the resource status is queried directly.
        self.dry_run = dry_run
        # <props="china">The billing method of the NAT gateway instance to query. Valid values:
        # 
        # <props="china">
        # - **PostPaid**: pay-as-you-go.
        # - **PrePaid**: the legacy subscription billing method. The subscription billing method is no longer available for new purchases.
        # 
        # 
        # 
        # <props="intl">The billing method of the NAT gateway instance to query. Valid value: **PostPaid** (pay-as-you-go).
        self.instance_charge_type = instance_charge_type
        # The name of the NAT gateway to query.
        # 
        # The name must be 1 to 128 characters in length and cannot start with `http://` or `https://`.
        self.name = name
        # The ID of the NAT gateway to query.
        self.nat_gateway_id = nat_gateway_id
        # The type of the NAT gateway. Valid value: **Enhanced** (enhanced NAT gateway).
        self.nat_type = nat_type
        # The type of the NAT gateway to query. Valid values:
        # 
        # - **internet**: Internet NAT gateway.
        # - **intranet**: VPC NAT gateway.
        self.network_type = network_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page for paginated queries. Maximum value: **50**. Default value: **10**.
        self.page_size = page_size
        # The region ID of the NAT gateway to query.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to obtain the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the NAT gateway to query belongs.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # <props="china">The specification of the Internet NAT gateway. Only when **InstanceChargeType** is **PrePaid** (legacy subscription Internet NAT gateway), creating a NAT gateway by fixed specification is supported. Valid values:
        # 
        # <props="china">
        # - **Small** (default): small.
        # - **Middle**: medium.
        # - **Large**: large.
        # 
        # 
        # <props="intl">The specification of the NAT gateway. Leave this parameter empty.
        self.spec = spec
        # The status of the NAT gateway to query. Valid values:
        # - **Creating**: Creating a NAT gateway is an asynchronous operation. The status is **Creating** before the creation is complete.
        # 
        # - **Available**: The status after the NAT gateway is created. This is a stable status.
        # 
        # - **Modifying**: Modifying a NAT gateway is an asynchronous operation. The status is **Modifying** during the modification process.
        # 
        # - **Deleting**: Deleting a NAT gateway is an asynchronous operation. The status is **Deleting** during the deletion process.
        # 
        # - **Converting**: Converting a standard NAT gateway to an enhanced NAT gateway is an asynchronous operation. The status is **Converting** during the conversion process.
        self.status = status
        # The list of tags.
        self.tag = tag
        # The ID of the VPC to which the NAT gateway to query belongs.
        self.vpc_id = vpc_id
        # The ID of the zone where the NAT gateway is deployed.
        self.zone_id = zone_id

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
        if self.availability_mode is not None:
            result['AvailabilityMode'] = self.availability_mode

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type

        if self.name is not None:
            result['Name'] = self.name

        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

        if self.nat_type is not None:
            result['NatType'] = self.nat_type

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.spec is not None:
            result['Spec'] = self.spec

        if self.status is not None:
            result['Status'] = self.status

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailabilityMode') is not None:
            self.availability_mode = m.get('AvailabilityMode')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

        if m.get('NatType') is not None:
            self.nat_type = m.get('NatType')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeNatGatewaysRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeNatGatewaysRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the NAT gateway instance. You can specify up to 20 tag keys.
        # 
        # The tag key can be up to 128 characters in length. It cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
        self.key = key
        # The tag value of the NAT gateway instance. You can specify up to 20 tag values.
        # 
        # The tag value can be up to 128 characters in length. It cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
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

