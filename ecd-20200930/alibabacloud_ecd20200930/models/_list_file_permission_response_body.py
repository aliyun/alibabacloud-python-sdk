# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class ListFilePermissionResponseBody(DaraModel):
    def __init__(
        self,
        file_permissions: List[main_models.FilePermissionMember] = None,
        request_id: str = None,
    ):
        # The permissions on the shared file.
        self.file_permissions = file_permissions
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.file_permissions:
            for v1 in self.file_permissions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FilePermissions'] = []
        if self.file_permissions is not None:
            for k1 in self.file_permissions:
                result['FilePermissions'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.file_permissions = []
        if m.get('FilePermissions') is not None:
            for k1 in m.get('FilePermissions'):
                temp_model = main_models.FilePermissionMember()
                self.file_permissions.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

