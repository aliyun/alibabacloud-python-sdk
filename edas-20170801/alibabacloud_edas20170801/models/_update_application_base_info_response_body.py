# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class UpdateApplicationBaseInfoResponseBody(DaraModel):
    def __init__(
        self,
        applcation: main_models.UpdateApplicationBaseInfoResponseBodyApplcation = None,
        code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        # The applications that you want to modify.
        self.applcation = applcation
        # The HTTP status code that is returned.
        self.code = code
        # The message that is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.applcation:
            self.applcation.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.applcation is not None:
            result['Applcation'] = self.applcation.to_map()

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Applcation') is not None:
            temp_model = main_models.UpdateApplicationBaseInfoResponseBodyApplcation()
            self.applcation = temp_model.from_map(m.get('Applcation'))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class UpdateApplicationBaseInfoResponseBodyApplcation(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        application_type: str = None,
        build_package_id: int = None,
        cluster_id: str = None,
        cluster_type: int = None,
        cpu: int = None,
        create_time: int = None,
        description: str = None,
        dockerize: bool = None,
        ext_slb_id: str = None,
        ext_slb_ip: str = None,
        ext_slb_name: str = None,
        health_check_url: str = None,
        instance_count: int = None,
        memory: int = None,
        name: str = None,
        owner: str = None,
        port: int = None,
        region_id: str = None,
        running_instance_count: int = None,
        slb_id: str = None,
        slb_ip: str = None,
        slb_name: str = None,
        slb_port: int = None,
        user_id: str = None,
    ):
        # The ID of the application.
        self.app_id = app_id
        # The deployment type of the application. Valid values:
        # 
        # - War: The application is deployed by using a WAR package.
        # 
        # - FatJar: The application is deployed by using a JAR package.
        # 
        # - Image: The application is deployed by using an image.
        # 
        # - If this parameter is empty, the application is not deployed.
        self.application_type = application_type
        # The build package number of Enterprise Distributed Application Service (EDAS) Container.
        self.build_package_id = build_package_id
        # The ID of the cluster.
        self.cluster_id = cluster_id
        # The type of the cluster. Valid values:
        # 
        # - 0: normal Docker cluster
        # 
        # - 1: Swarm cluster
        # 
        # - 2: ECS cluster
        # 
        # - 3: self-managed Kubernetes cluster in EDAS
        # 
        # - 4: cluster in which Pandora automatically registers applications
        # 
        # - 5: Container Service for Kubernetes (ACK) clusters
        self.cluster_type = cluster_type
        # The number of CPU cores.
        self.cpu = cpu
        # The time when the application was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_time = create_time
        # The description of the application.
        self.description = description
        # Indicates whether the application is a Docker application.
        self.dockerize = dockerize
        # The ID of the Internet-facing SLB instance.
        self.ext_slb_id = ext_slb_id
        # The IP address of the Internet-facing Server Load Balancer (SLB) instance.
        self.ext_slb_ip = ext_slb_ip
        # The name of the Internet-facing SLB instance.
        self.ext_slb_name = ext_slb_name
        # The health check URL.
        self.health_check_url = health_check_url
        # The number of application instances.
        self.instance_count = instance_count
        # The size of memory configured for an application instance. Unit: MB.
        self.memory = memory
        # The name of the application.
        self.name = name
        # The owner of the application.
        self.owner = owner
        # The port used by the application.
        self.port = port
        # The ID of the region.
        self.region_id = region_id
        # The number of running application instances.
        self.running_instance_count = running_instance_count
        # The ID of the internal-facing SLB instance.
        self.slb_id = slb_id
        # The IP address of the internal-facing SLB instance.
        self.slb_ip = slb_ip
        # The name of the internal-facing SLB instance.
        self.slb_name = slb_name
        # The port used by the internal-facing SLB instance.
        self.slb_port = slb_port
        # The ID of the Alibaba Cloud account.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

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

        if self.ext_slb_id is not None:
            result['ExtSlbId'] = self.ext_slb_id

        if self.ext_slb_ip is not None:
            result['ExtSlbIp'] = self.ext_slb_ip

        if self.ext_slb_name is not None:
            result['ExtSlbName'] = self.ext_slb_name

        if self.health_check_url is not None:
            result['HealthCheckUrl'] = self.health_check_url

        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.port is not None:
            result['Port'] = self.port

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.running_instance_count is not None:
            result['RunningInstanceCount'] = self.running_instance_count

        if self.slb_id is not None:
            result['SlbId'] = self.slb_id

        if self.slb_ip is not None:
            result['SlbIp'] = self.slb_ip

        if self.slb_name is not None:
            result['SlbName'] = self.slb_name

        if self.slb_port is not None:
            result['SlbPort'] = self.slb_port

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

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

        if m.get('ExtSlbId') is not None:
            self.ext_slb_id = m.get('ExtSlbId')

        if m.get('ExtSlbIp') is not None:
            self.ext_slb_ip = m.get('ExtSlbIp')

        if m.get('ExtSlbName') is not None:
            self.ext_slb_name = m.get('ExtSlbName')

        if m.get('HealthCheckUrl') is not None:
            self.health_check_url = m.get('HealthCheckUrl')

        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RunningInstanceCount') is not None:
            self.running_instance_count = m.get('RunningInstanceCount')

        if m.get('SlbId') is not None:
            self.slb_id = m.get('SlbId')

        if m.get('SlbIp') is not None:
            self.slb_ip = m.get('SlbIp')

        if m.get('SlbName') is not None:
            self.slb_name = m.get('SlbName')

        if m.get('SlbPort') is not None:
            self.slb_port = m.get('SlbPort')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

