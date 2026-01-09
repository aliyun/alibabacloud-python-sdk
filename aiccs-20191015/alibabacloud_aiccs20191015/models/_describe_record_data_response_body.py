# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRecordDataResponseBody(DaraModel):
    def __init__(
        self,
        acid: str = None,
        agent_id: str = None,
        code: str = None,
        message: str = None,
        oss_link: str = None,
        request_id: str = None,
    ):
        self.acid = acid
        self.agent_id = agent_id
        self.code = code
        self.message = message
        self.oss_link = oss_link
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acid is not None:
            result['Acid'] = self.acid

        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.oss_link is not None:
            result['OssLink'] = self.oss_link

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Acid') is not None:
            self.acid = m.get('Acid')

        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('OssLink') is not None:
            self.oss_link = m.get('OssLink')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

