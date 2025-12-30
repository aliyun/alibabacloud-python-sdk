# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ehpc20240730 import models as main_models
from darabonba.model import DaraModel

class ListClustersResponseBody(DaraModel):
    def __init__(
        self,
        clusters: List[main_models.ListClustersResponseBodyClusters] = None,
        page_number: str = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of clusters.
        self.clusters = clusters
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.clusters:
            for v1 in self.clusters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Clusters'] = []
        if self.clusters is not None:
            for k1 in self.clusters:
                result['Clusters'].append(k1.to_map() if k1 else None)

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
        self.clusters = []
        if m.get('Clusters') is not None:
            for k1 in m.get('Clusters'):
                temp_model = main_models.ListClustersResponseBodyClusters()
                self.clusters.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListClustersResponseBodyClusters(DaraModel):
    def __init__(
        self,
        additional_packages: List[main_models.ListClustersResponseBodyClustersAdditionalPackages] = None,
        addons: List[main_models.ListClustersResponseBodyClustersAddons] = None,
        cluster_category: str = None,
        cluster_create_time: str = None,
        cluster_credentials: List[str] = None,
        cluster_custom_configuration: main_models.ListClustersResponseBodyClustersClusterCustomConfiguration = None,
        cluster_description: str = None,
        cluster_id: str = None,
        cluster_mode: str = None,
        cluster_modify_time: str = None,
        cluster_name: str = None,
        cluster_status: str = None,
        cluster_used_core_time: float = None,
        cluster_vswitch_id: str = None,
        cluster_vpc_id: str = None,
        deletion_protection: bool = None,
        ehpc_version: str = None,
        manager: main_models.ListClustersResponseBodyClustersManager = None,
        max_core_count: int = None,
        max_count: int = None,
        nodes: main_models.ListClustersResponseBodyClustersNodes = None,
        resource_group_id: str = None,
        security_group_id: str = None,
        users: main_models.ListClustersResponseBodyClustersUsers = None,
    ):
        # The information about installed software in the cluster.
        self.additional_packages = additional_packages
        # The information about the addons in the cluster.
        self.addons = addons
        # The cluster type. Valid values:
        # 
        # *   Standard
        # *   Serverless
        self.cluster_category = cluster_category
        # The time when the cluster was created. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. The time is displayed in UTC. For more information, see [ISO 8601](https://help.aliyun.com/document_detail/25696.html).
        self.cluster_create_time = cluster_create_time
        # The logon credential type of the cluster. Valid values:
        # 
        # *   password: requires passwords for logons.
        # *   keypair: requires key pairs for logons.
        self.cluster_credentials = cluster_credentials
        # The post-processing script used by the cluster.
        self.cluster_custom_configuration = cluster_custom_configuration
        # The cluster description.
        self.cluster_description = cluster_description
        # The cluster ID.
        self.cluster_id = cluster_id
        # The deployment type of the cluster. Valid values:
        # 
        # *   Integrated: public cloud
        # *   Hybrid: hybrid cloud
        # *   Custom: a custom cluster
        self.cluster_mode = cluster_mode
        # The time when the cluster was modified. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. The time is displayed in UTC. For more information, see [ISO 8601](https://help.aliyun.com/document_detail/25696.html).
        self.cluster_modify_time = cluster_modify_time
        # The cluster name.
        self.cluster_name = cluster_name
        # The cluster state. Valid values:
        # 
        # *   uninit: The cluster is being installed.
        # *   creating: The cluster is being created.
        # *   initing: The cluster is being initialized.
        # *   running: The cluster is running.
        # *   Releasing: The cluster is being released.
        # *   stopping: The cluster is being stopped.
        # *   stopped: The cluster is stopped.
        # *   exception: The cluster has run into an exception.
        # *   pending: The cluster is waiting to be configured.
        self.cluster_status = cluster_status
        # The vCPU-hour usage of the cluster.
        self.cluster_used_core_time = cluster_used_core_time
        # The ID of the vSwitch used by the cluster.
        self.cluster_vswitch_id = cluster_vswitch_id
        # The ID of the virtual private cloud (VPC) used by the cluster.
        self.cluster_vpc_id = cluster_vpc_id
        # Indicates whether deletion protection is enabled for the cluster. Valid values:
        # 
        # *   true
        # *   false
        self.deletion_protection = deletion_protection
        # The Elastic High Performance Computing (E-HPC) version.
        self.ehpc_version = ehpc_version
        # The configurations of the cluster management node.
        self.manager = manager
        # The maximum total number of vCPUs used by the compute nodes that can be managed by the cluster.
        self.max_core_count = max_core_count
        # The maximum number of compute nodes that can be managed by the cluster.
        self.max_count = max_count
        # The node statistics of the cluster.
        self.nodes = nodes
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The ID of the security group used by the cluster.
        self.security_group_id = security_group_id
        # The user attribute information of the cluster.
        self.users = users

    def validate(self):
        if self.additional_packages:
            for v1 in self.additional_packages:
                 if v1:
                    v1.validate()
        if self.addons:
            for v1 in self.addons:
                 if v1:
                    v1.validate()
        if self.cluster_custom_configuration:
            self.cluster_custom_configuration.validate()
        if self.manager:
            self.manager.validate()
        if self.nodes:
            self.nodes.validate()
        if self.users:
            self.users.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AdditionalPackages'] = []
        if self.additional_packages is not None:
            for k1 in self.additional_packages:
                result['AdditionalPackages'].append(k1.to_map() if k1 else None)

        result['Addons'] = []
        if self.addons is not None:
            for k1 in self.addons:
                result['Addons'].append(k1.to_map() if k1 else None)

        if self.cluster_category is not None:
            result['ClusterCategory'] = self.cluster_category

        if self.cluster_create_time is not None:
            result['ClusterCreateTime'] = self.cluster_create_time

        if self.cluster_credentials is not None:
            result['ClusterCredentials'] = self.cluster_credentials

        if self.cluster_custom_configuration is not None:
            result['ClusterCustomConfiguration'] = self.cluster_custom_configuration.to_map()

        if self.cluster_description is not None:
            result['ClusterDescription'] = self.cluster_description

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

        if self.cluster_used_core_time is not None:
            result['ClusterUsedCoreTime'] = self.cluster_used_core_time

        if self.cluster_vswitch_id is not None:
            result['ClusterVSwitchId'] = self.cluster_vswitch_id

        if self.cluster_vpc_id is not None:
            result['ClusterVpcId'] = self.cluster_vpc_id

        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection

        if self.ehpc_version is not None:
            result['EhpcVersion'] = self.ehpc_version

        if self.manager is not None:
            result['Manager'] = self.manager.to_map()

        if self.max_core_count is not None:
            result['MaxCoreCount'] = self.max_core_count

        if self.max_count is not None:
            result['MaxCount'] = self.max_count

        if self.nodes is not None:
            result['Nodes'] = self.nodes.to_map()

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.users is not None:
            result['Users'] = self.users.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.additional_packages = []
        if m.get('AdditionalPackages') is not None:
            for k1 in m.get('AdditionalPackages'):
                temp_model = main_models.ListClustersResponseBodyClustersAdditionalPackages()
                self.additional_packages.append(temp_model.from_map(k1))

        self.addons = []
        if m.get('Addons') is not None:
            for k1 in m.get('Addons'):
                temp_model = main_models.ListClustersResponseBodyClustersAddons()
                self.addons.append(temp_model.from_map(k1))

        if m.get('ClusterCategory') is not None:
            self.cluster_category = m.get('ClusterCategory')

        if m.get('ClusterCreateTime') is not None:
            self.cluster_create_time = m.get('ClusterCreateTime')

        if m.get('ClusterCredentials') is not None:
            self.cluster_credentials = m.get('ClusterCredentials')

        if m.get('ClusterCustomConfiguration') is not None:
            temp_model = main_models.ListClustersResponseBodyClustersClusterCustomConfiguration()
            self.cluster_custom_configuration = temp_model.from_map(m.get('ClusterCustomConfiguration'))

        if m.get('ClusterDescription') is not None:
            self.cluster_description = m.get('ClusterDescription')

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

        if m.get('ClusterUsedCoreTime') is not None:
            self.cluster_used_core_time = m.get('ClusterUsedCoreTime')

        if m.get('ClusterVSwitchId') is not None:
            self.cluster_vswitch_id = m.get('ClusterVSwitchId')

        if m.get('ClusterVpcId') is not None:
            self.cluster_vpc_id = m.get('ClusterVpcId')

        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')

        if m.get('EhpcVersion') is not None:
            self.ehpc_version = m.get('EhpcVersion')

        if m.get('Manager') is not None:
            temp_model = main_models.ListClustersResponseBodyClustersManager()
            self.manager = temp_model.from_map(m.get('Manager'))

        if m.get('MaxCoreCount') is not None:
            self.max_core_count = m.get('MaxCoreCount')

        if m.get('MaxCount') is not None:
            self.max_count = m.get('MaxCount')

        if m.get('Nodes') is not None:
            temp_model = main_models.ListClustersResponseBodyClustersNodes()
            self.nodes = temp_model.from_map(m.get('Nodes'))

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('Users') is not None:
            temp_model = main_models.ListClustersResponseBodyClustersUsers()
            self.users = temp_model.from_map(m.get('Users'))

        return self

class ListClustersResponseBodyClustersUsers(DaraModel):
    def __init__(
        self,
        normal_counts: int = None,
        sudo_counts: int = None,
    ):
        # The number of ordinary users.
        self.normal_counts = normal_counts
        # The number of administrators.
        self.sudo_counts = sudo_counts

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.normal_counts is not None:
            result['NormalCounts'] = self.normal_counts

        if self.sudo_counts is not None:
            result['SudoCounts'] = self.sudo_counts

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NormalCounts') is not None:
            self.normal_counts = m.get('NormalCounts')

        if m.get('SudoCounts') is not None:
            self.sudo_counts = m.get('SudoCounts')

        return self

class ListClustersResponseBodyClustersNodes(DaraModel):
    def __init__(
        self,
        abnormal_counts: int = None,
        creating_counts: int = None,
        running_counts: int = None,
    ):
        # The number of malfunctioning compute nodes.
        self.abnormal_counts = abnormal_counts
        # The number of compute nodes that are being created.
        self.creating_counts = creating_counts
        # The number of running compute nodes.
        self.running_counts = running_counts

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.abnormal_counts is not None:
            result['AbnormalCounts'] = self.abnormal_counts

        if self.creating_counts is not None:
            result['CreatingCounts'] = self.creating_counts

        if self.running_counts is not None:
            result['RunningCounts'] = self.running_counts

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AbnormalCounts') is not None:
            self.abnormal_counts = m.get('AbnormalCounts')

        if m.get('CreatingCounts') is not None:
            self.creating_counts = m.get('CreatingCounts')

        if m.get('RunningCounts') is not None:
            self.running_counts = m.get('RunningCounts')

        return self

class ListClustersResponseBodyClustersManager(DaraModel):
    def __init__(
        self,
        dns: main_models.ListClustersResponseBodyClustersManagerDNS = None,
        directory_service: main_models.ListClustersResponseBodyClustersManagerDirectoryService = None,
        scheduler: main_models.ListClustersResponseBodyClustersManagerScheduler = None,
    ):
        # The configurations of the domain name resolution service.
        self.dns = dns
        # The configurations of the directory service.
        self.directory_service = directory_service
        # The configurations of the scheduler service.
        self.scheduler = scheduler

    def validate(self):
        if self.dns:
            self.dns.validate()
        if self.directory_service:
            self.directory_service.validate()
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

        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DNS') is not None:
            temp_model = main_models.ListClustersResponseBodyClustersManagerDNS()
            self.dns = temp_model.from_map(m.get('DNS'))

        if m.get('DirectoryService') is not None:
            temp_model = main_models.ListClustersResponseBodyClustersManagerDirectoryService()
            self.directory_service = temp_model.from_map(m.get('DirectoryService'))

        if m.get('Scheduler') is not None:
            temp_model = main_models.ListClustersResponseBodyClustersManagerScheduler()
            self.scheduler = temp_model.from_map(m.get('Scheduler'))

        return self

class ListClustersResponseBodyClustersManagerScheduler(DaraModel):
    def __init__(
        self,
        type: str = None,
        version: str = None,
    ):
        # The scheduler type.
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
        if self.type is not None:
            result['Type'] = self.type

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class ListClustersResponseBodyClustersManagerDirectoryService(DaraModel):
    def __init__(
        self,
        type: str = None,
        version: str = None,
    ):
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
        if self.type is not None:
            result['Type'] = self.type

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class ListClustersResponseBodyClustersManagerDNS(DaraModel):
    def __init__(
        self,
        type: str = None,
        version: str = None,
    ):
        # The resolution type.
        self.type = type
        # The version of the domain name resolution service.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['Type'] = self.type

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class ListClustersResponseBodyClustersClusterCustomConfiguration(DaraModel):
    def __init__(
        self,
        args: str = None,
        script: str = None,
    ):
        # The parameters of the post-processing script.
        self.args = args
        # The link to the post-processing script.
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

class ListClustersResponseBodyClustersAddons(DaraModel):
    def __init__(
        self,
        addon_id: str = None,
        description: str = None,
        label: str = None,
        name: str = None,
        resources_spec: main_models.ListClustersResponseBodyClustersAddonsResourcesSpec = None,
        services_spec: List[main_models.ListClustersResponseBodyClustersAddonsServicesSpec] = None,
        status: str = None,
        version: str = None,
    ):
        # The addon ID.
        self.addon_id = addon_id
        # The addon description.
        self.description = description
        # The addon label.
        self.label = label
        # The addon name.
        # 
        # This parameter is required.
        self.name = name
        # The resource configurations of the addon.
        self.resources_spec = resources_spec
        # The information about the addon services.
        self.services_spec = services_spec
        # The addon state.
        self.status = status
        # The addon version.
        # 
        # This parameter is required.
        self.version = version

    def validate(self):
        if self.resources_spec:
            self.resources_spec.validate()
        if self.services_spec:
            for v1 in self.services_spec:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addon_id is not None:
            result['AddonId'] = self.addon_id

        if self.description is not None:
            result['Description'] = self.description

        if self.label is not None:
            result['Label'] = self.label

        if self.name is not None:
            result['Name'] = self.name

        if self.resources_spec is not None:
            result['ResourcesSpec'] = self.resources_spec.to_map()

        result['ServicesSpec'] = []
        if self.services_spec is not None:
            for k1 in self.services_spec:
                result['ServicesSpec'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddonId') is not None:
            self.addon_id = m.get('AddonId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ResourcesSpec') is not None:
            temp_model = main_models.ListClustersResponseBodyClustersAddonsResourcesSpec()
            self.resources_spec = temp_model.from_map(m.get('ResourcesSpec'))

        self.services_spec = []
        if m.get('ServicesSpec') is not None:
            for k1 in m.get('ServicesSpec'):
                temp_model = main_models.ListClustersResponseBodyClustersAddonsServicesSpec()
                self.services_spec.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class ListClustersResponseBodyClustersAddonsServicesSpec(DaraModel):
    def __init__(
        self,
        service_access_type: str = None,
        service_access_url: str = None,
        service_name: str = None,
    ):
        # The service access type.
        self.service_access_type = service_access_type
        # The service access URL.
        self.service_access_url = service_access_url
        # The service name.
        # 
        # This parameter is required.
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.service_access_type is not None:
            result['ServiceAccessType'] = self.service_access_type

        if self.service_access_url is not None:
            result['ServiceAccessUrl'] = self.service_access_url

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceAccessType') is not None:
            self.service_access_type = m.get('ServiceAccessType')

        if m.get('ServiceAccessUrl') is not None:
            self.service_access_url = m.get('ServiceAccessUrl')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        return self

class ListClustersResponseBodyClustersAddonsResourcesSpec(DaraModel):
    def __init__(
        self,
        ecs_instance_id: str = None,
        eip_instance_id: str = None,
    ):
        # The instance ID.
        self.ecs_instance_id = ecs_instance_id
        # The Elastic IP Address (EIP) ID.
        self.eip_instance_id = eip_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ecs_instance_id is not None:
            result['EcsInstanceId'] = self.ecs_instance_id

        if self.eip_instance_id is not None:
            result['EipInstanceId'] = self.eip_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EcsInstanceId') is not None:
            self.ecs_instance_id = m.get('EcsInstanceId')

        if m.get('EipInstanceId') is not None:
            self.eip_instance_id = m.get('EipInstanceId')

        return self

class ListClustersResponseBodyClustersAdditionalPackages(DaraModel):
    def __init__(
        self,
        name: str = None,
        version: str = None,
    ):
        # The software name.
        self.name = name
        # The software version.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

