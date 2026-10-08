# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateReadOnlyDBInstanceRequest(DaraModel):
    def __init__(
        self,
        auto_create_proxy: bool = None,
        auto_pay: bool = None,
        auto_renew: str = None,
        auto_use_coupon: bool = None,
        bpe_enabled: str = None,
        bursting_enabled: bool = None,
        category: str = None,
        client_token: str = None,
        custom_extra_info: str = None,
        dbinstance_class: str = None,
        dbinstance_description: str = None,
        dbinstance_id: str = None,
        dbinstance_storage: int = None,
        dbinstance_storage_type: str = None,
        dedicated_host_group_id: str = None,
        deletion_protection: bool = None,
        engine_version: str = None,
        gdn_instance_name: str = None,
        instance_network_type: str = None,
        instruction_set_arch: str = None,
        io_acceleration_enabled: str = None,
        is_analytic_read_only_ins: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        pay_type: str = None,
        period: str = None,
        port: str = None,
        private_ip_address: str = None,
        promotion_code: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        target_dedicated_host_id_for_master: str = None,
        tddl_biz_type: str = None,
        tddl_region_config: str = None,
        used_time: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        # Specifies whether to automatically create a database proxy. Valid values:
        # 
        # - **true**: enables automatic creation. By default, a general-purpose database proxy is created.
        # 
        # - **false**: does not enable automatic creation of a database proxy.
        self.auto_create_proxy = auto_create_proxy
        # Specifies whether to enable automatic payment. Valid values:
        # 
        # - **true**: enables automatic payment. Make sure that your account balance is sufficient.
        # - **false**: generates an order without charging your account.
        # 
        # 
        # 
        # 
        # > The default value is true. If your payment method has an insufficient balance, set AutoPay to false. In this case, an unpaid order is generated. You can log on to the ApsaraDB RDS console to complete the payment.
        # >
        self.auto_pay = auto_pay
        # Specifies whether to enable auto-renewal. This parameter is required only for subscription instances. Valid values:
        # * **true**: enables auto-renewal.
        # * **false**: disables auto-renewal.
        # 
        # > * If you purchase the instance on a monthly basis, the auto-renewal cycle is one month.
        # > * If you purchase the instance on a yearly basis, the auto-renewal cycle is one year.
        self.auto_renew = auto_renew
        # Specifies whether to use coupons. Valid values:
        # * **true**: uses coupons.
        # * **false** (default): does not use coupons.
        self.auto_use_coupon = auto_use_coupon
        self.bpe_enabled = bpe_enabled
        # Specifies whether to enable the I/O performance burst feature for [Premium ESSDs](https://help.aliyun.com/document_detail/2340501.html). Valid values:
        # * **true**: enables the feature.
        # * **false**: disables the feature.
        self.bursting_enabled = bursting_enabled
        # The instance edition. Valid values:
        # 
        # * **Basic**: Basic Edition
        # * **HighAvailability**: High-availability Edition (default)
        # * **AlwaysOn**: Cluster Edition
        # 
        # <props="china">* **Finance**: Finance Edition
        # 
        # > The read-only instances of ApsaraDB RDS for PostgreSQL cloud disk instances use the Basic Edition. You must set this parameter to **Basic**.
        self.category = category
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # A reserved parameter. You do not need to specify this parameter.
        self.custom_extra_info = custom_extra_info
        # The instance type. For more information, see [Read-only instance types](https://help.aliyun.com/document_detail/145759.html). We recommend that the specifications of the read-only instance be equal to or higher than those of the primary instance. Otherwise, the read-only instance may experience high latency and heavy loads.
        # 
        # This parameter is required.
        self.dbinstance_class = dbinstance_class
        # The instance description. The description must be 2 to 256 characters in length and can contain letters, digits, underscores (_), and hyphens (-). It must start with a letter or a Chinese character.
        # > The description cannot start with http:// or https://.
        self.dbinstance_description = dbinstance_description
        # The primary instance ID. You can call [DescribeDBInstances](https://help.aliyun.com/document_detail/26232.html) to query the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # Instance storage capacity. Instance storage capacity of the read-only instance must be greater than or equal to that of the primary instance. For more information, see the **Storage capacity** column in [Read-only instance types](https://help.aliyun.com/document_detail/145759.html). The value is incremented in units of 5 GB. Unit: GB.
        # 
        # This parameter is required.
        self.dbinstance_storage = dbinstance_storage
        # The storage type of the instance. Valid values:
        # * **local_ssd**: Premium Local SSDs
        # * **cloud_ssd**: standard SSDs
        # * **cloud_essd**: PL1 ESSDs
        # * **cloud_essd2**: PL2 ESSDs
        # * **cloud_essd3**: PL3 ESSDs
        # * **general_essd**: Premium ESSDs
        # 
        # 
        # > * If the primary ApsaraDB RDS for MySQL instance uses Premium Local SSDs, only **local_ssd** is supported. If the primary ApsaraDB RDS for MySQL instance uses cloud disks, premium performance disk storage types are supported.
        # > * ApsaraDB RDS for SQL Server supports premium performance disk storage types.
        self.dbinstance_storage_type = dbinstance_storage_type
        # The dedicated cluster ID. This parameter is required when you create a read-only instance in a dedicated cluster.
        self.dedicated_host_group_id = dedicated_host_group_id
        # Specifies whether to enable the release protection feature for the instance. Valid values:
        # * **true**: enables release protection.
        # * **false**: disables release protection. (default)
        # 
        # > This feature is supported only when the **billing method** is **pay-as-you-go**.
        self.deletion_protection = deletion_protection
        # The database engine version. The version must be the same as that of the primary instance.
        # 
        # * Valid values for MySQL: **5.6**, **5.7**, and **8.0**.
        # * Valid values for SQL Server: **2017_ent, 2019_ent, and 2022_ent**.
        # * Valid values for PostgreSQL: **10.0, 11.0, 12.0, 13.0, 14.0, and 15.0**.
        # 
        # This parameter is required.
        self.engine_version = engine_version
        # A reserved parameter. You do not need to specify this parameter.
        self.gdn_instance_name = gdn_instance_name
        # The network type of the read-only instance. Valid values:
        # 
        # * **VPC**: virtual private cloud (VPC)
        # * **Classic**: classic network
        # 
        # By default, a VPC-connected instance is created. You must also specify **VPCId** and **VSwitchId**.
        # > The network type of the read-only instance can be different from that of the primary instance.
        self.instance_network_type = instance_network_type
        # A reserved parameter. You do not need to specify this parameter.
        self.instruction_set_arch = instruction_set_arch
        # Specifies whether to enable the [Buffer Pool Extension (BPE)](https://help.aliyun.com/document_detail/2527067.html) feature for Premium ESSDs. Valid values:
        # 
        #  - **1**: enables the feature.
        #  - **0**: does not enable the feature.
        self.io_acceleration_enabled = io_acceleration_enabled
        # Specifies whether to create a DuckDB-based analytical instance. Valid values:
        # 
        # - **true**: creates a DuckDB-based analytical instance.
        # - **false**: does not create a DuckDB-based analytical instance.
        # 
        # > Only ApsaraDB RDS for MySQL and ApsaraDB RDS for PostgreSQL support DuckDB-based analytical instances.
        self.is_analytic_read_only_ins = is_analytic_read_only_ins
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The billing method. Valid values:
        # * **Postpaid**: pay-as-you-go
        # * **Prepaid**: subscription
        # 
        # This parameter is required.
        self.pay_type = pay_type
        # The subscription type of the instance. Valid values:
        # * **Year**: yearly subscription
        # * **Month**: monthly subscription
        self.period = period
        # The port that is initialized when you create a read-only instance for an ApsaraDB RDS for MySQL primary instance.
        # 
        # Valid values: 1000 to 65534.
        self.port = port
        # The internal IP address of the read-only instance. The IP address must be within the address range of the specified vSwitch. The system automatically allocates an internal IP address based on the values of **VPCId** and **VSwitchId** by default.
        self.private_ip_address = private_ip_address
        # The coupon code.
        self.promotion_code = promotion_code
        # The region ID. The read-only instance must reside in the same region as the primary instance. You can call [DescribeRegions](https://help.aliyun.com/document_detail/26243.html) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The host ID of the primary instance in the dedicated cluster. This parameter is required when you create a read-only instance in a dedicated cluster.
        self.target_dedicated_host_id_for_master = target_dedicated_host_id_for_master
        # A reserved parameter. You do not need to specify this parameter.
        self.tddl_biz_type = tddl_biz_type
        # A reserved parameter. You do not need to specify this parameter.
        self.tddl_region_config = tddl_region_config
        # The subscription duration. Valid values:
        # * If **Period** is set to **Year**, the valid values of **UsedTime** are **1** to **5**.
        # * If **Period** is set to **Month**, the valid values of **UsedTime** are **1** to **9**.
        # 
        # > This parameter is required when **PayType** is set to **Prepaid**.
        self.used_time = used_time
        # The VPC ID of the read-only instance. This parameter is required when **InstanceNetworkType** is left empty or set to **VPC**.
        # 
        # > * If the storage type of the primary instance is Premium Local SSDs, the read-only instance can use any VPC.
        # > * If the storage type of the primary instance is cloud disks, the VPC of the read-only instance must be the same as that of the primary instance.
        self.vpcid = vpcid
        # The vSwitch ID of the read-only instance. This parameter is required when **InstanceNetworkType** is left empty or set to **VPC**.
        self.v_switch_id = v_switch_id
        # The zone ID. You can call [DescribeRegions](https://help.aliyun.com/document_detail/26243.html) to query the most recent zone list.
        # 
        # - For single-zone deployment, specify one zone ID, such as `cn-hangzhou-b`.
        # - For multi-zone deployment, specify multiple zone IDs separated by colons (:), such as `cn-hangzhou-b:cn-hangzhou-c`.
        # - The number of specified zones must be less than or equal to the number of nodes in the read-only instance. A Basic Edition read-only instance contains only one node. A High-availability Edition read-only instance contains two nodes (one primary node and one secondary node).
        # 
        # This parameter is required.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_create_proxy is not None:
            result['AutoCreateProxy'] = self.auto_create_proxy

        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.auto_use_coupon is not None:
            result['AutoUseCoupon'] = self.auto_use_coupon

        if self.bpe_enabled is not None:
            result['BpeEnabled'] = self.bpe_enabled

        if self.bursting_enabled is not None:
            result['BurstingEnabled'] = self.bursting_enabled

        if self.category is not None:
            result['Category'] = self.category

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.custom_extra_info is not None:
            result['CustomExtraInfo'] = self.custom_extra_info

        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class

        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dbinstance_storage is not None:
            result['DBInstanceStorage'] = self.dbinstance_storage

        if self.dbinstance_storage_type is not None:
            result['DBInstanceStorageType'] = self.dbinstance_storage_type

        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id

        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.gdn_instance_name is not None:
            result['GdnInstanceName'] = self.gdn_instance_name

        if self.instance_network_type is not None:
            result['InstanceNetworkType'] = self.instance_network_type

        if self.instruction_set_arch is not None:
            result['InstructionSetArch'] = self.instruction_set_arch

        if self.io_acceleration_enabled is not None:
            result['IoAccelerationEnabled'] = self.io_acceleration_enabled

        if self.is_analytic_read_only_ins is not None:
            result['IsAnalyticReadOnlyIns'] = self.is_analytic_read_only_ins

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.period is not None:
            result['Period'] = self.period

        if self.port is not None:
            result['Port'] = self.port

        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address

        if self.promotion_code is not None:
            result['PromotionCode'] = self.promotion_code

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.target_dedicated_host_id_for_master is not None:
            result['TargetDedicatedHostIdForMaster'] = self.target_dedicated_host_id_for_master

        if self.tddl_biz_type is not None:
            result['TddlBizType'] = self.tddl_biz_type

        if self.tddl_region_config is not None:
            result['TddlRegionConfig'] = self.tddl_region_config

        if self.used_time is not None:
            result['UsedTime'] = self.used_time

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoCreateProxy') is not None:
            self.auto_create_proxy = m.get('AutoCreateProxy')

        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('AutoUseCoupon') is not None:
            self.auto_use_coupon = m.get('AutoUseCoupon')

        if m.get('BpeEnabled') is not None:
            self.bpe_enabled = m.get('BpeEnabled')

        if m.get('BurstingEnabled') is not None:
            self.bursting_enabled = m.get('BurstingEnabled')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CustomExtraInfo') is not None:
            self.custom_extra_info = m.get('CustomExtraInfo')

        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')

        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DBInstanceStorage') is not None:
            self.dbinstance_storage = m.get('DBInstanceStorage')

        if m.get('DBInstanceStorageType') is not None:
            self.dbinstance_storage_type = m.get('DBInstanceStorageType')

        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')

        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('GdnInstanceName') is not None:
            self.gdn_instance_name = m.get('GdnInstanceName')

        if m.get('InstanceNetworkType') is not None:
            self.instance_network_type = m.get('InstanceNetworkType')

        if m.get('InstructionSetArch') is not None:
            self.instruction_set_arch = m.get('InstructionSetArch')

        if m.get('IoAccelerationEnabled') is not None:
            self.io_acceleration_enabled = m.get('IoAccelerationEnabled')

        if m.get('IsAnalyticReadOnlyIns') is not None:
            self.is_analytic_read_only_ins = m.get('IsAnalyticReadOnlyIns')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')

        if m.get('PromotionCode') is not None:
            self.promotion_code = m.get('PromotionCode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('TargetDedicatedHostIdForMaster') is not None:
            self.target_dedicated_host_id_for_master = m.get('TargetDedicatedHostIdForMaster')

        if m.get('TddlBizType') is not None:
            self.tddl_biz_type = m.get('TddlBizType')

        if m.get('TddlRegionConfig') is not None:
            self.tddl_region_config = m.get('TddlRegionConfig')

        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

