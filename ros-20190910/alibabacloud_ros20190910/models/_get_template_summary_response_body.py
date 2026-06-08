# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_ros20190910 import models as main_models
from darabonba.model import DaraModel

class GetTemplateSummaryResponseBody(DaraModel):
    def __init__(
        self,
        description: str = None,
        metadata: Dict[str, Any] = None,
        parameters: List[Dict[str, Any]] = None,
        request_id: str = None,
        resource_identifier_summaries: List[main_models.GetTemplateSummaryResponseBodyResourceIdentifierSummaries] = None,
        resource_types: List[str] = None,
        version: str = None,
    ):
        # The description of the stack template.
        self.description = description
        # The metadata that is defined in the template.
        self.metadata = metadata
        # The declarations of the parameters in the template.
        self.parameters = parameters
        # The request ID.
        self.request_id = request_id
        # The resource identifier summaries.\\
        # A summary describes the resource that you want to import and the properties that are used to identify the resource during the import. For example, VpcId is an identifier property of ALIYUN::ECS::VPC.
        self.resource_identifier_summaries = resource_identifier_summaries
        # All resource types that are used in the template.
        self.resource_types = resource_types
        # The version of the template.
        self.version = version

    def validate(self):
        if self.resource_identifier_summaries:
            for v1 in self.resource_identifier_summaries:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.metadata is not None:
            result['Metadata'] = self.metadata

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ResourceIdentifierSummaries'] = []
        if self.resource_identifier_summaries is not None:
            for k1 in self.resource_identifier_summaries:
                result['ResourceIdentifierSummaries'].append(k1.to_map() if k1 else None)

        if self.resource_types is not None:
            result['ResourceTypes'] = self.resource_types

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.resource_identifier_summaries = []
        if m.get('ResourceIdentifierSummaries') is not None:
            for k1 in m.get('ResourceIdentifierSummaries'):
                temp_model = main_models.GetTemplateSummaryResponseBodyResourceIdentifierSummaries()
                self.resource_identifier_summaries.append(temp_model.from_map(k1))

        if m.get('ResourceTypes') is not None:
            self.resource_types = m.get('ResourceTypes')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class GetTemplateSummaryResponseBodyResourceIdentifierSummaries(DaraModel):
    def __init__(
        self,
        logical_resource_ids: List[str] = None,
        resource_identifiers: List[str] = None,
        resource_type: str = None,
    ):
        # The logical IDs of all resources of the type that is specified by ResouceType in the template.
        self.logical_resource_ids = logical_resource_ids
        # The resource properties. You can use a resource property to identify the resource that you want to manage. For example, VpcId is an identifier property of ALIYUN::ECS::VPC.
        self.resource_identifiers = resource_identifiers
        # The resource type.
        # 
        # > The resource import feature is supported for the resource type.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.logical_resource_ids is not None:
            result['LogicalResourceIds'] = self.logical_resource_ids

        if self.resource_identifiers is not None:
            result['ResourceIdentifiers'] = self.resource_identifiers

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogicalResourceIds') is not None:
            self.logical_resource_ids = m.get('LogicalResourceIds')

        if m.get('ResourceIdentifiers') is not None:
            self.resource_identifiers = m.get('ResourceIdentifiers')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

