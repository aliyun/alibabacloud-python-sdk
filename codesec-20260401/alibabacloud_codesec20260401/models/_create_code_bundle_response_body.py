# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_codesec20260401 import models as main_models
from darabonba.model import DaraModel

class CreateCodeBundleResponseBody(DaraModel):
    def __init__(
        self,
        bundle_version: str = None,
        code_bundle_id: int = None,
        created_at: str = None,
        filename: str = None,
        project_id: int = None,
        request_id: str = None,
        status: str = None,
        updated_at: str = None,
        upload: main_models.CreateCodeBundleResponseBodyUpload = None,
    ):
        # The version identifier of the function code package.
        self.bundle_version = bundle_version
        # The function code package ID.
        self.code_bundle_id = code_bundle_id
        # The time when the function code package was created.
        self.created_at = created_at
        # The file name.
        self.filename = filename
        # The project ID.
        self.project_id = project_id
        # The request ID.
        self.request_id = request_id
        # The status of the function code package.
        self.status = status
        # The time when the function code package was last updated.
        self.updated_at = updated_at
        # The upload credential. See the following fields for details.
        self.upload = upload

    def validate(self):
        if self.upload:
            self.upload.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bundle_version is not None:
            result['bundleVersion'] = self.bundle_version

        if self.code_bundle_id is not None:
            result['codeBundleId'] = self.code_bundle_id

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

        if self.upload is not None:
            result['upload'] = self.upload.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bundleVersion') is not None:
            self.bundle_version = m.get('bundleVersion')

        if m.get('codeBundleId') is not None:
            self.code_bundle_id = m.get('codeBundleId')

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

        if m.get('upload') is not None:
            temp_model = main_models.CreateCodeBundleResponseBodyUpload()
            self.upload = temp_model.from_map(m.get('upload'))

        return self



class CreateCodeBundleResponseBodyUpload(DaraModel):
    def __init__(
        self,
        expires_at: str = None,
        method: str = None,
        put_url: str = None,
        required_content_type: str = None,
    ):
        # The expiration time of the credential in RFC 3339 format.
        self.expires_at = expires_at
        # The HTTP method of the pre-signed URL. Valid values: PUT.
        self.method = method
        # The pre-signed OSS PUT upload URL.
        self.put_url = put_url
        # The Content-Type header that the client must include when performing the PUT request. This field is returned when putUrl is present.
        self.required_content_type = required_content_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expires_at is not None:
            result['expiresAt'] = self.expires_at

        if self.method is not None:
            result['method'] = self.method

        if self.put_url is not None:
            result['putUrl'] = self.put_url

        if self.required_content_type is not None:
            result['requiredContentType'] = self.required_content_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expiresAt') is not None:
            self.expires_at = m.get('expiresAt')

        if m.get('method') is not None:
            self.method = m.get('method')

        if m.get('putUrl') is not None:
            self.put_url = m.get('putUrl')

        if m.get('requiredContentType') is not None:
            self.required_content_type = m.get('requiredContentType')

        return self

