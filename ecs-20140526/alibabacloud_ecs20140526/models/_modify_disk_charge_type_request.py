# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDiskChargeTypeRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        client_token: str = None,
        disk_charge_type: str = None,
        disk_ids: str = None,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # Specifies whether to enable automatic payment. Valid values: 
        #          
        # - true (default): Automatic payment is enabled. Make sure that your account balance is sufficient. If your account balance is insufficient, an abnormal order is generated, and you can only void the order. 
        # - false: An order is generated without automatic payment. If your account balance is insufficient, an unpaid order is generated. You can log on to the Alibaba Cloud **Expenses and Costs** console and go to the <props="china"><ph>[Orders](https://usercenter2.aliyun.com/order/list)</ph><props="intl"><ph>[Orders](https://usercenter2-intl.aliyun.com/order/list)</ph> page to complete the payment.
        self.auto_pay = auto_pay
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but make sure that the token is unique among different requests. The **ClientToken** value can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The billing method of the disk. Valid values: 
        #          
        # - PrePaid (default): The pay-as-you-go data disk is converted to a subscription data disk. 
        # - PostPaid: The subscription data disk is converted to a pay-as-you-go data disk.
        # 
        # > When you convert a pay-as-you-go disk to subscription, the billing cycle of the capacity fee is automatically synchronized with the associated ECS instance.
        self.disk_charge_type = disk_charge_type
        # The list of disk IDs. The value is a JSON array that contains up to 16 IDs separated by commas (,).
        # 
        # This parameter is required.
        self.disk_ids = disk_ids
        # The instance ID of the instance to which the disk is attached.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the instance. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the most recent list of Alibaba Cloud regions.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.disk_charge_type is not None:
            result['DiskChargeType'] = self.disk_charge_type

        if self.disk_ids is not None:
            result['DiskIds'] = self.disk_ids

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DiskChargeType') is not None:
            self.disk_charge_type = m.get('DiskChargeType')

        if m.get('DiskIds') is not None:
            self.disk_ids = m.get('DiskIds')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

