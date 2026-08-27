# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePersonalFeishuDocShrinkRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        directory_id: str = None,
        doc_url: str = None,
        name: str = None,
        notes: str = None,
        object_bindings_shrink: str = None,
        operating_object_name: str = None,
        source_tags: str = None,
        sync_config_shrink: str = None,
        tenant_id: str = None,
    ):
        # The pipeline description.
        self.description = description
        # The folder ID.
        self.directory_id = directory_id
        # The document URL.
        # 
        # This parameter is required.
        self.doc_url = doc_url
        # The updated name of the filter view.
        self.name = name
        # The meeting notes content (optional). The notes are used for auxiliary analysis.
        self.notes = notes
        # The object bindings.
        self.object_bindings_shrink = object_bindings_shrink
        # The digital employee name (operating object name, optional).
        self.operating_object_name = operating_object_name
        # The resource tags (optional, a JSON string list, such as ["tagA","tagB"]).
        self.source_tags = source_tags
        # The synchronization settings.
        self.sync_config_shrink = sync_config_shrink
        # The tenant ID.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.directory_id is not None:
            result['directoryId'] = self.directory_id

        if self.doc_url is not None:
            result['docUrl'] = self.doc_url

        if self.name is not None:
            result['name'] = self.name

        if self.notes is not None:
            result['notes'] = self.notes

        if self.object_bindings_shrink is not None:
            result['objectBindings'] = self.object_bindings_shrink

        if self.operating_object_name is not None:
            result['operatingObjectName'] = self.operating_object_name

        if self.source_tags is not None:
            result['sourceTags'] = self.source_tags

        if self.sync_config_shrink is not None:
            result['syncConfig'] = self.sync_config_shrink

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('directoryId') is not None:
            self.directory_id = m.get('directoryId')

        if m.get('docUrl') is not None:
            self.doc_url = m.get('docUrl')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('notes') is not None:
            self.notes = m.get('notes')

        if m.get('objectBindings') is not None:
            self.object_bindings_shrink = m.get('objectBindings')

        if m.get('operatingObjectName') is not None:
            self.operating_object_name = m.get('operatingObjectName')

        if m.get('sourceTags') is not None:
            self.source_tags = m.get('sourceTags')

        if m.get('syncConfig') is not None:
            self.sync_config_shrink = m.get('syncConfig')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

