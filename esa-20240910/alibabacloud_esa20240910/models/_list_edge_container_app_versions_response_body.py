# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ListEdgeContainerAppVersionsResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        versions: List[main_models.ListEdgeContainerAppVersionsResponseBodyVersions] = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count
        # The versions.
        self.versions = versions

    def validate(self):
        if self.versions:
            for v1 in self.versions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['Versions'] = []
        if self.versions is not None:
            for k1 in self.versions:
                result['Versions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.versions = []
        if m.get('Versions') is not None:
            for k1 in m.get('Versions'):
                temp_model = main_models.ListEdgeContainerAppVersionsResponseBodyVersions()
                self.versions.append(temp_model.from_map(k1))

        return self

class ListEdgeContainerAppVersionsResponseBodyVersions(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        containers: List[main_models.ListEdgeContainerAppVersionsResponseBodyVersionsContainers] = None,
        create_time: str = None,
        last_publish_time: str = None,
        name: str = None,
        publish_time: str = None,
        remarks: str = None,
        status: str = None,
        update_time: str = None,
        version_id: str = None,
    ):
        # The application ID.
        self.app_id = app_id
        # The containers in the version.
        self.containers = containers
        # The time when the version was created. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC.
        self.create_time = create_time
        # The time when the version was last released. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC.
        self.last_publish_time = last_publish_time
        # The version name.
        self.name = name
        # The time when the version was released. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC.
        self.publish_time = publish_time
        # The remarks.
        self.remarks = remarks
        # The status of the current version. Valid values:
        # 
        # *   **created**
        # *   **failed**
        # *   **creating**
        self.status = status
        # The time when the version was last modified. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC.
        self.update_time = update_time
        # The version ID.
        self.version_id = version_id

    def validate(self):
        if self.containers:
            for v1 in self.containers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        result['Containers'] = []
        if self.containers is not None:
            for k1 in self.containers:
                result['Containers'].append(k1.to_map() if k1 else None)

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.last_publish_time is not None:
            result['LastPublishTime'] = self.last_publish_time

        if self.name is not None:
            result['Name'] = self.name

        if self.publish_time is not None:
            result['PublishTime'] = self.publish_time

        if self.remarks is not None:
            result['Remarks'] = self.remarks

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        self.containers = []
        if m.get('Containers') is not None:
            for k1 in m.get('Containers'):
                temp_model = main_models.ListEdgeContainerAppVersionsResponseBodyVersionsContainers()
                self.containers.append(temp_model.from_map(k1))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('LastPublishTime') is not None:
            self.last_publish_time = m.get('LastPublishTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PublishTime') is not None:
            self.publish_time = m.get('PublishTime')

        if m.get('Remarks') is not None:
            self.remarks = m.get('Remarks')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        return self

class ListEdgeContainerAppVersionsResponseBodyVersionsContainers(DaraModel):
    def __init__(
        self,
        args: str = None,
        command: str = None,
        env_variables: str = None,
        image: str = None,
        name: str = None,
        post_start: str = None,
        pre_stop: str = None,
        probe_content: main_models.ListEdgeContainerAppVersionsResponseBodyVersionsContainersProbeContent = None,
        probe_type: str = None,
        spec: str = None,
    ):
        # The arguments that are passed to the container startup command.
        self.args = args
        # The command that is used to start the container.
        self.command = command
        # The environment variables of the container.
        self.env_variables = env_variables
        # The address of the container image.
        self.image = image
        # The container name.
        self.name = name
        # The command that is run before the container is started. Format: `{"exec":{"command":["cat","/etc/group"\\]}}`.
        # 
        # If you want to cancel this configuration, set the parameter value to `""` or `{}`. If you do not specify this parameter, this configuration is ignored.
        self.post_start = post_start
        # The command that is run before the container is stopped.
        self.pre_stop = pre_stop
        # The container probe content.
        self.probe_content = probe_content
        # The probe type of the container.
        self.probe_type = probe_type
        # The compute specification of the container.
        self.spec = spec

    def validate(self):
        if self.probe_content:
            self.probe_content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.args is not None:
            result['Args'] = self.args

        if self.command is not None:
            result['Command'] = self.command

        if self.env_variables is not None:
            result['EnvVariables'] = self.env_variables

        if self.image is not None:
            result['Image'] = self.image

        if self.name is not None:
            result['Name'] = self.name

        if self.post_start is not None:
            result['PostStart'] = self.post_start

        if self.pre_stop is not None:
            result['PreStop'] = self.pre_stop

        if self.probe_content is not None:
            result['ProbeContent'] = self.probe_content.to_map()

        if self.probe_type is not None:
            result['ProbeType'] = self.probe_type

        if self.spec is not None:
            result['Spec'] = self.spec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Args') is not None:
            self.args = m.get('Args')

        if m.get('Command') is not None:
            self.command = m.get('Command')

        if m.get('EnvVariables') is not None:
            self.env_variables = m.get('EnvVariables')

        if m.get('Image') is not None:
            self.image = m.get('Image')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PostStart') is not None:
            self.post_start = m.get('PostStart')

        if m.get('PreStop') is not None:
            self.pre_stop = m.get('PreStop')

        if m.get('ProbeContent') is not None:
            temp_model = main_models.ListEdgeContainerAppVersionsResponseBodyVersionsContainersProbeContent()
            self.probe_content = temp_model.from_map(m.get('ProbeContent'))

        if m.get('ProbeType') is not None:
            self.probe_type = m.get('ProbeType')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        return self

class ListEdgeContainerAppVersionsResponseBodyVersionsContainersProbeContent(DaraModel):
    def __init__(
        self,
        command: str = None,
        failure_threshold: int = None,
        host: str = None,
        http_headers: str = None,
        initial_delay_seconds: int = None,
        path: str = None,
        period_seconds: int = None,
        port: int = None,
        scheme: str = None,
        success_threshold: int = None,
        timeout_seconds: int = None,
    ):
        # The probe command.
        self.command = command
        # The number of consecutive failed health checks required for a container to be considered as unhealthy.
        self.failure_threshold = failure_threshold
        # The domain name that is used for health checks.
        self.host = host
        # The request headers that are included in the container health check request.
        self.http_headers = http_headers
        # The latency for container probe initialization.
        self.initial_delay_seconds = initial_delay_seconds
        # The path of the container health check.
        self.path = path
        # The interval between container health checks.
        self.period_seconds = period_seconds
        # The port of the container health check.
        self.port = port
        # The protocol that the container health check request uses.
        self.scheme = scheme
        # The number of consecutive successful health checks required for a container to be considered as healthy.
        self.success_threshold = success_threshold
        # The timeout period of the container health check.
        self.timeout_seconds = timeout_seconds

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.command is not None:
            result['Command'] = self.command

        if self.failure_threshold is not None:
            result['FailureThreshold'] = self.failure_threshold

        if self.host is not None:
            result['Host'] = self.host

        if self.http_headers is not None:
            result['HttpHeaders'] = self.http_headers

        if self.initial_delay_seconds is not None:
            result['InitialDelaySeconds'] = self.initial_delay_seconds

        if self.path is not None:
            result['Path'] = self.path

        if self.period_seconds is not None:
            result['PeriodSeconds'] = self.period_seconds

        if self.port is not None:
            result['Port'] = self.port

        if self.scheme is not None:
            result['Scheme'] = self.scheme

        if self.success_threshold is not None:
            result['SuccessThreshold'] = self.success_threshold

        if self.timeout_seconds is not None:
            result['TimeoutSeconds'] = self.timeout_seconds

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Command') is not None:
            self.command = m.get('Command')

        if m.get('FailureThreshold') is not None:
            self.failure_threshold = m.get('FailureThreshold')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('HttpHeaders') is not None:
            self.http_headers = m.get('HttpHeaders')

        if m.get('InitialDelaySeconds') is not None:
            self.initial_delay_seconds = m.get('InitialDelaySeconds')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('PeriodSeconds') is not None:
            self.period_seconds = m.get('PeriodSeconds')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Scheme') is not None:
            self.scheme = m.get('Scheme')

        if m.get('SuccessThreshold') is not None:
            self.success_threshold = m.get('SuccessThreshold')

        if m.get('TimeoutSeconds') is not None:
            self.timeout_seconds = m.get('TimeoutSeconds')

        return self

