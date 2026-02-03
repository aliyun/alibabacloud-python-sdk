# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SwitchNetworkRequest(DaraModel):
    def __init__(
        self,
        classic_expired_days: str = None,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        retain_classic: str = None,
        security_token: str = None,
        target_network_type: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The retention period of the classic network endpoint. Valid values: **14**, **30**, **60**, and **120**. Unit: days.
        # 
        # > 
        # 
        # *   This parameter is available and required only when the **RetainClassic** parameter is set to **True**.
        # 
        # *   After you complete the switchover operation, you can also call the [ModifyInstanceNetExpireTime](https://help.aliyun.com/document_detail/473793.html) operation to modify the retention period of the classic network endpoint.
        self.classic_expired_days = classic_expired_days
        # The ID of the instance. You can call the [DescribeInstances](https://help.aliyun.com/document_detail/473778.html) operation to query the ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Specifies whether to retain the original classic network endpoint after you switch the instance from classic network to VPC. Default value: False. Valid values:
        # 
        # *   **True**: retains the classic network endpoint.
        # *   **False**: does not retain the classic network endpoint.
        # 
        # > This parameter is available only when the network type of the instance is classic network.
        self.retain_classic = retain_classic
        self.security_token = security_token
        # The network type to which you want to switch. If you want to switch to VPC network, Set the value to **VPC**.
        self.target_network_type = target_network_type
        # The ID of the vSwitch that belongs to the VPC to which you want to switch. You can call the [DescribeVpcs](https://help.aliyun.com/document_detail/35739.html) operation to query the vSwitch ID.
        # 
        # >  The vSwitch and the instance must be deployed in the same zone.
        self.v_switch_id = v_switch_id
        # The ID of the VPC to which you want to switch. You can call the [DescribeVpcs](https://help.aliyun.com/document_detail/35739.html) operation to query the VPC ID.
        # 
        # > 
        # 
        # *   The VPC and the instance must be deployed in the same region.
        # 
        # *   After you set this parameter, you must also set the **VSwitchId** parameter.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.classic_expired_days is not None:
            result['ClassicExpiredDays'] = self.classic_expired_days

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.retain_classic is not None:
            result['RetainClassic'] = self.retain_classic

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.target_network_type is not None:
            result['TargetNetworkType'] = self.target_network_type

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassicExpiredDays') is not None:
            self.classic_expired_days = m.get('ClassicExpiredDays')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RetainClassic') is not None:
            self.retain_classic = m.get('RetainClassic')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('TargetNetworkType') is not None:
            self.target_network_type = m.get('TargetNetworkType')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

