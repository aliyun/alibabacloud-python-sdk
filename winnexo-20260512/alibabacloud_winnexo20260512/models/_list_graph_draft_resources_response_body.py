# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class ListGraphDraftResourcesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        items: List[main_models.ListGraphDraftResourcesResponseBodyItems] = None,
        message: str = None,
        request_id: str = None,
    ):
        # The status code.
        self.code = code
        # The MCP card list.
        self.items = items
        # The prompt message.
        self.message = message
        # The request trace ID.
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
                temp_model = main_models.ListGraphDraftResourcesResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListGraphDraftResourcesResponseBodyItems(DaraModel):
    def __init__(
        self,
        base_content_hash: str = None,
        base_schema_version: str = None,
        draft_change_id: int = None,
        draft_content_hash: str = None,
        edit_mode: str = None,
        effective_operation: str = None,
        element_type: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        has_online_changed: bool = None,
        operation_type: str = None,
        resource_name: str = None,
        resource_type: str = None,
        risk: str = None,
        source_type: str = None,
    ):
        # The hash of the draft content itself. The value is a 64-character SHA-256 hexadecimal string.
        self.base_content_hash = base_content_hash
        # The active schema version number on which the draft is based.
        self.base_schema_version = base_schema_version
        # The unique ID of the draft change. This ID is referenced when you revoke a draft or publish changes.
        # 
        # This parameter is required.
        self.draft_change_id = draft_change_id
        # The hash of the online content on which the draft was based when it was saved (draft starting point). The value is a 64-character SHA-256 hexadecimal string.
        self.draft_content_hash = draft_content_hash
        # The edit mode. In the current implementation, the value is always YAML, which corresponds to sourceType.
        self.edit_mode = edit_mode
        # The actual publish effect relative to the current online state. After a draft is saved, the online graph may have changed, and the operation intent is adjusted based on the current online state.
        self.effective_operation = effective_operation
        # The element type. Currently, only text is supported.
        # 
        # This parameter is required.
        self.element_type = element_type
        # The creation time.
        self.gmt_create = gmt_create
        # The last modification time in ISO 8601 format.
        self.gmt_modified = gmt_modified
        # Indicates whether the draft baseline has expired. The value is true if the hash of the online content at the time the draft was saved is inconsistent with the hash of the current active content. The ONLINE_CHANGED risk is prompted during publishing.
        # 
        # This parameter is required.
        self.has_online_changed = has_online_changed
        # The operation type.
        self.operation_type = operation_type
        # The resource name of the agent at runtime.
        # 
        # This parameter is required.
        self.resource_name = resource_name
        # The resource type.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The online risk aggregation JSON text (risk_code / risk_message). The value is null if no risk exists.
        self.risk = risk
        # The skill source type.
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

        if self.edit_mode is not None:
            result['editMode'] = self.edit_mode

        if self.effective_operation is not None:
            result['effectiveOperation'] = self.effective_operation

        if self.element_type is not None:
            result['elementType'] = self.element_type

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.has_online_changed is not None:
            result['hasOnlineChanged'] = self.has_online_changed

        if self.operation_type is not None:
            result['operationType'] = self.operation_type

        if self.resource_name is not None:
            result['resourceName'] = self.resource_name

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        if self.risk is not None:
            result['risk'] = self.risk

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

        if m.get('editMode') is not None:
            self.edit_mode = m.get('editMode')

        if m.get('effectiveOperation') is not None:
            self.effective_operation = m.get('effectiveOperation')

        if m.get('elementType') is not None:
            self.element_type = m.get('elementType')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('hasOnlineChanged') is not None:
            self.has_online_changed = m.get('hasOnlineChanged')

        if m.get('operationType') is not None:
            self.operation_type = m.get('operationType')

        if m.get('resourceName') is not None:
            self.resource_name = m.get('resourceName')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        if m.get('risk') is not None:
            self.risk = m.get('risk')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        return self

