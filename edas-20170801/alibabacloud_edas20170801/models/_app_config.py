# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class AppConfig(DaraModel):
    def __init__(
        self,
        command: str = None,
        command_args: List[str] = None,
        config_mount_descs: List[main_models.AppConfigConfigMountDescs] = None,
        deploy_across_nodes: bool = None,
        deploy_across_zones: bool = None,
        empty_dirs: List[main_models.AppConfigEmptyDirs] = None,
        enable_ahas: bool = None,
        env_froms: List[main_models.AppConfigEnvFroms] = None,
        envs: List[main_models.AppConfigEnvs] = None,
        image_config: main_models.AppConfigImageConfig = None,
        is_multilingual_app: bool = None,
        java_start_up_config: str = None,
        limit_cpu: str = None,
        limit_mem: str = None,
        liveness: str = None,
        local_volumes: List[main_models.AppConfigLocalVolumes] = None,
        nas_id: str = None,
        nas_mount_descs: List[main_models.AppConfigNasMountDescs] = None,
        nas_storage_type: str = None,
        package_config: main_models.AppConfigPackageConfig = None,
        post_start: str = None,
        pre_stop: str = None,
        pvc_mount_descs: List[main_models.AppConfigPvcMountDescs] = None,
        readiness: str = None,
        replicas: int = None,
        request_cpu: str = None,
        request_mem: str = None,
        runtime_class_name: str = None,
        sls_configs: List[main_models.AppConfigSlsConfigs] = None,
        web_container_config: main_models.AppConfigWebContainerConfig = None,
    ):
        self.command = command
        self.command_args = command_args
        self.config_mount_descs = config_mount_descs
        self.deploy_across_nodes = deploy_across_nodes
        self.deploy_across_zones = deploy_across_zones
        self.empty_dirs = empty_dirs
        self.enable_ahas = enable_ahas
        self.env_froms = env_froms
        self.envs = envs
        self.image_config = image_config
        self.is_multilingual_app = is_multilingual_app
        self.java_start_up_config = java_start_up_config
        self.limit_cpu = limit_cpu
        self.limit_mem = limit_mem
        self.liveness = liveness
        self.local_volumes = local_volumes
        self.nas_id = nas_id
        self.nas_mount_descs = nas_mount_descs
        self.nas_storage_type = nas_storage_type
        self.package_config = package_config
        self.post_start = post_start
        self.pre_stop = pre_stop
        self.pvc_mount_descs = pvc_mount_descs
        self.readiness = readiness
        self.replicas = replicas
        self.request_cpu = request_cpu
        self.request_mem = request_mem
        self.runtime_class_name = runtime_class_name
        self.sls_configs = sls_configs
        self.web_container_config = web_container_config

    def validate(self):
        if self.config_mount_descs:
            for v1 in self.config_mount_descs:
                 if v1:
                    v1.validate()
        if self.empty_dirs:
            for v1 in self.empty_dirs:
                 if v1:
                    v1.validate()
        if self.env_froms:
            for v1 in self.env_froms:
                 if v1:
                    v1.validate()
        if self.envs:
            for v1 in self.envs:
                 if v1:
                    v1.validate()
        if self.image_config:
            self.image_config.validate()
        if self.local_volumes:
            for v1 in self.local_volumes:
                 if v1:
                    v1.validate()
        if self.nas_mount_descs:
            for v1 in self.nas_mount_descs:
                 if v1:
                    v1.validate()
        if self.package_config:
            self.package_config.validate()
        if self.pvc_mount_descs:
            for v1 in self.pvc_mount_descs:
                 if v1:
                    v1.validate()
        if self.sls_configs:
            for v1 in self.sls_configs:
                 if v1:
                    v1.validate()
        if self.web_container_config:
            self.web_container_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.command is not None:
            result['Command'] = self.command

        if self.command_args is not None:
            result['CommandArgs'] = self.command_args

        result['ConfigMountDescs'] = []
        if self.config_mount_descs is not None:
            for k1 in self.config_mount_descs:
                result['ConfigMountDescs'].append(k1.to_map() if k1 else None)

        if self.deploy_across_nodes is not None:
            result['DeployAcrossNodes'] = self.deploy_across_nodes

        if self.deploy_across_zones is not None:
            result['DeployAcrossZones'] = self.deploy_across_zones

        result['EmptyDirs'] = []
        if self.empty_dirs is not None:
            for k1 in self.empty_dirs:
                result['EmptyDirs'].append(k1.to_map() if k1 else None)

        if self.enable_ahas is not None:
            result['EnableAhas'] = self.enable_ahas

        result['EnvFroms'] = []
        if self.env_froms is not None:
            for k1 in self.env_froms:
                result['EnvFroms'].append(k1.to_map() if k1 else None)

        result['Envs'] = []
        if self.envs is not None:
            for k1 in self.envs:
                result['Envs'].append(k1.to_map() if k1 else None)

        if self.image_config is not None:
            result['ImageConfig'] = self.image_config.to_map()

        if self.is_multilingual_app is not None:
            result['IsMultilingualApp'] = self.is_multilingual_app

        if self.java_start_up_config is not None:
            result['JavaStartUpConfig'] = self.java_start_up_config

        if self.limit_cpu is not None:
            result['LimitCpu'] = self.limit_cpu

        if self.limit_mem is not None:
            result['LimitMem'] = self.limit_mem

        if self.liveness is not None:
            result['Liveness'] = self.liveness

        result['LocalVolumes'] = []
        if self.local_volumes is not None:
            for k1 in self.local_volumes:
                result['LocalVolumes'].append(k1.to_map() if k1 else None)

        if self.nas_id is not None:
            result['NasId'] = self.nas_id

        result['NasMountDescs'] = []
        if self.nas_mount_descs is not None:
            for k1 in self.nas_mount_descs:
                result['NasMountDescs'].append(k1.to_map() if k1 else None)

        if self.nas_storage_type is not None:
            result['NasStorageType'] = self.nas_storage_type

        if self.package_config is not None:
            result['PackageConfig'] = self.package_config.to_map()

        if self.post_start is not None:
            result['PostStart'] = self.post_start

        if self.pre_stop is not None:
            result['PreStop'] = self.pre_stop

        result['PvcMountDescs'] = []
        if self.pvc_mount_descs is not None:
            for k1 in self.pvc_mount_descs:
                result['PvcMountDescs'].append(k1.to_map() if k1 else None)

        if self.readiness is not None:
            result['Readiness'] = self.readiness

        if self.replicas is not None:
            result['Replicas'] = self.replicas

        if self.request_cpu is not None:
            result['RequestCpu'] = self.request_cpu

        if self.request_mem is not None:
            result['RequestMem'] = self.request_mem

        if self.runtime_class_name is not None:
            result['RuntimeClassName'] = self.runtime_class_name

        result['SlsConfigs'] = []
        if self.sls_configs is not None:
            for k1 in self.sls_configs:
                result['SlsConfigs'].append(k1.to_map() if k1 else None)

        if self.web_container_config is not None:
            result['WebContainerConfig'] = self.web_container_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Command') is not None:
            self.command = m.get('Command')

        if m.get('CommandArgs') is not None:
            self.command_args = m.get('CommandArgs')

        self.config_mount_descs = []
        if m.get('ConfigMountDescs') is not None:
            for k1 in m.get('ConfigMountDescs'):
                temp_model = main_models.AppConfigConfigMountDescs()
                self.config_mount_descs.append(temp_model.from_map(k1))

        if m.get('DeployAcrossNodes') is not None:
            self.deploy_across_nodes = m.get('DeployAcrossNodes')

        if m.get('DeployAcrossZones') is not None:
            self.deploy_across_zones = m.get('DeployAcrossZones')

        self.empty_dirs = []
        if m.get('EmptyDirs') is not None:
            for k1 in m.get('EmptyDirs'):
                temp_model = main_models.AppConfigEmptyDirs()
                self.empty_dirs.append(temp_model.from_map(k1))

        if m.get('EnableAhas') is not None:
            self.enable_ahas = m.get('EnableAhas')

        self.env_froms = []
        if m.get('EnvFroms') is not None:
            for k1 in m.get('EnvFroms'):
                temp_model = main_models.AppConfigEnvFroms()
                self.env_froms.append(temp_model.from_map(k1))

        self.envs = []
        if m.get('Envs') is not None:
            for k1 in m.get('Envs'):
                temp_model = main_models.AppConfigEnvs()
                self.envs.append(temp_model.from_map(k1))

        if m.get('ImageConfig') is not None:
            temp_model = main_models.AppConfigImageConfig()
            self.image_config = temp_model.from_map(m.get('ImageConfig'))

        if m.get('IsMultilingualApp') is not None:
            self.is_multilingual_app = m.get('IsMultilingualApp')

        if m.get('JavaStartUpConfig') is not None:
            self.java_start_up_config = m.get('JavaStartUpConfig')

        if m.get('LimitCpu') is not None:
            self.limit_cpu = m.get('LimitCpu')

        if m.get('LimitMem') is not None:
            self.limit_mem = m.get('LimitMem')

        if m.get('Liveness') is not None:
            self.liveness = m.get('Liveness')

        self.local_volumes = []
        if m.get('LocalVolumes') is not None:
            for k1 in m.get('LocalVolumes'):
                temp_model = main_models.AppConfigLocalVolumes()
                self.local_volumes.append(temp_model.from_map(k1))

        if m.get('NasId') is not None:
            self.nas_id = m.get('NasId')

        self.nas_mount_descs = []
        if m.get('NasMountDescs') is not None:
            for k1 in m.get('NasMountDescs'):
                temp_model = main_models.AppConfigNasMountDescs()
                self.nas_mount_descs.append(temp_model.from_map(k1))

        if m.get('NasStorageType') is not None:
            self.nas_storage_type = m.get('NasStorageType')

        if m.get('PackageConfig') is not None:
            temp_model = main_models.AppConfigPackageConfig()
            self.package_config = temp_model.from_map(m.get('PackageConfig'))

        if m.get('PostStart') is not None:
            self.post_start = m.get('PostStart')

        if m.get('PreStop') is not None:
            self.pre_stop = m.get('PreStop')

        self.pvc_mount_descs = []
        if m.get('PvcMountDescs') is not None:
            for k1 in m.get('PvcMountDescs'):
                temp_model = main_models.AppConfigPvcMountDescs()
                self.pvc_mount_descs.append(temp_model.from_map(k1))

        if m.get('Readiness') is not None:
            self.readiness = m.get('Readiness')

        if m.get('Replicas') is not None:
            self.replicas = m.get('Replicas')

        if m.get('RequestCpu') is not None:
            self.request_cpu = m.get('RequestCpu')

        if m.get('RequestMem') is not None:
            self.request_mem = m.get('RequestMem')

        if m.get('RuntimeClassName') is not None:
            self.runtime_class_name = m.get('RuntimeClassName')

        self.sls_configs = []
        if m.get('SlsConfigs') is not None:
            for k1 in m.get('SlsConfigs'):
                temp_model = main_models.AppConfigSlsConfigs()
                self.sls_configs.append(temp_model.from_map(k1))

        if m.get('WebContainerConfig') is not None:
            temp_model = main_models.AppConfigWebContainerConfig()
            self.web_container_config = temp_model.from_map(m.get('WebContainerConfig'))

        return self

class AppConfigWebContainerConfig(DaraModel):
    def __init__(
        self,
        connector_type: str = None,
        context_input_type: str = None,
        context_path: str = None,
        http_port: int = None,
        max_threads: int = None,
        server_xml: str = None,
        uri_encoding: str = None,
        use_advanced_server_xml: bool = None,
        use_body_encoding: bool = None,
        use_default_config: bool = None,
    ):
        self.connector_type = connector_type
        self.context_input_type = context_input_type
        self.context_path = context_path
        self.http_port = http_port
        self.max_threads = max_threads
        self.server_xml = server_xml
        self.uri_encoding = uri_encoding
        self.use_advanced_server_xml = use_advanced_server_xml
        self.use_body_encoding = use_body_encoding
        self.use_default_config = use_default_config

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connector_type is not None:
            result['ConnectorType'] = self.connector_type

        if self.context_input_type is not None:
            result['ContextInputType'] = self.context_input_type

        if self.context_path is not None:
            result['ContextPath'] = self.context_path

        if self.http_port is not None:
            result['HttpPort'] = self.http_port

        if self.max_threads is not None:
            result['MaxThreads'] = self.max_threads

        if self.server_xml is not None:
            result['ServerXml'] = self.server_xml

        if self.uri_encoding is not None:
            result['UriEncoding'] = self.uri_encoding

        if self.use_advanced_server_xml is not None:
            result['UseAdvancedServerXml'] = self.use_advanced_server_xml

        if self.use_body_encoding is not None:
            result['UseBodyEncoding'] = self.use_body_encoding

        if self.use_default_config is not None:
            result['UseDefaultConfig'] = self.use_default_config

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectorType') is not None:
            self.connector_type = m.get('ConnectorType')

        if m.get('ContextInputType') is not None:
            self.context_input_type = m.get('ContextInputType')

        if m.get('ContextPath') is not None:
            self.context_path = m.get('ContextPath')

        if m.get('HttpPort') is not None:
            self.http_port = m.get('HttpPort')

        if m.get('MaxThreads') is not None:
            self.max_threads = m.get('MaxThreads')

        if m.get('ServerXml') is not None:
            self.server_xml = m.get('ServerXml')

        if m.get('UriEncoding') is not None:
            self.uri_encoding = m.get('UriEncoding')

        if m.get('UseAdvancedServerXml') is not None:
            self.use_advanced_server_xml = m.get('UseAdvancedServerXml')

        if m.get('UseBodyEncoding') is not None:
            self.use_body_encoding = m.get('UseBodyEncoding')

        if m.get('UseDefaultConfig') is not None:
            self.use_default_config = m.get('UseDefaultConfig')

        return self

class AppConfigSlsConfigs(DaraModel):
    def __init__(
        self,
        log_dir: str = None,
        logstore: str = None,
        project: str = None,
        type: str = None,
    ):
        self.log_dir = log_dir
        self.logstore = logstore
        self.project = project
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.log_dir is not None:
            result['LogDir'] = self.log_dir

        if self.logstore is not None:
            result['Logstore'] = self.logstore

        if self.project is not None:
            result['Project'] = self.project

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogDir') is not None:
            self.log_dir = m.get('LogDir')

        if m.get('Logstore') is not None:
            self.logstore = m.get('Logstore')

        if m.get('Project') is not None:
            self.project = m.get('Project')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class AppConfigPvcMountDescs(DaraModel):
    def __init__(
        self,
        mount_paths: List[main_models.AppConfigPvcMountDescsMountPaths] = None,
        pvc_name: str = None,
    ):
        self.mount_paths = mount_paths
        self.pvc_name = pvc_name

    def validate(self):
        if self.mount_paths:
            for v1 in self.mount_paths:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MountPaths'] = []
        if self.mount_paths is not None:
            for k1 in self.mount_paths:
                result['MountPaths'].append(k1.to_map() if k1 else None)

        if self.pvc_name is not None:
            result['PvcName'] = self.pvc_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.mount_paths = []
        if m.get('MountPaths') is not None:
            for k1 in m.get('MountPaths'):
                temp_model = main_models.AppConfigPvcMountDescsMountPaths()
                self.mount_paths.append(temp_model.from_map(k1))

        if m.get('PvcName') is not None:
            self.pvc_name = m.get('PvcName')

        return self

class AppConfigPvcMountDescsMountPaths(DaraModel):
    def __init__(
        self,
        mount_path: str = None,
        read_only: bool = None,
        sub_path_expr: str = None,
    ):
        self.mount_path = mount_path
        self.read_only = read_only
        self.sub_path_expr = sub_path_expr

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path

        if self.read_only is not None:
            result['ReadOnly'] = self.read_only

        if self.sub_path_expr is not None:
            result['SubPathExpr'] = self.sub_path_expr

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')

        if m.get('ReadOnly') is not None:
            self.read_only = m.get('ReadOnly')

        if m.get('SubPathExpr') is not None:
            self.sub_path_expr = m.get('SubPathExpr')

        return self

class AppConfigPackageConfig(DaraModel):
    def __init__(
        self,
        edas_container_version: str = None,
        jdk: str = None,
        package_type: str = None,
        package_url: str = None,
        package_version: str = None,
        timezone: str = None,
        uri_encoding: str = None,
        use_body_encoding: bool = None,
        web_container: str = None,
    ):
        self.edas_container_version = edas_container_version
        self.jdk = jdk
        self.package_type = package_type
        self.package_url = package_url
        self.package_version = package_version
        self.timezone = timezone
        self.uri_encoding = uri_encoding
        self.use_body_encoding = use_body_encoding
        self.web_container = web_container

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.edas_container_version is not None:
            result['EdasContainerVersion'] = self.edas_container_version

        if self.jdk is not None:
            result['Jdk'] = self.jdk

        if self.package_type is not None:
            result['PackageType'] = self.package_type

        if self.package_url is not None:
            result['PackageUrl'] = self.package_url

        if self.package_version is not None:
            result['PackageVersion'] = self.package_version

        if self.timezone is not None:
            result['Timezone'] = self.timezone

        if self.uri_encoding is not None:
            result['UriEncoding'] = self.uri_encoding

        if self.use_body_encoding is not None:
            result['UseBodyEncoding'] = self.use_body_encoding

        if self.web_container is not None:
            result['WebContainer'] = self.web_container

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EdasContainerVersion') is not None:
            self.edas_container_version = m.get('EdasContainerVersion')

        if m.get('Jdk') is not None:
            self.jdk = m.get('Jdk')

        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')

        if m.get('PackageUrl') is not None:
            self.package_url = m.get('PackageUrl')

        if m.get('PackageVersion') is not None:
            self.package_version = m.get('PackageVersion')

        if m.get('Timezone') is not None:
            self.timezone = m.get('Timezone')

        if m.get('UriEncoding') is not None:
            self.uri_encoding = m.get('UriEncoding')

        if m.get('UseBodyEncoding') is not None:
            self.use_body_encoding = m.get('UseBodyEncoding')

        if m.get('WebContainer') is not None:
            self.web_container = m.get('WebContainer')

        return self

class AppConfigNasMountDescs(DaraModel):
    def __init__(
        self,
        mount_path: str = None,
        nas_path: str = None,
    ):
        self.mount_path = mount_path
        self.nas_path = nas_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path

        if self.nas_path is not None:
            result['NasPath'] = self.nas_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')

        if m.get('NasPath') is not None:
            self.nas_path = m.get('NasPath')

        return self

class AppConfigLocalVolumes(DaraModel):
    def __init__(
        self,
        mount_path: str = None,
        name: str = None,
        node_path: str = None,
        ops_auth: int = None,
        type: str = None,
    ):
        self.mount_path = mount_path
        self.name = name
        self.node_path = node_path
        self.ops_auth = ops_auth
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path

        if self.name is not None:
            result['Name'] = self.name

        if self.node_path is not None:
            result['NodePath'] = self.node_path

        if self.ops_auth is not None:
            result['OpsAuth'] = self.ops_auth

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NodePath') is not None:
            self.node_path = m.get('NodePath')

        if m.get('OpsAuth') is not None:
            self.ops_auth = m.get('OpsAuth')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class AppConfigImageConfig(DaraModel):
    def __init__(
        self,
        container_registry_id: str = None,
        cr_instance_id: str = None,
        cr_region_id: str = None,
        image_url: str = None,
    ):
        self.container_registry_id = container_registry_id
        self.cr_instance_id = cr_instance_id
        self.cr_region_id = cr_region_id
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.container_registry_id is not None:
            result['ContainerRegistryId'] = self.container_registry_id

        if self.cr_instance_id is not None:
            result['CrInstanceId'] = self.cr_instance_id

        if self.cr_region_id is not None:
            result['CrRegionId'] = self.cr_region_id

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerRegistryId') is not None:
            self.container_registry_id = m.get('ContainerRegistryId')

        if m.get('CrInstanceId') is not None:
            self.cr_instance_id = m.get('CrInstanceId')

        if m.get('CrRegionId') is not None:
            self.cr_region_id = m.get('CrRegionId')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        return self

class AppConfigEnvs(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
        value_from: str = None,
    ):
        self.name = name
        self.value = value
        self.value_from = value_from

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

        if self.value_from is not None:
            result['ValueFrom'] = self.value_from

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        if m.get('ValueFrom') is not None:
            self.value_from = m.get('ValueFrom')

        return self

class AppConfigEnvFroms(DaraModel):
    def __init__(
        self,
        config_map_ref: str = None,
        secret_ref: str = None,
    ):
        self.config_map_ref = config_map_ref
        self.secret_ref = secret_ref

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_map_ref is not None:
            result['ConfigMapRef'] = self.config_map_ref

        if self.secret_ref is not None:
            result['SecretRef'] = self.secret_ref

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigMapRef') is not None:
            self.config_map_ref = m.get('ConfigMapRef')

        if m.get('SecretRef') is not None:
            self.secret_ref = m.get('SecretRef')

        return self

class AppConfigEmptyDirs(DaraModel):
    def __init__(
        self,
        mount_path: str = None,
        name: str = None,
        read_only: bool = None,
        sub_path_expr: str = None,
    ):
        self.mount_path = mount_path
        self.name = name
        self.read_only = read_only
        self.sub_path_expr = sub_path_expr

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path

        if self.name is not None:
            result['Name'] = self.name

        if self.read_only is not None:
            result['ReadOnly'] = self.read_only

        if self.sub_path_expr is not None:
            result['SubPathExpr'] = self.sub_path_expr

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ReadOnly') is not None:
            self.read_only = m.get('ReadOnly')

        if m.get('SubPathExpr') is not None:
            self.sub_path_expr = m.get('SubPathExpr')

        return self

class AppConfigConfigMountDescs(DaraModel):
    def __init__(
        self,
        mount_items: List[main_models.AppConfigConfigMountDescsMountItems] = None,
        mount_path: str = None,
        name: str = None,
        type: str = None,
    ):
        self.mount_items = mount_items
        self.mount_path = mount_path
        self.name = name
        self.type = type

    def validate(self):
        if self.mount_items:
            for v1 in self.mount_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MountItems'] = []
        if self.mount_items is not None:
            for k1 in self.mount_items:
                result['MountItems'].append(k1.to_map() if k1 else None)

        if self.mount_path is not None:
            result['MountPath'] = self.mount_path

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.mount_items = []
        if m.get('MountItems') is not None:
            for k1 in m.get('MountItems'):
                temp_model = main_models.AppConfigConfigMountDescsMountItems()
                self.mount_items.append(temp_model.from_map(k1))

        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self



class AppConfigConfigMountDescsMountItems(DaraModel):
    def __init__(
        self,
        key: str = None,
        path: str = None,
    ):
        self.key = key
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.path is not None:
            result['Path'] = self.path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        return self

