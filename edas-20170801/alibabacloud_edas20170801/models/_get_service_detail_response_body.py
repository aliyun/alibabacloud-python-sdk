# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class GetServiceDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetServiceDetailResponseBodyData = None,
        message: str = None,
        success: bool = None,
    ):
        # The HTTP status code returned.
        self.code = code
        # The data structure.
        self.data = data
        # The message returned for the request.
        self.message = message
        # Indicates whether the call was successful.
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

        if self.message is not None:
            result['Message'] = self.message

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetServiceDetailResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetServiceDetailResponseBodyData(DaraModel):
    def __init__(
        self,
        dubbo_application_name: str = None,
        edas_app_name: str = None,
        group: str = None,
        metadata: str = None,
        methods: List[main_models.GetServiceDetailResponseBodyDataMethods] = None,
        registry_type: str = None,
        service_name: str = None,
        service_type: str = None,
        spring_application_name: str = None,
        version: str = None,
    ):
        # The name of the Dubbo application.
        self.dubbo_application_name = dubbo_application_name
        # The name of the Enterprise Distributed Application Service (EDAS) application.
        self.edas_app_name = edas_app_name
        # The group.
        self.group = group
        # The metadata.
        self.metadata = metadata
        # The methods.
        self.methods = methods
        # The type of the service registry.
        self.registry_type = registry_type
        # The name of the service.
        self.service_name = service_name
        # The type of the service.
        self.service_type = service_type
        # The name of the Spring application.
        self.spring_application_name = spring_application_name
        # The version number.
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

        if self.registry_type is not None:
            result['RegistryType'] = self.registry_type

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

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
                temp_model = main_models.GetServiceDetailResponseBodyDataMethods()
                self.methods.append(temp_model.from_map(k1))

        if m.get('RegistryType') is not None:
            self.registry_type = m.get('RegistryType')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')

        if m.get('SpringApplicationName') is not None:
            self.spring_application_name = m.get('SpringApplicationName')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class GetServiceDetailResponseBodyDataMethods(DaraModel):
    def __init__(
        self,
        method_controller: str = None,
        name: str = None,
        name_detail: str = None,
        parameter_definitions: str = None,
        parameter_details: str = None,
        parameter_names: str = None,
        parameter_types: str = None,
        paths: str = None,
        request_methods: str = None,
        return_definition: main_models.GetServiceDetailResponseBodyDataMethodsReturnDefinition = None,
        return_details: str = None,
        return_type: str = None,
    ):
        # The controllers.
        self.method_controller = method_controller
        # The name of the service.
        self.name = name
        # The specific name.
        self.name_detail = name_detail
        # The parameter definitions.
        self.parameter_definitions = parameter_definitions
        # The parameter details.
        self.parameter_details = parameter_details
        # The parameter names.
        self.parameter_names = parameter_names
        # The parameter types.
        self.parameter_types = parameter_types
        # The method paths.
        self.paths = paths
        # The request methods.
        self.request_methods = request_methods
        # The definition of the value returned by the method.
        self.return_definition = return_definition
        # The response details.
        self.return_details = return_details
        # The type of the response.
        self.return_type = return_type

    def validate(self):
        if self.return_definition:
            self.return_definition.validate()

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

        if self.parameter_definitions is not None:
            result['ParameterDefinitions'] = self.parameter_definitions

        if self.parameter_details is not None:
            result['ParameterDetails'] = self.parameter_details

        if self.parameter_names is not None:
            result['ParameterNames'] = self.parameter_names

        if self.parameter_types is not None:
            result['ParameterTypes'] = self.parameter_types

        if self.paths is not None:
            result['Paths'] = self.paths

        if self.request_methods is not None:
            result['RequestMethods'] = self.request_methods

        if self.return_definition is not None:
            result['ReturnDefinition'] = self.return_definition.to_map()

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

        if m.get('ParameterDefinitions') is not None:
            self.parameter_definitions = m.get('ParameterDefinitions')

        if m.get('ParameterDetails') is not None:
            self.parameter_details = m.get('ParameterDetails')

        if m.get('ParameterNames') is not None:
            self.parameter_names = m.get('ParameterNames')

        if m.get('ParameterTypes') is not None:
            self.parameter_types = m.get('ParameterTypes')

        if m.get('Paths') is not None:
            self.paths = m.get('Paths')

        if m.get('RequestMethods') is not None:
            self.request_methods = m.get('RequestMethods')

        if m.get('ReturnDefinition') is not None:
            temp_model = main_models.GetServiceDetailResponseBodyDataMethodsReturnDefinition()
            self.return_definition = temp_model.from_map(m.get('ReturnDefinition'))

        if m.get('ReturnDetails') is not None:
            self.return_details = m.get('ReturnDetails')

        if m.get('ReturnType') is not None:
            self.return_type = m.get('ReturnType')

        return self

class GetServiceDetailResponseBodyDataMethodsReturnDefinition(DaraModel):
    def __init__(
        self,
        id: str = None,
        type: str = None,
    ):
        # The ID of the return value.
        self.id = id
        # The type of the response.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

