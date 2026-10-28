# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateFileDeepAnalyzeRequest(DaraModel):
    def __init__(
        self,
        context: str = None,
        event_id: int = None,
        hash: str = None,
        source: str = None,
        source_ip: str = None,
    ):
        # The request context information.
        self.context = context
        # The event ID. If a file-related alert event already exists, you can use this parameter to trigger deep analysis.
        self.event_id = event_id
        # The file hash. If the file already exists in the cloud, you can use this parameter to trigger deep analysis.
        self.hash = hash
        # The request source. The system verifies the purchased edition based on the request source. Valid values:
        # 
        # - **edr**: AgenticEDR.
        # 
        # - **secOpsAgent**: Security operations agent.
        self.source = source
        # The IP address of the access source.
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.context is not None:
            result['Context'] = self.context

        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.hash is not None:
            result['Hash'] = self.hash

        if self.source is not None:
            result['Source'] = self.source

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Context') is not None:
            self.context = m.get('Context')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('Hash') is not None:
            self.hash = m.get('Hash')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        return self

