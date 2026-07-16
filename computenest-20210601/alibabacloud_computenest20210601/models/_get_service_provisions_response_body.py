# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_computenest20210601 import models as main_models
from darabonba.model import DaraModel

class GetServiceProvisionsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        service_provisions: List[main_models.GetServiceProvisionsResponseBodyServiceProvisions] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The service details.
        self.service_provisions = service_provisions

    def validate(self):
        if self.service_provisions:
            for v1 in self.service_provisions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ServiceProvisions'] = []
        if self.service_provisions is not None:
            for k1 in self.service_provisions:
                result['ServiceProvisions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.service_provisions = []
        if m.get('ServiceProvisions') is not None:
            for k1 in m.get('ServiceProvisions'):
                temp_model = main_models.GetServiceProvisionsResponseBodyServiceProvisions()
                self.service_provisions.append(temp_model.from_map(k1))

        return self

class GetServiceProvisionsResponseBodyServiceProvisions(DaraModel):
    def __init__(
        self,
        auto_enable_service: bool = None,
        commodity_provisions: List[main_models.GetServiceProvisionsResponseBodyServiceProvisionsCommodityProvisions] = None,
        enable_url: str = None,
        role_provision: main_models.GetServiceProvisionsResponseBodyServiceProvisionsRoleProvision = None,
        service_name: str = None,
        status: str = None,
        status_reason: str = None,
    ):
        # Indicates whether the service is automatically activated as defined in the template. Valid values:
        # 
        # - true: The service is automatically activated.
        # 
        # - false: The service is manually activated.
        self.auto_enable_service = auto_enable_service
        # The commodity details. Some services, such as ACS, require the activation of multiple commodities.
        self.commodity_provisions = commodity_provisions
        # The URL for activating the Alibaba Cloud service.
        # 
        # > This parameter is returned when Status is set to Disabled.
        self.enable_url = enable_url
        # The information about the service role. If this parameter is empty, no service role is associated with the service.
        self.role_provision = role_provision
        # The service name.
        self.service_name = service_name
        # The activation status of the service. Valid values:
        # 
        # - Enabled: The service is activated.
        # 
        # - EnabledByDefault: The service is activated by default.
        # 
        # - Disabled: The service is not activated.
        # 
        # - Unknown: The activation status is unknown.
        self.status = status
        # The reason why the Alibaba Cloud service is not activated or the activation status is unknown.
        # 
        # > This parameter is returned when Status is set to Disabled or Unknown.
        self.status_reason = status_reason

    def validate(self):
        if self.commodity_provisions:
            for v1 in self.commodity_provisions:
                 if v1:
                    v1.validate()
        if self.role_provision:
            self.role_provision.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_enable_service is not None:
            result['AutoEnableService'] = self.auto_enable_service

        result['CommodityProvisions'] = []
        if self.commodity_provisions is not None:
            for k1 in self.commodity_provisions:
                result['CommodityProvisions'].append(k1.to_map() if k1 else None)

        if self.enable_url is not None:
            result['EnableURL'] = self.enable_url

        if self.role_provision is not None:
            result['RoleProvision'] = self.role_provision.to_map()

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.status is not None:
            result['Status'] = self.status

        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoEnableService') is not None:
            self.auto_enable_service = m.get('AutoEnableService')

        self.commodity_provisions = []
        if m.get('CommodityProvisions') is not None:
            for k1 in m.get('CommodityProvisions'):
                temp_model = main_models.GetServiceProvisionsResponseBodyServiceProvisionsCommodityProvisions()
                self.commodity_provisions.append(temp_model.from_map(k1))

        if m.get('EnableURL') is not None:
            self.enable_url = m.get('EnableURL')

        if m.get('RoleProvision') is not None:
            temp_model = main_models.GetServiceProvisionsResponseBodyServiceProvisionsRoleProvision()
            self.role_provision = temp_model.from_map(m.get('RoleProvision'))

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')

        return self

class GetServiceProvisionsResponseBodyServiceProvisionsRoleProvision(DaraModel):
    def __init__(
        self,
        authorization_url: str = None,
        roles: List[main_models.GetServiceProvisionsResponseBodyServiceProvisionsRoleProvisionRoles] = None,
    ):
        # The authorization URL for accessing the cloud resources of the service.
        # This URL is returned if the role is not created.
        self.authorization_url = authorization_url
        # The list of service roles.
        self.roles = roles

    def validate(self):
        if self.roles:
            for v1 in self.roles:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorization_url is not None:
            result['AuthorizationURL'] = self.authorization_url

        result['Roles'] = []
        if self.roles is not None:
            for k1 in self.roles:
                result['Roles'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationURL') is not None:
            self.authorization_url = m.get('AuthorizationURL')

        self.roles = []
        if m.get('Roles') is not None:
            for k1 in m.get('Roles'):
                temp_model = main_models.GetServiceProvisionsResponseBodyServiceProvisionsRoleProvisionRoles()
                self.roles.append(temp_model.from_map(k1))

        return self

class GetServiceProvisionsResponseBodyServiceProvisionsRoleProvisionRoles(DaraModel):
    def __init__(
        self,
        api_for_creation: main_models.GetServiceProvisionsResponseBodyServiceProvisionsRoleProvisionRolesApiForCreation = None,
        created: bool = None,
        function: str = None,
        role_name: str = None,
    ):
        # The information about the API operation used to create the role.
        self.api_for_creation = api_for_creation
        # Indicates whether the role is created. Valid values:
        # 
        # - true: The role is created.
        # 
        # - false: The role is not created.
        self.created = created
        # The purpose of the role.
        # Default value: Default. This value indicates that the role is the default role for the service.
        self.function = function
        # The role name.
        self.role_name = role_name

    def validate(self):
        if self.api_for_creation:
            self.api_for_creation.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_for_creation is not None:
            result['ApiForCreation'] = self.api_for_creation.to_map()

        if self.created is not None:
            result['Created'] = self.created

        if self.function is not None:
            result['Function'] = self.function

        if self.role_name is not None:
            result['RoleName'] = self.role_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiForCreation') is not None:
            temp_model = main_models.GetServiceProvisionsResponseBodyServiceProvisionsRoleProvisionRolesApiForCreation()
            self.api_for_creation = temp_model.from_map(m.get('ApiForCreation'))

        if m.get('Created') is not None:
            self.created = m.get('Created')

        if m.get('Function') is not None:
            self.function = m.get('Function')

        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')

        return self

class GetServiceProvisionsResponseBodyServiceProvisionsRoleProvisionRolesApiForCreation(DaraModel):
    def __init__(
        self,
        api_name: str = None,
        api_product_id: str = None,
        api_type: str = None,
        parameters: Dict[str, Any] = None,
    ):
        # The API operation name.
        self.api_name = api_name
        # The ID of the product to which the API operation belongs.
        self.api_product_id = api_product_id
        # The API type.
        # Valid values:
        # 
        # - Open: public API.
        # 
        # - Inner: internal API.
        self.api_type = api_type
        # The API parameters. ${variable} indicates a dynamic parameter.
        self.parameters = parameters

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_name is not None:
            result['ApiName'] = self.api_name

        if self.api_product_id is not None:
            result['ApiProductId'] = self.api_product_id

        if self.api_type is not None:
            result['ApiType'] = self.api_type

        if self.parameters is not None:
            result['parameters'] = self.parameters

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')

        if m.get('ApiProductId') is not None:
            self.api_product_id = m.get('ApiProductId')

        if m.get('ApiType') is not None:
            self.api_type = m.get('ApiType')

        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')

        return self

class GetServiceProvisionsResponseBodyServiceProvisionsCommodityProvisions(DaraModel):
    def __init__(
        self,
        commodity_code: str = None,
        enable_url: str = None,
        status: str = None,
    ):
        # The commodity code.
        self.commodity_code = commodity_code
        # The URL for activating the commodity.
        self.enable_url = enable_url
        # The activation status of the Alibaba Cloud service. Valid values:
        # 
        # - Enabled: The service is activated.
        # 
        # - Disabled: The service is not activated.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.enable_url is not None:
            result['EnableURL'] = self.enable_url

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('EnableURL') is not None:
            self.enable_url = m.get('EnableURL')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

