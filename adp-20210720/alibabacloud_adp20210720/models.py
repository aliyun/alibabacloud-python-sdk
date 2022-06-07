# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class Platform(TeaModel):
    def __init__(
        self,
        architecture: str = None,
        os: str = None,
    ):
        # architecture
        self.architecture = architecture
        # os
        self.os = os

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture is not None:
            result['architecture'] = self.architecture
        if self.os is not None:
            result['os'] = self.os
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('architecture') is not None:
            self.architecture = m.get('architecture')
        if m.get('os') is not None:
            self.os = m.get('os')
        return self


class ComponentVersion(TeaModel):
    def __init__(
        self,
        app_version: str = None,
        component_name: str = None,
        component_uid: str = None,
        description: str = None,
        documents: str = None,
        images_mapping: str = None,
        namespace: str = None,
        orchestration_type: str = None,
        orchestration_values: str = None,
        package_url: str = None,
        parent_component: bool = None,
        platforms: List[Platform] = None,
        readme: str = None,
        resources: str = None,
        source: str = None,
        uid: str = None,
        version: str = None,
    ):
        # appVersion
        self.app_version = app_version
        # componentName
        self.component_name = component_name
        # componentUID
        self.component_uid = component_uid
        # description
        self.description = description
        # documents
        self.documents = documents
        # imagesMapping
        self.images_mapping = images_mapping
        # namespace
        self.namespace = namespace
        # orchestrationType
        self.orchestration_type = orchestration_type
        # orchestrationValues
        self.orchestration_values = orchestration_values
        # packageURL
        self.package_url = package_url
        # parentComponent
        self.parent_component = parent_component
        # platforms
        self.platforms = platforms
        # readme
        self.readme = readme
        # resources
        self.resources = resources
        # source
        self.source = source
        # uid
        self.uid = uid
        # version
        self.version = version

    def validate(self):
        if self.platforms:
            for k in self.platforms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version is not None:
            result['appVersion'] = self.app_version
        if self.component_name is not None:
            result['componentName'] = self.component_name
        if self.component_uid is not None:
            result['componentUID'] = self.component_uid
        if self.description is not None:
            result['description'] = self.description
        if self.documents is not None:
            result['documents'] = self.documents
        if self.images_mapping is not None:
            result['imagesMapping'] = self.images_mapping
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.orchestration_type is not None:
            result['orchestrationType'] = self.orchestration_type
        if self.orchestration_values is not None:
            result['orchestrationValues'] = self.orchestration_values
        if self.package_url is not None:
            result['packageURL'] = self.package_url
        if self.parent_component is not None:
            result['parentComponent'] = self.parent_component
        result['platforms'] = []
        if self.platforms is not None:
            for k in self.platforms:
                result['platforms'].append(k.to_map() if k else None)
        if self.readme is not None:
            result['readme'] = self.readme
        if self.resources is not None:
            result['resources'] = self.resources
        if self.source is not None:
            result['source'] = self.source
        if self.uid is not None:
            result['uid'] = self.uid
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appVersion') is not None:
            self.app_version = m.get('appVersion')
        if m.get('componentName') is not None:
            self.component_name = m.get('componentName')
        if m.get('componentUID') is not None:
            self.component_uid = m.get('componentUID')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('documents') is not None:
            self.documents = m.get('documents')
        if m.get('imagesMapping') is not None:
            self.images_mapping = m.get('imagesMapping')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('orchestrationType') is not None:
            self.orchestration_type = m.get('orchestrationType')
        if m.get('orchestrationValues') is not None:
            self.orchestration_values = m.get('orchestrationValues')
        if m.get('packageURL') is not None:
            self.package_url = m.get('packageURL')
        if m.get('parentComponent') is not None:
            self.parent_component = m.get('parentComponent')
        self.platforms = []
        if m.get('platforms') is not None:
            for k in m.get('platforms'):
                temp_model = Platform()
                self.platforms.append(temp_model.from_map(k))
        if m.get('readme') is not None:
            self.readme = m.get('readme')
        if m.get('resources') is not None:
            self.resources = m.get('resources')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class Disk(TeaModel):
    def __init__(
        self,
        capacity: int = None,
        fs_type: str = None,
        mount_point: str = None,
        name: str = None,
        remain: int = None,
        type: str = None,
    ):
        # capacity
        self.capacity = capacity
        # fsType
        self.fs_type = fs_type
        # mountPoint
        self.mount_point = mount_point
        # name
        self.name = name
        # remain
        self.remain = remain
        # type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capacity is not None:
            result['capacity'] = self.capacity
        if self.fs_type is not None:
            result['fsType'] = self.fs_type
        if self.mount_point is not None:
            result['mountPoint'] = self.mount_point
        if self.name is not None:
            result['name'] = self.name
        if self.remain is not None:
            result['remain'] = self.remain
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('capacity') is not None:
            self.capacity = m.get('capacity')
        if m.get('fsType') is not None:
            self.fs_type = m.get('fsType')
        if m.get('mountPoint') is not None:
            self.mount_point = m.get('mountPoint')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('remain') is not None:
            self.remain = m.get('remain')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ExportPort(TeaModel):
    def __init__(
        self,
        cidr_ip: str = None,
        port_range: str = None,
        protocol: str = None,
        unallowed: bool = None,
    ):
        # 目标IP 段
        self.cidr_ip = cidr_ip
        # 端口范围，格式：start/end
        self.port_range = port_range
        # 协议
        self.protocol = protocol
        # 为true，则代表deny
        self.unallowed = unallowed

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr_ip is not None:
            result['cidrIP'] = self.cidr_ip
        if self.port_range is not None:
            result['portRange'] = self.port_range
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.unallowed is not None:
            result['unallowed'] = self.unallowed
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cidrIP') is not None:
            self.cidr_ip = m.get('cidrIP')
        if m.get('portRange') is not None:
            self.port_range = m.get('portRange')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('unallowed') is not None:
            self.unallowed = m.get('unallowed')
        return self


class FoundationComponentReferenceDetail(TeaModel):
    def __init__(
        self,
        app_version: str = None,
        category: str = None,
        class_: str = None,
        component_description: str = None,
        component_name: str = None,
        component_reference_uid: str = None,
        component_uid: str = None,
        component_version_description: str = None,
        component_version_uid: str = None,
        created_at: str = None,
        documents: str = None,
        enable: bool = None,
        images_mapping: str = None,
        namespace: str = None,
        orchestration_type: str = None,
        orchestration_values: str = None,
        parent_component: bool = None,
        parent_component_version_uid: str = None,
        priority: int = None,
        provider: str = None,
        public: bool = None,
        readme: str = None,
        relation_uid: str = None,
        release_name: str = None,
        resources: str = None,
        sequence: int = None,
        singleton: bool = None,
        source: str = None,
        values: str = None,
        version: str = None,
    ):
        # appVersion
        self.app_version = app_version
        # category
        self.category = category
        # class
        self.class_ = class_
        # componentDescription
        self.component_description = component_description
        # componentName
        self.component_name = component_name
        # componentReferenceUID
        self.component_reference_uid = component_reference_uid
        # componentUID
        self.component_uid = component_uid
        # componentVersionDescription
        self.component_version_description = component_version_description
        # componentVersionUID
        self.component_version_uid = component_version_uid
        # createdAt
        self.created_at = created_at
        # documents
        self.documents = documents
        # enable
        self.enable = enable
        # imagesMapping
        self.images_mapping = images_mapping
        # namespace
        self.namespace = namespace
        # orchestrationType
        self.orchestration_type = orchestration_type
        # orchestrationValues
        self.orchestration_values = orchestration_values
        # parentComponent
        self.parent_component = parent_component
        # parentComponentVersionUID
        self.parent_component_version_uid = parent_component_version_uid
        # priority
        self.priority = priority
        # provider
        self.provider = provider
        # public
        self.public = public
        # readme
        self.readme = readme
        # relationUID
        self.relation_uid = relation_uid
        # releaseName
        self.release_name = release_name
        # resources
        self.resources = resources
        # sequence
        self.sequence = sequence
        # singleton
        self.singleton = singleton
        # source
        self.source = source
        # values
        self.values = values
        # version
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version is not None:
            result['appVersion'] = self.app_version
        if self.category is not None:
            result['category'] = self.category
        if self.class_ is not None:
            result['class'] = self.class_
        if self.component_description is not None:
            result['componentDescription'] = self.component_description
        if self.component_name is not None:
            result['componentName'] = self.component_name
        if self.component_reference_uid is not None:
            result['componentReferenceUID'] = self.component_reference_uid
        if self.component_uid is not None:
            result['componentUID'] = self.component_uid
        if self.component_version_description is not None:
            result['componentVersionDescription'] = self.component_version_description
        if self.component_version_uid is not None:
            result['componentVersionUID'] = self.component_version_uid
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.documents is not None:
            result['documents'] = self.documents
        if self.enable is not None:
            result['enable'] = self.enable
        if self.images_mapping is not None:
            result['imagesMapping'] = self.images_mapping
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.orchestration_type is not None:
            result['orchestrationType'] = self.orchestration_type
        if self.orchestration_values is not None:
            result['orchestrationValues'] = self.orchestration_values
        if self.parent_component is not None:
            result['parentComponent'] = self.parent_component
        if self.parent_component_version_uid is not None:
            result['parentComponentVersionUID'] = self.parent_component_version_uid
        if self.priority is not None:
            result['priority'] = self.priority
        if self.provider is not None:
            result['provider'] = self.provider
        if self.public is not None:
            result['public'] = self.public
        if self.readme is not None:
            result['readme'] = self.readme
        if self.relation_uid is not None:
            result['relationUID'] = self.relation_uid
        if self.release_name is not None:
            result['releaseName'] = self.release_name
        if self.resources is not None:
            result['resources'] = self.resources
        if self.sequence is not None:
            result['sequence'] = self.sequence
        if self.singleton is not None:
            result['singleton'] = self.singleton
        if self.source is not None:
            result['source'] = self.source
        if self.values is not None:
            result['values'] = self.values
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appVersion') is not None:
            self.app_version = m.get('appVersion')
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('class') is not None:
            self.class_ = m.get('class')
        if m.get('componentDescription') is not None:
            self.component_description = m.get('componentDescription')
        if m.get('componentName') is not None:
            self.component_name = m.get('componentName')
        if m.get('componentReferenceUID') is not None:
            self.component_reference_uid = m.get('componentReferenceUID')
        if m.get('componentUID') is not None:
            self.component_uid = m.get('componentUID')
        if m.get('componentVersionDescription') is not None:
            self.component_version_description = m.get('componentVersionDescription')
        if m.get('componentVersionUID') is not None:
            self.component_version_uid = m.get('componentVersionUID')
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('documents') is not None:
            self.documents = m.get('documents')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('imagesMapping') is not None:
            self.images_mapping = m.get('imagesMapping')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('orchestrationType') is not None:
            self.orchestration_type = m.get('orchestrationType')
        if m.get('orchestrationValues') is not None:
            self.orchestration_values = m.get('orchestrationValues')
        if m.get('parentComponent') is not None:
            self.parent_component = m.get('parentComponent')
        if m.get('parentComponentVersionUID') is not None:
            self.parent_component_version_uid = m.get('parentComponentVersionUID')
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('public') is not None:
            self.public = m.get('public')
        if m.get('readme') is not None:
            self.readme = m.get('readme')
        if m.get('relationUID') is not None:
            self.relation_uid = m.get('relationUID')
        if m.get('releaseName') is not None:
            self.release_name = m.get('releaseName')
        if m.get('resources') is not None:
            self.resources = m.get('resources')
        if m.get('sequence') is not None:
            self.sequence = m.get('sequence')
        if m.get('singleton') is not None:
            self.singleton = m.get('singleton')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('values') is not None:
            self.values = m.get('values')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class FoundationVersionClusterEnginesPackageToolsInstallToolPackages(TeaModel):
    def __init__(
        self,
        architecture: str = None,
        os: str = None,
        url: str = None,
    ):
        # 安装工具架构类型
        self.architecture = architecture
        # 安装工具支持的操作系统
        self.os = os
        # 地址
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture is not None:
            result['architecture'] = self.architecture
        if self.os is not None:
            result['os'] = self.os
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('architecture') is not None:
            self.architecture = m.get('architecture')
        if m.get('os') is not None:
            self.os = m.get('os')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class FoundationVersionClusterEnginesPackageTools(TeaModel):
    def __init__(
        self,
        image: str = None,
        install_tool_packages: List[FoundationVersionClusterEnginesPackageToolsInstallToolPackages] = None,
        name: str = None,
        package_format: str = None,
        type: str = None,
        version: str = None,
    ):
        # 打包工具image 地址
        self.image = image
        # 安装工具
        self.install_tool_packages = install_tool_packages
        # 打包工具名称
        self.name = name
        # 包类型
        self.package_format = package_format
        # 打包工具类型
        self.type = type
        # 打包工具版本
        self.version = version

    def validate(self):
        if self.install_tool_packages:
            for k in self.install_tool_packages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image is not None:
            result['image'] = self.image
        result['installToolPackages'] = []
        if self.install_tool_packages is not None:
            for k in self.install_tool_packages:
                result['installToolPackages'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        if self.package_format is not None:
            result['packageFormat'] = self.package_format
        if self.type is not None:
            result['type'] = self.type
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('image') is not None:
            self.image = m.get('image')
        self.install_tool_packages = []
        if m.get('installToolPackages') is not None:
            for k in m.get('installToolPackages'):
                temp_model = FoundationVersionClusterEnginesPackageToolsInstallToolPackages()
                self.install_tool_packages.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('packageFormat') is not None:
            self.package_format = m.get('packageFormat')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class FoundationVersionClusterEnginesPackages(TeaModel):
    def __init__(
        self,
        architecture: str = None,
        os: str = None,
        url: str = None,
    ):
        # 包支持的架构
        self.architecture = architecture
        # 包支持的操作系统
        self.os = os
        # 包地址
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture is not None:
            result['architecture'] = self.architecture
        if self.os is not None:
            result['os'] = self.os
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('architecture') is not None:
            self.architecture = m.get('architecture')
        if m.get('os') is not None:
            self.os = m.get('os')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class FoundationVersionClusterEngines(TeaModel):
    def __init__(
        self,
        package_tools: List[FoundationVersionClusterEnginesPackageTools] = None,
        packages: List[FoundationVersionClusterEnginesPackages] = None,
        type: str = None,
        version: str = None,
    ):
        # cluster engine 支持的打包工具定义
        self.package_tools = package_tools
        # cluster engine 的包
        self.packages = packages
        # cluster engine 列表
        self.type = type
        # cluster engine 版本
        self.version = version

    def validate(self):
        if self.package_tools:
            for k in self.package_tools:
                if k:
                    k.validate()
        if self.packages:
            for k in self.packages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['packageTools'] = []
        if self.package_tools is not None:
            for k in self.package_tools:
                result['packageTools'].append(k.to_map() if k else None)
        result['packages'] = []
        if self.packages is not None:
            for k in self.packages:
                result['packages'].append(k.to_map() if k else None)
        if self.type is not None:
            result['type'] = self.type
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.package_tools = []
        if m.get('packageTools') is not None:
            for k in m.get('packageTools'):
                temp_model = FoundationVersionClusterEnginesPackageTools()
                self.package_tools.append(temp_model.from_map(k))
        self.packages = []
        if m.get('packages') is not None:
            for k in m.get('packages'):
                temp_model = FoundationVersionClusterEnginesPackages()
                self.packages.append(temp_model.from_map(k))
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class FoundationVersionDriverComponents(TeaModel):
    def __init__(
        self,
        name: str = None,
        version: str = None,
    ):
        # 组件名称
        self.name = name
        # 组件版本
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class FoundationVersionDriver(TeaModel):
    def __init__(
        self,
        components: List[FoundationVersionDriverComponents] = None,
    ):
        # 驱动层组件
        self.components = components

    def validate(self):
        if self.components:
            for k in self.components:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['components'] = []
        if self.components is not None:
            for k in self.components:
                result['components'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.components = []
        if m.get('components') is not None:
            for k in m.get('components'):
                temp_model = FoundationVersionDriverComponents()
                self.components.append(temp_model.from_map(k))
        return self


class FoundationVersionPackageTools(TeaModel):
    def __init__(
        self,
        name: str = None,
        version: str = None,
    ):
        # 工具名
        self.name = name
        # 工具版本
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class FoundationVersion(TeaModel):
    def __init__(
        self,
        cluster_config_schema: str = None,
        cluster_engines: List[FoundationVersionClusterEngines] = None,
        default_cluster_config: str = None,
        description: str = None,
        documents: str = None,
        driver: FoundationVersionDriver = None,
        features: List[str] = None,
        labels: str = None,
        name: str = None,
        package_tools: List[FoundationVersionPackageTools] = None,
        platforms: List[Platform] = None,
        status: str = None,
        type: str = None,
        uid: str = None,
        version: str = None,
    ):
        # cluster config schema，用作针对 cluster config 进行校验以及前端可根据改数据进行展示
        self.cluster_config_schema = cluster_config_schema
        # 支持的 cluster 引擎列表
        self.cluster_engines = cluster_engines
        # 默认 cluster config，需要通过base64 进行编码
        self.default_cluster_config = default_cluster_config
        # description
        self.description = description
        # documents
        self.documents = documents
        # 驱动层描述
        self.driver = driver
        # 底座功能列表
        self.features = features
        # 标签
        self.labels = labels
        # name，目前仅能是 “ADP 底座“
        self.name = name
        # 打包工具
        self.package_tools = package_tools
        # platforms
        self.platforms = platforms
        # status，ENUM:["Testing","Published","Deprecated"] Published 后，则全平台所有用户可见，请谨慎操作
        self.status = status
        # the type of foundation version,ENUM:["trident","ack"]
        self.type = type
        # uid
        self.uid = uid
        # version
        self.version = version

    def validate(self):
        if self.cluster_engines:
            for k in self.cluster_engines:
                if k:
                    k.validate()
        if self.driver:
            self.driver.validate()
        if self.package_tools:
            for k in self.package_tools:
                if k:
                    k.validate()
        if self.platforms:
            for k in self.platforms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_config_schema is not None:
            result['clusterConfigSchema'] = self.cluster_config_schema
        result['clusterEngines'] = []
        if self.cluster_engines is not None:
            for k in self.cluster_engines:
                result['clusterEngines'].append(k.to_map() if k else None)
        if self.default_cluster_config is not None:
            result['defaultClusterConfig'] = self.default_cluster_config
        if self.description is not None:
            result['description'] = self.description
        if self.documents is not None:
            result['documents'] = self.documents
        if self.driver is not None:
            result['driver'] = self.driver.to_map()
        if self.features is not None:
            result['features'] = self.features
        if self.labels is not None:
            result['labels'] = self.labels
        if self.name is not None:
            result['name'] = self.name
        result['packageTools'] = []
        if self.package_tools is not None:
            for k in self.package_tools:
                result['packageTools'].append(k.to_map() if k else None)
        result['platforms'] = []
        if self.platforms is not None:
            for k in self.platforms:
                result['platforms'].append(k.to_map() if k else None)
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        if self.uid is not None:
            result['uid'] = self.uid
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusterConfigSchema') is not None:
            self.cluster_config_schema = m.get('clusterConfigSchema')
        self.cluster_engines = []
        if m.get('clusterEngines') is not None:
            for k in m.get('clusterEngines'):
                temp_model = FoundationVersionClusterEngines()
                self.cluster_engines.append(temp_model.from_map(k))
        if m.get('defaultClusterConfig') is not None:
            self.default_cluster_config = m.get('defaultClusterConfig')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('documents') is not None:
            self.documents = m.get('documents')
        if m.get('driver') is not None:
            temp_model = FoundationVersionDriver()
            self.driver = temp_model.from_map(m['driver'])
        if m.get('features') is not None:
            self.features = m.get('features')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('name') is not None:
            self.name = m.get('name')
        self.package_tools = []
        if m.get('packageTools') is not None:
            for k in m.get('packageTools'):
                temp_model = FoundationVersionPackageTools()
                self.package_tools.append(temp_model.from_map(k))
        self.platforms = []
        if m.get('platforms') is not None:
            for k in m.get('platforms'):
                temp_model = Platform()
                self.platforms.append(temp_model.from_map(k))
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetInstanceInfoResponseClusterTaints(TeaModel):
    def __init__(
        self,
        effect: str = None,
        key: str = None,
        value: str = None,
    ):
        # effect
        self.effect = effect
        # key
        self.key = key
        # value
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.effect is not None:
            result['effect'] = self.effect
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('effect') is not None:
            self.effect = m.get('effect')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetInstanceInfoResponseNetworkCards(TeaModel):
    def __init__(
        self,
        ip: str = None,
        name: str = None,
    ):
        # ip
        self.ip = ip
        # name
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['ip'] = self.ip
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class GetInstanceInfoResponseTaints(TeaModel):
    def __init__(
        self,
        effect: str = None,
        key: str = None,
        value: str = None,
    ):
        # effect
        self.effect = effect
        # key
        self.key = key
        # value
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.effect is not None:
            result['effect'] = self.effect
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('effect') is not None:
            self.effect = m.get('effect')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetInstanceInfoResponse(TeaModel):
    def __init__(
        self,
        annotations: Dict[str, str] = None,
        arch: str = None,
        cluster_labels: Dict[str, str] = None,
        cluster_taints: List[GetInstanceInfoResponseClusterTaints] = None,
        cpu: str = None,
        data_disk: List[Disk] = None,
        host_name: str = None,
        identifier: str = None,
        image_id: str = None,
        instance_type: str = None,
        internet_bandwidth: int = None,
        kernel: str = None,
        labels: Dict[str, str] = None,
        mac_address: str = None,
        memory: str = None,
        network_cards: List[GetInstanceInfoResponseNetworkCards] = None,
        os: str = None,
        os_version: str = None,
        private_ip: str = None,
        public_ip: str = None,
        root_password: str = None,
        system_disk: List[Disk] = None,
        system_info: str = None,
        taints: List[GetInstanceInfoResponseTaints] = None,
        uid: str = None,
    ):
        # annotations
        self.annotations = annotations
        # arch
        self.arch = arch
        # clusterLabels
        self.cluster_labels = cluster_labels
        # clusterTaints
        self.cluster_taints = cluster_taints
        # cpu
        self.cpu = cpu
        # dataDisk
        self.data_disk = data_disk
        # hostName
        self.host_name = host_name
        # identifier
        self.identifier = identifier
        # imageID
        self.image_id = image_id
        # instanceType
        self.instance_type = instance_type
        # internetBandwidth
        self.internet_bandwidth = internet_bandwidth
        # kernel
        self.kernel = kernel
        # labels
        self.labels = labels
        # macAddress
        self.mac_address = mac_address
        # memory
        self.memory = memory
        # networkCards
        self.network_cards = network_cards
        # os
        self.os = os
        # osVersion
        self.os_version = os_version
        # privateIP
        self.private_ip = private_ip
        # publicIP
        self.public_ip = public_ip
        # rootPassword
        self.root_password = root_password
        # systemDisk
        self.system_disk = system_disk
        # systemInfo
        self.system_info = system_info
        # taints
        self.taints = taints
        # uid
        self.uid = uid

    def validate(self):
        if self.cluster_taints:
            for k in self.cluster_taints:
                if k:
                    k.validate()
        if self.data_disk:
            for k in self.data_disk:
                if k:
                    k.validate()
        if self.network_cards:
            for k in self.network_cards:
                if k:
                    k.validate()
        if self.system_disk:
            for k in self.system_disk:
                if k:
                    k.validate()
        if self.taints:
            for k in self.taints:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.annotations is not None:
            result['annotations'] = self.annotations
        if self.arch is not None:
            result['arch'] = self.arch
        if self.cluster_labels is not None:
            result['clusterLabels'] = self.cluster_labels
        result['clusterTaints'] = []
        if self.cluster_taints is not None:
            for k in self.cluster_taints:
                result['clusterTaints'].append(k.to_map() if k else None)
        if self.cpu is not None:
            result['cpu'] = self.cpu
        result['dataDisk'] = []
        if self.data_disk is not None:
            for k in self.data_disk:
                result['dataDisk'].append(k.to_map() if k else None)
        if self.host_name is not None:
            result['hostName'] = self.host_name
        if self.identifier is not None:
            result['identifier'] = self.identifier
        if self.image_id is not None:
            result['imageID'] = self.image_id
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.internet_bandwidth is not None:
            result['internetBandwidth'] = self.internet_bandwidth
        if self.kernel is not None:
            result['kernel'] = self.kernel
        if self.labels is not None:
            result['labels'] = self.labels
        if self.mac_address is not None:
            result['macAddress'] = self.mac_address
        if self.memory is not None:
            result['memory'] = self.memory
        result['networkCards'] = []
        if self.network_cards is not None:
            for k in self.network_cards:
                result['networkCards'].append(k.to_map() if k else None)
        if self.os is not None:
            result['os'] = self.os
        if self.os_version is not None:
            result['osVersion'] = self.os_version
        if self.private_ip is not None:
            result['privateIP'] = self.private_ip
        if self.public_ip is not None:
            result['publicIP'] = self.public_ip
        if self.root_password is not None:
            result['rootPassword'] = self.root_password
        result['systemDisk'] = []
        if self.system_disk is not None:
            for k in self.system_disk:
                result['systemDisk'].append(k.to_map() if k else None)
        if self.system_info is not None:
            result['systemInfo'] = self.system_info
        result['taints'] = []
        if self.taints is not None:
            for k in self.taints:
                result['taints'].append(k.to_map() if k else None)
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('annotations') is not None:
            self.annotations = m.get('annotations')
        if m.get('arch') is not None:
            self.arch = m.get('arch')
        if m.get('clusterLabels') is not None:
            self.cluster_labels = m.get('clusterLabels')
        self.cluster_taints = []
        if m.get('clusterTaints') is not None:
            for k in m.get('clusterTaints'):
                temp_model = GetInstanceInfoResponseClusterTaints()
                self.cluster_taints.append(temp_model.from_map(k))
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        self.data_disk = []
        if m.get('dataDisk') is not None:
            for k in m.get('dataDisk'):
                temp_model = Disk()
                self.data_disk.append(temp_model.from_map(k))
        if m.get('hostName') is not None:
            self.host_name = m.get('hostName')
        if m.get('identifier') is not None:
            self.identifier = m.get('identifier')
        if m.get('imageID') is not None:
            self.image_id = m.get('imageID')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('internetBandwidth') is not None:
            self.internet_bandwidth = m.get('internetBandwidth')
        if m.get('kernel') is not None:
            self.kernel = m.get('kernel')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('macAddress') is not None:
            self.mac_address = m.get('macAddress')
        if m.get('memory') is not None:
            self.memory = m.get('memory')
        self.network_cards = []
        if m.get('networkCards') is not None:
            for k in m.get('networkCards'):
                temp_model = GetInstanceInfoResponseNetworkCards()
                self.network_cards.append(temp_model.from_map(k))
        if m.get('os') is not None:
            self.os = m.get('os')
        if m.get('osVersion') is not None:
            self.os_version = m.get('osVersion')
        if m.get('privateIP') is not None:
            self.private_ip = m.get('privateIP')
        if m.get('publicIP') is not None:
            self.public_ip = m.get('publicIP')
        if m.get('rootPassword') is not None:
            self.root_password = m.get('rootPassword')
        self.system_disk = []
        if m.get('systemDisk') is not None:
            for k in m.get('systemDisk'):
                temp_model = Disk()
                self.system_disk.append(temp_model.from_map(k))
        if m.get('systemInfo') is not None:
            self.system_info = m.get('systemInfo')
        self.taints = []
        if m.get('taints') is not None:
            for k in m.get('taints'):
                temp_model = GetInstanceInfoResponseTaints()
                self.taints.append(temp_model.from_map(k))
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class GetPayAsYouGoPriceDataModuleList(TeaModel):
    def __init__(
        self,
        config: str = None,
        module_code: str = None,
        price_type: str = None,
    ):
        # Config
        self.config = config
        # ModuleCode
        self.module_code = module_code
        # PriceType
        self.price_type = price_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.module_code is not None:
            result['ModuleCode'] = self.module_code
        if self.price_type is not None:
            result['PriceType'] = self.price_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('ModuleCode') is not None:
            self.module_code = m.get('ModuleCode')
        if m.get('PriceType') is not None:
            self.price_type = m.get('PriceType')
        return self


class GetPayAsYouGoPriceData(TeaModel):
    def __init__(
        self,
        module_list: List[GetPayAsYouGoPriceDataModuleList] = None,
        owner_id: str = None,
        product_code: str = None,
        product_type: str = None,
        region: str = None,
        subscription_type: str = None,
    ):
        # ModuleList
        self.module_list = module_list
        # OwnerId
        self.owner_id = owner_id
        # ProductCode
        self.product_code = product_code
        # ProductType
        self.product_type = product_type
        # Region
        self.region = region
        # SubscriptionType
        self.subscription_type = subscription_type

    def validate(self):
        if self.module_list:
            for k in self.module_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ModuleList'] = []
        if self.module_list is not None:
            for k in self.module_list:
                result['ModuleList'].append(k.to_map() if k else None)
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.region is not None:
            result['Region'] = self.region
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.module_list = []
        if m.get('ModuleList') is not None:
            for k in m.get('ModuleList'):
                temp_model = GetPayAsYouGoPriceDataModuleList()
                self.module_list.append(temp_model.from_map(k))
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        return self


class InstanceInfoClusterTaints(TeaModel):
    def __init__(
        self,
        effect: str = None,
        key: str = None,
        value: str = None,
    ):
        # effect
        self.effect = effect
        # key
        self.key = key
        # value
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.effect is not None:
            result['effect'] = self.effect
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('effect') is not None:
            self.effect = m.get('effect')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class InstanceInfoNetworkCards(TeaModel):
    def __init__(
        self,
        ip: str = None,
        name: str = None,
    ):
        # ip
        self.ip = ip
        # name
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['ip'] = self.ip
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class InstanceInfoTaints(TeaModel):
    def __init__(
        self,
        effect: str = None,
        key: str = None,
        value: str = None,
    ):
        # effect
        self.effect = effect
        # key
        self.key = key
        # value
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.effect is not None:
            result['effect'] = self.effect
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('effect') is not None:
            self.effect = m.get('effect')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class InstanceInfo(TeaModel):
    def __init__(
        self,
        annotations: Dict[str, str] = None,
        arch: str = None,
        cluster_labels: Dict[str, str] = None,
        cluster_taints: List[InstanceInfoClusterTaints] = None,
        cluster_uid: str = None,
        cpu: str = None,
        created_at: str = None,
        data_disk: List[Disk] = None,
        disk_config_annotations: Dict[str, str] = None,
        host_name: str = None,
        identifier: str = None,
        image_id: str = None,
        instance_type: str = None,
        internet_bandwidth: int = None,
        kernel: str = None,
        labels: Dict[str, str] = None,
        mac_address: str = None,
        memory: str = None,
        network_cards: List[InstanceInfoNetworkCards] = None,
        os: str = None,
        os_version: str = None,
        private_ip: str = None,
        public_ip: str = None,
        root_password: str = None,
        system_disk: List[Disk] = None,
        system_info: str = None,
        taints: List[InstanceInfoTaints] = None,
        uid: str = None,
    ):
        # annotations
        self.annotations = annotations
        # arch
        self.arch = arch
        # clusterLabels
        self.cluster_labels = cluster_labels
        # clusterTaints
        self.cluster_taints = cluster_taints
        # clusterUID
        self.cluster_uid = cluster_uid
        # cpu
        self.cpu = cpu
        # createdAt
        self.created_at = created_at
        # dataDisk
        self.data_disk = data_disk
        # diskConfigAnnotations
        self.disk_config_annotations = disk_config_annotations
        # hostName
        self.host_name = host_name
        # identifier
        self.identifier = identifier
        # imageID
        self.image_id = image_id
        # instanceType
        self.instance_type = instance_type
        # internetBandwidth
        self.internet_bandwidth = internet_bandwidth
        # kernel
        self.kernel = kernel
        # labels
        self.labels = labels
        # macAddress
        self.mac_address = mac_address
        # memory
        self.memory = memory
        # networkCards
        self.network_cards = network_cards
        # os
        self.os = os
        # osVersion
        self.os_version = os_version
        # privateIP
        self.private_ip = private_ip
        # publicIP
        self.public_ip = public_ip
        # rootPassword
        self.root_password = root_password
        # systemDisk
        self.system_disk = system_disk
        # systemInfo
        self.system_info = system_info
        # taints
        self.taints = taints
        # uid
        self.uid = uid

    def validate(self):
        if self.cluster_taints:
            for k in self.cluster_taints:
                if k:
                    k.validate()
        if self.data_disk:
            for k in self.data_disk:
                if k:
                    k.validate()
        if self.network_cards:
            for k in self.network_cards:
                if k:
                    k.validate()
        if self.system_disk:
            for k in self.system_disk:
                if k:
                    k.validate()
        if self.taints:
            for k in self.taints:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.annotations is not None:
            result['annotations'] = self.annotations
        if self.arch is not None:
            result['arch'] = self.arch
        if self.cluster_labels is not None:
            result['clusterLabels'] = self.cluster_labels
        result['clusterTaints'] = []
        if self.cluster_taints is not None:
            for k in self.cluster_taints:
                result['clusterTaints'].append(k.to_map() if k else None)
        if self.cluster_uid is not None:
            result['clusterUID'] = self.cluster_uid
        if self.cpu is not None:
            result['cpu'] = self.cpu
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        result['dataDisk'] = []
        if self.data_disk is not None:
            for k in self.data_disk:
                result['dataDisk'].append(k.to_map() if k else None)
        if self.disk_config_annotations is not None:
            result['diskConfigAnnotations'] = self.disk_config_annotations
        if self.host_name is not None:
            result['hostName'] = self.host_name
        if self.identifier is not None:
            result['identifier'] = self.identifier
        if self.image_id is not None:
            result['imageID'] = self.image_id
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.internet_bandwidth is not None:
            result['internetBandwidth'] = self.internet_bandwidth
        if self.kernel is not None:
            result['kernel'] = self.kernel
        if self.labels is not None:
            result['labels'] = self.labels
        if self.mac_address is not None:
            result['macAddress'] = self.mac_address
        if self.memory is not None:
            result['memory'] = self.memory
        result['networkCards'] = []
        if self.network_cards is not None:
            for k in self.network_cards:
                result['networkCards'].append(k.to_map() if k else None)
        if self.os is not None:
            result['os'] = self.os
        if self.os_version is not None:
            result['osVersion'] = self.os_version
        if self.private_ip is not None:
            result['privateIP'] = self.private_ip
        if self.public_ip is not None:
            result['publicIP'] = self.public_ip
        if self.root_password is not None:
            result['rootPassword'] = self.root_password
        result['systemDisk'] = []
        if self.system_disk is not None:
            for k in self.system_disk:
                result['systemDisk'].append(k.to_map() if k else None)
        if self.system_info is not None:
            result['systemInfo'] = self.system_info
        result['taints'] = []
        if self.taints is not None:
            for k in self.taints:
                result['taints'].append(k.to_map() if k else None)
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('annotations') is not None:
            self.annotations = m.get('annotations')
        if m.get('arch') is not None:
            self.arch = m.get('arch')
        if m.get('clusterLabels') is not None:
            self.cluster_labels = m.get('clusterLabels')
        self.cluster_taints = []
        if m.get('clusterTaints') is not None:
            for k in m.get('clusterTaints'):
                temp_model = InstanceInfoClusterTaints()
                self.cluster_taints.append(temp_model.from_map(k))
        if m.get('clusterUID') is not None:
            self.cluster_uid = m.get('clusterUID')
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        self.data_disk = []
        if m.get('dataDisk') is not None:
            for k in m.get('dataDisk'):
                temp_model = Disk()
                self.data_disk.append(temp_model.from_map(k))
        if m.get('diskConfigAnnotations') is not None:
            self.disk_config_annotations = m.get('diskConfigAnnotations')
        if m.get('hostName') is not None:
            self.host_name = m.get('hostName')
        if m.get('identifier') is not None:
            self.identifier = m.get('identifier')
        if m.get('imageID') is not None:
            self.image_id = m.get('imageID')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('internetBandwidth') is not None:
            self.internet_bandwidth = m.get('internetBandwidth')
        if m.get('kernel') is not None:
            self.kernel = m.get('kernel')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('macAddress') is not None:
            self.mac_address = m.get('macAddress')
        if m.get('memory') is not None:
            self.memory = m.get('memory')
        self.network_cards = []
        if m.get('networkCards') is not None:
            for k in m.get('networkCards'):
                temp_model = InstanceInfoNetworkCards()
                self.network_cards.append(temp_model.from_map(k))
        if m.get('os') is not None:
            self.os = m.get('os')
        if m.get('osVersion') is not None:
            self.os_version = m.get('osVersion')
        if m.get('privateIP') is not None:
            self.private_ip = m.get('privateIP')
        if m.get('publicIP') is not None:
            self.public_ip = m.get('publicIP')
        if m.get('rootPassword') is not None:
            self.root_password = m.get('rootPassword')
        self.system_disk = []
        if m.get('systemDisk') is not None:
            for k in m.get('systemDisk'):
                temp_model = Disk()
                self.system_disk.append(temp_model.from_map(k))
        if m.get('systemInfo') is not None:
            self.system_info = m.get('systemInfo')
        self.taints = []
        if m.get('taints') is not None:
            for k in m.get('taints'):
                temp_model = InstanceInfoTaints()
                self.taints.append(temp_model.from_map(k))
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class ProductComponentRelationDetail(TeaModel):
    def __init__(
        self,
        app_version: str = None,
        category: str = None,
        class_: str = None,
        component_name: str = None,
        component_orchestration_values: str = None,
        component_uid: str = None,
        component_version_uid: str = None,
        created_at: str = None,
        description: str = None,
        documents: str = None,
        enable: bool = None,
        images_mapping: str = None,
        namespace: str = None,
        orchestration_type: str = None,
        parent_component: bool = None,
        parent_component_version_relation_uid: str = None,
        parent_component_version_uid: str = None,
        priority: int = None,
        product_version_uid: str = None,
        provider: str = None,
        public: bool = None,
        readme: str = None,
        relation_uid: str = None,
        release_name: str = None,
        resources: str = None,
        sequence: int = None,
        singleton: bool = None,
        source: str = None,
        version: str = None,
    ):
        # appVersion
        self.app_version = app_version
        # category
        self.category = category
        # class
        self.class_ = class_
        # componentName
        self.component_name = component_name
        # componentOrchestrationValues
        self.component_orchestration_values = component_orchestration_values
        # componentUID
        self.component_uid = component_uid
        # componentVersionUID
        self.component_version_uid = component_version_uid
        # createdAt
        self.created_at = created_at
        # description
        self.description = description
        # documents
        self.documents = documents
        # enable
        self.enable = enable
        # imagesMapping
        self.images_mapping = images_mapping
        # namespace
        self.namespace = namespace
        # orchestrationType
        self.orchestration_type = orchestration_type
        # parentComponent
        self.parent_component = parent_component
        # parentComponentVersionRelationUID
        self.parent_component_version_relation_uid = parent_component_version_relation_uid
        # parentComponentVersionUID
        self.parent_component_version_uid = parent_component_version_uid
        # priority
        self.priority = priority
        # productVersionUID
        self.product_version_uid = product_version_uid
        # provider
        self.provider = provider
        # public
        self.public = public
        # readme
        self.readme = readme
        # relationUID
        self.relation_uid = relation_uid
        # releaseName
        self.release_name = release_name
        # resources
        self.resources = resources
        # sequence
        self.sequence = sequence
        # singleton
        self.singleton = singleton
        # source
        self.source = source
        # version
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version is not None:
            result['appVersion'] = self.app_version
        if self.category is not None:
            result['category'] = self.category
        if self.class_ is not None:
            result['class'] = self.class_
        if self.component_name is not None:
            result['componentName'] = self.component_name
        if self.component_orchestration_values is not None:
            result['componentOrchestrationValues'] = self.component_orchestration_values
        if self.component_uid is not None:
            result['componentUID'] = self.component_uid
        if self.component_version_uid is not None:
            result['componentVersionUID'] = self.component_version_uid
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.documents is not None:
            result['documents'] = self.documents
        if self.enable is not None:
            result['enable'] = self.enable
        if self.images_mapping is not None:
            result['imagesMapping'] = self.images_mapping
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.orchestration_type is not None:
            result['orchestrationType'] = self.orchestration_type
        if self.parent_component is not None:
            result['parentComponent'] = self.parent_component
        if self.parent_component_version_relation_uid is not None:
            result['parentComponentVersionRelationUID'] = self.parent_component_version_relation_uid
        if self.parent_component_version_uid is not None:
            result['parentComponentVersionUID'] = self.parent_component_version_uid
        if self.priority is not None:
            result['priority'] = self.priority
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        if self.provider is not None:
            result['provider'] = self.provider
        if self.public is not None:
            result['public'] = self.public
        if self.readme is not None:
            result['readme'] = self.readme
        if self.relation_uid is not None:
            result['relationUID'] = self.relation_uid
        if self.release_name is not None:
            result['releaseName'] = self.release_name
        if self.resources is not None:
            result['resources'] = self.resources
        if self.sequence is not None:
            result['sequence'] = self.sequence
        if self.singleton is not None:
            result['singleton'] = self.singleton
        if self.source is not None:
            result['source'] = self.source
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appVersion') is not None:
            self.app_version = m.get('appVersion')
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('class') is not None:
            self.class_ = m.get('class')
        if m.get('componentName') is not None:
            self.component_name = m.get('componentName')
        if m.get('componentOrchestrationValues') is not None:
            self.component_orchestration_values = m.get('componentOrchestrationValues')
        if m.get('componentUID') is not None:
            self.component_uid = m.get('componentUID')
        if m.get('componentVersionUID') is not None:
            self.component_version_uid = m.get('componentVersionUID')
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('documents') is not None:
            self.documents = m.get('documents')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('imagesMapping') is not None:
            self.images_mapping = m.get('imagesMapping')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('orchestrationType') is not None:
            self.orchestration_type = m.get('orchestrationType')
        if m.get('parentComponent') is not None:
            self.parent_component = m.get('parentComponent')
        if m.get('parentComponentVersionRelationUID') is not None:
            self.parent_component_version_relation_uid = m.get('parentComponentVersionRelationUID')
        if m.get('parentComponentVersionUID') is not None:
            self.parent_component_version_uid = m.get('parentComponentVersionUID')
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('productVersionUID') is not None:
            self.product_version_uid = m.get('productVersionUID')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('public') is not None:
            self.public = m.get('public')
        if m.get('readme') is not None:
            self.readme = m.get('readme')
        if m.get('relationUID') is not None:
            self.relation_uid = m.get('relationUID')
        if m.get('releaseName') is not None:
            self.release_name = m.get('releaseName')
        if m.get('resources') is not None:
            self.resources = m.get('resources')
        if m.get('sequence') is not None:
            self.sequence = m.get('sequence')
        if m.get('singleton') is not None:
            self.singleton = m.get('singleton')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ResourceCpu(TeaModel):
    def __init__(
        self,
        required: int = None,
    ):
        # 需要的数量
        self.required = required

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.required is not None:
            result['required'] = self.required
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('required') is not None:
            self.required = m.get('required')
        return self


class ResourceImage(TeaModel):
    def __init__(
        self,
        id: str = None,
        name_regex: str = None,
    ):
        # image id
        self.id = id
        # 名称正则
        self.name_regex = name_regex

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.name_regex is not None:
            result['nameRegex'] = self.name_regex
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('nameRegex') is not None:
            self.name_regex = m.get('nameRegex')
        return self


class ResourceMemory(TeaModel):
    def __init__(
        self,
        required: int = None,
    ):
        # 需要的内存，单位 G
        self.required = required

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.required is not None:
            result['required'] = self.required
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('required') is not None:
            self.required = m.get('required')
        return self


class ResourcePublicIP(TeaModel):
    def __init__(
        self,
        bandwidth: int = None,
        required: int = None,
    ):
        # 带宽
        self.bandwidth = bandwidth
        # 需要的数量
        self.required = required

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['bandwidth'] = self.bandwidth
        if self.required is not None:
            result['required'] = self.required
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bandwidth') is not None:
            self.bandwidth = m.get('bandwidth')
        if m.get('required') is not None:
            self.required = m.get('required')
        return self


class ResourceStorage(TeaModel):
    def __init__(
        self,
        required: int = None,
    ):
        # 磁盘大小
        self.required = required

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.required is not None:
            result['required'] = self.required
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('required') is not None:
            self.required = m.get('required')
        return self


class Resource(TeaModel):
    def __init__(
        self,
        cpu: ResourceCpu = None,
        hostname: str = None,
        identifier: str = None,
        image: ResourceImage = None,
        instance_type: str = None,
        memory: ResourceMemory = None,
        ports: List[ExportPort] = None,
        public_ip: ResourcePublicIP = None,
        replica: int = None,
        storage: List[ResourceStorage] = None,
    ):
        # cpu
        self.cpu = cpu
        # 实例hostname
        self.hostname = hostname
        # 资源分组名
        self.identifier = identifier
        # 镜像
        self.image = image
        # 实例类型
        self.instance_type = instance_type
        # memory
        self.memory = memory
        # 需要开放的端口
        self.ports = ports
        # 公网IP 需求
        self.public_ip = public_ip
        # 数量
        self.replica = replica
        # 存储需求
        self.storage = storage

    def validate(self):
        if self.cpu:
            self.cpu.validate()
        if self.image:
            self.image.validate()
        if self.memory:
            self.memory.validate()
        if self.ports:
            for k in self.ports:
                if k:
                    k.validate()
        if self.public_ip:
            self.public_ip.validate()
        if self.storage:
            for k in self.storage:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['cpu'] = self.cpu.to_map()
        if self.hostname is not None:
            result['hostname'] = self.hostname
        if self.identifier is not None:
            result['identifier'] = self.identifier
        if self.image is not None:
            result['image'] = self.image.to_map()
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.memory is not None:
            result['memory'] = self.memory.to_map()
        result['ports'] = []
        if self.ports is not None:
            for k in self.ports:
                result['ports'].append(k.to_map() if k else None)
        if self.public_ip is not None:
            result['publicIP'] = self.public_ip.to_map()
        if self.replica is not None:
            result['replica'] = self.replica
        result['storage'] = []
        if self.storage is not None:
            for k in self.storage:
                result['storage'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cpu') is not None:
            temp_model = ResourceCpu()
            self.cpu = temp_model.from_map(m['cpu'])
        if m.get('hostname') is not None:
            self.hostname = m.get('hostname')
        if m.get('identifier') is not None:
            self.identifier = m.get('identifier')
        if m.get('image') is not None:
            temp_model = ResourceImage()
            self.image = temp_model.from_map(m['image'])
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('memory') is not None:
            temp_model = ResourceMemory()
            self.memory = temp_model.from_map(m['memory'])
        self.ports = []
        if m.get('ports') is not None:
            for k in m.get('ports'):
                temp_model = ExportPort()
                self.ports.append(temp_model.from_map(k))
        if m.get('publicIP') is not None:
            temp_model = ResourcePublicIP()
            self.public_ip = temp_model.from_map(m['publicIP'])
        if m.get('replica') is not None:
            self.replica = m.get('replica')
        self.storage = []
        if m.get('storage') is not None:
            for k in m.get('storage'):
                temp_model = ResourceStorage()
                self.storage.append(temp_model.from_map(k))
        return self


class AddEnvironmentNodesRequestDataDisk(TeaModel):
    def __init__(
        self,
        name: str = None,
        required: int = None,
    ):
        self.name = name
        self.required = required

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.required is not None:
            result['required'] = self.required
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('required') is not None:
            self.required = m.get('required')
        return self


class AddEnvironmentNodesRequestSystemDisk(TeaModel):
    def __init__(
        self,
        name: str = None,
        required: int = None,
    ):
        self.name = name
        self.required = required

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.required is not None:
            result['required'] = self.required
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('required') is not None:
            self.required = m.get('required')
        return self


class AddEnvironmentNodesRequestTaints(TeaModel):
    def __init__(
        self,
        effect: str = None,
        key: str = None,
        value: str = None,
    ):
        self.effect = effect
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.effect is not None:
            result['effect'] = self.effect
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('effect') is not None:
            self.effect = m.get('effect')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class AddEnvironmentNodesRequest(TeaModel):
    def __init__(
        self,
        application_disk: str = None,
        cpu: int = None,
        data_disk: List[AddEnvironmentNodesRequestDataDisk] = None,
        etcd_disk: str = None,
        host_name: str = None,
        labels: Dict[str, Any] = None,
        master_private_ips: List[str] = None,
        memory: int = None,
        os: str = None,
        root_password: str = None,
        system_disk: List[AddEnvironmentNodesRequestSystemDisk] = None,
        taints: List[AddEnvironmentNodesRequestTaints] = None,
        trident_system_disk: str = None,
        trident_system_size_disk: int = None,
        worker_private_ips: List[str] = None,
    ):
        # 保留业务分区
        self.application_disk = application_disk
        self.cpu = cpu
        self.data_disk = data_disk
        # etcd数据盘
        self.etcd_disk = etcd_disk
        self.host_name = host_name
        self.labels = labels
        # master privateId
        self.master_private_ips = master_private_ips
        self.memory = memory
        self.os = os
        self.root_password = root_password
        self.system_disk = system_disk
        self.taints = taints
        # k8s管控数据盘
        self.trident_system_disk = trident_system_disk
        # k8s管控数据盘大小
        self.trident_system_size_disk = trident_system_size_disk
        # work privateIp
        self.worker_private_ips = worker_private_ips

    def validate(self):
        if self.data_disk:
            for k in self.data_disk:
                if k:
                    k.validate()
        if self.system_disk:
            for k in self.system_disk:
                if k:
                    k.validate()
        if self.taints:
            for k in self.taints:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_disk is not None:
            result['applicationDisk'] = self.application_disk
        if self.cpu is not None:
            result['cpu'] = self.cpu
        result['dataDisk'] = []
        if self.data_disk is not None:
            for k in self.data_disk:
                result['dataDisk'].append(k.to_map() if k else None)
        if self.etcd_disk is not None:
            result['etcdDisk'] = self.etcd_disk
        if self.host_name is not None:
            result['hostName'] = self.host_name
        if self.labels is not None:
            result['labels'] = self.labels
        if self.master_private_ips is not None:
            result['masterPrivateIPs'] = self.master_private_ips
        if self.memory is not None:
            result['memory'] = self.memory
        if self.os is not None:
            result['os'] = self.os
        if self.root_password is not None:
            result['rootPassword'] = self.root_password
        result['systemDisk'] = []
        if self.system_disk is not None:
            for k in self.system_disk:
                result['systemDisk'].append(k.to_map() if k else None)
        result['taints'] = []
        if self.taints is not None:
            for k in self.taints:
                result['taints'].append(k.to_map() if k else None)
        if self.trident_system_disk is not None:
            result['tridentSystemDisk'] = self.trident_system_disk
        if self.trident_system_size_disk is not None:
            result['tridentSystemSizeDisk'] = self.trident_system_size_disk
        if self.worker_private_ips is not None:
            result['workerPrivateIPs'] = self.worker_private_ips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applicationDisk') is not None:
            self.application_disk = m.get('applicationDisk')
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        self.data_disk = []
        if m.get('dataDisk') is not None:
            for k in m.get('dataDisk'):
                temp_model = AddEnvironmentNodesRequestDataDisk()
                self.data_disk.append(temp_model.from_map(k))
        if m.get('etcdDisk') is not None:
            self.etcd_disk = m.get('etcdDisk')
        if m.get('hostName') is not None:
            self.host_name = m.get('hostName')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('masterPrivateIPs') is not None:
            self.master_private_ips = m.get('masterPrivateIPs')
        if m.get('memory') is not None:
            self.memory = m.get('memory')
        if m.get('os') is not None:
            self.os = m.get('os')
        if m.get('rootPassword') is not None:
            self.root_password = m.get('rootPassword')
        self.system_disk = []
        if m.get('systemDisk') is not None:
            for k in m.get('systemDisk'):
                temp_model = AddEnvironmentNodesRequestSystemDisk()
                self.system_disk.append(temp_model.from_map(k))
        self.taints = []
        if m.get('taints') is not None:
            for k in m.get('taints'):
                temp_model = AddEnvironmentNodesRequestTaints()
                self.taints.append(temp_model.from_map(k))
        if m.get('tridentSystemDisk') is not None:
            self.trident_system_disk = m.get('tridentSystemDisk')
        if m.get('tridentSystemSizeDisk') is not None:
            self.trident_system_size_disk = m.get('tridentSystemSizeDisk')
        if m.get('workerPrivateIPs') is not None:
            self.worker_private_ips = m.get('workerPrivateIPs')
        return self


class AddEnvironmentNodesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
    ):
        self.code = code
        self.msg = msg

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class AddEnvironmentNodesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddEnvironmentNodesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddEnvironmentNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddEnvironmentProductVersionsRequest(TeaModel):
    def __init__(
        self,
        product_version_uidlist: List[str] = None,
    ):
        self.product_version_uidlist = product_version_uidlist

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_version_uidlist is not None:
            result['productVersionUIDList'] = self.product_version_uidlist
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('productVersionUIDList') is not None:
            self.product_version_uidlist = m.get('productVersionUIDList')
        return self


class AddEnvironmentProductVersionsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
    ):
        self.code = code
        self.msg = msg

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class AddEnvironmentProductVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddEnvironmentProductVersionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddEnvironmentProductVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddProductComponentVersionRequest(TeaModel):
    def __init__(
        self,
        release_name: str = None,
    ):
        self.release_name = release_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.release_name is not None:
            result['releaseName'] = self.release_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('releaseName') is not None:
            self.release_name = m.get('releaseName')
        return self


class AddProductComponentVersionResponseBodyData(TeaModel):
    def __init__(
        self,
        uid: str = None,
    ):
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class AddProductComponentVersionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: AddProductComponentVersionResponseBodyData = None,
        msg: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = AddProductComponentVersionResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class AddProductComponentVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddProductComponentVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddProductComponentVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddProductVersionConfigRequest(TeaModel):
    def __init__(
        self,
        component_version_uid: str = None,
        description: str = None,
        name: str = None,
        parent_component_version_uid: str = None,
        value: str = None,
        value_type: str = None,
    ):
        # 组件uid
        self.component_version_uid = component_version_uid
        # 配置说明
        self.description = description
        # 配置信息key
        self.name = name
        # 父组件uid
        self.parent_component_version_uid = parent_component_version_uid
        # 配置信息value
        self.value = value
        self.value_type = value_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_version_uid is not None:
            result['componentVersionUID'] = self.component_version_uid
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.parent_component_version_uid is not None:
            result['parentComponentVersionUID'] = self.parent_component_version_uid
        if self.value is not None:
            result['value'] = self.value
        if self.value_type is not None:
            result['valueType'] = self.value_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('componentVersionUID') is not None:
            self.component_version_uid = m.get('componentVersionUID')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parentComponentVersionUID') is not None:
            self.parent_component_version_uid = m.get('parentComponentVersionUID')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('valueType') is not None:
            self.value_type = m.get('valueType')
        return self


class AddProductVersionConfigResponseBodyData(TeaModel):
    def __init__(
        self,
        uid: str = None,
    ):
        # product version config uid
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class AddProductVersionConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: AddProductVersionConfigResponseBodyData = None,
        msg: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = AddProductVersionConfigResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class AddProductVersionConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddProductVersionConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddProductVersionConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddResourceSnapshotRequest(TeaModel):
    def __init__(
        self,
        cluster_uid: str = None,
        product_version_uid: str = None,
    ):
        self.cluster_uid = cluster_uid
        self.product_version_uid = product_version_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_uid is not None:
            result['clusterUID'] = self.cluster_uid
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusterUID') is not None:
            self.cluster_uid = m.get('clusterUID')
        if m.get('productVersionUID') is not None:
            self.product_version_uid = m.get('productVersionUID')
        return self


class AddResourceSnapshotResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
    ):
        self.code = code
        self.msg = msg

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class AddResourceSnapshotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddResourceSnapshotResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddResourceSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchAddEnvironmentNodesRequest(TeaModel):
    def __init__(
        self,
        instance_list: List[InstanceInfo] = None,
        overwrite: bool = None,
    ):
        self.instance_list = instance_list
        # 是否覆盖
        self.overwrite = overwrite

    def validate(self):
        if self.instance_list:
            for k in self.instance_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['instanceList'] = []
        if self.instance_list is not None:
            for k in self.instance_list:
                result['instanceList'].append(k.to_map() if k else None)
        if self.overwrite is not None:
            result['overwrite'] = self.overwrite
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_list = []
        if m.get('instanceList') is not None:
            for k in m.get('instanceList'):
                temp_model = InstanceInfo()
                self.instance_list.append(temp_model.from_map(k))
        if m.get('overwrite') is not None:
            self.overwrite = m.get('overwrite')
        return self


class BatchAddEnvironmentNodesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
    ):
        self.code = code
        self.msg = msg

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class BatchAddEnvironmentNodesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchAddEnvironmentNodesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BatchAddEnvironmentNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchAddProductVersionConfigRequestProductVersionConfigList(TeaModel):
    def __init__(
        self,
        component_version_uid: str = None,
        description: str = None,
        name: str = None,
        parent_component_version_uid: str = None,
        value: str = None,
        value_type: str = None,
    ):
        # 组件uid
        self.component_version_uid = component_version_uid
        # 配置说明
        self.description = description
        # 配置信息key
        self.name = name
        # 父组件uid
        self.parent_component_version_uid = parent_component_version_uid
        # 配置信息value
        self.value = value
        self.value_type = value_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_version_uid is not None:
            result['componentVersionUID'] = self.component_version_uid
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.parent_component_version_uid is not None:
            result['parentComponentVersionUID'] = self.parent_component_version_uid
        if self.value is not None:
            result['value'] = self.value
        if self.value_type is not None:
            result['valueType'] = self.value_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('componentVersionUID') is not None:
            self.component_version_uid = m.get('componentVersionUID')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parentComponentVersionUID') is not None:
            self.parent_component_version_uid = m.get('parentComponentVersionUID')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('valueType') is not None:
            self.value_type = m.get('valueType')
        return self


class BatchAddProductVersionConfigRequest(TeaModel):
    def __init__(
        self,
        product_version_config_list: List[BatchAddProductVersionConfigRequestProductVersionConfigList] = None,
    ):
        self.product_version_config_list = product_version_config_list

    def validate(self):
        if self.product_version_config_list:
            for k in self.product_version_config_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['productVersionConfigList'] = []
        if self.product_version_config_list is not None:
            for k in self.product_version_config_list:
                result['productVersionConfigList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.product_version_config_list = []
        if m.get('productVersionConfigList') is not None:
            for k in m.get('productVersionConfigList'):
                temp_model = BatchAddProductVersionConfigRequestProductVersionConfigList()
                self.product_version_config_list.append(temp_model.from_map(k))
        return self


class BatchAddProductVersionConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
    ):
        self.code = code
        self.msg = msg

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class BatchAddProductVersionConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchAddProductVersionConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BatchAddProductVersionConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEnvironmentHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        client_token: str = None,
    ):
        self.common_headers = common_headers
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateEnvironmentRequestPlatform(TeaModel):
    def __init__(
        self,
        architecture: str = None,
        os: str = None,
    ):
        self.architecture = architecture
        self.os = os

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture is not None:
            result['architecture'] = self.architecture
        if self.os is not None:
            result['os'] = self.os
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('architecture') is not None:
            self.architecture = m.get('architecture')
        if m.get('os') is not None:
            self.os = m.get('os')
        return self


class CreateEnvironmentRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        location: str = None,
        name: str = None,
        platform: CreateEnvironmentRequestPlatform = None,
        platform_list: List[Platform] = None,
        product_version_uid: str = None,
        type: str = None,
        vendor_config: str = None,
        vendor_type: str = None,
    ):
        self.description = description
        self.location = location
        self.name = name
        self.platform = platform
        self.platform_list = platform_list
        self.product_version_uid = product_version_uid
        # 环境类型
        self.type = type
        self.vendor_config = vendor_config
        self.vendor_type = vendor_type

    def validate(self):
        if self.platform:
            self.platform.validate()
        if self.platform_list:
            for k in self.platform_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.location is not None:
            result['location'] = self.location
        if self.name is not None:
            result['name'] = self.name
        if self.platform is not None:
            result['platform'] = self.platform.to_map()
        result['platformList'] = []
        if self.platform_list is not None:
            for k in self.platform_list:
                result['platformList'].append(k.to_map() if k else None)
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        if self.type is not None:
            result['type'] = self.type
        if self.vendor_config is not None:
            result['vendorConfig'] = self.vendor_config
        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('platform') is not None:
            temp_model = CreateEnvironmentRequestPlatform()
            self.platform = temp_model.from_map(m['platform'])
        self.platform_list = []
        if m.get('platformList') is not None:
            for k in m.get('platformList'):
                temp_model = Platform()
                self.platform_list.append(temp_model.from_map(k))
        if m.get('productVersionUID') is not None:
            self.product_version_uid = m.get('productVersionUID')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('vendorConfig') is not None:
            self.vendor_config = m.get('vendorConfig')
        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')
        return self


class CreateEnvironmentResponseBodyData(TeaModel):
    def __init__(
        self,
        environment_uid: str = None,
        vendor_config: str = None,
    ):
        self.environment_uid = environment_uid
        self.vendor_config = vendor_config

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.environment_uid is not None:
            result['environmentUID'] = self.environment_uid
        if self.vendor_config is not None:
            result['vendorConfig'] = self.vendor_config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('environmentUID') is not None:
            self.environment_uid = m.get('environmentUID')
        if m.get('vendorConfig') is not None:
            self.vendor_config = m.get('vendorConfig')
        return self


class CreateEnvironmentResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateEnvironmentResponseBodyData = None,
        msg: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = CreateEnvironmentResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class CreateEnvironmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateEnvironmentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateEnvironmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEnvironmentLicenseRequestLicenseQuotaClusterQuota(TeaModel):
    def __init__(
        self,
        cpu_core_limit: int = None,
    ):
        self.cpu_core_limit = cpu_core_limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_core_limit is not None:
            result['cpuCoreLimit'] = self.cpu_core_limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cpuCoreLimit') is not None:
            self.cpu_core_limit = m.get('cpuCoreLimit')
        return self


class CreateEnvironmentLicenseRequestLicenseQuotaCustomQuotas(TeaModel):
    def __init__(
        self,
        description: str = None,
        key: str = None,
        value: str = None,
    ):
        self.description = description
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class CreateEnvironmentLicenseRequestLicenseQuota(TeaModel):
    def __init__(
        self,
        cluster_quota: CreateEnvironmentLicenseRequestLicenseQuotaClusterQuota = None,
        custom_quotas: List[CreateEnvironmentLicenseRequestLicenseQuotaCustomQuotas] = None,
    ):
        self.cluster_quota = cluster_quota
        self.custom_quotas = custom_quotas

    def validate(self):
        if self.cluster_quota:
            self.cluster_quota.validate()
        if self.custom_quotas:
            for k in self.custom_quotas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_quota is not None:
            result['clusterQuota'] = self.cluster_quota.to_map()
        result['customQuotas'] = []
        if self.custom_quotas is not None:
            for k in self.custom_quotas:
                result['customQuotas'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusterQuota') is not None:
            temp_model = CreateEnvironmentLicenseRequestLicenseQuotaClusterQuota()
            self.cluster_quota = temp_model.from_map(m['clusterQuota'])
        self.custom_quotas = []
        if m.get('customQuotas') is not None:
            for k in m.get('customQuotas'):
                temp_model = CreateEnvironmentLicenseRequestLicenseQuotaCustomQuotas()
                self.custom_quotas.append(temp_model.from_map(k))
        return self


class CreateEnvironmentLicenseRequest(TeaModel):
    def __init__(
        self,
        company_name: str = None,
        contact: str = None,
        license_quota: CreateEnvironmentLicenseRequestLicenseQuota = None,
        machine_fingerprint: str = None,
        name: str = None,
        product_version_uid: str = None,
        scenario: str = None,
        scope: str = None,
        type: str = None,
    ):
        # 企业名称
        self.company_name = company_name
        # 联系方式
        self.contact = contact
        self.license_quota = license_quota
        # 机器指纹信息
        self.machine_fingerprint = machine_fingerprint
        self.name = name
        self.product_version_uid = product_version_uid
        # 使用场景
        self.scenario = scenario
        self.scope = scope
        # 证书类型
        self.type = type

    def validate(self):
        if self.license_quota:
            self.license_quota.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.company_name is not None:
            result['companyName'] = self.company_name
        if self.contact is not None:
            result['contact'] = self.contact
        if self.license_quota is not None:
            result['licenseQuota'] = self.license_quota.to_map()
        if self.machine_fingerprint is not None:
            result['machineFingerprint'] = self.machine_fingerprint
        if self.name is not None:
            result['name'] = self.name
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        if self.scenario is not None:
            result['scenario'] = self.scenario
        if self.scope is not None:
            result['scope'] = self.scope
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('companyName') is not None:
            self.company_name = m.get('companyName')
        if m.get('contact') is not None:
            self.contact = m.get('contact')
        if m.get('licenseQuota') is not None:
            temp_model = CreateEnvironmentLicenseRequestLicenseQuota()
            self.license_quota = temp_model.from_map(m['licenseQuota'])
        if m.get('machineFingerprint') is not None:
            self.machine_fingerprint = m.get('machineFingerprint')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('productVersionUID') is not None:
            self.product_version_uid = m.get('productVersionUID')
        if m.get('scenario') is not None:
            self.scenario = m.get('scenario')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateEnvironmentLicenseResponseBodyData(TeaModel):
    def __init__(
        self,
        uid: str = None,
    ):
        # license uid
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class CreateEnvironmentLicenseResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateEnvironmentLicenseResponseBodyData = None,
        msg: str = None,
    ):
        self.code = code
        # 业务数据
        self.data = data
        self.msg = msg

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = CreateEnvironmentLicenseResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class CreateEnvironmentLicenseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateEnvironmentLicenseResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateEnvironmentLicenseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFoundationReferenceRequest(TeaModel):
    def __init__(
        self,
        cluster_config: str = None,
        foundation_version_uid: str = None,
    ):
        self.cluster_config = cluster_config
        self.foundation_version_uid = foundation_version_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_config is not None:
            result['clusterConfig'] = self.cluster_config
        if self.foundation_version_uid is not None:
            result['foundationVersionUID'] = self.foundation_version_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusterConfig') is not None:
            self.cluster_config = m.get('clusterConfig')
        if m.get('foundationVersionUID') is not None:
            self.foundation_version_uid = m.get('foundationVersionUID')
        return self


class CreateFoundationReferenceResponseBodyData(TeaModel):
    def __init__(
        self,
        uid: str = None,
    ):
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class CreateFoundationReferenceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateFoundationReferenceResponseBodyData = None,
        msg: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = CreateFoundationReferenceResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class CreateFoundationReferenceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFoundationReferenceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateFoundationReferenceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProductHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        client_token: str = None,
    ):
        self.common_headers = common_headers
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateProductRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        foundation_version_uid: str = None,
        product_name: str = None,
    ):
        self.description = description
        self.foundation_version_uid = foundation_version_uid
        self.product_name = product_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.foundation_version_uid is not None:
            result['foundationVersionUID'] = self.foundation_version_uid
        if self.product_name is not None:
            result['productName'] = self.product_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('foundationVersionUID') is not None:
            self.foundation_version_uid = m.get('foundationVersionUID')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        return self


class CreateProductResponseBodyData(TeaModel):
    def __init__(
        self,
        uid: str = None,
    ):
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class CreateProductResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateProductResponseBodyData = None,
        msg: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = CreateProductResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class CreateProductResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateProductResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProductDeploymentRequest(TeaModel):
    def __init__(
        self,
        environment_uid: str = None,
        namespace: str = None,
        old_product_version_uid: str = None,
        package_config: str = None,
        package_uid: str = None,
        product_version_uid: str = None,
    ):
        # 环境uid
        self.environment_uid = environment_uid
        # 指定产品部署的 namespace，仅 ACK 底座支持
        self.namespace = namespace
        # 旧产品版本uid
        self.old_product_version_uid = old_product_version_uid
        # 部署包配置文件
        self.package_config = package_config
        # 部署包uid
        self.package_uid = package_uid
        # 产品版本uid
        self.product_version_uid = product_version_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.environment_uid is not None:
            result['environmentUID'] = self.environment_uid
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.old_product_version_uid is not None:
            result['oldProductVersionUID'] = self.old_product_version_uid
        if self.package_config is not None:
            result['packageConfig'] = self.package_config
        if self.package_uid is not None:
            result['packageUID'] = self.package_uid
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('environmentUID') is not None:
            self.environment_uid = m.get('environmentUID')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('oldProductVersionUID') is not None:
            self.old_product_version_uid = m.get('oldProductVersionUID')
        if m.get('packageConfig') is not None:
            self.package_config = m.get('packageConfig')
        if m.get('packageUID') is not None:
            self.package_uid = m.get('packageUID')
        if m.get('productVersionUID') is not None:
            self.product_version_uid = m.get('productVersionUID')
        return self


class CreateProductDeploymentResponseBodyData(TeaModel):
    def __init__(
        self,
        uid: str = None,
    ):
        # 部署uid
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class CreateProductDeploymentResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateProductDeploymentResponseBodyData = None,
        msg: str = None,
    ):
        # 错误码
        self.code = code
        # 数据
        self.data = data
        # 错误信息
        self.msg = msg

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = CreateProductDeploymentResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class CreateProductDeploymentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateProductDeploymentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateProductDeploymentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProductVersionRequest(TeaModel):
    def __init__(
        self,
        base_product_version_uid: str = None,
    ):
        # 基于哪个版本克隆
        self.base_product_version_uid = base_product_version_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_product_version_uid is not None:
            result['baseProductVersionUID'] = self.base_product_version_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('baseProductVersionUID') is not None:
            self.base_product_version_uid = m.get('baseProductVersionUID')
        return self


class CreateProductVersionResponseBodyData(TeaModel):
    def __init__(
        self,
        uid: str = None,
    ):
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class CreateProductVersionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateProductVersionResponseBodyData = None,
        msg: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = CreateProductVersionResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class CreateProductVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateProductVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateProductVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProductVersionPackageHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        client_token: str = None,
    ):
        self.common_headers = common_headers
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateProductVersionPackageRequest(TeaModel):
    def __init__(
        self,
        cluster_engine_type: str = None,
        old_product_version_uid: str = None,
        package_content_type: str = None,
        package_tool_type: str = None,
        package_type: str = None,
        platform: str = None,
    ):
        # ENUM["TRIDENT","ACK-D"]
        self.cluster_engine_type = cluster_engine_type
        self.old_product_version_uid = old_product_version_uid
        # ENUM:["all","base"."application"]
        self.package_content_type = package_content_type
        # "ENUM value: ["Hopctl", "Sealer"]"
        self.package_tool_type = package_tool_type
        # ENUM:["full","upgrade"]
        self.package_type = package_type
        self.platform = platform

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_engine_type is not None:
            result['clusterEngineType'] = self.cluster_engine_type
        if self.old_product_version_uid is not None:
            result['oldProductVersionUID'] = self.old_product_version_uid
        if self.package_content_type is not None:
            result['packageContentType'] = self.package_content_type
        if self.package_tool_type is not None:
            result['packageToolType'] = self.package_tool_type
        if self.package_type is not None:
            result['packageType'] = self.package_type
        if self.platform is not None:
            result['platform'] = self.platform
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusterEngineType') is not None:
            self.cluster_engine_type = m.get('clusterEngineType')
        if m.get('oldProductVersionUID') is not None:
            self.old_product_version_uid = m.get('oldProductVersionUID')
        if m.get('packageContentType') is not None:
            self.package_content_type = m.get('packageContentType')
        if m.get('packageToolType') is not None:
            self.package_tool_type = m.get('packageToolType')
        if m.get('packageType') is not None:
            self.package_type = m.get('packageType')
        if m.get('platform') is not None:
            self.platform = m.get('platform')
        return self


class CreateProductVersionPackageResponseBodyData(TeaModel):
    def __init__(
        self,
        uid: str = None,
    ):
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class CreateProductVersionPackageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateProductVersionPackageResponseBodyData = None,
        msg: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = CreateProductVersionPackageResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class CreateProductVersionPackageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateProductVersionPackageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateProductVersionPackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEnvironmentResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
    ):
        self.code = code
        self.msg = msg

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class DeleteEnvironmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteEnvironmentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteEnvironmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEnvironmentLicenseResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.msg = msg
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteEnvironmentLicenseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteEnvironmentLicenseResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteEnvironmentLicenseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEnvironmentNodeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
    ):
        self.code = code
        self.msg = msg

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class DeleteEnvironmentNodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteEnvironmentNodeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteEnvironmentNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEnvironmentProductVersionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
    ):
        self.code = code
        self.msg = msg

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class DeleteEnvironmentProductVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteEnvironmentProductVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteEnvironmentProductVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProductResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
    ):
        self.code = code
        self.msg = msg

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class DeleteProductResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteProductResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProductComponentVersionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
    ):
        self.code = code
        self.msg = msg

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class DeleteProductComponentVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteProductComponentVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteProductComponentVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProductInstanceConfigRequest(TeaModel):
    def __init__(
        self,
        environment_uid: str = None,
        product_version_uid: str = None,
    ):
        self.environment_uid = environment_uid
        self.product_version_uid = product_version_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.environment_uid is not None:
            result['environmentUID'] = self.environment_uid
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('environmentUID') is not None:
            self.environment_uid = m.get('environmentUID')
        if m.get('productVersionUID') is not None:
            self.product_version_uid = m.get('productVersionUID')
        return self


class DeleteProductInstanceConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
    ):
        self.code = code
        self.msg = msg

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class DeleteProductInstanceConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteProductInstanceConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteProductInstanceConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProductVersionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.msg = msg
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteProductVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteProductVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteProductVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProductVersionConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.msg = msg
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteProductVersionConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteProductVersionConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteProductVersionConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateProductInstanceDeploymentConfigRequest(TeaModel):
    def __init__(
        self,
        environment_uid: str = None,
        package_uid: str = None,
        product_version_uid: str = None,
    ):
        self.environment_uid = environment_uid
        self.package_uid = package_uid
        self.product_version_uid = product_version_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.environment_uid is not None:
            result['environmentUID'] = self.environment_uid
        if self.package_uid is not None:
            result['packageUID'] = self.package_uid
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('environmentUID') is not None:
            self.environment_uid = m.get('environmentUID')
        if m.get('packageUID') is not None:
            self.package_uid = m.get('packageUID')
        if m.get('productVersionUID') is not None:
            self.product_version_uid = m.get('productVersionUID')
        return self


class GenerateProductInstanceDeploymentConfigResponseBodyData(TeaModel):
    def __init__(
        self,
        package_config: str = None,
    ):
        self.package_config = package_config

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.package_config is not None:
            result['packageConfig'] = self.package_config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('packageConfig') is not None:
            self.package_config = m.get('packageConfig')
        return self


class GenerateProductInstanceDeploymentConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GenerateProductInstanceDeploymentConfigResponseBodyData = None,
        msg: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GenerateProductInstanceDeploymentConfigResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class GenerateProductInstanceDeploymentConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateProductInstanceDeploymentConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GenerateProductInstanceDeploymentConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetComponentResponseBodyData(TeaModel):
    def __init__(
        self,
        category: str = None,
        description: str = None,
        documents: str = None,
        name: str = None,
        public: bool = None,
        singleton: bool = None,
        source: str = None,
        uid: str = None,
    ):
        self.category = category
        self.description = description
        self.documents = documents
        self.name = name
        self.public = public
        self.singleton = singleton
        self.source = source
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.description is not None:
            result['description'] = self.description
        if self.documents is not None:
            result['documents'] = self.documents
        if self.name is not None:
            result['name'] = self.name
        if self.public is not None:
            result['public'] = self.public
        if self.singleton is not None:
            result['singleton'] = self.singleton
        if self.source is not None:
            result['source'] = self.source
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('documents') is not None:
            self.documents = m.get('documents')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('public') is not None:
            self.public = m.get('public')
        if m.get('singleton') is not None:
            self.singleton = m.get('singleton')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class GetComponentResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetComponentResponseBodyData = None,
        msg: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetComponentResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class GetComponentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetComponentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetComponentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetComponentVersionRequest(TeaModel):
    def __init__(
        self,
        without_chart_content: bool = None,
    ):
        self.without_chart_content = without_chart_content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.without_chart_content is not None:
            result['withoutChartContent'] = self.without_chart_content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('withoutChartContent') is not None:
            self.without_chart_content = m.get('withoutChartContent')
        return self


class GetComponentVersionResponseBodyData(TeaModel):
    def __init__(
        self,
        component_name: str = None,
        component_uid: str = None,
        description: str = None,
        documents: List[str] = None,
        orchestration_values: str = None,
        package_url: str = None,
        parent_component: bool = None,
        product_component_version_uid: str = None,
        provider: str = None,
        readme: str = None,
        resources: str = None,
        uid: str = None,
        version: str = None,
    ):
        self.component_name = component_name
        self.component_uid = component_uid
        self.description = description
        self.documents = documents
        self.orchestration_values = orchestration_values
        self.package_url = package_url
        self.parent_component = parent_component
        self.product_component_version_uid = product_component_version_uid
        self.provider = provider
        self.readme = readme
        self.resources = resources
        self.uid = uid
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_name is not None:
            result['componentName'] = self.component_name
        if self.component_uid is not None:
            result['componentUID'] = self.component_uid
        if self.description is not None:
            result['description'] = self.description
        if self.documents is not None:
            result['documents'] = self.documents
        if self.orchestration_values is not None:
            result['orchestrationValues'] = self.orchestration_values
        if self.package_url is not None:
            result['packageURL'] = self.package_url
        if self.parent_component is not None:
            result['parentComponent'] = self.parent_component
        if self.product_component_version_uid is not None:
            result['productComponentVersionUID'] = self.product_component_version_uid
        if self.provider is not None:
            result['provider'] = self.provider
        if self.readme is not None:
            result['readme'] = self.readme
        if self.resources is not None:
            result['resources'] = self.resources
        if self.uid is not None:
            result['uid'] = self.uid
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('componentName') is not None:
            self.component_name = m.get('componentName')
        if m.get('componentUID') is not None:
            self.component_uid = m.get('componentUID')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('documents') is not None:
            self.documents = m.get('documents')
        if m.get('orchestrationValues') is not None:
            self.orchestration_values = m.get('orchestrationValues')
        if m.get('packageURL') is not None:
            self.package_url = m.get('packageURL')
        if m.get('parentComponent') is not None:
            self.parent_component = m.get('parentComponent')
        if m.get('productComponentVersionUID') is not None:
            self.product_component_version_uid = m.get('productComponentVersionUID')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('readme') is not None:
            self.readme = m.get('readme')
        if m.get('resources') is not None:
            self.resources = m.get('resources')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetComponentVersionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetComponentVersionResponseBodyData] = None,
        msg: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = GetComponentVersionResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class GetComponentVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetComponentVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetComponentVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEnvironmentRequestOptions(TeaModel):
    def __init__(
        self,
        with_site_survey_report: bool = None,
    ):
        self.with_site_survey_report = with_site_survey_report

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.with_site_survey_report is not None:
            result['withSiteSurveyReport'] = self.with_site_survey_report
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('withSiteSurveyReport') is not None:
            self.with_site_survey_report = m.get('withSiteSurveyReport')
        return self


class GetEnvironmentRequest(TeaModel):
    def __init__(
        self,
        options: GetEnvironmentRequestOptions = None,
    ):
        self.options = options

    def validate(self):
        if self.options:
            self.options.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.options is not None:
            result['options'] = self.options.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('options') is not None:
            temp_model = GetEnvironmentRequestOptions()
            self.options = temp_model.from_map(m['options'])
        return self


class GetEnvironmentShrinkRequest(TeaModel):
    def __init__(
        self,
        options_shrink: str = None,
    ):
        self.options_shrink = options_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.options_shrink is not None:
            result['options'] = self.options_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('options') is not None:
            self.options_shrink = m.get('options')
        return self


class GetEnvironmentResponseBodyDataPlatform(TeaModel):
    def __init__(
        self,
        architecture: str = None,
        os: str = None,
    ):
        self.architecture = architecture
        self.os = os

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture is not None:
            result['architecture'] = self.architecture
        if self.os is not None:
            result['os'] = self.os
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('architecture') is not None:
            self.architecture = m.get('architecture')
        if m.get('os') is not None:
            self.os = m.get('os')
        return self


class GetEnvironmentResponseBodyDataSiteSurveyReportCheckListFailedList(TeaModel):
    def __init__(
        self,
        ip: str = None,
        reason: Dict[str, Any] = None,
    ):
        self.ip = ip
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['ip'] = self.ip
        if self.reason is not None:
            result['reason'] = self.reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('reason') is not None:
            self.reason = m.get('reason')
        return self


class GetEnvironmentResponseBodyDataSiteSurveyReportCheckList(TeaModel):
    def __init__(
        self,
        description: Dict[str, Any] = None,
        failed_list: List[GetEnvironmentResponseBodyDataSiteSurveyReportCheckListFailedList] = None,
        level: str = None,
        name: str = None,
        status: str = None,
    ):
        self.description = description
        self.failed_list = failed_list
        self.level = level
        self.name = name
        self.status = status

    def validate(self):
        if self.failed_list:
            for k in self.failed_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        result['failedList'] = []
        if self.failed_list is not None:
            for k in self.failed_list:
                result['failedList'].append(k.to_map() if k else None)
        if self.level is not None:
            result['level'] = self.level
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        self.failed_list = []
        if m.get('failedList') is not None:
            for k in m.get('failedList'):
                temp_model = GetEnvironmentResponseBodyDataSiteSurveyReportCheckListFailedList()
                self.failed_list.append(temp_model.from_map(k))
        if m.get('level') is not None:
            self.level = m.get('level')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class GetEnvironmentResponseBodyDataSiteSurveyReport(TeaModel):
    def __init__(
        self,
        check_list: List[GetEnvironmentResponseBodyDataSiteSurveyReportCheckList] = None,
        result: str = None,
    ):
        self.check_list = check_list
        self.result = result

    def validate(self):
        if self.check_list:
            for k in self.check_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['checkList'] = []
        if self.check_list is not None:
            for k in self.check_list:
                result['checkList'].append(k.to_map() if k else None)
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.check_list = []
        if m.get('checkList') is not None:
            for k in m.get('checkList'):
                temp_model = GetEnvironmentResponseBodyDataSiteSurveyReportCheckList()
                self.check_list.append(temp_model.from_map(k))
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class GetEnvironmentResponseBodyData(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        created_at: str = None,
        description: str = None,
        foundation_version: str = None,
        foundation_version_uid: str = None,
        instance_list: List[InstanceInfo] = None,
        instance_status: str = None,
        location: str = None,
        name: str = None,
        old_product_version: str = None,
        old_product_version_uid: str = None,
        platform: GetEnvironmentResponseBodyDataPlatform = None,
        platform_list: List[Platform] = None,
        platform_status: str = None,
        product_name: str = None,
        product_version: str = None,
        site_survey_report: GetEnvironmentResponseBodyDataSiteSurveyReport = None,
        uid: str = None,
        vendor_config: str = None,
        vendor_type: str = None,
    ):
        self.cluster_id = cluster_id
        self.created_at = created_at
        self.description = description
        self.foundation_version = foundation_version
        self.foundation_version_uid = foundation_version_uid
        self.instance_list = instance_list
        self.instance_status = instance_status
        self.location = location
        self.name = name
        self.old_product_version = old_product_version
        self.old_product_version_uid = old_product_version_uid
        self.platform = platform
        self.platform_list = platform_list
        self.platform_status = platform_status
        self.product_name = product_name
        self.product_version = product_version
        self.site_survey_report = site_survey_report
        self.uid = uid
        self.vendor_config = vendor_config
        self.vendor_type = vendor_type

    def validate(self):
        if self.instance_list:
            for k in self.instance_list:
                if k:
                    k.validate()
        if self.platform:
            self.platform.validate()
        if self.platform_list:
            for k in self.platform_list:
                if k:
                    k.validate()
        if self.site_survey_report:
            self.site_survey_report.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.foundation_version is not None:
            result['foundationVersion'] = self.foundation_version
        if self.foundation_version_uid is not None:
            result['foundationVersionUID'] = self.foundation_version_uid
        result['instanceList'] = []
        if self.instance_list is not None:
            for k in self.instance_list:
                result['instanceList'].append(k.to_map() if k else None)
        if self.instance_status is not None:
            result['instanceStatus'] = self.instance_status
        if self.location is not None:
            result['location'] = self.location
        if self.name is not None:
            result['name'] = self.name
        if self.old_product_version is not None:
            result['oldProductVersion'] = self.old_product_version
        if self.old_product_version_uid is not None:
            result['oldProductVersionUID'] = self.old_product_version_uid
        if self.platform is not None:
            result['platform'] = self.platform.to_map()
        result['platformList'] = []
        if self.platform_list is not None:
            for k in self.platform_list:
                result['platformList'].append(k.to_map() if k else None)
        if self.platform_status is not None:
            result['platformStatus'] = self.platform_status
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.product_version is not None:
            result['productVersion'] = self.product_version
        if self.site_survey_report is not None:
            result['siteSurveyReport'] = self.site_survey_report.to_map()
        if self.uid is not None:
            result['uid'] = self.uid
        if self.vendor_config is not None:
            result['vendorConfig'] = self.vendor_config
        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('foundationVersion') is not None:
            self.foundation_version = m.get('foundationVersion')
        if m.get('foundationVersionUID') is not None:
            self.foundation_version_uid = m.get('foundationVersionUID')
        self.instance_list = []
        if m.get('instanceList') is not None:
            for k in m.get('instanceList'):
                temp_model = InstanceInfo()
                self.instance_list.append(temp_model.from_map(k))
        if m.get('instanceStatus') is not None:
            self.instance_status = m.get('instanceStatus')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('oldProductVersion') is not None:
            self.old_product_version = m.get('oldProductVersion')
        if m.get('oldProductVersionUID') is not None:
            self.old_product_version_uid = m.get('oldProductVersionUID')
        if m.get('platform') is not None:
            temp_model = GetEnvironmentResponseBodyDataPlatform()
            self.platform = temp_model.from_map(m['platform'])
        self.platform_list = []
        if m.get('platformList') is not None:
            for k in m.get('platformList'):
                temp_model = Platform()
                self.platform_list.append(temp_model.from_map(k))
        if m.get('platformStatus') is not None:
            self.platform_status = m.get('platformStatus')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('productVersion') is not None:
            self.product_version = m.get('productVersion')
        if m.get('siteSurveyReport') is not None:
            temp_model = GetEnvironmentResponseBodyDataSiteSurveyReport()
            self.site_survey_report = temp_model.from_map(m['siteSurveyReport'])
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('vendorConfig') is not None:
            self.vendor_config = m.get('vendorConfig')
        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')
        return self


class GetEnvironmentResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetEnvironmentResponseBodyData = None,
        msg: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetEnvironmentResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class GetEnvironmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetEnvironmentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetEnvironmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEnvironmentLicenseRequestOptions(TeaModel):
    def __init__(
        self,
        with_secret_yaml: bool = None,
    ):
        self.with_secret_yaml = with_secret_yaml

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.with_secret_yaml is not None:
            result['withSecretYAML'] = self.with_secret_yaml
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('withSecretYAML') is not None:
            self.with_secret_yaml = m.get('withSecretYAML')
        return self


class GetEnvironmentLicenseRequest(TeaModel):
    def __init__(
        self,
        options: GetEnvironmentLicenseRequestOptions = None,
    ):
        self.options = options

    def validate(self):
        if self.options:
            self.options.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.options is not None:
            result['options'] = self.options.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('options') is not None:
            temp_model = GetEnvironmentLicenseRequestOptions()
            self.options = temp_model.from_map(m['options'])
        return self


class GetEnvironmentLicenseShrinkRequest(TeaModel):
    def __init__(
        self,
        options_shrink: str = None,
    ):
        self.options_shrink = options_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.options_shrink is not None:
            result['options'] = self.options_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('options') is not None:
            self.options_shrink = m.get('options')
        return self


class GetEnvironmentLicenseResponseBodyDataLicenseQuotaClusterQuota(TeaModel):
    def __init__(
        self,
        cpu_core_limit: int = None,
    ):
        # cpu核数限制
        self.cpu_core_limit = cpu_core_limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_core_limit is not None:
            result['cpuCoreLimit'] = self.cpu_core_limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cpuCoreLimit') is not None:
            self.cpu_core_limit = m.get('cpuCoreLimit')
        return self


class GetEnvironmentLicenseResponseBodyDataLicenseQuotaComponentQuotas(TeaModel):
    def __init__(
        self,
        component_name: str = None,
        component_source: str = None,
        instance_limit: int = None,
    ):
        # 组件名
        self.component_name = component_name
        # 组件来源
        self.component_source = component_source
        # 实例数限制
        self.instance_limit = instance_limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_name is not None:
            result['componentName'] = self.component_name
        if self.component_source is not None:
            result['componentSource'] = self.component_source
        if self.instance_limit is not None:
            result['instanceLimit'] = self.instance_limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('componentName') is not None:
            self.component_name = m.get('componentName')
        if m.get('componentSource') is not None:
            self.component_source = m.get('componentSource')
        if m.get('instanceLimit') is not None:
            self.instance_limit = m.get('instanceLimit')
        return self


class GetEnvironmentLicenseResponseBodyDataLicenseQuotaCustomQuotas(TeaModel):
    def __init__(
        self,
        description: str = None,
        key: str = None,
        value: str = None,
    ):
        self.description = description
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetEnvironmentLicenseResponseBodyDataLicenseQuota(TeaModel):
    def __init__(
        self,
        cluster_quota: GetEnvironmentLicenseResponseBodyDataLicenseQuotaClusterQuota = None,
        component_quotas: List[GetEnvironmentLicenseResponseBodyDataLicenseQuotaComponentQuotas] = None,
        custom_quotas: List[GetEnvironmentLicenseResponseBodyDataLicenseQuotaCustomQuotas] = None,
    ):
        # 集群配额
        self.cluster_quota = cluster_quota
        # 组件配额
        self.component_quotas = component_quotas
        self.custom_quotas = custom_quotas

    def validate(self):
        if self.cluster_quota:
            self.cluster_quota.validate()
        if self.component_quotas:
            for k in self.component_quotas:
                if k:
                    k.validate()
        if self.custom_quotas:
            for k in self.custom_quotas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_quota is not None:
            result['clusterQuota'] = self.cluster_quota.to_map()
        result['componentQuotas'] = []
        if self.component_quotas is not None:
            for k in self.component_quotas:
                result['componentQuotas'].append(k.to_map() if k else None)
        result['customQuotas'] = []
        if self.custom_quotas is not None:
            for k in self.custom_quotas:
                result['customQuotas'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusterQuota') is not None:
            temp_model = GetEnvironmentLicenseResponseBodyDataLicenseQuotaClusterQuota()
            self.cluster_quota = temp_model.from_map(m['clusterQuota'])
        self.component_quotas = []
        if m.get('componentQuotas') is not None:
            for k in m.get('componentQuotas'):
                temp_model = GetEnvironmentLicenseResponseBodyDataLicenseQuotaComponentQuotas()
                self.component_quotas.append(temp_model.from_map(k))
        self.custom_quotas = []
        if m.get('customQuotas') is not None:
            for k in m.get('customQuotas'):
                temp_model = GetEnvironmentLicenseResponseBodyDataLicenseQuotaCustomQuotas()
                self.custom_quotas.append(temp_model.from_map(k))
        return self


class GetEnvironmentLicenseResponseBodyData(TeaModel):
    def __init__(
        self,
        expire_time: str = None,
        license_key: str = None,
        license_quota: GetEnvironmentLicenseResponseBodyDataLicenseQuota = None,
        product_version_uid: str = None,
        reject_reason: str = None,
        scope: str = None,
        secret_yaml: str = None,
        status: str = None,
        type: str = None,
        uid: str = None,
    ):
        # 过期时间
        self.expire_time = expire_time
        # license内容
        self.license_key = license_key
        # license配额
        self.license_quota = license_quota
        self.product_version_uid = product_version_uid
        # 拒绝原因
        self.reject_reason = reject_reason
        self.scope = scope
        self.secret_yaml = secret_yaml
        # 状态
        self.status = status
        # 类型
        self.type = type
        # license uid
        self.uid = uid

    def validate(self):
        if self.license_quota:
            self.license_quota.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expire_time is not None:
            result['expireTime'] = self.expire_time
        if self.license_key is not None:
            result['licenseKey'] = self.license_key
        if self.license_quota is not None:
            result['licenseQuota'] = self.license_quota.to_map()
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        if self.reject_reason is not None:
            result['rejectReason'] = self.reject_reason
        if self.scope is not None:
            result['scope'] = self.scope
        if self.secret_yaml is not None:
            result['secretYAML'] = self.secret_yaml
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')
        if m.get('licenseKey') is not None:
            self.license_key = m.get('licenseKey')
        if m.get('licenseQuota') is not None:
            temp_model = GetEnvironmentLicenseResponseBodyDataLicenseQuota()
            self.license_quota = temp_model.from_map(m['licenseQuota'])
        if m.get('productVersionUID') is not None:
            self.product_version_uid = m.get('productVersionUID')
        if m.get('rejectReason') is not None:
            self.reject_reason = m.get('rejectReason')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('secretYAML') is not None:
            self.secret_yaml = m.get('secretYAML')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class GetEnvironmentLicenseResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetEnvironmentLicenseResponseBodyData = None,
        msg: str = None,
    ):
        # 错误码
        self.code = code
        self.data = data
        # 错误信息
        self.msg = msg

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetEnvironmentLicenseResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class GetEnvironmentLicenseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetEnvironmentLicenseResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetEnvironmentLicenseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEnvironmentNodeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: InstanceInfo = None,
        msg: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = InstanceInfo()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class GetEnvironmentNodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetEnvironmentNodeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetEnvironmentNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFoundationComponentReferenceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[FoundationComponentReferenceDetail] = None,
        msg: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = FoundationComponentReferenceDetail()
                self.data.append(temp_model.from_map(k))
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class GetFoundationComponentReferenceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFoundationComponentReferenceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetFoundationComponentReferenceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFoundationReferenceResponseBodyData(TeaModel):
    def __init__(
        self,
        cluster_config: str = None,
        foundation_version_uid: str = None,
        uid: str = None,
    ):
        self.cluster_config = cluster_config
        self.foundation_version_uid = foundation_version_uid
        # foundation reference uid
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_config is not None:
            result['clusterConfig'] = self.cluster_config
        if self.foundation_version_uid is not None:
            result['foundationVersionUID'] = self.foundation_version_uid
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusterConfig') is not None:
            self.cluster_config = m.get('clusterConfig')
        if m.get('foundationVersionUID') is not None:
            self.foundation_version_uid = m.get('foundationVersionUID')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class GetFoundationReferenceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetFoundationReferenceResponseBodyData = None,
        msg: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetFoundationReferenceResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class GetFoundationReferenceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFoundationReferenceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetFoundationReferenceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFoundationVersionResponseBodyDataSiteSurveyTool(TeaModel):
    def __init__(
        self,
        cluster_checker_url: str = None,
        cluster_info_brief: str = None,
    ):
        self.cluster_checker_url = cluster_checker_url
        self.cluster_info_brief = cluster_info_brief

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_checker_url is not None:
            result['clusterCheckerURL'] = self.cluster_checker_url
        if self.cluster_info_brief is not None:
            result['clusterInfoBrief'] = self.cluster_info_brief
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusterCheckerURL') is not None:
            self.cluster_checker_url = m.get('clusterCheckerURL')
        if m.get('clusterInfoBrief') is not None:
            self.cluster_info_brief = m.get('clusterInfoBrief')
        return self


class GetFoundationVersionResponseBodyData(TeaModel):
    def __init__(
        self,
        description: str = None,
        features: List[str] = None,
        labels: str = None,
        name: str = None,
        platforms: List[Platform] = None,
        site_survey_tool: GetFoundationVersionResponseBodyDataSiteSurveyTool = None,
        status: str = None,
        type: str = None,
        uid: str = None,
        version: str = None,
    ):
        # description
        self.description = description
        # 底座功能列表
        self.features = features
        self.labels = labels
        # name，目前仅能是 “ADP 底座“
        self.name = name
        # platforms
        self.platforms = platforms
        self.site_survey_tool = site_survey_tool
        # status，ENUM:["Testing","Published","Deprecated"] Published 后，则全平台所有用户可见，请谨慎操作
        self.status = status
        # the type of foundation version,ENUM:["trident","ack"]
        self.type = type
        # uid
        self.uid = uid
        # version
        self.version = version

    def validate(self):
        if self.platforms:
            for k in self.platforms:
                if k:
                    k.validate()
        if self.site_survey_tool:
            self.site_survey_tool.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.features is not None:
            result['features'] = self.features
        if self.labels is not None:
            result['labels'] = self.labels
        if self.name is not None:
            result['name'] = self.name
        result['platforms'] = []
        if self.platforms is not None:
            for k in self.platforms:
                result['platforms'].append(k.to_map() if k else None)
        if self.site_survey_tool is not None:
            result['siteSurveyTool'] = self.site_survey_tool.to_map()
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        if self.uid is not None:
            result['uid'] = self.uid
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('features') is not None:
            self.features = m.get('features')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('name') is not None:
            self.name = m.get('name')
        self.platforms = []
        if m.get('platforms') is not None:
            for k in m.get('platforms'):
                temp_model = Platform()
                self.platforms.append(temp_model.from_map(k))
        if m.get('siteSurveyTool') is not None:
            temp_model = GetFoundationVersionResponseBodyDataSiteSurveyTool()
            self.site_survey_tool = temp_model.from_map(m['siteSurveyTool'])
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetFoundationVersionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetFoundationVersionResponseBodyData = None,
        msg: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetFoundationVersionResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class GetFoundationVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFoundationVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetFoundationVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProductResponseBodyData(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        uid: str = None,
    ):
        self.description = description
        self.name = name
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class GetProductResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetProductResponseBodyData = None,
        msg: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetProductResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class GetProductResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetProductResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProductComponentVersionResponseBodyData(TeaModel):
    def __init__(
        self,
        app_version: str = None,
        component_description: str = None,
        component_name: str = None,
        component_uid: str = None,
        component_version_description: str = None,
        component_version_uid: str = None,
        enable: bool = None,
        namespace: str = None,
        orchestration_values: str = None,
        parent_component: bool = None,
        parent_component_version_relation_uid: str = None,
        parent_component_version_uid: str = None,
        product_version_uid: str = None,
        relation_uid: str = None,
        release_name: str = None,
        resources: str = None,
        sequence: int = None,
        values: str = None,
        version: str = None,
    ):
        self.app_version = app_version
        self.component_description = component_description
        self.component_name = component_name
        self.component_uid = component_uid
        self.component_version_description = component_version_description
        self.component_version_uid = component_version_uid
        self.enable = enable
        self.namespace = namespace
        self.orchestration_values = orchestration_values
        self.parent_component = parent_component
        self.parent_component_version_relation_uid = parent_component_version_relation_uid
        self.parent_component_version_uid = parent_component_version_uid
        self.product_version_uid = product_version_uid
        self.relation_uid = relation_uid
        self.release_name = release_name
        self.resources = resources
        self.sequence = sequence
        self.values = values
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version is not None:
            result['appVersion'] = self.app_version
        if self.component_description is not None:
            result['componentDescription'] = self.component_description
        if self.component_name is not None:
            result['componentName'] = self.component_name
        if self.component_uid is not None:
            result['componentUID'] = self.component_uid
        if self.component_version_description is not None:
            result['componentVersionDescription'] = self.component_version_description
        if self.component_version_uid is not None:
            result['componentVersionUID'] = self.component_version_uid
        if self.enable is not None:
            result['enable'] = self.enable
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.orchestration_values is not None:
            result['orchestrationValues'] = self.orchestration_values
        if self.parent_component is not None:
            result['parentComponent'] = self.parent_component
        if self.parent_component_version_relation_uid is not None:
            result['parentComponentVersionRelationUID'] = self.parent_component_version_relation_uid
        if self.parent_component_version_uid is not None:
            result['parentComponentVersionUID'] = self.parent_component_version_uid
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        if self.relation_uid is not None:
            result['relationUID'] = self.relation_uid
        if self.release_name is not None:
            result['releaseName'] = self.release_name
        if self.resources is not None:
            result['resources'] = self.resources
        if self.sequence is not None:
            result['sequence'] = self.sequence
        if self.values is not None:
            result['values'] = self.values
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appVersion') is not None:
            self.app_version = m.get('appVersion')
        if m.get('componentDescription') is not None:
            self.component_description = m.get('componentDescription')
        if m.get('componentName') is not None:
            self.component_name = m.get('componentName')
        if m.get('componentUID') is not None:
            self.component_uid = m.get('componentUID')
        if m.get('componentVersionDescription') is not None:
            self.component_version_description = m.get('componentVersionDescription')
        if m.get('componentVersionUID') is not None:
            self.component_version_uid = m.get('componentVersionUID')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('orchestrationValues') is not None:
            self.orchestration_values = m.get('orchestrationValues')
        if m.get('parentComponent') is not None:
            self.parent_component = m.get('parentComponent')
        if m.get('parentComponentVersionRelationUID') is not None:
            self.parent_component_version_relation_uid = m.get('parentComponentVersionRelationUID')
        if m.get('parentComponentVersionUID') is not None:
            self.parent_component_version_uid = m.get('parentComponentVersionUID')
        if m.get('productVersionUID') is not None:
            self.product_version_uid = m.get('productVersionUID')
        if m.get('relationUID') is not None:
            self.relation_uid = m.get('relationUID')
        if m.get('releaseName') is not None:
            self.release_name = m.get('releaseName')
        if m.get('resources') is not None:
            self.resources = m.get('resources')
        if m.get('sequence') is not None:
            self.sequence = m.get('sequence')
        if m.get('values') is not None:
            self.values = m.get('values')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetProductComponentVersionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetProductComponentVersionResponseBodyData] = None,
        msg: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = GetProductComponentVersionResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class GetProductComponentVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetProductComponentVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetProductComponentVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProductDeploymentRequest(TeaModel):
    def __init__(
        self,
        environment_uid: str = None,
        product_version_uid: str = None,
        with_param_config: bool = None,
    ):
        self.environment_uid = environment_uid
        self.product_version_uid = product_version_uid
        self.with_param_config = with_param_config

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.environment_uid is not None:
            result['environmentUID'] = self.environment_uid
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        if self.with_param_config is not None:
            result['withParamConfig'] = self.with_param_config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('environmentUID') is not None:
            self.environment_uid = m.get('environmentUID')
        if m.get('productVersionUID') is not None:
            self.product_version_uid = m.get('productVersionUID')
        if m.get('withParamConfig') is not None:
            self.with_param_config = m.get('withParamConfig')
        return self


class GetProductDeploymentResponseBodyData(TeaModel):
    def __init__(
        self,
        env_params: str = None,
        env_uid: str = None,
        status: str = None,
        uid: str = None,
    ):
        self.env_params = env_params
        self.env_uid = env_uid
        self.status = status
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env_params is not None:
            result['envParams'] = self.env_params
        if self.env_uid is not None:
            result['envUID'] = self.env_uid
        if self.status is not None:
            result['status'] = self.status
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('envParams') is not None:
            self.env_params = m.get('envParams')
        if m.get('envUID') is not None:
            self.env_uid = m.get('envUID')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class GetProductDeploymentResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetProductDeploymentResponseBodyData = None,
        msg: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetProductDeploymentResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class GetProductDeploymentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetProductDeploymentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetProductDeploymentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProductVersionResponseBodyData(TeaModel):
    def __init__(
        self,
        description: str = None,
        foundation_version_uid: str = None,
        package_url: str = None,
        platforms: List[Platform] = None,
        product_name: str = None,
        product_uid: str = None,
        provider: str = None,
        uid: str = None,
        version: str = None,
    ):
        self.description = description
        self.foundation_version_uid = foundation_version_uid
        self.package_url = package_url
        self.platforms = platforms
        self.product_name = product_name
        self.product_uid = product_uid
        self.provider = provider
        self.uid = uid
        self.version = version

    def validate(self):
        if self.platforms:
            for k in self.platforms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.foundation_version_uid is not None:
            result['foundationVersionUID'] = self.foundation_version_uid
        if self.package_url is not None:
            result['packageURL'] = self.package_url
        result['platforms'] = []
        if self.platforms is not None:
            for k in self.platforms:
                result['platforms'].append(k.to_map() if k else None)
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.product_uid is not None:
            result['productUID'] = self.product_uid
        if self.provider is not None:
            result['provider'] = self.provider
        if self.uid is not None:
            result['uid'] = self.uid
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('foundationVersionUID') is not None:
            self.foundation_version_uid = m.get('foundationVersionUID')
        if m.get('packageURL') is not None:
            self.package_url = m.get('packageURL')
        self.platforms = []
        if m.get('platforms') is not None:
            for k in m.get('platforms'):
                temp_model = Platform()
                self.platforms.append(temp_model.from_map(k))
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('productUID') is not None:
            self.product_uid = m.get('productUID')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetProductVersionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetProductVersionResponseBodyData = None,
        msg: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetProductVersionResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class GetProductVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetProductVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetProductVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProductVersionDifferencesRequest(TeaModel):
    def __init__(
        self,
        pre_version_uid: str = None,
    ):
        # 上一个产品版本id
        self.pre_version_uid = pre_version_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pre_version_uid is not None:
            result['preVersionUID'] = self.pre_version_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('preVersionUID') is not None:
            self.pre_version_uid = m.get('preVersionUID')
        return self


class GetProductVersionDifferencesResponseBodyData(TeaModel):
    def __init__(
        self,
        component_name: str = None,
        difference: str = None,
        message: str = None,
        pre_version: str = None,
        release_name: str = None,
        upgrade_flag: bool = None,
        version: str = None,
    ):
        # 组件名称
        self.component_name = component_name
        # 变更类型，ENUM 类型
        self.difference = difference
        # 变更描述信息
        self.message = message
        # 组件之前的版本号
        self.pre_version = pre_version
        # 组件实例名称
        self.release_name = release_name
        self.upgrade_flag = upgrade_flag
        # 组件当前的版本号
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_name is not None:
            result['componentName'] = self.component_name
        if self.difference is not None:
            result['difference'] = self.difference
        if self.message is not None:
            result['message'] = self.message
        if self.pre_version is not None:
            result['preVersion'] = self.pre_version
        if self.release_name is not None:
            result['releaseName'] = self.release_name
        if self.upgrade_flag is not None:
            result['upgradeFlag'] = self.upgrade_flag
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('componentName') is not None:
            self.component_name = m.get('componentName')
        if m.get('difference') is not None:
            self.difference = m.get('difference')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('preVersion') is not None:
            self.pre_version = m.get('preVersion')
        if m.get('releaseName') is not None:
            self.release_name = m.get('releaseName')
        if m.get('upgradeFlag') is not None:
            self.upgrade_flag = m.get('upgradeFlag')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetProductVersionDifferencesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetProductVersionDifferencesResponseBodyData] = None,
        msg: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.msg is not None:
            result['msg'] = self.msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = GetProductVersionDifferencesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetProductVersionDifferencesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetProductVersionDifferencesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetProductVersionDifferencesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProductVersionPackageRequest(TeaModel):
    def __init__(
        self,
        old_product_version_uid: str = None,
        package_content_type: str = None,
        package_type: str = None,
        package_uid: str = None,
        platform: str = None,
        with_url: bool = None,
    ):
        self.old_product_version_uid = old_product_version_uid
        self.package_content_type = package_content_type
        self.package_type = package_type
        self.package_uid = package_uid
        self.platform = platform
        self.with_url = with_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.old_product_version_uid is not None:
            result['oldProductVersionUID'] = self.old_product_version_uid
        if self.package_content_type is not None:
            result['packageContentType'] = self.package_content_type
        if self.package_type is not None:
            result['packageType'] = self.package_type
        if self.package_uid is not None:
            result['packageUID'] = self.package_uid
        if self.platform is not None:
            result['platform'] = self.platform
        if self.with_url is not None:
            result['withURL'] = self.with_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('oldProductVersionUID') is not None:
            self.old_product_version_uid = m.get('oldProductVersionUID')
        if m.get('packageContentType') is not None:
            self.package_content_type = m.get('packageContentType')
        if m.get('packageType') is not None:
            self.package_type = m.get('packageType')
        if m.get('packageUID') is not None:
            self.package_uid = m.get('packageUID')
        if m.get('platform') is not None:
            self.platform = m.get('platform')
        if m.get('withURL') is not None:
            self.with_url = m.get('withURL')
        return self


class GetProductVersionPackageResponseBodyData(TeaModel):
    def __init__(
        self,
        package_content_type: str = None,
        package_size: str = None,
        package_status: str = None,
        package_type: str = None,
        package_uid: str = None,
        package_url: str = None,
        platform: Platform = None,
        platform_list: List[Platform] = None,
    ):
        self.package_content_type = package_content_type
        self.package_size = package_size
        self.package_status = package_status
        self.package_type = package_type
        self.package_uid = package_uid
        self.package_url = package_url
        self.platform = platform
        self.platform_list = platform_list

    def validate(self):
        if self.platform:
            self.platform.validate()
        if self.platform_list:
            for k in self.platform_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.package_content_type is not None:
            result['packageContentType'] = self.package_content_type
        if self.package_size is not None:
            result['packageSize'] = self.package_size
        if self.package_status is not None:
            result['packageStatus'] = self.package_status
        if self.package_type is not None:
            result['packageType'] = self.package_type
        if self.package_uid is not None:
            result['packageUID'] = self.package_uid
        if self.package_url is not None:
            result['packageURL'] = self.package_url
        if self.platform is not None:
            result['platform'] = self.platform.to_map()
        result['platformList'] = []
        if self.platform_list is not None:
            for k in self.platform_list:
                result['platformList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('packageContentType') is not None:
            self.package_content_type = m.get('packageContentType')
        if m.get('packageSize') is not None:
            self.package_size = m.get('packageSize')
        if m.get('packageStatus') is not None:
            self.package_status = m.get('packageStatus')
        if m.get('packageType') is not None:
            self.package_type = m.get('packageType')
        if m.get('packageUID') is not None:
            self.package_uid = m.get('packageUID')
        if m.get('packageURL') is not None:
            self.package_url = m.get('packageURL')
        if m.get('platform') is not None:
            temp_model = Platform()
            self.platform = temp_model.from_map(m['platform'])
        self.platform_list = []
        if m.get('platformList') is not None:
            for k in m.get('platformList'):
                temp_model = Platform()
                self.platform_list.append(temp_model.from_map(k))
        return self


class GetProductVersionPackageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetProductVersionPackageResponseBodyData = None,
        msg: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetProductVersionPackageResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class GetProductVersionPackageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetProductVersionPackageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetProductVersionPackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceSnapshotRequest(TeaModel):
    def __init__(
        self,
        product_version_uid: str = None,
    ):
        self.product_version_uid = product_version_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('productVersionUID') is not None:
            self.product_version_uid = m.get('productVersionUID')
        return self


class GetResourceSnapshotResponseBodyAdpInfoComponents(TeaModel):
    def __init__(
        self,
        cpulimit: str = None,
        cpurequest: str = None,
        component_name: str = None,
        component_release_name: str = None,
        component_version: str = None,
        memory_limit: str = None,
        memory_request: str = None,
        orchestration_value: str = None,
        status: str = None,
        storage_request: str = None,
    ):
        self.cpulimit = cpulimit
        self.cpurequest = cpurequest
        self.component_name = component_name
        self.component_release_name = component_release_name
        self.component_version = component_version
        self.memory_limit = memory_limit
        self.memory_request = memory_request
        self.orchestration_value = orchestration_value
        self.status = status
        self.storage_request = storage_request

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpulimit is not None:
            result['CPULimit'] = self.cpulimit
        if self.cpurequest is not None:
            result['CPURequest'] = self.cpurequest
        if self.component_name is not None:
            result['componentName'] = self.component_name
        if self.component_release_name is not None:
            result['componentReleaseName'] = self.component_release_name
        if self.component_version is not None:
            result['componentVersion'] = self.component_version
        if self.memory_limit is not None:
            result['memoryLimit'] = self.memory_limit
        if self.memory_request is not None:
            result['memoryRequest'] = self.memory_request
        if self.orchestration_value is not None:
            result['orchestrationValue'] = self.orchestration_value
        if self.status is not None:
            result['status'] = self.status
        if self.storage_request is not None:
            result['storageRequest'] = self.storage_request
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CPULimit') is not None:
            self.cpulimit = m.get('CPULimit')
        if m.get('CPURequest') is not None:
            self.cpurequest = m.get('CPURequest')
        if m.get('componentName') is not None:
            self.component_name = m.get('componentName')
        if m.get('componentReleaseName') is not None:
            self.component_release_name = m.get('componentReleaseName')
        if m.get('componentVersion') is not None:
            self.component_version = m.get('componentVersion')
        if m.get('memoryLimit') is not None:
            self.memory_limit = m.get('memoryLimit')
        if m.get('memoryRequest') is not None:
            self.memory_request = m.get('memoryRequest')
        if m.get('orchestrationValue') is not None:
            self.orchestration_value = m.get('orchestrationValue')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('storageRequest') is not None:
            self.storage_request = m.get('storageRequest')
        return self


class GetResourceSnapshotResponseBodyAdpInfo(TeaModel):
    def __init__(
        self,
        cpurequest: str = None,
        component_num: int = None,
        components: List[GetResourceSnapshotResponseBodyAdpInfoComponents] = None,
        memory_request: str = None,
        pod_num: int = None,
        storage_request: str = None,
        workload_num: int = None,
    ):
        self.cpurequest = cpurequest
        self.component_num = component_num
        self.components = components
        self.memory_request = memory_request
        self.pod_num = pod_num
        self.storage_request = storage_request
        self.workload_num = workload_num

    def validate(self):
        if self.components:
            for k in self.components:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpurequest is not None:
            result['CPURequest'] = self.cpurequest
        if self.component_num is not None:
            result['componentNum'] = self.component_num
        result['components'] = []
        if self.components is not None:
            for k in self.components:
                result['components'].append(k.to_map() if k else None)
        if self.memory_request is not None:
            result['memoryRequest'] = self.memory_request
        if self.pod_num is not None:
            result['podNum'] = self.pod_num
        if self.storage_request is not None:
            result['storageRequest'] = self.storage_request
        if self.workload_num is not None:
            result['workloadNum'] = self.workload_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CPURequest') is not None:
            self.cpurequest = m.get('CPURequest')
        if m.get('componentNum') is not None:
            self.component_num = m.get('componentNum')
        self.components = []
        if m.get('components') is not None:
            for k in m.get('components'):
                temp_model = GetResourceSnapshotResponseBodyAdpInfoComponents()
                self.components.append(temp_model.from_map(k))
        if m.get('memoryRequest') is not None:
            self.memory_request = m.get('memoryRequest')
        if m.get('podNum') is not None:
            self.pod_num = m.get('podNum')
        if m.get('storageRequest') is not None:
            self.storage_request = m.get('storageRequest')
        if m.get('workloadNum') is not None:
            self.workload_num = m.get('workloadNum')
        return self


class GetResourceSnapshotResponseBodyProductInfoComponents(TeaModel):
    def __init__(
        self,
        cpulimit: str = None,
        cpurequest: str = None,
        component_name: str = None,
        component_release_name: str = None,
        component_version: str = None,
        memory_limit: str = None,
        memory_request: str = None,
        orchestration_value: str = None,
        status: str = None,
        storage_request: str = None,
    ):
        self.cpulimit = cpulimit
        self.cpurequest = cpurequest
        self.component_name = component_name
        self.component_release_name = component_release_name
        self.component_version = component_version
        self.memory_limit = memory_limit
        self.memory_request = memory_request
        self.orchestration_value = orchestration_value
        self.status = status
        self.storage_request = storage_request

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpulimit is not None:
            result['CPULimit'] = self.cpulimit
        if self.cpurequest is not None:
            result['CPURequest'] = self.cpurequest
        if self.component_name is not None:
            result['componentName'] = self.component_name
        if self.component_release_name is not None:
            result['componentReleaseName'] = self.component_release_name
        if self.component_version is not None:
            result['componentVersion'] = self.component_version
        if self.memory_limit is not None:
            result['memoryLimit'] = self.memory_limit
        if self.memory_request is not None:
            result['memoryRequest'] = self.memory_request
        if self.orchestration_value is not None:
            result['orchestrationValue'] = self.orchestration_value
        if self.status is not None:
            result['status'] = self.status
        if self.storage_request is not None:
            result['storageRequest'] = self.storage_request
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CPULimit') is not None:
            self.cpulimit = m.get('CPULimit')
        if m.get('CPURequest') is not None:
            self.cpurequest = m.get('CPURequest')
        if m.get('componentName') is not None:
            self.component_name = m.get('componentName')
        if m.get('componentReleaseName') is not None:
            self.component_release_name = m.get('componentReleaseName')
        if m.get('componentVersion') is not None:
            self.component_version = m.get('componentVersion')
        if m.get('memoryLimit') is not None:
            self.memory_limit = m.get('memoryLimit')
        if m.get('memoryRequest') is not None:
            self.memory_request = m.get('memoryRequest')
        if m.get('orchestrationValue') is not None:
            self.orchestration_value = m.get('orchestrationValue')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('storageRequest') is not None:
            self.storage_request = m.get('storageRequest')
        return self


class GetResourceSnapshotResponseBodyProductInfo(TeaModel):
    def __init__(
        self,
        cpurequest: str = None,
        component_num: int = None,
        components: List[GetResourceSnapshotResponseBodyProductInfoComponents] = None,
        memory_request: str = None,
        pod_num: int = None,
        storage_request: str = None,
        workload_num: int = None,
    ):
        self.cpurequest = cpurequest
        self.component_num = component_num
        self.components = components
        self.memory_request = memory_request
        self.pod_num = pod_num
        self.storage_request = storage_request
        self.workload_num = workload_num

    def validate(self):
        if self.components:
            for k in self.components:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpurequest is not None:
            result['CPURequest'] = self.cpurequest
        if self.component_num is not None:
            result['componentNum'] = self.component_num
        result['components'] = []
        if self.components is not None:
            for k in self.components:
                result['components'].append(k.to_map() if k else None)
        if self.memory_request is not None:
            result['memoryRequest'] = self.memory_request
        if self.pod_num is not None:
            result['podNum'] = self.pod_num
        if self.storage_request is not None:
            result['storageRequest'] = self.storage_request
        if self.workload_num is not None:
            result['workloadNum'] = self.workload_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CPURequest') is not None:
            self.cpurequest = m.get('CPURequest')
        if m.get('componentNum') is not None:
            self.component_num = m.get('componentNum')
        self.components = []
        if m.get('components') is not None:
            for k in m.get('components'):
                temp_model = GetResourceSnapshotResponseBodyProductInfoComponents()
                self.components.append(temp_model.from_map(k))
        if m.get('memoryRequest') is not None:
            self.memory_request = m.get('memoryRequest')
        if m.get('podNum') is not None:
            self.pod_num = m.get('podNum')
        if m.get('storageRequest') is not None:
            self.storage_request = m.get('storageRequest')
        if m.get('workloadNum') is not None:
            self.workload_num = m.get('workloadNum')
        return self


class GetResourceSnapshotResponseBody(TeaModel):
    def __init__(
        self,
        cpulimit: str = None,
        cpurequest: str = None,
        adp_info: GetResourceSnapshotResponseBodyAdpInfo = None,
        memory_limit: str = None,
        memory_request: str = None,
        product_info: GetResourceSnapshotResponseBodyProductInfo = None,
        storage_request: str = None,
    ):
        self.cpulimit = cpulimit
        self.cpurequest = cpurequest
        self.adp_info = adp_info
        self.memory_limit = memory_limit
        self.memory_request = memory_request
        self.product_info = product_info
        self.storage_request = storage_request

    def validate(self):
        if self.adp_info:
            self.adp_info.validate()
        if self.product_info:
            self.product_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpulimit is not None:
            result['CPULimit'] = self.cpulimit
        if self.cpurequest is not None:
            result['CPURequest'] = self.cpurequest
        if self.adp_info is not None:
            result['adpInfo'] = self.adp_info.to_map()
        if self.memory_limit is not None:
            result['memoryLimit'] = self.memory_limit
        if self.memory_request is not None:
            result['memoryRequest'] = self.memory_request
        if self.product_info is not None:
            result['productInfo'] = self.product_info.to_map()
        if self.storage_request is not None:
            result['storageRequest'] = self.storage_request
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CPULimit') is not None:
            self.cpulimit = m.get('CPULimit')
        if m.get('CPURequest') is not None:
            self.cpurequest = m.get('CPURequest')
        if m.get('adpInfo') is not None:
            temp_model = GetResourceSnapshotResponseBodyAdpInfo()
            self.adp_info = temp_model.from_map(m['adpInfo'])
        if m.get('memoryLimit') is not None:
            self.memory_limit = m.get('memoryLimit')
        if m.get('memoryRequest') is not None:
            self.memory_request = m.get('memoryRequest')
        if m.get('productInfo') is not None:
            temp_model = GetResourceSnapshotResponseBodyProductInfo()
            self.product_info = temp_model.from_map(m['productInfo'])
        if m.get('storageRequest') is not None:
            self.storage_request = m.get('storageRequest')
        return self


class GetResourceSnapshotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetResourceSnapshotResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetResourceSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWorkflowStatusRequest(TeaModel):
    def __init__(
        self,
        workflow_type: str = None,
        xuid: str = None,
    ):
        # ENUM:["CreateCluster","DeleteCluster","Pack","Deploy","UnbindProductVersion"]
        self.workflow_type = workflow_type
        # xuid，根据场景传递env_uid/package_uid/deploy_uid
        self.xuid = xuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workflow_type is not None:
            result['workflowType'] = self.workflow_type
        if self.xuid is not None:
            result['xuid'] = self.xuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('workflowType') is not None:
            self.workflow_type = m.get('workflowType')
        if m.get('xuid') is not None:
            self.xuid = m.get('xuid')
        return self


class GetWorkflowStatusResponseBodyDataStepStatusWorkflowTasks(TeaModel):
    def __init__(
        self,
        name: str = None,
        status: str = None,
    ):
        # task name
        self.name = name
        # task status
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class GetWorkflowStatusResponseBodyDataStepStatus(TeaModel):
    def __init__(
        self,
        name: str = None,
        status: str = None,
        workflow_tasks: List[GetWorkflowStatusResponseBodyDataStepStatusWorkflowTasks] = None,
    ):
        # step name
        self.name = name
        # step status
        self.status = status
        self.workflow_tasks = workflow_tasks

    def validate(self):
        if self.workflow_tasks:
            for k in self.workflow_tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        result['workflowTasks'] = []
        if self.workflow_tasks is not None:
            for k in self.workflow_tasks:
                result['workflowTasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        self.workflow_tasks = []
        if m.get('workflowTasks') is not None:
            for k in m.get('workflowTasks'):
                temp_model = GetWorkflowStatusResponseBodyDataStepStatusWorkflowTasks()
                self.workflow_tasks.append(temp_model.from_map(k))
        return self


class GetWorkflowStatusResponseBodyData(TeaModel):
    def __init__(
        self,
        status: str = None,
        step_status: List[GetWorkflowStatusResponseBodyDataStepStatus] = None,
    ):
        self.status = status
        self.step_status = step_status

    def validate(self):
        if self.step_status:
            for k in self.step_status:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['status'] = self.status
        result['stepStatus'] = []
        if self.step_status is not None:
            for k in self.step_status:
                result['stepStatus'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')
        self.step_status = []
        if m.get('stepStatus') is not None:
            for k in m.get('stepStatus'):
                temp_model = GetWorkflowStatusResponseBodyDataStepStatus()
                self.step_status.append(temp_model.from_map(k))
        return self


class GetWorkflowStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetWorkflowStatusResponseBodyData = None,
        msg: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetWorkflowStatusResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class GetWorkflowStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetWorkflowStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetWorkflowStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InitEnvironmentResourceRequest(TeaModel):
    def __init__(
        self,
        access_key_id: str = None,
        access_key_secret: str = None,
        security_token: str = None,
    ):
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['accessKeyID'] = self.access_key_id
        if self.access_key_secret is not None:
            result['accessKeySecret'] = self.access_key_secret
        if self.security_token is not None:
            result['securityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKeyID') is not None:
            self.access_key_id = m.get('accessKeyID')
        if m.get('accessKeySecret') is not None:
            self.access_key_secret = m.get('accessKeySecret')
        if m.get('securityToken') is not None:
            self.security_token = m.get('securityToken')
        return self


class InitEnvironmentResourceResponseBodyData(TeaModel):
    def __init__(
        self,
        status: str = None,
    ):
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class InitEnvironmentResourceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: InitEnvironmentResourceResponseBodyData = None,
        msg: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = InitEnvironmentResourceResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class InitEnvironmentResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InitEnvironmentResourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = InitEnvironmentResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListComponentVersionsRequestPlatforms(TeaModel):
    def __init__(
        self,
        architecture: str = None,
        os: str = None,
    ):
        self.architecture = architecture
        self.os = os

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture is not None:
            result['architecture'] = self.architecture
        if self.os is not None:
            result['os'] = self.os
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('architecture') is not None:
            self.architecture = m.get('architecture')
        if m.get('os') is not None:
            self.os = m.get('os')
        return self


class ListComponentVersionsRequest(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        platforms: List[ListComponentVersionsRequestPlatforms] = None,
    ):
        self.page_num = page_num
        self.page_size = page_size
        self.platforms = platforms

    def validate(self):
        if self.platforms:
            for k in self.platforms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        result['platforms'] = []
        if self.platforms is not None:
            for k in self.platforms:
                result['platforms'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        self.platforms = []
        if m.get('platforms') is not None:
            for k in m.get('platforms'):
                temp_model = ListComponentVersionsRequestPlatforms()
                self.platforms.append(temp_model.from_map(k))
        return self


class ListComponentVersionsShrinkRequest(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        platforms_shrink: str = None,
    ):
        self.page_num = page_num
        self.page_size = page_size
        self.platforms_shrink = platforms_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.platforms_shrink is not None:
            result['platforms'] = self.platforms_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('platforms') is not None:
            self.platforms_shrink = m.get('platforms')
        return self


class ListComponentVersionsResponseBodyDataList(TeaModel):
    def __init__(
        self,
        app_version: str = None,
        component_name: str = None,
        component_uid: str = None,
        description: str = None,
        documents: str = None,
        images_mapping: str = None,
        orchestration_values: str = None,
        package_url: str = None,
        parent_component: bool = None,
        readme: str = None,
        resources: str = None,
        uid: str = None,
        version: str = None,
    ):
        self.app_version = app_version
        self.component_name = component_name
        self.component_uid = component_uid
        self.description = description
        self.documents = documents
        self.images_mapping = images_mapping
        self.orchestration_values = orchestration_values
        self.package_url = package_url
        self.parent_component = parent_component
        self.readme = readme
        self.resources = resources
        self.uid = uid
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version is not None:
            result['appVersion'] = self.app_version
        if self.component_name is not None:
            result['componentName'] = self.component_name
        if self.component_uid is not None:
            result['componentUID'] = self.component_uid
        if self.description is not None:
            result['description'] = self.description
        if self.documents is not None:
            result['documents'] = self.documents
        if self.images_mapping is not None:
            result['imagesMapping'] = self.images_mapping
        if self.orchestration_values is not None:
            result['orchestrationValues'] = self.orchestration_values
        if self.package_url is not None:
            result['packageURL'] = self.package_url
        if self.parent_component is not None:
            result['parentComponent'] = self.parent_component
        if self.readme is not None:
            result['readme'] = self.readme
        if self.resources is not None:
            result['resources'] = self.resources
        if self.uid is not None:
            result['uid'] = self.uid
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appVersion') is not None:
            self.app_version = m.get('appVersion')
        if m.get('componentName') is not None:
            self.component_name = m.get('componentName')
        if m.get('componentUID') is not None:
            self.component_uid = m.get('componentUID')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('documents') is not None:
            self.documents = m.get('documents')
        if m.get('imagesMapping') is not None:
            self.images_mapping = m.get('imagesMapping')
        if m.get('orchestrationValues') is not None:
            self.orchestration_values = m.get('orchestrationValues')
        if m.get('packageURL') is not None:
            self.package_url = m.get('packageURL')
        if m.get('parentComponent') is not None:
            self.parent_component = m.get('parentComponent')
        if m.get('readme') is not None:
            self.readme = m.get('readme')
        if m.get('resources') is not None:
            self.resources = m.get('resources')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ListComponentVersionsResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[ListComponentVersionsResponseBodyDataList] = None,
        page_num: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.list = list
        self.page_num = page_num
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListComponentVersionsResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListComponentVersionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: ListComponentVersionsResponseBodyData = None,
        msg: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data
        self.msg = msg

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = ListComponentVersionsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class ListComponentVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListComponentVersionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListComponentVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListComponentsRequest(TeaModel):
    def __init__(
        self,
        category: str = None,
        fuzzy: str = None,
        name: str = None,
        page_num: int = None,
        page_size: int = None,
        public: bool = None,
    ):
        self.category = category
        self.fuzzy = fuzzy
        self.name = name
        self.page_num = page_num
        self.page_size = page_size
        self.public = public

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.fuzzy is not None:
            result['fuzzy'] = self.fuzzy
        if self.name is not None:
            result['name'] = self.name
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.public is not None:
            result['public'] = self.public
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('fuzzy') is not None:
            self.fuzzy = m.get('fuzzy')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('public') is not None:
            self.public = m.get('public')
        return self


class ListComponentsResponseBodyDataListAnnotations(TeaModel):
    def __init__(
        self,
        annotations: str = None,
    ):
        self.annotations = annotations

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.annotations is not None:
            result['annotations'] = self.annotations
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('annotations') is not None:
            self.annotations = m.get('annotations')
        return self


class ListComponentsResponseBodyDataList(TeaModel):
    def __init__(
        self,
        annotations: ListComponentsResponseBodyDataListAnnotations = None,
        category: str = None,
        description: str = None,
        documents: str = None,
        name: str = None,
        provider: str = None,
        public: bool = None,
        singleton: bool = None,
        source: str = None,
        uid: str = None,
    ):
        self.annotations = annotations
        self.category = category
        self.description = description
        self.documents = documents
        self.name = name
        self.provider = provider
        self.public = public
        self.singleton = singleton
        self.source = source
        self.uid = uid

    def validate(self):
        if self.annotations:
            self.annotations.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.annotations is not None:
            result['annotations'] = self.annotations.to_map()
        if self.category is not None:
            result['category'] = self.category
        if self.description is not None:
            result['description'] = self.description
        if self.documents is not None:
            result['documents'] = self.documents
        if self.name is not None:
            result['name'] = self.name
        if self.provider is not None:
            result['provider'] = self.provider
        if self.public is not None:
            result['public'] = self.public
        if self.singleton is not None:
            result['singleton'] = self.singleton
        if self.source is not None:
            result['source'] = self.source
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('annotations') is not None:
            temp_model = ListComponentsResponseBodyDataListAnnotations()
            self.annotations = temp_model.from_map(m['annotations'])
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('documents') is not None:
            self.documents = m.get('documents')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('public') is not None:
            self.public = m.get('public')
        if m.get('singleton') is not None:
            self.singleton = m.get('singleton')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class ListComponentsResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[ListComponentsResponseBodyDataList] = None,
        page_num: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.list = list
        self.page_num = page_num
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListComponentsResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListComponentsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListComponentsResponseBodyData = None,
        msg: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = ListComponentsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class ListComponentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListComponentsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListComponentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEnvironmentLicensesRequest(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        scope: str = None,
        type: str = None,
    ):
        # 页码
        self.page_num = page_num
        # 页大小
        self.page_size = page_size
        self.scope = scope
        # 类型
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.scope is not None:
            result['scope'] = self.scope
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListEnvironmentLicensesResponseBodyDataListLicenseQuotaClusterQuota(TeaModel):
    def __init__(
        self,
        cpu_core_limit: int = None,
    ):
        # cpu核数限制
        self.cpu_core_limit = cpu_core_limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_core_limit is not None:
            result['cpuCoreLimit'] = self.cpu_core_limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cpuCoreLimit') is not None:
            self.cpu_core_limit = m.get('cpuCoreLimit')
        return self


class ListEnvironmentLicensesResponseBodyDataListLicenseQuotaComponentQuotas(TeaModel):
    def __init__(
        self,
        component_name: str = None,
        component_source: str = None,
        instance_limit: int = None,
    ):
        # 组件名
        self.component_name = component_name
        # 组件来源
        self.component_source = component_source
        # 实例数限制
        self.instance_limit = instance_limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_name is not None:
            result['componentName'] = self.component_name
        if self.component_source is not None:
            result['componentSource'] = self.component_source
        if self.instance_limit is not None:
            result['instanceLimit'] = self.instance_limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('componentName') is not None:
            self.component_name = m.get('componentName')
        if m.get('componentSource') is not None:
            self.component_source = m.get('componentSource')
        if m.get('instanceLimit') is not None:
            self.instance_limit = m.get('instanceLimit')
        return self


class ListEnvironmentLicensesResponseBodyDataListLicenseQuotaCustomQuotas(TeaModel):
    def __init__(
        self,
        description: str = None,
        key: str = None,
        value: str = None,
    ):
        self.description = description
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ListEnvironmentLicensesResponseBodyDataListLicenseQuota(TeaModel):
    def __init__(
        self,
        cluster_quota: ListEnvironmentLicensesResponseBodyDataListLicenseQuotaClusterQuota = None,
        component_quotas: List[ListEnvironmentLicensesResponseBodyDataListLicenseQuotaComponentQuotas] = None,
        custom_quotas: List[ListEnvironmentLicensesResponseBodyDataListLicenseQuotaCustomQuotas] = None,
    ):
        # 集群配额
        self.cluster_quota = cluster_quota
        # 组件配额
        self.component_quotas = component_quotas
        self.custom_quotas = custom_quotas

    def validate(self):
        if self.cluster_quota:
            self.cluster_quota.validate()
        if self.component_quotas:
            for k in self.component_quotas:
                if k:
                    k.validate()
        if self.custom_quotas:
            for k in self.custom_quotas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_quota is not None:
            result['clusterQuota'] = self.cluster_quota.to_map()
        result['componentQuotas'] = []
        if self.component_quotas is not None:
            for k in self.component_quotas:
                result['componentQuotas'].append(k.to_map() if k else None)
        result['customQuotas'] = []
        if self.custom_quotas is not None:
            for k in self.custom_quotas:
                result['customQuotas'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusterQuota') is not None:
            temp_model = ListEnvironmentLicensesResponseBodyDataListLicenseQuotaClusterQuota()
            self.cluster_quota = temp_model.from_map(m['clusterQuota'])
        self.component_quotas = []
        if m.get('componentQuotas') is not None:
            for k in m.get('componentQuotas'):
                temp_model = ListEnvironmentLicensesResponseBodyDataListLicenseQuotaComponentQuotas()
                self.component_quotas.append(temp_model.from_map(k))
        self.custom_quotas = []
        if m.get('customQuotas') is not None:
            for k in m.get('customQuotas'):
                temp_model = ListEnvironmentLicensesResponseBodyDataListLicenseQuotaCustomQuotas()
                self.custom_quotas.append(temp_model.from_map(k))
        return self


class ListEnvironmentLicensesResponseBodyDataList(TeaModel):
    def __init__(
        self,
        expire_time: str = None,
        license_key: str = None,
        license_quota: ListEnvironmentLicensesResponseBodyDataListLicenseQuota = None,
        product_version_uid: str = None,
        reject_reason: str = None,
        scope: str = None,
        status: str = None,
        type: str = None,
        uid: str = None,
    ):
        # 过期时间
        self.expire_time = expire_time
        # license内容
        self.license_key = license_key
        # license配额
        self.license_quota = license_quota
        self.product_version_uid = product_version_uid
        # 拒绝原因
        self.reject_reason = reject_reason
        self.scope = scope
        # 状态
        self.status = status
        # 类型
        self.type = type
        # license uid
        self.uid = uid

    def validate(self):
        if self.license_quota:
            self.license_quota.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expire_time is not None:
            result['expireTime'] = self.expire_time
        if self.license_key is not None:
            result['licenseKey'] = self.license_key
        if self.license_quota is not None:
            result['licenseQuota'] = self.license_quota.to_map()
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        if self.reject_reason is not None:
            result['rejectReason'] = self.reject_reason
        if self.scope is not None:
            result['scope'] = self.scope
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')
        if m.get('licenseKey') is not None:
            self.license_key = m.get('licenseKey')
        if m.get('licenseQuota') is not None:
            temp_model = ListEnvironmentLicensesResponseBodyDataListLicenseQuota()
            self.license_quota = temp_model.from_map(m['licenseQuota'])
        if m.get('productVersionUID') is not None:
            self.product_version_uid = m.get('productVersionUID')
        if m.get('rejectReason') is not None:
            self.reject_reason = m.get('rejectReason')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class ListEnvironmentLicensesResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[ListEnvironmentLicensesResponseBodyDataList] = None,
        page_num: int = None,
        page_size: int = None,
        total: int = None,
    ):
        # license列表
        self.list = list
        # 页码
        self.page_num = page_num
        # 页大小
        self.page_size = page_size
        # 总数
        self.total = total

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListEnvironmentLicensesResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListEnvironmentLicensesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListEnvironmentLicensesResponseBodyData = None,
        msg: str = None,
    ):
        # 错误码
        self.code = code
        # 业务数据
        self.data = data
        # 错误信息
        self.msg = msg

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = ListEnvironmentLicensesResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class ListEnvironmentLicensesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListEnvironmentLicensesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListEnvironmentLicensesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEnvironmentNodesRequest(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
    ):
        self.page_num = page_num
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListEnvironmentNodesResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[InstanceInfo] = None,
        page_num: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.list = list
        self.page_num = page_num
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = InstanceInfo()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListEnvironmentNodesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListEnvironmentNodesResponseBodyData = None,
        msg: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = ListEnvironmentNodesResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class ListEnvironmentNodesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListEnvironmentNodesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListEnvironmentNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEnvironmentTunnelsResponseBodyDataListTunnelConfig(TeaModel):
    def __init__(
        self,
        hostname: str = None,
        password: str = None,
        region_id: str = None,
        ssh_port: int = None,
        username: str = None,
        vpc_id: str = None,
    ):
        # 跳板机hostname
        self.hostname = hostname
        # 跳板机密码
        self.password = password
        # 直连regionId
        self.region_id = region_id
        # 跳板机ssh端口号
        self.ssh_port = ssh_port
        # 跳板机用户名
        self.username = username
        # 直连vpcId
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hostname is not None:
            result['hostname'] = self.hostname
        if self.password is not None:
            result['password'] = self.password
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.ssh_port is not None:
            result['sshPort'] = self.ssh_port
        if self.username is not None:
            result['username'] = self.username
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hostname') is not None:
            self.hostname = m.get('hostname')
        if m.get('password') is not None:
            self.password = m.get('password')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('sshPort') is not None:
            self.ssh_port = m.get('sshPort')
        if m.get('username') is not None:
            self.username = m.get('username')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        return self


class ListEnvironmentTunnelsResponseBodyDataList(TeaModel):
    def __init__(
        self,
        tunnel_config: ListEnvironmentTunnelsResponseBodyDataListTunnelConfig = None,
        tunnel_type: str = None,
    ):
        self.tunnel_config = tunnel_config
        # 通道类型
        self.tunnel_type = tunnel_type

    def validate(self):
        if self.tunnel_config:
            self.tunnel_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tunnel_config is not None:
            result['tunnelConfig'] = self.tunnel_config.to_map()
        if self.tunnel_type is not None:
            result['tunnelType'] = self.tunnel_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tunnelConfig') is not None:
            temp_model = ListEnvironmentTunnelsResponseBodyDataListTunnelConfig()
            self.tunnel_config = temp_model.from_map(m['tunnelConfig'])
        if m.get('tunnelType') is not None:
            self.tunnel_type = m.get('tunnelType')
        return self


class ListEnvironmentTunnelsResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[ListEnvironmentTunnelsResponseBodyDataList] = None,
    ):
        self.list = list

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListEnvironmentTunnelsResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        return self


class ListEnvironmentTunnelsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListEnvironmentTunnelsResponseBodyData = None,
        msg: str = None,
    ):
        # 错误码
        self.code = code
        self.data = data
        # 错误信息
        self.msg = msg

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = ListEnvironmentTunnelsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class ListEnvironmentTunnelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListEnvironmentTunnelsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListEnvironmentTunnelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEnvironmentsRequest(TeaModel):
    def __init__(
        self,
        cluster_uid: str = None,
        foundation_type: str = None,
        fuzzy: str = None,
        instance_status: str = None,
        name: str = None,
        page_num: int = None,
        page_size: int = None,
        type: str = None,
        vendor_type: str = None,
    ):
        self.cluster_uid = cluster_uid
        self.foundation_type = foundation_type
        self.fuzzy = fuzzy
        self.instance_status = instance_status
        self.name = name
        self.page_num = page_num
        self.page_size = page_size
        self.type = type
        self.vendor_type = vendor_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_uid is not None:
            result['clusterUID'] = self.cluster_uid
        if self.foundation_type is not None:
            result['foundationType'] = self.foundation_type
        if self.fuzzy is not None:
            result['fuzzy'] = self.fuzzy
        if self.instance_status is not None:
            result['instanceStatus'] = self.instance_status
        if self.name is not None:
            result['name'] = self.name
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.type is not None:
            result['type'] = self.type
        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusterUID') is not None:
            self.cluster_uid = m.get('clusterUID')
        if m.get('foundationType') is not None:
            self.foundation_type = m.get('foundationType')
        if m.get('fuzzy') is not None:
            self.fuzzy = m.get('fuzzy')
        if m.get('instanceStatus') is not None:
            self.instance_status = m.get('instanceStatus')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')
        return self


class ListEnvironmentsResponseBodyDataListPlatform(TeaModel):
    def __init__(
        self,
        architecture: str = None,
        os: str = None,
    ):
        self.architecture = architecture
        self.os = os

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture is not None:
            result['architecture'] = self.architecture
        if self.os is not None:
            result['os'] = self.os
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('architecture') is not None:
            self.architecture = m.get('architecture')
        if m.get('os') is not None:
            self.os = m.get('os')
        return self


class ListEnvironmentsResponseBodyDataList(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        description: str = None,
        location: str = None,
        name: str = None,
        platform: ListEnvironmentsResponseBodyDataListPlatform = None,
        platform_list: List[Platform] = None,
        product_name: str = None,
        product_version: str = None,
        product_version_uid: str = None,
        uid: str = None,
        vendor_type: str = None,
    ):
        self.created_at = created_at
        self.description = description
        self.location = location
        self.name = name
        self.platform = platform
        self.platform_list = platform_list
        self.product_name = product_name
        self.product_version = product_version
        self.product_version_uid = product_version_uid
        self.uid = uid
        self.vendor_type = vendor_type

    def validate(self):
        if self.platform:
            self.platform.validate()
        if self.platform_list:
            for k in self.platform_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.location is not None:
            result['location'] = self.location
        if self.name is not None:
            result['name'] = self.name
        if self.platform is not None:
            result['platform'] = self.platform.to_map()
        result['platformList'] = []
        if self.platform_list is not None:
            for k in self.platform_list:
                result['platformList'].append(k.to_map() if k else None)
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.product_version is not None:
            result['productVersion'] = self.product_version
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        if self.uid is not None:
            result['uid'] = self.uid
        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('platform') is not None:
            temp_model = ListEnvironmentsResponseBodyDataListPlatform()
            self.platform = temp_model.from_map(m['platform'])
        self.platform_list = []
        if m.get('platformList') is not None:
            for k in m.get('platformList'):
                temp_model = Platform()
                self.platform_list.append(temp_model.from_map(k))
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('productVersion') is not None:
            self.product_version = m.get('productVersion')
        if m.get('productVersionUID') is not None:
            self.product_version_uid = m.get('productVersionUID')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')
        return self


class ListEnvironmentsResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[ListEnvironmentsResponseBodyDataList] = None,
        page_num: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.list = list
        self.page_num = page_num
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListEnvironmentsResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListEnvironmentsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListEnvironmentsResponseBodyData = None,
        msg: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = ListEnvironmentsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class ListEnvironmentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListEnvironmentsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListEnvironmentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFoundationComponentVersionsResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[ComponentVersion] = None,
        page_num: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.list = list
        self.page_num = page_num
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ComponentVersion()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListFoundationComponentVersionsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListFoundationComponentVersionsResponseBodyData = None,
        msg: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = ListFoundationComponentVersionsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class ListFoundationComponentVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFoundationComponentVersionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListFoundationComponentVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFoundationReferenceComponentsRequest(TeaModel):
    def __init__(
        self,
        foundation_reference_uid: str = None,
        foundation_version_uid: str = None,
        only_enabled: bool = None,
        product_version_uid: str = None,
    ):
        self.foundation_reference_uid = foundation_reference_uid
        # foundation version uid
        self.foundation_version_uid = foundation_version_uid
        self.only_enabled = only_enabled
        # 产品版本uid
        self.product_version_uid = product_version_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.foundation_reference_uid is not None:
            result['foundationReferenceUID'] = self.foundation_reference_uid
        if self.foundation_version_uid is not None:
            result['foundationVersionUID'] = self.foundation_version_uid
        if self.only_enabled is not None:
            result['onlyEnabled'] = self.only_enabled
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('foundationReferenceUID') is not None:
            self.foundation_reference_uid = m.get('foundationReferenceUID')
        if m.get('foundationVersionUID') is not None:
            self.foundation_version_uid = m.get('foundationVersionUID')
        if m.get('onlyEnabled') is not None:
            self.only_enabled = m.get('onlyEnabled')
        if m.get('productVersionUID') is not None:
            self.product_version_uid = m.get('productVersionUID')
        return self


class ListFoundationReferenceComponentsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ProductComponentRelationDetail] = None,
        msg: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ProductComponentRelationDetail()
                self.data.append(temp_model.from_map(k))
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class ListFoundationReferenceComponentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFoundationReferenceComponentsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListFoundationReferenceComponentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFoundationVersionsResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[FoundationVersion] = None,
    ):
        self.list = list

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = FoundationVersion()
                self.list.append(temp_model.from_map(k))
        return self


class ListFoundationVersionsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListFoundationVersionsResponseBodyData = None,
        msg: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = ListFoundationVersionsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class ListFoundationVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFoundationVersionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListFoundationVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProductComponentVersionsRequest(TeaModel):
    def __init__(
        self,
        category: str = None,
        page_num: str = None,
        page_size: str = None,
        sort_direct: str = None,
        sort_key: str = None,
    ):
        # 组件类型，不填写则为全部
        self.category = category
        self.page_num = page_num
        self.page_size = page_size
        self.sort_direct = sort_direct
        self.sort_key = sort_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.sort_direct is not None:
            result['sortDirect'] = self.sort_direct
        if self.sort_key is not None:
            result['sortKey'] = self.sort_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('sortDirect') is not None:
            self.sort_direct = m.get('sortDirect')
        if m.get('sortKey') is not None:
            self.sort_key = m.get('sortKey')
        return self


class ListProductComponentVersionsResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[ProductComponentRelationDetail] = None,
        page_num: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.list = list
        self.page_num = page_num
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ProductComponentRelationDetail()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListProductComponentVersionsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListProductComponentVersionsResponseBodyData = None,
        msg: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = ListProductComponentVersionsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class ListProductComponentVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListProductComponentVersionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListProductComponentVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProductDeploymentsRequest(TeaModel):
    def __init__(
        self,
        environment_uid: str = None,
        page_num: int = None,
        page_size: int = None,
        product_version_uid: str = None,
    ):
        self.environment_uid = environment_uid
        self.page_num = page_num
        self.page_size = page_size
        self.product_version_uid = product_version_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.environment_uid is not None:
            result['environmentUID'] = self.environment_uid
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('environmentUID') is not None:
            self.environment_uid = m.get('environmentUID')
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('productVersionUID') is not None:
            self.product_version_uid = m.get('productVersionUID')
        return self


class ListProductDeploymentsResponseBodyDataList(TeaModel):
    def __init__(
        self,
        env_params: str = None,
        env_uid: str = None,
        old_product_version: str = None,
        package_content_type: str = None,
        package_info_uid: str = None,
        package_type: str = None,
        product_name: str = None,
        product_version: str = None,
        status: str = None,
        uid: str = None,
    ):
        self.env_params = env_params
        self.env_uid = env_uid
        self.old_product_version = old_product_version
        self.package_content_type = package_content_type
        self.package_info_uid = package_info_uid
        self.package_type = package_type
        self.product_name = product_name
        self.product_version = product_version
        self.status = status
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env_params is not None:
            result['envParams'] = self.env_params
        if self.env_uid is not None:
            result['envUID'] = self.env_uid
        if self.old_product_version is not None:
            result['oldProductVersion'] = self.old_product_version
        if self.package_content_type is not None:
            result['packageContentType'] = self.package_content_type
        if self.package_info_uid is not None:
            result['packageInfoUID'] = self.package_info_uid
        if self.package_type is not None:
            result['packageType'] = self.package_type
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.product_version is not None:
            result['productVersion'] = self.product_version
        if self.status is not None:
            result['status'] = self.status
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('envParams') is not None:
            self.env_params = m.get('envParams')
        if m.get('envUID') is not None:
            self.env_uid = m.get('envUID')
        if m.get('oldProductVersion') is not None:
            self.old_product_version = m.get('oldProductVersion')
        if m.get('packageContentType') is not None:
            self.package_content_type = m.get('packageContentType')
        if m.get('packageInfoUID') is not None:
            self.package_info_uid = m.get('packageInfoUID')
        if m.get('packageType') is not None:
            self.package_type = m.get('packageType')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('productVersion') is not None:
            self.product_version = m.get('productVersion')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class ListProductDeploymentsResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[ListProductDeploymentsResponseBodyDataList] = None,
        page_num: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.list = list
        self.page_num = page_num
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListProductDeploymentsResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListProductDeploymentsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListProductDeploymentsResponseBodyData = None,
        msg: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = ListProductDeploymentsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class ListProductDeploymentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListProductDeploymentsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListProductDeploymentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProductEnvironmentsRequestPlatforms(TeaModel):
    def __init__(
        self,
        architecture: str = None,
        os: str = None,
    ):
        self.architecture = architecture
        self.os = os

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture is not None:
            result['architecture'] = self.architecture
        if self.os is not None:
            result['os'] = self.os
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('architecture') is not None:
            self.architecture = m.get('architecture')
        if m.get('os') is not None:
            self.os = m.get('os')
        return self


class ListProductEnvironmentsRequest(TeaModel):
    def __init__(
        self,
        compatible_product_version_uid: str = None,
        env_type: str = None,
        platforms: List[ListProductEnvironmentsRequestPlatforms] = None,
        product_version_uid: str = None,
    ):
        # 兼容版本产品版本id
        self.compatible_product_version_uid = compatible_product_version_uid
        self.env_type = env_type
        self.platforms = platforms
        self.product_version_uid = product_version_uid

    def validate(self):
        if self.platforms:
            for k in self.platforms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compatible_product_version_uid is not None:
            result['compatibleProductVersionUID'] = self.compatible_product_version_uid
        if self.env_type is not None:
            result['envType'] = self.env_type
        result['platforms'] = []
        if self.platforms is not None:
            for k in self.platforms:
                result['platforms'].append(k.to_map() if k else None)
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('compatibleProductVersionUID') is not None:
            self.compatible_product_version_uid = m.get('compatibleProductVersionUID')
        if m.get('envType') is not None:
            self.env_type = m.get('envType')
        self.platforms = []
        if m.get('platforms') is not None:
            for k in m.get('platforms'):
                temp_model = ListProductEnvironmentsRequestPlatforms()
                self.platforms.append(temp_model.from_map(k))
        if m.get('productVersionUID') is not None:
            self.product_version_uid = m.get('productVersionUID')
        return self


class ListProductEnvironmentsShrinkRequest(TeaModel):
    def __init__(
        self,
        compatible_product_version_uid: str = None,
        env_type: str = None,
        platforms_shrink: str = None,
        product_version_uid: str = None,
    ):
        # 兼容版本产品版本id
        self.compatible_product_version_uid = compatible_product_version_uid
        self.env_type = env_type
        self.platforms_shrink = platforms_shrink
        self.product_version_uid = product_version_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compatible_product_version_uid is not None:
            result['compatibleProductVersionUID'] = self.compatible_product_version_uid
        if self.env_type is not None:
            result['envType'] = self.env_type
        if self.platforms_shrink is not None:
            result['platforms'] = self.platforms_shrink
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('compatibleProductVersionUID') is not None:
            self.compatible_product_version_uid = m.get('compatibleProductVersionUID')
        if m.get('envType') is not None:
            self.env_type = m.get('envType')
        if m.get('platforms') is not None:
            self.platforms_shrink = m.get('platforms')
        if m.get('productVersionUID') is not None:
            self.product_version_uid = m.get('productVersionUID')
        return self


class ListProductEnvironmentsResponseBodyData(TeaModel):
    def __init__(
        self,
        env_name: str = None,
        env_type: str = None,
        env_uid: str = None,
        instance_status: str = None,
        old_product_version: str = None,
        old_product_version_uid: str = None,
        platform_status: str = None,
        product_name: str = None,
        product_uid: str = None,
        product_version: str = None,
        product_version_uid: str = None,
        provider: str = None,
        uid: str = None,
        vendor_config: str = None,
        vendor_type: str = None,
    ):
        self.env_name = env_name
        self.env_type = env_type
        self.env_uid = env_uid
        self.instance_status = instance_status
        self.old_product_version = old_product_version
        self.old_product_version_uid = old_product_version_uid
        self.platform_status = platform_status
        self.product_name = product_name
        self.product_uid = product_uid
        self.product_version = product_version
        self.product_version_uid = product_version_uid
        self.provider = provider
        self.uid = uid
        self.vendor_config = vendor_config
        self.vendor_type = vendor_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env_name is not None:
            result['envName'] = self.env_name
        if self.env_type is not None:
            result['envType'] = self.env_type
        if self.env_uid is not None:
            result['envUID'] = self.env_uid
        if self.instance_status is not None:
            result['instanceStatus'] = self.instance_status
        if self.old_product_version is not None:
            result['oldProductVersion'] = self.old_product_version
        if self.old_product_version_uid is not None:
            result['oldProductVersionUID'] = self.old_product_version_uid
        if self.platform_status is not None:
            result['platformStatus'] = self.platform_status
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.product_uid is not None:
            result['productUID'] = self.product_uid
        if self.product_version is not None:
            result['productVersion'] = self.product_version
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        if self.provider is not None:
            result['provider'] = self.provider
        if self.uid is not None:
            result['uid'] = self.uid
        if self.vendor_config is not None:
            result['vendorConfig'] = self.vendor_config
        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('envName') is not None:
            self.env_name = m.get('envName')
        if m.get('envType') is not None:
            self.env_type = m.get('envType')
        if m.get('envUID') is not None:
            self.env_uid = m.get('envUID')
        if m.get('instanceStatus') is not None:
            self.instance_status = m.get('instanceStatus')
        if m.get('oldProductVersion') is not None:
            self.old_product_version = m.get('oldProductVersion')
        if m.get('oldProductVersionUID') is not None:
            self.old_product_version_uid = m.get('oldProductVersionUID')
        if m.get('platformStatus') is not None:
            self.platform_status = m.get('platformStatus')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('productUID') is not None:
            self.product_uid = m.get('productUID')
        if m.get('productVersion') is not None:
            self.product_version = m.get('productVersion')
        if m.get('productVersionUID') is not None:
            self.product_version_uid = m.get('productVersionUID')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('vendorConfig') is not None:
            self.vendor_config = m.get('vendorConfig')
        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')
        return self


class ListProductEnvironmentsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListProductEnvironmentsResponseBodyData] = None,
        msg: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListProductEnvironmentsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class ListProductEnvironmentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListProductEnvironmentsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListProductEnvironmentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProductFoundationReferencesResponseBodyData(TeaModel):
    def __init__(
        self,
        foundation_reference_uid: str = None,
        foundation_version: str = None,
        foundation_version_name: str = None,
        foundation_version_type: str = None,
        foundation_version_uid: str = None,
        product_version_uid: str = None,
    ):
        self.foundation_reference_uid = foundation_reference_uid
        self.foundation_version = foundation_version
        self.foundation_version_name = foundation_version_name
        self.foundation_version_type = foundation_version_type
        self.foundation_version_uid = foundation_version_uid
        self.product_version_uid = product_version_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.foundation_reference_uid is not None:
            result['foundationReferenceUID'] = self.foundation_reference_uid
        if self.foundation_version is not None:
            result['foundationVersion'] = self.foundation_version
        if self.foundation_version_name is not None:
            result['foundationVersionName'] = self.foundation_version_name
        if self.foundation_version_type is not None:
            result['foundationVersionType'] = self.foundation_version_type
        if self.foundation_version_uid is not None:
            result['foundationVersionUID'] = self.foundation_version_uid
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('foundationReferenceUID') is not None:
            self.foundation_reference_uid = m.get('foundationReferenceUID')
        if m.get('foundationVersion') is not None:
            self.foundation_version = m.get('foundationVersion')
        if m.get('foundationVersionName') is not None:
            self.foundation_version_name = m.get('foundationVersionName')
        if m.get('foundationVersionType') is not None:
            self.foundation_version_type = m.get('foundationVersionType')
        if m.get('foundationVersionUID') is not None:
            self.foundation_version_uid = m.get('foundationVersionUID')
        if m.get('productVersionUID') is not None:
            self.product_version_uid = m.get('productVersionUID')
        return self


class ListProductFoundationReferencesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListProductFoundationReferencesResponseBodyData] = None,
        msg: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListProductFoundationReferencesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class ListProductFoundationReferencesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListProductFoundationReferencesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListProductFoundationReferencesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProductInstanceConfigsRequest(TeaModel):
    def __init__(
        self,
        environment_uid: str = None,
        page_num: int = None,
        page_size: int = None,
        param_type: str = None,
        product_version_uid: str = None,
    ):
        self.environment_uid = environment_uid
        self.page_num = page_num
        self.page_size = page_size
        # 组件和全局类型字段
        self.param_type = param_type
        self.product_version_uid = product_version_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.environment_uid is not None:
            result['environmentUID'] = self.environment_uid
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.param_type is not None:
            result['paramType'] = self.param_type
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('environmentUID') is not None:
            self.environment_uid = m.get('environmentUID')
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('paramType') is not None:
            self.param_type = m.get('paramType')
        if m.get('productVersionUID') is not None:
            self.product_version_uid = m.get('productVersionUID')
        return self


class ListProductInstanceConfigsResponseBodyDataList(TeaModel):
    def __init__(
        self,
        component_name: str = None,
        component_release_name: str = None,
        component_uid: str = None,
        component_version_uid: str = None,
        created_at: str = None,
        description: str = None,
        env_uid: str = None,
        name: str = None,
        parent_component_name: str = None,
        parent_component_release_name: str = None,
        parent_component_version_uid: str = None,
        product_name: str = None,
        product_version: str = None,
        product_version_uid: str = None,
        uid: str = None,
        value: str = None,
        value_type: str = None,
        vendor_type: str = None,
    ):
        self.component_name = component_name
        self.component_release_name = component_release_name
        self.component_uid = component_uid
        self.component_version_uid = component_version_uid
        self.created_at = created_at
        self.description = description
        self.env_uid = env_uid
        self.name = name
        self.parent_component_name = parent_component_name
        self.parent_component_release_name = parent_component_release_name
        self.parent_component_version_uid = parent_component_version_uid
        self.product_name = product_name
        self.product_version = product_version
        self.product_version_uid = product_version_uid
        self.uid = uid
        self.value = value
        self.value_type = value_type
        self.vendor_type = vendor_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_name is not None:
            result['componentName'] = self.component_name
        if self.component_release_name is not None:
            result['componentReleaseName'] = self.component_release_name
        if self.component_uid is not None:
            result['componentUID'] = self.component_uid
        if self.component_version_uid is not None:
            result['componentVersionUID'] = self.component_version_uid
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.env_uid is not None:
            result['envUID'] = self.env_uid
        if self.name is not None:
            result['name'] = self.name
        if self.parent_component_name is not None:
            result['parentComponentName'] = self.parent_component_name
        if self.parent_component_release_name is not None:
            result['parentComponentReleaseName'] = self.parent_component_release_name
        if self.parent_component_version_uid is not None:
            result['parentComponentVersionUID'] = self.parent_component_version_uid
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.product_version is not None:
            result['productVersion'] = self.product_version
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        if self.uid is not None:
            result['uid'] = self.uid
        if self.value is not None:
            result['value'] = self.value
        if self.value_type is not None:
            result['valueType'] = self.value_type
        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('componentName') is not None:
            self.component_name = m.get('componentName')
        if m.get('componentReleaseName') is not None:
            self.component_release_name = m.get('componentReleaseName')
        if m.get('componentUID') is not None:
            self.component_uid = m.get('componentUID')
        if m.get('componentVersionUID') is not None:
            self.component_version_uid = m.get('componentVersionUID')
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('envUID') is not None:
            self.env_uid = m.get('envUID')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parentComponentName') is not None:
            self.parent_component_name = m.get('parentComponentName')
        if m.get('parentComponentReleaseName') is not None:
            self.parent_component_release_name = m.get('parentComponentReleaseName')
        if m.get('parentComponentVersionUID') is not None:
            self.parent_component_version_uid = m.get('parentComponentVersionUID')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('productVersion') is not None:
            self.product_version = m.get('productVersion')
        if m.get('productVersionUID') is not None:
            self.product_version_uid = m.get('productVersionUID')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('valueType') is not None:
            self.value_type = m.get('valueType')
        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')
        return self


class ListProductInstanceConfigsResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[ListProductInstanceConfigsResponseBodyDataList] = None,
        page_num: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.list = list
        self.page_num = page_num
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListProductInstanceConfigsResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListProductInstanceConfigsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListProductInstanceConfigsResponseBodyData = None,
        msg: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = ListProductInstanceConfigsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class ListProductInstanceConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListProductInstanceConfigsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListProductInstanceConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProductInstancesRequest(TeaModel):
    def __init__(
        self,
        env_uid: str = None,
        page_num: str = None,
        page_size: str = None,
        product_version_uid: str = None,
    ):
        self.env_uid = env_uid
        self.page_num = page_num
        self.page_size = page_size
        self.product_version_uid = product_version_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env_uid is not None:
            result['envUID'] = self.env_uid
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('envUID') is not None:
            self.env_uid = m.get('envUID')
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('productVersionUID') is not None:
            self.product_version_uid = m.get('productVersionUID')
        return self


class ListProductInstancesResponseBodyDataList(TeaModel):
    def __init__(
        self,
        product_name: str = None,
        product_version: str = None,
        product_version_uid: str = None,
        status: str = None,
        uid: str = None,
    ):
        self.product_name = product_name
        self.product_version = product_version
        self.product_version_uid = product_version_uid
        self.status = status
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.product_version is not None:
            result['productVersion'] = self.product_version
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        if self.status is not None:
            result['status'] = self.status
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('productVersion') is not None:
            self.product_version = m.get('productVersion')
        if m.get('productVersionUID') is not None:
            self.product_version_uid = m.get('productVersionUID')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class ListProductInstancesResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[ListProductInstancesResponseBodyDataList] = None,
    ):
        self.list = list

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListProductInstancesResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        return self


class ListProductInstancesResponseBody(TeaModel):
    def __init__(
        self,
        data: ListProductInstancesResponseBodyData = None,
    ):
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListProductInstancesResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        return self


class ListProductInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListProductInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListProductInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProductVersionConfigsRequest(TeaModel):
    def __init__(
        self,
        config_type: str = None,
        page_num: str = None,
        page_size: str = None,
    ):
        self.config_type = config_type
        self.page_num = page_num
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_type is not None:
            result['configType'] = self.config_type
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configType') is not None:
            self.config_type = m.get('configType')
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListProductVersionConfigsResponseBodyDataList(TeaModel):
    def __init__(
        self,
        component_name: str = None,
        component_release_name: str = None,
        component_version_uid: str = None,
        description: str = None,
        name: str = None,
        parent_component_name: str = None,
        parent_component_release_name: str = None,
        parent_component_version_uid: str = None,
        product_version_uid: str = None,
        uid: str = None,
        value: str = None,
    ):
        self.component_name = component_name
        self.component_release_name = component_release_name
        self.component_version_uid = component_version_uid
        self.description = description
        self.name = name
        self.parent_component_name = parent_component_name
        self.parent_component_release_name = parent_component_release_name
        self.parent_component_version_uid = parent_component_version_uid
        self.product_version_uid = product_version_uid
        self.uid = uid
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_name is not None:
            result['componentName'] = self.component_name
        if self.component_release_name is not None:
            result['componentReleaseName'] = self.component_release_name
        if self.component_version_uid is not None:
            result['componentVersionUID'] = self.component_version_uid
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.parent_component_name is not None:
            result['parentComponentName'] = self.parent_component_name
        if self.parent_component_release_name is not None:
            result['parentComponentReleaseName'] = self.parent_component_release_name
        if self.parent_component_version_uid is not None:
            result['parentComponentVersionUID'] = self.parent_component_version_uid
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        if self.uid is not None:
            result['uid'] = self.uid
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('componentName') is not None:
            self.component_name = m.get('componentName')
        if m.get('componentReleaseName') is not None:
            self.component_release_name = m.get('componentReleaseName')
        if m.get('componentVersionUID') is not None:
            self.component_version_uid = m.get('componentVersionUID')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parentComponentName') is not None:
            self.parent_component_name = m.get('parentComponentName')
        if m.get('parentComponentReleaseName') is not None:
            self.parent_component_release_name = m.get('parentComponentReleaseName')
        if m.get('parentComponentVersionUID') is not None:
            self.parent_component_version_uid = m.get('parentComponentVersionUID')
        if m.get('productVersionUID') is not None:
            self.product_version_uid = m.get('productVersionUID')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ListProductVersionConfigsResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[ListProductVersionConfigsResponseBodyDataList] = None,
        page_num: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.list = list
        self.page_num = page_num
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListProductVersionConfigsResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListProductVersionConfigsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListProductVersionConfigsResponseBodyData = None,
        msg: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = ListProductVersionConfigsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class ListProductVersionConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListProductVersionConfigsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListProductVersionConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProductVersionsRequestPlatforms(TeaModel):
    def __init__(
        self,
        architecture: str = None,
        os: str = None,
    ):
        self.architecture = architecture
        self.os = os

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture is not None:
            result['architecture'] = self.architecture
        if self.os is not None:
            result['os'] = self.os
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('architecture') is not None:
            self.architecture = m.get('architecture')
        if m.get('os') is not None:
            self.os = m.get('os')
        return self


class ListProductVersionsRequest(TeaModel):
    def __init__(
        self,
        page_num: str = None,
        page_size: str = None,
        platforms: List[ListProductVersionsRequestPlatforms] = None,
        product_name: str = None,
        product_uid: str = None,
        released: bool = None,
        supported_foundation_types: List[str] = None,
        version: str = None,
    ):
        self.page_num = page_num
        self.page_size = page_size
        # 支持的platform，为空则不过滤
        self.platforms = platforms
        # 过滤参数，产品名称
        self.product_name = product_name
        # 过滤参数，产品uid
        self.product_uid = product_uid
        # 过滤参数，是否已发布
        self.released = released
        # 过滤参数，支持的环境类型
        self.supported_foundation_types = supported_foundation_types
        # 过滤参数，产品版本号
        self.version = version

    def validate(self):
        if self.platforms:
            for k in self.platforms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        result['platforms'] = []
        if self.platforms is not None:
            for k in self.platforms:
                result['platforms'].append(k.to_map() if k else None)
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.product_uid is not None:
            result['productUID'] = self.product_uid
        if self.released is not None:
            result['released'] = self.released
        if self.supported_foundation_types is not None:
            result['supportedFoundationTypes'] = self.supported_foundation_types
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        self.platforms = []
        if m.get('platforms') is not None:
            for k in m.get('platforms'):
                temp_model = ListProductVersionsRequestPlatforms()
                self.platforms.append(temp_model.from_map(k))
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('productUID') is not None:
            self.product_uid = m.get('productUID')
        if m.get('released') is not None:
            self.released = m.get('released')
        if m.get('supportedFoundationTypes') is not None:
            self.supported_foundation_types = m.get('supportedFoundationTypes')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ListProductVersionsShrinkRequest(TeaModel):
    def __init__(
        self,
        page_num: str = None,
        page_size: str = None,
        platforms_shrink: str = None,
        product_name: str = None,
        product_uid: str = None,
        released: bool = None,
        supported_foundation_types_shrink: str = None,
        version: str = None,
    ):
        self.page_num = page_num
        self.page_size = page_size
        # 支持的platform，为空则不过滤
        self.platforms_shrink = platforms_shrink
        # 过滤参数，产品名称
        self.product_name = product_name
        # 过滤参数，产品uid
        self.product_uid = product_uid
        # 过滤参数，是否已发布
        self.released = released
        # 过滤参数，支持的环境类型
        self.supported_foundation_types_shrink = supported_foundation_types_shrink
        # 过滤参数，产品版本号
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.platforms_shrink is not None:
            result['platforms'] = self.platforms_shrink
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.product_uid is not None:
            result['productUID'] = self.product_uid
        if self.released is not None:
            result['released'] = self.released
        if self.supported_foundation_types_shrink is not None:
            result['supportedFoundationTypes'] = self.supported_foundation_types_shrink
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('platforms') is not None:
            self.platforms_shrink = m.get('platforms')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('productUID') is not None:
            self.product_uid = m.get('productUID')
        if m.get('released') is not None:
            self.released = m.get('released')
        if m.get('supportedFoundationTypes') is not None:
            self.supported_foundation_types_shrink = m.get('supportedFoundationTypes')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ListProductVersionsResponseBodyDataListAnnotations(TeaModel):
    def __init__(
        self,
        additional_prop_1: str = None,
        additional_prop_2: str = None,
        additional_prop_3: str = None,
    ):
        self.additional_prop_1 = additional_prop_1
        self.additional_prop_2 = additional_prop_2
        self.additional_prop_3 = additional_prop_3

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.additional_prop_1 is not None:
            result['additionalProp1'] = self.additional_prop_1
        if self.additional_prop_2 is not None:
            result['additionalProp2'] = self.additional_prop_2
        if self.additional_prop_3 is not None:
            result['additionalProp3'] = self.additional_prop_3
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('additionalProp1') is not None:
            self.additional_prop_1 = m.get('additionalProp1')
        if m.get('additionalProp2') is not None:
            self.additional_prop_2 = m.get('additionalProp2')
        if m.get('additionalProp3') is not None:
            self.additional_prop_3 = m.get('additionalProp3')
        return self


class ListProductVersionsResponseBodyDataList(TeaModel):
    def __init__(
        self,
        annotations: ListProductVersionsResponseBodyDataListAnnotations = None,
        description: str = None,
        package_url: str = None,
        product_name: str = None,
        product_uid: str = None,
        provider: str = None,
        uid: str = None,
        version: str = None,
    ):
        self.annotations = annotations
        self.description = description
        self.package_url = package_url
        self.product_name = product_name
        self.product_uid = product_uid
        self.provider = provider
        self.uid = uid
        self.version = version

    def validate(self):
        if self.annotations:
            self.annotations.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.annotations is not None:
            result['annotations'] = self.annotations.to_map()
        if self.description is not None:
            result['description'] = self.description
        if self.package_url is not None:
            result['packageURL'] = self.package_url
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.product_uid is not None:
            result['productUID'] = self.product_uid
        if self.provider is not None:
            result['provider'] = self.provider
        if self.uid is not None:
            result['uid'] = self.uid
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('annotations') is not None:
            temp_model = ListProductVersionsResponseBodyDataListAnnotations()
            self.annotations = temp_model.from_map(m['annotations'])
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('packageURL') is not None:
            self.package_url = m.get('packageURL')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('productUID') is not None:
            self.product_uid = m.get('productUID')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ListProductVersionsResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[ListProductVersionsResponseBodyDataList] = None,
        page_num: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.list = list
        self.page_num = page_num
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListProductVersionsResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListProductVersionsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListProductVersionsResponseBodyData = None,
        msg: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = ListProductVersionsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class ListProductVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListProductVersionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListProductVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProductsRequest(TeaModel):
    def __init__(
        self,
        fuzzy: str = None,
        name: str = None,
        page_num: int = None,
        page_size: int = None,
    ):
        self.fuzzy = fuzzy
        self.name = name
        self.page_num = page_num
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fuzzy is not None:
            result['fuzzy'] = self.fuzzy
        if self.name is not None:
            result['name'] = self.name
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fuzzy') is not None:
            self.fuzzy = m.get('fuzzy')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListProductsResponseBodyDataList(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        uid: str = None,
    ):
        self.description = description
        self.name = name
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class ListProductsResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[ListProductsResponseBodyDataList] = None,
        page_num: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.list = list
        self.page_num = page_num
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListProductsResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListProductsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListProductsResponseBodyData = None,
        msg: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = ListProductsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class ListProductsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListProductsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListProductsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListWorkflowTaskLogsRequest(TeaModel):
    def __init__(
        self,
        filter_values: List[str] = None,
        order_type: str = None,
        page_num: int = None,
        page_size: int = None,
        workflow_type: str = None,
        xuid: str = None,
    ):
        self.filter_values = filter_values
        # log 的顺序，positive 代表最新的数据在最后，reverse 代表最新的数据在最前
        self.order_type = order_type
        self.page_num = page_num
        # 每一页的行数，最大值 100
        self.page_size = page_size
        # ENUM:["CreateCluster","DeleteCluster","Pack","Deploy"]
        self.workflow_type = workflow_type
        self.xuid = xuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter_values is not None:
            result['filterValues'] = self.filter_values
        if self.order_type is not None:
            result['orderType'] = self.order_type
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.workflow_type is not None:
            result['workflowType'] = self.workflow_type
        if self.xuid is not None:
            result['xuid'] = self.xuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filterValues') is not None:
            self.filter_values = m.get('filterValues')
        if m.get('orderType') is not None:
            self.order_type = m.get('orderType')
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('workflowType') is not None:
            self.workflow_type = m.get('workflowType')
        if m.get('xuid') is not None:
            self.xuid = m.get('xuid')
        return self


class ListWorkflowTaskLogsShrinkRequest(TeaModel):
    def __init__(
        self,
        filter_values_shrink: str = None,
        order_type: str = None,
        page_num: int = None,
        page_size: int = None,
        workflow_type: str = None,
        xuid: str = None,
    ):
        self.filter_values_shrink = filter_values_shrink
        # log 的顺序，positive 代表最新的数据在最后，reverse 代表最新的数据在最前
        self.order_type = order_type
        self.page_num = page_num
        # 每一页的行数，最大值 100
        self.page_size = page_size
        # ENUM:["CreateCluster","DeleteCluster","Pack","Deploy"]
        self.workflow_type = workflow_type
        self.xuid = xuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter_values_shrink is not None:
            result['filterValues'] = self.filter_values_shrink
        if self.order_type is not None:
            result['orderType'] = self.order_type
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.workflow_type is not None:
            result['workflowType'] = self.workflow_type
        if self.xuid is not None:
            result['xuid'] = self.xuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filterValues') is not None:
            self.filter_values_shrink = m.get('filterValues')
        if m.get('orderType') is not None:
            self.order_type = m.get('orderType')
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('workflowType') is not None:
            self.workflow_type = m.get('workflowType')
        if m.get('xuid') is not None:
            self.xuid = m.get('xuid')
        return self


class ListWorkflowTaskLogsResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[str] = None,
        page_num: int = None,
        page_size: int = None,
        total: int = None,
    ):
        # 日志数据
        self.list = list
        self.page_num = page_num
        self.page_size = page_size
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.list is not None:
            result['list'] = self.list
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('list') is not None:
            self.list = m.get('list')
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListWorkflowTaskLogsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListWorkflowTaskLogsResponseBodyData = None,
        msg: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = ListWorkflowTaskLogsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class ListWorkflowTaskLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListWorkflowTaskLogsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListWorkflowTaskLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutEnvironmentTunnelRequestTunnelConfig(TeaModel):
    def __init__(
        self,
        hostname: str = None,
        password: str = None,
        region_id: str = None,
        ssh_port: int = None,
        username: str = None,
        vpc_id: str = None,
    ):
        # 跳板机hostname
        self.hostname = hostname
        # 跳板机密码
        self.password = password
        # 直连地域id
        self.region_id = region_id
        # 跳板机ssh端口号
        self.ssh_port = ssh_port
        # 跳板机用户名
        self.username = username
        # 直连vpcId
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hostname is not None:
            result['hostname'] = self.hostname
        if self.password is not None:
            result['password'] = self.password
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.ssh_port is not None:
            result['sshPort'] = self.ssh_port
        if self.username is not None:
            result['username'] = self.username
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hostname') is not None:
            self.hostname = m.get('hostname')
        if m.get('password') is not None:
            self.password = m.get('password')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('sshPort') is not None:
            self.ssh_port = m.get('sshPort')
        if m.get('username') is not None:
            self.username = m.get('username')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        return self


class PutEnvironmentTunnelRequest(TeaModel):
    def __init__(
        self,
        tunnel_config: PutEnvironmentTunnelRequestTunnelConfig = None,
        tunnel_type: str = None,
    ):
        # 通道配置
        self.tunnel_config = tunnel_config
        # 通道类型
        self.tunnel_type = tunnel_type

    def validate(self):
        if self.tunnel_config:
            self.tunnel_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tunnel_config is not None:
            result['tunnelConfig'] = self.tunnel_config.to_map()
        if self.tunnel_type is not None:
            result['tunnelType'] = self.tunnel_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tunnelConfig') is not None:
            temp_model = PutEnvironmentTunnelRequestTunnelConfig()
            self.tunnel_config = temp_model.from_map(m['tunnelConfig'])
        if m.get('tunnelType') is not None:
            self.tunnel_type = m.get('tunnelType')
        return self


class PutEnvironmentTunnelResponseBodyData(TeaModel):
    def __init__(
        self,
        uid: str = None,
    ):
        # 通道id，可空
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class PutEnvironmentTunnelResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: PutEnvironmentTunnelResponseBodyData = None,
        msg: str = None,
    ):
        # 错误码
        self.code = code
        # 数据
        self.data = data
        # 错误信息
        self.msg = msg

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = PutEnvironmentTunnelResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class PutEnvironmentTunnelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PutEnvironmentTunnelResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PutEnvironmentTunnelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutProductInstanceConfigRequest(TeaModel):
    def __init__(
        self,
        component_uid: str = None,
        component_version_uid: str = None,
        config_uid: str = None,
        description: str = None,
        environment_uid: str = None,
        name: str = None,
        parent_component_name: str = None,
        parent_component_version_uid: str = None,
        product_version_uid: str = None,
        release_name: str = None,
        scope: List[str] = None,
        value: str = None,
        value_type: str = None,
    ):
        self.component_uid = component_uid
        self.component_version_uid = component_version_uid
        self.config_uid = config_uid
        self.description = description
        self.environment_uid = environment_uid
        self.name = name
        self.parent_component_name = parent_component_name
        self.parent_component_version_uid = parent_component_version_uid
        self.product_version_uid = product_version_uid
        self.release_name = release_name
        self.scope = scope
        self.value = value
        self.value_type = value_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_uid is not None:
            result['componentUID'] = self.component_uid
        if self.component_version_uid is not None:
            result['componentVersionUID'] = self.component_version_uid
        if self.config_uid is not None:
            result['configUID'] = self.config_uid
        if self.description is not None:
            result['description'] = self.description
        if self.environment_uid is not None:
            result['environmentUID'] = self.environment_uid
        if self.name is not None:
            result['name'] = self.name
        if self.parent_component_name is not None:
            result['parentComponentName'] = self.parent_component_name
        if self.parent_component_version_uid is not None:
            result['parentComponentVersionUID'] = self.parent_component_version_uid
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        if self.release_name is not None:
            result['releaseName'] = self.release_name
        if self.scope is not None:
            result['scope'] = self.scope
        if self.value is not None:
            result['value'] = self.value
        if self.value_type is not None:
            result['valueType'] = self.value_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('componentUID') is not None:
            self.component_uid = m.get('componentUID')
        if m.get('componentVersionUID') is not None:
            self.component_version_uid = m.get('componentVersionUID')
        if m.get('configUID') is not None:
            self.config_uid = m.get('configUID')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('environmentUID') is not None:
            self.environment_uid = m.get('environmentUID')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parentComponentName') is not None:
            self.parent_component_name = m.get('parentComponentName')
        if m.get('parentComponentVersionUID') is not None:
            self.parent_component_version_uid = m.get('parentComponentVersionUID')
        if m.get('productVersionUID') is not None:
            self.product_version_uid = m.get('productVersionUID')
        if m.get('releaseName') is not None:
            self.release_name = m.get('releaseName')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('valueType') is not None:
            self.value_type = m.get('valueType')
        return self


class PutProductInstanceConfigResponseBodyData(TeaModel):
    def __init__(
        self,
        uid: str = None,
    ):
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class PutProductInstanceConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: PutProductInstanceConfigResponseBodyData = None,
        msg: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = PutProductInstanceConfigResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class PutProductInstanceConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PutProductInstanceConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PutProductInstanceConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetEnvironmentFoundationReferenceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
    ):
        self.code = code
        self.msg = msg

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class SetEnvironmentFoundationReferenceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetEnvironmentFoundationReferenceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SetEnvironmentFoundationReferenceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEnvironmentRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        location: str = None,
        vendor_config: str = None,
    ):
        self.description = description
        self.location = location
        self.vendor_config = vendor_config

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.location is not None:
            result['location'] = self.location
        if self.vendor_config is not None:
            result['vendorConfig'] = self.vendor_config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('vendorConfig') is not None:
            self.vendor_config = m.get('vendorConfig')
        return self


class UpdateEnvironmentResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
    ):
        self.code = code
        self.msg = msg

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class UpdateEnvironmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateEnvironmentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateEnvironmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEnvironmentNodeRequestTaints(TeaModel):
    def __init__(
        self,
        effect: str = None,
        key: str = None,
        value: str = None,
    ):
        self.effect = effect
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.effect is not None:
            result['effect'] = self.effect
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('effect') is not None:
            self.effect = m.get('effect')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class UpdateEnvironmentNodeRequest(TeaModel):
    def __init__(
        self,
        application_disk: str = None,
        etcd_disk: str = None,
        labels: Dict[str, Any] = None,
        root_password: str = None,
        taints: List[UpdateEnvironmentNodeRequestTaints] = None,
        trident_system_disk: str = None,
        trident_system_size_disk: int = None,
    ):
        # 保留业务分区
        self.application_disk = application_disk
        # etcd数据盘
        self.etcd_disk = etcd_disk
        self.labels = labels
        self.root_password = root_password
        self.taints = taints
        # k8s管控数据盘
        self.trident_system_disk = trident_system_disk
        # k8s管控数据盘大小
        self.trident_system_size_disk = trident_system_size_disk

    def validate(self):
        if self.taints:
            for k in self.taints:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_disk is not None:
            result['applicationDisk'] = self.application_disk
        if self.etcd_disk is not None:
            result['etcdDisk'] = self.etcd_disk
        if self.labels is not None:
            result['labels'] = self.labels
        if self.root_password is not None:
            result['rootPassword'] = self.root_password
        result['taints'] = []
        if self.taints is not None:
            for k in self.taints:
                result['taints'].append(k.to_map() if k else None)
        if self.trident_system_disk is not None:
            result['tridentSystemDisk'] = self.trident_system_disk
        if self.trident_system_size_disk is not None:
            result['tridentSystemSizeDisk'] = self.trident_system_size_disk
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applicationDisk') is not None:
            self.application_disk = m.get('applicationDisk')
        if m.get('etcdDisk') is not None:
            self.etcd_disk = m.get('etcdDisk')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('rootPassword') is not None:
            self.root_password = m.get('rootPassword')
        self.taints = []
        if m.get('taints') is not None:
            for k in m.get('taints'):
                temp_model = UpdateEnvironmentNodeRequestTaints()
                self.taints.append(temp_model.from_map(k))
        if m.get('tridentSystemDisk') is not None:
            self.trident_system_disk = m.get('tridentSystemDisk')
        if m.get('tridentSystemSizeDisk') is not None:
            self.trident_system_size_disk = m.get('tridentSystemSizeDisk')
        return self


class UpdateEnvironmentNodeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
    ):
        self.code = code
        self.msg = msg

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class UpdateEnvironmentNodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateEnvironmentNodeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateEnvironmentNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEnvironmentProductVersionRequest(TeaModel):
    def __init__(
        self,
        old_product_version_uid: str = None,
        product_version_uid: str = None,
    ):
        self.old_product_version_uid = old_product_version_uid
        self.product_version_uid = product_version_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.old_product_version_uid is not None:
            result['oldProductVersionUID'] = self.old_product_version_uid
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('oldProductVersionUID') is not None:
            self.old_product_version_uid = m.get('oldProductVersionUID')
        if m.get('productVersionUID') is not None:
            self.product_version_uid = m.get('productVersionUID')
        return self


class UpdateEnvironmentProductVersionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
    ):
        self.code = code
        self.msg = msg

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class UpdateEnvironmentProductVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateEnvironmentProductVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateEnvironmentProductVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFoundationComponentReferenceRequest(TeaModel):
    def __init__(
        self,
        component_orchestration_values: str = None,
        enable: bool = None,
    ):
        self.component_orchestration_values = component_orchestration_values
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_orchestration_values is not None:
            result['componentOrchestrationValues'] = self.component_orchestration_values
        if self.enable is not None:
            result['enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('componentOrchestrationValues') is not None:
            self.component_orchestration_values = m.get('componentOrchestrationValues')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        return self


class UpdateFoundationComponentReferenceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
    ):
        self.code = code
        self.msg = msg

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class UpdateFoundationComponentReferenceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateFoundationComponentReferenceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateFoundationComponentReferenceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFoundationReferenceRequest(TeaModel):
    def __init__(
        self,
        cluster_config: str = None,
    ):
        self.cluster_config = cluster_config

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_config is not None:
            result['clusterConfig'] = self.cluster_config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusterConfig') is not None:
            self.cluster_config = m.get('clusterConfig')
        return self


class UpdateFoundationReferenceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
    ):
        self.code = code
        self.msg = msg

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class UpdateFoundationReferenceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateFoundationReferenceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateFoundationReferenceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProductRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
    ):
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        return self


class UpdateProductResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
    ):
        self.code = code
        self.msg = msg

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class UpdateProductResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateProductResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProductComponentVersionRequest(TeaModel):
    def __init__(
        self,
        component_orchestration_values: str = None,
        enable: bool = None,
        new_component_version_uid: str = None,
        release_name: str = None,
    ):
        self.component_orchestration_values = component_orchestration_values
        self.enable = enable
        # 如果该参数不为空，则代表更新组件版本
        self.new_component_version_uid = new_component_version_uid
        self.release_name = release_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_orchestration_values is not None:
            result['componentOrchestrationValues'] = self.component_orchestration_values
        if self.enable is not None:
            result['enable'] = self.enable
        if self.new_component_version_uid is not None:
            result['newComponentVersionUID'] = self.new_component_version_uid
        if self.release_name is not None:
            result['releaseName'] = self.release_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('componentOrchestrationValues') is not None:
            self.component_orchestration_values = m.get('componentOrchestrationValues')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('newComponentVersionUID') is not None:
            self.new_component_version_uid = m.get('newComponentVersionUID')
        if m.get('releaseName') is not None:
            self.release_name = m.get('releaseName')
        return self


class UpdateProductComponentVersionResponseBodyData(TeaModel):
    def __init__(
        self,
        relation_uid: str = None,
    ):
        self.relation_uid = relation_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.relation_uid is not None:
            result['relationUID'] = self.relation_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('relationUID') is not None:
            self.relation_uid = m.get('relationUID')
        return self


class UpdateProductComponentVersionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: UpdateProductComponentVersionResponseBodyData = None,
        msg: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = UpdateProductComponentVersionResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class UpdateProductComponentVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateProductComponentVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateProductComponentVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProductFoundationVersionRequest(TeaModel):
    def __init__(
        self,
        foundation_version_uid: str = None,
    ):
        # 底座版本uid
        self.foundation_version_uid = foundation_version_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.foundation_version_uid is not None:
            result['foundationVersionUID'] = self.foundation_version_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('foundationVersionUID') is not None:
            self.foundation_version_uid = m.get('foundationVersionUID')
        return self


class UpdateProductFoundationVersionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
    ):
        self.code = code
        self.msg = msg

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class UpdateProductFoundationVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateProductFoundationVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateProductFoundationVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProductVersionRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        version: str = None,
    ):
        self.description = description
        # 更新版本号，只允许从latest 更新到其他版本号，更新之后代表已发布
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class UpdateProductVersionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
    ):
        self.code = code
        self.msg = msg

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class UpdateProductVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateProductVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateProductVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProductVersionConfigRequest(TeaModel):
    def __init__(
        self,
        component_version_uid: str = None,
        description: str = None,
        name: str = None,
        parent_component_version_uid: str = None,
        value: str = None,
        value_type: str = None,
    ):
        # 子组件versinid
        self.component_version_uid = component_version_uid
        # 配置说明
        self.description = description
        # 配置信息key
        self.name = name
        # 父组件versionid
        self.parent_component_version_uid = parent_component_version_uid
        # 配置信息value
        self.value = value
        # value类型
        self.value_type = value_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_version_uid is not None:
            result['componentVersionUID'] = self.component_version_uid
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.parent_component_version_uid is not None:
            result['parentComponentVersionUID'] = self.parent_component_version_uid
        if self.value is not None:
            result['value'] = self.value
        if self.value_type is not None:
            result['valueType'] = self.value_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('componentVersionUID') is not None:
            self.component_version_uid = m.get('componentVersionUID')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parentComponentVersionUID') is not None:
            self.parent_component_version_uid = m.get('parentComponentVersionUID')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('valueType') is not None:
            self.value_type = m.get('valueType')
        return self


class UpdateProductVersionConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.msg = msg
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateProductVersionConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateProductVersionConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateProductVersionConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ValidateEnvironmentTunnelRequestTunnelConfig(TeaModel):
    def __init__(
        self,
        hostname: str = None,
        password: str = None,
        region_id: str = None,
        ssh_port: int = None,
        username: str = None,
        vpc_id: str = None,
    ):
        # 跳板机hostname
        self.hostname = hostname
        # 跳板机密码
        self.password = password
        # 直连地域id
        self.region_id = region_id
        # 跳板机ssh端口号
        self.ssh_port = ssh_port
        # 跳板机用户名
        self.username = username
        # 直连vpcId
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hostname is not None:
            result['hostname'] = self.hostname
        if self.password is not None:
            result['password'] = self.password
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.ssh_port is not None:
            result['sshPort'] = self.ssh_port
        if self.username is not None:
            result['username'] = self.username
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hostname') is not None:
            self.hostname = m.get('hostname')
        if m.get('password') is not None:
            self.password = m.get('password')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('sshPort') is not None:
            self.ssh_port = m.get('sshPort')
        if m.get('username') is not None:
            self.username = m.get('username')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        return self


class ValidateEnvironmentTunnelRequest(TeaModel):
    def __init__(
        self,
        tunnel_config: ValidateEnvironmentTunnelRequestTunnelConfig = None,
        tunnel_type: str = None,
    ):
        # 通道配置
        self.tunnel_config = tunnel_config
        # 通道类型
        self.tunnel_type = tunnel_type

    def validate(self):
        if self.tunnel_config:
            self.tunnel_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tunnel_config is not None:
            result['tunnelConfig'] = self.tunnel_config.to_map()
        if self.tunnel_type is not None:
            result['tunnelType'] = self.tunnel_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tunnelConfig') is not None:
            temp_model = ValidateEnvironmentTunnelRequestTunnelConfig()
            self.tunnel_config = temp_model.from_map(m['tunnelConfig'])
        if m.get('tunnelType') is not None:
            self.tunnel_type = m.get('tunnelType')
        return self


class ValidateEnvironmentTunnelResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
    ):
        # 错误码
        self.code = code
        # 错误信息
        self.msg = msg

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class ValidateEnvironmentTunnelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ValidateEnvironmentTunnelResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ValidateEnvironmentTunnelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


