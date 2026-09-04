# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class CreateGroupFeishuDocRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        directory_id: str = None,
        doc_url: str = None,
        group_id: str = None,
        name: str = None,
        notes: str = None,
        object_bindings: List[main_models.CreateGroupFeishuDocRequestObjectBindings] = None,
        operating_object_name: str = None,
        source_tags: str = None,
        sync_config: main_models.CreateGroupFeishuDocRequestSyncConfig = None,
        tenant_id: str = None,
    ):
        # The description of the AI assistant.
        self.description = description
        # The directory ID.
        self.directory_id = directory_id
        # The document URL.
        # 
        # This parameter is required.
        self.doc_url = doc_url
        # The project group ID.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The image name.
        self.name = name
        # The meeting notes content (optional). The notes are used for auxiliary analysis.
        self.notes = notes
        # The object bindings.
        self.object_bindings = object_bindings
        # The name of the operating object.
        self.operating_object_name = operating_object_name
        # The resource tags (optional, a JSON string list, such as ["tagA","tagB"]).
        self.source_tags = source_tags
        # The synchronization settings.
        self.sync_config = sync_config
        # The tenant ID. This is a common parameter. In winnexo-cli, pass it explicitly with --tenant-id.
        self.tenant_id = tenant_id

    def validate(self):
        if self.object_bindings:
            for v1 in self.object_bindings:
                 if v1:
                    v1.validate()
        if self.sync_config:
            self.sync_config.validate()

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

        if self.group_id is not None:
            result['groupId'] = self.group_id

        if self.name is not None:
            result['name'] = self.name

        if self.notes is not None:
            result['notes'] = self.notes

        result['objectBindings'] = []
        if self.object_bindings is not None:
            for k1 in self.object_bindings:
                result['objectBindings'].append(k1.to_map() if k1 else None)

        if self.operating_object_name is not None:
            result['operatingObjectName'] = self.operating_object_name

        if self.source_tags is not None:
            result['sourceTags'] = self.source_tags

        if self.sync_config is not None:
            result['syncConfig'] = self.sync_config.to_map()

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

        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('notes') is not None:
            self.notes = m.get('notes')

        self.object_bindings = []
        if m.get('objectBindings') is not None:
            for k1 in m.get('objectBindings'):
                temp_model = main_models.CreateGroupFeishuDocRequestObjectBindings()
                self.object_bindings.append(temp_model.from_map(k1))

        if m.get('operatingObjectName') is not None:
            self.operating_object_name = m.get('operatingObjectName')

        if m.get('sourceTags') is not None:
            self.source_tags = m.get('sourceTags')

        if m.get('syncConfig') is not None:
            temp_model = main_models.CreateGroupFeishuDocRequestSyncConfig()
            self.sync_config = temp_model.from_map(m.get('syncConfig'))

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

class CreateGroupFeishuDocRequestSyncConfig(DaraModel):
    def __init__(
        self,
        cron: str = None,
        enabled: bool = None,
        preset: str = None,
    ):
        # The cron expression for the timed scheduling task.
        self.cron = cron
        # Specifies whether to enable or disable synchronization.
        # 
        # This parameter is required.
        self.enabled = enabled
        # The preset mode (can be ignored).
        self.preset = preset

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cron is not None:
            result['cron'] = self.cron

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.preset is not None:
            result['preset'] = self.preset

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cron') is not None:
            self.cron = m.get('cron')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('preset') is not None:
            self.preset = m.get('preset')

        return self

class CreateGroupFeishuDocRequestObjectBindings(DaraModel):
    def __init__(
        self,
        graph_name: str = None,
        object_id: str = None,
        object_type: str = None,
    ):
        # The name of the semantic graph to which the object belongs.
        self.graph_name = graph_name
        # The ID of the recommended item, which can be a **feedId** or a mini-app ID.
        # 
        # This parameter is required.
        self.object_id = object_id
        # The advanced field type.
        # 
        # This parameter is required.
        self.object_type = object_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.graph_name is not None:
            result['graphName'] = self.graph_name

        if self.object_id is not None:
            result['objectId'] = self.object_id

        if self.object_type is not None:
            result['objectType'] = self.object_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('graphName') is not None:
            self.graph_name = m.get('graphName')

        if m.get('objectId') is not None:
            self.object_id = m.get('objectId')

        if m.get('objectType') is not None:
            self.object_type = m.get('objectType')

        return self

