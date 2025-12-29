# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class DescribeApplicationInstancesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeApplicationInstancesResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        # The HTTP status code. Valid values:
        # 
        # *   **2xx**: indicates that the request was successful.
        # *   **3xx**: indicates that the request was redirected.
        # *   **4xx**: indicates that the request was invalid.
        # *   **5xx**: indicates that a server error occurred.
        self.code = code
        # The details of the application instance.
        self.data = data
        # The error code. 
        # 
        # - The **ErrorCode** parameter is not returned when the request succeeds.
        # - The **ErrorCode** parameter is returned when the request fails. For more information, see **Error codes** in this topic.
        self.error_code = error_code
        # The returned message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the list of application instances was obtained. Valid values:
        # 
        # *   **true**: indicates that the list was obtained.
        # *   **false**: indicates that the list could not be obtained.
        self.success = success
        # The ID of the trace. It is used to query the details of a request.
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.DescribeApplicationInstancesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        return self

class DescribeApplicationInstancesResponseBodyData(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        instances: List[main_models.DescribeApplicationInstancesResponseBodyDataInstances] = None,
        page_size: int = None,
        total_size: int = None,
    ):
        # The number of the returned page.
        self.current_page = current_page
        # The application instances.
        self.instances = instances
        # The number of entries returned on each page.
        self.page_size = page_size
        # The total number of returned instances.
        self.total_size = total_size

    def validate(self):
        if self.instances:
            for v1 in self.instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        result['Instances'] = []
        if self.instances is not None:
            for k1 in self.instances:
                result['Instances'].append(k1.to_map() if k1 else None)

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_size is not None:
            result['TotalSize'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.instances = []
        if m.get('Instances') is not None:
            for k1 in m.get('Instances'):
                temp_model = main_models.DescribeApplicationInstancesResponseBodyDataInstances()
                self.instances.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')

        return self

class DescribeApplicationInstancesResponseBodyDataInstances(DaraModel):
    def __init__(
        self,
        create_time_stamp: int = None,
        debug_status: bool = None,
        eip: str = None,
        finish_time_stamp: int = None,
        group_id: str = None,
        image_url: str = None,
        instance_container_ip: str = None,
        instance_container_restarts: int = None,
        instance_container_status: str = None,
        instance_health_status: str = None,
        instance_id: str = None,
        main_container_status: str = None,
        package_version: str = None,
        sidecar_containers_status: List[main_models.DescribeApplicationInstancesResponseBodyDataInstancesSidecarContainersStatus] = None,
        tags: List[main_models.DescribeApplicationInstancesResponseBodyDataInstancesTags] = None,
        timestamp: int = None,
        traffic_status: str = None,
        unhealthy_message: str = None,
        v_switch_id: str = None,
    ):
        # The start time of the instance creation process. Unit: milliseconds.
        self.create_time_stamp = create_time_stamp
        self.debug_status = debug_status
        # The elastic IP address (EIP).
        self.eip = eip
        # The end time of the instance creation process. Unit: milliseconds.
        self.finish_time_stamp = finish_time_stamp
        # The ID of the group to which the instance belongs.
        self.group_id = group_id
        # The address of the repository.
        # 
        # >  If you deploy the application by using a JAR or WAR package, the image generated by SAE is not available for download.
        self.image_url = image_url
        # The internal IP address of the instance.
        self.instance_container_ip = instance_container_ip
        # The number of times that the instance restarted.
        self.instance_container_restarts = instance_container_restarts
        # The state of the instance. Valid values:
        # 
        # *   **Error**: An error occurred during the instance startup.
        # *   **CrashLoopBackOff**: The container failed to start. An error occurred during the startup process and persisted after the restart.
        # *   **ErrImagePull**: An error occurred while the container image was being pulled from the instance.
        # *   **ImagePullBackOff**: The container image could not be obtained.
        # *   **Pending**: The instance is waiting to be scheduled.
        # *   **Unknown**: An unknown exception occurred.
        # *   **Terminating**: The instance creation process is being terminated.
        # *   **NotFound**: The instance cannot be found.
        # *   **PodInitializing**: The instance is being initialized.
        # *   **Init:0/1**: The instance is initialized.
        # *   **Running**: The instance is running.
        self.instance_container_status = instance_container_status
        # The configurations of health checks. Valid values:
        # 
        # *   **WithoutHealthCheckConfig**: Liveness and readiness checks are not configured.
        # *   **WithoutLivenessConfig**: The liveness check is not configured.
        # *   **WithoutReadinessConfig**: The readiness check is not configured.
        # *   **NotCheckedYet**: The health checks are not performed or are in progress.
        # *   **LivenessUnhealthy**: The instance failed the liveness check.
        # *   **ReadinessUnhealthy**: The instance failed the readiness check.
        # *   **Unhealthy**: The instance failed both liveness and readiness checks.
        # *   **Healthy**: The instance passed both liveness and readiness checks.
        self.instance_health_status = instance_health_status
        # The ID of the instance.
        self.instance_id = instance_id
        # The status of the main container.
        self.main_container_status = main_container_status
        # The version of the package.
        self.package_version = package_version
        # The status of the sidecar container.
        self.sidecar_containers_status = sidecar_containers_status
        self.tags = tags
        self.timestamp = timestamp
        self.traffic_status = traffic_status
        # If the health check of an application instance fails, the detailed failure cause or error message is returned. If the health check of an application instance passes, no response is returned.
        self.unhealthy_message = unhealthy_message
        # The ID of the zone where the instance is deployed.
        self.v_switch_id = v_switch_id

    def validate(self):
        if self.sidecar_containers_status:
            for v1 in self.sidecar_containers_status:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time_stamp is not None:
            result['CreateTimeStamp'] = self.create_time_stamp

        if self.debug_status is not None:
            result['DebugStatus'] = self.debug_status

        if self.eip is not None:
            result['Eip'] = self.eip

        if self.finish_time_stamp is not None:
            result['FinishTimeStamp'] = self.finish_time_stamp

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.instance_container_ip is not None:
            result['InstanceContainerIp'] = self.instance_container_ip

        if self.instance_container_restarts is not None:
            result['InstanceContainerRestarts'] = self.instance_container_restarts

        if self.instance_container_status is not None:
            result['InstanceContainerStatus'] = self.instance_container_status

        if self.instance_health_status is not None:
            result['InstanceHealthStatus'] = self.instance_health_status

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.main_container_status is not None:
            result['MainContainerStatus'] = self.main_container_status

        if self.package_version is not None:
            result['PackageVersion'] = self.package_version

        result['SidecarContainersStatus'] = []
        if self.sidecar_containers_status is not None:
            for k1 in self.sidecar_containers_status:
                result['SidecarContainersStatus'].append(k1.to_map() if k1 else None)

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        if self.traffic_status is not None:
            result['TrafficStatus'] = self.traffic_status

        if self.unhealthy_message is not None:
            result['UnhealthyMessage'] = self.unhealthy_message

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTimeStamp') is not None:
            self.create_time_stamp = m.get('CreateTimeStamp')

        if m.get('DebugStatus') is not None:
            self.debug_status = m.get('DebugStatus')

        if m.get('Eip') is not None:
            self.eip = m.get('Eip')

        if m.get('FinishTimeStamp') is not None:
            self.finish_time_stamp = m.get('FinishTimeStamp')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('InstanceContainerIp') is not None:
            self.instance_container_ip = m.get('InstanceContainerIp')

        if m.get('InstanceContainerRestarts') is not None:
            self.instance_container_restarts = m.get('InstanceContainerRestarts')

        if m.get('InstanceContainerStatus') is not None:
            self.instance_container_status = m.get('InstanceContainerStatus')

        if m.get('InstanceHealthStatus') is not None:
            self.instance_health_status = m.get('InstanceHealthStatus')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MainContainerStatus') is not None:
            self.main_container_status = m.get('MainContainerStatus')

        if m.get('PackageVersion') is not None:
            self.package_version = m.get('PackageVersion')

        self.sidecar_containers_status = []
        if m.get('SidecarContainersStatus') is not None:
            for k1 in m.get('SidecarContainersStatus'):
                temp_model = main_models.DescribeApplicationInstancesResponseBodyDataInstancesSidecarContainersStatus()
                self.sidecar_containers_status.append(temp_model.from_map(k1))

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeApplicationInstancesResponseBodyDataInstancesTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        if m.get('TrafficStatus') is not None:
            self.traffic_status = m.get('TrafficStatus')

        if m.get('UnhealthyMessage') is not None:
            self.unhealthy_message = m.get('UnhealthyMessage')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

class DescribeApplicationInstancesResponseBodyDataInstancesTags(DaraModel):
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

class DescribeApplicationInstancesResponseBodyDataInstancesSidecarContainersStatus(DaraModel):
    def __init__(
        self,
        container_id: str = None,
        container_status: str = None,
        image_url: str = None,
    ):
        # The ID of the sidecar container.
        self.container_id = container_id
        # The status of the container.
        self.container_status = container_status
        # The URL of the image.
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.container_id is not None:
            result['ContainerId'] = self.container_id

        if self.container_status is not None:
            result['ContainerStatus'] = self.container_status

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerId') is not None:
            self.container_id = m.get('ContainerId')

        if m.get('ContainerStatus') is not None:
            self.container_status = m.get('ContainerStatus')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        return self

