# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class SaveGraphDraftBatchDefineResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        graph_name: str = None,
        items: List[main_models.SaveGraphDraftBatchDefineResponseBodyItems] = None,
        message: str = None,
        request_id: str = None,
        save_mode: str = None,
        saved_count: int = None,
    ):
        # The status code.
        self.code = code
        # The graph name.
        self.graph_name = graph_name
        # The list of MCP cards.
        self.items = items
        # The status code description.
        self.message = message
        # The request trace ID.
        self.request_id = request_id
        # The save mode.
        self.save_mode = save_mode
        # The number of saved items.
        self.saved_count = saved_count

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

        if self.graph_name is not None:
            result['graphName'] = self.graph_name

        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.save_mode is not None:
            result['saveMode'] = self.save_mode

        if self.saved_count is not None:
            result['savedCount'] = self.saved_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('graphName') is not None:
            self.graph_name = m.get('graphName')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.SaveGraphDraftBatchDefineResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('saveMode') is not None:
            self.save_mode = m.get('saveMode')

        if m.get('savedCount') is not None:
            self.saved_count = m.get('savedCount')

        return self

class SaveGraphDraftBatchDefineResponseBodyItems(DaraModel):
    def __init__(
        self,
        base_content_hash: str = None,
        base_schema_version: str = None,
        draft_change_id: int = None,
        draft_content_hash: str = None,
        element_type: str = None,
        gmt_modified: str = None,
        operation_type: str = None,
        resource_name: str = None,
        resource_type: str = None,
        source_type: str = None,
    ):
        # The hash of the draft content itself, a 64-character SHA-256 hexadecimal string.
        self.base_content_hash = base_content_hash
        # The active schema version number on which the draft is based.
        self.base_schema_version = base_schema_version
        # The unique draft change ID, referenced when revoking drafts or publishing.
        self.draft_change_id = draft_change_id
        # The online content hash on which the draft save is based (draft starting point), a 64-character SHA-256 hexadecimal string.
        self.draft_content_hash = draft_content_hash
        # The element type. Currently, only text is supported.
        # 
        # This parameter is required.
        self.element_type = element_type
        # The update time in ISO 8601 format.
        self.gmt_modified = gmt_modified
        # The operation type.
        self.operation_type = operation_type
        # The resource name of the agent runtime.
        # 
        # This parameter is required.
        self.resource_name = resource_name
        # The resource type.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The source type.
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.base_content_hash is not None:
            result['baseContentHash'] = self.base_content_hash

        if self.base_schema_version is not None:
            result['baseSchemaVersion'] = self.base_schema_version

        if self.draft_change_id is not None:
            result['draftChangeId'] = self.draft_change_id

        if self.draft_content_hash is not None:
            result['draftContentHash'] = self.draft_content_hash

        if self.element_type is not None:
            result['elementType'] = self.element_type

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.operation_type is not None:
            result['operationType'] = self.operation_type

        if self.resource_name is not None:
            result['resourceName'] = self.resource_name

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('baseContentHash') is not None:
            self.base_content_hash = m.get('baseContentHash')

        if m.get('baseSchemaVersion') is not None:
            self.base_schema_version = m.get('baseSchemaVersion')

        if m.get('draftChangeId') is not None:
            self.draft_change_id = m.get('draftChangeId')

        if m.get('draftContentHash') is not None:
            self.draft_content_hash = m.get('draftContentHash')

        if m.get('elementType') is not None:
            self.element_type = m.get('elementType')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('operationType') is not None:
            self.operation_type = m.get('operationType')

        if m.get('resourceName') is not None:
            self.resource_name = m.get('resourceName')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        return self

