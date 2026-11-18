# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_r_kvstore20150101 import models as main_models
from darabonba.model import DaraModel

class CreateTairAIGatewayInstanceRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        auto_renew: bool = None,
        auto_renew_period: str = None,
        auto_use_coupon: bool = None,
        business_info: str = None,
        charge_type: str = None,
        client_token: str = None,
        coupon_no: str = None,
        dry_run: bool = None,
        gateway_name: str = None,
        gateway_type: str = None,
        period: int = None,
        plugin_params: str = None,
        plugin_type: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        security_token: str = None,
        tag: List[main_models.CreateTairAIGatewayInstanceRequestTag] = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # Only pay-as-you-go is supported. Ignore this parameter. Specifies whether to enable automatic payment. The value is fixed to **true**.
        self.auto_pay = auto_pay
        # Only pay-as-you-go is supported. Ignore this parameter. Specifies whether to enable auto-renewal. Valid values:
        # * **true**: Enable auto-renewal.
        # * **false** (default): Disable auto-renewal.
        self.auto_renew = auto_renew
        # Only pay-as-you-go is supported. Ignore this parameter. The auto-renewal epoch. Unit: months. Valid values: **1**, **2**, **3**, **6**, and **12**.
        # > This parameter is required when **AutoRenew** is set to **true**.
        self.auto_renew_period = auto_renew_period
        # Only pay-as-you-go is supported. Ignore this parameter.
        # Specifies whether to use a voucher. Valid values:
        # * **true**: Use a voucher.
        # * **false** (default): Do not use a voucher.
        self.auto_use_coupon = auto_use_coupon
        # The activity ID and business information.
        self.business_info = business_info
        # The billing method. Only pay-as-you-go is supported. Valid values:
        # - **PostPaid**: pay-as-you-go.
        self.charge_type = charge_type
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token is case-sensitive and can be up to 64 ASCII characters in length.
        self.client_token = client_token
        # The coupon code. Default value: `default`.
        self.coupon_no = coupon_no
        # Specifies whether to perform a dry run before you create the instance. Valid values:
        # * **true**: performs a dry run and does not create the instance. The system checks the request parameters, request format, service limits, and available resources. If the request fails the dry run, the corresponding error code is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # * **false** (default): sends a normal request and creates the instance after the request passes the check.
        self.dry_run = dry_run
        # The name of the gateway.
        self.gateway_name = gateway_name
        # The specifications of the gateway.
        self.gateway_type = gateway_type
        # Only pay-as-you-go is supported. Ignore this parameter.
        # The renewal period. Unit: months. Valid values: **1** to **9**, **12**, **24**, and **36**.
        # > For example, if an instance expires in three months and you renew it for three months, the instance will expire in six months after the renewal.
        self.period = period
        # **[Deprecated]** This parameter is deprecated. Do not specify this parameter.
        self.plugin_params = plugin_params
        # **[Deprecated]** This parameter is deprecated. Do not specify this parameter.
        self.plugin_type = plugin_type
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        self.security_token = security_token
        # The tags of the instance.
        self.tag = tag
        # The ID of the vSwitch in the VPC. You can call the [DescribeVpcs](https://help.aliyun.com/document_detail/35739.html) operation to query the vSwitch ID.
        # 
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # The VPC ID.
        self.vpc_id = vpc_id
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

        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.gateway_name is not None:
            result['GatewayName'] = self.gateway_name

        if self.gateway_type is not None:
            result['GatewayType'] = self.gateway_type

        if self.period is not None:
            result['Period'] = self.period

        if self.plugin_params is not None:
            result['PluginParams'] = self.plugin_params

        if self.plugin_type is not None:
            result['PluginType'] = self.plugin_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

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

        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('GatewayName') is not None:
            self.gateway_name = m.get('GatewayName')

        if m.get('GatewayType') is not None:
            self.gateway_type = m.get('GatewayType')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PluginParams') is not None:
            self.plugin_params = m.get('PluginParams')

        if m.get('PluginType') is not None:
            self.plugin_type = m.get('PluginType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateTairAIGatewayInstanceRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class CreateTairAIGatewayInstanceRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        # 
        # > * **N** specifies the sequence number of the tag key. You can attach up to 20 tags to an instance. For example, Tag.1.Key specifies the key of the first tag, and Tag.2.Key specifies the key of the second tag.
        # > * If the tag key does not exist, it is automatically created.
        self.key = key
        # The tag value.
        # > **N** specifies the sequence number of the tag value. For example, **Tag.1.Value** specifies the value of the first tag, and **Tag.2.Value** specifies the value of the second tag.
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

