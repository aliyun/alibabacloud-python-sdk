# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class CreateApplicationFederatedCredentialRequest(DaraModel):
    def __init__(
        self,
        application_federated_credential_name: str = None,
        application_federated_credential_type: str = None,
        application_id: str = None,
        attribute_mappings: List[main_models.CreateApplicationFederatedCredentialRequestAttributeMappings] = None,
        description: str = None,
        federated_credential_provider_id: str = None,
        instance_id: str = None,
        verification_condition: str = None,
    ):
        # 应用联邦凭证名称
        # 
        # This parameter is required.
        self.application_federated_credential_name = application_federated_credential_name
        # 应用联邦凭证类型
        # 
        # This parameter is required.
        self.application_federated_credential_type = application_federated_credential_type
        # IDaaS的应用资源ID。
        # 
        # This parameter is required.
        self.application_id = application_id
        # 属性映射
        self.attribute_mappings = attribute_mappings
        # 描述
        self.description = description
        # 联邦凭证提供方ID
        # 
        # This parameter is required.
        self.federated_credential_provider_id = federated_credential_provider_id
        # IDaaS EIAM实例的ID。
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # 校验条件
        self.verification_condition = verification_condition

    def validate(self):
        if self.attribute_mappings:
            for v1 in self.attribute_mappings:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_federated_credential_name is not None:
            result['ApplicationFederatedCredentialName'] = self.application_federated_credential_name

        if self.application_federated_credential_type is not None:
            result['ApplicationFederatedCredentialType'] = self.application_federated_credential_type

        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        result['AttributeMappings'] = []
        if self.attribute_mappings is not None:
            for k1 in self.attribute_mappings:
                result['AttributeMappings'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['Description'] = self.description

        if self.federated_credential_provider_id is not None:
            result['FederatedCredentialProviderId'] = self.federated_credential_provider_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.verification_condition is not None:
            result['VerificationCondition'] = self.verification_condition

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationFederatedCredentialName') is not None:
            self.application_federated_credential_name = m.get('ApplicationFederatedCredentialName')

        if m.get('ApplicationFederatedCredentialType') is not None:
            self.application_federated_credential_type = m.get('ApplicationFederatedCredentialType')

        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        self.attribute_mappings = []
        if m.get('AttributeMappings') is not None:
            for k1 in m.get('AttributeMappings'):
                temp_model = main_models.CreateApplicationFederatedCredentialRequestAttributeMappings()
                self.attribute_mappings.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FederatedCredentialProviderId') is not None:
            self.federated_credential_provider_id = m.get('FederatedCredentialProviderId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('VerificationCondition') is not None:
            self.verification_condition = m.get('VerificationCondition')

        return self

class CreateApplicationFederatedCredentialRequestAttributeMappings(DaraModel):
    def __init__(
        self,
        source_value_expression: str = None,
        target_field: str = None,
    ):
        # 源值表达式
        self.source_value_expression = source_value_expression
        # 目标字段
        self.target_field = target_field

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.source_value_expression is not None:
            result['SourceValueExpression'] = self.source_value_expression

        if self.target_field is not None:
            result['TargetField'] = self.target_field

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceValueExpression') is not None:
            self.source_value_expression = m.get('SourceValueExpression')

        if m.get('TargetField') is not None:
            self.target_field = m.get('TargetField')

        return self

