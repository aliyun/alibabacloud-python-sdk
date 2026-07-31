# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class CreateInstanceRequest(DaraModel):
    def __init__(
        self,
        hibernation_options: main_models.CreateInstanceRequestHibernationOptions = None,
        private_pool_options: main_models.CreateInstanceRequestPrivatePoolOptions = None,
        system_disk: main_models.CreateInstanceRequestSystemDisk = None,
        affinity: str = None,
        arn: List[main_models.CreateInstanceRequestArn] = None,
        auto_renew: bool = None,
        auto_renew_period: int = None,
        client_token: str = None,
        cluster_id: str = None,
        credit_specification: str = None,
        data_disk: List[main_models.CreateInstanceRequestDataDisk] = None,
        dedicated_host_id: str = None,
        deletion_protection: bool = None,
        deployment_set_group_no: int = None,
        deployment_set_id: str = None,
        description: str = None,
        dry_run: bool = None,
        host_name: str = None,
        hpc_cluster_id: str = None,
        http_endpoint: str = None,
        http_put_response_hop_limit: int = None,
        http_tokens: str = None,
        image_family: str = None,
        image_id: str = None,
        inner_ip_address: str = None,
        instance_charge_type: str = None,
        instance_name: str = None,
        instance_type: str = None,
        internet_charge_type: str = None,
        internet_max_bandwidth_in: int = None,
        internet_max_bandwidth_out: int = None,
        io_optimized: str = None,
        key_pair_name: str = None,
        node_controller_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        password: str = None,
        password_inherit: bool = None,
        period: int = None,
        period_unit: str = None,
        private_ip_address: str = None,
        ram_role_name: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_enhancement_strategy: str = None,
        security_group_id: str = None,
        spot_duration: int = None,
        spot_interruption_behavior: str = None,
        spot_price_limit: float = None,
        spot_strategy: str = None,
        storage_set_id: str = None,
        storage_set_partition_number: int = None,
        tag: List[main_models.CreateInstanceRequestTag] = None,
        tenancy: str = None,
        use_additional_service: bool = None,
        user_data: str = None,
        v_switch_id: str = None,
        vlan_id: str = None,
        zone_id: str = None,
    ):
        self.hibernation_options = hibernation_options
        self.private_pool_options = private_pool_options
        self.system_disk = system_disk
        # Specifies whether the instance on a dedicated host is associated with the dedicated host. Valid values:
        self.affinity = affinity
        # > This parameter is in invitational preview and is not publicly available.
        self.arn = arn
        # Specifies whether to enable auto-renewal. This parameter takes effect only when `InstanceChargeType` is set to `PrePaid`. Valid values:
        self.auto_renew = auto_renew
        # The auto-renewal period. This parameter is required when AutoRenew is set to True.
        self.auto_renew_period = auto_renew_period
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but make sure that the token is unique among different requests. **ClientToken** can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The cluster ID of the instance.
        self.cluster_id = cluster_id
        # The running mode of the burstable instance. Valid values:
        self.credit_specification = credit_specification
        # The list of data disks.
        self.data_disk = data_disk
        # The ID of the dedicated host.
        self.dedicated_host_id = dedicated_host_id
        # The release protection attribute of the instance. Specifies whether the instance can be released from the ECS console or by calling the [DeleteInstance](https://help.aliyun.com/document_detail/25507.html) operation.
        self.deletion_protection = deletion_protection
        # The group number of the instance in the deployment set. This parameter takes effect only when the deployment set uses the high availability group strategy (AvailabilityGroup). Valid values: 1 to 7.
        self.deployment_set_group_no = deployment_set_group_no
        # The ID of the deployment set.
        self.deployment_set_id = deployment_set_id
        # The description of the instance. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # Specifies whether to perform only a dry run. Valid values:
        self.dry_run = dry_run
        # The hostname of the Elastic Compute Service server.
        self.host_name = host_name
        # The ID of the HPC cluster to which the instance belongs.
        self.hpc_cluster_id = hpc_cluster_id
        # Specifies whether to enable the access channel for instance metadata. Valid values:
        self.http_endpoint = http_endpoint
        # > This parameter is not publicly available.
        self.http_put_response_hop_limit = http_put_response_hop_limit
        # Specifies whether to forcefully use the security-hardened mode (IMDSv2) to access instance metadata. Valid values:
        self.http_tokens = http_tokens
        # The name of the image family. You can set this parameter to obtain the latest available image from the specified image family to create the instance.
        self.image_family = image_family
        # The ID of the image used to start the instance. To use an Alibaba Cloud Marketplace image, you can view the `ImageId` on the image product page. If you do not specify `ImageFamily` to select the latest available image from an image family, this parameter is required.
        self.image_id = image_id
        # The internal IP address of the instance.
        self.inner_ip_address = inner_ip_address
        # The billing method of the instance. Valid values:
        self.instance_charge_type = instance_charge_type
        # The name of the instance. The name must be 2 to 128 characters in length and can contain letters, digits, and Unicode characters classified under the letter category (including Chinese characters). The name can also contain colons (:), underscores (_), periods (.), and hyphens (-). If this parameter is not specified, the default value is the instance ID.
        self.instance_name = instance_name
        # The instance type.
        # 
        # This parameter is required.
        self.instance_type = instance_type
        # The billing method for network usage. Valid values:
        self.internet_charge_type = internet_charge_type
        # The maximum inbound public bandwidth, in Mbit/s. Valid values:
        self.internet_max_bandwidth_in = internet_max_bandwidth_in
        # The maximum outbound public bandwidth, in Mbit/s. Valid values: 0 to 100.
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        # Specifies whether the instance is an I/O optimized instance. The I/O optimization improves instance performance. Valid values:
        # The default value for [retired instance types](https://help.aliyun.com/document_detail/55263.html) is none.
        self.io_optimized = io_optimized
        # The name of the key pair.
        self.key_pair_name = key_pair_name
        # > This parameter is in invitational preview and is not publicly available.
        self.node_controller_id = node_controller_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The password of the instance. The password must be 8 to 30 characters in length and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The following special characters are supported:
        self.password = password
        # Specifies whether to use the password preset in the image. When you use this parameter, the Password parameter must be empty, and you must make sure that the image has a password configured.
        self.password_inherit = password_inherit
        # The subscription period of the instance. The unit is specified by `PeriodUnit`. This parameter takes effect and is required only when `InstanceChargeType` is set to `PrePaid`. If `DedicatedHostId` is specified, the value of this parameter cannot exceed the subscription period of the dedicated host. Valid values:
        self.period = period
        # The unit of the subscription period. Valid values:
        self.period_unit = period_unit
        # The private IP address of the instance. The IP address must be an available address within the CIDR block of the specified vSwitch (VSwitchId).
        self.private_ip_address = private_ip_address
        # The name of the instance RAM role. You can call the RAM API [ListRoles](https://help.aliyun.com/document_detail/28713.html) to query the instance RAM roles that you have created.
        self.ram_role_name = ram_role_name
        # The region ID of the instance. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the most recent list of regions.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the enterprise resource group to which the instance belongs.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Specifies whether to enable security hardening. Valid values:
        self.security_enhancement_strategy = security_enhancement_strategy
        # The ID of the security group to which the new instance belongs.
        self.security_group_id = security_group_id
        # The protection period of the spot instance, in hours. Default value: 1. Valid values:
        self.spot_duration = spot_duration
        # The interruption pattern of the spot instance. Valid values:
        self.spot_interruption_behavior = spot_interruption_behavior
        # The maximum hourly price of the instance. A maximum of three decimal places is supported. This parameter takes effect only when `SpotStrategy` is set to `SpotWithPriceLimit`.
        self.spot_price_limit = spot_price_limit
        # The bidding policy for the instance. This parameter takes effect only when `InstanceChargeType` is set to `PostPaid`. Valid values:
        self.spot_strategy = spot_strategy
        # The ID of the storage set.
        self.storage_set_id = storage_set_id
        # The maximum number of partitions in the storage set. Valid values: greater than or equal to 2.
        self.storage_set_partition_number = storage_set_partition_number
        # The tags.
        self.tag = tag
        # Specifies whether to create the instance on a dedicated host. Valid values:
        self.tenancy = tenancy
        # Specifies whether to use the virtual machine system configuration provided by Alibaba Cloud (Windows: NTP and KMS. Linux: NTP and YUM).
        self.use_additional_service = use_additional_service
        # The instance user data. The data must be encoded in Base64. The raw data can be up to 32 KB in size.
        self.user_data = user_data
        # The vSwitch ID. This parameter is required when you create a VPC-connected instance. You can call [DescribeVSwitches](https://help.aliyun.com/document_detail/35748.html) to query created vSwitches.
        self.v_switch_id = v_switch_id
        # The virtual local area network ID.
        self.vlan_id = vlan_id
        # The zone ID of the instance. For more information, call [DescribeZones](https://help.aliyun.com/document_detail/25610.html) to query the zone list.
        self.zone_id = zone_id

    def validate(self):
        if self.hibernation_options:
            self.hibernation_options.validate()
        if self.private_pool_options:
            self.private_pool_options.validate()
        if self.system_disk:
            self.system_disk.validate()
        if self.arn:
            for v1 in self.arn:
                 if v1:
                    v1.validate()
        if self.data_disk:
            for v1 in self.data_disk:
                 if v1:
                    v1.validate()
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hibernation_options is not None:
            result['HibernationOptions'] = self.hibernation_options.to_map()

        if self.private_pool_options is not None:
            result['PrivatePoolOptions'] = self.private_pool_options.to_map()

        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk.to_map()

        if self.affinity is not None:
            result['Affinity'] = self.affinity

        result['Arn'] = []
        if self.arn is not None:
            for k1 in self.arn:
                result['Arn'].append(k1.to_map() if k1 else None)

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.credit_specification is not None:
            result['CreditSpecification'] = self.credit_specification

        result['DataDisk'] = []
        if self.data_disk is not None:
            for k1 in self.data_disk:
                result['DataDisk'].append(k1.to_map() if k1 else None)

        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id

        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection

        if self.deployment_set_group_no is not None:
            result['DeploymentSetGroupNo'] = self.deployment_set_group_no

        if self.deployment_set_id is not None:
            result['DeploymentSetId'] = self.deployment_set_id

        if self.description is not None:
            result['Description'] = self.description

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.host_name is not None:
            result['HostName'] = self.host_name

        if self.hpc_cluster_id is not None:
            result['HpcClusterId'] = self.hpc_cluster_id

        if self.http_endpoint is not None:
            result['HttpEndpoint'] = self.http_endpoint

        if self.http_put_response_hop_limit is not None:
            result['HttpPutResponseHopLimit'] = self.http_put_response_hop_limit

        if self.http_tokens is not None:
            result['HttpTokens'] = self.http_tokens

        if self.image_family is not None:
            result['ImageFamily'] = self.image_family

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.inner_ip_address is not None:
            result['InnerIpAddress'] = self.inner_ip_address

        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type

        if self.internet_max_bandwidth_in is not None:
            result['InternetMaxBandwidthIn'] = self.internet_max_bandwidth_in

        if self.internet_max_bandwidth_out is not None:
            result['InternetMaxBandwidthOut'] = self.internet_max_bandwidth_out

        if self.io_optimized is not None:
            result['IoOptimized'] = self.io_optimized

        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name

        if self.node_controller_id is not None:
            result['NodeControllerId'] = self.node_controller_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.password is not None:
            result['Password'] = self.password

        if self.password_inherit is not None:
            result['PasswordInherit'] = self.password_inherit

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address

        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.security_enhancement_strategy is not None:
            result['SecurityEnhancementStrategy'] = self.security_enhancement_strategy

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.spot_duration is not None:
            result['SpotDuration'] = self.spot_duration

        if self.spot_interruption_behavior is not None:
            result['SpotInterruptionBehavior'] = self.spot_interruption_behavior

        if self.spot_price_limit is not None:
            result['SpotPriceLimit'] = self.spot_price_limit

        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy

        if self.storage_set_id is not None:
            result['StorageSetId'] = self.storage_set_id

        if self.storage_set_partition_number is not None:
            result['StorageSetPartitionNumber'] = self.storage_set_partition_number

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.tenancy is not None:
            result['Tenancy'] = self.tenancy

        if self.use_additional_service is not None:
            result['UseAdditionalService'] = self.use_additional_service

        if self.user_data is not None:
            result['UserData'] = self.user_data

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vlan_id is not None:
            result['VlanId'] = self.vlan_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HibernationOptions') is not None:
            temp_model = main_models.CreateInstanceRequestHibernationOptions()
            self.hibernation_options = temp_model.from_map(m.get('HibernationOptions'))

        if m.get('PrivatePoolOptions') is not None:
            temp_model = main_models.CreateInstanceRequestPrivatePoolOptions()
            self.private_pool_options = temp_model.from_map(m.get('PrivatePoolOptions'))

        if m.get('SystemDisk') is not None:
            temp_model = main_models.CreateInstanceRequestSystemDisk()
            self.system_disk = temp_model.from_map(m.get('SystemDisk'))

        if m.get('Affinity') is not None:
            self.affinity = m.get('Affinity')

        self.arn = []
        if m.get('Arn') is not None:
            for k1 in m.get('Arn'):
                temp_model = main_models.CreateInstanceRequestArn()
                self.arn.append(temp_model.from_map(k1))

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('CreditSpecification') is not None:
            self.credit_specification = m.get('CreditSpecification')

        self.data_disk = []
        if m.get('DataDisk') is not None:
            for k1 in m.get('DataDisk'):
                temp_model = main_models.CreateInstanceRequestDataDisk()
                self.data_disk.append(temp_model.from_map(k1))

        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')

        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')

        if m.get('DeploymentSetGroupNo') is not None:
            self.deployment_set_group_no = m.get('DeploymentSetGroupNo')

        if m.get('DeploymentSetId') is not None:
            self.deployment_set_id = m.get('DeploymentSetId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')

        if m.get('HpcClusterId') is not None:
            self.hpc_cluster_id = m.get('HpcClusterId')

        if m.get('HttpEndpoint') is not None:
            self.http_endpoint = m.get('HttpEndpoint')

        if m.get('HttpPutResponseHopLimit') is not None:
            self.http_put_response_hop_limit = m.get('HttpPutResponseHopLimit')

        if m.get('HttpTokens') is not None:
            self.http_tokens = m.get('HttpTokens')

        if m.get('ImageFamily') is not None:
            self.image_family = m.get('ImageFamily')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('InnerIpAddress') is not None:
            self.inner_ip_address = m.get('InnerIpAddress')

        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')

        if m.get('InternetMaxBandwidthIn') is not None:
            self.internet_max_bandwidth_in = m.get('InternetMaxBandwidthIn')

        if m.get('InternetMaxBandwidthOut') is not None:
            self.internet_max_bandwidth_out = m.get('InternetMaxBandwidthOut')

        if m.get('IoOptimized') is not None:
            self.io_optimized = m.get('IoOptimized')

        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')

        if m.get('NodeControllerId') is not None:
            self.node_controller_id = m.get('NodeControllerId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('PasswordInherit') is not None:
            self.password_inherit = m.get('PasswordInherit')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')

        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecurityEnhancementStrategy') is not None:
            self.security_enhancement_strategy = m.get('SecurityEnhancementStrategy')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('SpotDuration') is not None:
            self.spot_duration = m.get('SpotDuration')

        if m.get('SpotInterruptionBehavior') is not None:
            self.spot_interruption_behavior = m.get('SpotInterruptionBehavior')

        if m.get('SpotPriceLimit') is not None:
            self.spot_price_limit = m.get('SpotPriceLimit')

        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')

        if m.get('StorageSetId') is not None:
            self.storage_set_id = m.get('StorageSetId')

        if m.get('StorageSetPartitionNumber') is not None:
            self.storage_set_partition_number = m.get('StorageSetPartitionNumber')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateInstanceRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('Tenancy') is not None:
            self.tenancy = m.get('Tenancy')

        if m.get('UseAdditionalService') is not None:
            self.use_additional_service = m.get('UseAdditionalService')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VlanId') is not None:
            self.vlan_id = m.get('VlanId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class CreateInstanceRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the instance, disk, and primary ENI. Valid values of N: 1 to 20. The tag key cannot be an empty string. The tag key can be up to 128 characters in length and cannot start with `aliyun` or `acs:`. The tag key cannot contain `http://` or `https://`.
        self.key = key
        # The tag value of the instance, disk, and primary ENI. Valid values of N: 1 to 20. The tag value can be an empty string. The tag value can be up to 128 characters in length and cannot contain `http://` or `https://`.
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

class CreateInstanceRequestDataDisk(DaraModel):
    def __init__(
        self,
        category: str = None,
        delete_with_instance: bool = None,
        description: str = None,
        device: str = None,
        disk_name: str = None,
        encrypt_algorithm: str = None,
        encrypted: bool = None,
        kmskey_id: str = None,
        performance_level: str = None,
        size: int = None,
        snapshot_id: str = None,
        storage_cluster_id: str = None,
    ):
        # The category of data disk N. Valid values:
        self.category = category
        # Specifies whether to release the data disk when the instance is released.
        self.delete_with_instance = delete_with_instance
        # The description of the data disk. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # The mount point of the data disk.
        self.device = device
        # The name of the data disk. The name must be 2 to 128 characters in length and can contain letters, digits, and Unicode characters classified under the letter category (including Chinese characters). The name can also contain colons (:), underscores (_), periods (.), and hyphens (-).
        self.disk_name = disk_name
        # > This parameter is not publicly available.
        self.encrypt_algorithm = encrypt_algorithm
        # Specifies whether to encrypt data disk N.
        self.encrypted = encrypted
        # The Key Management Service (KMS) key ID for the disk.
        self.kmskey_id = kmskey_id
        # The performance level (PL) of the enterprise SSD used as a data disk. The value of N must be the same as that in `DataDisk.N.Category=cloud_essd`. Settings for the performance level. If the data disk is a standard SSD, this parameter is ignored. Valid values:
        self.performance_level = performance_level
        # The size of data disk N, in GiB. Valid values of N: 1 to 16. Valid values:
        self.size = size
        # The snapshot ID used to create data disk N. Valid values of N: 1 to 16.
        self.snapshot_id = snapshot_id
        # The ID of the dedicated block storage cluster. If you want to use disks in a dedicated block storage cluster as data disks when you create an ECS instance, set this parameter.
        self.storage_cluster_id = storage_cluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.delete_with_instance is not None:
            result['DeleteWithInstance'] = self.delete_with_instance

        if self.description is not None:
            result['Description'] = self.description

        if self.device is not None:
            result['Device'] = self.device

        if self.disk_name is not None:
            result['DiskName'] = self.disk_name

        if self.encrypt_algorithm is not None:
            result['EncryptAlgorithm'] = self.encrypt_algorithm

        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted

        if self.kmskey_id is not None:
            result['KMSKeyId'] = self.kmskey_id

        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level

        if self.size is not None:
            result['Size'] = self.size

        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id

        if self.storage_cluster_id is not None:
            result['StorageClusterId'] = self.storage_cluster_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('DeleteWithInstance') is not None:
            self.delete_with_instance = m.get('DeleteWithInstance')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Device') is not None:
            self.device = m.get('Device')

        if m.get('DiskName') is not None:
            self.disk_name = m.get('DiskName')

        if m.get('EncryptAlgorithm') is not None:
            self.encrypt_algorithm = m.get('EncryptAlgorithm')

        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')

        if m.get('KMSKeyId') is not None:
            self.kmskey_id = m.get('KMSKeyId')

        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')

        if m.get('StorageClusterId') is not None:
            self.storage_cluster_id = m.get('StorageClusterId')

        return self

class CreateInstanceRequestArn(DaraModel):
    def __init__(
        self,
        assume_role_for: int = None,
        role_type: str = None,
        rolearn: str = None,
    ):
        # > This parameter is in invitational preview and is not publicly available.
        self.assume_role_for = assume_role_for
        # > This parameter is in invitational preview and is not publicly available.
        self.role_type = role_type
        # > This parameter is in invitational preview and is not publicly available.
        self.rolearn = rolearn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assume_role_for is not None:
            result['AssumeRoleFor'] = self.assume_role_for

        if self.role_type is not None:
            result['RoleType'] = self.role_type

        if self.rolearn is not None:
            result['Rolearn'] = self.rolearn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssumeRoleFor') is not None:
            self.assume_role_for = m.get('AssumeRoleFor')

        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')

        if m.get('Rolearn') is not None:
            self.rolearn = m.get('Rolearn')

        return self

class CreateInstanceRequestSystemDisk(DaraModel):
    def __init__(
        self,
        category: str = None,
        description: str = None,
        disk_name: str = None,
        performance_level: str = None,
        size: int = None,
        storage_cluster_id: str = None,
    ):
        # The category of the system disk. Valid values:
        self.category = category
        # The description of the system disk. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # The name of the system disk. The name must be 2 to 128 characters in length and can contain letters, digits, and Unicode characters classified under the letter category (including Chinese characters). The name can also contain colons (:), underscores (_), periods (.), and hyphens (-).
        self.disk_name = disk_name
        # The performance level (PL) of the enterprise SSD (ESSD) used as the system disk. Settings for the performance level. If the system disk is a standard SSD, this parameter is ignored. Valid values:
        self.performance_level = performance_level
        # The size of the system disk, in GiB. Valid values:
        self.size = size
        # The ID of the dedicated block storage cluster. To use a disk in a dedicated block storage cluster as the system disk when you create an ECS instance, specify this parameter.
        self.storage_cluster_id = storage_cluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.description is not None:
            result['Description'] = self.description

        if self.disk_name is not None:
            result['DiskName'] = self.disk_name

        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level

        if self.size is not None:
            result['Size'] = self.size

        if self.storage_cluster_id is not None:
            result['StorageClusterId'] = self.storage_cluster_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DiskName') is not None:
            self.disk_name = m.get('DiskName')

        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('StorageClusterId') is not None:
            self.storage_cluster_id = m.get('StorageClusterId')

        return self

class CreateInstanceRequestPrivatePoolOptions(DaraModel):
    def __init__(
        self,
        id: str = None,
        match_criteria: str = None,
    ):
        # The ID of the private pool. The ID of an elasticity assurance or capacity reservation.
        self.id = id
        # The private pool option for the instance launch. A private pool is generated when an elasticity assurance or capacity reservation takes effect. You can select a private pool when you start an instance. Valid values:
        self.match_criteria = match_criteria

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.match_criteria is not None:
            result['MatchCriteria'] = self.match_criteria

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MatchCriteria') is not None:
            self.match_criteria = m.get('MatchCriteria')

        return self

class CreateInstanceRequestHibernationOptions(DaraModel):
    def __init__(
        self,
        configured: bool = None,
    ):
        # > This parameter is in invitational preview and is not publicly available.
        self.configured = configured

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.configured is not None:
            result['Configured'] = self.configured

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Configured') is not None:
            self.configured = m.get('Configured')

        return self

