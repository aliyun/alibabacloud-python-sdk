# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class PrivilegeTransferResultEntrie(DaraModel):
    def __init__(
        self,
        children: List[main_models.PrivilegeTransferResultEntrie] = None,
        err_msg: str = None,
        is_leaf: bool = None,
        privilege: str = None,
        privilege_display_name: str = None,
        status: str = None,
        test: str = None,
    ):
        self.children = children
        self.err_msg = err_msg
        self.is_leaf = is_leaf
        self.privilege = privilege
        self.privilege_display_name = privilege_display_name
        self.status = status
        self.test = test

    def validate(self):
        if self.children:
            for v1 in self.children:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Children'] = []
        if self.children is not None:
            for k1 in self.children:
                result['Children'].append(k1.to_map() if k1 else None)

        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg

        if self.is_leaf is not None:
            result['IsLeaf'] = self.is_leaf

        if self.privilege is not None:
            result['Privilege'] = self.privilege

        if self.privilege_display_name is not None:
            result['PrivilegeDisplayName'] = self.privilege_display_name

        if self.status is not None:
            result['Status'] = self.status

        if self.test is not None:
            result['Test'] = self.test

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.children = []
        if m.get('Children') is not None:
            for k1 in m.get('Children'):
                temp_model = main_models.PrivilegeTransferResultEntrie()
                self.children.append(temp_model.from_map(k1))

        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')

        if m.get('IsLeaf') is not None:
            self.is_leaf = m.get('IsLeaf')

        if m.get('Privilege') is not None:
            self.privilege = m.get('Privilege')

        if m.get('PrivilegeDisplayName') is not None:
            self.privilege_display_name = m.get('PrivilegeDisplayName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Test') is not None:
            self.test = m.get('Test')

        return self

