# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReportChannelPublishResultRequest(DaraModel):
    def __init__(
        self,
        draft_id: str = None,
        external_id: str = None,
        external_url: str = None,
        fail_reason: str = None,
        success: bool = None,
    ):
        # The channel draft ID.
        # 
        # This parameter is required.
        self.draft_id = draft_id
        # The ID returned by the platform. Specify this parameter when the publish operation is successful.
        self.external_id = external_id
        # The redirect URL of the platform.
        self.external_url = external_url
        # The failure reason. Specify this parameter when the publish operation fails.
        self.fail_reason = fail_reason
        # Specifies whether the publish operation is successful (true/false).
        # 
        # This parameter is required.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.draft_id is not None:
            result['DraftId'] = self.draft_id

        if self.external_id is not None:
            result['ExternalId'] = self.external_id

        if self.external_url is not None:
            result['ExternalUrl'] = self.external_url

        if self.fail_reason is not None:
            result['FailReason'] = self.fail_reason

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DraftId') is not None:
            self.draft_id = m.get('DraftId')

        if m.get('ExternalId') is not None:
            self.external_id = m.get('ExternalId')

        if m.get('ExternalUrl') is not None:
            self.external_url = m.get('ExternalUrl')

        if m.get('FailReason') is not None:
            self.fail_reason = m.get('FailReason')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

