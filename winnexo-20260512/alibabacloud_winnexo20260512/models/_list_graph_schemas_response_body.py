# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class ListGraphSchemasResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        items: List[main_models.ListGraphSchemasResponseBodyItems] = None,
        message: str = None,
        request_id: str = None,
    ):
        # The status code.
        self.code = code
        # The location clustering.
        self.items = items
        # The prompt message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.ListGraphSchemasResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListGraphSchemasResponseBodyItems(DaraModel):
    def __init__(
        self,
        active_version: str = None,
        business_profile: str = None,
        display_name: str = None,
        graph_name: str = None,
        graph_status: str = None,
        has_draft: bool = None,
        is_default: bool = None,
        object_type_count: int = None,
        relation_count: int = None,
        semantic_tags: List[str] = None,
    ):
        # The currently active schema version number. The value is 0.0.0 for a quick-created placeholder graph.
        self.active_version = active_version
        # The business description of the graph. An empty string is returned if this parameter is not configured.
        self.business_profile = business_profile
        # The display name of the tool.
        self.display_name = display_name
        # The graph name.
        # 
        # This parameter is required.
        self.graph_name = graph_name
        # The status of the semantic graph.
        # 
        # This parameter is required.
        self.graph_status = graph_status
        # Indicates whether the graph contains a draft.
        # 
        # This parameter is required.
        self.has_draft = has_draft
        # Indicates whether this is the default group.
        # 
        # This parameter is required.
        self.is_default = is_default
        # The number of object types. The value falls back to 0 if parsing fails.
        # 
        # This parameter is required.
        self.object_type_count = object_type_count
        # The number of relations. The value falls back to 0 if parsing fails.
        # 
        # This parameter is required.
        self.relation_count = relation_count
        # The list of semantic tags. An empty array [] is returned if this parameter is not configured.
        # 
        # This parameter is required.
        self.semantic_tags = semantic_tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active_version is not None:
            result['activeVersion'] = self.active_version

        if self.business_profile is not None:
            result['businessProfile'] = self.business_profile

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.graph_name is not None:
            result['graphName'] = self.graph_name

        if self.graph_status is not None:
            result['graphStatus'] = self.graph_status

        if self.has_draft is not None:
            result['hasDraft'] = self.has_draft

        if self.is_default is not None:
            result['isDefault'] = self.is_default

        if self.object_type_count is not None:
            result['objectTypeCount'] = self.object_type_count

        if self.relation_count is not None:
            result['relationCount'] = self.relation_count

        if self.semantic_tags is not None:
            result['semanticTags'] = self.semantic_tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('activeVersion') is not None:
            self.active_version = m.get('activeVersion')

        if m.get('businessProfile') is not None:
            self.business_profile = m.get('businessProfile')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('graphName') is not None:
            self.graph_name = m.get('graphName')

        if m.get('graphStatus') is not None:
            self.graph_status = m.get('graphStatus')

        if m.get('hasDraft') is not None:
            self.has_draft = m.get('hasDraft')

        if m.get('isDefault') is not None:
            self.is_default = m.get('isDefault')

        if m.get('objectTypeCount') is not None:
            self.object_type_count = m.get('objectTypeCount')

        if m.get('relationCount') is not None:
            self.relation_count = m.get('relationCount')

        if m.get('semanticTags') is not None:
            self.semantic_tags = m.get('semanticTags')

        return self

