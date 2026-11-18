# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class EnableOutputItemShareResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        output_item_id: str = None,
        request_id: str = None,
        share_access_type: str = None,
        share_enabled: bool = None,
        share_enabled_at: str = None,
        share_path: str = None,
        share_token: str = None,
        share_url: str = None,
        share_user_group_ids: List[str] = None,
        share_user_ids: List[int] = None,
    ):
        # The response code.
        self.code = code
        # The description of the status code.
        self.message = message
        # The ID of the output item.
        self.output_item_id = output_item_id
        # The request ID.
        self.request_id = request_id
        # The current sharing scope. Valid values: PUBLIC and SPECIFIED.
        self.share_access_type = share_access_type
        # Indicates whether sharing is enabled.
        self.share_enabled = share_enabled
        # The time when sharing was last enabled.
        self.share_enabled_at = share_enabled_at
        # The relative path for in-site sharing. This parameter is empty if sharing is disabled.
        self.share_path = share_path
        # The share token. This token is returned when sharing is enabled and can be used to access the public share preview API operation.
        self.share_token = share_token
        # The absolute URL of the current share. This parameter is empty if sharing is disabled.
        self.share_url = share_url
        # The list of currently specified user group IDs.
        self.share_user_group_ids = share_user_group_ids
        # The list of currently specified user IDs.
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

        if self.output_item_id is not None:
            result['outputItemId'] = self.output_item_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

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

        if m.get('outputItemId') is not None:
            self.output_item_id = m.get('outputItemId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

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

