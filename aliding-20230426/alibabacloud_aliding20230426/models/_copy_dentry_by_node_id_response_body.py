# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CopyDentryByNodeIdResponseBody(DaraModel):
    def __init__(
        self,
        content_type: str = None,
        created_time: int = None,
        dentry_uuid: str = None,
        extension: str = None,
        request_id: str = None,
        space_id: str = None,
        vendor_request_id: str = None,
        vendor_type: str = None,
    ):
        self.content_type = content_type
        self.created_time = created_time
        self.dentry_uuid = dentry_uuid
        self.extension = extension
        self.request_id = request_id
        self.space_id = space_id
        self.vendor_request_id = vendor_request_id
        self.vendor_type = vendor_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_type is not None:
            result['contentType'] = self.content_type

        if self.created_time is not None:
            result['createdTime'] = self.created_time

        if self.dentry_uuid is not None:
            result['dentryUuid'] = self.dentry_uuid

        if self.extension is not None:
            result['extension'] = self.extension

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.space_id is not None:
            result['spaceId'] = self.space_id

        if self.vendor_request_id is not None:
            result['vendorRequestId'] = self.vendor_request_id

        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')

        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')

        if m.get('dentryUuid') is not None:
            self.dentry_uuid = m.get('dentryUuid')

        if m.get('extension') is not None:
            self.extension = m.get('extension')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('spaceId') is not None:
            self.space_id = m.get('spaceId')

        if m.get('vendorRequestId') is not None:
            self.vendor_request_id = m.get('vendorRequestId')

        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')

        return self

