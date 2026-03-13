# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_governance20210120 import models as main_models
from darabonba.model import DaraModel

class ListEvaluationMetricDetailsResponseBody(DaraModel):
    def __init__(
        self,
        date: str = None,
        next_token: str = None,
        request_id: str = None,
        resources: List[main_models.ListEvaluationMetricDetailsResponseBodyResources] = None,
    ):
        self.date = date
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The details of the non-compliant resources.
        self.resources = resources

    def validate(self):
        if self.resources:
            for v1 in self.resources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date is not None:
            result['Date'] = self.date

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Resources'] = []
        if self.resources is not None:
            for k1 in self.resources:
                result['Resources'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.resources = []
        if m.get('Resources') is not None:
            for k1 in m.get('Resources'):
                temp_model = main_models.ListEvaluationMetricDetailsResponseBodyResources()
                self.resources.append(temp_model.from_map(k1))

        return self

class ListEvaluationMetricDetailsResponseBodyResources(DaraModel):
    def __init__(
        self,
        compliance_type: str = None,
        region_id: str = None,
        resource_classification: str = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_owner_id: int = None,
        resource_properties: List[main_models.ListEvaluationMetricDetailsResponseBodyResourcesResourceProperties] = None,
        resource_type: str = None,
    ):
        # The compliance status of the resource. Valid values:
        # 
        # *   NonCompliant: non-compliant.
        # *   Excluded: ignored.
        # *   PendingExclusion: to be ignored.
        # *   PendingInclusion: to be unignored.
        self.compliance_type = compliance_type
        # The region ID of the resource.
        self.region_id = region_id
        # The check results further analyzed by auxiliary decision-making.
        # 
        # >  This parameter is returned only when the check item supports the auxiliary decision-making feature.
        self.resource_classification = resource_classification
        # The ID of the resource.
        self.resource_id = resource_id
        # The name of the resource.
        self.resource_name = resource_name
        # The ID of the Alibaba Cloud account that owns the resource.
        self.resource_owner_id = resource_owner_id
        # The attributes of the resource.
        self.resource_properties = resource_properties
        # The type of the resource.
        self.resource_type = resource_type

    def validate(self):
        if self.resource_properties:
            for v1 in self.resource_properties:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compliance_type is not None:
            result['ComplianceType'] = self.compliance_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_classification is not None:
            result['ResourceClassification'] = self.resource_classification

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        result['ResourceProperties'] = []
        if self.resource_properties is not None:
            for k1 in self.resource_properties:
                result['ResourceProperties'].append(k1.to_map() if k1 else None)

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComplianceType') is not None:
            self.compliance_type = m.get('ComplianceType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceClassification') is not None:
            self.resource_classification = m.get('ResourceClassification')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        self.resource_properties = []
        if m.get('ResourceProperties') is not None:
            for k1 in m.get('ResourceProperties'):
                temp_model = main_models.ListEvaluationMetricDetailsResponseBodyResourcesResourceProperties()
                self.resource_properties.append(temp_model.from_map(k1))

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

class ListEvaluationMetricDetailsResponseBodyResourcesResourceProperties(DaraModel):
    def __init__(
        self,
        property_name: str = None,
        property_value: str = None,
    ):
        # The name of the resource attribute.
        self.property_name = property_name
        # The value of the resource attribute.
        self.property_value = property_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.property_name is not None:
            result['PropertyName'] = self.property_name

        if self.property_value is not None:
            result['PropertyValue'] = self.property_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PropertyName') is not None:
            self.property_name = m.get('PropertyName')

        if m.get('PropertyValue') is not None:
            self.property_value = m.get('PropertyValue')

        return self

