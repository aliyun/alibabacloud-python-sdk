# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AuthorizeFileUploadRequest(DaraModel):
    def __init__(
        self,
        agent_name: str = None,
        file_format: str = None,
        region_id: str = None,
    ):
        # The Agent or client source that initiates the call, such as codex, cursor, or openapi. Maximum length: 32 characters. Used only for statistics and does not participate in authentication, throttling, quota, or billing.
        self.agent_name = agent_name
        # The format of the file to be uploaded.
        self.file_format = file_format
        # The region ID, such as cn-beijing.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_name is not None:
            result['AgentName'] = self.agent_name

        if self.file_format is not None:
            result['FileFormat'] = self.file_format

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')

        if m.get('FileFormat') is not None:
            self.file_format = m.get('FileFormat')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

