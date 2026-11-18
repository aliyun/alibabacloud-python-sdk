# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DisableConversationShareResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        session_id: str = None,
        share_access_type: str = None,
        share_enabled: bool = None,
        share_enabled_at: str = None,
        share_path: str = None,
        share_token: str = None,
        share_url: str = None,
        share_user_group_ids: List[str] = None,
        share_user_ids: List[int] = None,
    ):
        # The result code. A value of SUCCESS indicates success. For failures, the corresponding error type is returned, such as ERR_BAD_REQUEST, ERR_VALIDATION_FAILED, or ERR_INTERNAL_SERVER_ERROR.
        self.code = code
        # The description of the status code.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The ID of the source one-on-one session.
        self.session_id = session_id
        # The share access type.
        self.share_access_type = share_access_type
        # Indicates whether sharing is enabled.
        self.share_enabled = share_enabled
        # The time when sharing was most recently enabled.
        self.share_enabled_at = share_enabled_at
        # The share path.
        self.share_path = share_path
        # The share token. This token is present when sharing is enabled and can be used to access the public share preview API operation.
        self.share_token = share_token
        # The share URL.
        self.share_url = share_url
        # The currently specified user group IDs.
        self.share_user_group_ids = share_user_group_ids
        # The list of most recently specified user IDs.
        self.share_user_ids = share_user_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.share_access_type is not None:
            result['shareAccessType'] = self.share_access_type

        if self.share_enabled is not None:
            result['shareEnabled'] = self.share_enabled

        if self.share_enabled_at is not None:
            result['shareEnabledAt'] = self.share_enabled_at

        if self.share_path is not None:
            result['sharePath'] = self.share_path

        if self.share_token is not None:
            result['shareToken'] = self.share_token

        if self.share_url is not None:
            result['shareUrl'] = self.share_url

        if self.share_user_group_ids is not None:
            result['shareUserGroupIds'] = self.share_user_group_ids

        if self.share_user_ids is not None:
            result['shareUserIds'] = self.share_user_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('shareAccessType') is not None:
            self.share_access_type = m.get('shareAccessType')

        if m.get('shareEnabled') is not None:
            self.share_enabled = m.get('shareEnabled')

        if m.get('shareEnabledAt') is not None:
            self.share_enabled_at = m.get('shareEnabledAt')

        if m.get('sharePath') is not None:
            self.share_path = m.get('sharePath')

        if m.get('shareToken') is not None:
            self.share_token = m.get('shareToken')

        if m.get('shareUrl') is not None:
            self.share_url = m.get('shareUrl')

        if m.get('shareUserGroupIds') is not None:
            self.share_user_group_ids = m.get('shareUserGroupIds')

        if m.get('shareUserIds') is not None:
            self.share_user_ids = m.get('shareUserIds')

        return self

