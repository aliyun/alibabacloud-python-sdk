# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAgentIMChannelsRequest(DaraModel):
    def __init__(
        self,
        channel_type: str = None,
        max_results: int = None,
        next_token: str = None,
        status: str = None,
    ):
        # The IM channel type. Valid values:
        # - DINGTALK: DingTalk.
        # - FEISHU: Lark.
        # - WECOM: WeCom.
        self.channel_type = channel_type
        # The maximum number of entries to return per page. Default value: 20. Valid values: 1 to 100.
        self.max_results = max_results
        # The pagination token. You do not need to specify this parameter for the first request. For subsequent requests, use the nextToken value returned in the previous response.
        self.next_token = next_token
        # The IM channel status. Valid values:
        # - CREATING: being created.
        # - READY: ready.
        # - UPDATING: being updated.
        # - FAILED: failed.
        # - DELETING: being deleted.
        # - DELETE_FAILED: deletion failed.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_type is not None:
            result['channelType'] = self.channel_type

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channelType') is not None:
            self.channel_type = m.get('channelType')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

