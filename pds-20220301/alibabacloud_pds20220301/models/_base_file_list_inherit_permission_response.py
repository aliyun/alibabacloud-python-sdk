# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class BaseFileListInheritPermissionResponse(DaraModel):
    def __init__(
        self,
        file_id: str = None,
        member: main_models.FilePermissionMember = None,
    ):
        self.file_id = file_id
        self.member = member

    def validate(self):
        if self.member:
            self.member.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_id is not None:
            result['file_id'] = self.file_id

        if self.member is not None:
            result['member'] = self.member.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')

        if m.get('member') is not None:
            temp_model = main_models.FilePermissionMember()
            self.member = temp_model.from_map(m.get('member'))

        return self

