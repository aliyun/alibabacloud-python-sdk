# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_arms20210422 import models as main_models
from darabonba.model import DaraModel

class CreateAlertTemplateResponseBody(DaraModel):
    def __init__(
        self,
        alert_template: main_models.CreateAlertTemplateResponseBodyAlertTemplate = None,
        request_id: str = None,
    ):
        self.alert_template = alert_template
        self.request_id = request_id

    def validate(self):
        if self.alert_template:
            self.alert_template.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_template is not None:
            result['AlertTemplate'] = self.alert_template.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertTemplate') is not None:
            temp_model = main_models.CreateAlertTemplateResponseBodyAlertTemplate()
            self.alert_template = temp_model.from_map(m.get('AlertTemplate'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateAlertTemplateResponseBodyAlertTemplate(DaraModel):
    def __init__(
        self,
        alert_provider: str = None,
        annotations: Dict[str, Any] = None,
        id: int = None,
        label_match_expression_grid: main_models.CreateAlertTemplateResponseBodyAlertTemplateLabelMatchExpressionGrid = None,
        labels: Dict[str, Any] = None,
        message: str = None,
        name: str = None,
        parent_id: int = None,
        public: bool = None,
        rule: str = None,
        status: bool = None,
        template_provider: str = None,
        type: str = None,
        user_id: str = None,
    ):
        self.alert_provider = alert_provider
        self.annotations = annotations
        self.id = id
        self.label_match_expression_grid = label_match_expression_grid
        self.labels = labels
        self.message = message
        self.name = name
        self.parent_id = parent_id
        self.public = public
        self.rule = rule
        self.status = status
        self.template_provider = template_provider
        self.type = type
        self.user_id = user_id

    def validate(self):
        if self.label_match_expression_grid:
            self.label_match_expression_grid.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_provider is not None:
            result['AlertProvider'] = self.alert_provider

        if self.annotations is not None:
            result['Annotations'] = self.annotations

        if self.id is not None:
            result['Id'] = self.id

        if self.label_match_expression_grid is not None:
            result['LabelMatchExpressionGrid'] = self.label_match_expression_grid.to_map()

        if self.labels is not None:
            result['Labels'] = self.labels

        if self.message is not None:
            result['Message'] = self.message

        if self.name is not None:
            result['Name'] = self.name

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        if self.public is not None:
            result['Public'] = self.public

        if self.rule is not None:
            result['Rule'] = self.rule

        if self.status is not None:
            result['Status'] = self.status

        if self.template_provider is not None:
            result['TemplateProvider'] = self.template_provider

        if self.type is not None:
            result['Type'] = self.type

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertProvider') is not None:
            self.alert_provider = m.get('AlertProvider')

        if m.get('Annotations') is not None:
            self.annotations = m.get('Annotations')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LabelMatchExpressionGrid') is not None:
            temp_model = main_models.CreateAlertTemplateResponseBodyAlertTemplateLabelMatchExpressionGrid()
            self.label_match_expression_grid = temp_model.from_map(m.get('LabelMatchExpressionGrid'))

        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        if m.get('Public') is not None:
            self.public = m.get('Public')

        if m.get('Rule') is not None:
            self.rule = m.get('Rule')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TemplateProvider') is not None:
            self.template_provider = m.get('TemplateProvider')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class CreateAlertTemplateResponseBodyAlertTemplateLabelMatchExpressionGrid(DaraModel):
    def __init__(
        self,
        label_match_expression_groups: List[main_models.CreateAlertTemplateResponseBodyAlertTemplateLabelMatchExpressionGridLabelMatchExpressionGroups] = None,
    ):
        self.label_match_expression_groups = label_match_expression_groups

    def validate(self):
        if self.label_match_expression_groups:
            for v1 in self.label_match_expression_groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LabelMatchExpressionGroups'] = []
        if self.label_match_expression_groups is not None:
            for k1 in self.label_match_expression_groups:
                result['LabelMatchExpressionGroups'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.label_match_expression_groups = []
        if m.get('LabelMatchExpressionGroups') is not None:
            for k1 in m.get('LabelMatchExpressionGroups'):
                temp_model = main_models.CreateAlertTemplateResponseBodyAlertTemplateLabelMatchExpressionGridLabelMatchExpressionGroups()
                self.label_match_expression_groups.append(temp_model.from_map(k1))

        return self

class CreateAlertTemplateResponseBodyAlertTemplateLabelMatchExpressionGridLabelMatchExpressionGroups(DaraModel):
    def __init__(
        self,
        label_match_expressions: List[main_models.CreateAlertTemplateResponseBodyAlertTemplateLabelMatchExpressionGridLabelMatchExpressionGroupsLabelMatchExpressions] = None,
    ):
        self.label_match_expressions = label_match_expressions

    def validate(self):
        if self.label_match_expressions:
            for v1 in self.label_match_expressions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LabelMatchExpressions'] = []
        if self.label_match_expressions is not None:
            for k1 in self.label_match_expressions:
                result['LabelMatchExpressions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.label_match_expressions = []
        if m.get('LabelMatchExpressions') is not None:
            for k1 in m.get('LabelMatchExpressions'):
                temp_model = main_models.CreateAlertTemplateResponseBodyAlertTemplateLabelMatchExpressionGridLabelMatchExpressionGroupsLabelMatchExpressions()
                self.label_match_expressions.append(temp_model.from_map(k1))

        return self

class CreateAlertTemplateResponseBodyAlertTemplateLabelMatchExpressionGridLabelMatchExpressionGroupsLabelMatchExpressions(DaraModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        value: str = None,
    ):
        self.key = key
        self.operator = operator
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

