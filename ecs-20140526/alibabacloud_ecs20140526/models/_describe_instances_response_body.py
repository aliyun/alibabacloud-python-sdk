# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeInstancesResponseBody(DaraModel):
    def __init__(
        self,
        instances: main_models.DescribeInstancesResponseBodyInstances = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Details about the queried instances.
        self.instances = instances
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        self.next_token = next_token
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of instances queried.
        # 
        # >  If you specify the `MaxResults` and `NextToken` request parameters to perform a paged query, the value of the `TotalCount` response parameter is invalid.
        self.total_count = total_count

    def validate(self):
        if self.instances:
            self.instances.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instances is not None:
            result['Instances'] = self.instances.to_map()

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Instances') is not None:
            temp_model = main_models.DescribeInstancesResponseBodyInstances()
            self.instances = temp_model.from_map(m.get('Instances'))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeInstancesResponseBodyInstances(DaraModel):
    def __init__(
        self,
        instance: List[main_models.DescribeInstancesResponseBodyInstancesInstance] = None,
    ):
        self.instance = instance

    def validate(self):
        if self.instance:
            for v1 in self.instance:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Instance'] = []
        if self.instance is not None:
            for k1 in self.instance:
                result['Instance'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance = []
        if m.get('Instance') is not None:
            for k1 in m.get('Instance'):
                temp_model = main_models.DescribeInstancesResponseBodyInstancesInstance()
                self.instance.append(temp_model.from_map(k1))

        return self

class DescribeInstancesResponseBodyInstancesInstance(DaraModel):
    def __init__(
        self,
        additional_info: main_models.DescribeInstancesResponseBodyInstancesInstanceAdditionalInfo = None,
        auto_release_time: str = None,
        clock_options: main_models.DescribeInstancesResponseBodyInstancesInstanceClockOptions = None,
        cluster_id: str = None,
        cpu: int = None,
        cpu_options: main_models.DescribeInstancesResponseBodyInstancesInstanceCpuOptions = None,
        creation_time: str = None,
        credit_specification: str = None,
        dedicated_host_attribute: main_models.DescribeInstancesResponseBodyInstancesInstanceDedicatedHostAttribute = None,
        dedicated_instance_attribute: main_models.DescribeInstancesResponseBodyInstancesInstanceDedicatedInstanceAttribute = None,
        deletion_protection: bool = None,
        deployment_set_group_no: int = None,
        deployment_set_id: str = None,
        description: str = None,
        device_available: bool = None,
        ecs_capacity_reservation_attr: main_models.DescribeInstancesResponseBodyInstancesInstanceEcsCapacityReservationAttr = None,
        eip_address: main_models.DescribeInstancesResponseBodyInstancesInstanceEipAddress = None,
        enable_nvs: bool = None,
        expired_time: str = None,
        gpuamount: int = None,
        gpuspec: str = None,
        hibernation_options: main_models.DescribeInstancesResponseBodyInstancesInstanceHibernationOptions = None,
        host_name: str = None,
        hpc_cluster_id: str = None,
        isp: str = None,
        image_id: str = None,
        image_options: main_models.DescribeInstancesResponseBodyInstancesInstanceImageOptions = None,
        inner_ip_address: main_models.DescribeInstancesResponseBodyInstancesInstanceInnerIpAddress = None,
        instance_charge_type: str = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_network_type: str = None,
        instance_type: str = None,
        instance_type_family: str = None,
        internet_charge_type: str = None,
        internet_max_bandwidth_in: int = None,
        internet_max_bandwidth_out: int = None,
        io_optimized: bool = None,
        key_pair_name: str = None,
        local_storage_amount: int = None,
        local_storage_capacity: int = None,
        memory: int = None,
        metadata_options: main_models.DescribeInstancesResponseBodyInstancesInstanceMetadataOptions = None,
        network_interfaces: main_models.DescribeInstancesResponseBodyInstancesInstanceNetworkInterfaces = None,
        osname: str = None,
        osname_en: str = None,
        ostype: str = None,
        operation_locks: main_models.DescribeInstancesResponseBodyInstancesInstanceOperationLocks = None,
        private_dns_name_options: main_models.DescribeInstancesResponseBodyInstancesInstancePrivateDnsNameOptions = None,
        public_ip_address: main_models.DescribeInstancesResponseBodyInstancesInstancePublicIpAddress = None,
        rdma_ip_address: main_models.DescribeInstancesResponseBodyInstancesInstanceRdmaIpAddress = None,
        recyclable: bool = None,
        region_id: str = None,
        resource_group_id: str = None,
        sale_cycle: str = None,
        security_group_ids: main_models.DescribeInstancesResponseBodyInstancesInstanceSecurityGroupIds = None,
        serial_number: str = None,
        spot_duration: int = None,
        spot_interruption_behavior: str = None,
        spot_price_limit: float = None,
        spot_strategy: str = None,
        start_time: str = None,
        status: str = None,
        stopped_mode: str = None,
        tags: main_models.DescribeInstancesResponseBodyInstancesInstanceTags = None,
        vlan_id: str = None,
        vpc_attributes: main_models.DescribeInstancesResponseBodyInstancesInstanceVpcAttributes = None,
        zone_id: str = None,
    ):
        # >  This parameter is in invitational preview and is not publicly available.
        self.additional_info = additional_info
        # The automatic release time of the pay-as-you-go instance.
        self.auto_release_time = auto_release_time
        self.clock_options = clock_options
        # The ID of the cluster to which the instance belongs.
        # 
        # >  This parameter will be removed in the future. We recommend that you use other parameters to ensure future compatibility.
        self.cluster_id = cluster_id
        # The number of vCPUs.
        self.cpu = cpu
        # Details about the CPU options.
        self.cpu_options = cpu_options
        # The time when the instance was created. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. The time is displayed in UTC. For more information, see [ISO 8601](https://help.aliyun.com/document_detail/25696.html).
        self.creation_time = creation_time
        # The performance mode of the burstable instance. Valid values:
        # 
        # *   Standard: the standard mode. For more information, see the "Standard mode" section in [Overview of burstable instances](https://help.aliyun.com/document_detail/59977.html).
        # *   Unlimited: the unlimited mode. For more information, see the "Unlimited mode" section in [Overview of burstable instances](https://help.aliyun.com/document_detail/59977.html).
        self.credit_specification = credit_specification
        # The information about the dedicated host. The value is an array that consists of DedicatedHostClusterId, DedicatedHostId, and DedicatedHostName.
        self.dedicated_host_attribute = dedicated_host_attribute
        # The attributes of the instance on the dedicated host.
        self.dedicated_instance_attribute = dedicated_instance_attribute
        # Indicates whether release protection is enabled for the instance. This parameter determines whether you can use the ECS console or call the DeleteInstance operation to release the instance. Valid values:
        # 
        # *   true: Release protection is enabled for the instance.
        # *   false: Release protection is disabled for the instance.
        # 
        # >  This parameter is applicable only to pay-as-you-go instances. The release protection feature can protect instances against manual releases, but not against automatic releases.
        self.deletion_protection = deletion_protection
        # The number of the deployment set group to which the instance belongs in a deployment set.
        self.deployment_set_group_no = deployment_set_group_no
        # The ID of the deployment set to which the instance belongs.
        self.deployment_set_id = deployment_set_id
        # The description of the instance.
        self.description = description
        # Indicates whether data disks can be attached to the instance. Valid values:
        # 
        # *   true
        # *   false
        self.device_available = device_available
        # Details about the capacity reservation associated with the instance.
        self.ecs_capacity_reservation_attr = ecs_capacity_reservation_attr
        # Details about the EIP associated with the instance.
        self.eip_address = eip_address
        self.enable_nvs = enable_nvs
        # The expiration time of the instance. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. The time is displayed in UTC. For more information, see [ISO 8601](https://help.aliyun.com/document_detail/25696.html).
        self.expired_time = expired_time
        # The number of GPUs for the instance type.
        self.gpuamount = gpuamount
        # The category of GPUs for the instance type.
        self.gpuspec = gpuspec
        # >  This parameter is in invitational preview and is not publicly available.
        self.hibernation_options = hibernation_options
        # The hostname of the instance.
        self.host_name = host_name
        # The ID of the HPC cluster to which the instance belongs.
        self.hpc_cluster_id = hpc_cluster_id
        # >  This parameter is in invitational preview and is not publicly available.
        self.isp = isp
        # The image ID of the instance.
        self.image_id = image_id
        # The image options.
        self.image_options = image_options
        # The internal IP addresses of the instance located in the classic network.
        self.inner_ip_address = inner_ip_address
        # The billing method of the instance. Valid values:
        # 
        # *   PrePaid: subscription
        # *   PostPaid: pay-as-you-go
        self.instance_charge_type = instance_charge_type
        # The instance ID.
        self.instance_id = instance_id
        # The instance name.
        self.instance_name = instance_name
        # The network type of the instance. Valid values:
        # 
        # *   classic
        # *   vpc
        self.instance_network_type = instance_network_type
        # The instance type of the instance.
        self.instance_type = instance_type
        # The instance family of the instance.
        self.instance_type_family = instance_type_family
        # The billing method for network usage. Valid values:
        # 
        # *   PayByBandwidth: pay-by-bandwidth
        # *   PayByTraffic: pay-by-traffic
        self.internet_charge_type = internet_charge_type
        # The maximum inbound public bandwidth. Unit: Mbit/s.
        self.internet_max_bandwidth_in = internet_max_bandwidth_in
        # The maximum outbound public bandwidth. Unit: Mbit/s.
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        # Indicates whether the instance is an I/O optimized instance. Valid values:
        # 
        # *   true
        # *   false
        self.io_optimized = io_optimized
        # The name of the key pair.
        self.key_pair_name = key_pair_name
        # The number of local disks attached to the instance.
        self.local_storage_amount = local_storage_amount
        # The capacity of local disks attached to the instance. Unit: GiB.
        self.local_storage_capacity = local_storage_capacity
        # The memory size. Unit: MiB.
        self.memory = memory
        # Details about the metadata options.
        self.metadata_options = metadata_options
        # The ENIs attached to the instance.
        self.network_interfaces = network_interfaces
        # The name of the operating system of the instance.
        self.osname = osname
        # The English name of the operating system of the instance.
        self.osname_en = osname_en
        # The type of the operating system of the instance. Valid values:
        # 
        # *   windows: Windows operating systems
        # *   linux: Linux operating systems
        self.ostype = ostype
        # The reasons why the instance was locked.
        self.operation_locks = operation_locks
        # The private domain name options of the instance.
        # 
        # For information about the resolution of ECS private domain names, see [ECS private DNS resolution](https://help.aliyun.com/document_detail/2844797.html).
        # 
        # >  This parameter is returned only when the `AdditionalAttributes` parameter contains `PRIVATE_DNS_OPTIONS` in the request.
        self.private_dns_name_options = private_dns_name_options
        # The public IP addresses of the instance.
        self.public_ip_address = public_ip_address
        # The RDMA IP addresses of the instance in the HPC cluster.
        self.rdma_ip_address = rdma_ip_address
        # Indicates whether the instance can be recycled.
        self.recyclable = recyclable
        # The region ID of the instance.
        self.region_id = region_id
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id
        # >  The parameter is removed.
        self.sale_cycle = sale_cycle
        # The IDs of the security groups to which the instance belongs.
        self.security_group_ids = security_group_ids
        # The serial number of the instance.
        self.serial_number = serial_number
        # The protection period of the spot instance. Unit: hours. Valid values:
        # 
        # *   1: After a spot instance is created, Alibaba Cloud ensures that the instance is not automatically released within 1 hour. After the 1-hour protection period ends, the system compares the bid price with the market price and checks the resource inventory to determine whether to retain or release the instance.
        # *   0: After a spot instance is created, Alibaba Cloud does not ensure that the instance runs for 1 hour. The system compares the bid price with the market price and checks the resource inventory to determine whether to retain or release the instance.
        # 
        # Alibaba Cloud sends an ECS system event to notify you 5 minutes before the instance is released. Spot instances are billed by second. We recommend that you specify a protection period based on your business requirements.
        # 
        # >  This parameter is returned when SpotStrategy is set to SpotWithPriceLimit or SpotAsPriceGo.
        self.spot_duration = spot_duration
        # The interruption mode of the spot instance when the system initiates a spot instance interruption operation. Valid values:
        # 
        # *   Terminate: releases the spot instance.
        # *   Stop: stops the instance in economical mode.
        self.spot_interruption_behavior = spot_interruption_behavior
        # The maximum hourly price of the instance. The value can be accurate to three decimal places. This parameter is valid when SpotStrategy is set to SpotWithPriceLimit.
        self.spot_price_limit = spot_price_limit
        # The bidding policy for the pay-as-you-go instance. Valid values:
        # 
        # *   NoSpot: The instance is a regular pay-as-you-go instance.
        # *   SpotWithPriceLimit: The instance is a spot instance with a user-defined maximum hourly price.
        # *   SpotAsPriceGo: The instance is a spot instance for which the market price is automatically used as the bid price. The market price can be up to the pay-as-you-go price.
        self.spot_strategy = spot_strategy
        # The time when the instance was last started. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. The time is displayed in UTC. For more information, see [ISO 8601](https://help.aliyun.com/document_detail/25696.html).
        self.start_time = start_time
        # The status of the instance.
        self.status = status
        # Indicates whether the instance continues to be billed after it is stopped. Valid values:
        # 
        # *   KeepCharging: The instance is stopped in standard mode. Billing for the instance continues after the instance is stopped, and resources are retained for the instance.
        # *   StopCharging: The instance is stopped in economical mode. Billing for some resources of the instance stops after the instance is stopped. When the instance is stopped, its resources such as vCPUs, memory, and public IP addresses are released. The instance may be unable to restart if some required resources are out of stock in the current region.
        # *   Not-applicable: The instance does not support economical mode.
        self.stopped_mode = stopped_mode
        # The tags of the instance.
        self.tags = tags
        # The virtual LAN (VLAN) ID of the instance.
        # 
        # >  This parameter will be removed in the future. We recommend that you use other parameters to ensure future compatibility.
        self.vlan_id = vlan_id
        # The VPC attributes of the instance.
        self.vpc_attributes = vpc_attributes
        # The zone ID of the instance.
        self.zone_id = zone_id

    def validate(self):
        if self.additional_info:
            self.additional_info.validate()
        if self.clock_options:
            self.clock_options.validate()
        if self.cpu_options:
            self.cpu_options.validate()
        if self.dedicated_host_attribute:
            self.dedicated_host_attribute.validate()
        if self.dedicated_instance_attribute:
            self.dedicated_instance_attribute.validate()
        if self.ecs_capacity_reservation_attr:
            self.ecs_capacity_reservation_attr.validate()
        if self.eip_address:
            self.eip_address.validate()
        if self.hibernation_options:
            self.hibernation_options.validate()
        if self.image_options:
            self.image_options.validate()
        if self.inner_ip_address:
            self.inner_ip_address.validate()
        if self.metadata_options:
            self.metadata_options.validate()
        if self.network_interfaces:
            self.network_interfaces.validate()
        if self.operation_locks:
            self.operation_locks.validate()
        if self.private_dns_name_options:
            self.private_dns_name_options.validate()
        if self.public_ip_address:
            self.public_ip_address.validate()
        if self.rdma_ip_address:
            self.rdma_ip_address.validate()
        if self.security_group_ids:
            self.security_group_ids.validate()
        if self.tags:
            self.tags.validate()
        if self.vpc_attributes:
            self.vpc_attributes.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.additional_info is not None:
            result['AdditionalInfo'] = self.additional_info.to_map()

        if self.auto_release_time is not None:
            result['AutoReleaseTime'] = self.auto_release_time

        if self.clock_options is not None:
            result['ClockOptions'] = self.clock_options.to_map()

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.cpu_options is not None:
            result['CpuOptions'] = self.cpu_options.to_map()

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.credit_specification is not None:
            result['CreditSpecification'] = self.credit_specification

        if self.dedicated_host_attribute is not None:
            result['DedicatedHostAttribute'] = self.dedicated_host_attribute.to_map()

        if self.dedicated_instance_attribute is not None:
            result['DedicatedInstanceAttribute'] = self.dedicated_instance_attribute.to_map()

        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection

        if self.deployment_set_group_no is not None:
            result['DeploymentSetGroupNo'] = self.deployment_set_group_no

        if self.deployment_set_id is not None:
            result['DeploymentSetId'] = self.deployment_set_id

        if self.description is not None:
            result['Description'] = self.description

        if self.device_available is not None:
            result['DeviceAvailable'] = self.device_available

        if self.ecs_capacity_reservation_attr is not None:
            result['EcsCapacityReservationAttr'] = self.ecs_capacity_reservation_attr.to_map()

        if self.eip_address is not None:
            result['EipAddress'] = self.eip_address.to_map()

        if self.enable_nvs is not None:
            result['EnableNVS'] = self.enable_nvs

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.gpuamount is not None:
            result['GPUAmount'] = self.gpuamount

        if self.gpuspec is not None:
            result['GPUSpec'] = self.gpuspec

        if self.hibernation_options is not None:
            result['HibernationOptions'] = self.hibernation_options.to_map()

        if self.host_name is not None:
            result['HostName'] = self.host_name

        if self.hpc_cluster_id is not None:
            result['HpcClusterId'] = self.hpc_cluster_id

        if self.isp is not None:
            result['ISP'] = self.isp

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_options is not None:
            result['ImageOptions'] = self.image_options.to_map()

        if self.inner_ip_address is not None:
            result['InnerIpAddress'] = self.inner_ip_address.to_map()

        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_network_type is not None:
            result['InstanceNetworkType'] = self.instance_network_type

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.instance_type_family is not None:
            result['InstanceTypeFamily'] = self.instance_type_family

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

        if self.local_storage_amount is not None:
            result['LocalStorageAmount'] = self.local_storage_amount

        if self.local_storage_capacity is not None:
            result['LocalStorageCapacity'] = self.local_storage_capacity

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.metadata_options is not None:
            result['MetadataOptions'] = self.metadata_options.to_map()

        if self.network_interfaces is not None:
            result['NetworkInterfaces'] = self.network_interfaces.to_map()

        if self.osname is not None:
            result['OSName'] = self.osname

        if self.osname_en is not None:
            result['OSNameEn'] = self.osname_en

        if self.ostype is not None:
            result['OSType'] = self.ostype

        if self.operation_locks is not None:
            result['OperationLocks'] = self.operation_locks.to_map()

        if self.private_dns_name_options is not None:
            result['PrivateDnsNameOptions'] = self.private_dns_name_options.to_map()

        if self.public_ip_address is not None:
            result['PublicIpAddress'] = self.public_ip_address.to_map()

        if self.rdma_ip_address is not None:
            result['RdmaIpAddress'] = self.rdma_ip_address.to_map()

        if self.recyclable is not None:
            result['Recyclable'] = self.recyclable

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.sale_cycle is not None:
            result['SaleCycle'] = self.sale_cycle

        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids.to_map()

        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number

        if self.spot_duration is not None:
            result['SpotDuration'] = self.spot_duration

        if self.spot_interruption_behavior is not None:
            result['SpotInterruptionBehavior'] = self.spot_interruption_behavior

        if self.spot_price_limit is not None:
            result['SpotPriceLimit'] = self.spot_price_limit

        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.stopped_mode is not None:
            result['StoppedMode'] = self.stopped_mode

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.vlan_id is not None:
            result['VlanId'] = self.vlan_id

        if self.vpc_attributes is not None:
            result['VpcAttributes'] = self.vpc_attributes.to_map()

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdditionalInfo') is not None:
            temp_model = main_models.DescribeInstancesResponseBodyInstancesInstanceAdditionalInfo()
            self.additional_info = temp_model.from_map(m.get('AdditionalInfo'))

        if m.get('AutoReleaseTime') is not None:
            self.auto_release_time = m.get('AutoReleaseTime')

        if m.get('ClockOptions') is not None:
            temp_model = main_models.DescribeInstancesResponseBodyInstancesInstanceClockOptions()
            self.clock_options = temp_model.from_map(m.get('ClockOptions'))

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('CpuOptions') is not None:
            temp_model = main_models.DescribeInstancesResponseBodyInstancesInstanceCpuOptions()
            self.cpu_options = temp_model.from_map(m.get('CpuOptions'))

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('CreditSpecification') is not None:
            self.credit_specification = m.get('CreditSpecification')

        if m.get('DedicatedHostAttribute') is not None:
            temp_model = main_models.DescribeInstancesResponseBodyInstancesInstanceDedicatedHostAttribute()
            self.dedicated_host_attribute = temp_model.from_map(m.get('DedicatedHostAttribute'))

        if m.get('DedicatedInstanceAttribute') is not None:
            temp_model = main_models.DescribeInstancesResponseBodyInstancesInstanceDedicatedInstanceAttribute()
            self.dedicated_instance_attribute = temp_model.from_map(m.get('DedicatedInstanceAttribute'))

        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')

        if m.get('DeploymentSetGroupNo') is not None:
            self.deployment_set_group_no = m.get('DeploymentSetGroupNo')

        if m.get('DeploymentSetId') is not None:
            self.deployment_set_id = m.get('DeploymentSetId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DeviceAvailable') is not None:
            self.device_available = m.get('DeviceAvailable')

        if m.get('EcsCapacityReservationAttr') is not None:
            temp_model = main_models.DescribeInstancesResponseBodyInstancesInstanceEcsCapacityReservationAttr()
            self.ecs_capacity_reservation_attr = temp_model.from_map(m.get('EcsCapacityReservationAttr'))

        if m.get('EipAddress') is not None:
            temp_model = main_models.DescribeInstancesResponseBodyInstancesInstanceEipAddress()
            self.eip_address = temp_model.from_map(m.get('EipAddress'))

        if m.get('EnableNVS') is not None:
            self.enable_nvs = m.get('EnableNVS')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('GPUAmount') is not None:
            self.gpuamount = m.get('GPUAmount')

        if m.get('GPUSpec') is not None:
            self.gpuspec = m.get('GPUSpec')

        if m.get('HibernationOptions') is not None:
            temp_model = main_models.DescribeInstancesResponseBodyInstancesInstanceHibernationOptions()
            self.hibernation_options = temp_model.from_map(m.get('HibernationOptions'))

        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')

        if m.get('HpcClusterId') is not None:
            self.hpc_cluster_id = m.get('HpcClusterId')

        if m.get('ISP') is not None:
            self.isp = m.get('ISP')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageOptions') is not None:
            temp_model = main_models.DescribeInstancesResponseBodyInstancesInstanceImageOptions()
            self.image_options = temp_model.from_map(m.get('ImageOptions'))

        if m.get('InnerIpAddress') is not None:
            temp_model = main_models.DescribeInstancesResponseBodyInstancesInstanceInnerIpAddress()
            self.inner_ip_address = temp_model.from_map(m.get('InnerIpAddress'))

        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstanceNetworkType') is not None:
            self.instance_network_type = m.get('InstanceNetworkType')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('InstanceTypeFamily') is not None:
            self.instance_type_family = m.get('InstanceTypeFamily')

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

        if m.get('LocalStorageAmount') is not None:
            self.local_storage_amount = m.get('LocalStorageAmount')

        if m.get('LocalStorageCapacity') is not None:
            self.local_storage_capacity = m.get('LocalStorageCapacity')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('MetadataOptions') is not None:
            temp_model = main_models.DescribeInstancesResponseBodyInstancesInstanceMetadataOptions()
            self.metadata_options = temp_model.from_map(m.get('MetadataOptions'))

        if m.get('NetworkInterfaces') is not None:
            temp_model = main_models.DescribeInstancesResponseBodyInstancesInstanceNetworkInterfaces()
            self.network_interfaces = temp_model.from_map(m.get('NetworkInterfaces'))

        if m.get('OSName') is not None:
            self.osname = m.get('OSName')

        if m.get('OSNameEn') is not None:
            self.osname_en = m.get('OSNameEn')

        if m.get('OSType') is not None:
            self.ostype = m.get('OSType')

        if m.get('OperationLocks') is not None:
            temp_model = main_models.DescribeInstancesResponseBodyInstancesInstanceOperationLocks()
            self.operation_locks = temp_model.from_map(m.get('OperationLocks'))

        if m.get('PrivateDnsNameOptions') is not None:
            temp_model = main_models.DescribeInstancesResponseBodyInstancesInstancePrivateDnsNameOptions()
            self.private_dns_name_options = temp_model.from_map(m.get('PrivateDnsNameOptions'))

        if m.get('PublicIpAddress') is not None:
            temp_model = main_models.DescribeInstancesResponseBodyInstancesInstancePublicIpAddress()
            self.public_ip_address = temp_model.from_map(m.get('PublicIpAddress'))

        if m.get('RdmaIpAddress') is not None:
            temp_model = main_models.DescribeInstancesResponseBodyInstancesInstanceRdmaIpAddress()
            self.rdma_ip_address = temp_model.from_map(m.get('RdmaIpAddress'))

        if m.get('Recyclable') is not None:
            self.recyclable = m.get('Recyclable')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SaleCycle') is not None:
            self.sale_cycle = m.get('SaleCycle')

        if m.get('SecurityGroupIds') is not None:
            temp_model = main_models.DescribeInstancesResponseBodyInstancesInstanceSecurityGroupIds()
            self.security_group_ids = temp_model.from_map(m.get('SecurityGroupIds'))

        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')

        if m.get('SpotDuration') is not None:
            self.spot_duration = m.get('SpotDuration')

        if m.get('SpotInterruptionBehavior') is not None:
            self.spot_interruption_behavior = m.get('SpotInterruptionBehavior')

        if m.get('SpotPriceLimit') is not None:
            self.spot_price_limit = m.get('SpotPriceLimit')

        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StoppedMode') is not None:
            self.stopped_mode = m.get('StoppedMode')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeInstancesResponseBodyInstancesInstanceTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('VlanId') is not None:
            self.vlan_id = m.get('VlanId')

        if m.get('VpcAttributes') is not None:
            temp_model = main_models.DescribeInstancesResponseBodyInstancesInstanceVpcAttributes()
            self.vpc_attributes = temp_model.from_map(m.get('VpcAttributes'))

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeInstancesResponseBodyInstancesInstanceVpcAttributes(DaraModel):
    def __init__(
        self,
        nat_ip_address: str = None,
        private_ip_address: main_models.DescribeInstancesResponseBodyInstancesInstanceVpcAttributesPrivateIpAddress = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The NAT IP address of the instance. The NAT IP address is used by ECS instances in different VPCs for communication.
        self.nat_ip_address = nat_ip_address
        # The private IP addresses of the instance.
        self.private_ip_address = private_ip_address
        # The ID of the vSwitch to which the instance is connected.
        self.v_switch_id = v_switch_id
        # The ID of the VPC.
        self.vpc_id = vpc_id

    def validate(self):
        if self.private_ip_address:
            self.private_ip_address.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.nat_ip_address is not None:
            result['NatIpAddress'] = self.nat_ip_address

        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address.to_map()

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NatIpAddress') is not None:
            self.nat_ip_address = m.get('NatIpAddress')

        if m.get('PrivateIpAddress') is not None:
            temp_model = main_models.DescribeInstancesResponseBodyInstancesInstanceVpcAttributesPrivateIpAddress()
            self.private_ip_address = temp_model.from_map(m.get('PrivateIpAddress'))

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class DescribeInstancesResponseBodyInstancesInstanceVpcAttributesPrivateIpAddress(DaraModel):
    def __init__(
        self,
        ip_address: List[str] = None,
    ):
        self.ip_address = ip_address

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')

        return self

class DescribeInstancesResponseBodyInstancesInstanceTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeInstancesResponseBodyInstancesInstanceTagsTag] = None,
    ):
        self.tag = tag

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
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeInstancesResponseBodyInstancesInstanceTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeInstancesResponseBodyInstancesInstanceTagsTag(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key of the instance.
        self.tag_key = tag_key
        # The tag value of the instance.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

class DescribeInstancesResponseBodyInstancesInstanceSecurityGroupIds(DaraModel):
    def __init__(
        self,
        security_group_id: List[str] = None,
    ):
        self.security_group_id = security_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        return self

class DescribeInstancesResponseBodyInstancesInstanceRdmaIpAddress(DaraModel):
    def __init__(
        self,
        ip_address: List[str] = None,
    ):
        self.ip_address = ip_address

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')

        return self

class DescribeInstancesResponseBodyInstancesInstancePublicIpAddress(DaraModel):
    def __init__(
        self,
        ip_address: List[str] = None,
    ):
        self.ip_address = ip_address

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')

        return self

class DescribeInstancesResponseBodyInstancesInstancePrivateDnsNameOptions(DaraModel):
    def __init__(
        self,
        enable_instance_id_dns_aaaarecord: bool = None,
        enable_instance_id_dns_arecord: bool = None,
        enable_ip_dns_arecord: bool = None,
        enable_ip_dns_ptr_record: bool = None,
        hostname_type: str = None,
    ):
        # Indicates whether DNS Resolution from the Instance ID-based Hostname to the Instance Primary Private IPv6 Address (AAAA Record) is enabled. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        self.enable_instance_id_dns_aaaarecord = enable_instance_id_dns_aaaarecord
        # Indicates whether DNS Resolution from the Instance ID-based Hostname to the Instance Primary Private IPv4 Address (A Record) is enabled. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        self.enable_instance_id_dns_arecord = enable_instance_id_dns_arecord
        # Indicates whether DNS Resolution from the IP Address-based Hostname to the Instance Primary Private IPv4 Address (A Record) is enabled. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        self.enable_ip_dns_arecord = enable_ip_dns_arecord
        # Indicates whether Reverse DNS Resolution from the Instance Primary Private IPv4 Address to the IP Address-based Hostname (PTR Record) is enabled. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        self.enable_ip_dns_ptr_record = enable_ip_dns_ptr_record
        # The type of hostname. Valid values:
        # 
        # *   Custom: custom hostname
        # *   IpBased: IP address-based hostname
        # *   InstanceIdBased: instance ID-based hostname
        # 
        # Default value: Custom.
        self.hostname_type = hostname_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_instance_id_dns_aaaarecord is not None:
            result['EnableInstanceIdDnsAAAARecord'] = self.enable_instance_id_dns_aaaarecord

        if self.enable_instance_id_dns_arecord is not None:
            result['EnableInstanceIdDnsARecord'] = self.enable_instance_id_dns_arecord

        if self.enable_ip_dns_arecord is not None:
            result['EnableIpDnsARecord'] = self.enable_ip_dns_arecord

        if self.enable_ip_dns_ptr_record is not None:
            result['EnableIpDnsPtrRecord'] = self.enable_ip_dns_ptr_record

        if self.hostname_type is not None:
            result['HostnameType'] = self.hostname_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableInstanceIdDnsAAAARecord') is not None:
            self.enable_instance_id_dns_aaaarecord = m.get('EnableInstanceIdDnsAAAARecord')

        if m.get('EnableInstanceIdDnsARecord') is not None:
            self.enable_instance_id_dns_arecord = m.get('EnableInstanceIdDnsARecord')

        if m.get('EnableIpDnsARecord') is not None:
            self.enable_ip_dns_arecord = m.get('EnableIpDnsARecord')

        if m.get('EnableIpDnsPtrRecord') is not None:
            self.enable_ip_dns_ptr_record = m.get('EnableIpDnsPtrRecord')

        if m.get('HostnameType') is not None:
            self.hostname_type = m.get('HostnameType')

        return self

class DescribeInstancesResponseBodyInstancesInstanceOperationLocks(DaraModel):
    def __init__(
        self,
        lock_reason: List[main_models.DescribeInstancesResponseBodyInstancesInstanceOperationLocksLockReason] = None,
    ):
        self.lock_reason = lock_reason

    def validate(self):
        if self.lock_reason:
            for v1 in self.lock_reason:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LockReason'] = []
        if self.lock_reason is not None:
            for k1 in self.lock_reason:
                result['LockReason'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.lock_reason = []
        if m.get('LockReason') is not None:
            for k1 in m.get('LockReason'):
                temp_model = main_models.DescribeInstancesResponseBodyInstancesInstanceOperationLocksLockReason()
                self.lock_reason.append(temp_model.from_map(k1))

        return self

class DescribeInstancesResponseBodyInstancesInstanceOperationLocksLockReason(DaraModel):
    def __init__(
        self,
        lock_msg: str = None,
        lock_reason: str = None,
    ):
        # The message returned when the instance was locked.
        self.lock_msg = lock_msg
        # The reason why the instance was locked. Valid values:
        # 
        # *   financial: The instance was locked due to overdue payments.
        # *   security: The instance was locked due to security reasons.
        # *   recycling: The spot instance was locked and pending release.
        # *   dedicatedhostfinancial: The instance was locked due to overdue payments for the dedicated host.
        # *   refunded: The instance was locked because a refund was made for the instance.
        self.lock_reason = lock_reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lock_msg is not None:
            result['LockMsg'] = self.lock_msg

        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LockMsg') is not None:
            self.lock_msg = m.get('LockMsg')

        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')

        return self

class DescribeInstancesResponseBodyInstancesInstanceNetworkInterfaces(DaraModel):
    def __init__(
        self,
        network_interface: List[main_models.DescribeInstancesResponseBodyInstancesInstanceNetworkInterfacesNetworkInterface] = None,
    ):
        self.network_interface = network_interface

    def validate(self):
        if self.network_interface:
            for v1 in self.network_interface:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NetworkInterface'] = []
        if self.network_interface is not None:
            for k1 in self.network_interface:
                result['NetworkInterface'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.network_interface = []
        if m.get('NetworkInterface') is not None:
            for k1 in m.get('NetworkInterface'):
                temp_model = main_models.DescribeInstancesResponseBodyInstancesInstanceNetworkInterfacesNetworkInterface()
                self.network_interface.append(temp_model.from_map(k1))

        return self

class DescribeInstancesResponseBodyInstancesInstanceNetworkInterfacesNetworkInterface(DaraModel):
    def __init__(
        self,
        ipv_4prefix_sets: main_models.DescribeInstancesResponseBodyInstancesInstanceNetworkInterfacesNetworkInterfaceIpv4PrefixSets = None,
        ipv_6prefix_sets: main_models.DescribeInstancesResponseBodyInstancesInstanceNetworkInterfacesNetworkInterfaceIpv6PrefixSets = None,
        ipv_6sets: main_models.DescribeInstancesResponseBodyInstancesInstanceNetworkInterfacesNetworkInterfaceIpv6Sets = None,
        mac_address: str = None,
        network_interface_id: str = None,
        primary_ip_address: str = None,
        private_ip_sets: main_models.DescribeInstancesResponseBodyInstancesInstanceNetworkInterfacesNetworkInterfacePrivateIpSets = None,
        type: str = None,
    ):
        # The IPv4 prefixes of the ENI. This parameter has a value only when `AdditionalAttributes.N` is set to `NETWORK_PRIMARY_ENI_IP`.
        self.ipv_4prefix_sets = ipv_4prefix_sets
        # The IPv6 prefixes of the ENI. This parameter has a value only when `AdditionalAttributes.N` is set to `NETWORK_PRIMARY_ENI_IP`.
        self.ipv_6prefix_sets = ipv_6prefix_sets
        # The IPv6 addresses of the ENI. This parameter has a value only when `AdditionalAttributes.N` is set to `NETWORK_PRIMARY_ENI_IP`.
        self.ipv_6sets = ipv_6sets
        # The MAC address of the ENI.
        self.mac_address = mac_address
        # The ID of the ENI.
        self.network_interface_id = network_interface_id
        # The primary private IP address of the ENI.
        self.primary_ip_address = primary_ip_address
        # The private IP addresses of the ENI.
        self.private_ip_sets = private_ip_sets
        # The type of the ENI. Valid values:
        # 
        # *   Primary
        # *   Secondary
        self.type = type

    def validate(self):
        if self.ipv_4prefix_sets:
            self.ipv_4prefix_sets.validate()
        if self.ipv_6prefix_sets:
            self.ipv_6prefix_sets.validate()
        if self.ipv_6sets:
            self.ipv_6sets.validate()
        if self.private_ip_sets:
            self.private_ip_sets.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipv_4prefix_sets is not None:
            result['Ipv4PrefixSets'] = self.ipv_4prefix_sets.to_map()

        if self.ipv_6prefix_sets is not None:
            result['Ipv6PrefixSets'] = self.ipv_6prefix_sets.to_map()

        if self.ipv_6sets is not None:
            result['Ipv6Sets'] = self.ipv_6sets.to_map()

        if self.mac_address is not None:
            result['MacAddress'] = self.mac_address

        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id

        if self.primary_ip_address is not None:
            result['PrimaryIpAddress'] = self.primary_ip_address

        if self.private_ip_sets is not None:
            result['PrivateIpSets'] = self.private_ip_sets.to_map()

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ipv4PrefixSets') is not None:
            temp_model = main_models.DescribeInstancesResponseBodyInstancesInstanceNetworkInterfacesNetworkInterfaceIpv4PrefixSets()
            self.ipv_4prefix_sets = temp_model.from_map(m.get('Ipv4PrefixSets'))

        if m.get('Ipv6PrefixSets') is not None:
            temp_model = main_models.DescribeInstancesResponseBodyInstancesInstanceNetworkInterfacesNetworkInterfaceIpv6PrefixSets()
            self.ipv_6prefix_sets = temp_model.from_map(m.get('Ipv6PrefixSets'))

        if m.get('Ipv6Sets') is not None:
            temp_model = main_models.DescribeInstancesResponseBodyInstancesInstanceNetworkInterfacesNetworkInterfaceIpv6Sets()
            self.ipv_6sets = temp_model.from_map(m.get('Ipv6Sets'))

        if m.get('MacAddress') is not None:
            self.mac_address = m.get('MacAddress')

        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')

        if m.get('PrimaryIpAddress') is not None:
            self.primary_ip_address = m.get('PrimaryIpAddress')

        if m.get('PrivateIpSets') is not None:
            temp_model = main_models.DescribeInstancesResponseBodyInstancesInstanceNetworkInterfacesNetworkInterfacePrivateIpSets()
            self.private_ip_sets = temp_model.from_map(m.get('PrivateIpSets'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeInstancesResponseBodyInstancesInstanceNetworkInterfacesNetworkInterfacePrivateIpSets(DaraModel):
    def __init__(
        self,
        private_ip_set: List[main_models.DescribeInstancesResponseBodyInstancesInstanceNetworkInterfacesNetworkInterfacePrivateIpSetsPrivateIpSet] = None,
    ):
        self.private_ip_set = private_ip_set

    def validate(self):
        if self.private_ip_set:
            for v1 in self.private_ip_set:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PrivateIpSet'] = []
        if self.private_ip_set is not None:
            for k1 in self.private_ip_set:
                result['PrivateIpSet'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.private_ip_set = []
        if m.get('PrivateIpSet') is not None:
            for k1 in m.get('PrivateIpSet'):
                temp_model = main_models.DescribeInstancesResponseBodyInstancesInstanceNetworkInterfacesNetworkInterfacePrivateIpSetsPrivateIpSet()
                self.private_ip_set.append(temp_model.from_map(k1))

        return self

class DescribeInstancesResponseBodyInstancesInstanceNetworkInterfacesNetworkInterfacePrivateIpSetsPrivateIpSet(DaraModel):
    def __init__(
        self,
        primary: bool = None,
        private_dns_name: str = None,
        private_ip_address: str = None,
    ):
        # Indicates whether the IP address is the primary private IP address. Valid values:
        # 
        # *   true
        # *   false
        self.primary = primary
        # The private domain name of the instance.
        # 
        # >  This parameter has a value in a specific format only if `HostnameType` is set to `IpBased` or `InstanceIdBased`.
        self.private_dns_name = private_dns_name
        # The private IP address of the ENI.
        self.private_ip_address = private_ip_address

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.primary is not None:
            result['Primary'] = self.primary

        if self.private_dns_name is not None:
            result['PrivateDnsName'] = self.private_dns_name

        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Primary') is not None:
            self.primary = m.get('Primary')

        if m.get('PrivateDnsName') is not None:
            self.private_dns_name = m.get('PrivateDnsName')

        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')

        return self

class DescribeInstancesResponseBodyInstancesInstanceNetworkInterfacesNetworkInterfaceIpv6Sets(DaraModel):
    def __init__(
        self,
        ipv_6set: List[main_models.DescribeInstancesResponseBodyInstancesInstanceNetworkInterfacesNetworkInterfaceIpv6SetsIpv6Set] = None,
    ):
        self.ipv_6set = ipv_6set

    def validate(self):
        if self.ipv_6set:
            for v1 in self.ipv_6set:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Ipv6Set'] = []
        if self.ipv_6set is not None:
            for k1 in self.ipv_6set:
                result['Ipv6Set'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ipv_6set = []
        if m.get('Ipv6Set') is not None:
            for k1 in m.get('Ipv6Set'):
                temp_model = main_models.DescribeInstancesResponseBodyInstancesInstanceNetworkInterfacesNetworkInterfaceIpv6SetsIpv6Set()
                self.ipv_6set.append(temp_model.from_map(k1))

        return self

class DescribeInstancesResponseBodyInstancesInstanceNetworkInterfacesNetworkInterfaceIpv6SetsIpv6Set(DaraModel):
    def __init__(
        self,
        ipv_6address: str = None,
    ):
        # The IPv6 address of the ENI.
        self.ipv_6address = ipv_6address

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipv_6address is not None:
            result['Ipv6Address'] = self.ipv_6address

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ipv6Address') is not None:
            self.ipv_6address = m.get('Ipv6Address')

        return self

class DescribeInstancesResponseBodyInstancesInstanceNetworkInterfacesNetworkInterfaceIpv6PrefixSets(DaraModel):
    def __init__(
        self,
        ipv_6prefix_set: List[main_models.DescribeInstancesResponseBodyInstancesInstanceNetworkInterfacesNetworkInterfaceIpv6PrefixSetsIpv6PrefixSet] = None,
    ):
        self.ipv_6prefix_set = ipv_6prefix_set

    def validate(self):
        if self.ipv_6prefix_set:
            for v1 in self.ipv_6prefix_set:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Ipv6PrefixSet'] = []
        if self.ipv_6prefix_set is not None:
            for k1 in self.ipv_6prefix_set:
                result['Ipv6PrefixSet'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ipv_6prefix_set = []
        if m.get('Ipv6PrefixSet') is not None:
            for k1 in m.get('Ipv6PrefixSet'):
                temp_model = main_models.DescribeInstancesResponseBodyInstancesInstanceNetworkInterfacesNetworkInterfaceIpv6PrefixSetsIpv6PrefixSet()
                self.ipv_6prefix_set.append(temp_model.from_map(k1))

        return self

class DescribeInstancesResponseBodyInstancesInstanceNetworkInterfacesNetworkInterfaceIpv6PrefixSetsIpv6PrefixSet(DaraModel):
    def __init__(
        self,
        ipv_6prefix: str = None,
    ):
        # The IPv6 prefix of the ENI.
        self.ipv_6prefix = ipv_6prefix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipv_6prefix is not None:
            result['Ipv6Prefix'] = self.ipv_6prefix

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ipv6Prefix') is not None:
            self.ipv_6prefix = m.get('Ipv6Prefix')

        return self

class DescribeInstancesResponseBodyInstancesInstanceNetworkInterfacesNetworkInterfaceIpv4PrefixSets(DaraModel):
    def __init__(
        self,
        ipv_4prefix_set: List[main_models.DescribeInstancesResponseBodyInstancesInstanceNetworkInterfacesNetworkInterfaceIpv4PrefixSetsIpv4PrefixSet] = None,
    ):
        self.ipv_4prefix_set = ipv_4prefix_set

    def validate(self):
        if self.ipv_4prefix_set:
            for v1 in self.ipv_4prefix_set:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Ipv4PrefixSet'] = []
        if self.ipv_4prefix_set is not None:
            for k1 in self.ipv_4prefix_set:
                result['Ipv4PrefixSet'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ipv_4prefix_set = []
        if m.get('Ipv4PrefixSet') is not None:
            for k1 in m.get('Ipv4PrefixSet'):
                temp_model = main_models.DescribeInstancesResponseBodyInstancesInstanceNetworkInterfacesNetworkInterfaceIpv4PrefixSetsIpv4PrefixSet()
                self.ipv_4prefix_set.append(temp_model.from_map(k1))

        return self

class DescribeInstancesResponseBodyInstancesInstanceNetworkInterfacesNetworkInterfaceIpv4PrefixSetsIpv4PrefixSet(DaraModel):
    def __init__(
        self,
        ipv_4prefix: str = None,
    ):
        # The IPv4 prefix of the ENI.
        self.ipv_4prefix = ipv_4prefix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipv_4prefix is not None:
            result['Ipv4Prefix'] = self.ipv_4prefix

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ipv4Prefix') is not None:
            self.ipv_4prefix = m.get('Ipv4Prefix')

        return self

class DescribeInstancesResponseBodyInstancesInstanceMetadataOptions(DaraModel):
    def __init__(
        self,
        http_endpoint: str = None,
        http_put_response_hop_limit: int = None,
        http_tokens: str = None,
    ):
        # Indicates whether the access channel is enabled for instance metadata. Valid values:
        # 
        # *   enabled
        # *   disabled
        self.http_endpoint = http_endpoint
        # >  This parameter is not publicly available.
        self.http_put_response_hop_limit = http_put_response_hop_limit
        # Indicates whether the security hardening mode (IMDSv2) is forcefully used to access instance metadata. Valid values:
        # 
        # *   optional: The security hardening mode (IMDSv2) is not forcefully used.
        # *   required: The security hardening mode (IMDSv2) is forcefully used.
        self.http_tokens = http_tokens

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.http_endpoint is not None:
            result['HttpEndpoint'] = self.http_endpoint

        if self.http_put_response_hop_limit is not None:
            result['HttpPutResponseHopLimit'] = self.http_put_response_hop_limit

        if self.http_tokens is not None:
            result['HttpTokens'] = self.http_tokens

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpEndpoint') is not None:
            self.http_endpoint = m.get('HttpEndpoint')

        if m.get('HttpPutResponseHopLimit') is not None:
            self.http_put_response_hop_limit = m.get('HttpPutResponseHopLimit')

        if m.get('HttpTokens') is not None:
            self.http_tokens = m.get('HttpTokens')

        return self

class DescribeInstancesResponseBodyInstancesInstanceInnerIpAddress(DaraModel):
    def __init__(
        self,
        ip_address: List[str] = None,
    ):
        self.ip_address = ip_address

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')

        return self

class DescribeInstancesResponseBodyInstancesInstanceImageOptions(DaraModel):
    def __init__(
        self,
        current_osnvme_supported: bool = None,
        login_as_non_root: bool = None,
    ):
        # Indicates whether the operating system supports access to disks over the NVMe protocol. Valid values:
        # 
        # *   true
        # *   false
        # 
        # >  This parameter is returned only if you specify CURRENT_OS_NVME_SUPPORTED in AdditionalAttributes in the request.
        self.current_osnvme_supported = current_osnvme_supported
        # Indicates whether the instance that uses the image supports logons of the ecs-user user. Valid values:
        # 
        # *   true
        # *   false
        self.login_as_non_root = login_as_non_root

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_osnvme_supported is not None:
            result['CurrentOSNVMeSupported'] = self.current_osnvme_supported

        if self.login_as_non_root is not None:
            result['LoginAsNonRoot'] = self.login_as_non_root

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentOSNVMeSupported') is not None:
            self.current_osnvme_supported = m.get('CurrentOSNVMeSupported')

        if m.get('LoginAsNonRoot') is not None:
            self.login_as_non_root = m.get('LoginAsNonRoot')

        return self

class DescribeInstancesResponseBodyInstancesInstanceHibernationOptions(DaraModel):
    def __init__(
        self,
        configured: bool = None,
    ):
        # >  This parameter is in invitational preview and is not publicly available.
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

class DescribeInstancesResponseBodyInstancesInstanceEipAddress(DaraModel):
    def __init__(
        self,
        allocation_id: str = None,
        bandwidth: int = None,
        internet_charge_type: str = None,
        ip_address: str = None,
        is_support_unassociate: bool = None,
    ):
        # The ID of the EIP.
        self.allocation_id = allocation_id
        # The maximum public bandwidth of the EIP. Unit: Mbit/s.
        self.bandwidth = bandwidth
        # The metering method of the EIP. Valid values:
        # 
        # *   PayByBandwidth
        # *   PayByTraffic
        self.internet_charge_type = internet_charge_type
        # The EIP.
        self.ip_address = ip_address
        # Indicates whether the EIP can be disassociated.
        self.is_support_unassociate = is_support_unassociate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allocation_id is not None:
            result['AllocationId'] = self.allocation_id

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type

        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address

        if self.is_support_unassociate is not None:
            result['IsSupportUnassociate'] = self.is_support_unassociate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationId') is not None:
            self.allocation_id = m.get('AllocationId')

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')

        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')

        if m.get('IsSupportUnassociate') is not None:
            self.is_support_unassociate = m.get('IsSupportUnassociate')

        return self

class DescribeInstancesResponseBodyInstancesInstanceEcsCapacityReservationAttr(DaraModel):
    def __init__(
        self,
        capacity_reservation_id: str = None,
        capacity_reservation_preference: str = None,
    ):
        # The ID of the capacity reservation.
        self.capacity_reservation_id = capacity_reservation_id
        # The preference of the capacity reservation.
        self.capacity_reservation_preference = capacity_reservation_preference

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.capacity_reservation_id is not None:
            result['CapacityReservationId'] = self.capacity_reservation_id

        if self.capacity_reservation_preference is not None:
            result['CapacityReservationPreference'] = self.capacity_reservation_preference

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CapacityReservationId') is not None:
            self.capacity_reservation_id = m.get('CapacityReservationId')

        if m.get('CapacityReservationPreference') is not None:
            self.capacity_reservation_preference = m.get('CapacityReservationPreference')

        return self

class DescribeInstancesResponseBodyInstancesInstanceDedicatedInstanceAttribute(DaraModel):
    def __init__(
        self,
        affinity: str = None,
        tenancy: str = None,
    ):
        # Indicates whether the instance on the dedicated host is associated with the dedicated host. Valid values:
        # 
        # *   default: The instance is not associated with the dedicated host. When the instance is restarted from economical mode, the instance may be automatically deployed on another dedicated host in the automatic deployment resource pool.
        # *   host: The instance is associated with the dedicated host. When the instance is restarted from economical mode, the instance is still deployed on the original dedicated host.
        self.affinity = affinity
        # Indicates whether the instance is hosted on a dedicated host. Valid values:
        # 
        # *   default: The instance is not hosted on a dedicated host.
        # *   host: The instance is hosted on a dedicated host.
        self.tenancy = tenancy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.affinity is not None:
            result['Affinity'] = self.affinity

        if self.tenancy is not None:
            result['Tenancy'] = self.tenancy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Affinity') is not None:
            self.affinity = m.get('Affinity')

        if m.get('Tenancy') is not None:
            self.tenancy = m.get('Tenancy')

        return self

class DescribeInstancesResponseBodyInstancesInstanceDedicatedHostAttribute(DaraModel):
    def __init__(
        self,
        dedicated_host_cluster_id: str = None,
        dedicated_host_id: str = None,
        dedicated_host_name: str = None,
    ):
        # The ID of the dedicated host cluster.
        self.dedicated_host_cluster_id = dedicated_host_cluster_id
        # The ID of the dedicated host.
        self.dedicated_host_id = dedicated_host_id
        # The name of the dedicated host.
        self.dedicated_host_name = dedicated_host_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dedicated_host_cluster_id is not None:
            result['DedicatedHostClusterId'] = self.dedicated_host_cluster_id

        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id

        if self.dedicated_host_name is not None:
            result['DedicatedHostName'] = self.dedicated_host_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedHostClusterId') is not None:
            self.dedicated_host_cluster_id = m.get('DedicatedHostClusterId')

        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')

        if m.get('DedicatedHostName') is not None:
            self.dedicated_host_name = m.get('DedicatedHostName')

        return self

class DescribeInstancesResponseBodyInstancesInstanceCpuOptions(DaraModel):
    def __init__(
        self,
        core_count: int = None,
        enable_visst: bool = None,
        enable_vrdt: bool = None,
        numa: str = None,
        threads_per_core: int = None,
        topology_type: str = None,
        turbo_mode: str = None,
    ):
        # The number of physical CPU cores.
        self.core_count = core_count
        self.enable_visst = enable_visst
        self.enable_vrdt = enable_vrdt
        # >  This parameter is deprecated.
        self.numa = numa
        # The number of threads per CPU core.
        self.threads_per_core = threads_per_core
        # The CPU topology type of the instance. Valid values:
        # 
        # *   ContinuousCoreToHTMapping: Hyper-Threading (HT) continuous CPU topology
        # *   DiscreteCoreToHTMapping: HT discrete CPU topology
        self.topology_type = topology_type
        self.turbo_mode = turbo_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.core_count is not None:
            result['CoreCount'] = self.core_count

        if self.enable_visst is not None:
            result['EnableVISST'] = self.enable_visst

        if self.enable_vrdt is not None:
            result['EnableVRDT'] = self.enable_vrdt

        if self.numa is not None:
            result['Numa'] = self.numa

        if self.threads_per_core is not None:
            result['ThreadsPerCore'] = self.threads_per_core

        if self.topology_type is not None:
            result['TopologyType'] = self.topology_type

        if self.turbo_mode is not None:
            result['TurboMode'] = self.turbo_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoreCount') is not None:
            self.core_count = m.get('CoreCount')

        if m.get('EnableVISST') is not None:
            self.enable_visst = m.get('EnableVISST')

        if m.get('EnableVRDT') is not None:
            self.enable_vrdt = m.get('EnableVRDT')

        if m.get('Numa') is not None:
            self.numa = m.get('Numa')

        if m.get('ThreadsPerCore') is not None:
            self.threads_per_core = m.get('ThreadsPerCore')

        if m.get('TopologyType') is not None:
            self.topology_type = m.get('TopologyType')

        if m.get('TurboMode') is not None:
            self.turbo_mode = m.get('TurboMode')

        return self

class DescribeInstancesResponseBodyInstancesInstanceClockOptions(DaraModel):
    def __init__(
        self,
        ptp_status: str = None,
    ):
        self.ptp_status = ptp_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ptp_status is not None:
            result['PtpStatus'] = self.ptp_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PtpStatus') is not None:
            self.ptp_status = m.get('PtpStatus')

        return self

class DescribeInstancesResponseBodyInstancesInstanceAdditionalInfo(DaraModel):
    def __init__(
        self,
        enable_high_density_mode: bool = None,
    ):
        # >  This parameter is in invitational preview and is not publicly available.
        self.enable_high_density_mode = enable_high_density_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_high_density_mode is not None:
            result['EnableHighDensityMode'] = self.enable_high_density_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableHighDensityMode') is not None:
            self.enable_high_density_mode = m.get('EnableHighDensityMode')

        return self

