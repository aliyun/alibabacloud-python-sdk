# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class ListAppServicesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListAppServicesResponseBodyData] = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        # The HTTP status code that is returned. Valid values:
        # 
        # *   **2xx**: The request was successful.
        # *   **3xx**: The request was redirected.
        # *   **4xx**: The request failed.
        # *   **5xx**: A server error occurred.
        self.code = code
        # The details of the microservice.
        self.data = data
        # The status code. Valid values:
        # 
        # *   If the request was successful, the **ErrorCode** parameter is not returned.
        # *   If the request failed, **ErrorCode** is returned. For more information, see **Error codes** in this topic.
        self.error_code = error_code
        # The message returned. Valid values:
        # 
        # *   If the request was successful, **success** is returned.
        # *   If the request failed, an error message is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success
        # The ID of the trace. The ID is used to query the details of a request.
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

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

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListAppServicesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

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

class ListAppServicesResponseBodyData(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        instance_count: str = None,
        namespace_id: str = None,
        namespace_name: str = None,
        registry_type: str = None,
        security_group_id: str = None,
        service_group: str = None,
        service_name: str = None,
        service_port_and_protocol: Dict[str, str] = None,
        service_ports: List[int] = None,
        service_protocol: str = None,
        service_type: str = None,
        service_version: str = None,
    ):
        # The application ID.
        self.app_id = app_id
        # The name of the application.
        self.app_name = app_name
        # The number of instances of the microservice.
        self.instance_count = instance_count
        # The ID of the namespace to which the application belongs.
        self.namespace_id = namespace_id
        # The name of the namespace.
        self.namespace_name = namespace_name
        # The registry type. Valid values:
        # 
        # *   **0**：SAE Nacos
        # *   **1**: SAE built-in Nacos
        # *   **2**: MSE Nacos
        # *   **9**: SAE Kubernets service
        self.registry_type = registry_type
        # The IDs of the security groups.
        self.security_group_id = security_group_id
        # The group to which the microservice belongs.
        self.service_group = service_group
        # The name of the microservice.
        self.service_name = service_name
        # The ports and protocols.
        self.service_port_and_protocol = service_port_and_protocol
        # The list of ports.
        self.service_ports = service_ports
        # The protocol used by the microservice.
        self.service_protocol = service_protocol
        # The type of the microservice. Valid values:
        # 
        # *   **dubbo**
        # *   **springCloud**
        # *   **hsf**
        # *   **k8sService**
        self.service_type = service_type
        # The version of the microservice.
        self.service_version = service_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name

        if self.registry_type is not None:
            result['RegistryType'] = self.registry_type

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.service_group is not None:
            result['ServiceGroup'] = self.service_group

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.service_port_and_protocol is not None:
            result['ServicePortAndProtocol'] = self.service_port_and_protocol

        if self.service_ports is not None:
            result['ServicePorts'] = self.service_ports

        if self.service_protocol is not None:
            result['ServiceProtocol'] = self.service_protocol

        if self.service_type is not None:
            result['ServiceType'] = self.service_type

        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')

        if m.get('RegistryType') is not None:
            self.registry_type = m.get('RegistryType')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('ServiceGroup') is not None:
            self.service_group = m.get('ServiceGroup')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('ServicePortAndProtocol') is not None:
            self.service_port_and_protocol = m.get('ServicePortAndProtocol')

        if m.get('ServicePorts') is not None:
            self.service_ports = m.get('ServicePorts')

        if m.get('ServiceProtocol') is not None:
            self.service_protocol = m.get('ServiceProtocol')

        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')

        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')

        return self

