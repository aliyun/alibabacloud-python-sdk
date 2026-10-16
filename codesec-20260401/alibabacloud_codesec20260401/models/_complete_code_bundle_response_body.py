# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CompleteCodeBundleResponseBody(DaraModel):
    def __init__(
        self,
        bundle_version: str = None,
        byte_size: int = None,
        code_bundle_id: int = None,
        content_type: str = None,
        created_at: str = None,
        filename: str = None,
        project_id: int = None,
        request_id: str = None,
        status: str = None,
        updated_at: str = None,
    ):
        # The code bundle version identifier.
        self.bundle_version = bundle_version
        # The object size.
        self.byte_size = byte_size
        # The code bundle ID.
        self.code_bundle_id = code_bundle_id
        # The MIME type of the stored code bundle. This is typically application/octet-stream for pre-signed PUT operations.
        self.content_type = content_type
        # The time when the record was created, in RFC 3339 format.
        self.created_at = created_at
        # The file name.
        self.filename = filename
        # The project ID.
        self.project_id = project_id
        # The request ID.
        self.request_id = request_id
        # The code bundle status.
        self.status = status
        # The time when the record was last updated.
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bundle_version is not None:
            result['bundleVersion'] = self.bundle_version

        if self.byte_size is not None:
            result['byteSize'] = self.byte_size

        if self.code_bundle_id is not None:
            result['codeBundleId'] = self.code_bundle_id

        if self.content_type is not None:
            result['contentType'] = self.content_type

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.filename is not None:
            result['filename'] = self.filename

        if self.project_id is not None:
            result['projectId'] = self.project_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.status is not None:
            result['status'] = self.status

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bundleVersion') is not None:
            self.bundle_version = m.get('bundleVersion')

        if m.get('byteSize') is not None:
            self.byte_size = m.get('byteSize')

        if m.get('codeBundleId') is not None:
            self.code_bundle_id = m.get('codeBundleId')

        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('filename') is not None:
            self.filename = m.get('filename')

        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        return self

