# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class PublishKgSchemaRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        publish_command: main_models.PublishKgSchemaRequestPublishCommand = None,
        workspace_id: str = None,
    ):
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # The publish command and its details.
        # 
        # This parameter is required.
        self.publish_command = publish_command
        # The model ID.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        if self.publish_command:
            self.publish_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.publish_command is not None:
            result['PublishCommand'] = self.publish_command.to_map()

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('PublishCommand') is not None:
            temp_model = main_models.PublishKgSchemaRequestPublishCommand()
            self.publish_command = temp_model.from_map(m.get('PublishCommand'))

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class PublishKgSchemaRequestPublishCommand(DaraModel):
    def __init__(
        self,
        data_adjustment_policies: List[main_models.PublishKgSchemaRequestPublishCommandDataAdjustmentPolicies] = None,
        description: str = None,
    ):
        # The data adjustment policies.
        self.data_adjustment_policies = data_adjustment_policies
        # The description.
        # 
        # This parameter is required.
        self.description = description

    def validate(self):
        if self.data_adjustment_policies:
            for v1 in self.data_adjustment_policies:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataAdjustmentPolicies'] = []
        if self.data_adjustment_policies is not None:
            for k1 in self.data_adjustment_policies:
                result['DataAdjustmentPolicies'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['Description'] = self.description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_adjustment_policies = []
        if m.get('DataAdjustmentPolicies') is not None:
            for k1 in m.get('DataAdjustmentPolicies'):
                temp_model = main_models.PublishKgSchemaRequestPublishCommandDataAdjustmentPolicies()
                self.data_adjustment_policies.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        return self

class PublishKgSchemaRequestPublishCommandDataAdjustmentPolicies(DaraModel):
    def __init__(
        self,
        back_fill_default_value_policy: main_models.PublishKgSchemaRequestPublishCommandDataAdjustmentPoliciesBackFillDefaultValuePolicy = None,
        policy_type: str = None,
        type: str = None,
        type_code: str = None,
    ):
        # The backfill property default value policy. This parameter takes effect only when PolicyType is set to BackFillDefault.
        # 
        # This parameter is required.
        self.back_fill_default_value_policy = back_fill_default_value_policy
        # The policy type. Valid values:
        # 
        # - BackFillDefault: backfills default values when a property changes from optional to required.
        # 
        # This parameter is required.
        self.policy_type = policy_type
        # The type to which the policy applies. Valid values:
        # 
        # - ENTITY: applies to entity types.
        # - RELATION: applies to relation types.
        # 
        # This parameter is required.
        self.type = type
        # The code of the entity type or relation type.
        # 
        # This parameter is required.
        self.type_code = type_code

    def validate(self):
        if self.back_fill_default_value_policy:
            self.back_fill_default_value_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.back_fill_default_value_policy is not None:
            result['BackFillDefaultValuePolicy'] = self.back_fill_default_value_policy.to_map()

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        if self.type is not None:
            result['Type'] = self.type

        if self.type_code is not None:
            result['TypeCode'] = self.type_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackFillDefaultValuePolicy') is not None:
            temp_model = main_models.PublishKgSchemaRequestPublishCommandDataAdjustmentPoliciesBackFillDefaultValuePolicy()
            self.back_fill_default_value_policy = temp_model.from_map(m.get('BackFillDefaultValuePolicy'))

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('TypeCode') is not None:
            self.type_code = m.get('TypeCode')

        return self

class PublishKgSchemaRequestPublishCommandDataAdjustmentPoliciesBackFillDefaultValuePolicy(DaraModel):
    def __init__(
        self,
        default_value: str = None,
        property_code: str = None,
    ):
        # The default value to backfill for the property.
        # 
        # This parameter is required.
        self.default_value = default_value
        # The property code.
        # 
        # This parameter is required.
        self.property_code = property_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value

        if self.property_code is not None:
            result['PropertyCode'] = self.property_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')

        if m.get('PropertyCode') is not None:
            self.property_code = m.get('PropertyCode')

        return self

