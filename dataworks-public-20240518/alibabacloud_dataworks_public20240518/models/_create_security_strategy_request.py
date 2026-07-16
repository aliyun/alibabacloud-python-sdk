# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class CreateSecurityStrategyRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        content: main_models.CreateSecurityStrategyRequestContent = None,
        control_dw_scope: str = None,
        control_module: str = None,
        control_sub_module: str = None,
        description: str = None,
        name: str = None,
        schema_name: str = None,
        workspaces: List[int] = None,
    ):
        # A client-generated token that ensures request idempotency, preventing duplicate operations if you retry the request.
        self.client_token = client_token
        # The content of the strategy. This value is constrained by the `SecurityStrategySchema`.
        # 
        # This parameter is required.
        self.content = content
        # **The control scope. Valid values: Workspace and Tenant.**
        # 
        # This parameter is required.
        self.control_dw_scope = control_dw_scope
        # **Control module**
        # 
        # This parameter is required.
        self.control_module = control_module
        # **Control submodule**
        self.control_sub_module = control_sub_module
        # **Strategy description**
        self.description = description
        # **Strategy name**
        # 
        # This parameter is required.
        self.name = name
        # **Schema template name**
        # 
        # This parameter is required.
        self.schema_name = schema_name
        # A list of associated workspace IDs.
        self.workspaces = workspaces

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.content is not None:
            result['Content'] = self.content.to_map()

        if self.control_dw_scope is not None:
            result['ControlDwScope'] = self.control_dw_scope

        if self.control_module is not None:
            result['ControlModule'] = self.control_module

        if self.control_sub_module is not None:
            result['ControlSubModule'] = self.control_sub_module

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        if self.workspaces is not None:
            result['Workspaces'] = self.workspaces

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Content') is not None:
            temp_model = main_models.CreateSecurityStrategyRequestContent()
            self.content = temp_model.from_map(m.get('Content'))

        if m.get('ControlDwScope') is not None:
            self.control_dw_scope = m.get('ControlDwScope')

        if m.get('ControlModule') is not None:
            self.control_module = m.get('ControlModule')

        if m.get('ControlSubModule') is not None:
            self.control_sub_module = m.get('ControlSubModule')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('Workspaces') is not None:
            self.workspaces = m.get('Workspaces')

        return self

class CreateSecurityStrategyRequestContent(DaraModel):
    def __init__(
        self,
        control_dw_scope: str = None,
        control_module: str = None,
        control_sub_module: str = None,
        controllers: List[main_models.CreateSecurityStrategyRequestContentControllers] = None,
        display_name: str = None,
        display_name_en: str = None,
        name: str = None,
        system_policy_display_name: str = None,
        system_policy_name: str = None,
    ):
        # The control scope. This corresponds to the `controlDwScope` property of the `SecurityStrategySchema` associated with the current strategy.
        self.control_dw_scope = control_dw_scope
        # The control module. This corresponds to the `controlModule` property of the `SecurityStrategySchema` associated with the current strategy.
        # 
        # This parameter is required.
        self.control_module = control_module
        # The control submodule. This corresponds to the `controlSubModule` property of the `SecurityStrategySchema` associated with the current strategy.
        self.control_sub_module = control_sub_module
        # A list of controllers.
        # 
        # **Note:** Valid controllers depend on the selected schema. For more information, see the controller definitions and the list of controllers for each schema.
        self.controllers = controllers
        # The `displayName` property of the `SecurityStrategySchema` associated with the current strategy.
        self.display_name = display_name
        # The `displayNameEn` property of the `SecurityStrategySchema` associated with the current strategy.
        self.display_name_en = display_name_en
        # The `name` property of the `SecurityStrategySchema` associated with the current strategy.
        # 
        # This parameter is required.
        self.name = name
        # The `systemPolicyDisplayName` property of the `SecurityStrategySchema` associated with the current strategy.
        self.system_policy_display_name = system_policy_display_name
        # The `systemPolicyName` property of the `SecurityStrategySchema` associated with the current strategy.
        self.system_policy_name = system_policy_name

    def validate(self):
        if self.controllers:
            for v1 in self.controllers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.control_dw_scope is not None:
            result['ControlDwScope'] = self.control_dw_scope

        if self.control_module is not None:
            result['ControlModule'] = self.control_module

        if self.control_sub_module is not None:
            result['ControlSubModule'] = self.control_sub_module

        result['Controllers'] = []
        if self.controllers is not None:
            for k1 in self.controllers:
                result['Controllers'].append(k1.to_map() if k1 else None)

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.display_name_en is not None:
            result['DisplayNameEn'] = self.display_name_en

        if self.name is not None:
            result['Name'] = self.name

        if self.system_policy_display_name is not None:
            result['SystemPolicyDisplayName'] = self.system_policy_display_name

        if self.system_policy_name is not None:
            result['SystemPolicyName'] = self.system_policy_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ControlDwScope') is not None:
            self.control_dw_scope = m.get('ControlDwScope')

        if m.get('ControlModule') is not None:
            self.control_module = m.get('ControlModule')

        if m.get('ControlSubModule') is not None:
            self.control_sub_module = m.get('ControlSubModule')

        self.controllers = []
        if m.get('Controllers') is not None:
            for k1 in m.get('Controllers'):
                temp_model = main_models.CreateSecurityStrategyRequestContentControllers()
                self.controllers.append(temp_model.from_map(k1))

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('DisplayNameEn') is not None:
            self.display_name_en = m.get('DisplayNameEn')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SystemPolicyDisplayName') is not None:
            self.system_policy_display_name = m.get('SystemPolicyDisplayName')

        if m.get('SystemPolicyName') is not None:
            self.system_policy_name = m.get('SystemPolicyName')

        return self

class CreateSecurityStrategyRequestContentControllers(DaraModel):
    def __init__(
        self,
        basic_edition_default_value: Any = None,
        basic_edition_interval_value: List[int] = None,
        controller: str = None,
        controller_value_type: str = None,
        display_name: str = None,
        display_name_en: str = None,
        enable: bool = None,
        enterprise_edition_default_value: Any = None,
        enterprise_edition_interval_value: List[int] = None,
        professional_edition_default_value: Any = None,
        professional_edition_interval_value: List[int] = None,
        standard_edition_default_value: Any = None,
        standard_edition_interval_value: List[int] = None,
        user_config_value: Any = None,
    ):
        # The default value for Basic Edition.
        self.basic_edition_default_value = basic_edition_default_value
        # The valid value interval for Basic Edition, in the format `[min, max]`.
        self.basic_edition_interval_value = basic_edition_interval_value
        # The controller identifier. For valid values, see the list of controllers for each schema.
        self.controller = controller
        # The value type. Valid values: `Boolean`, `Integer`, `Long`, and `String`.
        self.controller_value_type = controller_value_type
        # The display name.
        self.display_name = display_name
        # The English display name.
        self.display_name_en = display_name_en
        # Specifies whether to enable this controller.
        self.enable = enable
        # The default value for Enterprise Edition.
        self.enterprise_edition_default_value = enterprise_edition_default_value
        # The valid value interval for Enterprise Edition, in the format `[min, max]`.
        self.enterprise_edition_interval_value = enterprise_edition_interval_value
        # The default value for Professional Edition.
        self.professional_edition_default_value = professional_edition_default_value
        # The valid value interval for Professional Edition, in the format `[min, max]`.
        self.professional_edition_interval_value = professional_edition_interval_value
        # The default value for Standard Edition.
        self.standard_edition_default_value = standard_edition_default_value
        # The valid value interval for Standard Edition, in the format `[min, max]`.
        self.standard_edition_interval_value = standard_edition_interval_value
        # The user-configured value. The type of this value depends on the `ControllerValueType` parameter.
        self.user_config_value = user_config_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.basic_edition_default_value is not None:
            result['BasicEditionDefaultValue'] = self.basic_edition_default_value

        if self.basic_edition_interval_value is not None:
            result['BasicEditionIntervalValue'] = self.basic_edition_interval_value

        if self.controller is not None:
            result['Controller'] = self.controller

        if self.controller_value_type is not None:
            result['ControllerValueType'] = self.controller_value_type

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.display_name_en is not None:
            result['DisplayNameEn'] = self.display_name_en

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.enterprise_edition_default_value is not None:
            result['EnterpriseEditionDefaultValue'] = self.enterprise_edition_default_value

        if self.enterprise_edition_interval_value is not None:
            result['EnterpriseEditionIntervalValue'] = self.enterprise_edition_interval_value

        if self.professional_edition_default_value is not None:
            result['ProfessionalEditionDefaultValue'] = self.professional_edition_default_value

        if self.professional_edition_interval_value is not None:
            result['ProfessionalEditionIntervalValue'] = self.professional_edition_interval_value

        if self.standard_edition_default_value is not None:
            result['StandardEditionDefaultValue'] = self.standard_edition_default_value

        if self.standard_edition_interval_value is not None:
            result['StandardEditionIntervalValue'] = self.standard_edition_interval_value

        if self.user_config_value is not None:
            result['UserConfigValue'] = self.user_config_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BasicEditionDefaultValue') is not None:
            self.basic_edition_default_value = m.get('BasicEditionDefaultValue')

        if m.get('BasicEditionIntervalValue') is not None:
            self.basic_edition_interval_value = m.get('BasicEditionIntervalValue')

        if m.get('Controller') is not None:
            self.controller = m.get('Controller')

        if m.get('ControllerValueType') is not None:
            self.controller_value_type = m.get('ControllerValueType')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('DisplayNameEn') is not None:
            self.display_name_en = m.get('DisplayNameEn')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('EnterpriseEditionDefaultValue') is not None:
            self.enterprise_edition_default_value = m.get('EnterpriseEditionDefaultValue')

        if m.get('EnterpriseEditionIntervalValue') is not None:
            self.enterprise_edition_interval_value = m.get('EnterpriseEditionIntervalValue')

        if m.get('ProfessionalEditionDefaultValue') is not None:
            self.professional_edition_default_value = m.get('ProfessionalEditionDefaultValue')

        if m.get('ProfessionalEditionIntervalValue') is not None:
            self.professional_edition_interval_value = m.get('ProfessionalEditionIntervalValue')

        if m.get('StandardEditionDefaultValue') is not None:
            self.standard_edition_default_value = m.get('StandardEditionDefaultValue')

        if m.get('StandardEditionIntervalValue') is not None:
            self.standard_edition_interval_value = m.get('StandardEditionIntervalValue')

        if m.get('UserConfigValue') is not None:
            self.user_config_value = m.get('UserConfigValue')

        return self

