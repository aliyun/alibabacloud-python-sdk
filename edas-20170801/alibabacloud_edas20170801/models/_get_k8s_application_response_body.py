# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class GetK8sApplicationResponseBody(DaraModel):
    def __init__(
        self,
        applcation: main_models.GetK8sApplicationResponseBodyApplcation = None,
        code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        # The application information.
        self.applcation = applcation
        # The HTTP status code.
        self.code = code
        # The additional information.
        self.message = message
        # The request ID.
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
            temp_model = main_models.GetK8sApplicationResponseBodyApplcation()
            self.applcation = temp_model.from_map(m.get('Applcation'))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetK8sApplicationResponseBodyApplcation(DaraModel):
    def __init__(
        self,
        app: main_models.GetK8sApplicationResponseBodyApplcationApp = None,
        app_id: str = None,
        conf: main_models.GetK8sApplicationResponseBodyApplcationConf = None,
        deploy_groups: main_models.GetK8sApplicationResponseBodyApplcationDeployGroups = None,
        image_info: main_models.GetK8sApplicationResponseBodyApplcationImageInfo = None,
        latest_version: main_models.GetK8sApplicationResponseBodyApplcationLatestVersion = None,
    ):
        # The basic information about the application.
        self.app = app
        # The ID of the application. You can call the [ListApplication](https://help.aliyun.com/document_detail/149390.html) operation to obtain the application ID.
        self.app_id = app_id
        # The configuration information.
        self.conf = conf
        self.deploy_groups = deploy_groups
        # The image information.
        self.image_info = image_info
        # The information about the latest version.
        self.latest_version = latest_version

    def validate(self):
        if self.app:
            self.app.validate()
        if self.conf:
            self.conf.validate()
        if self.deploy_groups:
            self.deploy_groups.validate()
        if self.image_info:
            self.image_info.validate()
        if self.latest_version:
            self.latest_version.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app is not None:
            result['App'] = self.app.to_map()

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.conf is not None:
            result['Conf'] = self.conf.to_map()

        if self.deploy_groups is not None:
            result['DeployGroups'] = self.deploy_groups.to_map()

        if self.image_info is not None:
            result['ImageInfo'] = self.image_info.to_map()

        if self.latest_version is not None:
            result['LatestVersion'] = self.latest_version.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            temp_model = main_models.GetK8sApplicationResponseBodyApplcationApp()
            self.app = temp_model.from_map(m.get('App'))

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Conf') is not None:
            temp_model = main_models.GetK8sApplicationResponseBodyApplcationConf()
            self.conf = temp_model.from_map(m.get('Conf'))

        if m.get('DeployGroups') is not None:
            temp_model = main_models.GetK8sApplicationResponseBodyApplcationDeployGroups()
            self.deploy_groups = temp_model.from_map(m.get('DeployGroups'))

        if m.get('ImageInfo') is not None:
            temp_model = main_models.GetK8sApplicationResponseBodyApplcationImageInfo()
            self.image_info = temp_model.from_map(m.get('ImageInfo'))

        if m.get('LatestVersion') is not None:
            temp_model = main_models.GetK8sApplicationResponseBodyApplcationLatestVersion()
            self.latest_version = temp_model.from_map(m.get('LatestVersion'))

        return self

class GetK8sApplicationResponseBodyApplcationLatestVersion(DaraModel):
    def __init__(
        self,
        package_version: str = None,
        url: str = None,
        war_url: str = None,
    ):
        # The version number of the deployment package.
        self.package_version = package_version
        # The URL of the deployment package. This parameter is required for applications that are deployed using a FatJar or WAR package.
        self.url = url
        # The URL of the deployment package. This parameter is required for applications that are deployed using a FatJar or WAR package.
        self.war_url = war_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.package_version is not None:
            result['PackageVersion'] = self.package_version

        if self.url is not None:
            result['Url'] = self.url

        if self.war_url is not None:
            result['WarUrl'] = self.war_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PackageVersion') is not None:
            self.package_version = m.get('PackageVersion')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('WarUrl') is not None:
            self.war_url = m.get('WarUrl')

        return self

class GetK8sApplicationResponseBodyApplcationImageInfo(DaraModel):
    def __init__(
        self,
        image_url: str = None,
        region_id: str = None,
        repo_id: str = None,
        repo_name: str = None,
        repo_namespace: str = None,
        repo_origin_type: str = None,
        tag: str = None,
    ):
        # The URL of the image.
        self.image_url = image_url
        # The ID of the region where the image is located.
        self.region_id = region_id
        # The ID of the image repository.
        self.repo_id = repo_id
        # The name of the image repository.
        self.repo_name = repo_name
        # The namespace of the image repository.
        self.repo_namespace = repo_namespace
        # The type of the source of the image repository.
        self.repo_origin_type = repo_origin_type
        # The tag of the image.
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.repo_id is not None:
            result['RepoId'] = self.repo_id

        if self.repo_name is not None:
            result['RepoName'] = self.repo_name

        if self.repo_namespace is not None:
            result['RepoNamespace'] = self.repo_namespace

        if self.repo_origin_type is not None:
            result['RepoOriginType'] = self.repo_origin_type

        if self.tag is not None:
            result['Tag'] = self.tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')

        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')

        if m.get('RepoNamespace') is not None:
            self.repo_namespace = m.get('RepoNamespace')

        if m.get('RepoOriginType') is not None:
            self.repo_origin_type = m.get('RepoOriginType')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        return self

class GetK8sApplicationResponseBodyApplcationDeployGroups(DaraModel):
    def __init__(
        self,
        deploy_group: List[main_models.GetK8sApplicationResponseBodyApplcationDeployGroupsDeployGroup] = None,
    ):
        self.deploy_group = deploy_group

    def validate(self):
        if self.deploy_group:
            for v1 in self.deploy_group:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DeployGroup'] = []
        if self.deploy_group is not None:
            for k1 in self.deploy_group:
                result['DeployGroup'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.deploy_group = []
        if m.get('DeployGroup') is not None:
            for k1 in m.get('DeployGroup'):
                temp_model = main_models.GetK8sApplicationResponseBodyApplcationDeployGroupsDeployGroup()
                self.deploy_group.append(temp_model.from_map(k1))

        return self

class GetK8sApplicationResponseBodyApplcationDeployGroupsDeployGroup(DaraModel):
    def __init__(
        self,
        components: main_models.GetK8sApplicationResponseBodyApplcationDeployGroupsDeployGroupComponents = None,
        env: str = None,
        env_from: str = None,
    ):
        self.components = components
        self.env = env
        self.env_from = env_from

    def validate(self):
        if self.components:
            self.components.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.components is not None:
            result['Components'] = self.components.to_map()

        if self.env is not None:
            result['Env'] = self.env

        if self.env_from is not None:
            result['EnvFrom'] = self.env_from

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Components') is not None:
            temp_model = main_models.GetK8sApplicationResponseBodyApplcationDeployGroupsDeployGroupComponents()
            self.components = temp_model.from_map(m.get('Components'))

        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('EnvFrom') is not None:
            self.env_from = m.get('EnvFrom')

        return self

class GetK8sApplicationResponseBodyApplcationDeployGroupsDeployGroupComponents(DaraModel):
    def __init__(
        self,
        components: List[main_models.GetK8sApplicationResponseBodyApplcationDeployGroupsDeployGroupComponentsComponents] = None,
    ):
        self.components = components

    def validate(self):
        if self.components:
            for v1 in self.components:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Components'] = []
        if self.components is not None:
            for k1 in self.components:
                result['Components'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.components = []
        if m.get('Components') is not None:
            for k1 in m.get('Components'):
                temp_model = main_models.GetK8sApplicationResponseBodyApplcationDeployGroupsDeployGroupComponentsComponents()
                self.components.append(temp_model.from_map(k1))

        return self

class GetK8sApplicationResponseBodyApplcationDeployGroupsDeployGroupComponentsComponents(DaraModel):
    def __init__(
        self,
        component_id: str = None,
        component_key: str = None,
        type: str = None,
    ):
        self.component_id = component_id
        self.component_key = component_key
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_id is not None:
            result['ComponentId'] = self.component_id

        if self.component_key is not None:
            result['ComponentKey'] = self.component_key

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentId') is not None:
            self.component_id = m.get('ComponentId')

        if m.get('ComponentKey') is not None:
            self.component_key = m.get('ComponentKey')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetK8sApplicationResponseBodyApplcationConf(DaraModel):
    def __init__(
        self,
        affinity: str = None,
        ahas_enabled: bool = None,
        deploy_across_nodes: str = None,
        deploy_across_zones: str = None,
        jar_start_args: str = None,
        jar_start_options: str = None,
        k_8s_cmd: str = None,
        k_8s_cmd_args: str = None,
        k_8s_localvolume_info: str = None,
        k_8s_nas_info: str = None,
        k_8s_volume_info: str = None,
        liveness: str = None,
        post_start: str = None,
        pre_stop: str = None,
        readiness: str = None,
        runtime_class_name: str = None,
        tolerations: str = None,
        user_base_image_url: str = None,
    ):
        # The pod affinity configuration.
        self.affinity = affinity
        # Indicates whether the application is connected to AHAS.
        self.ahas_enabled = ahas_enabled
        # Indicates whether to distribute application instances across multiple nodes:
        # 
        # - `true`: The application instances are distributed across multiple nodes.
        # 
        # - Other values: The application instances are not distributed across multiple nodes.
        self.deploy_across_nodes = deploy_across_nodes
        # Indicates whether to distribute application instances across multiple zones:
        # 
        # - `true`: The application instances are distributed across multiple zones.
        # 
        # - Other values: The application instances are not distributed across multiple zones.
        self.deploy_across_zones = deploy_across_zones
        # The startup parameters of the JAR package. This parameter is deprecated.
        self.jar_start_args = jar_start_args
        # The startup options of the JAR package. This parameter is deprecated.
        self.jar_start_options = jar_start_options
        # The startup command.
        self.k_8s_cmd = k_8s_cmd
        # The parameters of the startup command.
        self.k_8s_cmd_args = k_8s_cmd_args
        # The local storage information.
        self.k_8s_localvolume_info = k_8s_localvolume_info
        # The NAS storage information.
        self.k_8s_nas_info = k_8s_nas_info
        # The storage information.
        self.k_8s_volume_info = k_8s_volume_info
        # The information about the liveness probe of the Kubernetes container.
        self.liveness = liveness
        # The information about the post-start execution of the Kubernetes container.
        self.post_start = post_start
        # The information about the pre-stop execution of the Kubernetes container.
        self.pre_stop = pre_stop
        # The information about the readiness probe of the Kubernetes container.
        self.readiness = readiness
        # The pod runtime class. This parameter is applicable only to clusters that use sandboxed containers.
        self.runtime_class_name = runtime_class_name
        # The pod scheduling toleration configuration.
        self.tolerations = tolerations
        # The URL of the base image. This parameter is configured when a custom OpenJDK runtime is used.
        self.user_base_image_url = user_base_image_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.affinity is not None:
            result['Affinity'] = self.affinity

        if self.ahas_enabled is not None:
            result['AhasEnabled'] = self.ahas_enabled

        if self.deploy_across_nodes is not None:
            result['DeployAcrossNodes'] = self.deploy_across_nodes

        if self.deploy_across_zones is not None:
            result['DeployAcrossZones'] = self.deploy_across_zones

        if self.jar_start_args is not None:
            result['JarStartArgs'] = self.jar_start_args

        if self.jar_start_options is not None:
            result['JarStartOptions'] = self.jar_start_options

        if self.k_8s_cmd is not None:
            result['K8sCmd'] = self.k_8s_cmd

        if self.k_8s_cmd_args is not None:
            result['K8sCmdArgs'] = self.k_8s_cmd_args

        if self.k_8s_localvolume_info is not None:
            result['K8sLocalvolumeInfo'] = self.k_8s_localvolume_info

        if self.k_8s_nas_info is not None:
            result['K8sNasInfo'] = self.k_8s_nas_info

        if self.k_8s_volume_info is not None:
            result['K8sVolumeInfo'] = self.k_8s_volume_info

        if self.liveness is not None:
            result['Liveness'] = self.liveness

        if self.post_start is not None:
            result['PostStart'] = self.post_start

        if self.pre_stop is not None:
            result['PreStop'] = self.pre_stop

        if self.readiness is not None:
            result['Readiness'] = self.readiness

        if self.runtime_class_name is not None:
            result['RuntimeClassName'] = self.runtime_class_name

        if self.tolerations is not None:
            result['Tolerations'] = self.tolerations

        if self.user_base_image_url is not None:
            result['UserBaseImageUrl'] = self.user_base_image_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Affinity') is not None:
            self.affinity = m.get('Affinity')

        if m.get('AhasEnabled') is not None:
            self.ahas_enabled = m.get('AhasEnabled')

        if m.get('DeployAcrossNodes') is not None:
            self.deploy_across_nodes = m.get('DeployAcrossNodes')

        if m.get('DeployAcrossZones') is not None:
            self.deploy_across_zones = m.get('DeployAcrossZones')

        if m.get('JarStartArgs') is not None:
            self.jar_start_args = m.get('JarStartArgs')

        if m.get('JarStartOptions') is not None:
            self.jar_start_options = m.get('JarStartOptions')

        if m.get('K8sCmd') is not None:
            self.k_8s_cmd = m.get('K8sCmd')

        if m.get('K8sCmdArgs') is not None:
            self.k_8s_cmd_args = m.get('K8sCmdArgs')

        if m.get('K8sLocalvolumeInfo') is not None:
            self.k_8s_localvolume_info = m.get('K8sLocalvolumeInfo')

        if m.get('K8sNasInfo') is not None:
            self.k_8s_nas_info = m.get('K8sNasInfo')

        if m.get('K8sVolumeInfo') is not None:
            self.k_8s_volume_info = m.get('K8sVolumeInfo')

        if m.get('Liveness') is not None:
            self.liveness = m.get('Liveness')

        if m.get('PostStart') is not None:
            self.post_start = m.get('PostStart')

        if m.get('PreStop') is not None:
            self.pre_stop = m.get('PreStop')

        if m.get('Readiness') is not None:
            self.readiness = m.get('Readiness')

        if m.get('RuntimeClassName') is not None:
            self.runtime_class_name = m.get('RuntimeClassName')

        if m.get('Tolerations') is not None:
            self.tolerations = m.get('Tolerations')

        if m.get('UserBaseImageUrl') is not None:
            self.user_base_image_url = m.get('UserBaseImageUrl')

        return self

class GetK8sApplicationResponseBodyApplcationApp(DaraModel):
    def __init__(
        self,
        annotations: str = None,
        app_id: str = None,
        application_name: str = None,
        application_type: str = None,
        buildpack_id: int = None,
        cluster_id: str = None,
        cmd: str = None,
        cmd_args: main_models.GetK8sApplicationResponseBodyApplcationAppCmdArgs = None,
        cs_cluster_id: str = None,
        deploy_type: str = None,
        develop_type: str = None,
        edas_container_version: str = None,
        enable_empty_push_reject: bool = None,
        enable_lossless_rule: bool = None,
        env_list: main_models.GetK8sApplicationResponseBodyApplcationAppEnvList = None,
        feature_annotations: str = None,
        instances: int = None,
        instances_before_scaling: int = None,
        k_8s_namespace: str = None,
        labels: str = None,
        limit_cpu_m: int = None,
        limit_ephemeral_storage: str = None,
        limit_mem: int = None,
        lossless_rule_aligned: bool = None,
        lossless_rule_delay_time: int = None,
        lossless_rule_func_type: int = None,
        lossless_rule_related: bool = None,
        lossless_rule_warmup_time: int = None,
        region_id: str = None,
        request_cpu_m: int = None,
        request_ephemeral_storage: str = None,
        request_mem: int = None,
        security_context: str = None,
        slb_info: str = None,
        tomcat_version: str = None,
        workload_type: str = None,
    ):
        # The annotations of the application pod.
        self.annotations = annotations
        # The ID of the application. You can call the [ListApplication](https://help.aliyun.com/document_detail/149390.html) operation to obtain the application ID.
        self.app_id = app_id
        # The name of the application.
        self.application_name = application_name
        # The application type.
        self.application_type = application_type
        # The ID of the application build type.
        self.buildpack_id = buildpack_id
        # The cluster ID.
        self.cluster_id = cluster_id
        # The startup command.
        self.cmd = cmd
        self.cmd_args = cmd_args
        # The ID of the container cluster.
        self.cs_cluster_id = cs_cluster_id
        # The deployment type. The value is Image.
        self.deploy_type = deploy_type
        # The application type:
        # 
        # - General: a native Java application.
        # 
        # - Pandora: a Pandora application.
        # 
        # - Multilingual: a multilingual application.
        self.develop_type = develop_type
        # The version of the EDAS container.
        self.edas_container_version = edas_container_version
        # Indicates whether empty-push protection is enabled for the application.
        self.enable_empty_push_reject = enable_empty_push_reject
        # Indicates whether graceful start is enabled for the application.
        self.enable_lossless_rule = enable_lossless_rule
        self.env_list = env_list
        # The tags of advanced configurations for the current application. This parameter indicates the features that are enabled. Valid values:
        # 
        # - base.combination.edas: the EDAS integrated management solution.
        # 
        # - base.combination.arms: ARMS monitoring is enabled.
        # 
        # - base.combination.mse: MSE is enabled.
        # 
        # - base.combination.none: Only lifecycle management is enabled.
        self.feature_annotations = feature_annotations
        # The number of application instances.
        self.instances = instances
        # The number of application instances before the last scaling event.
        self.instances_before_scaling = instances_before_scaling
        # The Kubernetes namespace.
        self.k_8s_namespace = k_8s_namespace
        # The labels of the application pod.
        self.labels = labels
        # The CPU limit. Unit: millicores. 1,000 millicores are equal to one CPU core.
        self.limit_cpu_m = limit_cpu_m
        # The limit of ephemeral storage resources. Unit: GB. A value of 0 indicates that no limit is set.
        self.limit_ephemeral_storage = limit_ephemeral_storage
        # The memory limit. Unit: MiB.
        self.limit_mem = limit_mem
        # Indicates whether the application, in graceful rolling deployment mode, is configured to complete service registration before it passes the readiness probe.
        self.lossless_rule_aligned = lossless_rule_aligned
        # The duration of delayed service registration that is configured for the application. Unit: seconds.
        self.lossless_rule_delay_time = lossless_rule_delay_time
        # The service prefetch curve that is set for the application.
        self.lossless_rule_func_type = lossless_rule_func_type
        # Indicates whether the application, in graceful rolling deployment mode, is configured to complete service prefetch before it passes the readiness probe.
        self.lossless_rule_related = lossless_rule_related
        # The service prefetch duration that is set for the application. Unit: seconds.
        self.lossless_rule_warmup_time = lossless_rule_warmup_time
        # The region ID.
        self.region_id = region_id
        # The number of CPU cores that are requested. Unit: millicores. 1,000 millicores are equal to one CPU core.
        self.request_cpu_m = request_cpu_m
        # The amount of ephemeral storage resources to reserve. Unit: GB. A value of 0 indicates that no limit is set.
        self.request_ephemeral_storage = request_ephemeral_storage
        # The amount of memory that is reserved. Unit: MiB.
        self.request_mem = request_mem
        # The SecurityContext properties of the application pod container.
        self.security_context = security_context
        # The SLB configurations.
        self.slb_info = slb_info
        # The version of Apache Tomcat.
        self.tomcat_version = tomcat_version
        # The type of the workload that is used to create the application. Valid values: Deployment and StatefulSet. If you leave this parameter empty, Deployment is used.
        self.workload_type = workload_type

    def validate(self):
        if self.cmd_args:
            self.cmd_args.validate()
        if self.env_list:
            self.env_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.annotations is not None:
            result['Annotations'] = self.annotations

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.application_name is not None:
            result['ApplicationName'] = self.application_name

        if self.application_type is not None:
            result['ApplicationType'] = self.application_type

        if self.buildpack_id is not None:
            result['BuildpackId'] = self.buildpack_id

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cmd is not None:
            result['Cmd'] = self.cmd

        if self.cmd_args is not None:
            result['CmdArgs'] = self.cmd_args.to_map()

        if self.cs_cluster_id is not None:
            result['CsClusterId'] = self.cs_cluster_id

        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type

        if self.develop_type is not None:
            result['DevelopType'] = self.develop_type

        if self.edas_container_version is not None:
            result['EdasContainerVersion'] = self.edas_container_version

        if self.enable_empty_push_reject is not None:
            result['EnableEmptyPushReject'] = self.enable_empty_push_reject

        if self.enable_lossless_rule is not None:
            result['EnableLosslessRule'] = self.enable_lossless_rule

        if self.env_list is not None:
            result['EnvList'] = self.env_list.to_map()

        if self.feature_annotations is not None:
            result['FeatureAnnotations'] = self.feature_annotations

        if self.instances is not None:
            result['Instances'] = self.instances

        if self.instances_before_scaling is not None:
            result['InstancesBeforeScaling'] = self.instances_before_scaling

        if self.k_8s_namespace is not None:
            result['K8sNamespace'] = self.k_8s_namespace

        if self.labels is not None:
            result['Labels'] = self.labels

        if self.limit_cpu_m is not None:
            result['LimitCpuM'] = self.limit_cpu_m

        if self.limit_ephemeral_storage is not None:
            result['LimitEphemeralStorage'] = self.limit_ephemeral_storage

        if self.limit_mem is not None:
            result['LimitMem'] = self.limit_mem

        if self.lossless_rule_aligned is not None:
            result['LosslessRuleAligned'] = self.lossless_rule_aligned

        if self.lossless_rule_delay_time is not None:
            result['LosslessRuleDelayTime'] = self.lossless_rule_delay_time

        if self.lossless_rule_func_type is not None:
            result['LosslessRuleFuncType'] = self.lossless_rule_func_type

        if self.lossless_rule_related is not None:
            result['LosslessRuleRelated'] = self.lossless_rule_related

        if self.lossless_rule_warmup_time is not None:
            result['LosslessRuleWarmupTime'] = self.lossless_rule_warmup_time

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_cpu_m is not None:
            result['RequestCpuM'] = self.request_cpu_m

        if self.request_ephemeral_storage is not None:
            result['RequestEphemeralStorage'] = self.request_ephemeral_storage

        if self.request_mem is not None:
            result['RequestMem'] = self.request_mem

        if self.security_context is not None:
            result['SecurityContext'] = self.security_context

        if self.slb_info is not None:
            result['SlbInfo'] = self.slb_info

        if self.tomcat_version is not None:
            result['TomcatVersion'] = self.tomcat_version

        if self.workload_type is not None:
            result['WorkloadType'] = self.workload_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Annotations') is not None:
            self.annotations = m.get('Annotations')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')

        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')

        if m.get('BuildpackId') is not None:
            self.buildpack_id = m.get('BuildpackId')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Cmd') is not None:
            self.cmd = m.get('Cmd')

        if m.get('CmdArgs') is not None:
            temp_model = main_models.GetK8sApplicationResponseBodyApplcationAppCmdArgs()
            self.cmd_args = temp_model.from_map(m.get('CmdArgs'))

        if m.get('CsClusterId') is not None:
            self.cs_cluster_id = m.get('CsClusterId')

        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')

        if m.get('DevelopType') is not None:
            self.develop_type = m.get('DevelopType')

        if m.get('EdasContainerVersion') is not None:
            self.edas_container_version = m.get('EdasContainerVersion')

        if m.get('EnableEmptyPushReject') is not None:
            self.enable_empty_push_reject = m.get('EnableEmptyPushReject')

        if m.get('EnableLosslessRule') is not None:
            self.enable_lossless_rule = m.get('EnableLosslessRule')

        if m.get('EnvList') is not None:
            temp_model = main_models.GetK8sApplicationResponseBodyApplcationAppEnvList()
            self.env_list = temp_model.from_map(m.get('EnvList'))

        if m.get('FeatureAnnotations') is not None:
            self.feature_annotations = m.get('FeatureAnnotations')

        if m.get('Instances') is not None:
            self.instances = m.get('Instances')

        if m.get('InstancesBeforeScaling') is not None:
            self.instances_before_scaling = m.get('InstancesBeforeScaling')

        if m.get('K8sNamespace') is not None:
            self.k_8s_namespace = m.get('K8sNamespace')

        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        if m.get('LimitCpuM') is not None:
            self.limit_cpu_m = m.get('LimitCpuM')

        if m.get('LimitEphemeralStorage') is not None:
            self.limit_ephemeral_storage = m.get('LimitEphemeralStorage')

        if m.get('LimitMem') is not None:
            self.limit_mem = m.get('LimitMem')

        if m.get('LosslessRuleAligned') is not None:
            self.lossless_rule_aligned = m.get('LosslessRuleAligned')

        if m.get('LosslessRuleDelayTime') is not None:
            self.lossless_rule_delay_time = m.get('LosslessRuleDelayTime')

        if m.get('LosslessRuleFuncType') is not None:
            self.lossless_rule_func_type = m.get('LosslessRuleFuncType')

        if m.get('LosslessRuleRelated') is not None:
            self.lossless_rule_related = m.get('LosslessRuleRelated')

        if m.get('LosslessRuleWarmupTime') is not None:
            self.lossless_rule_warmup_time = m.get('LosslessRuleWarmupTime')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestCpuM') is not None:
            self.request_cpu_m = m.get('RequestCpuM')

        if m.get('RequestEphemeralStorage') is not None:
            self.request_ephemeral_storage = m.get('RequestEphemeralStorage')

        if m.get('RequestMem') is not None:
            self.request_mem = m.get('RequestMem')

        if m.get('SecurityContext') is not None:
            self.security_context = m.get('SecurityContext')

        if m.get('SlbInfo') is not None:
            self.slb_info = m.get('SlbInfo')

        if m.get('TomcatVersion') is not None:
            self.tomcat_version = m.get('TomcatVersion')

        if m.get('WorkloadType') is not None:
            self.workload_type = m.get('WorkloadType')

        return self

class GetK8sApplicationResponseBodyApplcationAppEnvList(DaraModel):
    def __init__(
        self,
        env: List[main_models.GetK8sApplicationResponseBodyApplcationAppEnvListEnv] = None,
    ):
        self.env = env

    def validate(self):
        if self.env:
            for v1 in self.env:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Env'] = []
        if self.env is not None:
            for k1 in self.env:
                result['Env'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.env = []
        if m.get('Env') is not None:
            for k1 in m.get('Env'):
                temp_model = main_models.GetK8sApplicationResponseBodyApplcationAppEnvListEnv()
                self.env.append(temp_model.from_map(k1))

        return self

class GetK8sApplicationResponseBodyApplcationAppEnvListEnv(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetK8sApplicationResponseBodyApplcationAppCmdArgs(DaraModel):
    def __init__(
        self,
        cmd_arg: List[str] = None,
    ):
        self.cmd_arg = cmd_arg

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cmd_arg is not None:
            result['CmdArg'] = self.cmd_arg

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CmdArg') is not None:
            self.cmd_arg = m.get('CmdArg')

        return self

