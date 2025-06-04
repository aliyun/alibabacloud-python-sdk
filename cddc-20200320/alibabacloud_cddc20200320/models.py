# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class CreateDedicatedHostRequestMyBaseEcsClass(TeaModel):
    def __init__(
        self,
        amount: int = None,
        auto_renew: bool = None,
        charge_type: str = None,
        data_disk_category: str = None,
        data_disk_count: int = None,
        data_disk_size: int = None,
        depolyment_set_id: str = None,
        ecs_class_code: str = None,
        internet_charge_type: str = None,
        internet_max_bandwidth_out: int = None,
        key_pair_name: str = None,
        password: str = None,
        period: int = None,
        period_type: str = None,
        security_group_ids: List[str] = None,
        system_disk_category: str = None,
        system_disk_size: int = None,
        tags: List[str] = None,
    ):
        # The number of hosts that you want to create.
        self.amount = amount
        # Specifies whether to enable auto-renewal for the host. Default value: false.
        self.auto_renew = auto_renew
        # The billing method. Valid values:
        # 
        # *   PrePaid: subscription.
        # *   PostPaid: pay-as-you-go.
        self.charge_type = charge_type
        # The type of the data disk.
        self.data_disk_category = data_disk_category
        # The number of data disks.
        self.data_disk_count = data_disk_count
        # The size of the data disk. Unit: GB.
        self.data_disk_size = data_disk_size
        # The deployment set ID.
        self.depolyment_set_id = depolyment_set_id
        # The instance type.
        self.ecs_class_code = ecs_class_code
        # The metering method for network usage. Valid values:
        # 
        # *   PayByBandwidth
        # *   PayByTraffic
        self.internet_charge_type = internet_charge_type
        # The maximum outbound public bandwidth. Unit: Mbit/s.
        # 
        # Default value: 0. If you specify the parameter to a value greater than 0, a public IP address is automatically created.
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        # The name of the key pair.
        self.key_pair_name = key_pair_name
        # The password of the host.
        self.password = password
        # The subscription duration of the host. The Period parameter must be specified when ChargeType is set to PrePaid.
        self.period = period
        # The unit of the subscription duration. Default value: Month.
        self.period_type = period_type
        # The IDs of the security groups to which the instance belongs.
        self.security_group_ids = security_group_ids
        # The type of the system disk.
        self.system_disk_category = system_disk_category
        # The size of the system disk. Unit: GB.
        self.system_disk_size = system_disk_size
        # The tags that you want to add to the host.
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.data_disk_category is not None:
            result['DataDiskCategory'] = self.data_disk_category
        if self.data_disk_count is not None:
            result['DataDiskCount'] = self.data_disk_count
        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size
        if self.depolyment_set_id is not None:
            result['DepolymentSetId'] = self.depolyment_set_id
        if self.ecs_class_code is not None:
            result['EcsClassCode'] = self.ecs_class_code
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.internet_max_bandwidth_out is not None:
            result['InternetMaxBandwidthOut'] = self.internet_max_bandwidth_out
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.password is not None:
            result['Password'] = self.password
        if self.period is not None:
            result['Period'] = self.period
        if self.period_type is not None:
            result['PeriodType'] = self.period_type
        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids
        if self.system_disk_category is not None:
            result['SystemDiskCategory'] = self.system_disk_category
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('DataDiskCategory') is not None:
            self.data_disk_category = m.get('DataDiskCategory')
        if m.get('DataDiskCount') is not None:
            self.data_disk_count = m.get('DataDiskCount')
        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')
        if m.get('DepolymentSetId') is not None:
            self.depolyment_set_id = m.get('DepolymentSetId')
        if m.get('EcsClassCode') is not None:
            self.ecs_class_code = m.get('EcsClassCode')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('InternetMaxBandwidthOut') is not None:
            self.internet_max_bandwidth_out = m.get('InternetMaxBandwidthOut')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodType') is not None:
            self.period_type = m.get('PeriodType')
        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')
        if m.get('SystemDiskCategory') is not None:
            self.system_disk_category = m.get('SystemDiskCategory')
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class CreateDedicatedHostRequest(TeaModel):
    def __init__(
        self,
        auto_renew: str = None,
        client_token: str = None,
        cluster_alias: str = None,
        cluster_services: List[str] = None,
        cluster_type: str = None,
        dedicated_host_group_id: str = None,
        host_class: str = None,
        host_storage: str = None,
        host_storage_type: str = None,
        image_category: str = None,
        my_base_ecs_class: CreateDedicatedHostRequestMyBaseEcsClass = None,
        os_password: str = None,
        owner_id: int = None,
        pay_type: str = None,
        period: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        used_time: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # Specifies whether to enable the auto-renewal feature. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        # 
        # >  If you do not specify this parameter, the default value **false** is used.
        self.auto_renew = auto_renew
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        # 
        # This parameter is required.
        self.client_token = client_token
        # The alias of the Self-managed MyBase cluster.
        self.cluster_alias = cluster_alias
        # The services associated with the instances in the Self-managed MyBase on Elastic Compute Service (ECS) cluster.
        self.cluster_services = cluster_services
        # The deployment type of the Self-managed MyBase cluster. Valid values: onACK and onECS.
        self.cluster_type = cluster_type
        # The dedicated cluster ID. You can log on to the ApsaraDB for MyBase console and go to the **Dedicated Clusters** page to view the dedicated cluster ID.
        # 
        # >  The database engine of the host is the same as the database engine of the cluster.
        # 
        # This parameter is required.
        self.dedicated_host_group_id = dedicated_host_group_id
        # The instance type of the host. For information about the host instance types supported by different database engines, see [Instance types of hosts](https://help.aliyun.com/document_detail/206343.html).
        # 
        # This parameter is required.
        self.host_class = host_class
        # The disk storage of the host. This parameter takes effect only for dedicated clusters that run Tair. Unit: GB. Valid values:
        # 
        # *   512
        # *   1024
        # *   1536
        # *   2048
        # *   2560
        # *   3072
        # *   3584
        # *   4096
        self.host_storage = host_storage
        # The disk type of the host. This parameter takes effect only for dedicated clusters that run Tair. Valid values:
        # 
        # *   **cloud_essd**: PL1 enhanced SSD (ESSD).
        # *   **cloud_essd0**: PL0 ESSD.
        self.host_storage_type = host_storage_type
        # The image of the host. Valid values:
        # 
        # *   **WindowsWithMssqlEntAlwaysonLicense**: SQL Server Cluster Edition.
        # *   **WindowsWithMssqlStdLicense**: SQL Server Standard Edition.
        # *   **WindowsWithMssqlEntLicense**: SQL Server Enterprise Edition.
        # *   **WindowsWithMssqlWebLicense**: SQL Server Web Edition.
        # *   **AliLinux**: other images.
        # 
        # >  When you create a host that runs SQL Server, you must specify a host image.
        self.image_category = image_category
        # The parameters of the instances in the Self-managed MyBase on Elastic Compute Service (ECS) cluster.
        self.my_base_ecs_class = my_base_ecs_class
        # The password of the host. You can specify a password only when you create a host in a **Proprietary MyBase** dedicated cluster.
        # 
        # *   The password must be 8 to 30 characters in length.
        # *   The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters.
        # *   The password can contain the following special characters: () \\ \\` ~ ! @ # $ % ^ & \\* - _ + = | { } [ ] : ; \\" < > , . ? /\
        self.os_password = os_password
        self.owner_id = owner_id
        # The billing method of the host. Set the value to **prepaid**.
        # 
        # This parameter is required.
        self.pay_type = pay_type
        # The unit of the subscription duration. Valid values:
        # 
        # *   **Year**\
        # *   **Month**\
        self.period = period
        # The [region ID](https://help.aliyun.com/document_detail/198326.html) of the dedicated cluster.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The subscription duration of the host.
        # 
        # *   Valid values when **Period** is set to **Year**: **1** to **5**.****\
        # *   Valid values when **Period** is set to **Month**: **1** to **9**.
        self.used_time = used_time
        # The vSwitch ID. You can view the vSwitch ID in the Virtual Private Cloud (VPC) console.
        # 
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # The VPC ID of the Self-managed MyBase cluster.
        self.vpc_id = vpc_id
        # The zone ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/214103.html) operation to query the most recent zone list.
        # 
        # This parameter is required.
        self.zone_id = zone_id

    def validate(self):
        if self.my_base_ecs_class:
            self.my_base_ecs_class.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.cluster_alias is not None:
            result['ClusterAlias'] = self.cluster_alias
        if self.cluster_services is not None:
            result['ClusterServices'] = self.cluster_services
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        if self.host_class is not None:
            result['HostClass'] = self.host_class
        if self.host_storage is not None:
            result['HostStorage'] = self.host_storage
        if self.host_storage_type is not None:
            result['HostStorageType'] = self.host_storage_type
        if self.image_category is not None:
            result['ImageCategory'] = self.image_category
        if self.my_base_ecs_class is not None:
            result['MyBaseEcsClass'] = self.my_base_ecs_class.to_map()
        if self.os_password is not None:
            result['OsPassword'] = self.os_password
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.period is not None:
            result['Period'] = self.period
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.used_time is not None:
            result['UsedTime'] = self.used_time
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcID'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ClusterAlias') is not None:
            self.cluster_alias = m.get('ClusterAlias')
        if m.get('ClusterServices') is not None:
            self.cluster_services = m.get('ClusterServices')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        if m.get('HostClass') is not None:
            self.host_class = m.get('HostClass')
        if m.get('HostStorage') is not None:
            self.host_storage = m.get('HostStorage')
        if m.get('HostStorageType') is not None:
            self.host_storage_type = m.get('HostStorageType')
        if m.get('ImageCategory') is not None:
            self.image_category = m.get('ImageCategory')
        if m.get('MyBaseEcsClass') is not None:
            temp_model = CreateDedicatedHostRequestMyBaseEcsClass()
            self.my_base_ecs_class = temp_model.from_map(m['MyBaseEcsClass'])
        if m.get('OsPassword') is not None:
            self.os_password = m.get('OsPassword')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcID') is not None:
            self.vpc_id = m.get('VpcID')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateDedicatedHostShrinkRequest(TeaModel):
    def __init__(
        self,
        auto_renew: str = None,
        client_token: str = None,
        cluster_alias: str = None,
        cluster_services_shrink: str = None,
        cluster_type: str = None,
        dedicated_host_group_id: str = None,
        host_class: str = None,
        host_storage: str = None,
        host_storage_type: str = None,
        image_category: str = None,
        my_base_ecs_class_shrink: str = None,
        os_password: str = None,
        owner_id: int = None,
        pay_type: str = None,
        period: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        used_time: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # Specifies whether to enable the auto-renewal feature. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        # 
        # >  If you do not specify this parameter, the default value **false** is used.
        self.auto_renew = auto_renew
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        # 
        # This parameter is required.
        self.client_token = client_token
        # The alias of the Self-managed MyBase cluster.
        self.cluster_alias = cluster_alias
        # The services associated with the instances in the Self-managed MyBase on Elastic Compute Service (ECS) cluster.
        self.cluster_services_shrink = cluster_services_shrink
        # The deployment type of the Self-managed MyBase cluster. Valid values: onACK and onECS.
        self.cluster_type = cluster_type
        # The dedicated cluster ID. You can log on to the ApsaraDB for MyBase console and go to the **Dedicated Clusters** page to view the dedicated cluster ID.
        # 
        # >  The database engine of the host is the same as the database engine of the cluster.
        # 
        # This parameter is required.
        self.dedicated_host_group_id = dedicated_host_group_id
        # The instance type of the host. For information about the host instance types supported by different database engines, see [Instance types of hosts](https://help.aliyun.com/document_detail/206343.html).
        # 
        # This parameter is required.
        self.host_class = host_class
        # The disk storage of the host. This parameter takes effect only for dedicated clusters that run Tair. Unit: GB. Valid values:
        # 
        # *   512
        # *   1024
        # *   1536
        # *   2048
        # *   2560
        # *   3072
        # *   3584
        # *   4096
        self.host_storage = host_storage
        # The disk type of the host. This parameter takes effect only for dedicated clusters that run Tair. Valid values:
        # 
        # *   **cloud_essd**: PL1 enhanced SSD (ESSD).
        # *   **cloud_essd0**: PL0 ESSD.
        self.host_storage_type = host_storage_type
        # The image of the host. Valid values:
        # 
        # *   **WindowsWithMssqlEntAlwaysonLicense**: SQL Server Cluster Edition.
        # *   **WindowsWithMssqlStdLicense**: SQL Server Standard Edition.
        # *   **WindowsWithMssqlEntLicense**: SQL Server Enterprise Edition.
        # *   **WindowsWithMssqlWebLicense**: SQL Server Web Edition.
        # *   **AliLinux**: other images.
        # 
        # >  When you create a host that runs SQL Server, you must specify a host image.
        self.image_category = image_category
        # The parameters of the instances in the Self-managed MyBase on Elastic Compute Service (ECS) cluster.
        self.my_base_ecs_class_shrink = my_base_ecs_class_shrink
        # The password of the host. You can specify a password only when you create a host in a **Proprietary MyBase** dedicated cluster.
        # 
        # *   The password must be 8 to 30 characters in length.
        # *   The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters.
        # *   The password can contain the following special characters: () \\ \\` ~ ! @ # $ % ^ & \\* - _ + = | { } [ ] : ; \\" < > , . ? /\
        self.os_password = os_password
        self.owner_id = owner_id
        # The billing method of the host. Set the value to **prepaid**.
        # 
        # This parameter is required.
        self.pay_type = pay_type
        # The unit of the subscription duration. Valid values:
        # 
        # *   **Year**\
        # *   **Month**\
        self.period = period
        # The [region ID](https://help.aliyun.com/document_detail/198326.html) of the dedicated cluster.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The subscription duration of the host.
        # 
        # *   Valid values when **Period** is set to **Year**: **1** to **5**.****\
        # *   Valid values when **Period** is set to **Month**: **1** to **9**.
        self.used_time = used_time
        # The vSwitch ID. You can view the vSwitch ID in the Virtual Private Cloud (VPC) console.
        # 
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # The VPC ID of the Self-managed MyBase cluster.
        self.vpc_id = vpc_id
        # The zone ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/214103.html) operation to query the most recent zone list.
        # 
        # This parameter is required.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.cluster_alias is not None:
            result['ClusterAlias'] = self.cluster_alias
        if self.cluster_services_shrink is not None:
            result['ClusterServices'] = self.cluster_services_shrink
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        if self.host_class is not None:
            result['HostClass'] = self.host_class
        if self.host_storage is not None:
            result['HostStorage'] = self.host_storage
        if self.host_storage_type is not None:
            result['HostStorageType'] = self.host_storage_type
        if self.image_category is not None:
            result['ImageCategory'] = self.image_category
        if self.my_base_ecs_class_shrink is not None:
            result['MyBaseEcsClass'] = self.my_base_ecs_class_shrink
        if self.os_password is not None:
            result['OsPassword'] = self.os_password
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.period is not None:
            result['Period'] = self.period
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.used_time is not None:
            result['UsedTime'] = self.used_time
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcID'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ClusterAlias') is not None:
            self.cluster_alias = m.get('ClusterAlias')
        if m.get('ClusterServices') is not None:
            self.cluster_services_shrink = m.get('ClusterServices')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        if m.get('HostClass') is not None:
            self.host_class = m.get('HostClass')
        if m.get('HostStorage') is not None:
            self.host_storage = m.get('HostStorage')
        if m.get('HostStorageType') is not None:
            self.host_storage_type = m.get('HostStorageType')
        if m.get('ImageCategory') is not None:
            self.image_category = m.get('ImageCategory')
        if m.get('MyBaseEcsClass') is not None:
            self.my_base_ecs_class_shrink = m.get('MyBaseEcsClass')
        if m.get('OsPassword') is not None:
            self.os_password = m.get('OsPassword')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcID') is not None:
            self.vpc_id = m.get('VpcID')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateDedicatedHostResponseBodyDedicateHostListDedicateHostList(TeaModel):
    def __init__(
        self,
        dedicated_host_id: str = None,
    ):
        # The ID of the created host.
        self.dedicated_host_id = dedicated_host_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        return self


class CreateDedicatedHostResponseBodyDedicateHostList(TeaModel):
    def __init__(
        self,
        dedicate_host_list: List[CreateDedicatedHostResponseBodyDedicateHostListDedicateHostList] = None,
    ):
        self.dedicate_host_list = dedicate_host_list

    def validate(self):
        if self.dedicate_host_list:
            for k in self.dedicate_host_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DedicateHostList'] = []
        if self.dedicate_host_list is not None:
            for k in self.dedicate_host_list:
                result['DedicateHostList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dedicate_host_list = []
        if m.get('DedicateHostList') is not None:
            for k in m.get('DedicateHostList'):
                temp_model = CreateDedicatedHostResponseBodyDedicateHostListDedicateHostList()
                self.dedicate_host_list.append(temp_model.from_map(k))
        return self


class CreateDedicatedHostResponseBody(TeaModel):
    def __init__(
        self,
        cluster_name: str = None,
        dedicate_host_list: CreateDedicatedHostResponseBodyDedicateHostList = None,
        order_id: int = None,
        request_id: str = None,
    ):
        # The name of the cluster.
        self.cluster_name = cluster_name
        # The created hosts.
        self.dedicate_host_list = dedicate_host_list
        # The order ID.
        self.order_id = order_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.dedicate_host_list:
            self.dedicate_host_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.dedicate_host_list is not None:
            result['DedicateHostList'] = self.dedicate_host_list.to_map()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('DedicateHostList') is not None:
            temp_model = CreateDedicatedHostResponseBodyDedicateHostList()
            self.dedicate_host_list = temp_model.from_map(m['DedicateHostList'])
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDedicatedHostResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDedicatedHostResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateDedicatedHostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDedicatedHostAccountRequest(TeaModel):
    def __init__(
        self,
        account_name: str = None,
        account_password: str = None,
        account_type: str = None,
        bastion_instance_id: str = None,
        client_token: str = None,
        dedicated_host_id: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The name of the host account.
        # 
        # *   The name must be 2 to 16 characters in length.
        # *   The name must start with a lowercase letter and end with a lowercase letter or a digit.
        # *   The name can contain lowercase letters, digits, and underscores (_).
        # 
        # This parameter is required.
        self.account_name = account_name
        # The password of the host account.
        # 
        # *   The password must be 6 to 32 characters in length.
        # *   The password must contain three of the following character types: upper letters, lower letters, digits, and special characters.
        # *   The password can contain the following special characters: `! @ # $ % ^ & * ( ) _ + - =`
        # 
        # >  If your host runs SQL Server, the password cannot contain the account name (case-insensitive).
        # 
        # This parameter is required.
        self.account_password = account_password
        # The type of the host account. Valid values:
        # 
        # *   **Normal**: standard account.
        # *   **Admin**: administrator account.
        # 
        # For more information, see [Host permissions](https://help.aliyun.com/document_detail/176240.html).
        self.account_type = account_type
        # The ID of the bastion host with which the host is associated. You can log on to the ApsaraDB for MyBase console and go to the **Bastion Hosts** page to view the bastion host ID.
        self.bastion_instance_id = bastion_instance_id
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The host ID. You can call the [DescribeDedicatedHosts](https://help.aliyun.com/document_detail/200944.html) operation to query the host ID.
        # 
        # This parameter is required.
        self.dedicated_host_id = dedicated_host_id
        self.owner_id = owner_id
        # The region ID of the host. You can call the [DescribeDedicatedHostAttribute](https://help.aliyun.com/document_detail/213010.html) operation to query the region ID.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_password is not None:
            result['AccountPassword'] = self.account_password
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.bastion_instance_id is not None:
            result['BastionInstanceId'] = self.bastion_instance_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
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
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('BastionInstanceId') is not None:
            self.bastion_instance_id = m.get('BastionInstanceId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CreateDedicatedHostAccountResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDedicatedHostAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDedicatedHostAccountResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateDedicatedHostAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDedicatedHostGroupRequest(TeaModel):
    def __init__(
        self,
        allocation_policy: str = None,
        client_token: str = None,
        cpu_allocation_ratio: int = None,
        dedicated_host_group_desc: str = None,
        disk_allocation_ratio: int = None,
        engine: str = None,
        host_replace_policy: str = None,
        mem_allocation_ratio: int = None,
        open_permission: int = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        vpcid: str = None,
    ):
        # The policy that is used to allocate resources in the dedicated cluster. Valid values:
        # 
        # *   **Evenly** (default): The system preferentially deploys database instances on the hosts where no resources or fewer resources are allocated. This maximizes system stability.
        # *   **Intensively**: The system preferentially deploys database instances on the hosts that are created earlier and have more allocated resources. This maximizes resource utilization.
        self.allocation_policy = allocation_policy
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        # 
        # This parameter is required.
        self.client_token = client_token
        # The CPU overcommit ratio of the dedicated cluster.
        # 
        # >  Unit: %. Valid values: **100** to **300**. Default value: **200**, which specifies that the total amount of CPU resources allocated to all instances is twice the amount of actual CPU resources. This helps you maximize CPU utilization.
        self.cpu_allocation_ratio = cpu_allocation_ratio
        # The name of the dedicated cluster. The name must be 1 to 64 characters in length and can contain letters, digits, underscores (_), and hyphens (-). The name must start with a letter.
        self.dedicated_host_group_desc = dedicated_host_group_desc
        # The storage overcommit ratio of the dedicated cluster.
        # 
        # >  Unit: %. Valid values: **100** to **300**. Default value: **200**, which specifies that the total amount of storage resources allocated to all instances is twice the amount of actual storage resources. This helps you maximize storage usage. This parameter does not take effect for dedicated clusters that run SQL Server.
        self.disk_allocation_ratio = disk_allocation_ratio
        # The database engine of the dedicated cluster. Valid values:
        # 
        # *   **MySQL**\
        # *   **SQL Server**\
        # 
        # This parameter is required.
        self.engine = engine
        # The policy that is used to handle host failures. Valid values:
        # 
        # *   **Auto** (default): The system automatically replaces faulty hosts.
        # *   **Manual**: You must manually replace faulty hosts.
        # 
        # >  When you create a dedicated cluster that runs **MySQL**, you can select a policy based on your business requirements. For dedicated clusters that run other database engines, the default value **Auto** is used.
        self.host_replace_policy = host_replace_policy
        # The maximum memory usage of each host in the dedicated cluster.
        # 
        # >  Unit: %. Valid values: **0** to **100**. Default value: **100**.
        self.mem_allocation_ratio = mem_allocation_ratio
        # Specifies whether to grant the host OS permissions. Valid values:
        # 
        # *   **0**: no.
        # *   **1**: yes.
        # 
        # >  When you create a dedicated cluster that runs **MySQL or SQL Server**, you can grant the host OS permissions based on your business requirements. For dedicated clusters that run other database engines, the default value **0** is used. When you create an ApsaraDB MyBase for SQL Server dedicated cluster, you must set this parameter to 1.
        self.open_permission = open_permission
        self.owner_id = owner_id
        # The region ID. For more information, see [Region IDs](https://help.aliyun.com/document_detail/198326.html).
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the virtual private cloud (VPC) where you want to create the dedicated cluster. You can log on to the VPC console and click **VPCs** in the left-side navigation pane to view the VPC ID.
        # 
        # This parameter is required.
        self.vpcid = vpcid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allocation_policy is not None:
            result['AllocationPolicy'] = self.allocation_policy
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.cpu_allocation_ratio is not None:
            result['CpuAllocationRatio'] = self.cpu_allocation_ratio
        if self.dedicated_host_group_desc is not None:
            result['DedicatedHostGroupDesc'] = self.dedicated_host_group_desc
        if self.disk_allocation_ratio is not None:
            result['DiskAllocationRatio'] = self.disk_allocation_ratio
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.host_replace_policy is not None:
            result['HostReplacePolicy'] = self.host_replace_policy
        if self.mem_allocation_ratio is not None:
            result['MemAllocationRatio'] = self.mem_allocation_ratio
        if self.open_permission is not None:
            result['OpenPermission'] = self.open_permission
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationPolicy') is not None:
            self.allocation_policy = m.get('AllocationPolicy')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CpuAllocationRatio') is not None:
            self.cpu_allocation_ratio = m.get('CpuAllocationRatio')
        if m.get('DedicatedHostGroupDesc') is not None:
            self.dedicated_host_group_desc = m.get('DedicatedHostGroupDesc')
        if m.get('DiskAllocationRatio') is not None:
            self.disk_allocation_ratio = m.get('DiskAllocationRatio')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('HostReplacePolicy') is not None:
            self.host_replace_policy = m.get('HostReplacePolicy')
        if m.get('MemAllocationRatio') is not None:
            self.mem_allocation_ratio = m.get('MemAllocationRatio')
        if m.get('OpenPermission') is not None:
            self.open_permission = m.get('OpenPermission')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        return self


class CreateDedicatedHostGroupResponseBody(TeaModel):
    def __init__(
        self,
        dedicated_host_group_id: str = None,
        request_id: str = None,
    ):
        # The dedicated cluster ID.
        self.dedicated_host_group_id = dedicated_host_group_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDedicatedHostGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDedicatedHostGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateDedicatedHostGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMyBaseRequestECSClassList(TeaModel):
    def __init__(
        self,
        data_disk_auto_snapshot_policy_id: str = None,
        data_disk_encrypted: bool = None,
        data_disk_kmskey_id: str = None,
        data_disk_performance_level: str = None,
        disk_capacity: int = None,
        disk_count: int = None,
        disk_type: str = None,
        instance_type: str = None,
        node_count: int = None,
        sys_disk_auto_snapshot_policy_id: str = None,
        sys_disk_capacity: int = None,
        sys_disk_encrypted: bool = None,
        sys_disk_kmskey_id: str = None,
        sys_disk_type: str = None,
        system_disk_performance_level: str = None,
    ):
        self.data_disk_auto_snapshot_policy_id = data_disk_auto_snapshot_policy_id
        self.data_disk_encrypted = data_disk_encrypted
        self.data_disk_kmskey_id = data_disk_kmskey_id
        self.data_disk_performance_level = data_disk_performance_level
        self.disk_capacity = disk_capacity
        self.disk_count = disk_count
        self.disk_type = disk_type
        # This parameter is required.
        self.instance_type = instance_type
        # This parameter is required.
        self.node_count = node_count
        self.sys_disk_auto_snapshot_policy_id = sys_disk_auto_snapshot_policy_id
        # This parameter is required.
        self.sys_disk_capacity = sys_disk_capacity
        self.sys_disk_encrypted = sys_disk_encrypted
        self.sys_disk_kmskey_id = sys_disk_kmskey_id
        # This parameter is required.
        self.sys_disk_type = sys_disk_type
        self.system_disk_performance_level = system_disk_performance_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_disk_auto_snapshot_policy_id is not None:
            result['dataDiskAutoSnapshotPolicyId'] = self.data_disk_auto_snapshot_policy_id
        if self.data_disk_encrypted is not None:
            result['dataDiskEncrypted'] = self.data_disk_encrypted
        if self.data_disk_kmskey_id is not None:
            result['dataDiskKMSKeyId'] = self.data_disk_kmskey_id
        if self.data_disk_performance_level is not None:
            result['dataDiskPerformanceLevel'] = self.data_disk_performance_level
        if self.disk_capacity is not None:
            result['diskCapacity'] = self.disk_capacity
        if self.disk_count is not None:
            result['diskCount'] = self.disk_count
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.node_count is not None:
            result['nodeCount'] = self.node_count
        if self.sys_disk_auto_snapshot_policy_id is not None:
            result['sysDiskAutoSnapshotPolicyId'] = self.sys_disk_auto_snapshot_policy_id
        if self.sys_disk_capacity is not None:
            result['sysDiskCapacity'] = self.sys_disk_capacity
        if self.sys_disk_encrypted is not None:
            result['sysDiskEncrypted'] = self.sys_disk_encrypted
        if self.sys_disk_kmskey_id is not None:
            result['sysDiskKMSKeyId'] = self.sys_disk_kmskey_id
        if self.sys_disk_type is not None:
            result['sysDiskType'] = self.sys_disk_type
        if self.system_disk_performance_level is not None:
            result['systemDiskPerformanceLevel'] = self.system_disk_performance_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataDiskAutoSnapshotPolicyId') is not None:
            self.data_disk_auto_snapshot_policy_id = m.get('dataDiskAutoSnapshotPolicyId')
        if m.get('dataDiskEncrypted') is not None:
            self.data_disk_encrypted = m.get('dataDiskEncrypted')
        if m.get('dataDiskKMSKeyId') is not None:
            self.data_disk_kmskey_id = m.get('dataDiskKMSKeyId')
        if m.get('dataDiskPerformanceLevel') is not None:
            self.data_disk_performance_level = m.get('dataDiskPerformanceLevel')
        if m.get('diskCapacity') is not None:
            self.disk_capacity = m.get('diskCapacity')
        if m.get('diskCount') is not None:
            self.disk_count = m.get('diskCount')
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('nodeCount') is not None:
            self.node_count = m.get('nodeCount')
        if m.get('sysDiskAutoSnapshotPolicyId') is not None:
            self.sys_disk_auto_snapshot_policy_id = m.get('sysDiskAutoSnapshotPolicyId')
        if m.get('sysDiskCapacity') is not None:
            self.sys_disk_capacity = m.get('sysDiskCapacity')
        if m.get('sysDiskEncrypted') is not None:
            self.sys_disk_encrypted = m.get('sysDiskEncrypted')
        if m.get('sysDiskKMSKeyId') is not None:
            self.sys_disk_kmskey_id = m.get('sysDiskKMSKeyId')
        if m.get('sysDiskType') is not None:
            self.sys_disk_type = m.get('sysDiskType')
        if m.get('systemDiskPerformanceLevel') is not None:
            self.system_disk_performance_level = m.get('systemDiskPerformanceLevel')
        return self


class CreateMyBaseRequestTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateMyBaseRequest(TeaModel):
    def __init__(
        self,
        auto_pay: bool = None,
        auto_renew: str = None,
        client_token: str = None,
        dedicated_host_group_description: str = None,
        dedicated_host_group_id: str = None,
        ecsclass_list: List[CreateMyBaseRequestECSClassList] = None,
        ecs_deployment_set_id: str = None,
        ecs_host_name: str = None,
        ecs_instance_name: str = None,
        ecs_unique_suffix: str = None,
        engine: str = None,
        image_id: str = None,
        internet_charge_type: str = None,
        internet_max_bandwidth_out: int = None,
        key_pair_name: str = None,
        os_password: str = None,
        owner_id: int = None,
        password_inherit: str = None,
        pay_type: str = None,
        period: str = None,
        period_type: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_group_id: str = None,
        tags: List[CreateMyBaseRequestTags] = None,
        user_data: str = None,
        user_data_in_base_64: bool = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        self.auto_pay = auto_pay
        self.auto_renew = auto_renew
        self.client_token = client_token
        self.dedicated_host_group_description = dedicated_host_group_description
        self.dedicated_host_group_id = dedicated_host_group_id
        # This parameter is required.
        self.ecsclass_list = ecsclass_list
        self.ecs_deployment_set_id = ecs_deployment_set_id
        self.ecs_host_name = ecs_host_name
        self.ecs_instance_name = ecs_instance_name
        self.ecs_unique_suffix = ecs_unique_suffix
        # This parameter is required.
        self.engine = engine
        self.image_id = image_id
        self.internet_charge_type = internet_charge_type
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        self.key_pair_name = key_pair_name
        self.os_password = os_password
        self.owner_id = owner_id
        self.password_inherit = password_inherit
        # This parameter is required.
        self.pay_type = pay_type
        self.period = period
        self.period_type = period_type
        # This parameter is required.
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # This parameter is required.
        self.security_group_id = security_group_id
        self.tags = tags
        self.user_data = user_data
        self.user_data_in_base_64 = user_data_in_base_64
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # This parameter is required.
        self.vpc_id = vpc_id
        # This parameter is required.
        self.zone_id = zone_id

    def validate(self):
        if self.ecsclass_list:
            for k in self.ecsclass_list:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dedicated_host_group_description is not None:
            result['DedicatedHostGroupDescription'] = self.dedicated_host_group_description
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        result['ECSClassList'] = []
        if self.ecsclass_list is not None:
            for k in self.ecsclass_list:
                result['ECSClassList'].append(k.to_map() if k else None)
        if self.ecs_deployment_set_id is not None:
            result['EcsDeploymentSetId'] = self.ecs_deployment_set_id
        if self.ecs_host_name is not None:
            result['EcsHostName'] = self.ecs_host_name
        if self.ecs_instance_name is not None:
            result['EcsInstanceName'] = self.ecs_instance_name
        if self.ecs_unique_suffix is not None:
            result['EcsUniqueSuffix'] = self.ecs_unique_suffix
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.internet_max_bandwidth_out is not None:
            result['InternetMaxBandwidthOut'] = self.internet_max_bandwidth_out
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.os_password is not None:
            result['OsPassword'] = self.os_password
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.password_inherit is not None:
            result['PasswordInherit'] = self.password_inherit
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.period is not None:
            result['Period'] = self.period
        if self.period_type is not None:
            result['PeriodType'] = self.period_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.user_data_in_base_64 is not None:
            result['UserDataInBase64'] = self.user_data_in_base_64
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
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DedicatedHostGroupDescription') is not None:
            self.dedicated_host_group_description = m.get('DedicatedHostGroupDescription')
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        self.ecsclass_list = []
        if m.get('ECSClassList') is not None:
            for k in m.get('ECSClassList'):
                temp_model = CreateMyBaseRequestECSClassList()
                self.ecsclass_list.append(temp_model.from_map(k))
        if m.get('EcsDeploymentSetId') is not None:
            self.ecs_deployment_set_id = m.get('EcsDeploymentSetId')
        if m.get('EcsHostName') is not None:
            self.ecs_host_name = m.get('EcsHostName')
        if m.get('EcsInstanceName') is not None:
            self.ecs_instance_name = m.get('EcsInstanceName')
        if m.get('EcsUniqueSuffix') is not None:
            self.ecs_unique_suffix = m.get('EcsUniqueSuffix')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('InternetMaxBandwidthOut') is not None:
            self.internet_max_bandwidth_out = m.get('InternetMaxBandwidthOut')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('OsPassword') is not None:
            self.os_password = m.get('OsPassword')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PasswordInherit') is not None:
            self.password_inherit = m.get('PasswordInherit')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodType') is not None:
            self.period_type = m.get('PeriodType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = CreateMyBaseRequestTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('UserDataInBase64') is not None:
            self.user_data_in_base_64 = m.get('UserDataInBase64')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateMyBaseShrinkRequest(TeaModel):
    def __init__(
        self,
        auto_pay: bool = None,
        auto_renew: str = None,
        client_token: str = None,
        dedicated_host_group_description: str = None,
        dedicated_host_group_id: str = None,
        ecsclass_list_shrink: str = None,
        ecs_deployment_set_id: str = None,
        ecs_host_name: str = None,
        ecs_instance_name: str = None,
        ecs_unique_suffix: str = None,
        engine: str = None,
        image_id: str = None,
        internet_charge_type: str = None,
        internet_max_bandwidth_out: int = None,
        key_pair_name: str = None,
        os_password: str = None,
        owner_id: int = None,
        password_inherit: str = None,
        pay_type: str = None,
        period: str = None,
        period_type: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_group_id: str = None,
        tags_shrink: str = None,
        user_data: str = None,
        user_data_in_base_64: bool = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        self.auto_pay = auto_pay
        self.auto_renew = auto_renew
        self.client_token = client_token
        self.dedicated_host_group_description = dedicated_host_group_description
        self.dedicated_host_group_id = dedicated_host_group_id
        # This parameter is required.
        self.ecsclass_list_shrink = ecsclass_list_shrink
        self.ecs_deployment_set_id = ecs_deployment_set_id
        self.ecs_host_name = ecs_host_name
        self.ecs_instance_name = ecs_instance_name
        self.ecs_unique_suffix = ecs_unique_suffix
        # This parameter is required.
        self.engine = engine
        self.image_id = image_id
        self.internet_charge_type = internet_charge_type
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        self.key_pair_name = key_pair_name
        self.os_password = os_password
        self.owner_id = owner_id
        self.password_inherit = password_inherit
        # This parameter is required.
        self.pay_type = pay_type
        self.period = period
        self.period_type = period_type
        # This parameter is required.
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # This parameter is required.
        self.security_group_id = security_group_id
        self.tags_shrink = tags_shrink
        self.user_data = user_data
        self.user_data_in_base_64 = user_data_in_base_64
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # This parameter is required.
        self.vpc_id = vpc_id
        # This parameter is required.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dedicated_host_group_description is not None:
            result['DedicatedHostGroupDescription'] = self.dedicated_host_group_description
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        if self.ecsclass_list_shrink is not None:
            result['ECSClassList'] = self.ecsclass_list_shrink
        if self.ecs_deployment_set_id is not None:
            result['EcsDeploymentSetId'] = self.ecs_deployment_set_id
        if self.ecs_host_name is not None:
            result['EcsHostName'] = self.ecs_host_name
        if self.ecs_instance_name is not None:
            result['EcsInstanceName'] = self.ecs_instance_name
        if self.ecs_unique_suffix is not None:
            result['EcsUniqueSuffix'] = self.ecs_unique_suffix
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.internet_max_bandwidth_out is not None:
            result['InternetMaxBandwidthOut'] = self.internet_max_bandwidth_out
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.os_password is not None:
            result['OsPassword'] = self.os_password
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.password_inherit is not None:
            result['PasswordInherit'] = self.password_inherit
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.period is not None:
            result['Period'] = self.period
        if self.period_type is not None:
            result['PeriodType'] = self.period_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.user_data_in_base_64 is not None:
            result['UserDataInBase64'] = self.user_data_in_base_64
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
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DedicatedHostGroupDescription') is not None:
            self.dedicated_host_group_description = m.get('DedicatedHostGroupDescription')
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        if m.get('ECSClassList') is not None:
            self.ecsclass_list_shrink = m.get('ECSClassList')
        if m.get('EcsDeploymentSetId') is not None:
            self.ecs_deployment_set_id = m.get('EcsDeploymentSetId')
        if m.get('EcsHostName') is not None:
            self.ecs_host_name = m.get('EcsHostName')
        if m.get('EcsInstanceName') is not None:
            self.ecs_instance_name = m.get('EcsInstanceName')
        if m.get('EcsUniqueSuffix') is not None:
            self.ecs_unique_suffix = m.get('EcsUniqueSuffix')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('InternetMaxBandwidthOut') is not None:
            self.internet_max_bandwidth_out = m.get('InternetMaxBandwidthOut')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('OsPassword') is not None:
            self.os_password = m.get('OsPassword')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PasswordInherit') is not None:
            self.password_inherit = m.get('PasswordInherit')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodType') is not None:
            self.period_type = m.get('PeriodType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('UserDataInBase64') is not None:
            self.user_data_in_base_64 = m.get('UserDataInBase64')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateMyBaseResponseBodyOrderListOrderList(TeaModel):
    def __init__(
        self,
        create_timestamp: int = None,
        dedicated_host_group_name: str = None,
        ecsinstance_ids: str = None,
        order_id: str = None,
    ):
        self.create_timestamp = create_timestamp
        self.dedicated_host_group_name = dedicated_host_group_name
        self.ecsinstance_ids = ecsinstance_ids
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        if self.dedicated_host_group_name is not None:
            result['DedicatedHostGroupName'] = self.dedicated_host_group_name
        if self.ecsinstance_ids is not None:
            result['ECSInstanceIds'] = self.ecsinstance_ids
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        if m.get('DedicatedHostGroupName') is not None:
            self.dedicated_host_group_name = m.get('DedicatedHostGroupName')
        if m.get('ECSInstanceIds') is not None:
            self.ecsinstance_ids = m.get('ECSInstanceIds')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class CreateMyBaseResponseBodyOrderList(TeaModel):
    def __init__(
        self,
        order_list: List[CreateMyBaseResponseBodyOrderListOrderList] = None,
    ):
        self.order_list = order_list

    def validate(self):
        if self.order_list:
            for k in self.order_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OrderList'] = []
        if self.order_list is not None:
            for k in self.order_list:
                result['OrderList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.order_list = []
        if m.get('OrderList') is not None:
            for k in m.get('OrderList'):
                temp_model = CreateMyBaseResponseBodyOrderListOrderList()
                self.order_list.append(temp_model.from_map(k))
        return self


class CreateMyBaseResponseBody(TeaModel):
    def __init__(
        self,
        order_list: CreateMyBaseResponseBodyOrderList = None,
        request_id: str = None,
    ):
        self.order_list = order_list
        self.request_id = request_id

    def validate(self):
        if self.order_list:
            self.order_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_list is not None:
            result['OrderList'] = self.order_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderList') is not None:
            temp_model = CreateMyBaseResponseBodyOrderList()
            self.order_list = temp_model.from_map(m['OrderList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateMyBaseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateMyBaseResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateMyBaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDedicatedHostAccountRequest(TeaModel):
    def __init__(
        self,
        account_name: str = None,
        dedicated_host_id: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The name of the host account.
        # 
        # *   The name can contain lowercase letters, digits, and underscores (_).
        # *   The name must start with a lowercase letter and end with a lowercase letter or a digit.
        # *   The name must be 2 to 16 characters in length.
        # 
        # This parameter is required.
        self.account_name = account_name
        # The host ID. You can call the [DescribeDedicatedHosts](https://help.aliyun.com/document_detail/200944.html) operation to query the host ID.
        # 
        # This parameter is required.
        self.dedicated_host_id = dedicated_host_id
        # The ID of the account to which the AccessKey pair belongs.
        self.owner_id = owner_id
        # The region ID of the host. You can call the [DescribeDedicatedHostAttribute](https://help.aliyun.com/document_detail/213010.html) operation to query the region ID.
        self.region_id = region_id
        # ResourceOwnerAccount
        self.resource_owner_account = resource_owner_account
        # The ID of the asset owner.
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
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
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteDedicatedHostAccountResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDedicatedHostAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDedicatedHostAccountResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteDedicatedHostAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDedicatedHostGroupRequest(TeaModel):
    def __init__(
        self,
        dedicated_host_group_id: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The dedicated cluster ID. You can log on to the ApsaraDB for MyBase console and go to the Dedicated Clusters page to view the dedicated cluster ID.
        # 
        # This parameter is required.
        self.dedicated_host_group_id = dedicated_host_group_id
        # 账号ID。
        self.owner_id = owner_id
        # The region ID of the dedicated cluster. For more information, see [Region IDs](https://help.aliyun.com/document_detail/198326.html).
        self.region_id = region_id
        # 资源主账号的账号名称。
        self.resource_owner_account = resource_owner_account
        # The ID of the asset owner.
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
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
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteDedicatedHostGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDedicatedHostGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDedicatedHostGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteDedicatedHostGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDedicatedHostAttributeRequest(TeaModel):
    def __init__(
        self,
        dedicated_host_group_id: str = None,
        dedicated_host_id: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the dedicated cluster in which the host is created. You can log on to the ApsaraDB for MyBase console and go to the **Dedicated Clusters** page to view the dedicated cluster ID.
        # 
        # This parameter is required.
        self.dedicated_host_group_id = dedicated_host_group_id
        # The host ID. You can log on to the ApsaraDB for MyBase console and go to the **Hosts** page to view the host ID.
        # 
        # This parameter is required.
        self.dedicated_host_id = dedicated_host_id
        self.owner_id = owner_id
        # [The region ID](https://help.aliyun.com/document_detail/198326.html).
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
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
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeDedicatedHostAttributeResponseBody(TeaModel):
    def __init__(
        self,
        account_name: str = None,
        account_type: str = None,
        allocation_status: str = None,
        auto_renew: str = None,
        cpuallocation_ratio: str = None,
        cpu_used: str = None,
        created_time: str = None,
        dedicated_host_group_id: str = None,
        dedicated_host_id: str = None,
        disk_allocation_ratio: str = None,
        distribution_tag: str = None,
        ecs_class_code: str = None,
        expired_time: str = None,
        host_cpu: int = None,
        host_class: str = None,
        host_mem: int = None,
        host_name: str = None,
        host_status: str = None,
        host_storage: int = None,
        host_type: str = None,
        ipaddress: str = None,
        image_category: str = None,
        instance_number: int = None,
        instance_number_master: int = None,
        instance_number_romaster: int = None,
        instance_number_roslave: int = None,
        instance_number_slave: int = None,
        mem_allocation_ratio: str = None,
        memory_used: str = None,
        open_permission: str = None,
        region_id: str = None,
        request_id: str = None,
        storage_used: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        # The account name of the host.
        # 
        # *   The name can contain lowercase letters, digits, and underscores (_).
        # *   The name must start with a lowercase letter and end with a lowercase letter or a digit.
        # *   The name must be 2 to 16 characters in length.
        self.account_name = account_name
        # The account type of the host. Valid values:
        # 
        # *   **Normal**: standard account.
        # *   **Admin**: administrator account.
        self.account_type = account_type
        # Indicates whether instances can be deployed on the host. Valid values:
        # 
        # *   **Allocatable**: yes.
        # *   **Suspended**: no.
        self.allocation_status = allocation_status
        # Indicates whether auto-renewal is enabled on the host. Valid values:
        # 
        # *   **true**\
        # *   **false** (default)
        self.auto_renew = auto_renew
        # The CPU overcommit ratio of the dedicated cluster. Unit: %. The value is accurate to the tens digit.
        self.cpuallocation_ratio = cpuallocation_ratio
        # The number of CPU cores used by the host.
        self.cpu_used = cpu_used
        # The time when the host was created. The time follows the ISO 8601 standard in the **yyyy-MM-ddTHH:mm:ssZ** format. The time is displayed in UTC.
        self.created_time = created_time
        # The ID of the dedicated cluster in which the host is created.
        self.dedicated_host_group_id = dedicated_host_group_id
        # The host ID.
        self.dedicated_host_id = dedicated_host_id
        # The storage overcommit ratio of the dedicated cluster.
        self.disk_allocation_ratio = disk_allocation_ratio
        # The distribution tag of the host.
        self.distribution_tag = distribution_tag
        # The instance type of the Elastic Compute Service (ECS) instance.
        self.ecs_class_code = ecs_class_code
        # The expiration time of the host. The time follows the ISO 8601 standard in the **yyyy-MM-ddTHH:mm:ssZ** format. The time is displayed in UTC.
        self.expired_time = expired_time
        # The number of CPU cores of the host.
        self.host_cpu = host_cpu
        # The instance type of the host.
        self.host_class = host_class
        # The memory size of the host. Unit: MB.
        self.host_mem = host_mem
        # The name of the host.
        self.host_name = host_name
        # The state of the host. Valid values:
        # 
        # *   **0**: The host is being created.
        # *   **1**: The host is running.
        # *   **2**: The host is faulty.
        # *   **3**: The host is ready for disabling.
        # *   **4**: The host is being maintained.
        # *   **5**: The host is disabled.
        # *   **6**: The host is restarting.
        # *   **7**: The host is locked.
        # 
        # >  When a host fails, the host is disabled. Before the host is disabled, the data of the instances that run on the host is migrated to another host. This ensures data integrity.
        self.host_status = host_status
        # The total storage of the host. Unit: GB.
        self.host_storage = host_storage
        # The storage type of the host. Valid values:
        # 
        # *   **dhg_cloud_ssd** or **dhg_cloud_essd**: enhanced SSD (ESSD).
        # *   **dhg_local_ssd**: local SSD.
        self.host_type = host_type
        # The IP address of the host.
        self.ipaddress = ipaddress
        # The image of the host. This parameter is returned only when the database engine is **SQL Server**. Valid values:
        # 
        # *   **WindowsWithMssqlEntAlwaysonLicense**: SQL Server Cluster Edition (AlwaysOn).
        # *   **WindowsWithMssqlStdLicense**: SQL Server Standard Edition.
        # *   **WindowsWithMssqlEntLicense**: SQL Server Enterprise Edition.
        # *   **WindowsWithMssqlWebLicense**: SQL Server Web Edition.
        self.image_category = image_category
        # The number of instances deployed on the host.
        self.instance_number = instance_number
        # The number of primary instances deployed on the host.
        self.instance_number_master = instance_number_master
        # The number of primary instances of the read-only instance deployed on the host.
        self.instance_number_romaster = instance_number_romaster
        # The number of secondary instances of the read-only instance deployed on the host.
        self.instance_number_roslave = instance_number_roslave
        # The number of secondary instances deployed on the host.
        self.instance_number_slave = instance_number_slave
        # The memory usage of the host. Unit: %.
        self.mem_allocation_ratio = mem_allocation_ratio
        # The amount of memory used by the host. Unit: GB.
        self.memory_used = memory_used
        # Indicates whether the host OS permissions are grated. Valid values:
        # 
        # *   **0**: no.
        # *   **1**: yes.
        self.open_permission = open_permission
        # [The region ID](https://help.aliyun.com/document_detail/198326.html).
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
        # The storage usage of the host. Unit: GB.
        self.storage_used = storage_used
        # The virtual private cloud (VPC) ID.
        self.vpcid = vpcid
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.allocation_status is not None:
            result['AllocationStatus'] = self.allocation_status
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.cpuallocation_ratio is not None:
            result['CPUAllocationRatio'] = self.cpuallocation_ratio
        if self.cpu_used is not None:
            result['CpuUsed'] = self.cpu_used
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.disk_allocation_ratio is not None:
            result['DiskAllocationRatio'] = self.disk_allocation_ratio
        if self.distribution_tag is not None:
            result['DistributionTag'] = self.distribution_tag
        if self.ecs_class_code is not None:
            result['EcsClassCode'] = self.ecs_class_code
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.host_cpu is not None:
            result['HostCPU'] = self.host_cpu
        if self.host_class is not None:
            result['HostClass'] = self.host_class
        if self.host_mem is not None:
            result['HostMem'] = self.host_mem
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.host_status is not None:
            result['HostStatus'] = self.host_status
        if self.host_storage is not None:
            result['HostStorage'] = self.host_storage
        if self.host_type is not None:
            result['HostType'] = self.host_type
        if self.ipaddress is not None:
            result['IPAddress'] = self.ipaddress
        if self.image_category is not None:
            result['ImageCategory'] = self.image_category
        if self.instance_number is not None:
            result['InstanceNumber'] = self.instance_number
        if self.instance_number_master is not None:
            result['InstanceNumberMaster'] = self.instance_number_master
        if self.instance_number_romaster is not None:
            result['InstanceNumberROMaster'] = self.instance_number_romaster
        if self.instance_number_roslave is not None:
            result['InstanceNumberROSlave'] = self.instance_number_roslave
        if self.instance_number_slave is not None:
            result['InstanceNumberSlave'] = self.instance_number_slave
        if self.mem_allocation_ratio is not None:
            result['MemAllocationRatio'] = self.mem_allocation_ratio
        if self.memory_used is not None:
            result['MemoryUsed'] = self.memory_used
        if self.open_permission is not None:
            result['OpenPermission'] = self.open_permission
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.storage_used is not None:
            result['StorageUsed'] = self.storage_used
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('AllocationStatus') is not None:
            self.allocation_status = m.get('AllocationStatus')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('CPUAllocationRatio') is not None:
            self.cpuallocation_ratio = m.get('CPUAllocationRatio')
        if m.get('CpuUsed') is not None:
            self.cpu_used = m.get('CpuUsed')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('DiskAllocationRatio') is not None:
            self.disk_allocation_ratio = m.get('DiskAllocationRatio')
        if m.get('DistributionTag') is not None:
            self.distribution_tag = m.get('DistributionTag')
        if m.get('EcsClassCode') is not None:
            self.ecs_class_code = m.get('EcsClassCode')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('HostCPU') is not None:
            self.host_cpu = m.get('HostCPU')
        if m.get('HostClass') is not None:
            self.host_class = m.get('HostClass')
        if m.get('HostMem') is not None:
            self.host_mem = m.get('HostMem')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('HostStatus') is not None:
            self.host_status = m.get('HostStatus')
        if m.get('HostStorage') is not None:
            self.host_storage = m.get('HostStorage')
        if m.get('HostType') is not None:
            self.host_type = m.get('HostType')
        if m.get('IPAddress') is not None:
            self.ipaddress = m.get('IPAddress')
        if m.get('ImageCategory') is not None:
            self.image_category = m.get('ImageCategory')
        if m.get('InstanceNumber') is not None:
            self.instance_number = m.get('InstanceNumber')
        if m.get('InstanceNumberMaster') is not None:
            self.instance_number_master = m.get('InstanceNumberMaster')
        if m.get('InstanceNumberROMaster') is not None:
            self.instance_number_romaster = m.get('InstanceNumberROMaster')
        if m.get('InstanceNumberROSlave') is not None:
            self.instance_number_roslave = m.get('InstanceNumberROSlave')
        if m.get('InstanceNumberSlave') is not None:
            self.instance_number_slave = m.get('InstanceNumberSlave')
        if m.get('MemAllocationRatio') is not None:
            self.mem_allocation_ratio = m.get('MemAllocationRatio')
        if m.get('MemoryUsed') is not None:
            self.memory_used = m.get('MemoryUsed')
        if m.get('OpenPermission') is not None:
            self.open_permission = m.get('OpenPermission')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StorageUsed') is not None:
            self.storage_used = m.get('StorageUsed')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDedicatedHostAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDedicatedHostAttributeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDedicatedHostAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDedicatedHostDisksRequest(TeaModel):
    def __init__(
        self,
        dedicated_host_id: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The host ID. You can log on to the ApsaraDB for MyBase console and go to the **Hosts** page to view the host ID.
        # 
        # This parameter is required.
        self.dedicated_host_id = dedicated_host_id
        self.owner_id = owner_id
        # The region ID of the host. You can log on to the ApsaraDB for MyBase console to view the [region ID](https://help.aliyun.com/document_detail/198326.html).
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
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
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeDedicatedHostDisksResponseBodyDisks(TeaModel):
    def __init__(
        self,
        category: str = None,
        dbinstance_id: str = None,
        device: str = None,
        disk_id: str = None,
        has_dbinstance: bool = None,
        max_iops: int = None,
        max_throughput: int = None,
        performance_level: str = None,
        size: int = None,
        status: str = None,
        type: str = None,
        zone_id: str = None,
    ):
        # The storage type of the host. Valid values:
        # 
        # *   **cloud_ssd**: local SSD.
        # *   **cloud_essd**: ESSD.
        self.category = category
        # The ID of the instance that uses the disk.
        self.dbinstance_id = dbinstance_id
        # The device name of the instance to which the ESSD or local SSD is attached.
        self.device = device
        # The ID of the ESSD or local SSD.
        self.disk_id = disk_id
        # Indicates whether the disk is attached to instances. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.has_dbinstance = has_dbinstance
        # The maximum IOPS of the disk, which is displayed after being divided by 10,000.
        self.max_iops = max_iops
        # The maximum throughput of the disk. Unit: MB/s.
        self.max_throughput = max_throughput
        # The performance level of the ESSD.
        # 
        # >  ApsaraDB for MyBase provides the following types of ESSDs: **ESSD**, **PL2 ESSD**, and **PL3 ESSD**. The higher performance level delivers better ESSD performance.
        self.performance_level = performance_level
        # The size of the ESSD or local SSD. Unit: GB.
        self.size = size
        # The state of the ESSD. Valid values:
        # 
        # *   **In_use**\
        # *   **Available**\
        # *   **Attaching**\
        # *   **Detaching**\
        # *   **Creating**\
        # *   **ReIniting**\
        self.status = status
        # The disk type of the enhanced SSD (ESSD) or local SSD. Valid values:
        # 
        # *   **system**: system disk.
        # *   **data**: data disk.
        self.type = type
        # The zone ID of the ESSD or local SSD.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.device is not None:
            result['Device'] = self.device
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id
        if self.has_dbinstance is not None:
            result['HasDBInstance'] = self.has_dbinstance
        if self.max_iops is not None:
            result['MaxIOPS'] = self.max_iops
        if self.max_throughput is not None:
            result['MaxThroughput'] = self.max_throughput
        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level
        if self.size is not None:
            result['Size'] = self.size
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Device') is not None:
            self.device = m.get('Device')
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')
        if m.get('HasDBInstance') is not None:
            self.has_dbinstance = m.get('HasDBInstance')
        if m.get('MaxIOPS') is not None:
            self.max_iops = m.get('MaxIOPS')
        if m.get('MaxThroughput') is not None:
            self.max_throughput = m.get('MaxThroughput')
        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDedicatedHostDisksResponseBody(TeaModel):
    def __init__(
        self,
        dedicated_host_id: str = None,
        disks: List[DescribeDedicatedHostDisksResponseBodyDisks] = None,
        request_id: str = None,
    ):
        # The host ID.
        self.dedicated_host_id = dedicated_host_id
        # The queried disks.
        self.disks = disks
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.disks:
            for k in self.disks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        result['Disks'] = []
        if self.disks is not None:
            for k in self.disks:
                result['Disks'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        self.disks = []
        if m.get('Disks') is not None:
            for k in m.get('Disks'):
                temp_model = DescribeDedicatedHostDisksResponseBodyDisks()
                self.disks.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDedicatedHostDisksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDedicatedHostDisksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDedicatedHostDisksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDedicatedHostGroupsRequest(TeaModel):
    def __init__(
        self,
        dedicated_host_group_id: str = None,
        engine: str = None,
        image_category: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The dedicated cluster ID. You can log on to the ApsaraDB for MyBase console and go to the Dedicated Clusters page to view the dedicated cluster ID.
        # 
        # *   If you leave this parameter empty, the information about all hosts within the region is returned.
        # *   If you specify a dedicated cluster ID, the information about all hosts in the dedicated cluster within the region is returned.
        self.dedicated_host_group_id = dedicated_host_group_id
        # The database engine used to filter hosts. Valid values:
        # 
        # *   MySQL
        # *   SQL Server
        # *   PosgreSQL
        # 
        # *   Redis
        self.engine = engine
        # The image of the host. Valid values:
        # 
        # *   **WindowsWithMssqlEntAlwaysonLicense**: SQL
        # 
        # Server Cluster Edition.
        # 
        # *   **WindowsWithMssqlStdLicense**: SQL
        # 
        # Server Standard Edition.
        # 
        # *   **WindowsWithMssqlEntLicense**: SQL
        # 
        # Server Enterprise Edition.
        # 
        # *   **WindowsWithMssqlWebLicense**: SQL
        # 
        # Server Web Edition.
        # 
        # *   **AliLinux**: other images.
        self.image_category = image_category
        self.owner_id = owner_id
        # The region ID. For more information, see [Region IDs](https://help.aliyun.com/document_detail/198326.html).
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.image_category is not None:
            result['ImageCategory'] = self.image_category
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
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('ImageCategory') is not None:
            self.image_category = m.get('ImageCategory')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeDedicatedHostGroupsResponseBodyDedicatedHostGroupsDedicatedHostGroupsZoneIDList(TeaModel):
    def __init__(
        self,
        zone_idlist: List[str] = None,
    ):
        self.zone_idlist = zone_idlist

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.zone_idlist is not None:
            result['ZoneIDList'] = self.zone_idlist
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ZoneIDList') is not None:
            self.zone_idlist = m.get('ZoneIDList')
        return self


class DescribeDedicatedHostGroupsResponseBodyDedicatedHostGroupsDedicatedHostGroups(TeaModel):
    def __init__(
        self,
        allocation_policy: str = None,
        bastion_instance_id: str = None,
        category: str = None,
        cpu_allocate_ration: float = None,
        cpu_allocated_amount: float = None,
        cpu_allocation_ratio: int = None,
        create_time: str = None,
        dedicated_host_count_group_by_host_type: Dict[str, Any] = None,
        dedicated_host_group_desc: str = None,
        dedicated_host_group_id: str = None,
        deploy_type: str = None,
        disk_allocate_ration: float = None,
        disk_allocated_amount: float = None,
        disk_allocation_ratio: int = None,
        disk_used_amount: float = None,
        disk_utility: float = None,
        engine: str = None,
        host_number: int = None,
        host_replace_policy: str = None,
        instance_number: int = None,
        mem_allocate_ration: float = None,
        mem_allocated_amount: float = None,
        mem_allocation_ratio: int = None,
        mem_used_amount: float = None,
        mem_utility: float = None,
        open_permission: str = None,
        text: str = None,
        vpcid: str = None,
        zone_idlist: DescribeDedicatedHostGroupsResponseBodyDedicatedHostGroupsDedicatedHostGroupsZoneIDList = None,
    ):
        # The policy that is used to allocate host resources. Valid values:
        # 
        # *   **Evenly**: The system preferentially deploys database instances on the hosts where no resources or fewer resources are allocated. This maximizes system stability.
        # *   **Intensively**: The system preferentially deploys database instances on the hosts that are created earlier and have more allocated resources. This maximizes resource utilization.
        self.allocation_policy = allocation_policy
        # The ID of the primary instance deployed on the host. If no primary instance is deployed on the host, an empty string is returned.
        self.bastion_instance_id = bastion_instance_id
        self.category = category
        # The CPU allocation ratio of the host.
        self.cpu_allocate_ration = cpu_allocate_ration
        # The number of CPU cores allocated to the host.
        self.cpu_allocated_amount = cpu_allocated_amount
        # The CPU overcommit ratio of the host.
        self.cpu_allocation_ratio = cpu_allocation_ratio
        # The time when the host was created.
        self.create_time = create_time
        # The number of hosts by storage type.
        self.dedicated_host_count_group_by_host_type = dedicated_host_count_group_by_host_type
        # The name of the dedicated cluster in which the host is created.
        self.dedicated_host_group_desc = dedicated_host_group_desc
        # The ID of the dedicated cluster in which the host is created.
        self.dedicated_host_group_id = dedicated_host_group_id
        # The instance deployment mode of the host.
        self.deploy_type = deploy_type
        # The disk allocation rate of the host.
        self.disk_allocate_ration = disk_allocate_ration
        # The disk storage allocated to the host.
        self.disk_allocated_amount = disk_allocated_amount
        # The storage overcommit ratio of the host.
        self.disk_allocation_ratio = disk_allocation_ratio
        # The disk storage used by the host.
        self.disk_used_amount = disk_used_amount
        # The disk usage of the host.
        self.disk_utility = disk_utility
        # The database engine of the host.
        self.engine = engine
        # The number of hosts.
        self.host_number = host_number
        # The policy that is used for host troubleshooting. Valid values:
        # 
        # *   Auto (default): The system automatically replaces faulty hosts.
        # *   Manual: You must manually replace faulty hosts.
        self.host_replace_policy = host_replace_policy
        # The number of instances deployed on the host.
        self.instance_number = instance_number
        # The memory allocation ratio of the host.
        self.mem_allocate_ration = mem_allocate_ration
        # The amount of memory allocated to the host.
        self.mem_allocated_amount = mem_allocated_amount
        # The memory overcommit ratio of the host.
        self.mem_allocation_ratio = mem_allocation_ratio
        # The amount of used memory.
        self.mem_used_amount = mem_used_amount
        # The memory usage.
        self.mem_utility = mem_utility
        # Indicates whether the host OS permissions are granted. Valid values:
        # 
        # *   **0 or 1**: no.
        # *   **2 or 3** (default): yes.
        # 
        # >  When you create a dedicated cluster that runs **MySQL**, **SQL Server**, or **PostgreSQL**, you can grant the host OS permissions based on your business requirements.
        self.open_permission = open_permission
        # The description of the host.
        self.text = text
        # The virtual private cloud (VPC) ID of the dedicated cluster in which the host is created.
        self.vpcid = vpcid
        self.zone_idlist = zone_idlist

    def validate(self):
        if self.zone_idlist:
            self.zone_idlist.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allocation_policy is not None:
            result['AllocationPolicy'] = self.allocation_policy
        if self.bastion_instance_id is not None:
            result['BastionInstanceId'] = self.bastion_instance_id
        if self.category is not None:
            result['Category'] = self.category
        if self.cpu_allocate_ration is not None:
            result['CpuAllocateRation'] = self.cpu_allocate_ration
        if self.cpu_allocated_amount is not None:
            result['CpuAllocatedAmount'] = self.cpu_allocated_amount
        if self.cpu_allocation_ratio is not None:
            result['CpuAllocationRatio'] = self.cpu_allocation_ratio
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dedicated_host_count_group_by_host_type is not None:
            result['DedicatedHostCountGroupByHostType'] = self.dedicated_host_count_group_by_host_type
        if self.dedicated_host_group_desc is not None:
            result['DedicatedHostGroupDesc'] = self.dedicated_host_group_desc
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type
        if self.disk_allocate_ration is not None:
            result['DiskAllocateRation'] = self.disk_allocate_ration
        if self.disk_allocated_amount is not None:
            result['DiskAllocatedAmount'] = self.disk_allocated_amount
        if self.disk_allocation_ratio is not None:
            result['DiskAllocationRatio'] = self.disk_allocation_ratio
        if self.disk_used_amount is not None:
            result['DiskUsedAmount'] = self.disk_used_amount
        if self.disk_utility is not None:
            result['DiskUtility'] = self.disk_utility
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.host_number is not None:
            result['HostNumber'] = self.host_number
        if self.host_replace_policy is not None:
            result['HostReplacePolicy'] = self.host_replace_policy
        if self.instance_number is not None:
            result['InstanceNumber'] = self.instance_number
        if self.mem_allocate_ration is not None:
            result['MemAllocateRation'] = self.mem_allocate_ration
        if self.mem_allocated_amount is not None:
            result['MemAllocatedAmount'] = self.mem_allocated_amount
        if self.mem_allocation_ratio is not None:
            result['MemAllocationRatio'] = self.mem_allocation_ratio
        if self.mem_used_amount is not None:
            result['MemUsedAmount'] = self.mem_used_amount
        if self.mem_utility is not None:
            result['MemUtility'] = self.mem_utility
        if self.open_permission is not None:
            result['OpenPermission'] = self.open_permission
        if self.text is not None:
            result['Text'] = self.text
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.zone_idlist is not None:
            result['ZoneIDList'] = self.zone_idlist.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationPolicy') is not None:
            self.allocation_policy = m.get('AllocationPolicy')
        if m.get('BastionInstanceId') is not None:
            self.bastion_instance_id = m.get('BastionInstanceId')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CpuAllocateRation') is not None:
            self.cpu_allocate_ration = m.get('CpuAllocateRation')
        if m.get('CpuAllocatedAmount') is not None:
            self.cpu_allocated_amount = m.get('CpuAllocatedAmount')
        if m.get('CpuAllocationRatio') is not None:
            self.cpu_allocation_ratio = m.get('CpuAllocationRatio')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DedicatedHostCountGroupByHostType') is not None:
            self.dedicated_host_count_group_by_host_type = m.get('DedicatedHostCountGroupByHostType')
        if m.get('DedicatedHostGroupDesc') is not None:
            self.dedicated_host_group_desc = m.get('DedicatedHostGroupDesc')
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')
        if m.get('DiskAllocateRation') is not None:
            self.disk_allocate_ration = m.get('DiskAllocateRation')
        if m.get('DiskAllocatedAmount') is not None:
            self.disk_allocated_amount = m.get('DiskAllocatedAmount')
        if m.get('DiskAllocationRatio') is not None:
            self.disk_allocation_ratio = m.get('DiskAllocationRatio')
        if m.get('DiskUsedAmount') is not None:
            self.disk_used_amount = m.get('DiskUsedAmount')
        if m.get('DiskUtility') is not None:
            self.disk_utility = m.get('DiskUtility')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('HostNumber') is not None:
            self.host_number = m.get('HostNumber')
        if m.get('HostReplacePolicy') is not None:
            self.host_replace_policy = m.get('HostReplacePolicy')
        if m.get('InstanceNumber') is not None:
            self.instance_number = m.get('InstanceNumber')
        if m.get('MemAllocateRation') is not None:
            self.mem_allocate_ration = m.get('MemAllocateRation')
        if m.get('MemAllocatedAmount') is not None:
            self.mem_allocated_amount = m.get('MemAllocatedAmount')
        if m.get('MemAllocationRatio') is not None:
            self.mem_allocation_ratio = m.get('MemAllocationRatio')
        if m.get('MemUsedAmount') is not None:
            self.mem_used_amount = m.get('MemUsedAmount')
        if m.get('MemUtility') is not None:
            self.mem_utility = m.get('MemUtility')
        if m.get('OpenPermission') is not None:
            self.open_permission = m.get('OpenPermission')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('ZoneIDList') is not None:
            temp_model = DescribeDedicatedHostGroupsResponseBodyDedicatedHostGroupsDedicatedHostGroupsZoneIDList()
            self.zone_idlist = temp_model.from_map(m['ZoneIDList'])
        return self


class DescribeDedicatedHostGroupsResponseBodyDedicatedHostGroups(TeaModel):
    def __init__(
        self,
        dedicated_host_groups: List[DescribeDedicatedHostGroupsResponseBodyDedicatedHostGroupsDedicatedHostGroups] = None,
    ):
        self.dedicated_host_groups = dedicated_host_groups

    def validate(self):
        if self.dedicated_host_groups:
            for k in self.dedicated_host_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DedicatedHostGroups'] = []
        if self.dedicated_host_groups is not None:
            for k in self.dedicated_host_groups:
                result['DedicatedHostGroups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dedicated_host_groups = []
        if m.get('DedicatedHostGroups') is not None:
            for k in m.get('DedicatedHostGroups'):
                temp_model = DescribeDedicatedHostGroupsResponseBodyDedicatedHostGroupsDedicatedHostGroups()
                self.dedicated_host_groups.append(temp_model.from_map(k))
        return self


class DescribeDedicatedHostGroupsResponseBody(TeaModel):
    def __init__(
        self,
        dedicated_host_groups: DescribeDedicatedHostGroupsResponseBodyDedicatedHostGroups = None,
        request_id: str = None,
    ):
        # The queried hosts.
        self.dedicated_host_groups = dedicated_host_groups
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.dedicated_host_groups:
            self.dedicated_host_groups.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_host_groups is not None:
            result['DedicatedHostGroups'] = self.dedicated_host_groups.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedHostGroups') is not None:
            temp_model = DescribeDedicatedHostGroupsResponseBodyDedicatedHostGroups()
            self.dedicated_host_groups = temp_model.from_map(m['DedicatedHostGroups'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDedicatedHostGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDedicatedHostGroupsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDedicatedHostGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDedicatedHostsRequest(TeaModel):
    def __init__(
        self,
        allocation_status: str = None,
        dedicated_host_group_id: str = None,
        dedicated_host_id: str = None,
        host_status: str = None,
        host_type: str = None,
        order_id: int = None,
        owner_id: int = None,
        page_numbers: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tags: str = None,
        zone_id: str = None,
    ):
        # Specifies whether instances can be deployed on the host. Valid values:
        # 
        # *   **Allocatable**: Instances can be deployed on the host.
        # *   **Suspended**: Instances cannot be deployed on the host.
        self.allocation_status = allocation_status
        # The dedicated cluster ID. You can log on to the ApsaraDB for MyBase console and go to the **Dedicated Clusters** page to view the dedicated cluster ID.
        self.dedicated_host_group_id = dedicated_host_group_id
        # The ID of the host in the dedicated cluster. You can log on to the ApsaraDB for MyBase console and go to the **Hosts** page to view the host ID.
        self.dedicated_host_id = dedicated_host_id
        # The state of the host. Valid values:
        # 
        # *   **0**: The host is being created.
        # *   **1**: The host is running.
        # *   **2**: The host is faulty.
        # *   **3**: The host is ready for disabling.
        # *   **4**: The host is being maintained.
        # *   **5**: The host is disabled.
        # *   **6**: The host is restarting.
        # *   **7**: The host is locked.
        # 
        # >  When a host fails, the host is disabled. Before the host is disabled, the data of the instances that run on the host is migrated to another host.
        self.host_status = host_status
        # The storage type of the host. Valid values:
        # 
        # *   **dhg_local_ssd**: local SSD.
        # *   **dhg_cloud_ssd** or **dhg_cloud_essd**: enhanced SSD (ESSD).
        self.host_type = host_type
        # The order ID. You can log on to the Billing Management console and go to the **Orders** page to view the order ID.
        self.order_id = order_id
        self.owner_id = owner_id
        # The page number.
        self.page_numbers = page_numbers
        # The number of entries per page.
        self.page_size = page_size
        # [The region ID](https://help.aliyun.com/document_detail/198326.html).
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tags that are added to the host. Each tag is a key-value pair that consists of TagKey and TagValue. You can specify a maximum of five tags in the following format for each request: {"key1":"value1","key2":"value2"...}.
        # 
        # >  If you want to filter hosts based on tags, do not specify the **DedicatedHostId** parameter. Otherwise, the **DedicatedHostId** parameter is used to filter hosts.
        self.tags = tags
        # The zone ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/214103.html) operation to query the most recent zone list.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allocation_status is not None:
            result['AllocationStatus'] = self.allocation_status
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.host_status is not None:
            result['HostStatus'] = self.host_status
        if self.host_type is not None:
            result['HostType'] = self.host_type
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_numbers is not None:
            result['PageNumbers'] = self.page_numbers
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationStatus') is not None:
            self.allocation_status = m.get('AllocationStatus')
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('HostStatus') is not None:
            self.host_status = m.get('HostStatus')
        if m.get('HostType') is not None:
            self.host_type = m.get('HostType')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumbers') is not None:
            self.page_numbers = m.get('PageNumbers')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHosts(TeaModel):
    def __init__(
        self,
        account_name: str = None,
        account_type: str = None,
        allocation_status: str = None,
        bastion_instance_id: str = None,
        cpuallocation_ratio: str = None,
        category: str = None,
        charge_type: str = None,
        cpu_used: str = None,
        created_time: str = None,
        dedicated_host_group_id: str = None,
        dedicated_host_id: str = None,
        disk_allocation_ratio: str = None,
        disk_info: str = None,
        distribution_symbol: str = None,
        distribution_tag: str = None,
        ecs_class_code: str = None,
        ecs_id: str = None,
        end_time: str = None,
        engine: str = None,
        host_cpu: str = None,
        host_class: str = None,
        host_mem: str = None,
        host_name: str = None,
        host_status: str = None,
        host_storage: str = None,
        host_type: str = None,
        ipaddress: str = None,
        image_category: str = None,
        instance_number: str = None,
        mem_allocation_ratio: str = None,
        memory_used: str = None,
        mssql_support_version: str = None,
        open_permission: str = None,
        storage_used: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        # The custom account name of the host.
        # 
        # *   The name can contain lowercase letters, digits, and underscores (_).
        # *   The name must start with a lowercase letter and end with a lowercase letter or a digit.
        # *   The name must be 2 to 16 characters in length.
        self.account_name = account_name
        # The account type of the host. Valid values:
        # 
        # **Normal**: standard account.
        # 
        # **Admin**: administrator account.
        self.account_type = account_type
        # Specifies whether instances can be deployed on the host. Valid values:
        # 
        # *   **Allocatable**: Instances can be deployed on the host.
        # *   **Suspended**: Instances cannot be deployed on the host.
        self.allocation_status = allocation_status
        # The ID of the bastion host with which the host is associated.
        self.bastion_instance_id = bastion_instance_id
        # The CPU utilization of the host.
        self.cpuallocation_ratio = cpuallocation_ratio
        # The type of the dedicated cluster. Valid values:
        # 
        # *   **Pro**: Proprietary MyBase.
        # *   **Standard**: Managed MyBase.
        # 
        # >  This parameter is returned only for the China site (aliyun.com).
        self.category = category
        # The billing method.
        self.charge_type = charge_type
        # The number of used CPU cores.
        self.cpu_used = cpu_used
        # The time when the host was created. The time follows the ISO 8601 standard in the **yyyy-MM-ddTHH:mm:ssZ** format. The time is displayed in UTC.
        self.created_time = created_time
        # The ID of the dedicated cluster in which the host is created.
        self.dedicated_host_group_id = dedicated_host_group_id
        # The host ID.
        self.dedicated_host_id = dedicated_host_id
        # The disk usage of the host. Unit: %.
        self.disk_allocation_ratio = disk_allocation_ratio
        # The disk information of the ECS instance.
        # 
        # >  This parameter is returned only for the China site (aliyun.com) when the dedicated cluster is of the **Proprietary MyBase** type.
        self.disk_info = disk_info
        # The distribution symbol of the host.
        # 
        # >  This parameter is returned only when the host runs **Tair**.
        self.distribution_symbol = distribution_symbol
        # The distribution tag of the host.
        self.distribution_tag = distribution_tag
        # The instance type of the Elastic Compute Service (ECS) instance. For more information, see [Overview of instance families](https://help.aliyun.com/document_detail/25378.html).
        self.ecs_class_code = ecs_class_code
        # The ID of the ECS instance.
        # 
        # >  This parameter is returned only for the China site (aliyun.com) when the dedicated cluster is of the **Proprietary MyBase** type.
        self.ecs_id = ecs_id
        # The expiration time of the host. The time follows the ISO 8601 standard in the **yyyy-MM-ddTHH:mm:ssZ** format. The time is displayed in UTC.
        self.end_time = end_time
        # The database engine of the host.
        self.engine = engine
        # The number of CPU cores of the host.
        self.host_cpu = host_cpu
        # The instance type of the host.
        self.host_class = host_class
        # The memory size of the host. Unit: GB.
        self.host_mem = host_mem
        # The name of the host.
        self.host_name = host_name
        # The state of the host. Valid values:
        # 
        # *   **0**: The host is being created.
        # *   **1**: The host is running.
        # *   **2**: The host is faulty.
        # *   **3**: The host is ready for disabling.
        # *   **4**: The host is being maintained.
        # *   **5**: The host is disabled.
        # *   **6**: The host is restarting.
        # *   **7**: The host is locked.
        # 
        # >  When a host fails, the host is disabled. Before the host is disabled, the data of the instances that run on the host is migrated to another host.
        self.host_status = host_status
        # The total storage of the host. Unit: GB.
        self.host_storage = host_storage
        # The storage type of the host.
        self.host_type = host_type
        # The IP address of the host.
        self.ipaddress = ipaddress
        # The image type of the host.
        self.image_category = image_category
        # The number of instances deployed on the host.
        self.instance_number = instance_number
        # The memory usage of the host. Unit: %.
        self.mem_allocation_ratio = mem_allocation_ratio
        # The amount of memory used by the host. Unit: GB.
        self.memory_used = memory_used
        # The versions supported by hosts in ApsaraDB MyBase for SQL Server.
        self.mssql_support_version = mssql_support_version
        # Indicates whether the host OS permissions are granted. Valid values:
        # 
        # *   **0**: no.
        # *   **1** (default): yes.
        self.open_permission = open_permission
        # The amount of storage used by the host. Unit: GB.
        self.storage_used = storage_used
        # The virtual private cloud (VPC) ID of the dedicated cluster in which the host is created.
        self.vpcid = vpcid
        # The ID of the vSwitch to which the host is connected.
        self.v_switch_id = v_switch_id
        # The ID of the zone in which the host resides.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.allocation_status is not None:
            result['AllocationStatus'] = self.allocation_status
        if self.bastion_instance_id is not None:
            result['BastionInstanceId'] = self.bastion_instance_id
        if self.cpuallocation_ratio is not None:
            result['CPUAllocationRatio'] = self.cpuallocation_ratio
        if self.category is not None:
            result['Category'] = self.category
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.cpu_used is not None:
            result['CpuUsed'] = self.cpu_used
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.disk_allocation_ratio is not None:
            result['DiskAllocationRatio'] = self.disk_allocation_ratio
        if self.disk_info is not None:
            result['DiskInfo'] = self.disk_info
        if self.distribution_symbol is not None:
            result['DistributionSymbol'] = self.distribution_symbol
        if self.distribution_tag is not None:
            result['DistributionTag'] = self.distribution_tag
        if self.ecs_class_code is not None:
            result['EcsClassCode'] = self.ecs_class_code
        if self.ecs_id is not None:
            result['EcsId'] = self.ecs_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.host_cpu is not None:
            result['HostCPU'] = self.host_cpu
        if self.host_class is not None:
            result['HostClass'] = self.host_class
        if self.host_mem is not None:
            result['HostMem'] = self.host_mem
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.host_status is not None:
            result['HostStatus'] = self.host_status
        if self.host_storage is not None:
            result['HostStorage'] = self.host_storage
        if self.host_type is not None:
            result['HostType'] = self.host_type
        if self.ipaddress is not None:
            result['IPAddress'] = self.ipaddress
        if self.image_category is not None:
            result['ImageCategory'] = self.image_category
        if self.instance_number is not None:
            result['InstanceNumber'] = self.instance_number
        if self.mem_allocation_ratio is not None:
            result['MemAllocationRatio'] = self.mem_allocation_ratio
        if self.memory_used is not None:
            result['MemoryUsed'] = self.memory_used
        if self.mssql_support_version is not None:
            result['MssqlSupportVersion'] = self.mssql_support_version
        if self.open_permission is not None:
            result['OpenPermission'] = self.open_permission
        if self.storage_used is not None:
            result['StorageUsed'] = self.storage_used
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('AllocationStatus') is not None:
            self.allocation_status = m.get('AllocationStatus')
        if m.get('BastionInstanceId') is not None:
            self.bastion_instance_id = m.get('BastionInstanceId')
        if m.get('CPUAllocationRatio') is not None:
            self.cpuallocation_ratio = m.get('CPUAllocationRatio')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('CpuUsed') is not None:
            self.cpu_used = m.get('CpuUsed')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('DiskAllocationRatio') is not None:
            self.disk_allocation_ratio = m.get('DiskAllocationRatio')
        if m.get('DiskInfo') is not None:
            self.disk_info = m.get('DiskInfo')
        if m.get('DistributionSymbol') is not None:
            self.distribution_symbol = m.get('DistributionSymbol')
        if m.get('DistributionTag') is not None:
            self.distribution_tag = m.get('DistributionTag')
        if m.get('EcsClassCode') is not None:
            self.ecs_class_code = m.get('EcsClassCode')
        if m.get('EcsId') is not None:
            self.ecs_id = m.get('EcsId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('HostCPU') is not None:
            self.host_cpu = m.get('HostCPU')
        if m.get('HostClass') is not None:
            self.host_class = m.get('HostClass')
        if m.get('HostMem') is not None:
            self.host_mem = m.get('HostMem')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('HostStatus') is not None:
            self.host_status = m.get('HostStatus')
        if m.get('HostStorage') is not None:
            self.host_storage = m.get('HostStorage')
        if m.get('HostType') is not None:
            self.host_type = m.get('HostType')
        if m.get('IPAddress') is not None:
            self.ipaddress = m.get('IPAddress')
        if m.get('ImageCategory') is not None:
            self.image_category = m.get('ImageCategory')
        if m.get('InstanceNumber') is not None:
            self.instance_number = m.get('InstanceNumber')
        if m.get('MemAllocationRatio') is not None:
            self.mem_allocation_ratio = m.get('MemAllocationRatio')
        if m.get('MemoryUsed') is not None:
            self.memory_used = m.get('MemoryUsed')
        if m.get('MssqlSupportVersion') is not None:
            self.mssql_support_version = m.get('MssqlSupportVersion')
        if m.get('OpenPermission') is not None:
            self.open_permission = m.get('OpenPermission')
        if m.get('StorageUsed') is not None:
            self.storage_used = m.get('StorageUsed')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDedicatedHostsResponseBodyDedicatedHosts(TeaModel):
    def __init__(
        self,
        dedicated_hosts: List[DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHosts] = None,
    ):
        self.dedicated_hosts = dedicated_hosts

    def validate(self):
        if self.dedicated_hosts:
            for k in self.dedicated_hosts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DedicatedHosts'] = []
        if self.dedicated_hosts is not None:
            for k in self.dedicated_hosts:
                result['DedicatedHosts'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dedicated_hosts = []
        if m.get('DedicatedHosts') is not None:
            for k in m.get('DedicatedHosts'):
                temp_model = DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHosts()
                self.dedicated_hosts.append(temp_model.from_map(k))
        return self


class DescribeDedicatedHostsResponseBody(TeaModel):
    def __init__(
        self,
        dedicated_host_group_id: str = None,
        dedicated_hosts: DescribeDedicatedHostsResponseBodyDedicatedHosts = None,
        max_auto_scale_host_storage: int = None,
        page_numbers: int = None,
        page_size: int = None,
        request_id: str = None,
        total_records: int = None,
    ):
        # The dedicated cluster ID.
        self.dedicated_host_group_id = dedicated_host_group_id
        # The queried hosts.
        self.dedicated_hosts = dedicated_hosts
        # The maximum storage of local SSDs for auto scaling. Unit: GB.
        self.max_auto_scale_host_storage = max_auto_scale_host_storage
        # The page number.
        self.page_numbers = page_numbers
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_records = total_records

    def validate(self):
        if self.dedicated_hosts:
            self.dedicated_hosts.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        if self.dedicated_hosts is not None:
            result['DedicatedHosts'] = self.dedicated_hosts.to_map()
        if self.max_auto_scale_host_storage is not None:
            result['MaxAutoScaleHostStorage'] = self.max_auto_scale_host_storage
        if self.page_numbers is not None:
            result['PageNumbers'] = self.page_numbers
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_records is not None:
            result['TotalRecords'] = self.total_records
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        if m.get('DedicatedHosts') is not None:
            temp_model = DescribeDedicatedHostsResponseBodyDedicatedHosts()
            self.dedicated_hosts = temp_model.from_map(m['DedicatedHosts'])
        if m.get('MaxAutoScaleHostStorage') is not None:
            self.max_auto_scale_host_storage = m.get('MaxAutoScaleHostStorage')
        if m.get('PageNumbers') is not None:
            self.page_numbers = m.get('PageNumbers')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalRecords') is not None:
            self.total_records = m.get('TotalRecords')
        return self


class DescribeDedicatedHostsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDedicatedHostsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDedicatedHostsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHostEcsLevelInfoRequest(TeaModel):
    def __init__(
        self,
        db_type: str = None,
        image_category: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        storage_type: str = None,
        zone_id: str = None,
    ):
        # The database engine. Valid values:
        # 
        # *   **mysql**\
        # *   **mssql**\
        # *   **pgsql**\
        # *   **redis**\
        # 
        # This parameter is required.
        self.db_type = db_type
        # The image of the host. Valid values:
        # 
        # *   **WindowsWithMssqlEntAlwaysonLicense**: SQL Server Cluster Edition.
        # *   **WindowsWithMssqlStdLicense**: SQL Server Standard Edition.
        # *   **WindowsWithMssqlEntLicense**: SQL Server Enterprise Edition.
        # *   **WindowsWithMssqlWebLicense**: SQL Server Web Edition.
        # *   **AliLinux**: other images.
        self.image_category = image_category
        self.owner_id = owner_id
        # The region ID. For more information, see [Region IDs](https://help.aliyun.com/document_detail/198326.html).
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The storage type. Valid values:
        # 
        # *   **local_ssd**: standard SSD.
        # *   **cloud_essd**: PL1 enhanced SSD (ESSD).
        # *   **cloud_essd2**: PL2 ESSD.
        # *   **cloud_essd3**: PL3 ESSD.
        # 
        # This parameter is required.
        self.storage_type = storage_type
        # The zone ID.
        # 
        # This parameter is required.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.image_category is not None:
            result['ImageCategory'] = self.image_category
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('ImageCategory') is not None:
            self.image_category = m.get('ImageCategory')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeHostEcsLevelInfoResponseBodyHostEcsLevelInfosItems(TeaModel):
    def __init__(
        self,
        cloud_storage_bandwidth: float = None,
        cpu: int = None,
        cpu_frequency: str = None,
        cpu_version: str = None,
        description: str = None,
        ecs_class: str = None,
        ecs_class_code: str = None,
        is_cloud_disk: int = None,
        local_storage: str = None,
        memory: int = None,
        net_band_width: float = None,
        net_package: int = None,
        rds_class_code: str = None,
        storage_iops: int = None,
    ):
        # The disk bandwidth. Unit: Gbit/s.
        self.cloud_storage_bandwidth = cloud_storage_bandwidth
        # The number of CPU cores of the host.
        self.cpu = cpu
        # The processor frequency. Unit: GHz.
        self.cpu_frequency = cpu_frequency
        # The CPU model of the host.
        self.cpu_version = cpu_version
        # The name of the host.
        self.description = description
        # The instance family of the host.
        self.ecs_class = ecs_class
        # The instance type of the host.
        self.ecs_class_code = ecs_class_code
        # Indicates whether the host uses cloud disks.
        self.is_cloud_disk = is_cloud_disk
        # The local storage.
        self.local_storage = local_storage
        # The memory size of the host. Unit: GB.
        self.memory = memory
        # The internal bandwidth of the host. Unit: Gbit/s.
        self.net_band_width = net_band_width
        # The packet forwarding rate over the internal network, which is displayed after being divided by 10,000. Unit: packets per second (PPS).
        self.net_package = net_package
        # The instance type of the instance.
        self.rds_class_code = rds_class_code
        # The storage IOPS of the host, which is displayed after being divided by 10,000.
        self.storage_iops = storage_iops

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cloud_storage_bandwidth is not None:
            result['CloudStorageBandwidth'] = self.cloud_storage_bandwidth
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.cpu_frequency is not None:
            result['CpuFrequency'] = self.cpu_frequency
        if self.cpu_version is not None:
            result['CpuVersion'] = self.cpu_version
        if self.description is not None:
            result['Description'] = self.description
        if self.ecs_class is not None:
            result['EcsClass'] = self.ecs_class
        if self.ecs_class_code is not None:
            result['EcsClassCode'] = self.ecs_class_code
        if self.is_cloud_disk is not None:
            result['IsCloudDisk'] = self.is_cloud_disk
        if self.local_storage is not None:
            result['LocalStorage'] = self.local_storage
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.net_band_width is not None:
            result['NetBandWidth'] = self.net_band_width
        if self.net_package is not None:
            result['NetPackage'] = self.net_package
        if self.rds_class_code is not None:
            result['RdsClassCode'] = self.rds_class_code
        if self.storage_iops is not None:
            result['StorageIops'] = self.storage_iops
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudStorageBandwidth') is not None:
            self.cloud_storage_bandwidth = m.get('CloudStorageBandwidth')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('CpuFrequency') is not None:
            self.cpu_frequency = m.get('CpuFrequency')
        if m.get('CpuVersion') is not None:
            self.cpu_version = m.get('CpuVersion')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EcsClass') is not None:
            self.ecs_class = m.get('EcsClass')
        if m.get('EcsClassCode') is not None:
            self.ecs_class_code = m.get('EcsClassCode')
        if m.get('IsCloudDisk') is not None:
            self.is_cloud_disk = m.get('IsCloudDisk')
        if m.get('LocalStorage') is not None:
            self.local_storage = m.get('LocalStorage')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('NetBandWidth') is not None:
            self.net_band_width = m.get('NetBandWidth')
        if m.get('NetPackage') is not None:
            self.net_package = m.get('NetPackage')
        if m.get('RdsClassCode') is not None:
            self.rds_class_code = m.get('RdsClassCode')
        if m.get('StorageIops') is not None:
            self.storage_iops = m.get('StorageIops')
        return self


class DescribeHostEcsLevelInfoResponseBodyHostEcsLevelInfos(TeaModel):
    def __init__(
        self,
        cddc_host_type: str = None,
        items: List[DescribeHostEcsLevelInfoResponseBodyHostEcsLevelInfosItems] = None,
    ):
        # The category of the host. Valid values:
        # 
        # *   **general**: general-purpose.
        # *   **compute**: compute-optimized.
        # *   **ram**: memory-optimized.
        # *   **dragon**: ECS Bare Metal Instance.
        self.cddc_host_type = cddc_host_type
        # The queried host specifications.
        self.items = items

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cddc_host_type is not None:
            result['CddcHostType'] = self.cddc_host_type
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CddcHostType') is not None:
            self.cddc_host_type = m.get('CddcHostType')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeHostEcsLevelInfoResponseBodyHostEcsLevelInfosItems()
                self.items.append(temp_model.from_map(k))
        return self


class DescribeHostEcsLevelInfoResponseBody(TeaModel):
    def __init__(
        self,
        host_ecs_level_infos: List[DescribeHostEcsLevelInfoResponseBodyHostEcsLevelInfos] = None,
        request_id: str = None,
    ):
        # The queried host.
        self.host_ecs_level_infos = host_ecs_level_infos
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.host_ecs_level_infos:
            for k in self.host_ecs_level_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HostEcsLevelInfos'] = []
        if self.host_ecs_level_infos is not None:
            for k in self.host_ecs_level_infos:
                result['HostEcsLevelInfos'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.host_ecs_level_infos = []
        if m.get('HostEcsLevelInfos') is not None:
            for k in m.get('HostEcsLevelInfos'):
                temp_model = DescribeHostEcsLevelInfoResponseBodyHostEcsLevelInfos()
                self.host_ecs_level_infos.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeHostEcsLevelInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeHostEcsLevelInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeHostEcsLevelInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHostWebShellRequest(TeaModel):
    def __init__(
        self,
        dedicated_host_id: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        zone_id: str = None,
    ):
        # The host ID. You can call the [DescribeDedicatedHosts](https://help.aliyun.com/document_detail/200944.html) operation to query the host ID.
        # 
        # This parameter is required.
        self.dedicated_host_id = dedicated_host_id
        # The ID of the Alibaba Cloud account to which the VPC belongs.
        self.owner_id = owner_id
        # The region ID of the host. You can call the [DescribeDedicatedHostAttribute](https://help.aliyun.com/document_detail/213010.html) operation to query the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # ResourceOwnerAccount
        self.resource_owner_account = resource_owner_account
        # The ID of the asset owner.
        self.resource_owner_id = resource_owner_id
        # The zone ID of the host. You can call the [DescribeDedicatedHostAttribute](https://help.aliyun.com/document_detail/213010.html) operation to query the zone ID.
        # 
        # This parameter is required.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeHostWebShellResponseBody(TeaModel):
    def __init__(
        self,
        login_url: str = None,
        request_id: str = None,
    ):
        # The URL of the webshell.
        self.login_url = login_url
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.login_url is not None:
            result['LoginUrl'] = self.login_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoginUrl') is not None:
            self.login_url = m.get('LoginUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeHostWebShellResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeHostWebShellResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeHostWebShellResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        resource_owner_id: int = None,
    ):
        # The ID of the asset owner.
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeRegionsResponseBodyRegionsRDSRegion(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        zone_id: str = None,
    ):
        # The region ID.
        self.region_id = region_id
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        rdsregion: List[DescribeRegionsResponseBodyRegionsRDSRegion] = None,
    ):
        self.rdsregion = rdsregion

    def validate(self):
        if self.rdsregion:
            for k in self.rdsregion:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RDSRegion'] = []
        if self.rdsregion is not None:
            for k in self.rdsregion:
                result['RDSRegion'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rdsregion = []
        if m.get('RDSRegion') is not None:
            for k in m.get('RDSRegion'):
                temp_model = DescribeRegionsResponseBodyRegionsRDSRegion()
                self.rdsregion.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        regions: DescribeRegionsResponseBodyRegions = None,
        request_id: str = None,
    ):
        # The queried regions.
        self.regions = regions
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Regions') is not None:
            temp_model = DescribeRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRegionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N.
        # 
        # *   **N** specifies the serial number of the tag. Examples:
        # 
        #     *   **Tag.1.Key** specifies the key of the first tag.
        #     *   **Tag.2.Key** specifies the key of the second tag.
        # 
        # *   You must specify one of this parameter and **ResourceId.N**.
        self.key = key
        # The value of tag N.
        # 
        # *   **N** specifies the serial number of the tag. Examples:
        # 
        #     *   **Tag.1.Value** specifies the value of the first tag.
        #     *   **Tag.2.Value** specifies the value of the second tag.
        # 
        # *   If no tag value exists, a value is automatically created.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListTagResourcesRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
        tag: List[ListTagResourcesRequestTag] = None,
    ):
        self.owner_id = owner_id
        # The region ID of the host.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of host N. You can specify multiple host IDs.
        self.resource_id = resource_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The resource type. Set the value to DEDICATEDHOST.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tags.
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The host ID.
        self.resource_id = resource_id
        # The resource type.
        # 
        # ALIYUN::CDDC::DEDICATEDHOST is returned, which indicates an ApsaraDB for MyBase host.
        self.resource_type = resource_type
        # The key of tag N.
        self.tag_key = tag_key
        # The tag value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tag_resources: List[ListTagResourcesResponseBodyTagResources] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The queried tags.
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            for k in self.tag_resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TagResources'] = []
        if self.tag_resources is not None:
            for k in self.tag_resources:
                result['TagResources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tag_resources = []
        if m.get('TagResources') is not None:
            for k in m.get('TagResources'):
                temp_model = ListTagResourcesResponseBodyTagResources()
                self.tag_resources.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDedicatedHostAccountRequest(TeaModel):
    def __init__(
        self,
        account_name: str = None,
        account_password: str = None,
        dedicated_host_id: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The account name of the host.
        # 
        # This parameter is required.
        self.account_name = account_name
        # The new account password of the host.
        # 
        # This parameter is required.
        self.account_password = account_password
        # The host ID. You can call the [DescribeDedicatedHosts](https://help.aliyun.com/document_detail/200944.html) operation to query the host ID.
        # 
        # This parameter is required.
        self.dedicated_host_id = dedicated_host_id
        # 账号ID。
        self.owner_id = owner_id
        # The region ID of the host. You can call the [DescribeDedicatedHostAttribute](https://help.aliyun.com/document_detail/213010.html) operation to query the region ID.
        self.region_id = region_id
        # 资源主账号的账号名称。
        self.resource_owner_account = resource_owner_account
        # ResourceOwnerId
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_password is not None:
            result['AccountPassword'] = self.account_password
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
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
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ModifyDedicatedHostAccountResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDedicatedHostAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDedicatedHostAccountResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyDedicatedHostAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDedicatedHostAttributeRequest(TeaModel):
    def __init__(
        self,
        allocation_status: str = None,
        dedicated_host_id: str = None,
        host_name: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # Indicates whether instances can be deployed on the host. Valid values:
        # 
        # *   **1**: yes.
        # *   **0**: no.
        self.allocation_status = allocation_status
        # The host ID. You can log on to the ApsaraDB for MyBase console and go to the **Hosts** page to view the host ID.
        # 
        # This parameter is required.
        self.dedicated_host_id = dedicated_host_id
        # The name of the host.
        self.host_name = host_name
        self.owner_id = owner_id
        # The [region ID](https://help.aliyun.com/document_detail/198326.html) of the host.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allocation_status is not None:
            result['AllocationStatus'] = self.allocation_status
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.host_name is not None:
            result['HostName'] = self.host_name
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
        if m.get('AllocationStatus') is not None:
            self.allocation_status = m.get('AllocationStatus')
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ModifyDedicatedHostAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDedicatedHostAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDedicatedHostAttributeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyDedicatedHostAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDedicatedHostClassRequest(TeaModel):
    def __init__(
        self,
        dedicated_host_id: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        switch_time: str = None,
        switch_time_mode: str = None,
        target_class_code: str = None,
    ):
        # The host ID. You can log on to the ApsaraDB for MyBase console and go to the **Hosts** page to view the host ID.
        # 
        # This parameter is required.
        self.dedicated_host_id = dedicated_host_id
        self.owner_id = owner_id
        # The [region ID](https://help.aliyun.com/document_detail/198326.html).
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The time when you want to upgrade the specifications of the host. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # >  This parameter must be specified only when SwitchTimeMode is set to 2.
        self.switch_time = switch_time
        # The execution mode that is used to upgrade host specifications. Valid values:
        # 
        # *   **0** (default): immediately upgrades host specifications.
        # *   **2**: upgrades host specifications at a specified point in time.
        # 
        # >  If you set this parameter to **2**, you must specify **SwitchTime**.
        self.switch_time_mode = switch_time_mode
        # The instance type to which you want the host to be upgraded. For more information, see [Host specification details](https://help.aliyun.com/document_detail/206343.html).
        # 
        # This parameter is required.
        self.target_class_code = target_class_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.switch_time is not None:
            result['SwitchTime'] = self.switch_time
        if self.switch_time_mode is not None:
            result['SwitchTimeMode'] = self.switch_time_mode
        if self.target_class_code is not None:
            result['TargetClassCode'] = self.target_class_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SwitchTime') is not None:
            self.switch_time = m.get('SwitchTime')
        if m.get('SwitchTimeMode') is not None:
            self.switch_time_mode = m.get('SwitchTimeMode')
        if m.get('TargetClassCode') is not None:
            self.target_class_code = m.get('TargetClassCode')
        return self


class ModifyDedicatedHostClassResponseBody(TeaModel):
    def __init__(
        self,
        dedicated_host_id: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        # The host ID.
        self.dedicated_host_id = dedicated_host_id
        # The request ID.
        self.request_id = request_id
        # The task ID.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ModifyDedicatedHostClassResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDedicatedHostClassResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyDedicatedHostClassResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDedicatedHostGroupAttributeRequest(TeaModel):
    def __init__(
        self,
        allocation_policy: str = None,
        cpu_allocation_ratio: int = None,
        dedicated_host_group_desc: str = None,
        dedicated_host_group_id: str = None,
        disk_allocation_ratio: int = None,
        host_replace_policy: str = None,
        mem_allocation_ratio: int = None,
        open_permission: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The policy that is used to allocate resources in the dedicated cluster. Valid values:
        # 
        # *   **Evenly**: The system preferentially deploys database instances on the hosts where no resources or fewer resources are allocated. This maximizes system stability.
        # *   **Intensively**: The system preferentially deploys database instances on the hosts that are created earlier and have more allocated resources. This maximizes resource utilization.
        self.allocation_policy = allocation_policy
        # The CPU overcommit ratio of the dedicated cluster. Valid values: **100** to **300**.
        # 
        # >  If you change the CPU overcommit ratio to **300%**, the total CPU resources of all instances are three times the actual CPU resources. This maximizes the use of CPU resources.
        self.cpu_allocation_ratio = cpu_allocation_ratio
        # The name of the dedicated cluster.
        self.dedicated_host_group_desc = dedicated_host_group_desc
        # The dedicated cluster ID.
        # 
        # >  You can log on to the ApsaraDB for MyBase console and go to the Dedicated Clusters page to view the dedicated cluster ID.
        # 
        # This parameter is required.
        self.dedicated_host_group_id = dedicated_host_group_id
        # The storage overcommit ratio of the dedicated cluster. Valid values: **100** to **200**.
        self.disk_allocation_ratio = disk_allocation_ratio
        # The policy that is used to handle host failures. Valid values:
        # 
        # *   **Auto**: The system automatically replaces faulty hosts.
        # *   **Manual**: You must manually replace faulty hosts.
        # 
        # >  You can select a policy based on your business requirements only for dedicated clusters that run **MySQL**. For dedicated clusters that run other database engines, the default value Auto is used.
        self.host_replace_policy = host_replace_policy
        # The maximum memory usage of each host in the dedicated cluster. Valid values: **0** to **100**.
        self.mem_allocation_ratio = mem_allocation_ratio
        # Specifies whether to grant the host OS permissions. Valid values:
        # 
        # *   **0**: no.
        # *   **1**: yes.
        # 
        # >  You can grant the host OS permissions based on your business requirements only when you create dedicated clusters that run **MySQL, SQL Server, or PostgreSQL**. For dedicated clusters that run other database engines, the default value 0 is used.
        self.open_permission = open_permission
        self.owner_id = owner_id
        # The region ID of the dedicated cluster. For more information, see [Region IDs](https://help.aliyun.com/document_detail/198326.html).
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allocation_policy is not None:
            result['AllocationPolicy'] = self.allocation_policy
        if self.cpu_allocation_ratio is not None:
            result['CpuAllocationRatio'] = self.cpu_allocation_ratio
        if self.dedicated_host_group_desc is not None:
            result['DedicatedHostGroupDesc'] = self.dedicated_host_group_desc
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        if self.disk_allocation_ratio is not None:
            result['DiskAllocationRatio'] = self.disk_allocation_ratio
        if self.host_replace_policy is not None:
            result['HostReplacePolicy'] = self.host_replace_policy
        if self.mem_allocation_ratio is not None:
            result['MemAllocationRatio'] = self.mem_allocation_ratio
        if self.open_permission is not None:
            result['OpenPermission'] = self.open_permission
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
        if m.get('AllocationPolicy') is not None:
            self.allocation_policy = m.get('AllocationPolicy')
        if m.get('CpuAllocationRatio') is not None:
            self.cpu_allocation_ratio = m.get('CpuAllocationRatio')
        if m.get('DedicatedHostGroupDesc') is not None:
            self.dedicated_host_group_desc = m.get('DedicatedHostGroupDesc')
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        if m.get('DiskAllocationRatio') is not None:
            self.disk_allocation_ratio = m.get('DiskAllocationRatio')
        if m.get('HostReplacePolicy') is not None:
            self.host_replace_policy = m.get('HostReplacePolicy')
        if m.get('MemAllocationRatio') is not None:
            self.mem_allocation_ratio = m.get('MemAllocationRatio')
        if m.get('OpenPermission') is not None:
            self.open_permission = m.get('OpenPermission')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ModifyDedicatedHostGroupAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDedicatedHostGroupAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDedicatedHostGroupAttributeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyDedicatedHostGroupAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDedicatedHostPasswordRequest(TeaModel):
    def __init__(
        self,
        dedicated_host_id: str = None,
        new_password: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The host ID. You can call the [DescribeDedicatedHosts](https://help.aliyun.com/document_detail/200944.html) operation to query the host ID.
        # 
        # This parameter is required.
        self.dedicated_host_id = dedicated_host_id
        # The new password.
        # 
        # *   The password must be 8 to 32 characters in length.
        # *   The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters.
        # *   The password can contain the following special characters: `! @ # $ % ^ & * ( ) _ + - =`
        # 
        # >  If your dedicated cluster runs SQL Server, the password cannot contain the account name (case-insensitive).
        # 
        # This parameter is required.
        self.new_password = new_password
        self.owner_id = owner_id
        # The region ID of the host. You can call the [DescribeDedicatedHostAttribute](https://help.aliyun.com/document_detail/213010.html) operation to query the region ID.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.new_password is not None:
            result['NewPassword'] = self.new_password
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
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('NewPassword') is not None:
            self.new_password = m.get('NewPassword')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ModifyDedicatedHostPasswordResponseBody(TeaModel):
    def __init__(
        self,
        dedicated_host_name: str = None,
        request_id: str = None,
    ):
        # The name of the host.
        self.dedicated_host_name = dedicated_host_name
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_host_name is not None:
            result['DedicatedHostName'] = self.dedicated_host_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedHostName') is not None:
            self.dedicated_host_name = m.get('DedicatedHostName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDedicatedHostPasswordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDedicatedHostPasswordResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyDedicatedHostPasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryHostBaseInfoByInstanceRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        self.owner_id = owner_id
        # The region ID of the instance. For more information, see [Region IDs](https://help.aliyun.com/document_detail/198326.html).
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
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
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryHostBaseInfoByInstanceResponseBodyHostInstanceConsoleInfos(TeaModel):
    def __init__(
        self,
        cluster_name: str = None,
        engine: str = None,
        engine_version: str = None,
        expired_time: str = None,
        host_name: str = None,
        ip: str = None,
        port: str = None,
        role: str = None,
        status: str = None,
        vpc_id: str = None,
    ):
        # The instance type of the instance.
        self.cluster_name = cluster_name
        # The database engine of the instance.
        self.engine = engine
        # The version of the database engine.
        self.engine_version = engine_version
        # The expiration time of the instance.
        self.expired_time = expired_time
        # The name of the host on which the instance is deployed.
        self.host_name = host_name
        # The IP address of the host on which the instance is deployed.
        self.ip = ip
        # The port number of the host on which the instance is deployed.
        self.port = port
        # The role of the instance.
        self.role = role
        # The state of the instance.
        self.status = status
        # The virtual private cloud (VPC) ID of the host on which the instance is deployed.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.port is not None:
            result['Port'] = self.port
        if self.role is not None:
            result['Role'] = self.role
        if self.status is not None:
            result['Status'] = self.status
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class QueryHostBaseInfoByInstanceResponseBody(TeaModel):
    def __init__(
        self,
        host_instance_console_infos: List[QueryHostBaseInfoByInstanceResponseBodyHostInstanceConsoleInfos] = None,
        request_id: str = None,
    ):
        # The queried host and instance information.
        self.host_instance_console_infos = host_instance_console_infos
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.host_instance_console_infos:
            for k in self.host_instance_console_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HostInstanceConsoleInfos'] = []
        if self.host_instance_console_infos is not None:
            for k in self.host_instance_console_infos:
                result['HostInstanceConsoleInfos'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.host_instance_console_infos = []
        if m.get('HostInstanceConsoleInfos') is not None:
            for k in m.get('HostInstanceConsoleInfos'):
                temp_model = QueryHostBaseInfoByInstanceResponseBodyHostInstanceConsoleInfos()
                self.host_instance_console_infos.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryHostBaseInfoByInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryHostBaseInfoByInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryHostBaseInfoByInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryHostInstanceConsoleInfoRequest(TeaModel):
    def __init__(
        self,
        dedicated_host_id: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The host ID. You can log on to the ApsaraDB for MyBase console and go to the **Hosts** page to view the host ID.
        # 
        # This parameter is required.
        self.dedicated_host_id = dedicated_host_id
        self.owner_id = owner_id
        # The region ID of the host. You can log on to the ApsaraDB for MyBase console to view the [region ID](https://help.aliyun.com/document_detail/198326.html).
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
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
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryHostInstanceConsoleInfoResponseBodyHostInstanceConsoleInfosPerfInfo(TeaModel):
    def __init__(
        self,
        cpu_ratio: float = None,
        disk_curr: float = None,
        mem_ratio: float = None,
        perf_idb_pio: float = None,
    ):
        # The number of CPU cores of the host.
        self.cpu_ratio = cpu_ratio
        # The disk storage of the host. Unit: GB.
        self.disk_curr = disk_curr
        # The memory size of the host. Unit: GB.
        self.mem_ratio = mem_ratio
        # The number of physical I/O operations performed on the host.
        self.perf_idb_pio = perf_idb_pio

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_ratio is not None:
            result['CpuRatio'] = self.cpu_ratio
        if self.disk_curr is not None:
            result['DiskCurr'] = self.disk_curr
        if self.mem_ratio is not None:
            result['MemRatio'] = self.mem_ratio
        if self.perf_idb_pio is not None:
            result['PerfIdbPio'] = self.perf_idb_pio
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuRatio') is not None:
            self.cpu_ratio = m.get('CpuRatio')
        if m.get('DiskCurr') is not None:
            self.disk_curr = m.get('DiskCurr')
        if m.get('MemRatio') is not None:
            self.mem_ratio = m.get('MemRatio')
        if m.get('PerfIdbPio') is not None:
            self.perf_idb_pio = m.get('PerfIdbPio')
        return self


class QueryHostInstanceConsoleInfoResponseBodyHostInstanceConsoleInfos(TeaModel):
    def __init__(
        self,
        cpu_cores: int = None,
        cpu_increase_ratio_value: int = None,
        dbinstance_description: str = None,
        dbinstance_id: str = None,
        disk_size: int = None,
        engine: str = None,
        engine_version: str = None,
        ip: str = None,
        level_name: str = None,
        max_conn_increase_ratio_value: int = None,
        mem_size: int = None,
        memory_increase_ratio_value: int = None,
        perf_info: QueryHostInstanceConsoleInfoResponseBodyHostInstanceConsoleInfosPerfInfo = None,
        port: str = None,
        role: str = None,
        status: str = None,
    ):
        # The number of CPU cores of the instance.
        self.cpu_cores = cpu_cores
        # The maximum number of CPU cores of the instance.
        self.cpu_increase_ratio_value = cpu_increase_ratio_value
        # The description of the instance.
        self.dbinstance_description = dbinstance_description
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        # The storage capacity of the instance. Unit: GB.
        self.disk_size = disk_size
        # The database engine of the instance.
        self.engine = engine
        # The version of the database engine.
        self.engine_version = engine_version
        # The IP address of the host on which the instance is deployed.
        self.ip = ip
        # The instance type of the instance.
        self.level_name = level_name
        # The maximum number of connections to the instance.
        self.max_conn_increase_ratio_value = max_conn_increase_ratio_value
        # The memory size of the instance. Unit: GB.
        self.mem_size = mem_size
        # The maximum memory size of the instance.
        self.memory_increase_ratio_value = memory_increase_ratio_value
        # The performance information of the host on which the instance is deployed.
        self.perf_info = perf_info
        # The port number of the host.
        self.port = port
        # The role of the instance.
        self.role = role
        # The state of the instance.
        self.status = status

    def validate(self):
        if self.perf_info:
            self.perf_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_cores is not None:
            result['CpuCores'] = self.cpu_cores
        if self.cpu_increase_ratio_value is not None:
            result['CpuIncreaseRatioValue'] = self.cpu_increase_ratio_value
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.level_name is not None:
            result['LevelName'] = self.level_name
        if self.max_conn_increase_ratio_value is not None:
            result['MaxConnIncreaseRatioValue'] = self.max_conn_increase_ratio_value
        if self.mem_size is not None:
            result['MemSize'] = self.mem_size
        if self.memory_increase_ratio_value is not None:
            result['MemoryIncreaseRatioValue'] = self.memory_increase_ratio_value
        if self.perf_info is not None:
            result['PerfInfo'] = self.perf_info.to_map()
        if self.port is not None:
            result['Port'] = self.port
        if self.role is not None:
            result['Role'] = self.role
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuCores') is not None:
            self.cpu_cores = m.get('CpuCores')
        if m.get('CpuIncreaseRatioValue') is not None:
            self.cpu_increase_ratio_value = m.get('CpuIncreaseRatioValue')
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('LevelName') is not None:
            self.level_name = m.get('LevelName')
        if m.get('MaxConnIncreaseRatioValue') is not None:
            self.max_conn_increase_ratio_value = m.get('MaxConnIncreaseRatioValue')
        if m.get('MemSize') is not None:
            self.mem_size = m.get('MemSize')
        if m.get('MemoryIncreaseRatioValue') is not None:
            self.memory_increase_ratio_value = m.get('MemoryIncreaseRatioValue')
        if m.get('PerfInfo') is not None:
            temp_model = QueryHostInstanceConsoleInfoResponseBodyHostInstanceConsoleInfosPerfInfo()
            self.perf_info = temp_model.from_map(m['PerfInfo'])
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryHostInstanceConsoleInfoResponseBody(TeaModel):
    def __init__(
        self,
        host_instance_console_infos: List[QueryHostInstanceConsoleInfoResponseBodyHostInstanceConsoleInfos] = None,
        request_id: str = None,
    ):
        # The queried instances.
        self.host_instance_console_infos = host_instance_console_infos
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.host_instance_console_infos:
            for k in self.host_instance_console_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HostInstanceConsoleInfos'] = []
        if self.host_instance_console_infos is not None:
            for k in self.host_instance_console_infos:
                result['HostInstanceConsoleInfos'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.host_instance_console_infos = []
        if m.get('HostInstanceConsoleInfos') is not None:
            for k in m.get('HostInstanceConsoleInfos'):
                temp_model = QueryHostInstanceConsoleInfoResponseBodyHostInstanceConsoleInfos()
                self.host_instance_console_infos.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryHostInstanceConsoleInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryHostInstanceConsoleInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryHostInstanceConsoleInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReplaceDedicatedHostRequest(TeaModel):
    def __init__(
        self,
        dedicated_host_id: str = None,
        failover_mode: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The host ID. You can call the [DescribeDedicatedHosts](https://help.aliyun.com/document_detail/200944.html) operation to query the host ID.
        # 
        # This parameter is required.
        self.dedicated_host_id = dedicated_host_id
        # The switchover method of the primary instance. Valid values:
        # 
        # *   **MaintainTime** (default): The system performs a switchover within a maintenance window. The system switches workloads from the primary instance on the host to the secondary instance on another host, and then restarts the current host. This prevents service interruptions.
        # *   **Immediate**: The system immediately restarts the host.
        # 
        # This parameter is required.
        self.failover_mode = failover_mode
        self.owner_id = owner_id
        # The region ID of the host. You can call the [DescribeDedicatedHostAttribute](https://help.aliyun.com/document_detail/213010.html) operation to query the region ID.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.failover_mode is not None:
            result['FailoverMode'] = self.failover_mode
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
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('FailoverMode') is not None:
            self.failover_mode = m.get('FailoverMode')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ReplaceDedicatedHostResponseBody(TeaModel):
    def __init__(
        self,
        dedicated_host_id: str = None,
        request_id: str = None,
        task_id: int = None,
    ):
        # The ID of the host in the dedicated cluster.
        self.dedicated_host_id = dedicated_host_id
        # The request ID.
        self.request_id = request_id
        # The task ID.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ReplaceDedicatedHostResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReplaceDedicatedHostResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ReplaceDedicatedHostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestartDedicatedHostRequest(TeaModel):
    def __init__(
        self,
        dedicated_host_id: str = None,
        failover_mode: str = None,
        force_stop: bool = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The host ID. You can log on to the ApsaraDB for MyBase console and go to the **Hosts** page to view the host ID.
        # 
        # This parameter is required.
        self.dedicated_host_id = dedicated_host_id
        # The switchover method of the primary instance. Valid values:
        # 
        # *   **MaintainTime** (default): The system performs a switchover within a maintenance window. The system switches workloads from the primary instance on the host to the secondary instance on another host, and then restarts the current host. This prevents service interruptions.
        # *   **Immediate**: The system immediately restarts the host.
        # 
        # This parameter is required.
        self.failover_mode = failover_mode
        # Specifies whether to forcefully restart the host. Valid values:
        # 
        # *   true: The system forcefully restarts the host. If this value is used, the system powers off the host. This results in the loss of cached data that is not written to storage. Exercise caution when you select this value.
        # *   false (default): The system restarts the host normally.
        # 
        # >  This parameter takes effect only for hosts that are created in ApsaraDB MyBase for Redis dedicated clusters of the Enhanced Edition (Tair). Hosts that are created in ApsaraDB MyBase dedicated clusters that run other database engines can be restarted normally.
        self.force_stop = force_stop
        self.owner_id = owner_id
        # [The region ID](https://help.aliyun.com/document_detail/198326.html) of the host.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.failover_mode is not None:
            result['FailoverMode'] = self.failover_mode
        if self.force_stop is not None:
            result['ForceStop'] = self.force_stop
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
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('FailoverMode') is not None:
            self.failover_mode = m.get('FailoverMode')
        if m.get('ForceStop') is not None:
            self.force_stop = m.get('ForceStop')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class RestartDedicatedHostResponseBody(TeaModel):
    def __init__(
        self,
        dedicated_host_id: str = None,
        request_id: str = None,
        task_id: int = None,
    ):
        # The host ID.
        self.dedicated_host_id = dedicated_host_id
        # The request ID.
        self.request_id = request_id
        # The task ID.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class RestartDedicatedHostResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RestartDedicatedHostResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RestartDedicatedHostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N.
        # 
        # *   **N** specifies the serial number of the tag. Examples:
        # 
        #     *   **Tag.1.Key** specifies the key of the first tag.
        #     *   **Tag.2.Key** specifies the key of the second tag.
        # 
        # *   If no tag key exists, a key is automatically created.
        # 
        # This parameter is required.
        self.key = key
        # The value of tag N.
        # 
        # *   **N** specifies the serial number of the tag. Examples:
        # 
        #     *   **Tag.1.Value** specifies the value of the first tag.
        #     *   **Tag.2.Value** specifies the value of the second tag.
        # 
        # *   If no tag value exists, a value is automatically created.
        # 
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class TagResourcesRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
        tag: List[TagResourcesRequestTag] = None,
    ):
        self.owner_id = owner_id
        # The region ID of the host.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of host N. You can specify multiple host IDs.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The resource type. Set the value to DEDICATEDHOST.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tags.
        # 
        # This parameter is required.
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        all: bool = None,
        owner_id: int = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
        tag_key: List[str] = None,
    ):
        # Specifies whether to remove all tags from the host. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        # 
        # >  If you specify both this parameter and the TagKey.N parameter, this parameter does not take effect.
        self.all = all
        self.owner_id = owner_id
        # The region ID of the host.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of host N. You can specify multiple host IDs.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The resource type. Set the value to DEDICATEDHOST.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The key of tag N.
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UntagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UntagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


