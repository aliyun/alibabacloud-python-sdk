# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class SetIdentityProviderAuthnConfigurationRequest(DaraModel):
    def __init__(
        self,
        auto_create_user_config: main_models.SetIdentityProviderAuthnConfigurationRequestAutoCreateUserConfig = None,
        auto_update_user_config: main_models.SetIdentityProviderAuthnConfigurationRequestAutoUpdateUserConfig = None,
        binding_config: main_models.SetIdentityProviderAuthnConfigurationRequestBindingConfig = None,
        identity_provider_id: str = None,
        instance_id: str = None,
        ldap_authn_config: main_models.SetIdentityProviderAuthnConfigurationRequestLdapAuthnConfig = None,
    ):
        # 自动创建账户账户规则配置。
        self.auto_create_user_config = auto_create_user_config
        self.auto_update_user_config = auto_update_user_config
        # 账户绑定规则配置
        self.binding_config = binding_config
        # IDaaS的身份提供方主键id
        # 
        # This parameter is required.
        self.identity_provider_id = identity_provider_id
        # IDaaS EIAM实例的ID。
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # AD/LDAP配置
        self.ldap_authn_config = ldap_authn_config

    def validate(self):
        if self.auto_create_user_config:
            self.auto_create_user_config.validate()
        if self.auto_update_user_config:
            self.auto_update_user_config.validate()
        if self.binding_config:
            self.binding_config.validate()
        if self.ldap_authn_config:
            self.ldap_authn_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_create_user_config is not None:
            result['AutoCreateUserConfig'] = self.auto_create_user_config.to_map()

        if self.auto_update_user_config is not None:
            result['AutoUpdateUserConfig'] = self.auto_update_user_config.to_map()

        if self.binding_config is not None:
            result['BindingConfig'] = self.binding_config.to_map()

        if self.identity_provider_id is not None:
            result['IdentityProviderId'] = self.identity_provider_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.ldap_authn_config is not None:
            result['LdapAuthnConfig'] = self.ldap_authn_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoCreateUserConfig') is not None:
            temp_model = main_models.SetIdentityProviderAuthnConfigurationRequestAutoCreateUserConfig()
            self.auto_create_user_config = temp_model.from_map(m.get('AutoCreateUserConfig'))

        if m.get('AutoUpdateUserConfig') is not None:
            temp_model = main_models.SetIdentityProviderAuthnConfigurationRequestAutoUpdateUserConfig()
            self.auto_update_user_config = temp_model.from_map(m.get('AutoUpdateUserConfig'))

        if m.get('BindingConfig') is not None:
            temp_model = main_models.SetIdentityProviderAuthnConfigurationRequestBindingConfig()
            self.binding_config = temp_model.from_map(m.get('BindingConfig'))

        if m.get('IdentityProviderId') is not None:
            self.identity_provider_id = m.get('IdentityProviderId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LdapAuthnConfig') is not None:
            temp_model = main_models.SetIdentityProviderAuthnConfigurationRequestLdapAuthnConfig()
            self.ldap_authn_config = temp_model.from_map(m.get('LdapAuthnConfig'))

        return self

class SetIdentityProviderAuthnConfigurationRequestLdapAuthnConfig(DaraModel):
    def __init__(
        self,
        auto_update_password_status: str = None,
        user_login_identifier: str = None,
        user_object_class: str = None,
    ):
        # 是否支持自动更新密码
        self.auto_update_password_status = auto_update_password_status
        # 用户登录标识
        self.user_login_identifier = user_login_identifier
        # 用户ObjectClass
        self.user_object_class = user_object_class

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_update_password_status is not None:
            result['AutoUpdatePasswordStatus'] = self.auto_update_password_status

        if self.user_login_identifier is not None:
            result['UserLoginIdentifier'] = self.user_login_identifier

        if self.user_object_class is not None:
            result['UserObjectClass'] = self.user_object_class

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoUpdatePasswordStatus') is not None:
            self.auto_update_password_status = m.get('AutoUpdatePasswordStatus')

        if m.get('UserLoginIdentifier') is not None:
            self.user_login_identifier = m.get('UserLoginIdentifier')

        if m.get('UserObjectClass') is not None:
            self.user_object_class = m.get('UserObjectClass')

        return self

class SetIdentityProviderAuthnConfigurationRequestBindingConfig(DaraModel):
    def __init__(
        self,
        auto_match_user_profile_expressions: List[main_models.SetIdentityProviderAuthnConfigurationRequestBindingConfigAutoMatchUserProfileExpressions] = None,
        auto_match_user_status: str = None,
        mapping_binding_status: str = None,
    ):
        # 自动匹配账户的规则
        self.auto_match_user_profile_expressions = auto_match_user_profile_expressions
        # 自动匹配账户是否开启
        self.auto_match_user_status = auto_match_user_status
        # 用户手动绑定账户功能是否开启
        self.mapping_binding_status = mapping_binding_status

    def validate(self):
        if self.auto_match_user_profile_expressions:
            for v1 in self.auto_match_user_profile_expressions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AutoMatchUserProfileExpressions'] = []
        if self.auto_match_user_profile_expressions is not None:
            for k1 in self.auto_match_user_profile_expressions:
                result['AutoMatchUserProfileExpressions'].append(k1.to_map() if k1 else None)

        if self.auto_match_user_status is not None:
            result['AutoMatchUserStatus'] = self.auto_match_user_status

        if self.mapping_binding_status is not None:
            result['MappingBindingStatus'] = self.mapping_binding_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.auto_match_user_profile_expressions = []
        if m.get('AutoMatchUserProfileExpressions') is not None:
            for k1 in m.get('AutoMatchUserProfileExpressions'):
                temp_model = main_models.SetIdentityProviderAuthnConfigurationRequestBindingConfigAutoMatchUserProfileExpressions()
                self.auto_match_user_profile_expressions.append(temp_model.from_map(k1))

        if m.get('AutoMatchUserStatus') is not None:
            self.auto_match_user_status = m.get('AutoMatchUserStatus')

        if m.get('MappingBindingStatus') is not None:
            self.mapping_binding_status = m.get('MappingBindingStatus')

        return self

class SetIdentityProviderAuthnConfigurationRequestBindingConfigAutoMatchUserProfileExpressions(DaraModel):
    def __init__(
        self,
        expression_mapping_type: str = None,
        source_value_expression: str = None,
        target_field: str = None,
        target_field_description: str = None,
    ):
        # 表达式的类型
        # 
        # This parameter is required.
        self.expression_mapping_type = expression_mapping_type
        # 映射属性取值表达式
        # 
        # This parameter is required.
        self.source_value_expression = source_value_expression
        # 映射目标属性名称
        # 
        # This parameter is required.
        self.target_field = target_field
        # 映射目标属性名称
        self.target_field_description = target_field_description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expression_mapping_type is not None:
            result['ExpressionMappingType'] = self.expression_mapping_type

        if self.source_value_expression is not None:
            result['SourceValueExpression'] = self.source_value_expression

        if self.target_field is not None:
            result['TargetField'] = self.target_field

        if self.target_field_description is not None:
            result['TargetFieldDescription'] = self.target_field_description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpressionMappingType') is not None:
            self.expression_mapping_type = m.get('ExpressionMappingType')

        if m.get('SourceValueExpression') is not None:
            self.source_value_expression = m.get('SourceValueExpression')

        if m.get('TargetField') is not None:
            self.target_field = m.get('TargetField')

        if m.get('TargetFieldDescription') is not None:
            self.target_field_description = m.get('TargetFieldDescription')

        return self

class SetIdentityProviderAuthnConfigurationRequestAutoUpdateUserConfig(DaraModel):
    def __init__(
        self,
        auto_update_user_status: str = None,
    ):
        self.auto_update_user_status = auto_update_user_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_update_user_status is not None:
            result['AutoUpdateUserStatus'] = self.auto_update_user_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoUpdateUserStatus') is not None:
            self.auto_update_user_status = m.get('AutoUpdateUserStatus')

        return self

class SetIdentityProviderAuthnConfigurationRequestAutoCreateUserConfig(DaraModel):
    def __init__(
        self,
        auto_create_user_status: str = None,
        target_organizational_unit_ids: List[str] = None,
    ):
        # 自动创建账户是否开启
        self.auto_create_user_status = auto_create_user_status
        self.target_organizational_unit_ids = target_organizational_unit_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_create_user_status is not None:
            result['AutoCreateUserStatus'] = self.auto_create_user_status

        if self.target_organizational_unit_ids is not None:
            result['TargetOrganizationalUnitIds'] = self.target_organizational_unit_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoCreateUserStatus') is not None:
            self.auto_create_user_status = m.get('AutoCreateUserStatus')

        if m.get('TargetOrganizationalUnitIds') is not None:
            self.target_organizational_unit_ids = m.get('TargetOrganizationalUnitIds')

        return self

