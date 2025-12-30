# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class CreateBizMetricRequest(DaraModel):
    def __init__(
        self,
        create_biz_metric_command: main_models.CreateBizMetricRequestCreateBizMetricCommand = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.create_biz_metric_command = create_biz_metric_command
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.create_biz_metric_command:
            self.create_biz_metric_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_biz_metric_command is not None:
            result['CreateBizMetricCommand'] = self.create_biz_metric_command.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateBizMetricCommand') is not None:
            temp_model = main_models.CreateBizMetricRequestCreateBizMetricCommand()
            self.create_biz_metric_command = temp_model.from_map(m.get('CreateBizMetricCommand'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class CreateBizMetricRequestCreateBizMetricCommand(DaraModel):
    def __init__(
        self,
        associated_tech_metric_full_names: List[str] = None,
        biz_owner_name: str = None,
        catalog_ids: List[int] = None,
        custom_attribute: List[main_models.CreateBizMetricRequestCreateBizMetricCommandCustomAttribute] = None,
        description: str = None,
        display_name: str = None,
        labels: List[str] = None,
        metric_definition: str = None,
        metric_relation_diagram_expression: str = None,
        metric_relation_diagram_switch_open: bool = None,
        name: str = None,
        operate_instruction_content: str = None,
        operate_instruction_enabled: bool = None,
        related_biz_metrics: List[main_models.CreateBizMetricRequestCreateBizMetricCommandRelatedBizMetrics] = None,
        view_scope: main_models.CreateBizMetricRequestCreateBizMetricCommandViewScope = None,
    ):
        self.associated_tech_metric_full_names = associated_tech_metric_full_names
        self.biz_owner_name = biz_owner_name
        self.catalog_ids = catalog_ids
        self.custom_attribute = custom_attribute
        self.description = description
        self.display_name = display_name
        self.labels = labels
        self.metric_definition = metric_definition
        self.metric_relation_diagram_expression = metric_relation_diagram_expression
        self.metric_relation_diagram_switch_open = metric_relation_diagram_switch_open
        # This parameter is required.
        self.name = name
        self.operate_instruction_content = operate_instruction_content
        self.operate_instruction_enabled = operate_instruction_enabled
        self.related_biz_metrics = related_biz_metrics
        self.view_scope = view_scope

    def validate(self):
        if self.custom_attribute:
            for v1 in self.custom_attribute:
                 if v1:
                    v1.validate()
        if self.related_biz_metrics:
            for v1 in self.related_biz_metrics:
                 if v1:
                    v1.validate()
        if self.view_scope:
            self.view_scope.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.associated_tech_metric_full_names is not None:
            result['AssociatedTechMetricFullNames'] = self.associated_tech_metric_full_names

        if self.biz_owner_name is not None:
            result['BizOwnerName'] = self.biz_owner_name

        if self.catalog_ids is not None:
            result['CatalogIds'] = self.catalog_ids

        result['CustomAttribute'] = []
        if self.custom_attribute is not None:
            for k1 in self.custom_attribute:
                result['CustomAttribute'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.labels is not None:
            result['Labels'] = self.labels

        if self.metric_definition is not None:
            result['MetricDefinition'] = self.metric_definition

        if self.metric_relation_diagram_expression is not None:
            result['MetricRelationDiagramExpression'] = self.metric_relation_diagram_expression

        if self.metric_relation_diagram_switch_open is not None:
            result['MetricRelationDiagramSwitchOpen'] = self.metric_relation_diagram_switch_open

        if self.name is not None:
            result['Name'] = self.name

        if self.operate_instruction_content is not None:
            result['OperateInstructionContent'] = self.operate_instruction_content

        if self.operate_instruction_enabled is not None:
            result['OperateInstructionEnabled'] = self.operate_instruction_enabled

        result['RelatedBizMetrics'] = []
        if self.related_biz_metrics is not None:
            for k1 in self.related_biz_metrics:
                result['RelatedBizMetrics'].append(k1.to_map() if k1 else None)

        if self.view_scope is not None:
            result['ViewScope'] = self.view_scope.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssociatedTechMetricFullNames') is not None:
            self.associated_tech_metric_full_names = m.get('AssociatedTechMetricFullNames')

        if m.get('BizOwnerName') is not None:
            self.biz_owner_name = m.get('BizOwnerName')

        if m.get('CatalogIds') is not None:
            self.catalog_ids = m.get('CatalogIds')

        self.custom_attribute = []
        if m.get('CustomAttribute') is not None:
            for k1 in m.get('CustomAttribute'):
                temp_model = main_models.CreateBizMetricRequestCreateBizMetricCommandCustomAttribute()
                self.custom_attribute.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        if m.get('MetricDefinition') is not None:
            self.metric_definition = m.get('MetricDefinition')

        if m.get('MetricRelationDiagramExpression') is not None:
            self.metric_relation_diagram_expression = m.get('MetricRelationDiagramExpression')

        if m.get('MetricRelationDiagramSwitchOpen') is not None:
            self.metric_relation_diagram_switch_open = m.get('MetricRelationDiagramSwitchOpen')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OperateInstructionContent') is not None:
            self.operate_instruction_content = m.get('OperateInstructionContent')

        if m.get('OperateInstructionEnabled') is not None:
            self.operate_instruction_enabled = m.get('OperateInstructionEnabled')

        self.related_biz_metrics = []
        if m.get('RelatedBizMetrics') is not None:
            for k1 in m.get('RelatedBizMetrics'):
                temp_model = main_models.CreateBizMetricRequestCreateBizMetricCommandRelatedBizMetrics()
                self.related_biz_metrics.append(temp_model.from_map(k1))

        if m.get('ViewScope') is not None:
            temp_model = main_models.CreateBizMetricRequestCreateBizMetricCommandViewScope()
            self.view_scope = temp_model.from_map(m.get('ViewScope'))

        return self

class CreateBizMetricRequestCreateBizMetricCommandViewScope(DaraModel):
    def __init__(
        self,
        scope_type: str = None,
        user_group_names: List[str] = None,
        user_names: List[str] = None,
    ):
        self.scope_type = scope_type
        self.user_group_names = user_group_names
        self.user_names = user_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.scope_type is not None:
            result['ScopeType'] = self.scope_type

        if self.user_group_names is not None:
            result['UserGroupNames'] = self.user_group_names

        if self.user_names is not None:
            result['UserNames'] = self.user_names

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ScopeType') is not None:
            self.scope_type = m.get('ScopeType')

        if m.get('UserGroupNames') is not None:
            self.user_group_names = m.get('UserGroupNames')

        if m.get('UserNames') is not None:
            self.user_names = m.get('UserNames')

        return self

class CreateBizMetricRequestCreateBizMetricCommandRelatedBizMetrics(DaraModel):
    def __init__(
        self,
        name: str = None,
        relation_type: str = None,
    ):
        self.name = name
        self.relation_type = relation_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.relation_type is not None:
            result['RelationType'] = self.relation_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RelationType') is not None:
            self.relation_type = m.get('RelationType')

        return self

class CreateBizMetricRequestCreateBizMetricCommandCustomAttribute(DaraModel):
    def __init__(
        self,
        code: str = None,
        values: List[str] = None,
    ):
        self.code = code
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

