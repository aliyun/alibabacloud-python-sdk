# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class GetGatewayServiceDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetGatewayServiceDetailResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code returned.
        self.code = code
        # The data returned.
        self.data = data
        # The HTTP status code returned.
        self.http_status_code = http_status_code
        # The message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   `true`: The request was successful.
        # *   `false`: The request failed.
        self.success = success

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

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetGatewayServiceDetailResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetGatewayServiceDetailResponseBodyData(DaraModel):
    def __init__(
        self,
        dns_server_list: List[str] = None,
        gateway_id: int = None,
        gateway_traffic_policy: main_models.TrafficPolicy = None,
        gateway_unique_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        group_name: str = None,
        health_check: str = None,
        health_status: str = None,
        id: int = None,
        ips: List[str] = None,
        label_details: List[main_models.GetGatewayServiceDetailResponseBodyDataLabelDetails] = None,
        meta_info: str = None,
        name: str = None,
        namespace: str = None,
        port_traffic_policy_list: List[main_models.GetGatewayServiceDetailResponseBodyDataPortTrafficPolicyList] = None,
        ports: List[int] = None,
        service_fqdn: str = None,
        service_name_in_registry: str = None,
        service_port: int = None,
        service_protocol: str = None,
        source_id: int = None,
        source_type: str = None,
        version_details: List[main_models.GetGatewayServiceDetailResponseBodyDataVersionDetails] = None,
        versions: List[main_models.GetGatewayServiceDetailResponseBodyDataVersions] = None,
    ):
        self.dns_server_list = dns_server_list
        # The ID of the gateway.
        self.gateway_id = gateway_id
        # The traffic policy of the service.
        self.gateway_traffic_policy = gateway_traffic_policy
        # The unique ID of the gateway.
        self.gateway_unique_id = gateway_unique_id
        # The creation time.
        self.gmt_create = gmt_create
        # The last modification time.
        self.gmt_modified = gmt_modified
        # The name of the group.
        self.group_name = group_name
        # Indicates whether the health check is enabled.
        self.health_check = health_check
        # The status of the health check. Valid values:
        self.health_status = health_status
        # The ID of the service.
        self.id = id
        # The IP address of the service.
        self.ips = ips
        # The details of the tag.
        self.label_details = label_details
        # The basic information about the service.
        self.meta_info = meta_info
        # The name of the service.
        self.name = name
        # The namespace.
        self.namespace = namespace
        # The traffic policy of service ports.
        self.port_traffic_policy_list = port_traffic_policy_list
        # The array of service ports.
        self.ports = ports
        self.service_fqdn = service_fqdn
        # The name of the service registered with the service registry.
        self.service_name_in_registry = service_name_in_registry
        self.service_port = service_port
        # The protocol of the service.
        self.service_protocol = service_protocol
        # The ID of the service source.
        self.source_id = source_id
        # The source type of the service.
        self.source_type = source_type
        # The details of versions.
        self.version_details = version_details
        # The service version. This parameter is deprecated.
        self.versions = versions

    def validate(self):
        if self.gateway_traffic_policy:
            self.gateway_traffic_policy.validate()
        if self.label_details:
            for v1 in self.label_details:
                 if v1:
                    v1.validate()
        if self.port_traffic_policy_list:
            for v1 in self.port_traffic_policy_list:
                 if v1:
                    v1.validate()
        if self.version_details:
            for v1 in self.version_details:
                 if v1:
                    v1.validate()
        if self.versions:
            for v1 in self.versions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dns_server_list is not None:
            result['DnsServerList'] = self.dns_server_list

        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id

        if self.gateway_traffic_policy is not None:
            result['GatewayTrafficPolicy'] = self.gateway_traffic_policy.to_map()

        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.health_check is not None:
            result['HealthCheck'] = self.health_check

        if self.health_status is not None:
            result['HealthStatus'] = self.health_status

        if self.id is not None:
            result['Id'] = self.id

        if self.ips is not None:
            result['Ips'] = self.ips

        result['LabelDetails'] = []
        if self.label_details is not None:
            for k1 in self.label_details:
                result['LabelDetails'].append(k1.to_map() if k1 else None)

        if self.meta_info is not None:
            result['MetaInfo'] = self.meta_info

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        result['PortTrafficPolicyList'] = []
        if self.port_traffic_policy_list is not None:
            for k1 in self.port_traffic_policy_list:
                result['PortTrafficPolicyList'].append(k1.to_map() if k1 else None)

        if self.ports is not None:
            result['Ports'] = self.ports

        if self.service_fqdn is not None:
            result['ServiceFQDN'] = self.service_fqdn

        if self.service_name_in_registry is not None:
            result['ServiceNameInRegistry'] = self.service_name_in_registry

        if self.service_port is not None:
            result['ServicePort'] = self.service_port

        if self.service_protocol is not None:
            result['ServiceProtocol'] = self.service_protocol

        if self.source_id is not None:
            result['SourceId'] = self.source_id

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        result['VersionDetails'] = []
        if self.version_details is not None:
            for k1 in self.version_details:
                result['VersionDetails'].append(k1.to_map() if k1 else None)

        result['Versions'] = []
        if self.versions is not None:
            for k1 in self.versions:
                result['Versions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DnsServerList') is not None:
            self.dns_server_list = m.get('DnsServerList')

        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')

        if m.get('GatewayTrafficPolicy') is not None:
            temp_model = main_models.TrafficPolicy()
            self.gateway_traffic_policy = temp_model.from_map(m.get('GatewayTrafficPolicy'))

        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('HealthCheck') is not None:
            self.health_check = m.get('HealthCheck')

        if m.get('HealthStatus') is not None:
            self.health_status = m.get('HealthStatus')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Ips') is not None:
            self.ips = m.get('Ips')

        self.label_details = []
        if m.get('LabelDetails') is not None:
            for k1 in m.get('LabelDetails'):
                temp_model = main_models.GetGatewayServiceDetailResponseBodyDataLabelDetails()
                self.label_details.append(temp_model.from_map(k1))

        if m.get('MetaInfo') is not None:
            self.meta_info = m.get('MetaInfo')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        self.port_traffic_policy_list = []
        if m.get('PortTrafficPolicyList') is not None:
            for k1 in m.get('PortTrafficPolicyList'):
                temp_model = main_models.GetGatewayServiceDetailResponseBodyDataPortTrafficPolicyList()
                self.port_traffic_policy_list.append(temp_model.from_map(k1))

        if m.get('Ports') is not None:
            self.ports = m.get('Ports')

        if m.get('ServiceFQDN') is not None:
            self.service_fqdn = m.get('ServiceFQDN')

        if m.get('ServiceNameInRegistry') is not None:
            self.service_name_in_registry = m.get('ServiceNameInRegistry')

        if m.get('ServicePort') is not None:
            self.service_port = m.get('ServicePort')

        if m.get('ServiceProtocol') is not None:
            self.service_protocol = m.get('ServiceProtocol')

        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        self.version_details = []
        if m.get('VersionDetails') is not None:
            for k1 in m.get('VersionDetails'):
                temp_model = main_models.GetGatewayServiceDetailResponseBodyDataVersionDetails()
                self.version_details.append(temp_model.from_map(k1))

        self.versions = []
        if m.get('Versions') is not None:
            for k1 in m.get('Versions'):
                temp_model = main_models.GetGatewayServiceDetailResponseBodyDataVersions()
                self.versions.append(temp_model.from_map(k1))

        return self

class GetGatewayServiceDetailResponseBodyDataVersions(DaraModel):
    def __init__(
        self,
        label: str = None,
        type: str = None,
        value: str = None,
    ):
        # The tag.
        self.label = label
        # The type.
        self.type = type
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label is not None:
            result['Label'] = self.label

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetGatewayServiceDetailResponseBodyDataVersionDetails(DaraModel):
    def __init__(
        self,
        endpoint_num: int = None,
        endpoint_num_percent: str = None,
        service_version: main_models.GetGatewayServiceDetailResponseBodyDataVersionDetailsServiceVersion = None,
    ):
        # The number of instances.
        self.endpoint_num = endpoint_num
        # The percentage of instances.
        self.endpoint_num_percent = endpoint_num_percent
        # The service version.
        self.service_version = service_version

    def validate(self):
        if self.service_version:
            self.service_version.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.endpoint_num is not None:
            result['EndpointNum'] = self.endpoint_num

        if self.endpoint_num_percent is not None:
            result['EndpointNumPercent'] = self.endpoint_num_percent

        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointNum') is not None:
            self.endpoint_num = m.get('EndpointNum')

        if m.get('EndpointNumPercent') is not None:
            self.endpoint_num_percent = m.get('EndpointNumPercent')

        if m.get('ServiceVersion') is not None:
            temp_model = main_models.GetGatewayServiceDetailResponseBodyDataVersionDetailsServiceVersion()
            self.service_version = temp_model.from_map(m.get('ServiceVersion'))

        return self

class GetGatewayServiceDetailResponseBodyDataVersionDetailsServiceVersion(DaraModel):
    def __init__(
        self,
        labels: List[main_models.GetGatewayServiceDetailResponseBodyDataVersionDetailsServiceVersionLabels] = None,
        name: str = None,
    ):
        # The tag.
        self.labels = labels
        # The version number.
        self.name = name

    def validate(self):
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.GetGatewayServiceDetailResponseBodyDataVersionDetailsServiceVersionLabels()
                self.labels.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class GetGatewayServiceDetailResponseBodyDataVersionDetailsServiceVersionLabels(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag.
        self.key = key
        # The tag value.
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

class GetGatewayServiceDetailResponseBodyDataPortTrafficPolicyList(DaraModel):
    def __init__(
        self,
        gateway_unique_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        service_id: int = None,
        service_port: int = None,
        traffic_policy: main_models.TrafficPolicy = None,
    ):
        # The unique ID of the gateway.
        self.gateway_unique_id = gateway_unique_id
        # The creation time.
        self.gmt_create = gmt_create
        # The modification time.
        self.gmt_modified = gmt_modified
        # The port ID.
        self.id = id
        # The service ID.
        self.service_id = service_id
        # The service port number.
        self.service_port = service_port
        # The traffic policy.
        self.traffic_policy = traffic_policy

    def validate(self):
        if self.traffic_policy:
            self.traffic_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.service_port is not None:
            result['ServicePort'] = self.service_port

        if self.traffic_policy is not None:
            result['TrafficPolicy'] = self.traffic_policy.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ServicePort') is not None:
            self.service_port = m.get('ServicePort')

        if m.get('TrafficPolicy') is not None:
            temp_model = main_models.TrafficPolicy()
            self.traffic_policy = temp_model.from_map(m.get('TrafficPolicy'))

        return self

class GetGatewayServiceDetailResponseBodyDataLabelDetails(DaraModel):
    def __init__(
        self,
        key: str = None,
        values: List[str] = None,
    ):
        # The tag.
        self.key = key
        # The tag value.
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

