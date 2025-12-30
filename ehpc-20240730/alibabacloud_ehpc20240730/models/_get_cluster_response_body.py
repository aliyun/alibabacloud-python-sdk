# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ehpc20240730 import models as main_models
from darabonba.model import DaraModel

class GetClusterResponseBody(DaraModel):
    def __init__(
        self,
        client_version: str = None,
        cluster_category: str = None,
        cluster_create_time: str = None,
        cluster_custom_configuration: main_models.GetClusterResponseBodyClusterCustomConfiguration = None,
        cluster_id: str = None,
        cluster_mode: str = None,
        cluster_modify_time: str = None,
        cluster_name: str = None,
        cluster_status: str = None,
        cluster_vswitch_id: str = None,
        cluster_vpc_id: str = None,
        delete_protection: str = None,
        ehpc_version: str = None,
        enable_scale_in: bool = None,
        enable_scale_out: bool = None,
        grow_interval: int = None,
        idle_interval: int = None,
        manager: main_models.GetClusterResponseBodyManager = None,
        max_core_count: str = None,
        max_count: str = None,
        monitor_spec: main_models.GetClusterResponseBodyMonitorSpec = None,
        request_id: str = None,
        resource_group_id: str = None,
        scheduler_spec: main_models.GetClusterResponseBodySchedulerSpec = None,
        security_group_id: str = None,
    ):
        # The E-HPC Util version.
        self.client_version = client_version
        # The cluster type. Valid values:
        # 
        # *   Standard
        # *   Serverless
        self.cluster_category = cluster_category
        # The time when the cluster was created. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. The time is displayed in UTC. For more information, see [ISO 8601](https://help.aliyun.com/document_detail/25696.html).
        self.cluster_create_time = cluster_create_time
        # The post-processing script of the cluster.
        self.cluster_custom_configuration = cluster_custom_configuration
        # The cluster ID.
        self.cluster_id = cluster_id
        # The deployment type of the cluster. Valid values:
        # 
        # *   Integrated: The cluster is deployed on a public cloud.
        # *   Hybrid: The cluster is deployed on a hybrid cloud.
        # *   Custom: The cluster is a custom cluster.
        self.cluster_mode = cluster_mode
        # The time when the cluster was last modified. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. The time is displayed in UTC. For more information, see [ISO 8601](https://help.aliyun.com/document_detail/25696.html).
        self.cluster_modify_time = cluster_modify_time
        # The cluster name.
        self.cluster_name = cluster_name
        # The cluster state. Valid values:
        # 
        # *   uninit: The cluster is being installed.
        # *   creating: The cluster is being created.
        # *   initing: The cluster is being initialized.
        # *   running: The cluster is running.
        # *   exception: The cluster has run into an exception.
        # *   raleasing: The cluster is being released.
        # *   stopping: The cluster is being stopped.
        # *   stopped: The cluster is stopped.
        # *   pending: The cluster is waiting to be configured.
        self.cluster_status = cluster_status
        # The ID of the vSwitch used by the cluster.
        self.cluster_vswitch_id = cluster_vswitch_id
        # The ID of the virtual private cloud (VPC) used by the cluster.
        self.cluster_vpc_id = cluster_vpc_id
        # Indicates whether deletion protection is enabled for the cluster. Valid values:
        # 
        # *   true
        # *   false
        self.delete_protection = delete_protection
        # The E-HPC version.
        self.ehpc_version = ehpc_version
        # Indicates whether automatic scale-in is enabled for the cluster. Valid values:
        # 
        # *   true
        # *   false
        self.enable_scale_in = enable_scale_in
        # Indicates whether automatic scale-out is enabled for the cluster. Valid values:
        # 
        # *   true
        # *   false
        self.enable_scale_out = enable_scale_out
        # The interval at which the cluster is automatically scaled out.
        self.grow_interval = grow_interval
        # The idle duration of the compute nodes allowed by the cluster.
        self.idle_interval = idle_interval
        # The management node configurations.
        self.manager = manager
        # The maximum total number of vCPUs that can be used by all compute nodes managed by the cluster.
        self.max_core_count = max_core_count
        # The maximum number of compute nodes that the cluster can manage.
        self.max_count = max_count
        # The monitoring details of the cluster.
        self.monitor_spec = monitor_spec
        # The request ID.
        self.request_id = request_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The scheduler specifications of the cluster.
        self.scheduler_spec = scheduler_spec
        # The security group ID.
        self.security_group_id = security_group_id

    def validate(self):
        if self.cluster_custom_configuration:
            self.cluster_custom_configuration.validate()
        if self.manager:
            self.manager.validate()
        if self.monitor_spec:
            self.monitor_spec.validate()
        if self.scheduler_spec:
            self.scheduler_spec.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version

        if self.cluster_category is not None:
            result['ClusterCategory'] = self.cluster_category

        if self.cluster_create_time is not None:
            result['ClusterCreateTime'] = self.cluster_create_time

        if self.cluster_custom_configuration is not None:
            result['ClusterCustomConfiguration'] = self.cluster_custom_configuration.to_map()

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_mode is not None:
            result['ClusterMode'] = self.cluster_mode

        if self.cluster_modify_time is not None:
            result['ClusterModifyTime'] = self.cluster_modify_time

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.cluster_status is not None:
            result['ClusterStatus'] = self.cluster_status

        if self.cluster_vswitch_id is not None:
            result['ClusterVSwitchId'] = self.cluster_vswitch_id

        if self.cluster_vpc_id is not None:
            result['ClusterVpcId'] = self.cluster_vpc_id

        if self.delete_protection is not None:
            result['DeleteProtection'] = self.delete_protection

        if self.ehpc_version is not None:
            result['EhpcVersion'] = self.ehpc_version

        if self.enable_scale_in is not None:
            result['EnableScaleIn'] = self.enable_scale_in

        if self.enable_scale_out is not None:
            result['EnableScaleOut'] = self.enable_scale_out

        if self.grow_interval is not None:
            result['GrowInterval'] = self.grow_interval

        if self.idle_interval is not None:
            result['IdleInterval'] = self.idle_interval

        if self.manager is not None:
            result['Manager'] = self.manager.to_map()

        if self.max_core_count is not None:
            result['MaxCoreCount'] = self.max_core_count

        if self.max_count is not None:
            result['MaxCount'] = self.max_count

        if self.monitor_spec is not None:
            result['MonitorSpec'] = self.monitor_spec.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.scheduler_spec is not None:
            result['SchedulerSpec'] = self.scheduler_spec.to_map()

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')

        if m.get('ClusterCategory') is not None:
            self.cluster_category = m.get('ClusterCategory')

        if m.get('ClusterCreateTime') is not None:
            self.cluster_create_time = m.get('ClusterCreateTime')

        if m.get('ClusterCustomConfiguration') is not None:
            temp_model = main_models.GetClusterResponseBodyClusterCustomConfiguration()
            self.cluster_custom_configuration = temp_model.from_map(m.get('ClusterCustomConfiguration'))

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterMode') is not None:
            self.cluster_mode = m.get('ClusterMode')

        if m.get('ClusterModifyTime') is not None:
            self.cluster_modify_time = m.get('ClusterModifyTime')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('ClusterStatus') is not None:
            self.cluster_status = m.get('ClusterStatus')

        if m.get('ClusterVSwitchId') is not None:
            self.cluster_vswitch_id = m.get('ClusterVSwitchId')

        if m.get('ClusterVpcId') is not None:
            self.cluster_vpc_id = m.get('ClusterVpcId')

        if m.get('DeleteProtection') is not None:
            self.delete_protection = m.get('DeleteProtection')

        if m.get('EhpcVersion') is not None:
            self.ehpc_version = m.get('EhpcVersion')

        if m.get('EnableScaleIn') is not None:
            self.enable_scale_in = m.get('EnableScaleIn')

        if m.get('EnableScaleOut') is not None:
            self.enable_scale_out = m.get('EnableScaleOut')

        if m.get('GrowInterval') is not None:
            self.grow_interval = m.get('GrowInterval')

        if m.get('IdleInterval') is not None:
            self.idle_interval = m.get('IdleInterval')

        if m.get('Manager') is not None:
            temp_model = main_models.GetClusterResponseBodyManager()
            self.manager = temp_model.from_map(m.get('Manager'))

        if m.get('MaxCoreCount') is not None:
            self.max_core_count = m.get('MaxCoreCount')

        if m.get('MaxCount') is not None:
            self.max_count = m.get('MaxCount')

        if m.get('MonitorSpec') is not None:
            temp_model = main_models.GetClusterResponseBodyMonitorSpec()
            self.monitor_spec = temp_model.from_map(m.get('MonitorSpec'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SchedulerSpec') is not None:
            temp_model = main_models.GetClusterResponseBodySchedulerSpec()
            self.scheduler_spec = temp_model.from_map(m.get('SchedulerSpec'))

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        return self

class GetClusterResponseBodySchedulerSpec(DaraModel):
    def __init__(
        self,
        enable_power_saving: bool = None,
        enable_topology_awareness: bool = None,
    ):
        self.enable_power_saving = enable_power_saving
        # Indicates whether the topology awareness feature is enabled for the cluster. Valid values:
        # 
        # *   true
        # *   false
        self.enable_topology_awareness = enable_topology_awareness

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_power_saving is not None:
            result['EnablePowerSaving'] = self.enable_power_saving

        if self.enable_topology_awareness is not None:
            result['EnableTopologyAwareness'] = self.enable_topology_awareness

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnablePowerSaving') is not None:
            self.enable_power_saving = m.get('EnablePowerSaving')

        if m.get('EnableTopologyAwareness') is not None:
            self.enable_topology_awareness = m.get('EnableTopologyAwareness')

        return self

class GetClusterResponseBodyMonitorSpec(DaraModel):
    def __init__(
        self,
        enable_compute_load_monitor: bool = None,
    ):
        # Indicates whether the monitoring component of compute nodes is enabled for the cluster. Valid values:
        # 
        # *   true
        # *   false
        self.enable_compute_load_monitor = enable_compute_load_monitor

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_compute_load_monitor is not None:
            result['EnableComputeLoadMonitor'] = self.enable_compute_load_monitor

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableComputeLoadMonitor') is not None:
            self.enable_compute_load_monitor = m.get('EnableComputeLoadMonitor')

        return self

class GetClusterResponseBodyManager(DaraModel):
    def __init__(
        self,
        dns: main_models.GetClusterResponseBodyManagerDNS = None,
        directory_service: main_models.GetClusterResponseBodyManagerDirectoryService = None,
        manager_node: main_models.GetClusterResponseBodyManagerManagerNode = None,
        scheduler: main_models.GetClusterResponseBodyManagerScheduler = None,
    ):
        # The configurations of the domain name resolution service.
        self.dns = dns
        # The information about the domain account service.
        self.directory_service = directory_service
        # The configurations of the management node.
        self.manager_node = manager_node
        # The information about the scheduler.
        self.scheduler = scheduler

    def validate(self):
        if self.dns:
            self.dns.validate()
        if self.directory_service:
            self.directory_service.validate()
        if self.manager_node:
            self.manager_node.validate()
        if self.scheduler:
            self.scheduler.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dns is not None:
            result['DNS'] = self.dns.to_map()

        if self.directory_service is not None:
            result['DirectoryService'] = self.directory_service.to_map()

        if self.manager_node is not None:
            result['ManagerNode'] = self.manager_node.to_map()

        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DNS') is not None:
            temp_model = main_models.GetClusterResponseBodyManagerDNS()
            self.dns = temp_model.from_map(m.get('DNS'))

        if m.get('DirectoryService') is not None:
            temp_model = main_models.GetClusterResponseBodyManagerDirectoryService()
            self.directory_service = temp_model.from_map(m.get('DirectoryService'))

        if m.get('ManagerNode') is not None:
            temp_model = main_models.GetClusterResponseBodyManagerManagerNode()
            self.manager_node = temp_model.from_map(m.get('ManagerNode'))

        if m.get('Scheduler') is not None:
            temp_model = main_models.GetClusterResponseBodyManagerScheduler()
            self.scheduler = temp_model.from_map(m.get('Scheduler'))

        return self

class GetClusterResponseBodyManagerScheduler(DaraModel):
    def __init__(
        self,
        status: str = None,
        type: str = None,
        version: str = None,
    ):
        # The scheduler state. Valid values:
        # 
        # *   uninit: The scheduler is being installed.
        # *   initing: The scheduler is being initialized.
        # *   running: The scheduler is running.
        # *   exception: The scheduler has run into an exception.
        # *   releasing: The scheduler is being released.
        # *   stopped: The scheduler is stopped.
        # *   pending: The scheduler is waiting to be configured.
        self.status = status
        # The scheduler type. Valid values:
        # 
        # *   SLURM
        # *   PBS
        # *   OPENGRIDSCHEDULER
        # *   LSF_PLUGIN
        # *   PBS_PLUGIN
        self.type = type
        # The scheduler version.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class GetClusterResponseBodyManagerManagerNode(DaraModel):
    def __init__(
        self,
        auto_renew: bool = None,
        auto_renew_period: int = None,
        duration: int = None,
        enable_ht: bool = None,
        expired_time: str = None,
        image_id: str = None,
        instance_charge_type: str = None,
        instance_id: str = None,
        instance_type: str = None,
        period: int = None,
        period_unit: str = None,
        spot_price_limit: float = None,
        spot_strategy: str = None,
        system_disk: main_models.GetClusterResponseBodyManagerManagerNodeSystemDisk = None,
    ):
        self.auto_renew = auto_renew
        self.auto_renew_period = auto_renew_period
        self.duration = duration
        self.enable_ht = enable_ht
        # The expiration time of the management node.
        self.expired_time = expired_time
        self.image_id = image_id
        # The instance billing method of the management node. Valid values:
        # 
        # *   PostPaid: pay-as-you-go
        # *   PrePaid: subscription
        self.instance_charge_type = instance_charge_type
        # The instance ID of the management node.
        self.instance_id = instance_id
        # The instance type of the management node.
        self.instance_type = instance_type
        self.period = period
        self.period_unit = period_unit
        self.spot_price_limit = spot_price_limit
        self.spot_strategy = spot_strategy
        self.system_disk = system_disk

    def validate(self):
        if self.system_disk:
            self.system_disk.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.enable_ht is not None:
            result['EnableHt'] = self.enable_ht

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.spot_price_limit is not None:
            result['SpotPriceLimit'] = self.spot_price_limit

        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy

        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('EnableHt') is not None:
            self.enable_ht = m.get('EnableHt')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('SpotPriceLimit') is not None:
            self.spot_price_limit = m.get('SpotPriceLimit')

        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')

        if m.get('SystemDisk') is not None:
            temp_model = main_models.GetClusterResponseBodyManagerManagerNodeSystemDisk()
            self.system_disk = temp_model.from_map(m.get('SystemDisk'))

        return self

class GetClusterResponseBodyManagerManagerNodeSystemDisk(DaraModel):
    def __init__(
        self,
        category: str = None,
        level: str = None,
        size: int = None,
    ):
        self.category = category
        self.level = level
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.level is not None:
            result['Level'] = self.level

        if self.size is not None:
            result['Size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        return self

class GetClusterResponseBodyManagerDirectoryService(DaraModel):
    def __init__(
        self,
        status: str = None,
        type: str = None,
        version: str = None,
    ):
        # The state of the domain account service. Valid values:
        # 
        # *   uninit: The service is being installed.
        # *   initing: The service is being initialized.
        # *   running: The service is running.
        # *   exception: The service has run into an exception.
        # *   releasing: The service is being released.
        # *   stopped: The service is stopped.
        # *   pending: The service is waiting to be configured.
        self.status = status
        # The type of the domain account.
        self.type = type
        # The version of the domain account service.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class GetClusterResponseBodyManagerDNS(DaraModel):
    def __init__(
        self,
        status: str = None,
        type: str = None,
        version: str = None,
    ):
        # The state of the domain name resolution service. Valid values:
        # 
        # *   uninit: The service is being installed.
        # *   initing: The service is being initialized.
        # *   running: The service is running.
        # *   exception: The service has run into an exception.
        # *   releasing: The service is being released.
        # *   stopped: The service is stopped.
        # *   pending: The service is waiting to be configured.
        self.status = status
        # The resolution type.
        self.type = type
        # The version of the resolution service.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class GetClusterResponseBodyClusterCustomConfiguration(DaraModel):
    def __init__(
        self,
        args: str = None,
        script: str = None,
    ):
        # The arguments that are used to run the script after the scrip is installed.
        self.args = args
        # The URL that is used to download the post-processing script.
        self.script = script

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.args is not None:
            result['Args'] = self.args

        if self.script is not None:
            result['Script'] = self.script

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Args') is not None:
            self.args = m.get('Args')

        if m.get('Script') is not None:
            self.script = m.get('Script')

        return self

