# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class UpdateComputeResourceAuthUserMappingsRequest(DaraModel):
    def __init__(
        self,
        compute_resource_id: int = None,
        project_id: int = None,
        remove_user_ids: List[str] = None,
        upserts: List[main_models.UpdateComputeResourceAuthUserMappingsRequestUpserts] = None,
    ):
        # The compute resource ID.
        # 
        # This parameter is required.
        self.compute_resource_id = compute_resource_id
        # The workspace ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The list of user mappings to remove.
        self.remove_user_ids = remove_user_ids
        # The list of objects to update.
        self.upserts = upserts

    def validate(self):
        if self.upserts:
            for v1 in self.upserts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compute_resource_id is not None:
            result['ComputeResourceId'] = self.compute_resource_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.remove_user_ids is not None:
            result['RemoveUserIds'] = self.remove_user_ids

        result['Upserts'] = []
        if self.upserts is not None:
            for k1 in self.upserts:
                result['Upserts'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComputeResourceId') is not None:
            self.compute_resource_id = m.get('ComputeResourceId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RemoveUserIds') is not None:
            self.remove_user_ids = m.get('RemoveUserIds')

        self.upserts = []
        if m.get('Upserts') is not None:
            for k1 in m.get('Upserts'):
                temp_model = main_models.UpdateComputeResourceAuthUserMappingsRequestUpserts()
                self.upserts.append(temp_model.from_map(k1))

        return self

class UpdateComputeResourceAuthUserMappingsRequestUpserts(DaraModel):
    def __init__(
        self,
        password: str = None,
        user_id: str = None,
        username: str = None,
    ):
        # The password of the target system for the mapping, such as an LDAP password.
        self.password = password
        # The Alibaba Cloud UID.
        self.user_id = user_id
        # The username of the target system for the mapping, such as an LDAP username.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.password is not None:
            result['Password'] = self.password

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

