# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class CreateEdgeContainerAppVersionRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        containers: List[main_models.CreateEdgeContainerAppVersionRequestContainers] = None,
        name: str = None,
        remarks: str = None,
    ):
        # The application ID. You can call the [ListEdgeContainerApps](~~ListEdgeContainerApps~~) operation to obtain the application ID.
        # >Notice: 1) Your account must have an ESA plan with the Edge Container feature enabled. 2) Call CreateEdgeContainerApp first to create an application and obtain the AppId. 3) Complete call chain example: CreateEdgeContainerApp → ListEdgeContainerApps → CreateEdgeContainerAppVersion.</notice>
        # 
        # This parameter is required.
        self.app_id = app_id
        # The container group to be deployed for this version, including specific image information. The image information consists of the image address, startup command, parameters, environment variables, and probe rules. Multiple images are supported in a JSON array structure.
        # 
        # This parameter is required.
        self.containers = containers
        # The version name. The name must be **6 to 128** characters in length.
        # 
        # This parameter is required.
        self.name = name
        # The remarks.
        self.remarks = remarks

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

        if self.name is not None:
            result['Name'] = self.name

        if self.remarks is not None:
            result['Remarks'] = self.remarks

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        self.containers = []
        if m.get('Containers') is not None:
            for k1 in m.get('Containers'):
                temp_model = main_models.CreateEdgeContainerAppVersionRequestContainers()
                self.containers.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Remarks') is not None:
            self.remarks = m.get('Remarks')

        return self

class CreateEdgeContainerAppVersionRequestContainers(DaraModel):
    def __init__(
        self,
        acrimage_info: main_models.CreateEdgeContainerAppVersionRequestContainersACRImageInfo = None,
        args: str = None,
        command: str = None,
        env_variables: str = None,
        image: str = None,
        is_acrimage: bool = None,
        name: str = None,
        post_start: str = None,
        pre_stop: str = None,
        probe_content: main_models.CreateEdgeContainerAppVersionRequestContainersProbeContent = None,
        probe_type: str = None,
        spec: str = None,
        storage: str = None,
    ):
        # The ACR image information.
        self.acrimage_info = acrimage_info
        # The startup parameters. Separate multiple parameters with spaces.
        self.args = args
        # The startup command. Separate multiple commands with spaces.
        self.command = command
        # The environment variables. Format: key1=val1,key2=val2.
        self.env_variables = env_variables
        # The image address.
        # 
        # This parameter is required.
        self.image = image
        # Specifies whether the image is an Alibaba Cloud Container Registry (ACR) image.
        # 
        # This parameter is required.
        self.is_acrimage = is_acrimage
        # The container name. The name must be unique within the same container group.
        # 
        # This parameter is required.
        self.name = name
        # The command to execute before the container starts. Separate multiple commands with spaces. This command is executed before the service starts and is typically used for initialization operations.
        self.post_start = post_start
        # The command to execute before the container stops. Separate multiple commands with spaces. This command is executed before the service exits and is typically used for cleanup operations.
        self.pre_stop = pre_stop
        # The container health probe content.
        # 
        # This parameter is required.
        self.probe_content = probe_content
        # The probe type. Valid values:
        # - **exec**: Command-based.
        # - **tcpSocket**: TCP-based.
        # - **httpGet**: HTTP-based.
        # 
        # This parameter is required.
        self.probe_type = probe_type
        # The container specifications. Specifies the computing power specifications. Valid values: 1C2G, 2C4G, 2C8G, 4C8G, 4C16G, 8C16G, and 8C32G.
        # 
        # This parameter is required.
        self.spec = spec
        # The storage capacity. Valid values: 0.5G, 10G, 20G, and 30G.
        # 
        # This parameter is required.
        self.storage = storage

    def validate(self):
        if self.acrimage_info:
            self.acrimage_info.validate()
        if self.probe_content:
            self.probe_content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acrimage_info is not None:
            result['ACRImageInfo'] = self.acrimage_info.to_map()

        if self.args is not None:
            result['Args'] = self.args

        if self.command is not None:
            result['Command'] = self.command

        if self.env_variables is not None:
            result['EnvVariables'] = self.env_variables

        if self.image is not None:
            result['Image'] = self.image

        if self.is_acrimage is not None:
            result['IsACRImage'] = self.is_acrimage

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

        if self.storage is not None:
            result['Storage'] = self.storage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ACRImageInfo') is not None:
            temp_model = main_models.CreateEdgeContainerAppVersionRequestContainersACRImageInfo()
            self.acrimage_info = temp_model.from_map(m.get('ACRImageInfo'))

        if m.get('Args') is not None:
            self.args = m.get('Args')

        if m.get('Command') is not None:
            self.command = m.get('Command')

        if m.get('EnvVariables') is not None:
            self.env_variables = m.get('EnvVariables')

        if m.get('Image') is not None:
            self.image = m.get('Image')

        if m.get('IsACRImage') is not None:
            self.is_acrimage = m.get('IsACRImage')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PostStart') is not None:
            self.post_start = m.get('PostStart')

        if m.get('PreStop') is not None:
            self.pre_stop = m.get('PreStop')

        if m.get('ProbeContent') is not None:
            temp_model = main_models.CreateEdgeContainerAppVersionRequestContainersProbeContent()
            self.probe_content = temp_model.from_map(m.get('ProbeContent'))

        if m.get('ProbeType') is not None:
            self.probe_type = m.get('ProbeType')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        if m.get('Storage') is not None:
            self.storage = m.get('Storage')

        return self

class CreateEdgeContainerAppVersionRequestContainersProbeContent(DaraModel):
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
        # The probe command for exec-type probes.
        self.command = command
        # The number of consecutive failed health checks required.
        self.failure_threshold = failure_threshold
        # The domain name for the health check.
        self.host = host
        # The HTTP request headers.
        self.http_headers = http_headers
        # The initial delay time for the container probe, in seconds. For example, 5 indicates that the initial delay is set to 5 seconds.
        self.initial_delay_seconds = initial_delay_seconds
        # The path for the container health check.
        self.path = path
        # The interval between container health checks, in seconds. For example, 5 indicates that the health check interval is set to 5 seconds.
        self.period_seconds = period_seconds
        # The port for the container health check.
        self.port = port
        # The request protocol for the health check.
        self.scheme = scheme
        # The number of consecutive successful health checks required.
        self.success_threshold = success_threshold
        # The timeout period for the container health check, in seconds. For example, 5 indicates that the timeout is set to 5 seconds.
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

class CreateEdgeContainerAppVersionRequestContainersACRImageInfo(DaraModel):
    def __init__(
        self,
        domain: str = None,
        instance_id: str = None,
        is_enterprise_registry: bool = None,
        region_id: str = None,
        repo_id: str = None,
        repo_name: str = None,
        repo_namespace: str = None,
        tag: str = None,
        tag_url: str = None,
    ):
        # The ACR image domain name.
        self.domain = domain
        # The ACR instance ID.
        self.instance_id = instance_id
        # Specifies whether the image is an enterprise-level image.
        self.is_enterprise_registry = is_enterprise_registry
        # The region list of the ACR instance.
        self.region_id = region_id
        # The repository ID of the image.
        self.repo_id = repo_id
        # The image repository name.
        self.repo_name = repo_name
        # The namespace of the image repository.
        self.repo_namespace = repo_namespace
        # The ACR image tag.
        self.tag = tag
        # The ACR image tag URL.
        self.tag_url = tag_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.is_enterprise_registry is not None:
            result['IsEnterpriseRegistry'] = self.is_enterprise_registry

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.repo_id is not None:
            result['RepoId'] = self.repo_id

        if self.repo_name is not None:
            result['RepoName'] = self.repo_name

        if self.repo_namespace is not None:
            result['RepoNamespace'] = self.repo_namespace

        if self.tag is not None:
            result['Tag'] = self.tag

        if self.tag_url is not None:
            result['TagUrl'] = self.tag_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IsEnterpriseRegistry') is not None:
            self.is_enterprise_registry = m.get('IsEnterpriseRegistry')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')

        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')

        if m.get('RepoNamespace') is not None:
            self.repo_namespace = m.get('RepoNamespace')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('TagUrl') is not None:
            self.tag_url = m.get('TagUrl')

        return self

