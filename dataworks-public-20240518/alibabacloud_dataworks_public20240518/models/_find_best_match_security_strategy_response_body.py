# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class FindBestMatchSecurityStrategyResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.FindBestMatchSecurityStrategyResponseBodyData = None,
        request_id: str = None,
    ):
        # Data object.
        self.data = data
        # **API request ID**
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.FindBestMatchSecurityStrategyResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class FindBestMatchSecurityStrategyResponseBodyData(DaraModel):
    def __init__(
        self,
        edition: str = None,
        edition_display_name: str = None,
        security_strategy: main_models.FindBestMatchSecurityStrategyResponseBodyDataSecurityStrategy = None,
    ):
        # Purchased DataWorks edition.
        self.edition = edition
        # Purchased DataWorks edition name.
        self.edition_display_name = edition_display_name
        # Security policy.
        self.security_strategy = security_strategy

    def validate(self):
        if self.security_strategy:
            self.security_strategy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.edition is not None:
            result['Edition'] = self.edition

        if self.edition_display_name is not None:
            result['EditionDisplayName'] = self.edition_display_name

        if self.security_strategy is not None:
            result['SecurityStrategy'] = self.security_strategy.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Edition') is not None:
            self.edition = m.get('Edition')

        if m.get('EditionDisplayName') is not None:
            self.edition_display_name = m.get('EditionDisplayName')

        if m.get('SecurityStrategy') is not None:
            temp_model = main_models.FindBestMatchSecurityStrategyResponseBodyDataSecurityStrategy()
            self.security_strategy = temp_model.from_map(m.get('SecurityStrategy'))

        return self

class FindBestMatchSecurityStrategyResponseBodyDataSecurityStrategy(DaraModel):
    def __init__(
        self,
        content: main_models.FindBestMatchSecurityStrategyResponseBodyDataSecurityStrategyContent = None,
        control_dw_scope: str = None,
        control_module: str = None,
        control_sub_module: str = None,
        create_time: str = None,
        creator: str = None,
        description: str = None,
        enabled: bool = None,
        id: int = None,
        name: str = None,
        origin_policy_id: int = None,
        schema_name: str = None,
        update_time: str = None,
        updater: str = None,
        workspaces: List[int] = None,
    ):
        # **Policy content**. Refer to the StrategyContent definition.
        self.content = content
        # **Control scope** (Workspace/Tenant).
        self.control_dw_scope = control_dw_scope
        # **Control module**
        self.control_module = control_module
        # **Control sub-module**
        self.control_sub_module = control_sub_module
        # Creation time.
        self.create_time = create_time
        # Creator user ID.
        self.creator = creator
        # **Policy description**
        self.description = description
        # **Whether enabled**
        self.enabled = enabled
        # **Policy ID**
        self.id = id
        # **Policy name**
        self.name = name
        # System default policy source ID.
        self.origin_policy_id = origin_policy_id
        # **Schema template name**
        self.schema_name = schema_name
        # Update time.
        self.update_time = update_time
        # Last updater user ID.
        self.updater = updater
        # **Associated workspace ID list**
        self.workspaces = workspaces

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content.to_map()

        if self.control_dw_scope is not None:
            result['ControlDwScope'] = self.control_dw_scope

        if self.control_module is not None:
            result['ControlModule'] = self.control_module

        if self.control_sub_module is not None:
            result['ControlSubModule'] = self.control_sub_module

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.description is not None:
            result['Description'] = self.description

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.origin_policy_id is not None:
            result['OriginPolicyId'] = self.origin_policy_id

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.updater is not None:
            result['Updater'] = self.updater

        if self.workspaces is not None:
            result['Workspaces'] = self.workspaces

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            temp_model = main_models.FindBestMatchSecurityStrategyResponseBodyDataSecurityStrategyContent()
            self.content = temp_model.from_map(m.get('Content'))

        if m.get('ControlDwScope') is not None:
            self.control_dw_scope = m.get('ControlDwScope')

        if m.get('ControlModule') is not None:
            self.control_module = m.get('ControlModule')

        if m.get('ControlSubModule') is not None:
            self.control_sub_module = m.get('ControlSubModule')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OriginPolicyId') is not None:
            self.origin_policy_id = m.get('OriginPolicyId')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('Updater') is not None:
            self.updater = m.get('Updater')

        if m.get('Workspaces') is not None:
            self.workspaces = m.get('Workspaces')

        return self

class FindBestMatchSecurityStrategyResponseBodyDataSecurityStrategyContent(DaraModel):
    def __init__(
        self,
        control_dw_scope: str = None,
        control_module: str = None,
        control_sub_module: str = None,
        controllers: List[main_models.FindBestMatchSecurityStrategyResponseBodyDataSecurityStrategyContentControllers] = None,
        display_name: str = None,
        display_name_en: str = None,
        name: str = None,
        system_policy_display_name: str = None,
        system_policy_name: str = None,
    ):
        # **Control scope**
        self.control_dw_scope = control_dw_scope
        # **Control module**
        self.control_module = control_module
        # **Control sub-module**
        self.control_sub_module = control_sub_module
        # Controller list.
        # 
        # Note: Valid controllers depend on the selected Schema. Refer to the Controller definition and the controller list of each Schema.
        self.controllers = controllers
        # **Display name**
        self.display_name = display_name
        # **English display name**
        self.display_name_en = display_name_en
        # **Schema name**
        self.name = name
        # System policy display name.
        self.system_policy_display_name = system_policy_display_name
        # System policy name (when not empty, the system automatically creates a default policy).
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
                temp_model = main_models.FindBestMatchSecurityStrategyResponseBodyDataSecurityStrategyContentControllers()
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

class FindBestMatchSecurityStrategyResponseBodyDataSecurityStrategyContentControllers(DaraModel):
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
        # **Basic Edition default value**
        self.basic_edition_default_value = basic_edition_default_value
        # Basic Edition valid value range [min, max].
        self.basic_edition_interval_value = basic_edition_interval_value
        # Controller identifier. For values, see the controller list of each Schema.
        self.controller = controller
        # **Value type (Boolean/Integer/Long/String)**
        self.controller_value_type = controller_value_type
        # Display name.
        self.display_name = display_name
        # **English display name**
        self.display_name_en = display_name_en
        # **Whether this controller is enabled**
        self.enable = enable
        # Enterprise Edition default value.
        self.enterprise_edition_default_value = enterprise_edition_default_value
        # Enterprise Edition valid value range [min, max].
        self.enterprise_edition_interval_value = enterprise_edition_interval_value
        # Professional Edition default value.
        self.professional_edition_default_value = professional_edition_default_value
        # Professional Edition valid value range [min, max].
        self.professional_edition_interval_value = professional_edition_interval_value
        # **Standard Edition default value**
        self.standard_edition_default_value = standard_edition_default_value
        # Standard Edition valid value range [min, max].
        self.standard_edition_interval_value = standard_edition_interval_value
        # **User-configured value. The type depends on ControllerValueType.**
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

