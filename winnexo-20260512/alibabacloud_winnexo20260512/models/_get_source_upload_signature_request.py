# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSourceUploadSignatureRequest(DaraModel):
    def __init__(
        self,
        content_type: str = None,
        expires: int = None,
        filename: str = None,
        operating_object_name: str = None,
        scope: str = None,
        tenant_id: str = None,
    ):
        # The content type. Valid values: Text and Markdown.
        self.content_type = content_type
        # The expiration time of the signed URL, in seconds. Default value: 3600.
        self.expires = expires
        # The file name.
        # 
        # This parameter is required.
        self.filename = filename
        # The name of the digital employee (operating object name). This parameter is optional.
        self.operating_object_name = operating_object_name
        # The permission scope.
        self.scope = scope
        # The tenant ID to which the task belongs.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_type is not None:
            result['contentType'] = self.content_type

        if self.expires is not None:
            result['expires'] = self.expires

        if self.filename is not None:
            result['filename'] = self.filename

        if self.operating_object_name is not None:
            result['operatingObjectName'] = self.operating_object_name

        if self.scope is not None:
            result['scope'] = self.scope

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')

        if m.get('expires') is not None:
            self.expires = m.get('expires')

        if m.get('filename') is not None:
            self.filename = m.get('filename')

        if m.get('operatingObjectName') is not None:
            self.operating_object_name = m.get('operatingObjectName')

        if m.get('scope') is not None:
            self.scope = m.get('scope')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

