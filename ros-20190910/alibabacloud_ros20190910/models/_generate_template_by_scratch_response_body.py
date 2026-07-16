# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_ros20190910 import models as main_models
from darabonba.model import DaraModel

class GenerateTemplateByScratchResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        resources_to_import: List[main_models.GenerateTemplateByScratchResponseBodyResourcesToImport] = None,
        template_body: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The resources that you want to import into a stack in the resource management scenario.
        # 
        # > This parameter is returned only for a resource management scenario.
        self.resources_to_import = resources_to_import
        # The template content of the resource scenario.
        self.template_body = template_body

    def validate(self):
        if self.resources_to_import:
            for v1 in self.resources_to_import:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ResourcesToImport'] = []
        if self.resources_to_import is not None:
            for k1 in self.resources_to_import:
                result['ResourcesToImport'].append(k1.to_map() if k1 else None)

        if self.template_body is not None:
            result['TemplateBody'] = self.template_body

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.resources_to_import = []
        if m.get('ResourcesToImport') is not None:
            for k1 in m.get('ResourcesToImport'):
                temp_model = main_models.GenerateTemplateByScratchResponseBodyResourcesToImport()
                self.resources_to_import.append(temp_model.from_map(k1))

        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')

        return self

class GenerateTemplateByScratchResponseBodyResourcesToImport(DaraModel):
    def __init__(
        self,
        logical_resource_id: str = None,
        resource_identifier: Dict[str, Any] = None,
        resource_type: str = None,
    ):
        # The logical ID of the resource.
        self.logical_resource_id = logical_resource_id
        # The key-value mapping between strings. The value is a JSON string that identifies the resource that you want to import into a stack.\\
        # A key is an identifier for a resource, and a value is an assignment of data to the key. For example, VpcId is a key that indicates the ID of a virtual private cloud (VPC), and `vpc-bp1m6fww66xbntjyc****"` is a value that is assigned to VpcId.
        self.resource_identifier = resource_identifier
        # The type of the resource.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.logical_resource_id is not None:
            result['LogicalResourceId'] = self.logical_resource_id

        if self.resource_identifier is not None:
            result['ResourceIdentifier'] = self.resource_identifier

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogicalResourceId') is not None:
            self.logical_resource_id = m.get('LogicalResourceId')

        if m.get('ResourceIdentifier') is not None:
            self.resource_identifier = m.get('ResourceIdentifier')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

