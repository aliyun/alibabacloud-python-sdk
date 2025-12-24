# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyInstanceNetworkSpecRequest(DaraModel):
    def __init__(
        self,
        allocate_public_ip: bool = None,
        auto_pay: bool = None,
        client_token: str = None,
        end_time: str = None,
        isp: str = None,
        instance_id: str = None,
        internet_max_bandwidth_in: int = None,
        internet_max_bandwidth_out: int = None,
        network_charge_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        start_time: str = None,
    ):
        # Specifies whether to assign a public IP address. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        self.allocate_public_ip = allocate_public_ip
        # Specifies whether to automatically complete the payment. Valid values:
        # 
        # *   true: After you modify the bandwidth configurations, the payment is automatically completed. Make sure that your account balance is sufficient before you set AutoPay to true. If your account balance is insufficient, your order cannot be paid in the ECS console and becomes invalid. You must cancel the order.
        # *   false: After you modify the bandwidth configurations, an order is generated but the payment is not automatically completed. If your account balance is insufficient, you can set AutoPay to false to generate an unpaid order. Then, you can log on to the [ECS console](https://ecs.console.aliyun.com) to pay for the order.
        # 
        # Default value: true.
        self.auto_pay = auto_pay
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. **The token can contain only ASCII characters and cannot exceed 64 characters in length.** For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The end time of the temporary bandwidth upgrade. Specify the time in the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the yyyy-MM-ddThhZ format. The time must be in UTC and accurate to **hours** (hh).
        # 
        # >  The interval between the end time and start time of temporary bandwidth upgrade must be greater than or equal to 3 hours.
        self.end_time = end_time
        # > This parameter is in invitational preview and is not publicly available.
        self.isp = isp
        # The ID of the instance for which you want to modify network configurations.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The maximum inbound bandwidth from the Internet. Unit: Mbit/s. Valid values:
        # 
        # *   If the purchased outbound public bandwidth is less than or equal to 10 Mbit/s, the valid values of this parameter are 1 to 10 and the default value is 10.
        # *   If the purchased outbound public bandwidth is greater than 10 Mbit/s, the valid values of this parameter are 1 to the `InternetMaxBandwidthOut` value and the default value is the `InternetMaxBandwidthOut` value.
        self.internet_max_bandwidth_in = internet_max_bandwidth_in
        # The maximum outbound public bandwidth. Unit: Mbit/s. Valid values:
        # 
        # *   Valid values when the pay-by-traffic billing method for network usage is used: 0 to 100.
        # 
        # *   Valid values when the pay-by-bandwidth billing method for network usage is used:
        # 
        #     *   Valid values for subscription instances: 0 to 200.
        #     *   Valid values for pay-as-you-go instances: 0 to 100.
        # 
        # >  The maximum outbound bandwidth of a single instance is also limited by the **network baseline bandwidth (Gbit/s) and network burst bandwidth (Gbit/s)** of the instance type. For more information, see [Overview of instance families](https://help.aliyun.com/document_detail/25378.html).
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        # The billing method for network usage. Valid values:
        # 
        # *   PayByBandwidth
        # *   PayByTraffic
        # 
        # > When the **pay-by-traffic** billing method for network usage is used, the maximum inbound and outbound bandwidth values are used as the upper limits of bandwidths instead of guaranteed values. In scenarios where demand outstrips resource supplies, these maximum bandwidths may be limited. If you want guaranteed bandwidths for your instance, use the **pay-by-bandwidth** billing method for network usage.
        self.network_charge_type = network_charge_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The start time of the temporary bandwidth upgrade. Specify the time in the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the yyyy-MM-ddThh:mmZ format. The time must be in UTC and accurate to **minutes (mm)**.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allocate_public_ip is not None:
            result['AllocatePublicIp'] = self.allocate_public_ip

        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.isp is not None:
            result['ISP'] = self.isp

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.internet_max_bandwidth_in is not None:
            result['InternetMaxBandwidthIn'] = self.internet_max_bandwidth_in

        if self.internet_max_bandwidth_out is not None:
            result['InternetMaxBandwidthOut'] = self.internet_max_bandwidth_out

        if self.network_charge_type is not None:
            result['NetworkChargeType'] = self.network_charge_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocatePublicIp') is not None:
            self.allocate_public_ip = m.get('AllocatePublicIp')

        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ISP') is not None:
            self.isp = m.get('ISP')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InternetMaxBandwidthIn') is not None:
            self.internet_max_bandwidth_in = m.get('InternetMaxBandwidthIn')

        if m.get('InternetMaxBandwidthOut') is not None:
            self.internet_max_bandwidth_out = m.get('InternetMaxBandwidthOut')

        if m.get('NetworkChargeType') is not None:
            self.network_charge_type = m.get('NetworkChargeType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

