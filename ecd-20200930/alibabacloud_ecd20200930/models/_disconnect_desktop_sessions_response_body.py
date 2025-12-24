# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DisconnectDesktopSessionsResponseBody(DaraModel):
    def __init__(
        self,
        invalid_sessions: List[main_models.DisconnectDesktopSessionsResponseBodyInvalidSessions] = None,
        request_id: str = None,
    ):
        # The list of invalid sessions.
        self.invalid_sessions = invalid_sessions
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.invalid_sessions:
            for v1 in self.invalid_sessions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InvalidSessions'] = []
        if self.invalid_sessions is not None:
            for k1 in self.invalid_sessions:
                result['InvalidSessions'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.invalid_sessions = []
        if m.get('InvalidSessions') is not None:
            for k1 in m.get('InvalidSessions'):
                temp_model = main_models.DisconnectDesktopSessionsResponseBodyInvalidSessions()
                self.invalid_sessions.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DisconnectDesktopSessionsResponseBodyInvalidSessions(DaraModel):
    def __init__(
        self,
        desktop_id: str = None,
        end_user_id: str = None,
    ):
        # The cloud desktop ID.
        self.desktop_id = desktop_id
        # The end user ID.
        self.end_user_id = end_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        return self

