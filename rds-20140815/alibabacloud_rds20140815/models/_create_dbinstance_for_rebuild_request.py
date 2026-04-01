# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDBInstanceForRebuildRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dbinstance_description: str = None,
        dbinstance_id: str = None,
        dbinstance_net_type: str = None,
        instance_network_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        pay_type: str = None,
        period: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_iplist: str = None,
        security_token: str = None,
        used_time: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
        zone_id_slave_1: str = None,
        zone_id_slave_2: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The name of the instance. The name must be 2 to 256 characters in length. The name can contain letters, digits, underscores (_), and hyphens (-). The name must start with a letter.
        # 
        # > : The name cannot start with http:// or https://.
        self.dbinstance_description = dbinstance_description
        # The instance ID. You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/610396.html) operation to query the ID of the instance.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The type of the network connection to the instance. Valid values:
        # 
        # *   **Internet**
        # *   **Intranet**
        self.dbinstance_net_type = dbinstance_net_type
        # The network type of the instance. Valid values:
        # 
        # *   **VPC**
        # *   **Classic**
        # 
        # Default value: Classic.
        # 
        # >  If the instance uses cloud disks, this parameter is required. Set the value to **VPC**. The **VpcId** and **VSwitchId** parameters must be specified when this parameter is set to **VPC**.
        self.instance_network_type = instance_network_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The billing method of the destination instance. Valid values:
        # 
        # *   **Postpaid**: pay-as-you-go
        # *   **Prepaid**: subscription
        # 
        # This parameter is required.
        self.pay_type = pay_type
        # The unit of the subscription duration. Valid values:
        # 
        # *   **Year**
        # *   **Month**
        # 
        # >  If you set the PayType parameter to **Prepaid**, you must also specify this parameter.
        self.period = period
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/610399.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group. The value of this parameter can be NULL.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The IP address whitelist of the serverless instance. For more information, see [Use a database client or the CLI to connect to an ApsaraDB RDS for PostgreSQL instance](https://help.aliyun.com/document_detail/43185.html). If the IP address whitelist contains more than one entry, separate the entries with commas (,). Each entry must be unique. You can specify up to 1,000 entries. The entries in the IP address whitelist must be in one of the following formats:
        # 
        # *   IP addresses, such as 10.10.XX.XX.
        # *   CIDR blocks, such as 10.10.XX.XX/24. In this example, 24 indicates that the prefix of each IP address in the IP address whitelist is 24 bits in length. You can replace 24 with a value within the range of 1 to 32.
        # 
        # If this parameter is not specified, the default IP address whitelist is used.
        self.security_iplist = security_iplist
        self.security_token = security_token
        # The subscription duration of the instance. Valid values:
        # 
        # *   If you set **Period** to **Year**, the value of **UsedTime** ranges from **1** to **5**.
        # *   If you set **Period** to **Month**, the value of **UsedTime** ranges from **1** to **11**.
        # 
        # > If you set **PayType** to **Prepaid**, you must specify this parameter.
        self.used_time = used_time
        # The VPC ID of the instance. If you set **InstanceNetworkType** to **VPC**, you must specify this parameter.
        # 
        # > : If you specify this parameter, you must also specify **ZoneId**.
        self.vpcid = vpcid
        # The ID of the vSwitch. The vSwitch must belong to the zone that is specified by **ZoneId**.
        # 
        # > 
        # 
        # *   If you set **InstanceNetworkType** to **VPC**, you must also specify this parameter.
        # 
        # *   If you specify the ZoneSlaveId1 parameter, you must specify the IDs of two vSwitches for this parameter and separate the IDs with a comma (,).
        self.v_switch_id = v_switch_id
        # The zone ID of the primary instance. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/26243.html) operation to query the most recent zone list.
        # 
        # > If you specify a virtual private cloud (VPC) and a vSwitch, you must specify this parameter to identify the zone for the vSwitch.
        self.zone_id = zone_id
        # The zone ID of the secondary instance.
        # 
        # >  If the instance does not run RDS Basic Edition, you must specify this parameter.
        self.zone_id_slave_1 = zone_id_slave_1
        # The zone ID of the logger instance.
        # 
        # >  This parameter is available only when the instance runs RDS Enterprise Edition.
        self.zone_id_slave_2 = zone_id_slave_2

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dbinstance_net_type is not None:
            result['DBInstanceNetType'] = self.dbinstance_net_type

        if self.instance_network_type is not None:
            result['InstanceNetworkType'] = self.instance_network_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

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

        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.used_time is not None:
            result['UsedTime'] = self.used_time

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        if self.zone_id_slave_1 is not None:
            result['ZoneIdSlave1'] = self.zone_id_slave_1

        if self.zone_id_slave_2 is not None:
            result['ZoneIdSlave2'] = self.zone_id_slave_2

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DBInstanceNetType') is not None:
            self.dbinstance_net_type = m.get('DBInstanceNetType')

        if m.get('InstanceNetworkType') is not None:
            self.instance_network_type = m.get('InstanceNetworkType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

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

        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        if m.get('ZoneIdSlave1') is not None:
            self.zone_id_slave_1 = m.get('ZoneIdSlave1')

        if m.get('ZoneIdSlave2') is not None:
            self.zone_id_slave_2 = m.get('ZoneIdSlave2')

        return self

