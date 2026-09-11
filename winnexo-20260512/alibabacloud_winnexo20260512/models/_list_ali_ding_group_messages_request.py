# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAliDingGroupMessagesRequest(DaraModel):
    def __init__(
        self,
        chat_id: str = None,
        direction: str = None,
        page_size: int = None,
        tenant_id: str = None,
        time: str = None,
    ):
        # The session ID, typically used for JSSDK.
        # 
        # This parameter is required.
        self.chat_id = chat_id
        # The traffic direction. Valid values:
        # - OutBound: outbound.
        # - InBound: inbound.
        # - Both: bidirectional.
        self.direction = direction
        # The number of entries per page.
        self.page_size = page_size
        # The tenant ID. This is a common parameter. Pass it explicitly through `--tenant-id` in winnexo-cli.
        self.tenant_id = tenant_id
        # The relationship information.
        # 
        # This parameter is required.
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chat_id is not None:
            result['chatId'] = self.chat_id

        if self.direction is not None:
            result['direction'] = self.direction

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.time is not None:
            result['time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chatId') is not None:
            self.chat_id = m.get('chatId')

        if m.get('direction') is not None:
            self.direction = m.get('direction')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('time') is not None:
            self.time = m.get('time')

        return self

