# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetGroupSourceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        description: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        group_id: str = None,
        message: str = None,
        name: str = None,
        request_id: str = None,
        scope: str = None,
        source_id: str = None,
        source_kind: str = None,
        source_tags: str = None,
        source_type: str = None,
        status: str = None,
    ):
        # The error code.
        self.code = code
        # The pipeline description.
        self.description = description
        # The time when the resource was created.
        self.gmt_create = gmt_create
        # The time when the resource was last modified, in ISO 8601 format.
        self.gmt_modified = gmt_modified
        # The project group ID.
        self.group_id = group_id
        # The description of the status code.
        self.message = message
        # The name.
        self.name = name
        # The request trace ID.
        self.request_id = request_id
        # The permission scope.
        self.scope = scope
        # The data source ID.
        self.source_id = source_id
        # The knowledge base ownership type. Valid values:
        # 
        # - aliding_kb_doc: DingTalk knowledge base document.
        # - normal: Common knowledge.
        self.source_kind = source_kind
        # The resource tags. This parameter is optional. The value is a JSON string list, such as ["tagA","tagB"].
        self.source_tags = source_tags
        # The type of the resource source. Valid values:
        # 
        # - ExportTaskId: The resource export ID.
        # - TaskId: The module execution task ID.
        # - StatePath: The OSS path where the resource state is stored.
        self.source_type = source_type
        # The resource status. The initial status during the creation process is typically PENDING. If the on_create operation fails, the status is FAILED.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.description is not None:
            result['description'] = self.description

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.group_id is not None:
            result['groupId'] = self.group_id

        if self.message is not None:
            result['message'] = self.message

        if self.name is not None:
            result['name'] = self.name

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.scope is not None:
            result['scope'] = self.scope

        if self.source_id is not None:
            result['sourceId'] = self.source_id

        if self.source_kind is not None:
            result['sourceKind'] = self.source_kind

        if self.source_tags is not None:
            result['sourceTags'] = self.source_tags

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('scope') is not None:
            self.scope = m.get('scope')

        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')

        if m.get('sourceKind') is not None:
            self.source_kind = m.get('sourceKind')

        if m.get('sourceTags') is not None:
            self.source_tags = m.get('sourceTags')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

