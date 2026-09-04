# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class GetSourceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        completion_time: str = None,
        description: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        has_notes: bool = None,
        has_settings: bool = None,
        has_structured_tables: bool = None,
        has_unstructured_docs: bool = None,
        message: str = None,
        name: str = None,
        notes: str = None,
        object_bindings: List[main_models.GetSourceResponseBodyObjectBindings] = None,
        object_id: str = None,
        object_type: str = None,
        operating_object_name: str = None,
        request_id: str = None,
        scope: str = None,
        settings: Dict[str, Any] = None,
        skill_output_id: str = None,
        source_id: str = None,
        source_kind: str = None,
        source_tags: str = None,
        source_type: str = None,
        status: str = None,
        structured_tables: List[str] = None,
        unstructured_docs: List[main_models.GetSourceResponseBodyUnstructuredDocs] = None,
    ):
        # The error code.
        self.code = code
        # The completion time, in milliseconds.
        self.completion_time = completion_time
        # The description of the to-do card type.
        self.description = description
        # The creation time.
        self.gmt_create = gmt_create
        # The last modification time.
        self.gmt_modified = gmt_modified
        # Indicates whether notes exist.
        self.has_notes = has_notes
        # Indicates whether settings configuration exists.
        self.has_settings = has_settings
        # Indicates whether structured tables exist.
        self.has_structured_tables = has_structured_tables
        # Indicates whether unstructured documents exist.
        self.has_unstructured_docs = has_unstructured_docs
        # The status code description.
        self.message = message
        # The username.
        self.name = name
        # The meeting notes content (optional). The notes are used for auxiliary analysis.
        self.notes = notes
        # The object bindings.
        self.object_bindings = object_bindings
        # The associated variable ID.
        self.object_id = object_id
        # The object type, such as customer. This field has a value when type is set to mention.
        self.object_type = object_type
        # The digital employee name (operating object name, optional).
        self.operating_object_name = operating_object_name
        # The request ID.
        self.request_id = request_id
        # The task scope.
        self.scope = scope
        # The user profile settings.
        self.settings = settings
        # The skill output ID (carried when the output is saved as a resource).
        self.skill_output_id = skill_output_id
        # The data source ID.
        self.source_id = source_id
        # The knowledge base (KB) ownership type. Valid values:
        # - aliding_kb_doc: DingTalk knowledge base document.
        # - normal: common knowledge.
        self.source_kind = source_kind
        # The resource tags (optional, a JSON string list such as ["tagA","tagB"]).
        self.source_tags = source_tags
        # The resource type.
        self.source_type = source_type
        # The final status of the message.
        self.status = status
        # The list of structured tables.
        self.structured_tables = structured_tables
        # The unstructured documents.
        self.unstructured_docs = unstructured_docs

    def validate(self):
        if self.object_bindings:
            for v1 in self.object_bindings:
                 if v1:
                    v1.validate()
        if self.unstructured_docs:
            for v1 in self.unstructured_docs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.completion_time is not None:
            result['completionTime'] = self.completion_time

        if self.description is not None:
            result['description'] = self.description

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.has_notes is not None:
            result['hasNotes'] = self.has_notes

        if self.has_settings is not None:
            result['hasSettings'] = self.has_settings

        if self.has_structured_tables is not None:
            result['hasStructuredTables'] = self.has_structured_tables

        if self.has_unstructured_docs is not None:
            result['hasUnstructuredDocs'] = self.has_unstructured_docs

        if self.message is not None:
            result['message'] = self.message

        if self.name is not None:
            result['name'] = self.name

        if self.notes is not None:
            result['notes'] = self.notes

        result['objectBindings'] = []
        if self.object_bindings is not None:
            for k1 in self.object_bindings:
                result['objectBindings'].append(k1.to_map() if k1 else None)

        if self.object_id is not None:
            result['objectId'] = self.object_id

        if self.object_type is not None:
            result['objectType'] = self.object_type

        if self.operating_object_name is not None:
            result['operatingObjectName'] = self.operating_object_name

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.scope is not None:
            result['scope'] = self.scope

        if self.settings is not None:
            result['settings'] = self.settings

        if self.skill_output_id is not None:
            result['skillOutputId'] = self.skill_output_id

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

        if self.structured_tables is not None:
            result['structuredTables'] = self.structured_tables

        result['unstructuredDocs'] = []
        if self.unstructured_docs is not None:
            for k1 in self.unstructured_docs:
                result['unstructuredDocs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('completionTime') is not None:
            self.completion_time = m.get('completionTime')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('hasNotes') is not None:
            self.has_notes = m.get('hasNotes')

        if m.get('hasSettings') is not None:
            self.has_settings = m.get('hasSettings')

        if m.get('hasStructuredTables') is not None:
            self.has_structured_tables = m.get('hasStructuredTables')

        if m.get('hasUnstructuredDocs') is not None:
            self.has_unstructured_docs = m.get('hasUnstructuredDocs')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('notes') is not None:
            self.notes = m.get('notes')

        self.object_bindings = []
        if m.get('objectBindings') is not None:
            for k1 in m.get('objectBindings'):
                temp_model = main_models.GetSourceResponseBodyObjectBindings()
                self.object_bindings.append(temp_model.from_map(k1))

        if m.get('objectId') is not None:
            self.object_id = m.get('objectId')

        if m.get('objectType') is not None:
            self.object_type = m.get('objectType')

        if m.get('operatingObjectName') is not None:
            self.operating_object_name = m.get('operatingObjectName')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('scope') is not None:
            self.scope = m.get('scope')

        if m.get('settings') is not None:
            self.settings = m.get('settings')

        if m.get('skillOutputId') is not None:
            self.skill_output_id = m.get('skillOutputId')

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

        if m.get('structuredTables') is not None:
            self.structured_tables = m.get('structuredTables')

        self.unstructured_docs = []
        if m.get('unstructuredDocs') is not None:
            for k1 in m.get('unstructuredDocs'):
                temp_model = main_models.GetSourceResponseBodyUnstructuredDocs()
                self.unstructured_docs.append(temp_model.from_map(k1))

        return self

class GetSourceResponseBodyUnstructuredDocs(DaraModel):
    def __init__(
        self,
        completion_time: str = None,
        file_name: str = None,
        file_record_id: str = None,
        file_type: str = None,
        oss_url: str = None,
        semantics_id: str = None,
    ):
        # The completion time, in milliseconds.
        self.completion_time = completion_time
        # The file name, including the file name extension.
        self.file_name = file_name
        # The file record ID (optional, corresponding to settings.file_record_id).
        self.file_record_id = file_record_id
        # The file type. Valid values:
        # - **file**: file.
        # - **folder**: folder.
        self.file_type = file_type
        # The session analysis result in OSS URL format. The URL expires in one hour.
        self.oss_url = oss_url
        # The DocumentAgent semantic ID.
        self.semantics_id = semantics_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.completion_time is not None:
            result['completionTime'] = self.completion_time

        if self.file_name is not None:
            result['fileName'] = self.file_name

        if self.file_record_id is not None:
            result['fileRecordId'] = self.file_record_id

        if self.file_type is not None:
            result['fileType'] = self.file_type

        if self.oss_url is not None:
            result['ossUrl'] = self.oss_url

        if self.semantics_id is not None:
            result['semanticsId'] = self.semantics_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('completionTime') is not None:
            self.completion_time = m.get('completionTime')

        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')

        if m.get('fileRecordId') is not None:
            self.file_record_id = m.get('fileRecordId')

        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')

        if m.get('ossUrl') is not None:
            self.oss_url = m.get('ossUrl')

        if m.get('semanticsId') is not None:
            self.semantics_id = m.get('semanticsId')

        return self

class GetSourceResponseBodyObjectBindings(DaraModel):
    def __init__(
        self,
        graph_name: str = None,
        object_id: str = None,
        object_type: str = None,
    ):
        # The semantic graph name to which the object belongs.
        self.graph_name = graph_name
        # The ID of the recommended item, which can be a **feedId** or a micro-application ID.
        self.object_id = object_id
        # The object type, such as customer. This field has a value when type is set to mention.
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

