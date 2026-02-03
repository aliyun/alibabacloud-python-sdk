# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_r_kvstore20150101 import models as main_models
from darabonba.model import DaraModel

class CreateTairKVCacheVNodeRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        auto_renew: bool = None,
        auto_renew_period: str = None,
        auto_use_coupon: bool = None,
        business_info: str = None,
        charge_type: str = None,
        client_token: str = None,
        compute_unit_num: int = None,
        coupon_no: str = None,
        dry_run: bool = None,
        elastic_time_range: str = None,
        instance_class: str = None,
        instance_name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        period: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
        tag: List[main_models.CreateTairKVCacheVNodeRequestTag] = None,
        vnode_type: str = None,
        v_switch_id: str = None,
        vk_name: str = None,
        zone_id: str = None,
    ):
        # Specifies whether to enable automatic payment. Set the value to **true**.
        self.auto_pay = auto_pay
        # Specifies whether to enable auto-renewal for the instance. Default value: false. Valid values:
        # 
        # *   **true**: enabled
        # *   **false**: disables auto-renewal.
        self.auto_renew = auto_renew
        # The subscription duration that is supported by auto-renewal. Unit: month. Valid values: **1**, **2**, **3**, **6**, and **12**.
        # 
        # >  This parameter is required if the **AutoRenew** parameter is set to **true**.
        self.auto_renew_period = auto_renew_period
        # Specifies whether to use a coupon. Valid values:
        # 
        # *   **true**: uses a coupon.
        # *   **false**: does not use a coupon.
        self.auto_use_coupon = auto_use_coupon
        # The extended information such as the promotional event ID and business information.
        self.business_info = business_info
        # The new billing method. Valid values:
        # 
        # *   **PrePaid**: subscription. If you set this parameter to PrePaid, you must also specify the **Period** parameter.
        self.charge_type = charge_type
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests and is case-sensitive. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The number of compute units. Valid values: 1.
        # 
        # This parameter is required.
        self.compute_unit_num = compute_unit_num
        # The coupon code.
        self.coupon_no = coupon_no
        # Specifies whether to perform a dry run. Valid values:
        # 
        # *   **true**: performs a dry run and does not create the instance. The system prechecks the request parameters, request format, service limits, and available resources. If the request fails to pass the precheck, an error message is returned. If the request passes the precheck, the `DryRunOperation` error code is returned.
        # *   **false**: performs a dry run and performs the actual request. If the request passes the dry run, the instance is created.
        self.dry_run = dry_run
        self.elastic_time_range = elastic_time_range
        # Instance specification
        # 
        # This parameter is required.
        self.instance_class = instance_class
        # The name of the instance. The name must be 2 to 80 characters in length. The name must start with a letter and cannot contain spaces or the following special characters: `@ / : = " < > { [ ] }`
        self.instance_name = instance_name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The subscription duration. Valid values: **1** to **9**, **12**, **24**, and **36**. Unit: months.
        # 
        # >  This parameter is required only if the **ChargeType** parameter is set to **PrePaid**.
        self.period = period
        # The ID of the region where the instance resides.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group that you want to manage.
        # 
        # > 
        # 
        # *   You can query resource group IDs in the console or by calling the [ListResourceGroups](https://help.aliyun.com/document_detail/158855.html) operation. For more information, see [View the basic information about a resource group](https://help.aliyun.com/document_detail/151181.html).
        # 
        # *   Before you modify the resource group to which an instance belongs, you can call the [ListResources](https://help.aliyun.com/document_detail/158866.html) operation to view the current resource group of the instance.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token
        # Details of the tags.
        self.tag = tag
        self.vnode_type = vnode_type
        # The ID of the vSwitch to which the instance belongs. The vSwitch must belong to the VPC of the VCluser. You can call the [DescribeVpcs](https://help.aliyun.com/document_detail/35739.html) operation to query the VPC ID.
        # 
        # >  The vSwitch and the instance must be deployed in the same zone.
        # 
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # The ID of the VCluster that contains the VNode.
        # 
        # This parameter is required.
        self.vk_name = vk_name
        # The zone ID of the instance.
        # 
        # This parameter is required.
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
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period

        if self.auto_use_coupon is not None:
            result['AutoUseCoupon'] = self.auto_use_coupon

        if self.business_info is not None:
            result['BusinessInfo'] = self.business_info

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.compute_unit_num is not None:
            result['ComputeUnitNum'] = self.compute_unit_num

        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.elastic_time_range is not None:
            result['ElasticTimeRange'] = self.elastic_time_range

        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.period is not None:
            result['Period'] = self.period

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.vnode_type is not None:
            result['VNodeType'] = self.vnode_type

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vk_name is not None:
            result['VkName'] = self.vk_name

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')

        if m.get('AutoUseCoupon') is not None:
            self.auto_use_coupon = m.get('AutoUseCoupon')

        if m.get('BusinessInfo') is not None:
            self.business_info = m.get('BusinessInfo')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ComputeUnitNum') is not None:
            self.compute_unit_num = m.get('ComputeUnitNum')

        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('ElasticTimeRange') is not None:
            self.elastic_time_range = m.get('ElasticTimeRange')

        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateTairKVCacheVNodeRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('VNodeType') is not None:
            self.vnode_type = m.get('VNodeType')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VkName') is not None:
            self.vk_name = m.get('VkName')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class CreateTairKVCacheVNodeRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        # 
        # >  A maximum of five key-value pairs can be specified at a time.
        self.key = key
        # The value of tag N of the instance.
        # 
        # >  **N** specifies the value of the nth tag. For example, **Tag.1.Value** specifies the value of the first tag, and **Tag.2.Value** specifies the value of the second tag.
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

