# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListMembersRequest(DaraModel):
    def __init__(
        self,
        member_name: str = None,
        page_number: int = None,
        page_size: int = None,
        roles: str = None,
        user_id: str = None,
    ):
        # The member name. Fuzzy match is supported.
        self.member_name = member_name
        # The page number of the workspace list. Pages start from 1. Default value: 1.
        self.page_number = page_number
        # The paging Settings for the number of entries per page in a paged query. Default value: 20.
        self.page_size = page_size
        # Filters members by role. Separate multiple roles with commas (,).
        # Valid values:
        # - PAI.AlgoDeveloper: Algorithm developer.
        # - PAI.AlgoOperator: Algorithm O&M.
        # - PAI.LabelManager: Labeling administrator.
        # - PAI.MaxComputeDeveloper: MaxCompute developer.
        # - PAI.WorkspaceAdmin: Administrator.
        # - PAI.WorkspaceGuest: Guest.
        # - PAI.WorkspaceOwner: Owner.
        self.roles = roles
        # The ID of the user to query.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.member_name is not None:
            result['MemberName'] = self.member_name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.roles is not None:
            result['Roles'] = self.roles

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Roles') is not None:
            self.roles = m.get('Roles')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

