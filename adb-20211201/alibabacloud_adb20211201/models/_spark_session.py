# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SparkSession(DaraModel):
    def __init__(
        self,
        active: str = None,
        aliyun_uid: int = None,
        session_id: int = None,
        state: str = None,
    ):
        self.active = active
        self.aliyun_uid = aliyun_uid
        self.session_id = session_id
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active is not None:
            result['Active'] = self.active

        if self.aliyun_uid is not None:
            result['AliyunUid'] = self.aliyun_uid

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')

        if m.get('AliyunUid') is not None:
            self.aliyun_uid = m.get('AliyunUid')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

