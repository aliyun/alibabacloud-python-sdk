# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from darabonba.model import DaraModel

class SearchContextResponseBody(DaraModel):
    def __init__(
        self,
        audit_status: str = None,
        call_id: str = None,
        diagnostics: Dict[str, Any] = None,
        mode: str = None,
        recall_event_id: str = None,
        relevance: List[Dict[str, Any]] = None,
        request_id: str = None,
        results: List[Dict[str, Any]] = None,
        rewritten_queries: List[str] = None,
        status: str = None,
        strategy_version: str = None,
    ):
        # The audit write status. Valid values: ok and degraded.
        self.audit_status = audit_status
        # The call ID for the multi-strategy recall of the experience store.
        self.call_id = call_id
        # The diagnostics information for the current experience recall, including duration, model call volume, and filtering. The actual diagnostics items are determined by the running mode.
        self.diagnostics = diagnostics
        # The actual experience recall mode used for the current request. Valid values: direct, agentic, and hybrid.
        self.mode = mode
        # The ID of the recall event. You can use this ID to call the GetContextStoreRecall operation to view audit details.
        self.recall_event_id = recall_event_id
        # The list of relevance judgment results for candidate experiences.
        self.relevance = relevance
        # The ID of the request. You can use this ID to locate the request for troubleshooting.
        self.request_id = request_id
        # The list of retrieval results, sorted by similarity in descending order.
        self.results = results
        # The list of rewritten queries generated based on the original retrieval query. The original query is not included.
        self.rewritten_queries = rewritten_queries
        # The processing status of the current experience recall call. Valid values: success, degraded, failed, and error.
        self.status = status
        # The strategy implementation version used for the current experience recall. This is used for auditing and result tracing.
        self.strategy_version = strategy_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audit_status is not None:
            result['auditStatus'] = self.audit_status

        if self.call_id is not None:
            result['callId'] = self.call_id

        if self.diagnostics is not None:
            result['diagnostics'] = self.diagnostics

        if self.mode is not None:
            result['mode'] = self.mode

        if self.recall_event_id is not None:
            result['recallEventId'] = self.recall_event_id

        if self.relevance is not None:
            result['relevance'] = self.relevance

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.results is not None:
            result['results'] = self.results

        if self.rewritten_queries is not None:
            result['rewrittenQueries'] = self.rewritten_queries

        if self.status is not None:
            result['status'] = self.status

        if self.strategy_version is not None:
            result['strategyVersion'] = self.strategy_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auditStatus') is not None:
            self.audit_status = m.get('auditStatus')

        if m.get('callId') is not None:
            self.call_id = m.get('callId')

        if m.get('diagnostics') is not None:
            self.diagnostics = m.get('diagnostics')

        if m.get('mode') is not None:
            self.mode = m.get('mode')

        if m.get('recallEventId') is not None:
            self.recall_event_id = m.get('recallEventId')

        if m.get('relevance') is not None:
            self.relevance = m.get('relevance')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('results') is not None:
            self.results = m.get('results')

        if m.get('rewrittenQueries') is not None:
            self.rewritten_queries = m.get('rewrittenQueries')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('strategyVersion') is not None:
            self.strategy_version = m.get('strategyVersion')

        return self

