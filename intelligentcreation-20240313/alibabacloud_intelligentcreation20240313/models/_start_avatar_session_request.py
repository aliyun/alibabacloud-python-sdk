# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartAvatarSessionRequest(DaraModel):
    def __init__(
        self,
        channel_token: str = None,
        custom_push_url: str = None,
        custom_user_id: str = None,
        project_id: str = None,
        request_id: str = None,
    ):
        self.channel_token = channel_token
        self.custom_push_url = custom_push_url
        self.custom_user_id = custom_user_id
        self.project_id = project_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_token is not None:
            result['channelToken'] = self.channel_token

        if self.custom_push_url is not None:
            result['customPushUrl'] = self.custom_push_url

        if self.custom_user_id is not None:
            result['customUserId'] = self.custom_user_id

        if self.project_id is not None:
            result['projectId'] = self.project_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channelToken') is not None:
            self.channel_token = m.get('channelToken')

        if m.get('customPushUrl') is not None:
            self.custom_push_url = m.get('customPushUrl')

        if m.get('customUserId') is not None:
            self.custom_user_id = m.get('customUserId')

        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

