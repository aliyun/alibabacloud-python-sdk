# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetUserDocumentPermissionResponseBody(DaraModel):
    def __init__(
        self,
        auth_level: int = None,
        has_permission: bool = None,
        request_id: str = None,
        vendor_request_id: str = None,
        vendor_type: str = None,
    ):
        self.auth_level = auth_level
        self.has_permission = has_permission
        self.request_id = request_id
        self.vendor_request_id = vendor_request_id
        self.vendor_type = vendor_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_level is not None:
            result['authLevel'] = self.auth_level

        if self.has_permission is not None:
            result['hasPermission'] = self.has_permission

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.vendor_request_id is not None:
            result['vendorRequestId'] = self.vendor_request_id

        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authLevel') is not None:
            self.auth_level = m.get('authLevel')

        if m.get('hasPermission') is not None:
            self.has_permission = m.get('hasPermission')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('vendorRequestId') is not None:
            self.vendor_request_id = m.get('vendorRequestId')

        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')

        return self

