# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class ListDriveSpacesResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        spaces: List[main_models.ListDriveSpacesResponseBodySpaces] = None,
        vendor_request_id: str = None,
        vendor_type: str = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.spaces = spaces
        self.vendor_request_id = vendor_request_id
        self.vendor_type = vendor_type

    def validate(self):
        if self.spaces:
            for v1 in self.spaces:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['spaces'] = []
        if self.spaces is not None:
            for k1 in self.spaces:
                result['spaces'].append(k1.to_map() if k1 else None)

        if self.vendor_request_id is not None:
            result['vendorRequestId'] = self.vendor_request_id

        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.spaces = []
        if m.get('spaces') is not None:
            for k1 in m.get('spaces'):
                temp_model = main_models.ListDriveSpacesResponseBodySpaces()
                self.spaces.append(temp_model.from_map(k1))

        if m.get('vendorRequestId') is not None:
            self.vendor_request_id = m.get('vendorRequestId')

        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')

        return self

class ListDriveSpacesResponseBodySpaces(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        modify_time: str = None,
        permission_mode: str = None,
        quota: int = None,
        space_id: str = None,
        space_name: str = None,
        space_type: str = None,
        used_quota: int = None,
    ):
        self.create_time = create_time
        self.modify_time = modify_time
        self.permission_mode = permission_mode
        self.quota = quota
        self.space_id = space_id
        self.space_name = space_name
        self.space_type = space_type
        self.used_quota = used_quota

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.permission_mode is not None:
            result['PermissionMode'] = self.permission_mode

        if self.quota is not None:
            result['Quota'] = self.quota

        if self.space_id is not None:
            result['SpaceId'] = self.space_id

        if self.space_name is not None:
            result['SpaceName'] = self.space_name

        if self.space_type is not None:
            result['SpaceType'] = self.space_type

        if self.used_quota is not None:
            result['UsedQuota'] = self.used_quota

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('PermissionMode') is not None:
            self.permission_mode = m.get('PermissionMode')

        if m.get('Quota') is not None:
            self.quota = m.get('Quota')

        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')

        if m.get('SpaceName') is not None:
            self.space_name = m.get('SpaceName')

        if m.get('SpaceType') is not None:
            self.space_type = m.get('SpaceType')

        if m.get('UsedQuota') is not None:
            self.used_quota = m.get('UsedQuota')

        return self

