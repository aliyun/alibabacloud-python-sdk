# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class ListAuthPolicyResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.ListAuthPolicyResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code.
        self.code = code
        # The details of the data.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The returned message.
        self.message = message
        # The request ID.
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
            temp_model = main_models.ListAuthPolicyResponseBodyData()
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

class ListAuthPolicyResponseBodyData(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        result: List[main_models.ListAuthPolicyResponseBodyDataResult] = None,
        total_size: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The data returned.
        self.result = result
        # The total number of entries.
        self.total_size = total_size

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.total_size is not None:
            result['TotalSize'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListAuthPolicyResponseBodyDataResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')

        return self

class ListAuthPolicyResponseBodyDataResult(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        app_id: str = None,
        app_name: str = None,
        auth_rule: List[main_models.ListAuthPolicyResponseBodyDataResultAuthRule] = None,
        auth_type: int = None,
        enable: bool = None,
        id: int = None,
        k_8s_namespace: str = None,
        name: str = None,
        namespace_id: str = None,
        protocol: str = None,
        region_id: str = None,
        source: str = None,
        status: int = None,
    ):
        # The ID of the Alibaba Cloud account to which the resource belongs.
        self.account_id = account_id
        # The application ID.
        self.app_id = app_id
        # The application name.
        self.app_name = app_name
        # The content of the service authentication rule.
        self.auth_rule = auth_rule
        # The rule type. Valid values:
        # 
        # *   0: by application
        # *   1: by namespace
        self.auth_type = auth_type
        # Indicates whether the rule was enabled or disabled. Valid values:
        # 
        # *   `true`: enabled
        # *   `false`: disabled
        self.enable = enable
        # The rule ID.
        self.id = id
        # The namespace.
        self.k_8s_namespace = k_8s_namespace
        # The name of the authentication rule.
        self.name = name
        # The namespace ID.
        self.namespace_id = namespace_id
        # The protocol type. Valid values:
        # 
        # *   **SPRING_CLOUD**
        # *   **DUBBO**
        # *   **istio**
        self.protocol = protocol
        # The region ID.
        self.region_id = region_id
        # The source of the application.
        self.source = source
        # The status.
        self.status = status

    def validate(self):
        if self.auth_rule:
            for v1 in self.auth_rule:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        result['AuthRule'] = []
        if self.auth_rule is not None:
            for k1 in self.auth_rule:
                result['AuthRule'].append(k1.to_map() if k1 else None)

        if self.auth_type is not None:
            result['AuthType'] = self.auth_type

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.id is not None:
            result['Id'] = self.id

        if self.k_8s_namespace is not None:
            result['K8sNamespace'] = self.k_8s_namespace

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.source is not None:
            result['Source'] = self.source

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        self.auth_rule = []
        if m.get('AuthRule') is not None:
            for k1 in m.get('AuthRule'):
                temp_model = main_models.ListAuthPolicyResponseBodyDataResultAuthRule()
                self.auth_rule.append(temp_model.from_map(k1))

        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('K8sNamespace') is not None:
            self.k_8s_namespace = m.get('K8sNamespace')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class ListAuthPolicyResponseBodyDataResultAuthRule(DaraModel):
    def __init__(
        self,
        app_ids: List[str] = None,
        auth_type: int = None,
        black: bool = None,
        k_8s_namespaces: List[str] = None,
        method: main_models.ListAuthPolicyResponseBodyDataResultAuthRuleMethod = None,
        path: str = None,
    ):
        # The IDs of applications.
        self.app_ids = app_ids
        # The rule type. Valid values:
        # 
        # *   0: by application
        # *   1: by namespace
        self.auth_type = auth_type
        # Indicates whether the rule is a blacklist rule.
        self.black = black
        # The queried namespaces.
        self.k_8s_namespaces = k_8s_namespaces
        # The request method.
        self.method = method
        # The service path.
        self.path = path

    def validate(self):
        if self.method:
            self.method.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_ids is not None:
            result['AppIds'] = self.app_ids

        if self.auth_type is not None:
            result['AuthType'] = self.auth_type

        if self.black is not None:
            result['Black'] = self.black

        if self.k_8s_namespaces is not None:
            result['K8sNamespaces'] = self.k_8s_namespaces

        if self.method is not None:
            result['Method'] = self.method.to_map()

        if self.path is not None:
            result['Path'] = self.path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppIds') is not None:
            self.app_ids = m.get('AppIds')

        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')

        if m.get('Black') is not None:
            self.black = m.get('Black')

        if m.get('K8sNamespaces') is not None:
            self.k_8s_namespaces = m.get('K8sNamespaces')

        if m.get('Method') is not None:
            temp_model = main_models.ListAuthPolicyResponseBodyDataResultAuthRuleMethod()
            self.method = temp_model.from_map(m.get('Method'))

        if m.get('Path') is not None:
            self.path = m.get('Path')

        return self

class ListAuthPolicyResponseBodyDataResultAuthRuleMethod(DaraModel):
    def __init__(
        self,
        group: str = None,
        name: str = None,
        parameter_types: List[str] = None,
        return_type: str = None,
        service_name: str = None,
        version: str = None,
    ):
        # The group.
        self.group = group
        # The method name.
        self.name = name
        # The types of request parameters.
        self.parameter_types = parameter_types
        # The type of the return value.
        self.return_type = return_type
        # The service name.
        self.service_name = service_name
        # The method version.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group is not None:
            result['Group'] = self.group

        if self.name is not None:
            result['Name'] = self.name

        if self.parameter_types is not None:
            result['ParameterTypes'] = self.parameter_types

        if self.return_type is not None:
            result['ReturnType'] = self.return_type

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Group') is not None:
            self.group = m.get('Group')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ParameterTypes') is not None:
            self.parameter_types = m.get('ParameterTypes')

        if m.get('ReturnType') is not None:
            self.return_type = m.get('ReturnType')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

