# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class FileAddPermissionRequest(DaraModel):
    def __init__(
        self,
        drive_id: str = None,
        file_id: str = None,
        member_list: List[main_models.FilePermissionMember] = None,
    ):
        # The drive ID.
        # 
        # This parameter is required.
        self.drive_id = drive_id
        # The ID of the folder. If you want to authorize a user or group to access a team drive, set this parameter to root. If you want to authorize a user or group to access an individual drive, you cannot set this parameter to root.
        # 
        # This parameter is required.
        self.file_id = file_id
        # The members that are authorized to access files.
        # 
        # This parameter is required.
        self.member_list = member_list

    def validate(self):
        if self.member_list:
            for v1 in self.member_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id

        if self.file_id is not None:
            result['file_id'] = self.file_id

        result['member_list'] = []
        if self.member_list is not None:
            for k1 in self.member_list:
                result['member_list'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')

        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')

        self.member_list = []
        if m.get('member_list') is not None:
            for k1 in m.get('member_list'):
                temp_model = main_models.FilePermissionMember()
                self.member_list.append(temp_model.from_map(k1))

        return self

