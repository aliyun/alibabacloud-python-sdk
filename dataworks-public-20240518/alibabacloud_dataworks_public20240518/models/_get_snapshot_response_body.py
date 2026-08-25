# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class GetSnapshotResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        snapshot: main_models.GetSnapshotResponseBodySnapshot = None,
    ):
        # Id of the request
        self.request_id = request_id
        # The snapshot.
        self.snapshot = snapshot

    def validate(self):
        if self.snapshot:
            self.snapshot.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.snapshot is not None:
            result['Snapshot'] = self.snapshot.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Snapshot') is not None:
            temp_model = main_models.GetSnapshotResponseBodySnapshot()
            self.snapshot = temp_model.from_map(m.get('Snapshot'))

        return self

class GetSnapshotResponseBodySnapshot(DaraModel):
    def __init__(
        self,
        comment: str = None,
        content: main_models.GetSnapshotResponseBodySnapshotContent = None,
        content_url: str = None,
        create_time: int = None,
        creator: str = None,
        id: str = None,
        namespace: str = None,
        object_id: str = None,
        type: str = None,
        version: int = None,
    ):
        # The submit comment.
        self.comment = comment
        # The structured snapshot content. This parameter is mutually exclusive with ContentUrl.
        self.content = content
        # The OSS pre-signed download URL. This parameter is mutually exclusive with Content.
        self.content_url = content_url
        # The snapshot creation time in millisecond timestamp.
        self.create_time = create_time
        # The employee ID of the submitter.
        self.creator = creator
        # The unique ID of the snapshot.
        self.id = id
        # The namespace.
        self.namespace = namespace
        # The unique ID of the object to which the snapshot belongs.
        self.object_id = object_id
        # The snapshot type.
        self.type = type
        # The version number.
        self.version = version

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.content is not None:
            result['Content'] = self.content.to_map()

        if self.content_url is not None:
            result['ContentUrl'] = self.content_url

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.id is not None:
            result['Id'] = self.id

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.object_id is not None:
            result['ObjectId'] = self.object_id

        if self.type is not None:
            result['Type'] = self.type

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('Content') is not None:
            temp_model = main_models.GetSnapshotResponseBodySnapshotContent()
            self.content = temp_model.from_map(m.get('Content'))

        if m.get('ContentUrl') is not None:
            self.content_url = m.get('ContentUrl')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class GetSnapshotResponseBodySnapshotContent(DaraModel):
    def __init__(
        self,
        content: str = None,
        spec: str = None,
        stage_code: str = None,
    ):
        # The node script content.
        self.content = content
        # FlowSpec JSON
        self.spec = spec
        # The stage code.
        self.stage_code = stage_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.spec is not None:
            result['Spec'] = self.spec

        if self.stage_code is not None:
            result['StageCode'] = self.stage_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        if m.get('StageCode') is not None:
            self.stage_code = m.get('StageCode')

        return self

