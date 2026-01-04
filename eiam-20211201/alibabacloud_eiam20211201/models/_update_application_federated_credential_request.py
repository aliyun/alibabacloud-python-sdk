# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class UpdateApplicationFederatedCredentialRequest(DaraModel):
    def __init__(
        self,
        application_federated_credential_id: str = None,
        application_id: str = None,
        attribute_mappings: List[main_models.UpdateApplicationFederatedCredentialRequestAttributeMappings] = None,
        instance_id: str = None,
        verification_condition: str = None,
    ):
        # 应用联邦凭证Id
        # 
        # This parameter is required.
        self.application_federated_credential_id = application_federated_credential_id
        # IDaaS的应用资源ID。
        # 
        # This parameter is required.
        self.application_id = application_id
        # 属性映射
        self.attribute_mappings = attribute_mappings
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
        if self.application_federated_credential_id is not None:
            result['ApplicationFederatedCredentialId'] = self.application_federated_credential_id

        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        result['AttributeMappings'] = []
        if self.attribute_mappings is not None:
            for k1 in self.attribute_mappings:
                result['AttributeMappings'].append(k1.to_map() if k1 else None)

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.verification_condition is not None:
            result['VerificationCondition'] = self.verification_condition

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationFederatedCredentialId') is not None:
            self.application_federated_credential_id = m.get('ApplicationFederatedCredentialId')

        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        self.attribute_mappings = []
        if m.get('AttributeMappings') is not None:
            for k1 in m.get('AttributeMappings'):
                temp_model = main_models.UpdateApplicationFederatedCredentialRequestAttributeMappings()
                self.attribute_mappings.append(temp_model.from_map(k1))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('VerificationCondition') is not None:
            self.verification_condition = m.get('VerificationCondition')

        return self

class UpdateApplicationFederatedCredentialRequestAttributeMappings(DaraModel):
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

