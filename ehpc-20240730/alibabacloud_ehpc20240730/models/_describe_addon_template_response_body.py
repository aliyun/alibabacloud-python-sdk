# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ehpc20240730 import models as main_models
from darabonba.model import DaraModel

class DescribeAddonTemplateResponseBody(DaraModel):
    def __init__(
        self,
        addon: main_models.DescribeAddonTemplateResponseBodyAddon = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The details of the addon template.
        self.addon = addon
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.addon:
            self.addon.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addon is not None:
            result['Addon'] = self.addon.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Addon') is not None:
            temp_model = main_models.DescribeAddonTemplateResponseBodyAddon()
            self.addon = temp_model.from_map(m.get('Addon'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeAddonTemplateResponseBodyAddon(DaraModel):
    def __init__(
        self,
        description: str = None,
        icon: str = None,
        label: str = None,
        last_update: str = None,
        name: str = None,
        resources_spec: main_models.DescribeAddonTemplateResponseBodyAddonResourcesSpec = None,
        services_spec: List[main_models.DescribeAddonTemplateResponseBodyAddonServicesSpec] = None,
        version: str = None,
    ):
        # The addon description.
        self.description = description
        # The addon icon.
        self.icon = icon
        # The addon label.
        self.label = label
        # The date when the addon template was last updated.
        self.last_update = last_update
        # The addon name.
        # 
        # This parameter is required.
        self.name = name
        # The resource configurations of the addon.
        self.resources_spec = resources_spec
        # The addon configurations.
        self.services_spec = services_spec
        # The addon version.
        # 
        # This parameter is required.
        self.version = version

    def validate(self):
        if self.resources_spec:
            self.resources_spec.validate()
        if self.services_spec:
            for v1 in self.services_spec:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.icon is not None:
            result['Icon'] = self.icon

        if self.label is not None:
            result['Label'] = self.label

        if self.last_update is not None:
            result['LastUpdate'] = self.last_update

        if self.name is not None:
            result['Name'] = self.name

        if self.resources_spec is not None:
            result['ResourcesSpec'] = self.resources_spec.to_map()

        result['ServicesSpec'] = []
        if self.services_spec is not None:
            for k1 in self.services_spec:
                result['ServicesSpec'].append(k1.to_map() if k1 else None)

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Icon') is not None:
            self.icon = m.get('Icon')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('LastUpdate') is not None:
            self.last_update = m.get('LastUpdate')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ResourcesSpec') is not None:
            temp_model = main_models.DescribeAddonTemplateResponseBodyAddonResourcesSpec()
            self.resources_spec = temp_model.from_map(m.get('ResourcesSpec'))

        self.services_spec = []
        if m.get('ServicesSpec') is not None:
            for k1 in m.get('ServicesSpec'):
                temp_model = main_models.DescribeAddonTemplateResponseBodyAddonServicesSpec()
                self.services_spec.append(temp_model.from_map(k1))

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class DescribeAddonTemplateResponseBodyAddonServicesSpec(DaraModel):
    def __init__(
        self,
        input_params: List[main_models.DescribeAddonTemplateResponseBodyAddonServicesSpecInputParams] = None,
        network_acl: List[main_models.DescribeAddonTemplateResponseBodyAddonServicesSpecNetworkACL] = None,
        service_access_type: str = None,
        service_access_url: str = None,
        service_name: str = None,
    ):
        # The parameter configurations of the service.
        self.input_params = input_params
        # The security group configurations of the service.
        self.network_acl = network_acl
        # The service access type.
        self.service_access_type = service_access_type
        # The service access URL.
        self.service_access_url = service_access_url
        # The service name.
        # 
        # This parameter is required.
        self.service_name = service_name

    def validate(self):
        if self.input_params:
            for v1 in self.input_params:
                 if v1:
                    v1.validate()
        if self.network_acl:
            for v1 in self.network_acl:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InputParams'] = []
        if self.input_params is not None:
            for k1 in self.input_params:
                result['InputParams'].append(k1.to_map() if k1 else None)

        result['NetworkACL'] = []
        if self.network_acl is not None:
            for k1 in self.network_acl:
                result['NetworkACL'].append(k1.to_map() if k1 else None)

        if self.service_access_type is not None:
            result['ServiceAccessType'] = self.service_access_type

        if self.service_access_url is not None:
            result['ServiceAccessUrl'] = self.service_access_url

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.input_params = []
        if m.get('InputParams') is not None:
            for k1 in m.get('InputParams'):
                temp_model = main_models.DescribeAddonTemplateResponseBodyAddonServicesSpecInputParams()
                self.input_params.append(temp_model.from_map(k1))

        self.network_acl = []
        if m.get('NetworkACL') is not None:
            for k1 in m.get('NetworkACL'):
                temp_model = main_models.DescribeAddonTemplateResponseBodyAddonServicesSpecNetworkACL()
                self.network_acl.append(temp_model.from_map(k1))

        if m.get('ServiceAccessType') is not None:
            self.service_access_type = m.get('ServiceAccessType')

        if m.get('ServiceAccessUrl') is not None:
            self.service_access_url = m.get('ServiceAccessUrl')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        return self

class DescribeAddonTemplateResponseBodyAddonServicesSpecNetworkACL(DaraModel):
    def __init__(
        self,
        ip_protocol: str = None,
        port: float = None,
        source_cidr_ip: str = None,
    ):
        # The protocol type. Valid values:
        # 
        # *   **TCP**: forwards TCP packets.
        # *   **UDP**: forwards UDP packets.
        # *   **Any**: forwards all packets.
        # 
        # This parameter is required.
        self.ip_protocol = ip_protocol
        # The port number.
        # 
        # This parameter is required.
        self.port = port
        # The source CIDR block.
        # 
        # This parameter is required.
        self.source_cidr_ip = source_cidr_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol

        if self.port is not None:
            result['Port'] = self.port

        if self.source_cidr_ip is not None:
            result['SourceCidrIp'] = self.source_cidr_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('SourceCidrIp') is not None:
            self.source_cidr_ip = m.get('SourceCidrIp')

        return self

class DescribeAddonTemplateResponseBodyAddonServicesSpecInputParams(DaraModel):
    def __init__(
        self,
        help_text: str = None,
        label: str = None,
        name: str = None,
        type: str = None,
        value: str = None,
    ):
        # The help information of the parameter.
        self.help_text = help_text
        # The parameter label.
        self.label = label
        # The parameter name.
        # 
        # This parameter is required.
        self.name = name
        # The parameter type.
        # 
        # This parameter is required.
        self.type = type
        # The parameter value.
        # 
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.help_text is not None:
            result['HelpText'] = self.help_text

        if self.label is not None:
            result['Label'] = self.label

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HelpText') is not None:
            self.help_text = m.get('HelpText')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeAddonTemplateResponseBodyAddonResourcesSpec(DaraModel):
    def __init__(
        self,
        ecs_resources: List[main_models.AddonNodeTemplate] = None,
        eip_resource: main_models.DescribeAddonTemplateResponseBodyAddonResourcesSpecEipResource = None,
    ):
        # The Elastic Compute Service (ECS) resource configurations of the addon.
        self.ecs_resources = ecs_resources
        # The Elastic IP Address (EIP) configurations of the service.
        self.eip_resource = eip_resource

    def validate(self):
        if self.ecs_resources:
            for v1 in self.ecs_resources:
                 if v1:
                    v1.validate()
        if self.eip_resource:
            self.eip_resource.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EcsResources'] = []
        if self.ecs_resources is not None:
            for k1 in self.ecs_resources:
                result['EcsResources'].append(k1.to_map() if k1 else None)

        if self.eip_resource is not None:
            result['EipResource'] = self.eip_resource.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ecs_resources = []
        if m.get('EcsResources') is not None:
            for k1 in m.get('EcsResources'):
                temp_model = main_models.AddonNodeTemplate()
                self.ecs_resources.append(temp_model.from_map(k1))

        if m.get('EipResource') is not None:
            temp_model = main_models.DescribeAddonTemplateResponseBodyAddonResourcesSpecEipResource()
            self.eip_resource = temp_model.from_map(m.get('EipResource'))

        return self

class DescribeAddonTemplateResponseBodyAddonResourcesSpecEipResource(DaraModel):
    def __init__(
        self,
        auto_create: bool = None,
        bandwidth: str = None,
        eip_instance_id: str = None,
        instance_charge_type: str = None,
        internet_charge_type: str = None,
    ):
        # Indicates whether the EIP is automatically created.
        self.auto_create = auto_create
        # The maximum bandwidth of the EIP. Unit: Mbit/s.
        self.bandwidth = bandwidth
        # The EIP ID.
        self.eip_instance_id = eip_instance_id
        # The billing method of the EIP. Valid values:
        # 
        # *   PostPaid: pay-as-you-go.
        # *   PrePaid: subscription.
        # 
        # Default value: PostPaid
        self.instance_charge_type = instance_charge_type
        # The metering method of the EIP. Valid values:
        # 
        # *   PayByBandwidth: pay by bandwidth.
        # *   PayByTraffic: pay by data transfer.
        # 
        # Valid values of N: 1 to 10.
        self.internet_charge_type = internet_charge_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_create is not None:
            result['AutoCreate'] = self.auto_create

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.eip_instance_id is not None:
            result['EipInstanceId'] = self.eip_instance_id

        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type

        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoCreate') is not None:
            self.auto_create = m.get('AutoCreate')

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('EipInstanceId') is not None:
            self.eip_instance_id = m.get('EipInstanceId')

        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')

        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')

        return self

