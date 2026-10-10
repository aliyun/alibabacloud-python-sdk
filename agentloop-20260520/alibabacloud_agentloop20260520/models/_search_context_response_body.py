# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from darabonba.model import DaraModel

class SearchContextResponseBody(DaraModel):
    def __init__(
        self,
        audit_status: str = None,
        recall_event_id: str = None,
        request_id: str = None,
        results: List[Dict[str, Any]] = None,
    ):
        self.audit_status = audit_status
        self.recall_event_id = recall_event_id
        # The request ID. You can use this ID to locate and troubleshoot issues.
        self.request_id = request_id
        # The list of retrieval results, sorted by similarity in descending order.
        self.results = results

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audit_status is not None:
            result['auditStatus'] = self.audit_status

        if self.recall_event_id is not None:
            result['recallEventId'] = self.recall_event_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.results is not None:
            result['results'] = self.results

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auditStatus') is not None:
            self.audit_status = m.get('auditStatus')

        if m.get('recallEventId') is not None:
            self.recall_event_id = m.get('recallEventId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('results') is not None:
            self.results = m.get('results')

        return self

