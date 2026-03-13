# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_governance20210120 import models as main_models
from darabonba.model import DaraModel

class ListEvaluationMetadataResponseBody(DaraModel):
    def __init__(
        self,
        evaluation_metadata: List[main_models.ListEvaluationMetadataResponseBodyEvaluationMetadata] = None,
        request_id: str = None,
    ):
        # The metadata of a governance maturity check.
        self.evaluation_metadata = evaluation_metadata
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.evaluation_metadata:
            for v1 in self.evaluation_metadata:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EvaluationMetadata'] = []
        if self.evaluation_metadata is not None:
            for k1 in self.evaluation_metadata:
                result['EvaluationMetadata'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.evaluation_metadata = []
        if m.get('EvaluationMetadata') is not None:
            for k1 in m.get('EvaluationMetadata'):
                temp_model = main_models.ListEvaluationMetadataResponseBodyEvaluationMetadata()
                self.evaluation_metadata.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListEvaluationMetadataResponseBodyEvaluationMetadata(DaraModel):
    def __init__(
        self,
        metadata: List[main_models.ListEvaluationMetadataResponseBodyEvaluationMetadataMetadata] = None,
        type: str = None,
    ):
        # The metadata objects of a specific metadata type.
        self.metadata = metadata
        # The type of the metadata. Valid values:
        # 
        # *   Metric: the check item
        self.type = type

    def validate(self):
        if self.metadata:
            for v1 in self.metadata:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Metadata'] = []
        if self.metadata is not None:
            for k1 in self.metadata:
                result['Metadata'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.metadata = []
        if m.get('Metadata') is not None:
            for k1 in m.get('Metadata'):
                temp_model = main_models.ListEvaluationMetadataResponseBodyEvaluationMetadataMetadata()
                self.metadata.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListEvaluationMetadataResponseBodyEvaluationMetadataMetadata(DaraModel):
    def __init__(
        self,
        category: str = None,
        description: str = None,
        display_name: str = None,
        id: str = None,
        recommendation_level: str = None,
        remediation_metadata: main_models.ListEvaluationMetadataResponseBodyEvaluationMetadataMetadataRemediationMetadata = None,
        resource_metadata: main_models.ListEvaluationMetadataResponseBodyEvaluationMetadataMetadataResourceMetadata = None,
        scope: str = None,
        stage: str = None,
        topic_code: str = None,
    ):
        # The category of the check item.
        self.category = category
        # The description of the check item.
        self.description = description
        # The display name of the check item.
        self.display_name = display_name
        # The ID of the metadata.
        self.id = id
        # The governance level of the check item.
        self.recommendation_level = recommendation_level
        # The metadata of the fixing task.
        self.remediation_metadata = remediation_metadata
        # The metadata of the checked resources.
        self.resource_metadata = resource_metadata
        # The scope of the check item. Valid values:
        # 
        # *   Account: the check item in a single-account governance maturity check
        # *   ResourceDirectory: the check item in a multi-account governance maturity check
        self.scope = scope
        # The status of the check item. Valid values:
        # 
        # *   Released: The check item is released.
        # *   Beta: The check item is pre-released.
        self.stage = stage
        self.topic_code = topic_code

    def validate(self):
        if self.remediation_metadata:
            self.remediation_metadata.validate()
        if self.resource_metadata:
            self.resource_metadata.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.id is not None:
            result['Id'] = self.id

        if self.recommendation_level is not None:
            result['RecommendationLevel'] = self.recommendation_level

        if self.remediation_metadata is not None:
            result['RemediationMetadata'] = self.remediation_metadata.to_map()

        if self.resource_metadata is not None:
            result['ResourceMetadata'] = self.resource_metadata.to_map()

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.stage is not None:
            result['Stage'] = self.stage

        if self.topic_code is not None:
            result['TopicCode'] = self.topic_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('RecommendationLevel') is not None:
            self.recommendation_level = m.get('RecommendationLevel')

        if m.get('RemediationMetadata') is not None:
            temp_model = main_models.ListEvaluationMetadataResponseBodyEvaluationMetadataMetadataRemediationMetadata()
            self.remediation_metadata = temp_model.from_map(m.get('RemediationMetadata'))

        if m.get('ResourceMetadata') is not None:
            temp_model = main_models.ListEvaluationMetadataResponseBodyEvaluationMetadataMetadataResourceMetadata()
            self.resource_metadata = temp_model.from_map(m.get('ResourceMetadata'))

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('Stage') is not None:
            self.stage = m.get('Stage')

        if m.get('TopicCode') is not None:
            self.topic_code = m.get('TopicCode')

        return self

class ListEvaluationMetadataResponseBodyEvaluationMetadataMetadataResourceMetadata(DaraModel):
    def __init__(
        self,
        resource_property_metadata: List[main_models.ListEvaluationMetadataResponseBodyEvaluationMetadataMetadataResourceMetadataResourcePropertyMetadata] = None,
    ):
        # The metadata of the resource properties.
        self.resource_property_metadata = resource_property_metadata

    def validate(self):
        if self.resource_property_metadata:
            for v1 in self.resource_property_metadata:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ResourcePropertyMetadata'] = []
        if self.resource_property_metadata is not None:
            for k1 in self.resource_property_metadata:
                result['ResourcePropertyMetadata'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource_property_metadata = []
        if m.get('ResourcePropertyMetadata') is not None:
            for k1 in m.get('ResourcePropertyMetadata'):
                temp_model = main_models.ListEvaluationMetadataResponseBodyEvaluationMetadataMetadataResourceMetadataResourcePropertyMetadata()
                self.resource_property_metadata.append(temp_model.from_map(k1))

        return self

class ListEvaluationMetadataResponseBodyEvaluationMetadataMetadataResourceMetadataResourcePropertyMetadata(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        property_name: str = None,
        property_type: str = None,
    ):
        # The display name of the resource property.
        self.display_name = display_name
        # The name of the resource property.
        self.property_name = property_name
        # The type of the resource property.
        self.property_type = property_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.property_name is not None:
            result['PropertyName'] = self.property_name

        if self.property_type is not None:
            result['PropertyType'] = self.property_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('PropertyName') is not None:
            self.property_name = m.get('PropertyName')

        if m.get('PropertyType') is not None:
            self.property_type = m.get('PropertyType')

        return self

class ListEvaluationMetadataResponseBodyEvaluationMetadataMetadataRemediationMetadata(DaraModel):
    def __init__(
        self,
        remediation: List[main_models.ListEvaluationMetadataResponseBodyEvaluationMetadataMetadataRemediationMetadataRemediation] = None,
    ):
        # The fixing items.
        self.remediation = remediation

    def validate(self):
        if self.remediation:
            for v1 in self.remediation:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Remediation'] = []
        if self.remediation is not None:
            for k1 in self.remediation:
                result['Remediation'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.remediation = []
        if m.get('Remediation') is not None:
            for k1 in m.get('Remediation'):
                temp_model = main_models.ListEvaluationMetadataResponseBodyEvaluationMetadataMetadataRemediationMetadataRemediation()
                self.remediation.append(temp_model.from_map(k1))

        return self

class ListEvaluationMetadataResponseBodyEvaluationMetadataMetadataRemediationMetadataRemediation(DaraModel):
    def __init__(
        self,
        actions: List[main_models.ListEvaluationMetadataResponseBodyEvaluationMetadataMetadataRemediationMetadataRemediationActions] = None,
        remediation_type: str = None,
    ):
        # The fixing operations.
        self.actions = actions
        # The type of the fixing method. Valid values:
        # 
        # *   Manual: manual fixing
        # *   QuickFix: quick fixing
        # *   Analysis: auxiliary decision-making
        self.remediation_type = remediation_type

    def validate(self):
        if self.actions:
            for v1 in self.actions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Actions'] = []
        if self.actions is not None:
            for k1 in self.actions:
                result['Actions'].append(k1.to_map() if k1 else None)

        if self.remediation_type is not None:
            result['RemediationType'] = self.remediation_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.actions = []
        if m.get('Actions') is not None:
            for k1 in m.get('Actions'):
                temp_model = main_models.ListEvaluationMetadataResponseBodyEvaluationMetadataMetadataRemediationMetadataRemediationActions()
                self.actions.append(temp_model.from_map(k1))

        if m.get('RemediationType') is not None:
            self.remediation_type = m.get('RemediationType')

        return self

class ListEvaluationMetadataResponseBodyEvaluationMetadataMetadataRemediationMetadataRemediationActions(DaraModel):
    def __init__(
        self,
        classification: str = None,
        cost_description: str = None,
        description: str = None,
        guidance: List[main_models.ListEvaluationMetadataResponseBodyEvaluationMetadataMetadataRemediationMetadataRemediationActionsGuidance] = None,
        notice: str = None,
        suggestion: str = None,
    ):
        # The fixing method.
        # 
        # >  This parameter is returned only if the value of `RemediationType` is `Analysis`.
        self.classification = classification
        # The fixing cost.
        self.cost_description = cost_description
        # The description of the fixing item.
        # 
        # >  This parameter is returned only if the value of `RemediationType` is `Analysis`.
        self.description = description
        # The content of the fixing items.
        self.guidance = guidance
        # The usage notes of the fixing item.
        self.notice = notice
        # The fixing suggestion.
        # 
        # >  This parameter is returned only if the value of `RemediationType` is `Analysis`.
        self.suggestion = suggestion

    def validate(self):
        if self.guidance:
            for v1 in self.guidance:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.classification is not None:
            result['Classification'] = self.classification

        if self.cost_description is not None:
            result['CostDescription'] = self.cost_description

        if self.description is not None:
            result['Description'] = self.description

        result['Guidance'] = []
        if self.guidance is not None:
            for k1 in self.guidance:
                result['Guidance'].append(k1.to_map() if k1 else None)

        if self.notice is not None:
            result['Notice'] = self.notice

        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')

        if m.get('CostDescription') is not None:
            self.cost_description = m.get('CostDescription')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.guidance = []
        if m.get('Guidance') is not None:
            for k1 in m.get('Guidance'):
                temp_model = main_models.ListEvaluationMetadataResponseBodyEvaluationMetadataMetadataRemediationMetadataRemediationActionsGuidance()
                self.guidance.append(temp_model.from_map(k1))

        if m.get('Notice') is not None:
            self.notice = m.get('Notice')

        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')

        return self

class ListEvaluationMetadataResponseBodyEvaluationMetadataMetadataRemediationMetadataRemediationActionsGuidance(DaraModel):
    def __init__(
        self,
        button_name: str = None,
        button_ref: str = None,
        content: str = None,
        title: str = None,
    ):
        # The display name of the fixing button.
        self.button_name = button_name
        # The navigation URL of the fixing button.
        self.button_ref = button_ref
        # The fixing procedure.
        self.content = content
        # The title of the fixing procedure.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.button_name is not None:
            result['ButtonName'] = self.button_name

        if self.button_ref is not None:
            result['ButtonRef'] = self.button_ref

        if self.content is not None:
            result['Content'] = self.content

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ButtonName') is not None:
            self.button_name = m.get('ButtonName')

        if m.get('ButtonRef') is not None:
            self.button_ref = m.get('ButtonRef')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

