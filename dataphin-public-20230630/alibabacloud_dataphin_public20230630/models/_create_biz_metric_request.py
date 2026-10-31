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
        op_user_id: str = None,
    ):
        # The creation request.
        # 
        # This parameter is required.
        self.create_biz_metric_command = create_biz_metric_command
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # The ID of the operator.
        self.op_user_id = op_user_id

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

        if self.op_user_id is not None:
            result['OpUserId'] = self.op_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateBizMetricCommand') is not None:
            temp_model = main_models.CreateBizMetricRequestCreateBizMetricCommand()
            self.create_biz_metric_command = temp_model.from_map(m.get('CreateBizMetricCommand'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('OpUserId') is not None:
            self.op_user_id = m.get('OpUserId')

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
        # The list of full names of associated technical metrics. Enter the technical metric in the format of "Full table name.Metric name", where "Full table name" is equal to "Asset source.Table name". A technical metric can be associated with only one business metric and cannot be associated repeatedly.
        self.associated_tech_metric_full_names = associated_tech_metric_full_names
        # The name of the business owner. Enter the username of the owner\\"s account.
        self.biz_owner_name = biz_owner_name
        # The IDs of the parent folders.
        self.catalog_ids = catalog_ids
        # The custom attributes.
        self.custom_attribute = custom_attribute
        # The description.
        self.description = description
        # The display name.
        self.display_name = display_name
        # The asset labels.
        self.labels = labels
        # The metric definition. To reference other business metrics, enclose the metric names in half-width square brackets [ ].
        self.metric_definition = metric_definition
        # The expression for the metric relationship diagram. This information is read only when the metric relationship diagram is enabled. You can only enter a calculation expression composed of metric names selected from the related business metrics. The supported operators are +, -, *, /, (), %, and ∑. Each metric name must be enclosed in half-width square brackets [ ]. If no operator is specified between two metrics, the system automatically adds padding as a placeholder. If the metric relational expression is not configured, the metric relationship diagram switch is automatically set to shutdown.
        self.metric_relation_diagram_expression = metric_relation_diagram_expression
        # Specifies whether to enable the metric relationship diagram. Valid values:
        # - true: Enabled.
        # - false: Disabled.
        # This switch can be enabled only when at least one related business metric exists. Otherwise, it is automatically disabled.
        self.metric_relation_diagram_switch_open = metric_relation_diagram_switch_open
        # The name of the business metric. The name must be unique within the tenant. Only English letters, digits, and specific special characters (-_/\\·#$^&*()%+=) are supported. Maximum length: 256 characters.
        # 
        # This parameter is required.
        self.name = name
        # The content of the operation instructions. Only text format is supported.
        self.operate_instruction_content = operate_instruction_content
        # Specifies whether to enable operation instructions. Valid values:
        # - true: Enabled.
        # - false: Disabled.
        self.operate_instruction_enabled = operate_instruction_enabled
        # The list of related business metrics. Enter the names of the related business metrics and their relationships.
        self.related_biz_metrics = related_biz_metrics
        # The visibility scope.
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
        # The visibility scope type. Valid values:
        # - ALL_USERS_CAN_VIEW: Visible to all users.
        # - PART_USERS_CAN_VIEW: Visible to specific users.
        # - PART_USERS_CAN_NOT_VIEW: Invisible to specific users.
        self.scope_type = scope_type
        # The names of the user groups. This information is read only when the visibility scope of the asset is set to Visible to specific users or Invisible to specific users.
        self.user_group_names = user_group_names
        # The usernames of individual accounts. This parameter is valid only when the visibility scope of the asset is set to Visible to specific users or Invisible to specific users.
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
        # The metric name.
        self.name = name
        # The relationship type. Valid values:
        # - POSITIVE: Positive correlation.
        # - NEGATIVE: Negative correlation.
        # - OTHER: Other.
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
        # The code of the custom attribute.
        self.code = code
        # The list of attribute values. Rules: 1. For custom input and drop-down single-select attributes, only the first attribute value in the list is read. 2. For drop-down multi-select attributes, all attribute values in the list are read. 3. For hyperlink attributes, the first attribute value in the list is read as the display text, and the second attribute value is read as the redirect URL.
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

