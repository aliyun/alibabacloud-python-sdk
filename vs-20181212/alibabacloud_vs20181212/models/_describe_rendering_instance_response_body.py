# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class DescribeRenderingInstanceResponseBody(DaraModel):
    def __init__(
        self,
        additional_ingresses: List[main_models.DescribeRenderingInstanceResponseBodyAdditionalIngresses] = None,
        config_info: main_models.DescribeRenderingInstanceResponseBodyConfigInfo = None,
        creation_time: str = None,
        egress_ip: str = None,
        hostname: str = None,
        instance_charge_type: str = None,
        internal_ip: str = None,
        isp: str = None,
        port_mappings: List[main_models.DescribeRenderingInstanceResponseBodyPortMappings] = None,
        rendering_instance_id: str = None,
        rendering_spec: str = None,
        rendering_status: main_models.DescribeRenderingInstanceResponseBodyRenderingStatus = None,
        request_id: str = None,
        resource_attributes: main_models.DescribeRenderingInstanceResponseBodyResourceAttributes = None,
        storage_size: int = None,
        system_info: main_models.DescribeRenderingInstanceResponseBodySystemInfo = None,
    ):
        self.additional_ingresses = additional_ingresses
        self.config_info = config_info
        self.creation_time = creation_time
        self.egress_ip = egress_ip
        self.hostname = hostname
        self.instance_charge_type = instance_charge_type
        self.internal_ip = internal_ip
        self.isp = isp
        self.port_mappings = port_mappings
        self.rendering_instance_id = rendering_instance_id
        self.rendering_spec = rendering_spec
        self.rendering_status = rendering_status
        self.request_id = request_id
        self.resource_attributes = resource_attributes
        self.storage_size = storage_size
        self.system_info = system_info

    def validate(self):
        if self.additional_ingresses:
            for v1 in self.additional_ingresses:
                 if v1:
                    v1.validate()
        if self.config_info:
            self.config_info.validate()
        if self.port_mappings:
            for v1 in self.port_mappings:
                 if v1:
                    v1.validate()
        if self.rendering_status:
            self.rendering_status.validate()
        if self.resource_attributes:
            self.resource_attributes.validate()
        if self.system_info:
            self.system_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AdditionalIngresses'] = []
        if self.additional_ingresses is not None:
            for k1 in self.additional_ingresses:
                result['AdditionalIngresses'].append(k1.to_map() if k1 else None)

        if self.config_info is not None:
            result['ConfigInfo'] = self.config_info.to_map()

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.egress_ip is not None:
            result['EgressIp'] = self.egress_ip

        if self.hostname is not None:
            result['Hostname'] = self.hostname

        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type

        if self.internal_ip is not None:
            result['InternalIp'] = self.internal_ip

        if self.isp is not None:
            result['Isp'] = self.isp

        result['PortMappings'] = []
        if self.port_mappings is not None:
            for k1 in self.port_mappings:
                result['PortMappings'].append(k1.to_map() if k1 else None)

        if self.rendering_instance_id is not None:
            result['RenderingInstanceId'] = self.rendering_instance_id

        if self.rendering_spec is not None:
            result['RenderingSpec'] = self.rendering_spec

        if self.rendering_status is not None:
            result['RenderingStatus'] = self.rendering_status.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_attributes is not None:
            result['ResourceAttributes'] = self.resource_attributes.to_map()

        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size

        if self.system_info is not None:
            result['SystemInfo'] = self.system_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.additional_ingresses = []
        if m.get('AdditionalIngresses') is not None:
            for k1 in m.get('AdditionalIngresses'):
                temp_model = main_models.DescribeRenderingInstanceResponseBodyAdditionalIngresses()
                self.additional_ingresses.append(temp_model.from_map(k1))

        if m.get('ConfigInfo') is not None:
            temp_model = main_models.DescribeRenderingInstanceResponseBodyConfigInfo()
            self.config_info = temp_model.from_map(m.get('ConfigInfo'))

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('EgressIp') is not None:
            self.egress_ip = m.get('EgressIp')

        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')

        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')

        if m.get('InternalIp') is not None:
            self.internal_ip = m.get('InternalIp')

        if m.get('Isp') is not None:
            self.isp = m.get('Isp')

        self.port_mappings = []
        if m.get('PortMappings') is not None:
            for k1 in m.get('PortMappings'):
                temp_model = main_models.DescribeRenderingInstanceResponseBodyPortMappings()
                self.port_mappings.append(temp_model.from_map(k1))

        if m.get('RenderingInstanceId') is not None:
            self.rendering_instance_id = m.get('RenderingInstanceId')

        if m.get('RenderingSpec') is not None:
            self.rendering_spec = m.get('RenderingSpec')

        if m.get('RenderingStatus') is not None:
            temp_model = main_models.DescribeRenderingInstanceResponseBodyRenderingStatus()
            self.rendering_status = temp_model.from_map(m.get('RenderingStatus'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceAttributes') is not None:
            temp_model = main_models.DescribeRenderingInstanceResponseBodyResourceAttributes()
            self.resource_attributes = temp_model.from_map(m.get('ResourceAttributes'))

        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')

        if m.get('SystemInfo') is not None:
            temp_model = main_models.DescribeRenderingInstanceResponseBodySystemInfo()
            self.system_info = temp_model.from_map(m.get('SystemInfo'))

        return self

class DescribeRenderingInstanceResponseBodySystemInfo(DaraModel):
    def __init__(
        self,
        frequency: int = None,
        resolution: str = None,
    ):
        self.frequency = frequency
        self.resolution = resolution

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.frequency is not None:
            result['Frequency'] = self.frequency

        if self.resolution is not None:
            result['Resolution'] = self.resolution

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Frequency') is not None:
            self.frequency = m.get('Frequency')

        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')

        return self

class DescribeRenderingInstanceResponseBodyResourceAttributes(DaraModel):
    def __init__(
        self,
        edge_media_service: str = None,
        in_access: str = None,
        out_access: str = None,
        zone: str = None,
    ):
        self.edge_media_service = edge_media_service
        self.in_access = in_access
        self.out_access = out_access
        self.zone = zone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.edge_media_service is not None:
            result['EdgeMediaService'] = self.edge_media_service

        if self.in_access is not None:
            result['InAccess'] = self.in_access

        if self.out_access is not None:
            result['OutAccess'] = self.out_access

        if self.zone is not None:
            result['Zone'] = self.zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EdgeMediaService') is not None:
            self.edge_media_service = m.get('EdgeMediaService')

        if m.get('InAccess') is not None:
            self.in_access = m.get('InAccess')

        if m.get('OutAccess') is not None:
            self.out_access = m.get('OutAccess')

        if m.get('Zone') is not None:
            self.zone = m.get('Zone')

        return self

class DescribeRenderingInstanceResponseBodyRenderingStatus(DaraModel):
    def __init__(
        self,
        description: str = None,
        latest_action: str = None,
        status: str = None,
    ):
        self.description = description
        self.latest_action = latest_action
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.latest_action is not None:
            result['LatestAction'] = self.latest_action

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('LatestAction') is not None:
            self.latest_action = m.get('LatestAction')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeRenderingInstanceResponseBodyPortMappings(DaraModel):
    def __init__(
        self,
        external_port: str = None,
        internal_port: str = None,
    ):
        self.external_port = external_port
        self.internal_port = internal_port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.external_port is not None:
            result['ExternalPort'] = self.external_port

        if self.internal_port is not None:
            result['InternalPort'] = self.internal_port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternalPort') is not None:
            self.external_port = m.get('ExternalPort')

        if m.get('InternalPort') is not None:
            self.internal_port = m.get('InternalPort')

        return self

class DescribeRenderingInstanceResponseBodyConfigInfo(DaraModel):
    def __init__(
        self,
        configuration: List[main_models.DescribeRenderingInstanceResponseBodyConfigInfoConfiguration] = None,
        network_config: main_models.DescribeRenderingInstanceResponseBodyConfigInfoNetworkConfig = None,
    ):
        self.configuration = configuration
        self.network_config = network_config

    def validate(self):
        if self.configuration:
            for v1 in self.configuration:
                 if v1:
                    v1.validate()
        if self.network_config:
            self.network_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Configuration'] = []
        if self.configuration is not None:
            for k1 in self.configuration:
                result['Configuration'].append(k1.to_map() if k1 else None)

        if self.network_config is not None:
            result['NetworkConfig'] = self.network_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.configuration = []
        if m.get('Configuration') is not None:
            for k1 in m.get('Configuration'):
                temp_model = main_models.DescribeRenderingInstanceResponseBodyConfigInfoConfiguration()
                self.configuration.append(temp_model.from_map(k1))

        if m.get('NetworkConfig') is not None:
            temp_model = main_models.DescribeRenderingInstanceResponseBodyConfigInfoNetworkConfig()
            self.network_config = temp_model.from_map(m.get('NetworkConfig'))

        return self

class DescribeRenderingInstanceResponseBodyConfigInfoNetworkConfig(DaraModel):
    def __init__(
        self,
        bandwidth_status: str = None,
        max_egress_bandwidth: int = None,
        max_ingress_bandwidth: int = None,
        update_time: str = None,
    ):
        self.bandwidth_status = bandwidth_status
        self.max_egress_bandwidth = max_egress_bandwidth
        self.max_ingress_bandwidth = max_ingress_bandwidth
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth_status is not None:
            result['BandwidthStatus'] = self.bandwidth_status

        if self.max_egress_bandwidth is not None:
            result['MaxEgressBandwidth'] = self.max_egress_bandwidth

        if self.max_ingress_bandwidth is not None:
            result['MaxIngressBandwidth'] = self.max_ingress_bandwidth

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandwidthStatus') is not None:
            self.bandwidth_status = m.get('BandwidthStatus')

        if m.get('MaxEgressBandwidth') is not None:
            self.max_egress_bandwidth = m.get('MaxEgressBandwidth')

        if m.get('MaxIngressBandwidth') is not None:
            self.max_ingress_bandwidth = m.get('MaxIngressBandwidth')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class DescribeRenderingInstanceResponseBodyConfigInfoConfiguration(DaraModel):
    def __init__(
        self,
        attributes: List[main_models.DescribeRenderingInstanceResponseBodyConfigInfoConfigurationAttributes] = None,
        module_name: str = None,
    ):
        self.attributes = attributes
        self.module_name = module_name

    def validate(self):
        if self.attributes:
            for v1 in self.attributes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Attributes'] = []
        if self.attributes is not None:
            for k1 in self.attributes:
                result['Attributes'].append(k1.to_map() if k1 else None)

        if self.module_name is not None:
            result['ModuleName'] = self.module_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attributes = []
        if m.get('Attributes') is not None:
            for k1 in m.get('Attributes'):
                temp_model = main_models.DescribeRenderingInstanceResponseBodyConfigInfoConfigurationAttributes()
                self.attributes.append(temp_model.from_map(k1))

        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')

        return self

class DescribeRenderingInstanceResponseBodyConfigInfoConfigurationAttributes(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: Any = None,
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

class DescribeRenderingInstanceResponseBodyAdditionalIngresses(DaraModel):
    def __init__(
        self,
        hostname: str = None,
        isp: str = None,
        port_mappings: List[main_models.DescribeRenderingInstanceResponseBodyAdditionalIngressesPortMappings] = None,
    ):
        self.hostname = hostname
        self.isp = isp
        self.port_mappings = port_mappings

    def validate(self):
        if self.port_mappings:
            for v1 in self.port_mappings:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hostname is not None:
            result['Hostname'] = self.hostname

        if self.isp is not None:
            result['Isp'] = self.isp

        result['PortMappings'] = []
        if self.port_mappings is not None:
            for k1 in self.port_mappings:
                result['PortMappings'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')

        if m.get('Isp') is not None:
            self.isp = m.get('Isp')

        self.port_mappings = []
        if m.get('PortMappings') is not None:
            for k1 in m.get('PortMappings'):
                temp_model = main_models.DescribeRenderingInstanceResponseBodyAdditionalIngressesPortMappings()
                self.port_mappings.append(temp_model.from_map(k1))

        return self

class DescribeRenderingInstanceResponseBodyAdditionalIngressesPortMappings(DaraModel):
    def __init__(
        self,
        external_port: str = None,
        internal_port: str = None,
    ):
        self.external_port = external_port
        self.internal_port = internal_port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.external_port is not None:
            result['ExternalPort'] = self.external_port

        if self.internal_port is not None:
            result['InternalPort'] = self.internal_port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternalPort') is not None:
            self.external_port = m.get('ExternalPort')

        if m.get('InternalPort') is not None:
            self.internal_port = m.get('InternalPort')

        return self

