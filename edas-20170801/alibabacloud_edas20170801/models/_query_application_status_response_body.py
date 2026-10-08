# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class QueryApplicationStatusResponseBody(DaraModel):
    def __init__(
        self,
        app_info: main_models.QueryApplicationStatusResponseBodyAppInfo = None,
        code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        # The information about the application.
        self.app_info = app_info
        # The HTTP status code that is returned.
        self.code = code
        # The additional information that is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.app_info:
            self.app_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_info is not None:
            result['AppInfo'] = self.app_info.to_map()

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInfo') is not None:
            temp_model = main_models.QueryApplicationStatusResponseBodyAppInfo()
            self.app_info = temp_model.from_map(m.get('AppInfo'))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QueryApplicationStatusResponseBodyAppInfo(DaraModel):
    def __init__(
        self,
        application: main_models.QueryApplicationStatusResponseBodyAppInfoApplication = None,
        deploy_record_list: main_models.QueryApplicationStatusResponseBodyAppInfoDeployRecordList = None,
        ecc_list: main_models.QueryApplicationStatusResponseBodyAppInfoEccList = None,
        ecu_list: main_models.QueryApplicationStatusResponseBodyAppInfoEcuList = None,
        group_list: main_models.QueryApplicationStatusResponseBodyAppInfoGroupList = None,
    ):
        # The basic information about the application.
        self.application = application
        self.deploy_record_list = deploy_record_list
        self.ecc_list = ecc_list
        self.ecu_list = ecu_list
        self.group_list = group_list

    def validate(self):
        if self.application:
            self.application.validate()
        if self.deploy_record_list:
            self.deploy_record_list.validate()
        if self.ecc_list:
            self.ecc_list.validate()
        if self.ecu_list:
            self.ecu_list.validate()
        if self.group_list:
            self.group_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application is not None:
            result['Application'] = self.application.to_map()

        if self.deploy_record_list is not None:
            result['DeployRecordList'] = self.deploy_record_list.to_map()

        if self.ecc_list is not None:
            result['EccList'] = self.ecc_list.to_map()

        if self.ecu_list is not None:
            result['EcuList'] = self.ecu_list.to_map()

        if self.group_list is not None:
            result['GroupList'] = self.group_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Application') is not None:
            temp_model = main_models.QueryApplicationStatusResponseBodyAppInfoApplication()
            self.application = temp_model.from_map(m.get('Application'))

        if m.get('DeployRecordList') is not None:
            temp_model = main_models.QueryApplicationStatusResponseBodyAppInfoDeployRecordList()
            self.deploy_record_list = temp_model.from_map(m.get('DeployRecordList'))

        if m.get('EccList') is not None:
            temp_model = main_models.QueryApplicationStatusResponseBodyAppInfoEccList()
            self.ecc_list = temp_model.from_map(m.get('EccList'))

        if m.get('EcuList') is not None:
            temp_model = main_models.QueryApplicationStatusResponseBodyAppInfoEcuList()
            self.ecu_list = temp_model.from_map(m.get('EcuList'))

        if m.get('GroupList') is not None:
            temp_model = main_models.QueryApplicationStatusResponseBodyAppInfoGroupList()
            self.group_list = temp_model.from_map(m.get('GroupList'))

        return self

class QueryApplicationStatusResponseBodyAppInfoGroupList(DaraModel):
    def __init__(
        self,
        group: List[main_models.QueryApplicationStatusResponseBodyAppInfoGroupListGroup] = None,
    ):
        self.group = group

    def validate(self):
        if self.group:
            for v1 in self.group:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Group'] = []
        if self.group is not None:
            for k1 in self.group:
                result['Group'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.group = []
        if m.get('Group') is not None:
            for k1 in m.get('Group'):
                temp_model = main_models.QueryApplicationStatusResponseBodyAppInfoGroupListGroup()
                self.group.append(temp_model.from_map(k1))

        return self

class QueryApplicationStatusResponseBodyAppInfoGroupListGroup(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_version_id: str = None,
        cluster_id: str = None,
        create_time: int = None,
        group_id: str = None,
        group_name: str = None,
        group_type: int = None,
        package_version_id: str = None,
        update_time: int = None,
    ):
        self.app_id = app_id
        self.app_version_id = app_version_id
        self.cluster_id = cluster_id
        self.create_time = create_time
        self.group_id = group_id
        self.group_name = group_name
        self.group_type = group_type
        self.package_version_id = package_version_id
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_version_id is not None:
            result['AppVersionId'] = self.app_version_id

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.group_type is not None:
            result['GroupType'] = self.group_type

        if self.package_version_id is not None:
            result['PackageVersionId'] = self.package_version_id

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')

        if m.get('PackageVersionId') is not None:
            self.package_version_id = m.get('PackageVersionId')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class QueryApplicationStatusResponseBodyAppInfoEcuList(DaraModel):
    def __init__(
        self,
        ecu: List[main_models.QueryApplicationStatusResponseBodyAppInfoEcuListEcu] = None,
    ):
        self.ecu = ecu

    def validate(self):
        if self.ecu:
            for v1 in self.ecu:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Ecu'] = []
        if self.ecu is not None:
            for k1 in self.ecu:
                result['Ecu'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ecu = []
        if m.get('Ecu') is not None:
            for k1 in m.get('Ecu'):
                temp_model = main_models.QueryApplicationStatusResponseBodyAppInfoEcuListEcu()
                self.ecu.append(temp_model.from_map(k1))

        return self

class QueryApplicationStatusResponseBodyAppInfoEcuListEcu(DaraModel):
    def __init__(
        self,
        available_cpu: int = None,
        available_mem: int = None,
        create_time: int = None,
        docker_env: bool = None,
        ecu_id: str = None,
        group_id: str = None,
        heartbeat_time: int = None,
        instance_id: str = None,
        ip_addr: str = None,
        name: str = None,
        online: bool = None,
        region_id: str = None,
        update_time: int = None,
        user_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        self.available_cpu = available_cpu
        self.available_mem = available_mem
        self.create_time = create_time
        self.docker_env = docker_env
        self.ecu_id = ecu_id
        self.group_id = group_id
        self.heartbeat_time = heartbeat_time
        self.instance_id = instance_id
        self.ip_addr = ip_addr
        self.name = name
        self.online = online
        self.region_id = region_id
        self.update_time = update_time
        self.user_id = user_id
        self.vpc_id = vpc_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_cpu is not None:
            result['AvailableCpu'] = self.available_cpu

        if self.available_mem is not None:
            result['AvailableMem'] = self.available_mem

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.docker_env is not None:
            result['DockerEnv'] = self.docker_env

        if self.ecu_id is not None:
            result['EcuId'] = self.ecu_id

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.heartbeat_time is not None:
            result['HeartbeatTime'] = self.heartbeat_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.ip_addr is not None:
            result['IpAddr'] = self.ip_addr

        if self.name is not None:
            result['Name'] = self.name

        if self.online is not None:
            result['Online'] = self.online

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableCpu') is not None:
            self.available_cpu = m.get('AvailableCpu')

        if m.get('AvailableMem') is not None:
            self.available_mem = m.get('AvailableMem')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DockerEnv') is not None:
            self.docker_env = m.get('DockerEnv')

        if m.get('EcuId') is not None:
            self.ecu_id = m.get('EcuId')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('HeartbeatTime') is not None:
            self.heartbeat_time = m.get('HeartbeatTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IpAddr') is not None:
            self.ip_addr = m.get('IpAddr')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Online') is not None:
            self.online = m.get('Online')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class QueryApplicationStatusResponseBodyAppInfoEccList(DaraModel):
    def __init__(
        self,
        ecc: List[main_models.QueryApplicationStatusResponseBodyAppInfoEccListEcc] = None,
    ):
        self.ecc = ecc

    def validate(self):
        if self.ecc:
            for v1 in self.ecc:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Ecc'] = []
        if self.ecc is not None:
            for k1 in self.ecc:
                result['Ecc'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ecc = []
        if m.get('Ecc') is not None:
            for k1 in m.get('Ecc'):
                temp_model = main_models.QueryApplicationStatusResponseBodyAppInfoEccListEcc()
                self.ecc.append(temp_model.from_map(k1))

        return self

class QueryApplicationStatusResponseBodyAppInfoEccListEcc(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_state: int = None,
        container_status: str = None,
        create_time: int = None,
        ecc_id: str = None,
        ecu_id: str = None,
        group_id: str = None,
        ip: str = None,
        task_state: int = None,
        update_time: int = None,
        vpc_id: str = None,
    ):
        self.app_id = app_id
        self.app_state = app_state
        self.container_status = container_status
        self.create_time = create_time
        self.ecc_id = ecc_id
        self.ecu_id = ecu_id
        self.group_id = group_id
        self.ip = ip
        self.task_state = task_state
        self.update_time = update_time
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_state is not None:
            result['AppState'] = self.app_state

        if self.container_status is not None:
            result['ContainerStatus'] = self.container_status

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.ecc_id is not None:
            result['EccId'] = self.ecc_id

        if self.ecu_id is not None:
            result['EcuId'] = self.ecu_id

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.task_state is not None:
            result['TaskState'] = self.task_state

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppState') is not None:
            self.app_state = m.get('AppState')

        if m.get('ContainerStatus') is not None:
            self.container_status = m.get('ContainerStatus')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('EccId') is not None:
            self.ecc_id = m.get('EccId')

        if m.get('EcuId') is not None:
            self.ecu_id = m.get('EcuId')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('TaskState') is not None:
            self.task_state = m.get('TaskState')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class QueryApplicationStatusResponseBodyAppInfoDeployRecordList(DaraModel):
    def __init__(
        self,
        deploy_record: List[main_models.QueryApplicationStatusResponseBodyAppInfoDeployRecordListDeployRecord] = None,
    ):
        self.deploy_record = deploy_record

    def validate(self):
        if self.deploy_record:
            for v1 in self.deploy_record:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DeployRecord'] = []
        if self.deploy_record is not None:
            for k1 in self.deploy_record:
                result['DeployRecord'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.deploy_record = []
        if m.get('DeployRecord') is not None:
            for k1 in m.get('DeployRecord'):
                temp_model = main_models.QueryApplicationStatusResponseBodyAppInfoDeployRecordListDeployRecord()
                self.deploy_record.append(temp_model.from_map(k1))

        return self

class QueryApplicationStatusResponseBodyAppInfoDeployRecordListDeployRecord(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        deploy_record_id: str = None,
        ecc_id: str = None,
        ecu_id: str = None,
        package_md_5: str = None,
        package_version_id: str = None,
    ):
        self.create_time = create_time
        self.deploy_record_id = deploy_record_id
        self.ecc_id = ecc_id
        self.ecu_id = ecu_id
        self.package_md_5 = package_md_5
        self.package_version_id = package_version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.deploy_record_id is not None:
            result['DeployRecordId'] = self.deploy_record_id

        if self.ecc_id is not None:
            result['EccId'] = self.ecc_id

        if self.ecu_id is not None:
            result['EcuId'] = self.ecu_id

        if self.package_md_5 is not None:
            result['PackageMd5'] = self.package_md_5

        if self.package_version_id is not None:
            result['PackageVersionId'] = self.package_version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DeployRecordId') is not None:
            self.deploy_record_id = m.get('DeployRecordId')

        if m.get('EccId') is not None:
            self.ecc_id = m.get('EccId')

        if m.get('EcuId') is not None:
            self.ecu_id = m.get('EcuId')

        if m.get('PackageMd5') is not None:
            self.package_md_5 = m.get('PackageMd5')

        if m.get('PackageVersionId') is not None:
            self.package_version_id = m.get('PackageVersionId')

        return self

class QueryApplicationStatusResponseBodyAppInfoApplication(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        build_package_id: int = None,
        cluster_id: str = None,
        cpu: int = None,
        create_time: int = None,
        dockerize: bool = None,
        email: str = None,
        health_check_url: str = None,
        instance_count: int = None,
        launch_time: int = None,
        memory: int = None,
        name: str = None,
        owner: str = None,
        phone: str = None,
        port: int = None,
        region_id: str = None,
        running_instance_count: int = None,
        user_id: str = None,
    ):
        # The ID of the application.
        self.application_id = application_id
        # The build package number of Enterprise Distributed Application Service (EDAS) Container.
        self.build_package_id = build_package_id
        # The ID of the cluster.
        self.cluster_id = cluster_id
        # The number of CPU cores used by the application.
        self.cpu = cpu
        # The time when the application was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_time = create_time
        # Indicates whether the application is a Docker application.
        self.dockerize = dockerize
        # The email address of the user who created the application.
        self.email = email
        # The health check URL.
        self.health_check_url = health_check_url
        # The number of application instances.
        self.instance_count = instance_count
        # The time when the application was launched. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.launch_time = launch_time
        # The memory size.
        self.memory = memory
        # The name of the application.
        self.name = name
        # The ID of the user who created the application.
        self.owner = owner
        # The mobile number of the user who created the application.
        self.phone = phone
        # The port used by the application.
        self.port = port
        # The ID of the namespace.
        self.region_id = region_id
        # The number of application instances that are running.
        self.running_instance_count = running_instance_count
        # The ID of the Alibaba Cloud account.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.build_package_id is not None:
            result['BuildPackageId'] = self.build_package_id

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.dockerize is not None:
            result['Dockerize'] = self.dockerize

        if self.email is not None:
            result['Email'] = self.email

        if self.health_check_url is not None:
            result['HealthCheckUrl'] = self.health_check_url

        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count

        if self.launch_time is not None:
            result['LaunchTime'] = self.launch_time

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.phone is not None:
            result['Phone'] = self.phone

        if self.port is not None:
            result['Port'] = self.port

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.running_instance_count is not None:
            result['RunningInstanceCount'] = self.running_instance_count

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('BuildPackageId') is not None:
            self.build_package_id = m.get('BuildPackageId')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Dockerize') is not None:
            self.dockerize = m.get('Dockerize')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('HealthCheckUrl') is not None:
            self.health_check_url = m.get('HealthCheckUrl')

        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')

        if m.get('LaunchTime') is not None:
            self.launch_time = m.get('LaunchTime')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('Phone') is not None:
            self.phone = m.get('Phone')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RunningInstanceCount') is not None:
            self.running_instance_count = m.get('RunningInstanceCount')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

