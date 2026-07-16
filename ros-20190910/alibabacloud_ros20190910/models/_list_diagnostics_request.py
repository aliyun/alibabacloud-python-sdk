# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDiagnosticsRequest(DaraModel):
    def __init__(
        self,
        diagnostic_key: str = None,
        diagnostic_product: str = None,
        max_results: str = None,
        next_token: str = None,
        status: str = None,
    ):
        # The keyword in the diagnosis.
        self.diagnostic_key = diagnostic_key
        # The product that is diagnosed.
        self.diagnostic_product = diagnostic_product
        # The maximum number of results to be returned in a single call when NextToken is used for the query.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 50.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The diagnosis status.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.diagnostic_key is not None:
            result['DiagnosticKey'] = self.diagnostic_key

        if self.diagnostic_product is not None:
            result['DiagnosticProduct'] = self.diagnostic_product

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiagnosticKey') is not None:
            self.diagnostic_key = m.get('DiagnosticKey')

        if m.get('DiagnosticProduct') is not None:
            self.diagnostic_product = m.get('DiagnosticProduct')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

