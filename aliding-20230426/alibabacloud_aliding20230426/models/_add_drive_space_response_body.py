# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddDriveSpaceResponseBody(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        modify_time: str = None,
        permission_mode: str = None,
        quota: int = None,
        request_id: str = None,
        space_id: str = None,
        space_name: str = None,
        space_type: str = None,
        used_quota: int = None,
        vendor_request_id: str = None,
        vendor_type: str = None,
    ):
        self.create_time = create_time
        self.modify_time = modify_time
        self.permission_mode = permission_mode
        self.quota = quota
        self.request_id = request_id
        self.space_id = space_id
        self.space_name = space_name
        self.space_type = space_type
        self.used_quota = used_quota
        self.vendor_request_id = vendor_request_id
        self.vendor_type = vendor_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.modify_time is not None:
            result['modifyTime'] = self.modify_time

        if self.permission_mode is not None:
            result['permissionMode'] = self.permission_mode

        if self.quota is not None:
            result['quota'] = self.quota

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.space_id is not None:
            result['spaceId'] = self.space_id

        if self.space_name is not None:
            result['spaceName'] = self.space_name

        if self.space_type is not None:
            result['spaceType'] = self.space_type

        if self.used_quota is not None:
            result['usedQuota'] = self.used_quota

        if self.vendor_request_id is not None:
            result['vendorRequestId'] = self.vendor_request_id

        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('modifyTime') is not None:
            self.modify_time = m.get('modifyTime')

        if m.get('permissionMode') is not None:
            self.permission_mode = m.get('permissionMode')

        if m.get('quota') is not None:
            self.quota = m.get('quota')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('spaceId') is not None:
            self.space_id = m.get('spaceId')

        if m.get('spaceName') is not None:
            self.space_name = m.get('spaceName')

        if m.get('spaceType') is not None:
            self.space_type = m.get('spaceType')

        if m.get('usedQuota') is not None:
            self.used_quota = m.get('usedQuota')

        if m.get('vendorRequestId') is not None:
            self.vendor_request_id = m.get('vendorRequestId')

        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')

        return self

