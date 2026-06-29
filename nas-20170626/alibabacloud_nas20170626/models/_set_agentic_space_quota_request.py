# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetAgenticSpaceQuotaRequest(DaraModel):
    def __init__(
        self,
        agentic_space_id: str = None,
        client_token: str = None,
        dry_run: bool = None,
        file_count_limit: int = None,
        file_system_id: str = None,
        size_limit: int = None,
    ):
        # This parameter is required.
        self.agentic_space_id = agentic_space_id
        self.client_token = client_token
        self.dry_run = dry_run
        self.file_count_limit = file_count_limit
        # This parameter is required.
        self.file_system_id = file_system_id
        self.size_limit = size_limit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agentic_space_id is not None:
            result['AgenticSpaceId'] = self.agentic_space_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.file_count_limit is not None:
            result['FileCountLimit'] = self.file_count_limit

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.size_limit is not None:
            result['SizeLimit'] = self.size_limit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgenticSpaceId') is not None:
            self.agentic_space_id = m.get('AgenticSpaceId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('FileCountLimit') is not None:
            self.file_count_limit = m.get('FileCountLimit')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('SizeLimit') is not None:
            self.size_limit = m.get('SizeLimit')

        return self

