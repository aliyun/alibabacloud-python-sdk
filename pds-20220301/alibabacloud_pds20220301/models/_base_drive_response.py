# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class BaseDriveResponse(DaraModel):
    def __init__(
        self,
        action_list: List[str] = None,
        category: str = None,
        created_at: str = None,
        creator: str = None,
        delta_enabled: bool = None,
        description: str = None,
        domain_id: str = None,
        drive_id: str = None,
        drive_name: str = None,
        drive_type: str = None,
        encrypt_data_access: bool = None,
        encrypt_mode: str = None,
        is_handover: bool = None,
        owner: str = None,
        owner_type: str = None,
        path_status: str = None,
        permission: Dict[str, main_models.IDPermission] = None,
        relative_path: str = None,
        status: str = None,
        store_id: str = None,
        total_size: int = None,
        updated_at: str = None,
        used_size: int = None,
    ):
        self.action_list = action_list
        self.category = category
        self.created_at = created_at
        self.creator = creator
        self.delta_enabled = delta_enabled
        self.description = description
        self.domain_id = domain_id
        self.drive_id = drive_id
        self.drive_name = drive_name
        self.drive_type = drive_type
        self.encrypt_data_access = encrypt_data_access
        self.encrypt_mode = encrypt_mode
        self.is_handover = is_handover
        self.owner = owner
        self.owner_type = owner_type
        self.path_status = path_status
        self.permission = permission
        self.relative_path = relative_path
        self.status = status
        self.store_id = store_id
        self.total_size = total_size
        self.updated_at = updated_at
        self.used_size = used_size

    def validate(self):
        if self.permission:
            for v1 in self.permission.values():
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_list is not None:
            result['action_list'] = self.action_list

        if self.category is not None:
            result['category'] = self.category

        if self.created_at is not None:
            result['created_at'] = self.created_at

        if self.creator is not None:
            result['creator'] = self.creator

        if self.delta_enabled is not None:
            result['delta_enabled'] = self.delta_enabled

        if self.description is not None:
            result['description'] = self.description

        if self.domain_id is not None:
            result['domain_id'] = self.domain_id

        if self.drive_id is not None:
            result['drive_id'] = self.drive_id

        if self.drive_name is not None:
            result['drive_name'] = self.drive_name

        if self.drive_type is not None:
            result['drive_type'] = self.drive_type

        if self.encrypt_data_access is not None:
            result['encrypt_data_access'] = self.encrypt_data_access

        if self.encrypt_mode is not None:
            result['encrypt_mode'] = self.encrypt_mode

        if self.is_handover is not None:
            result['is_handover'] = self.is_handover

        if self.owner is not None:
            result['owner'] = self.owner

        if self.owner_type is not None:
            result['owner_type'] = self.owner_type

        if self.path_status is not None:
            result['path_status'] = self.path_status

        result['permission'] = {}
        if self.permission is not None:
            for k1, v1 in self.permission.items():
                result['permission'][k1] = v1.to_map() if v1 else None

        if self.relative_path is not None:
            result['relative_path'] = self.relative_path

        if self.status is not None:
            result['status'] = self.status

        if self.store_id is not None:
            result['store_id'] = self.store_id

        if self.total_size is not None:
            result['total_size'] = self.total_size

        if self.updated_at is not None:
            result['updated_at'] = self.updated_at

        if self.used_size is not None:
            result['used_size'] = self.used_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action_list') is not None:
            self.action_list = m.get('action_list')

        if m.get('category') is not None:
            self.category = m.get('category')

        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')

        if m.get('creator') is not None:
            self.creator = m.get('creator')

        if m.get('delta_enabled') is not None:
            self.delta_enabled = m.get('delta_enabled')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')

        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')

        if m.get('drive_name') is not None:
            self.drive_name = m.get('drive_name')

        if m.get('drive_type') is not None:
            self.drive_type = m.get('drive_type')

        if m.get('encrypt_data_access') is not None:
            self.encrypt_data_access = m.get('encrypt_data_access')

        if m.get('encrypt_mode') is not None:
            self.encrypt_mode = m.get('encrypt_mode')

        if m.get('is_handover') is not None:
            self.is_handover = m.get('is_handover')

        if m.get('owner') is not None:
            self.owner = m.get('owner')

        if m.get('owner_type') is not None:
            self.owner_type = m.get('owner_type')

        if m.get('path_status') is not None:
            self.path_status = m.get('path_status')

        self.permission = {}
        if m.get('permission') is not None:
            for k1, v1 in m.get('permission').items():
                temp_model = main_models.IDPermission()
                self.permission[k1] = temp_model.from_map(v1)

        if m.get('relative_path') is not None:
            self.relative_path = m.get('relative_path')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('store_id') is not None:
            self.store_id = m.get('store_id')

        if m.get('total_size') is not None:
            self.total_size = m.get('total_size')

        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')

        if m.get('used_size') is not None:
            self.used_size = m.get('used_size')

        return self

