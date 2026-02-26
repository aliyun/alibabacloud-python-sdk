# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcecenter20221201 import models as main_models
from darabonba.model import DaraModel

class ListResourceTypesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        resource_types: List[main_models.ListResourceTypesResponseBodyResourceTypes] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The resource types.
        self.resource_types = resource_types

    def validate(self):
        if self.resource_types:
            for v1 in self.resource_types:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ResourceTypes'] = []
        if self.resource_types is not None:
            for k1 in self.resource_types:
                result['ResourceTypes'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.resource_types = []
        if m.get('ResourceTypes') is not None:
            for k1 in m.get('ResourceTypes'):
                temp_model = main_models.ListResourceTypesResponseBodyResourceTypes()
                self.resource_types.append(temp_model.from_map(k1))

        return self

class ListResourceTypesResponseBodyResourceTypes(DaraModel):
    def __init__(
        self,
        code_mapping: main_models.ListResourceTypesResponseBodyResourceTypesCodeMapping = None,
        filter_keys: List[str] = None,
        product_name: str = None,
        related_resource_types: List[str] = None,
        resource_type: str = None,
        resource_type_name: str = None,
    ):
        # The code mapping of the resource type.
        self.code_mapping = code_mapping
        # The supported filter conditions.
        self.filter_keys = filter_keys
        # The name of the Alibaba Cloud service.
        self.product_name = product_name
        # The name of supported related resource types.
        self.related_resource_types = related_resource_types
        # The resource type.
        self.resource_type = resource_type
        # The name of the resource type.
        self.resource_type_name = resource_type_name

    def validate(self):
        if self.code_mapping:
            self.code_mapping.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code_mapping is not None:
            result['CodeMapping'] = self.code_mapping.to_map()

        if self.filter_keys is not None:
            result['FilterKeys'] = self.filter_keys

        if self.product_name is not None:
            result['ProductName'] = self.product_name

        if self.related_resource_types is not None:
            result['RelatedResourceTypes'] = self.related_resource_types

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.resource_type_name is not None:
            result['ResourceTypeName'] = self.resource_type_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CodeMapping') is not None:
            temp_model = main_models.ListResourceTypesResponseBodyResourceTypesCodeMapping()
            self.code_mapping = temp_model.from_map(m.get('CodeMapping'))

        if m.get('FilterKeys') is not None:
            self.filter_keys = m.get('FilterKeys')

        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')

        if m.get('RelatedResourceTypes') is not None:
            self.related_resource_types = m.get('RelatedResourceTypes')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('ResourceTypeName') is not None:
            self.resource_type_name = m.get('ResourceTypeName')

        return self

class ListResourceTypesResponseBodyResourceTypesCodeMapping(DaraModel):
    def __init__(
        self,
        resource_group: str = None,
        tag: str = None,
    ):
        # The resource group.
        self.resource_group = resource_group
        # The tag.
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group

        if self.tag is not None:
            result['Tag'] = self.tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroup') is not None:
            self.resource_group = m.get('ResourceGroup')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        return self

