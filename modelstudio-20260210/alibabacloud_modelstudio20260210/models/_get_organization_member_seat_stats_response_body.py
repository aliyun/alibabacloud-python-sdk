# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetOrganizationMemberSeatStatsResponseBody(DaraModel):
    def __init__(
        self,
        admin_role_user_count: int = None,
        member_role_user_count: int = None,
        org_id: str = None,
        owner_role_user_count: int = None,
        seated_member_count: int = None,
        total_member_count: int = None,
        unseated_member_count: int = None,
    ):
        # The number of administrators (ORG_ADMIN role).
        self.admin_role_user_count = admin_role_user_count
        # The number of regular members (ORG_MEMBER role).
        self.member_role_user_count = member_role_user_count
        # The organization ID.
        self.org_id = org_id
        # The number of owner accounts (ORG_OWNER role).
        self.owner_role_user_count = owner_role_user_count
        # The number of members with assigned seats.
        self.seated_member_count = seated_member_count
        # The total number of members.
        self.total_member_count = total_member_count
        # The number of members without assigned seats.
        self.unseated_member_count = unseated_member_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.admin_role_user_count is not None:
            result['AdminRoleUserCount'] = self.admin_role_user_count

        if self.member_role_user_count is not None:
            result['MemberRoleUserCount'] = self.member_role_user_count

        if self.org_id is not None:
            result['OrgId'] = self.org_id

        if self.owner_role_user_count is not None:
            result['OwnerRoleUserCount'] = self.owner_role_user_count

        if self.seated_member_count is not None:
            result['SeatedMemberCount'] = self.seated_member_count

        if self.total_member_count is not None:
            result['TotalMemberCount'] = self.total_member_count

        if self.unseated_member_count is not None:
            result['UnseatedMemberCount'] = self.unseated_member_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdminRoleUserCount') is not None:
            self.admin_role_user_count = m.get('AdminRoleUserCount')

        if m.get('MemberRoleUserCount') is not None:
            self.member_role_user_count = m.get('MemberRoleUserCount')

        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')

        if m.get('OwnerRoleUserCount') is not None:
            self.owner_role_user_count = m.get('OwnerRoleUserCount')

        if m.get('SeatedMemberCount') is not None:
            self.seated_member_count = m.get('SeatedMemberCount')

        if m.get('TotalMemberCount') is not None:
            self.total_member_count = m.get('TotalMemberCount')

        if m.get('UnseatedMemberCount') is not None:
            self.unseated_member_count = m.get('UnseatedMemberCount')

        return self

