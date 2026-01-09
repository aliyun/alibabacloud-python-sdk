# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateOuterAccountRequest(DaraModel):
    def __init__(
        self,
        avatar: str = None,
        ext: str = None,
        outer_account_id: str = None,
        outer_account_name: str = None,
        outer_account_type: str = None,
        outer_department_id: str = None,
        outer_department_type: str = None,
        outer_group_ids: str = None,
        outer_group_type: str = None,
        real_name: str = None,
    ):
        self.avatar = avatar
        self.ext = ext
        # This parameter is required.
        self.outer_account_id = outer_account_id
        self.outer_account_name = outer_account_name
        # This parameter is required.
        self.outer_account_type = outer_account_type
        self.outer_department_id = outer_department_id
        self.outer_department_type = outer_department_type
        self.outer_group_ids = outer_group_ids
        self.outer_group_type = outer_group_type
        self.real_name = real_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avatar is not None:
            result['Avatar'] = self.avatar

        if self.ext is not None:
            result['Ext'] = self.ext

        if self.outer_account_id is not None:
            result['OuterAccountId'] = self.outer_account_id

        if self.outer_account_name is not None:
            result['OuterAccountName'] = self.outer_account_name

        if self.outer_account_type is not None:
            result['OuterAccountType'] = self.outer_account_type

        if self.outer_department_id is not None:
            result['OuterDepartmentId'] = self.outer_department_id

        if self.outer_department_type is not None:
            result['OuterDepartmentType'] = self.outer_department_type

        if self.outer_group_ids is not None:
            result['OuterGroupIds'] = self.outer_group_ids

        if self.outer_group_type is not None:
            result['OuterGroupType'] = self.outer_group_type

        if self.real_name is not None:
            result['RealName'] = self.real_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Avatar') is not None:
            self.avatar = m.get('Avatar')

        if m.get('Ext') is not None:
            self.ext = m.get('Ext')

        if m.get('OuterAccountId') is not None:
            self.outer_account_id = m.get('OuterAccountId')

        if m.get('OuterAccountName') is not None:
            self.outer_account_name = m.get('OuterAccountName')

        if m.get('OuterAccountType') is not None:
            self.outer_account_type = m.get('OuterAccountType')

        if m.get('OuterDepartmentId') is not None:
            self.outer_department_id = m.get('OuterDepartmentId')

        if m.get('OuterDepartmentType') is not None:
            self.outer_department_type = m.get('OuterDepartmentType')

        if m.get('OuterGroupIds') is not None:
            self.outer_group_ids = m.get('OuterGroupIds')

        if m.get('OuterGroupType') is not None:
            self.outer_group_type = m.get('OuterGroupType')

        if m.get('RealName') is not None:
            self.real_name = m.get('RealName')

        return self

