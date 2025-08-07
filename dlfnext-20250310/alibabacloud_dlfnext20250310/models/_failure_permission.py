# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations
from darabonba.model import DaraModel 
from alibabacloud_dlfnext20250310 import models as main_models 


class FailurePermission(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        permission: main_models.Permission = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.permission = permission

    def validate(self):
        if self.permission:
            self.permission.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        if self.permission is not None:
            result['permission'] = self.permission.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('permission') is not None:
            temp_model = main_models.Permission()
            self.permission = temp_model.from_map(m.get('permission'))

        return self

