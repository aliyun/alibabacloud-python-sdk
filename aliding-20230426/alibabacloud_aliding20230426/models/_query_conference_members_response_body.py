# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class QueryConferenceMembersResponseBody(DaraModel):
    def __init__(
        self,
        member_models: List[main_models.QueryConferenceMembersResponseBodyMemberModels] = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.member_models = member_models
        self.next_token = next_token
        # requestId
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.member_models:
            for v1 in self.member_models:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['memberModels'] = []
        if self.member_models is not None:
            for k1 in self.member_models:
                result['memberModels'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.member_models = []
        if m.get('memberModels') is not None:
            for k1 in m.get('memberModels'):
                temp_model = main_models.QueryConferenceMembersResponseBodyMemberModels()
                self.member_models.append(temp_model.from_map(k1))

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class QueryConferenceMembersResponseBodyMemberModels(DaraModel):
    def __init__(
        self,
        attend_status: int = None,
        co_host: bool = None,
        conference_id: str = None,
        duration: int = None,
        host: bool = None,
        join_time: int = None,
        leave_time: int = None,
        outer_org_member: bool = None,
        pstn_join: bool = None,
        user_id: str = None,
        user_nick: str = None,
    ):
        self.attend_status = attend_status
        self.co_host = co_host
        self.conference_id = conference_id
        self.duration = duration
        self.host = host
        self.join_time = join_time
        self.leave_time = leave_time
        self.outer_org_member = outer_org_member
        self.pstn_join = pstn_join
        self.user_id = user_id
        self.user_nick = user_nick

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attend_status is not None:
            result['AttendStatus'] = self.attend_status

        if self.co_host is not None:
            result['CoHost'] = self.co_host

        if self.conference_id is not None:
            result['ConferenceId'] = self.conference_id

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.host is not None:
            result['Host'] = self.host

        if self.join_time is not None:
            result['JoinTime'] = self.join_time

        if self.leave_time is not None:
            result['LeaveTime'] = self.leave_time

        if self.outer_org_member is not None:
            result['OuterOrgMember'] = self.outer_org_member

        if self.pstn_join is not None:
            result['PstnJoin'] = self.pstn_join

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_nick is not None:
            result['UserNick'] = self.user_nick

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttendStatus') is not None:
            self.attend_status = m.get('AttendStatus')

        if m.get('CoHost') is not None:
            self.co_host = m.get('CoHost')

        if m.get('ConferenceId') is not None:
            self.conference_id = m.get('ConferenceId')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('JoinTime') is not None:
            self.join_time = m.get('JoinTime')

        if m.get('LeaveTime') is not None:
            self.leave_time = m.get('LeaveTime')

        if m.get('OuterOrgMember') is not None:
            self.outer_org_member = m.get('OuterOrgMember')

        if m.get('PstnJoin') is not None:
            self.pstn_join = m.get('PstnJoin')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserNick') is not None:
            self.user_nick = m.get('UserNick')

        return self

