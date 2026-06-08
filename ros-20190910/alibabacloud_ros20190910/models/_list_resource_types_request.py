# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListResourceTypesRequest(DaraModel):
    def __init__(
        self,
        entity_type: str = None,
        provider: str = None,
        resource_type: str = None,
    ):
        # The entity type. Valid values:
        # 
        # *   All: all types of resources.
        # *   Resource (default): regular resources. For more information, see [Resources](https://help.aliyun.com/document_detail/28863.html).
        # *   DataSource: DataSource resources. For more information, see [DataSource resources](https://help.aliyun.com/document_detail/404753.html).
        # *   Module: modules.
        self.entity_type = entity_type
        # The provider of the resource type. Valid values:
        # 
        # *   ROS (default): The resource type is provided by Resource Orchestration Service (ROS).
        # *   Self: The resource type is provided by you.
        self.provider = provider
        # The resource type. The resource type can contain letters, digits, colons (:), and asterisks (\\*). You can use an asterisk (\\*) to perform a fuzzy match.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type

        if self.provider is not None:
            result['Provider'] = self.provider

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')

        if m.get('Provider') is not None:
            self.provider = m.get('Provider')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

