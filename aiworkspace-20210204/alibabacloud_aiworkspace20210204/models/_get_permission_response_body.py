# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiworkspace20210204 import models as main_models
from darabonba.model import DaraModel

class GetPermissionResponseBody(DaraModel):
    def __init__(
        self,
        permission_code: str = None,
        permission_rules: List[main_models.GetPermissionResponseBodyPermissionRules] = None,
        request_id: str = None,
    ):
        # The permission name, which is unique in a region. For more information about permissions, see [Appendix: Roles and permissions](https://help.aliyun.com/document_detail/2840449.html).
        self.permission_code = permission_code
        # The permission rules.
        self.permission_rules = permission_rules
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.permission_rules:
            for v1 in self.permission_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.permission_code is not None:
            result['PermissionCode'] = self.permission_code

        result['PermissionRules'] = []
        if self.permission_rules is not None:
            for k1 in self.permission_rules:
                result['PermissionRules'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PermissionCode') is not None:
            self.permission_code = m.get('PermissionCode')

        self.permission_rules = []
        if m.get('PermissionRules') is not None:
            for k1 in m.get('PermissionRules'):
                temp_model = main_models.GetPermissionResponseBodyPermissionRules()
                self.permission_rules.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetPermissionResponseBodyPermissionRules(DaraModel):
    def __init__(
        self,
        accessibility: str = None,
        entity_access_type: str = None,
    ):
        # The accessibility. Valid values:
        # 
        # *   PUBLIC: All members can access the workspace.
        # *   PRIVATE: Only the creator can access the workspace.
        # *   ANY: All users can access the workspace.
        self.accessibility = accessibility
        # The access type. If you set Accessibility to PUBLIC, all users can access the workspace. This parameter is invalid. If you set Accessibility to PRIVATE, the value of this parameter can be:
        # 
        # *   PRIVATE: Only the creator can access the workspace.
        # *   ANY: All users can access the workspace.
        self.entity_access_type = entity_access_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility

        if self.entity_access_type is not None:
            result['EntityAccessType'] = self.entity_access_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')

        if m.get('EntityAccessType') is not None:
            self.entity_access_type = m.get('EntityAccessType')

        return self

