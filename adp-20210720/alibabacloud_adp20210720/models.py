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
        description: str = None,
        documents: str = None,
        features: List[str] = None,
        name: str = None,
        package_tools: List[FoundationVersionPackageTools] = None,
        platforms: List[Platform] = None,
        status: str = None,
        type: str = None,
        uid: str = None,
        version: str = None,
    ):
        # description
        self.description = description
        # documents
        self.documents = documents
        # 底座功能列表
        self.features = features
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
        if self.description is not None:
            result['description'] = self.description
        if self.documents is not None:
            result['documents'] = self.documents
        if self.features is not None:
            result['features'] = self.features
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
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('documents') is not None:
            self.documents = m.get('documents')
        if m.get('features') is not None:
            self.features = m.get('features')
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
        network_cards: List[InstanceInfoNetworkCards] = None,
        os: str = None,
        os_version: str = None,
        private_ip: str = None,
        public_ip: str = None,
        root_password: str = None,
        system_disk: List[Disk] = None,
        system_info: str = None,
        taints: List[InstanceInfoTaints] = None,
    ):
        # annotations
        self.annotations = annotations
        # arch
        self.arch = arch
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

    def validate(self):
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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('annotations') is not None:
            self.annotations = m.get('annotations')
        if m.get('arch') is not None:
            self.arch = m.get('arch')
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
        body: AddEnvironmentNodesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddEnvironmentNodesResponseBody()
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
        body: AddProductComponentVersionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: AddProductVersionConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddProductVersionConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AuthorizeProductVersionRequest(TeaModel):
    def __init__(
        self,
        grantee: str = None,
    ):
        # 被授权者uid
        self.grantee = grantee

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.grantee is not None:
            result['grantee'] = self.grantee
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('grantee') is not None:
            self.grantee = m.get('grantee')
        return self


class AuthorizeProductVersionResponseBody(TeaModel):
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


class AuthorizeProductVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AuthorizeProductVersionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AuthorizeProductVersionResponseBody()
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
        product_version_uid: str = None,
        type: str = None,
        vendor_config: str = None,
        vendor_type: str = None,
    ):
        self.description = description
        self.location = location
        self.name = name
        self.platform = platform
        self.product_version_uid = product_version_uid
        # 环境类型
        self.type = type
        self.vendor_config = vendor_config
        self.vendor_type = vendor_type

    def validate(self):
        if self.platform:
            self.platform.validate()

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
        body: CreateEnvironmentResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateEnvironmentResponseBody()
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
        body: CreateFoundationReferenceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: CreateProductResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProductDeploymentRequest(TeaModel):
    def __init__(
        self,
        environment_uid: str = None,
        old_product_version_uid: str = None,
        package_uid: str = None,
        product_version_uid: str = None,
    ):
        # 环境uid
        self.environment_uid = environment_uid
        # 旧产品版本uid
        self.old_product_version_uid = old_product_version_uid
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
        if self.old_product_version_uid is not None:
            result['oldProductVersionUID'] = self.old_product_version_uid
        if self.package_uid is not None:
            result['packageUID'] = self.package_uid
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('environmentUID') is not None:
            self.environment_uid = m.get('environmentUID')
        if m.get('oldProductVersionUID') is not None:
            self.old_product_version_uid = m.get('oldProductVersionUID')
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
        body: CreateProductDeploymentResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateProductDeploymentResponseBody()
            self.body = temp_model.from_map(m['body'])
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
        body: CreateProductVersionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        old_product_version_uid: str = None,
        package_content_type: str = None,
        package_type: str = None,
        platform: str = None,
    ):
        self.old_product_version_uid = old_product_version_uid
        # ENUM:["all","base"."application"]
        self.package_content_type = package_content_type
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
        if self.old_product_version_uid is not None:
            result['oldProductVersionUID'] = self.old_product_version_uid
        if self.package_content_type is not None:
            result['packageContentType'] = self.package_content_type
        if self.package_type is not None:
            result['packageType'] = self.package_type
        if self.platform is not None:
            result['platform'] = self.platform
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('oldProductVersionUID') is not None:
            self.old_product_version_uid = m.get('oldProductVersionUID')
        if m.get('packageContentType') is not None:
            self.package_content_type = m.get('packageContentType')
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
        body: CreateProductVersionPackageResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: DeleteEnvironmentResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteEnvironmentResponseBody()
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
        body: DeleteEnvironmentNodeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: DeleteEnvironmentProductVersionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: DeleteProductResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: DeleteProductComponentVersionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: DeleteProductInstanceConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: DeleteProductVersionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: DeleteProductVersionConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteProductVersionConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateProductInstanceDeploymentConfigRequest(TeaModel):
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
        body: GenerateProductInstanceDeploymentConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: GetComponentResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetComponentResponseBody()
            self.body = temp_model.from_map(m['body'])
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
        body: GetComponentVersionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetComponentVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
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
        product_name: str = None,
        product_version: str = None,
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
        self.product_name = product_name
        self.product_version = product_version
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
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.product_version is not None:
            result['productVersion'] = self.product_version
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
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('productVersion') is not None:
            self.product_version = m.get('productVersion')
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
        body: GetEnvironmentResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetEnvironmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEnvironmentNodeResponseBodyDataNetworkCards(TeaModel):
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


class GetEnvironmentNodeResponseBodyDataTaints(TeaModel):
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


class GetEnvironmentNodeResponseBodyData(TeaModel):
    def __init__(
        self,
        arch: str = None,
        cluster_uid: str = None,
        cpu: str = None,
        created_at: str = None,
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
        network_cards: List[GetEnvironmentNodeResponseBodyDataNetworkCards] = None,
        os: str = None,
        os_version: str = None,
        private_ip: str = None,
        public_ip: str = None,
        root_password: str = None,
        system_disk: List[Disk] = None,
        system_info: str = None,
        taints: List[GetEnvironmentNodeResponseBodyDataTaints] = None,
        uid: str = None,
    ):
        # arch
        self.arch = arch
        self.cluster_uid = cluster_uid
        # cpu
        self.cpu = cpu
        self.created_at = created_at
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
        self.uid = uid

    def validate(self):
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
        if self.arch is not None:
            result['arch'] = self.arch
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
        if m.get('arch') is not None:
            self.arch = m.get('arch')
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
                temp_model = GetEnvironmentNodeResponseBodyDataNetworkCards()
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
                temp_model = GetEnvironmentNodeResponseBodyDataTaints()
                self.taints.append(temp_model.from_map(k))
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class GetEnvironmentNodeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetEnvironmentNodeResponseBodyData = None,
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
            temp_model = GetEnvironmentNodeResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class GetEnvironmentNodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetEnvironmentNodeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetEnvironmentNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFoundationComponentReferenceResponseBodyData(TeaModel):
    def __init__(
        self,
        app_version: str = None,
        component_description: str = None,
        component_name: str = None,
        component_reference_uid: str = None,
        component_uid: str = None,
        component_version_description: str = None,
        component_version_uid: str = None,
        enable: bool = None,
        namespace: str = None,
        orchestration_values: str = None,
        parent_component: bool = None,
        parent_component_version_relation_uid: str = None,
        parent_component_version_uid: str = None,
        release_name: str = None,
        resources: str = None,
        sequence: int = None,
        values: str = None,
        version: str = None,
    ):
        self.app_version = app_version
        self.component_description = component_description
        self.component_name = component_name
        self.component_reference_uid = component_reference_uid
        self.component_uid = component_uid
        self.component_version_description = component_version_description
        self.component_version_uid = component_version_uid
        self.enable = enable
        self.namespace = namespace
        self.orchestration_values = orchestration_values
        self.parent_component = parent_component
        self.parent_component_version_relation_uid = parent_component_version_relation_uid
        self.parent_component_version_uid = parent_component_version_uid
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
        if self.component_reference_uid is not None:
            result['componentReferenceUID'] = self.component_reference_uid
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
        if m.get('componentReferenceUID') is not None:
            self.component_reference_uid = m.get('componentReferenceUID')
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


class GetFoundationComponentReferenceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetFoundationComponentReferenceResponseBodyData] = None,
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
                temp_model = GetFoundationComponentReferenceResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class GetFoundationComponentReferenceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetFoundationComponentReferenceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetFoundationComponentReferenceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFoundationVersionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[FoundationVersion] = None,
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
                temp_model = FoundationVersion()
                self.data.append(temp_model.from_map(k))
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class GetFoundationVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetFoundationVersionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: GetProductResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: GetProductComponentVersionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: GetProductDeploymentResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: GetProductVersionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: GetProductVersionDifferencesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
    ):
        self.package_content_type = package_content_type
        self.package_size = package_size
        self.package_status = package_status
        self.package_type = package_type
        self.package_uid = package_uid
        self.package_url = package_url
        self.platform = platform

    def validate(self):
        if self.platform:
            self.platform.validate()

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
        body: GetProductVersionPackageResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetProductVersionPackageResponseBody()
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
        body: GetWorkflowStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: InitEnvironmentResourceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: ListComponentVersionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: ListComponentsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListComponentsResponseBody()
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
        list: List[GetInstanceInfoResponse] = None,
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
                temp_model = GetInstanceInfoResponse()
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
        body: ListEnvironmentNodesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: ListEnvironmentTunnelsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        id: int = None,
        location: str = None,
        name: str = None,
        platform: ListEnvironmentsResponseBodyDataListPlatform = None,
        product_name: str = None,
        product_version: str = None,
        product_version_uid: str = None,
        uid: str = None,
        vendor_type: str = None,
    ):
        self.created_at = created_at
        self.description = description
        self.id = id
        self.location = location
        self.name = name
        self.platform = platform
        self.product_name = product_name
        self.product_version = product_version
        self.product_version_uid = product_version_uid
        self.uid = uid
        self.vendor_type = vendor_type

    def validate(self):
        if self.platform:
            self.platform.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.id is not None:
            result['id'] = self.id
        if self.location is not None:
            result['location'] = self.location
        if self.name is not None:
            result['name'] = self.name
        if self.platform is not None:
            result['platform'] = self.platform.to_map()
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
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('platform') is not None:
            temp_model = ListEnvironmentsResponseBodyDataListPlatform()
            self.platform = temp_model.from_map(m['platform'])
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
        body: ListEnvironmentsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: ListFoundationComponentVersionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListFoundationComponentVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFoundationReferenceComponentsRequest(TeaModel):
    def __init__(
        self,
        foundation_version_uid: str = None,
        only_enabled: bool = None,
        product_version_uid: str = None,
    ):
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
        if self.foundation_version_uid is not None:
            result['foundationVersionUID'] = self.foundation_version_uid
        if self.only_enabled is not None:
            result['onlyEnabled'] = self.only_enabled
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
        body: ListFoundationReferenceComponentsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: ListFoundationVersionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
                temp_model = ProductComponentRelationDetail()
                self.list.append(temp_model.from_map(k))
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
        body: ListProductComponentVersionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: ListProductDeploymentsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: ListProductEnvironmentsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListProductEnvironmentsResponseBody()
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
        body: ListProductInstanceConfigsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: ListProductInstancesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: ListProductVersionConfigsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: ListProductVersionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: ListProductsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: ListWorkflowTaskLogsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: PutEnvironmentTunnelResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: PutProductInstanceConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: SetEnvironmentFoundationReferenceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: UpdateEnvironmentResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: UpdateEnvironmentNodeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: UpdateEnvironmentProductVersionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: UpdateFoundationComponentReferenceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateFoundationComponentReferenceResponseBody()
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
        body: UpdateProductResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: UpdateProductComponentVersionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: UpdateProductFoundationVersionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: UpdateProductVersionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: UpdateProductVersionConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: ValidateEnvironmentTunnelResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ValidateEnvironmentTunnelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


