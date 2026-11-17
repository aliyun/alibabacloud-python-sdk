# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateKnowledgeObjectShrinkRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        content_shrink: str = None,
        description: str = None,
        expected_modify_time: int = None,
        knowledge_base_id: str = None,
        knowledge_object_id: str = None,
        name: str = None,
        upload_id: str = None,
        version_no: int = None,
    ):
        # The client token. This parameter is supported only for DOCUMENT. Model updates do not guarantee exactly-once remote save notifications.
        self.client_token = client_token
        # The typed content update. Object properties are submitted as needed. Arrays are replaced in their entirety when submitted. Unspecified properties are retained.
        self.content_shrink = content_shrink
        # The new description. An empty string clears the description. If this parameter is not specified, the original value is retained.
        self.description = description
        # The expected modification time. This parameter is supported only for DOCUMENT. It is required when modifying the body text and optional when modifying metadata.
        self.expected_modify_time = expected_modify_time
        # The ID of the knowledge base to which the object belongs.
        # 
        # This parameter is required.
        self.knowledge_base_id = knowledge_base_id
        # The stable knowledge object ID returned by the Get or List operation.
        # 
        # This parameter is required.
        self.knowledge_object_id = knowledge_object_id
        # The new name. This parameter cannot be empty. If this parameter is not specified, the original value is retained.
        self.name = name
        # The upload ID. This parameter is supported only for SEMANTIC_MODEL. It replaces the public model content with a complete YAML file and is mutually exclusive with Content.
        self.upload_id = upload_id
        # The version number. This parameter is required when updating Content or UploadId for SEMANTIC_MODEL. Use the VersionNo returned by the Get operation. This is not an optimistic lock.
        self.version_no = version_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.content_shrink is not None:
            result['Content'] = self.content_shrink

        if self.description is not None:
            result['Description'] = self.description

        if self.expected_modify_time is not None:
            result['ExpectedModifyTime'] = self.expected_modify_time

        if self.knowledge_base_id is not None:
            result['KnowledgeBaseId'] = self.knowledge_base_id

        if self.knowledge_object_id is not None:
            result['KnowledgeObjectId'] = self.knowledge_object_id

        if self.name is not None:
            result['Name'] = self.name

        if self.upload_id is not None:
            result['UploadId'] = self.upload_id

        if self.version_no is not None:
            result['VersionNo'] = self.version_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Content') is not None:
            self.content_shrink = m.get('Content')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExpectedModifyTime') is not None:
            self.expected_modify_time = m.get('ExpectedModifyTime')

        if m.get('KnowledgeBaseId') is not None:
            self.knowledge_base_id = m.get('KnowledgeBaseId')

        if m.get('KnowledgeObjectId') is not None:
            self.knowledge_object_id = m.get('KnowledgeObjectId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('UploadId') is not None:
            self.upload_id = m.get('UploadId')

        if m.get('VersionNo') is not None:
            self.version_no = m.get('VersionNo')

        return self

