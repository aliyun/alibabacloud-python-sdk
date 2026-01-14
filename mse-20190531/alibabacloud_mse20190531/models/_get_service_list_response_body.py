# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class GetServiceListResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: List[main_models.GetServiceListResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code returned.
        self.code = code
        # The data entries returned.
        self.data = data
        # The HTTP status code returned.
        self.http_status_code = http_status_code
        # The message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

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

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetServiceListResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetServiceListResponseBodyData(DaraModel):
    def __init__(
        self,
        dubbo_application_name: str = None,
        edas_app_name: str = None,
        group: str = None,
        metadata: Dict[str, Any] = None,
        methods: List[main_models.GetServiceListResponseBodyDataMethods] = None,
        registry_type: str = None,
        service_name: str = None,
        service_type: str = None,
        spring_application_name: str = None,
        version: str = None,
    ):
        # The name of the Dubbo application.
        self.dubbo_application_name = dubbo_application_name
        # The name of the application.
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
        # The version information.
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
                temp_model = main_models.GetServiceListResponseBodyDataMethods()
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

class GetServiceListResponseBodyDataMethods(DaraModel):
    def __init__(
        self,
        method_controller: str = None,
        name: str = None,
        parameter_types: List[str] = None,
        paths: List[str] = None,
        request_methods: List[str] = None,
        return_type: str = None,
    ):
        # The controller of the method.
        self.method_controller = method_controller
        # The name of the method.
        self.name = name
        # The data types of the parameters.
        self.parameter_types = parameter_types
        # The paths.
        self.paths = paths
        # The methods.
        self.request_methods = request_methods
        # The type of the return value.
        self.return_type = return_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.method_controller is not None:
            result['MethodController'] = self.method_controller

        if self.name is not None:
            result['Name'] = self.name

        if self.parameter_types is not None:
            result['ParameterTypes'] = self.parameter_types

        if self.paths is not None:
            result['Paths'] = self.paths

        if self.request_methods is not None:
            result['RequestMethods'] = self.request_methods

        if self.return_type is not None:
            result['ReturnType'] = self.return_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MethodController') is not None:
            self.method_controller = m.get('MethodController')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ParameterTypes') is not None:
            self.parameter_types = m.get('ParameterTypes')

        if m.get('Paths') is not None:
            self.paths = m.get('Paths')

        if m.get('RequestMethods') is not None:
            self.request_methods = m.get('RequestMethods')

        if m.get('ReturnType') is not None:
            self.return_type = m.get('ReturnType')

        return self

