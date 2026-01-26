# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAgentDownloadUrlResponseBody(DaraModel):
    def __init__(
        self,
        arms_agent_download_url: str = None,
        request_id: str = None,
    ):
        # The download URL of the ARMS agent.
        self.arms_agent_download_url = arms_agent_download_url
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arms_agent_download_url is not None:
            result['ArmsAgentDownloadUrl'] = self.arms_agent_download_url

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArmsAgentDownloadUrl') is not None:
            self.arms_agent_download_url = m.get('ArmsAgentDownloadUrl')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

