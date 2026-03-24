# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateUserAccessTokenRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        email: str = None,
        expire_time: int = None,
        extra_info: str = None,
        foreign_id: str = None,
        nick: str = None,
        telephone: str = None,
    ):
        self.agent_key = agent_key
        self.email = email
        self.expire_time = expire_time
        self.extra_info = extra_info
        # This parameter is required.
        self.foreign_id = foreign_id
        # This parameter is required.
        self.nick = nick
        self.telephone = telephone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.email is not None:
            result['Email'] = self.email

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info

        if self.foreign_id is not None:
            result['ForeignId'] = self.foreign_id

        if self.nick is not None:
            result['Nick'] = self.nick

        if self.telephone is not None:
            result['Telephone'] = self.telephone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')

        if m.get('ForeignId') is not None:
            self.foreign_id = m.get('ForeignId')

        if m.get('Nick') is not None:
            self.nick = m.get('Nick')

        if m.get('Telephone') is not None:
            self.telephone = m.get('Telephone')

        return self

