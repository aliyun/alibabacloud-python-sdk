# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class DescribeAppServiceDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeAppServiceDetailResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        # The HTTP status code. Valid values:
        # 
        # - **2xx**: indicates that the call was successful.
        # - **3xx**: indicates that the call was redirected.
        # - **4xx**: indicates that the call failed.
        # - **5xx**: indicates that a server error occurred.
        self.code = code
        # The data that is returned.
        self.data = data
        # The returned error code. Valid values:
        # 
        # - If the call is successful, the **ErrorCode** parameter is not returned.
        # - If the call fails, the **ErrorCode** parameter is returned. For more information, see the "**Error codes**" section of this topic.
        self.error_code = error_code
        # The returned information.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the meta data was obtained. Valid values:
        # 
        # *   **true**: The metadata was obtained.
        # *   **false**: The metadata failed to be obtained.
        self.success = success
        # The ID of the trace. The ID is used to query the details of a request.
        self.trace_id = trace_id

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

        if m.get('Data') is not None:
            temp_model = main_models.DescribeAppServiceDetailResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

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

class DescribeAppServiceDetailResponseBodyData(DaraModel):
    def __init__(
        self,
        dubbo_application_name: str = None,
        edas_app_name: str = None,
        group: str = None,
        metadata: Dict[str, Any] = None,
        methods: List[main_models.DescribeAppServiceDetailResponseBodyDataMethods] = None,
        service_name: str = None,
        service_ports: List[int] = None,
        service_protocol: str = None,
        service_tags: List[str] = None,
        service_type: str = None,
        spring_application_name: str = None,
        version: str = None,
    ):
        # The name of the Dubbo application.
        self.dubbo_application_name = dubbo_application_name
        # The name of the application.
        self.edas_app_name = edas_app_name
        # The group to which the service belongs. You can create a custom group.
        self.group = group
        # The metadata. Example: `{side: "provider", port: "18081", preserved: {register: {source: "SPRING_CLOUD"}},…}`.
        self.metadata = metadata
        # The methods.
        self.methods = methods
        # The name of the service.
        self.service_name = service_name
        # The port used by the service.
        self.service_ports = service_ports
        # The protocol used by the service.
        self.service_protocol = service_protocol
        # The tag of the service.
        self.service_tags = service_tags
        # The type of the service. Valid values:
        # 
        # *   **dubbo**
        # *   **springCloud**
        self.service_type = service_type
        # The name of the Spring Cloud application.
        self.spring_application_name = spring_application_name
        # The version of the service. You can create a custom version.
        self.version = version

    def validate(self):
        if self.methods:
            for v1 in self.methods:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dubbo_application_name is not None:
            result['DubboApplicationName'] = self.dubbo_application_name

        if self.edas_app_name is not None:
            result['EdasAppName'] = self.edas_app_name

        if self.group is not None:
            result['Group'] = self.group

        if self.metadata is not None:
            result['Metadata'] = self.metadata

        result['Methods'] = []
        if self.methods is not None:
            for k1 in self.methods:
                result['Methods'].append(k1.to_map() if k1 else None)

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.service_ports is not None:
            result['ServicePorts'] = self.service_ports

        if self.service_protocol is not None:
            result['ServiceProtocol'] = self.service_protocol

        if self.service_tags is not None:
            result['ServiceTags'] = self.service_tags

        if self.service_type is not None:
            result['ServiceType'] = self.service_type

        if self.spring_application_name is not None:
            result['SpringApplicationName'] = self.spring_application_name

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DubboApplicationName') is not None:
            self.dubbo_application_name = m.get('DubboApplicationName')

        if m.get('EdasAppName') is not None:
            self.edas_app_name = m.get('EdasAppName')

        if m.get('Group') is not None:
            self.group = m.get('Group')

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        self.methods = []
        if m.get('Methods') is not None:
            for k1 in m.get('Methods'):
                temp_model = main_models.DescribeAppServiceDetailResponseBodyDataMethods()
                self.methods.append(temp_model.from_map(k1))

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('ServicePorts') is not None:
            self.service_ports = m.get('ServicePorts')

        if m.get('ServiceProtocol') is not None:
            self.service_protocol = m.get('ServiceProtocol')

        if m.get('ServiceTags') is not None:
            self.service_tags = m.get('ServiceTags')

        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')

        if m.get('SpringApplicationName') is not None:
            self.spring_application_name = m.get('SpringApplicationName')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class DescribeAppServiceDetailResponseBodyDataMethods(DaraModel):
    def __init__(
        self,
        method_controller: str = None,
        name: str = None,
        name_detail: str = None,
        parameter_definitions: List[main_models.DescribeAppServiceDetailResponseBodyDataMethodsParameterDefinitions] = None,
        parameter_details: List[str] = None,
        parameter_types: List[str] = None,
        paths: List[str] = None,
        request_methods: List[str] = None,
        return_details: str = None,
        return_type: str = None,
    ):
        # The class to which the method belongs.
        self.method_controller = method_controller
        # The name of the method.
        self.name = name
        # The details of the method.
        self.name_detail = name_detail
        # The definition of the parameter.
        self.parameter_definitions = parameter_definitions
        # The details of the parameters.
        self.parameter_details = parameter_details
        # The types of the parameters.
        self.parameter_types = parameter_types
        # The request paths. Format:
        # 
        # `/path`
        self.paths = paths
        # The request methods. Valid values:
        # 
        # *   **GET**
        # *   **ALL**
        self.request_methods = request_methods
        # The details of the response.
        self.return_details = return_details
        # The data format of the response.
        self.return_type = return_type

    def validate(self):
        if self.parameter_definitions:
            for v1 in self.parameter_definitions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.method_controller is not None:
            result['MethodController'] = self.method_controller

        if self.name is not None:
            result['Name'] = self.name

        if self.name_detail is not None:
            result['NameDetail'] = self.name_detail

        result['ParameterDefinitions'] = []
        if self.parameter_definitions is not None:
            for k1 in self.parameter_definitions:
                result['ParameterDefinitions'].append(k1.to_map() if k1 else None)

        if self.parameter_details is not None:
            result['ParameterDetails'] = self.parameter_details

        if self.parameter_types is not None:
            result['ParameterTypes'] = self.parameter_types

        if self.paths is not None:
            result['Paths'] = self.paths

        if self.request_methods is not None:
            result['RequestMethods'] = self.request_methods

        if self.return_details is not None:
            result['ReturnDetails'] = self.return_details

        if self.return_type is not None:
            result['ReturnType'] = self.return_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MethodController') is not None:
            self.method_controller = m.get('MethodController')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NameDetail') is not None:
            self.name_detail = m.get('NameDetail')

        self.parameter_definitions = []
        if m.get('ParameterDefinitions') is not None:
            for k1 in m.get('ParameterDefinitions'):
                temp_model = main_models.DescribeAppServiceDetailResponseBodyDataMethodsParameterDefinitions()
                self.parameter_definitions.append(temp_model.from_map(k1))

        if m.get('ParameterDetails') is not None:
            self.parameter_details = m.get('ParameterDetails')

        if m.get('ParameterTypes') is not None:
            self.parameter_types = m.get('ParameterTypes')

        if m.get('Paths') is not None:
            self.paths = m.get('Paths')

        if m.get('RequestMethods') is not None:
            self.request_methods = m.get('RequestMethods')

        if m.get('ReturnDetails') is not None:
            self.return_details = m.get('ReturnDetails')

        if m.get('ReturnType') is not None:
            self.return_type = m.get('ReturnType')

        return self

class DescribeAppServiceDetailResponseBodyDataMethodsParameterDefinitions(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        type: str = None,
    ):
        # The description of the parameter.
        self.description = description
        # The name of the parameter.
        self.name = name
        # The type of the parameter.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

