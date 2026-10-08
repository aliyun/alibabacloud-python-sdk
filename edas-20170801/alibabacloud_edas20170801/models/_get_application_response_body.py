# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class GetApplicationResponseBody(DaraModel):
    def __init__(
        self,
        application: main_models.GetApplicationResponseBodyApplication = None,
        code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        # The application information.
        self.application = application
        # The status code.
        self.code = code
        # The additional information.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.application:
            self.application.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application is not None:
            result['Application'] = self.application.to_map()

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Application') is not None:
            temp_model = main_models.GetApplicationResponseBodyApplication()
            self.application = temp_model.from_map(m.get('Application'))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetApplicationResponseBodyApplication(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_phase: str = None,
        application_type: str = None,
        build_package_id: int = None,
        cluster_id: str = None,
        cluster_type: str = None,
        cpu: int = None,
        create_time: int = None,
        description: str = None,
        dockerize: bool = None,
        email: str = None,
        enable_port_check: bool = None,
        enable_url_check: bool = None,
        ext_slb_id: str = None,
        ext_slb_ip: str = None,
        ext_slb_name: str = None,
        have_manage_access: str = None,
        health_check_url: str = None,
        instance_count: int = None,
        memory: int = None,
        name: str = None,
        name_space: str = None,
        owner: str = None,
        port: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        running_instance_count: int = None,
        slb_id: str = None,
        slb_info: str = None,
        slb_ip: str = None,
        slb_name: str = None,
        slb_port: int = None,
        user_id: str = None,
        workload_type: str = None,
    ):
        # The application ID.
        self.app_id = app_id
        # The current phase of the Kubernetes application. This helps determine if the application is stable. Configuration operations are prohibited when the application is in an unstable state.
        # 
        # - ready: The application is ready and can be changed.
        # 
        # - progressing: The application is being changed.
        # 
        # - pending: The application change is blocked.
        # 
        # - failed: The application change failed.
        # 
        # The ready phase is stable. Other phases are unstable.
        self.app_phase = app_phase
        # The deployment type of the application:
        # 
        # - War: The application is deployed from a WAR package.
        # 
        # - FatJar: The application is deployed from a JAR package.
        # 
        # - Empty: The application is not deployed.
        self.application_type = application_type
        # The ID of the container version.
        self.build_package_id = build_package_id
        # The ID of the ECS cluster where the application is deployed.
        self.cluster_id = cluster_id
        # The type of the application cluster:
        # 
        # - 0: A regular Docker cluster.
        # 
        # - 1: A Swarm cluster.
        # 
        # - 2: An ECS cluster.
        # 
        # - 3: A Kubernetes cluster.
        # 
        # - 4: A Pandora application cluster that supports automatic registration.
        self.cluster_type = cluster_type
        # The number of CPU cores.
        self.cpu = cpu
        # The UNIX timestamp when the application was created.
        self.create_time = create_time
        # The description of the application.
        self.description = description
        # Indicates whether the application is a Docker application:
        # 
        # - false: The application is not a Docker application.
        # 
        # - true: The application is a Docker application.
        self.dockerize = dockerize
        # The email address.
        self.email = email
        # Indicates whether the port health check is enabled:
        # 
        # - true: Enabled.
        # 
        # - false: Disabled.
        # 
        # If enabled, EDAS checks if the port is in use during application startup. If the port is in use, the application is considered started.
        self.enable_port_check = enable_port_check
        # Indicates whether the URL health check is enabled:
        # 
        # - true: Enabled.
        # 
        # - false: Disabled.
        # 
        # If enabled, EDAS probes the specified URL during application startup. If the URL is accessible, the application is considered started.
        self.enable_url_check = enable_url_check
        # The ID of the public-facing SLB instance attached to the application.
        self.ext_slb_id = ext_slb_id
        # The public IP address of the SLB instance attached to the application.
        self.ext_slb_ip = ext_slb_ip
        # The name of the public-facing SLB instance attached to the application.
        self.ext_slb_name = ext_slb_name
        # Indicates whether the current user has management permissions on the application. This parameter is available only in RAM authentication mode.
        self.have_manage_access = have_manage_access
        # The health check URL of the application.
        self.health_check_url = health_check_url
        # The number of instances in the application.
        self.instance_count = instance_count
        # The memory size for the application instance, in MB.
        self.memory = memory
        # The name of the application.
        self.name = name
        # The namespace to which the application belongs.
        self.name_space = name_space
        # The creator of the application.
        self.owner = owner
        # The service port of the application.
        self.port = port
        # The ID of the region where the application is located.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The number of running application instances.
        self.running_instance_count = running_instance_count
        # The ID of the internal-facing SLB instance attached to the application.
        self.slb_id = slb_id
        # Information about the internal-facing SLB instance attached to the application.
        self.slb_info = slb_info
        # The IP address of the internal-facing SLB instance attached to the application.
        self.slb_ip = slb_ip
        # The name of the internal-facing SLB instance attached to the application.
        self.slb_name = slb_name
        # The port of the internal-facing SLB instance attached to the application.
        self.slb_port = slb_port
        # The ID of the Alibaba Cloud account.
        self.user_id = user_id
        # The workload type used to create the application. Supported types are Deployment and StatefulSet. This parameter does not apply to ECS applications.
        self.workload_type = workload_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_phase is not None:
            result['AppPhase'] = self.app_phase

        if self.application_type is not None:
            result['ApplicationType'] = self.application_type

        if self.build_package_id is not None:
            result['BuildPackageId'] = self.build_package_id

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.dockerize is not None:
            result['Dockerize'] = self.dockerize

        if self.email is not None:
            result['Email'] = self.email

        if self.enable_port_check is not None:
            result['EnablePortCheck'] = self.enable_port_check

        if self.enable_url_check is not None:
            result['EnableUrlCheck'] = self.enable_url_check

        if self.ext_slb_id is not None:
            result['ExtSlbId'] = self.ext_slb_id

        if self.ext_slb_ip is not None:
            result['ExtSlbIp'] = self.ext_slb_ip

        if self.ext_slb_name is not None:
            result['ExtSlbName'] = self.ext_slb_name

        if self.have_manage_access is not None:
            result['HaveManageAccess'] = self.have_manage_access

        if self.health_check_url is not None:
            result['HealthCheckUrl'] = self.health_check_url

        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.name is not None:
            result['Name'] = self.name

        if self.name_space is not None:
            result['NameSpace'] = self.name_space

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.port is not None:
            result['Port'] = self.port

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.running_instance_count is not None:
            result['RunningInstanceCount'] = self.running_instance_count

        if self.slb_id is not None:
            result['SlbId'] = self.slb_id

        if self.slb_info is not None:
            result['SlbInfo'] = self.slb_info

        if self.slb_ip is not None:
            result['SlbIp'] = self.slb_ip

        if self.slb_name is not None:
            result['SlbName'] = self.slb_name

        if self.slb_port is not None:
            result['SlbPort'] = self.slb_port

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.workload_type is not None:
            result['WorkloadType'] = self.workload_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppPhase') is not None:
            self.app_phase = m.get('AppPhase')

        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')

        if m.get('BuildPackageId') is not None:
            self.build_package_id = m.get('BuildPackageId')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Dockerize') is not None:
            self.dockerize = m.get('Dockerize')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('EnablePortCheck') is not None:
            self.enable_port_check = m.get('EnablePortCheck')

        if m.get('EnableUrlCheck') is not None:
            self.enable_url_check = m.get('EnableUrlCheck')

        if m.get('ExtSlbId') is not None:
            self.ext_slb_id = m.get('ExtSlbId')

        if m.get('ExtSlbIp') is not None:
            self.ext_slb_ip = m.get('ExtSlbIp')

        if m.get('ExtSlbName') is not None:
            self.ext_slb_name = m.get('ExtSlbName')

        if m.get('HaveManageAccess') is not None:
            self.have_manage_access = m.get('HaveManageAccess')

        if m.get('HealthCheckUrl') is not None:
            self.health_check_url = m.get('HealthCheckUrl')

        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NameSpace') is not None:
            self.name_space = m.get('NameSpace')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('RunningInstanceCount') is not None:
            self.running_instance_count = m.get('RunningInstanceCount')

        if m.get('SlbId') is not None:
            self.slb_id = m.get('SlbId')

        if m.get('SlbInfo') is not None:
            self.slb_info = m.get('SlbInfo')

        if m.get('SlbIp') is not None:
            self.slb_ip = m.get('SlbIp')

        if m.get('SlbName') is not None:
            self.slb_name = m.get('SlbName')

        if m.get('SlbPort') is not None:
            self.slb_port = m.get('SlbPort')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('WorkloadType') is not None:
            self.workload_type = m.get('WorkloadType')

        return self

