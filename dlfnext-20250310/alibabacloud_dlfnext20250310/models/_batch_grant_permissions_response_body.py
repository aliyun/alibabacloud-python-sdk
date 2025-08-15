# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dlfnext20250310 import models as main_models
from darabonba.model import DaraModel

class BatchGrantPermissionsResponseBody(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        failure_permissions: List[main_models.FailurePermission] = None,
        success: bool = None,
    ):
        self.error_message = error_message
        self.failure_permissions = failure_permissions
        self.success = success

    def validate(self):
        if self.failure_permissions:
            for v1 in self.failure_permissions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        result['failurePermissions'] = []
        if self.failure_permissions is not None:
            for k1 in self.failure_permissions:
                result['failurePermissions'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        self.failure_permissions = []
        if m.get('failurePermissions') is not None:
            for k1 in m.get('failurePermissions'):
                temp_model = main_models.FailurePermission()
                self.failure_permissions.append(temp_model.from_map(k1))

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

