# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class QueryUserHonorsResponseBody(DaraModel):
    def __init__(
        self,
        honors: List[main_models.QueryUserHonorsResponseBodyHonors] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.honors = honors
        self.next_token = next_token
        # requestId
        self.request_id = request_id

    def validate(self):
        if self.honors:
            for v1 in self.honors:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['honors'] = []
        if self.honors is not None:
            for k1 in self.honors:
                result['honors'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.honors = []
        if m.get('honors') is not None:
            for k1 in m.get('honors'):
                temp_model = main_models.QueryUserHonorsResponseBodyHonors()
                self.honors.append(temp_model.from_map(k1))

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class QueryUserHonorsResponseBodyHonors(DaraModel):
    def __init__(
        self,
        expiration_time: int = None,
        grant_history: List[main_models.QueryUserHonorsResponseBodyHonorsGrantHistory] = None,
        honor_desc: str = None,
        honor_id: str = None,
        honor_name: str = None,
    ):
        self.expiration_time = expiration_time
        self.grant_history = grant_history
        self.honor_desc = honor_desc
        self.honor_id = honor_id
        self.honor_name = honor_name

    def validate(self):
        if self.grant_history:
            for v1 in self.grant_history:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expiration_time is not None:
            result['expirationTime'] = self.expiration_time

        result['grantHistory'] = []
        if self.grant_history is not None:
            for k1 in self.grant_history:
                result['grantHistory'].append(k1.to_map() if k1 else None)

        if self.honor_desc is not None:
            result['honorDesc'] = self.honor_desc

        if self.honor_id is not None:
            result['honorId'] = self.honor_id

        if self.honor_name is not None:
            result['honorName'] = self.honor_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expirationTime') is not None:
            self.expiration_time = m.get('expirationTime')

        self.grant_history = []
        if m.get('grantHistory') is not None:
            for k1 in m.get('grantHistory'):
                temp_model = main_models.QueryUserHonorsResponseBodyHonorsGrantHistory()
                self.grant_history.append(temp_model.from_map(k1))

        if m.get('honorDesc') is not None:
            self.honor_desc = m.get('honorDesc')

        if m.get('honorId') is not None:
            self.honor_id = m.get('honorId')

        if m.get('honorName') is not None:
            self.honor_name = m.get('honorName')

        return self

class QueryUserHonorsResponseBodyHonorsGrantHistory(DaraModel):
    def __init__(
        self,
        grant_time: int = None,
        sender_userid: str = None,
    ):
        self.grant_time = grant_time
        self.sender_userid = sender_userid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.grant_time is not None:
            result['grantTime'] = self.grant_time

        if self.sender_userid is not None:
            result['senderUserid'] = self.sender_userid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('grantTime') is not None:
            self.grant_time = m.get('grantTime')

        if m.get('senderUserid') is not None:
            self.sender_userid = m.get('senderUserid')

        return self

