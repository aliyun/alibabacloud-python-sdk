# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSummaryInfoResponseBody(DaraModel):
    def __init__(
        self,
        aegis_client_offline_count: int = None,
        aegis_client_online_count: int = None,
        request_id: str = None,
        security_score: int = None,
        success: bool = None,
    ):
        # The number of unprotected assets.
        self.aegis_client_offline_count = aegis_client_offline_count
        # The number of protected assets.
        self.aegis_client_online_count = aegis_client_online_count
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The security score of the assets. Valid values:
        # 
        # *   95 to 100: The assets are secure.
        # *   85 to 94: The assets are exposed to a few security risks. We recommend that you reinforce your security system in a timely manner.
        # *   70 to 84: The assets are exposed to multiple security risks. We recommend that you reinforce your security system in a timely manner.
        # *   69 or lower: The current security system is unable to protect the assets against intrusions. We recommend that you reinforce your security system at the earliest opportunity.
        self.security_score = security_score
        # Indicates whether the request is successful. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aegis_client_offline_count is not None:
            result['AegisClientOfflineCount'] = self.aegis_client_offline_count

        if self.aegis_client_online_count is not None:
            result['AegisClientOnlineCount'] = self.aegis_client_online_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.security_score is not None:
            result['SecurityScore'] = self.security_score

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AegisClientOfflineCount') is not None:
            self.aegis_client_offline_count = m.get('AegisClientOfflineCount')

        if m.get('AegisClientOnlineCount') is not None:
            self.aegis_client_online_count = m.get('AegisClientOnlineCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SecurityScore') is not None:
            self.security_score = m.get('SecurityScore')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

