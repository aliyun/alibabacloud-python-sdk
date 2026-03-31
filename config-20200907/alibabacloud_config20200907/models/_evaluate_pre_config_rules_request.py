# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class EvaluatePreConfigRulesRequest(DaraModel):
    def __init__(
        self,
        enable_managed_rules: bool = None,
        resource_evaluate_items: List[main_models.EvaluatePreConfigRulesRequestResourceEvaluateItems] = None,
        resource_type_format: str = None,
    ):
        # Specifies whether to enable the managed rule. Valid values:
        # 
        # *   true: enables the managed rule.
        # *   false: does not enable the managed rule. This is the default value.
        # 
        # >  After you create an evaluation rule, a managed rule that has the same settings as the evaluation rule is created. After you create a resource, the managed rule can be used to continuously check the compliance of the resource.
        self.enable_managed_rules = enable_managed_rules
        # The resources that you want to evaluate.
        # 
        # This parameter is required.
        self.resource_evaluate_items = resource_evaluate_items
        # 下一个查询开始Token
        self.resource_type_format = resource_type_format

    def validate(self):
        if self.resource_evaluate_items:
            for v1 in self.resource_evaluate_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_managed_rules is not None:
            result['EnableManagedRules'] = self.enable_managed_rules

        result['ResourceEvaluateItems'] = []
        if self.resource_evaluate_items is not None:
            for k1 in self.resource_evaluate_items:
                result['ResourceEvaluateItems'].append(k1.to_map() if k1 else None)

        if self.resource_type_format is not None:
            result['ResourceTypeFormat'] = self.resource_type_format

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableManagedRules') is not None:
            self.enable_managed_rules = m.get('EnableManagedRules')

        self.resource_evaluate_items = []
        if m.get('ResourceEvaluateItems') is not None:
            for k1 in m.get('ResourceEvaluateItems'):
                temp_model = main_models.EvaluatePreConfigRulesRequestResourceEvaluateItems()
                self.resource_evaluate_items.append(temp_model.from_map(k1))

        if m.get('ResourceTypeFormat') is not None:
            self.resource_type_format = m.get('ResourceTypeFormat')

        return self

class EvaluatePreConfigRulesRequestResourceEvaluateItems(DaraModel):
    def __init__(
        self,
        resource_logical_id: str = None,
        resource_properties: str = None,
        resource_type: str = None,
        rules: List[main_models.EvaluatePreConfigRulesRequestResourceEvaluateItemsRules] = None,
    ):
        # The logical ID of the resource.
        self.resource_logical_id = resource_logical_id
        # The properties of the resource.
        self.resource_properties = resource_properties
        # The type of the resource.
        self.resource_type = resource_type
        # The evaluation rules.
        self.rules = rules

    def validate(self):
        if self.rules:
            for v1 in self.rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_logical_id is not None:
            result['ResourceLogicalId'] = self.resource_logical_id

        if self.resource_properties is not None:
            result['ResourceProperties'] = self.resource_properties

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceLogicalId') is not None:
            self.resource_logical_id = m.get('ResourceLogicalId')

        if m.get('ResourceProperties') is not None:
            self.resource_properties = m.get('ResourceProperties')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.EvaluatePreConfigRulesRequestResourceEvaluateItemsRules()
                self.rules.append(temp_model.from_map(k1))

        return self

class EvaluatePreConfigRulesRequestResourceEvaluateItemsRules(DaraModel):
    def __init__(
        self,
        identifier: str = None,
        input_parameters: str = None,
    ):
        # The identifier of the evaluation rule.
        # 
        # For more information about how to obtain the identifier of an evaluation rule, see [ListManagedRules](https://help.aliyun.com/document_detail/467810.html).
        self.identifier = identifier
        # The input parameters of the evaluation rule.
        self.input_parameters = input_parameters

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.identifier is not None:
            result['Identifier'] = self.identifier

        if self.input_parameters is not None:
            result['InputParameters'] = self.input_parameters

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')

        if m.get('InputParameters') is not None:
            self.input_parameters = m.get('InputParameters')

        return self

