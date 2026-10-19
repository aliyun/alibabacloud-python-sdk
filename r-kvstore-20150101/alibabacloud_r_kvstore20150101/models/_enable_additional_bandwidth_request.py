# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EnableAdditionalBandwidthRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        auto_renew: bool = None,
        auto_renew_period: int = None,
        band_width_burst: bool = None,
        bandwidth: str = None,
        charge_type: str = None,
        coupon_no: str = None,
        instance_id: str = None,
        node_id: str = None,
        order_time_length: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
        source_biz: str = None,
    ):
        # Specifies whether to enable automatic payment. Valid values:
        # 
        # * **true**: enables automatic payment. This is the default value. Make sure that your account has sufficient balance.
        # * **false**: disables automatic payment. You must manually complete the payment.
        self.auto_pay = auto_pay
        # Specifies whether to enable auto-renewal. Valid values:
        # * **true**: enables auto-renewal.
        # * **false**: disables auto-renewal. This is the default value.
        self.auto_renew = auto_renew
        # The auto-renewal period, in months. Valid values: **1**, **2**, **3**, **4**, **5**, **6**, **7**, **8**, **9**, **12**, **24**, **36**, and **60**.
        # 
        # > * This parameter is available and required only when the **AutoRenew** parameter is set to **true**.
        # > * After this parameter is configured, it cannot be queried by calling API operations. To query the auto-renewal period, choose **Billing** > **Renewal Management** in the top navigation bar of the console, and then enter the instance ID with the `-bw` suffix (for example, r-bp1zxszhcgatnx****-bw) in the **Instance ID** text box.
        self.auto_renew_period = auto_renew_period
        # Specifies whether to enable burstable (second-level) elastic bandwidth. After elastic scaling for bandwidth is enabled, burstable (second-level) elastic bandwidth cannot be enabled, and vice versa.
        self.band_width_burst = band_width_burst
        # The bandwidth to be increased, in MB/s. The value must be an integer greater than or equal to **0**. The maximum value is six times the default bandwidth of the instance (or a single shard) specifications, but the upper limit of the increase is 192 MB/s. For example, if the default bandwidth of the instance is 10 MB/s, the value range is **0** to **60**.
        # 
        # > * You can call the [DescribeRoleZoneInfo](https://help.aliyun.com/document_detail/473782.html) operation and use the **DefaultBandWidth** response parameter to obtain the default maximum bandwidth. For more information about instance specifications, see [Overview of instance specifications](https://help.aliyun.com/document_detail/26350.html).
        # > * If multiple data shard IDs are specified in the **NodeId** request parameter, the bandwidth values specified in this parameter must correspond to the order of the shard IDs. Separate multiple bandwidth values with commas (,).
        self.bandwidth = bandwidth
        # The billing method for the additional bandwidth. Valid values:
        # * **PrePaid**: subscription.
        # * **PostPaid**: pay-as-you-go. Currently, only this billing method is supported.
        self.charge_type = charge_type
        # The ID of the coupon.
        self.coupon_no = coupon_no
        # The ID of the instance. You can call [DescribeInstances](https://help.aliyun.com/document_detail/473778.html) to obtain the instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the data shard. You can call [DescribeLogicInstanceTopology](https://help.aliyun.com/document_detail/473786.html) to obtain the shard ID. Separate multiple shard IDs with commas (,). You can also set this parameter to **All** to specify all data shards.
        # > This parameter is available and required only when the instance uses the [cluster architecture](https://help.aliyun.com/document_detail/52228.html) or [read/write splitting architecture](https://help.aliyun.com/document_detail/62870.html).
        self.node_id = node_id
        # The subscription duration, in days. Valid values: **1**, **2**, **3**, **7**, **14**, **30**, **60**, **90**, **180**, **365**, **730**, **1095**, and **1825**.
        # > To continue using the purchased bandwidth, you must call the [RenewAdditionalBandwidth](https://help.aliyun.com/document_detail/473804.html) operation to renew the bandwidth before it expires.
        self.order_time_length = order_time_length
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token
        # The source of the call. This parameter is used only for internal maintenance and does not need to be specified.
        self.source_biz = source_biz

    def validate(self):
        pass

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

        if self.band_width_burst is not None:
            result['BandWidthBurst'] = self.band_width_burst

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.order_time_length is not None:
            result['OrderTimeLength'] = self.order_time_length

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.source_biz is not None:
            result['SourceBiz'] = self.source_biz

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')

        if m.get('BandWidthBurst') is not None:
            self.band_width_burst = m.get('BandWidthBurst')

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('OrderTimeLength') is not None:
            self.order_time_length = m.get('OrderTimeLength')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('SourceBiz') is not None:
            self.source_biz = m.get('SourceBiz')

        return self

