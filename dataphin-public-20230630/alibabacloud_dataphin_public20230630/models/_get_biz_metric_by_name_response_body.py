# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetBizMetricByNameResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetBizMetricByNameResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetBizMetricByNameResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetBizMetricByNameResponseBodyData(DaraModel):
    def __init__(
        self,
        associated_tech_metrics: List[main_models.GetBizMetricByNameResponseBodyDataAssociatedTechMetrics] = None,
        biz_owner_name: str = None,
        catalogs: List[main_models.GetBizMetricByNameResponseBodyDataCatalogs] = None,
        custom_attribute: List[main_models.GetBizMetricByNameResponseBodyDataCustomAttribute] = None,
        description: str = None,
        display_name: str = None,
        guid: str = None,
        labels: List[str] = None,
        metric_definition: str = None,
        metric_relation_diagram_expression: str = None,
        metric_relation_diagram_switch_open: bool = None,
        name: str = None,
        operate_instruction_content: str = None,
        operate_instruction_enabled: bool = None,
        related_biz_metrics: List[main_models.GetBizMetricByNameResponseBodyDataRelatedBizMetrics] = None,
        tenant_id: int = None,
        view_scope: main_models.GetBizMetricByNameResponseBodyDataViewScope = None,
    ):
        self.associated_tech_metrics = associated_tech_metrics
        self.biz_owner_name = biz_owner_name
        self.catalogs = catalogs
        self.custom_attribute = custom_attribute
        self.description = description
        self.display_name = display_name
        self.guid = guid
        self.labels = labels
        self.metric_definition = metric_definition
        self.metric_relation_diagram_expression = metric_relation_diagram_expression
        self.metric_relation_diagram_switch_open = metric_relation_diagram_switch_open
        self.name = name
        self.operate_instruction_content = operate_instruction_content
        self.operate_instruction_enabled = operate_instruction_enabled
        self.related_biz_metrics = related_biz_metrics
        self.tenant_id = tenant_id
        self.view_scope = view_scope

    def validate(self):
        if self.associated_tech_metrics:
            for v1 in self.associated_tech_metrics:
                 if v1:
                    v1.validate()
        if self.catalogs:
            for v1 in self.catalogs:
                 if v1:
                    v1.validate()
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
        result['AssociatedTechMetrics'] = []
        if self.associated_tech_metrics is not None:
            for k1 in self.associated_tech_metrics:
                result['AssociatedTechMetrics'].append(k1.to_map() if k1 else None)

        if self.biz_owner_name is not None:
            result['BizOwnerName'] = self.biz_owner_name

        result['Catalogs'] = []
        if self.catalogs is not None:
            for k1 in self.catalogs:
                result['Catalogs'].append(k1.to_map() if k1 else None)

        result['CustomAttribute'] = []
        if self.custom_attribute is not None:
            for k1 in self.custom_attribute:
                result['CustomAttribute'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.guid is not None:
            result['Guid'] = self.guid

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

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.view_scope is not None:
            result['ViewScope'] = self.view_scope.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.associated_tech_metrics = []
        if m.get('AssociatedTechMetrics') is not None:
            for k1 in m.get('AssociatedTechMetrics'):
                temp_model = main_models.GetBizMetricByNameResponseBodyDataAssociatedTechMetrics()
                self.associated_tech_metrics.append(temp_model.from_map(k1))

        if m.get('BizOwnerName') is not None:
            self.biz_owner_name = m.get('BizOwnerName')

        self.catalogs = []
        if m.get('Catalogs') is not None:
            for k1 in m.get('Catalogs'):
                temp_model = main_models.GetBizMetricByNameResponseBodyDataCatalogs()
                self.catalogs.append(temp_model.from_map(k1))

        self.custom_attribute = []
        if m.get('CustomAttribute') is not None:
            for k1 in m.get('CustomAttribute'):
                temp_model = main_models.GetBizMetricByNameResponseBodyDataCustomAttribute()
                self.custom_attribute.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Guid') is not None:
            self.guid = m.get('Guid')

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
                temp_model = main_models.GetBizMetricByNameResponseBodyDataRelatedBizMetrics()
                self.related_biz_metrics.append(temp_model.from_map(k1))

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('ViewScope') is not None:
            temp_model = main_models.GetBizMetricByNameResponseBodyDataViewScope()
            self.view_scope = temp_model.from_map(m.get('ViewScope'))

        return self

class GetBizMetricByNameResponseBodyDataViewScope(DaraModel):
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

class GetBizMetricByNameResponseBodyDataRelatedBizMetrics(DaraModel):
    def __init__(
        self,
        description: str = None,
        display_name: str = None,
        guid: str = None,
        name: str = None,
        relation_type: str = None,
    ):
        self.description = description
        self.display_name = display_name
        # guid
        self.guid = guid
        self.name = name
        self.relation_type = relation_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.guid is not None:
            result['Guid'] = self.guid

        if self.name is not None:
            result['Name'] = self.name

        if self.relation_type is not None:
            result['RelationType'] = self.relation_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Guid') is not None:
            self.guid = m.get('Guid')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RelationType') is not None:
            self.relation_type = m.get('RelationType')

        return self

class GetBizMetricByNameResponseBodyDataCustomAttribute(DaraModel):
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

class GetBizMetricByNameResponseBodyDataCatalogs(DaraModel):
    def __init__(
        self,
        catalog_desc: str = None,
        catalog_id: int = None,
        catalog_name: str = None,
        parent_catalog_id: int = None,
        parent_path: str = None,
        topic_id: int = None,
        topic_name: str = None,
    ):
        self.catalog_desc = catalog_desc
        self.catalog_id = catalog_id
        self.catalog_name = catalog_name
        self.parent_catalog_id = parent_catalog_id
        self.parent_path = parent_path
        self.topic_id = topic_id
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog_desc is not None:
            result['CatalogDesc'] = self.catalog_desc

        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id

        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name

        if self.parent_catalog_id is not None:
            result['ParentCatalogId'] = self.parent_catalog_id

        if self.parent_path is not None:
            result['ParentPath'] = self.parent_path

        if self.topic_id is not None:
            result['TopicId'] = self.topic_id

        if self.topic_name is not None:
            result['TopicName'] = self.topic_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogDesc') is not None:
            self.catalog_desc = m.get('CatalogDesc')

        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')

        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')

        if m.get('ParentCatalogId') is not None:
            self.parent_catalog_id = m.get('ParentCatalogId')

        if m.get('ParentPath') is not None:
            self.parent_path = m.get('ParentPath')

        if m.get('TopicId') is not None:
            self.topic_id = m.get('TopicId')

        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')

        return self

class GetBizMetricByNameResponseBodyDataAssociatedTechMetrics(DaraModel):
    def __init__(
        self,
        description: str = None,
        display_name: str = None,
        guid: str = None,
        name: str = None,
        sub_type: str = None,
    ):
        self.description = description
        self.display_name = display_name
        # guid
        self.guid = guid
        self.name = name
        self.sub_type = sub_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.guid is not None:
            result['Guid'] = self.guid

        if self.name is not None:
            result['Name'] = self.name

        if self.sub_type is not None:
            result['SubType'] = self.sub_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Guid') is not None:
            self.guid = m.get('Guid')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')

        return self

