# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class EvaluatePreConfigRulesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        resource_evaluations: List[main_models.EvaluatePreConfigRulesResponseBodyResourceEvaluations] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The details of the compliance evaluation result.
        self.resource_evaluations = resource_evaluations

    def validate(self):
        if self.resource_evaluations:
            for v1 in self.resource_evaluations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ResourceEvaluations'] = []
        if self.resource_evaluations is not None:
            for k1 in self.resource_evaluations:
                result['ResourceEvaluations'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.resource_evaluations = []
        if m.get('ResourceEvaluations') is not None:
            for k1 in m.get('ResourceEvaluations'):
                temp_model = main_models.EvaluatePreConfigRulesResponseBodyResourceEvaluations()
                self.resource_evaluations.append(temp_model.from_map(k1))

        return self

class EvaluatePreConfigRulesResponseBodyResourceEvaluations(DaraModel):
    def __init__(
        self,
        resource_logical_id: str = None,
        resource_type: str = None,
        rules: List[main_models.EvaluatePreConfigRulesResponseBodyResourceEvaluationsRules] = None,
    ):
        # The logical ID of the resource.
        # 
        # >  If the ResourceLogicalId request parameter is left empty, the value of the ResourceLogicalId response parameter is generated based on the value of the `ResourceProperties` parameter.
        self.resource_logical_id = resource_logical_id
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

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.EvaluatePreConfigRulesResponseBodyResourceEvaluationsRules()
                self.rules.append(temp_model.from_map(k1))

        return self

class EvaluatePreConfigRulesResponseBodyResourceEvaluationsRules(DaraModel):
    def __init__(
        self,
        annotation: str = None,
        compliance_type: str = None,
        help_url: str = None,
        identifier: str = None,
    ):
        # The reason why the resource was evaluated as incompliant.
        self.annotation = annotation
        # The compliance type of the resource that was evaluated by using the evaluation rule. Valid values:
        # 
        # *   COMPLIANT: The resource was evaluated as compliant.
        # *   NON_COMPLIANT: The resource was evaluated as incompliant.
        # *   NOT_APPLICABLE: The evaluation rule does not apply to the resource.
        self.compliance_type = compliance_type
        # The URL of the topic that describes how the managed rule remediates the incompliant configurations.
        self.help_url = help_url
        # The identifier of the evaluation rule.
        self.identifier = identifier

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.annotation is not None:
            result['Annotation'] = self.annotation

        if self.compliance_type is not None:
            result['ComplianceType'] = self.compliance_type

        if self.help_url is not None:
            result['HelpUrl'] = self.help_url

        if self.identifier is not None:
            result['Identifier'] = self.identifier

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Annotation') is not None:
            self.annotation = m.get('Annotation')

        if m.get('ComplianceType') is not None:
            self.compliance_type = m.get('ComplianceType')

        if m.get('HelpUrl') is not None:
            self.help_url = m.get('HelpUrl')

        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')

        return self

