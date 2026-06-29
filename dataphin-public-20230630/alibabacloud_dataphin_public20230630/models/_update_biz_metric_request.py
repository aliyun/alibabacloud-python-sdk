# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class UpdateBizMetricRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        update_biz_metric_command: main_models.UpdateBizMetricRequestUpdateBizMetricCommand = None,
    ):
        # Tenant ID
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # Update request
        # 
        # This parameter is required.
        self.update_biz_metric_command = update_biz_metric_command

    def validate(self):
        if self.update_biz_metric_command:
            self.update_biz_metric_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.update_biz_metric_command is not None:
            result['UpdateBizMetricCommand'] = self.update_biz_metric_command.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('UpdateBizMetricCommand') is not None:
            temp_model = main_models.UpdateBizMetricRequestUpdateBizMetricCommand()
            self.update_biz_metric_command = temp_model.from_map(m.get('UpdateBizMetricCommand'))

        return self

class UpdateBizMetricRequestUpdateBizMetricCommand(DaraModel):
    def __init__(
        self,
        associated_tech_metric_full_names: List[str] = None,
        biz_owner_name: str = None,
        catalog_ids: List[int] = None,
        custom_attribute: List[main_models.UpdateBizMetricRequestUpdateBizMetricCommandCustomAttribute] = None,
        description: str = None,
        display_name: str = None,
        labels: List[str] = None,
        metric_definition: str = None,
        metric_relation_diagram_expression: str = None,
        metric_relation_diagram_switch_open: bool = None,
        name: str = None,
        new_name: str = None,
        operate_instruction_content: str = None,
        operate_instruction_enabled: bool = None,
        related_biz_metrics: List[main_models.UpdateBizMetricRequestUpdateBizMetricCommandRelatedBizMetrics] = None,
        view_scope: main_models.UpdateBizMetricRequestUpdateBizMetricCommandViewScope = None,
    ):
        # List of associated technical metrics. Enter the full name of the technical metric in the format of "TableFullName.MetricName", where "TableFullName" equals "AssetSource.TableName". A technical metric can only be associated with one business metric and cannot be associated repeatedly
        self.associated_tech_metric_full_names = associated_tech_metric_full_names
        # Business owner. Enter the username of the owner account
        self.biz_owner_name = biz_owner_name
        # List of catalog IDs
        self.catalog_ids = catalog_ids
        # List of custom attributes. Enter the attribute code and attribute values for each
        self.custom_attribute = custom_attribute
        # Description
        self.description = description
        # Display name
        self.display_name = display_name
        # Asset labels
        self.labels = labels
        # Metric definition. To reference other business metrics, enclose the metric name in square brackets [ ]
        self.metric_definition = metric_definition
        # This parameter is read only when the metric relationship diagram is enabled. Only a calculation expression composed of metric names selected from related business metrics is supported. Supported operators include +, -, *, /, (), %, and ∑. Each metric name must be enclosed in square brackets [ ]. If no operator is specified between two metrics, the system automatically fills in a placeholder. If no metric relationship expression is configured, the metric relationship diagram switch is automatically disabled
        self.metric_relation_diagram_expression = metric_relation_diagram_expression
        # Metric relationship diagram switch. Valid values: true (enabled) and false (disabled). This can be enabled only when at least one related business metric exists. Otherwise, it is automatically disabled
        self.metric_relation_diagram_switch_open = metric_relation_diagram_switch_open
        # Enter the name of the business metric to update
        # 
        # This parameter is required.
        self.name = name
        # The new name. Enter this when you need to modify the metric name
        self.new_name = new_name
        # Content of the usage instructions. Only text format is supported
        self.operate_instruction_content = operate_instruction_content
        # Specifies whether the usage instructions are enabled. Valid values: true (enabled) and false (disabled)
        self.operate_instruction_enabled = operate_instruction_enabled
        # List of related business metrics
        self.related_biz_metrics = related_biz_metrics
        # Visibility scope
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

        if self.new_name is not None:
            result['NewName'] = self.new_name

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
                temp_model = main_models.UpdateBizMetricRequestUpdateBizMetricCommandCustomAttribute()
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

        if m.get('NewName') is not None:
            self.new_name = m.get('NewName')

        if m.get('OperateInstructionContent') is not None:
            self.operate_instruction_content = m.get('OperateInstructionContent')

        if m.get('OperateInstructionEnabled') is not None:
            self.operate_instruction_enabled = m.get('OperateInstructionEnabled')

        self.related_biz_metrics = []
        if m.get('RelatedBizMetrics') is not None:
            for k1 in m.get('RelatedBizMetrics'):
                temp_model = main_models.UpdateBizMetricRequestUpdateBizMetricCommandRelatedBizMetrics()
                self.related_biz_metrics.append(temp_model.from_map(k1))

        if m.get('ViewScope') is not None:
            temp_model = main_models.UpdateBizMetricRequestUpdateBizMetricCommandViewScope()
            self.view_scope = temp_model.from_map(m.get('ViewScope'))

        return self

class UpdateBizMetricRequestUpdateBizMetricCommandViewScope(DaraModel):
    def __init__(
        self,
        scope_type: str = None,
        user_group_names: List[str] = None,
        user_names: List[str] = None,
    ):
        # Visibility scope type. Valid values: ALL_USERS_CAN_VIEW (visible to all users), PART_USERS_CAN_VIEW (visible to specified users), and PART_USERS_CAN_NOT_VIEW (invisible to specified users)
        self.scope_type = scope_type
        # Enter user group names. This parameter is read only when the visibility scope is set to PART_USERS_CAN_VIEW or PART_USERS_CAN_NOT_VIEW
        self.user_group_names = user_group_names
        # Enter the usernames of individual accounts. This parameter takes effect only when the visibility scope is set to PART_USERS_CAN_VIEW or PART_USERS_CAN_NOT_VIEW
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

class UpdateBizMetricRequestUpdateBizMetricCommandRelatedBizMetrics(DaraModel):
    def __init__(
        self,
        name: str = None,
        relation_type: str = None,
    ):
        # Business metric name
        self.name = name
        # Correlation type. Valid values: POSITIVE (positive correlation), NEGATIVE (negative correlation), and OTHER (other)
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

class UpdateBizMetricRequestUpdateBizMetricCommandCustomAttribute(DaraModel):
    def __init__(
        self,
        code: str = None,
        values: List[str] = None,
    ):
        # Custom attribute code
        self.code = code
        # List of attribute values. 1. For custom input and single-select dropdown attributes, only the first value in the list is read. 2. For multi-select dropdown attributes, all values in the list are read. 3. For hyperlink attributes, the first value is used as the display text and the second value is used as the link URL.
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

