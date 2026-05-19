# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetMatchedResourcesRequest(DaraModel):
    def __init__(
        self,
        cert_ids: str = None,
        max_results: int = None,
        next_token: str = None,
        resource_scope: str = None,
    ):
        # This parameter is required.
        self.cert_ids = cert_ids
        self.max_results = max_results
        self.next_token = next_token
        self.resource_scope = resource_scope

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_ids is not None:
            result['CertIds'] = self.cert_ids

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.resource_scope is not None:
            result['ResourceScope'] = self.resource_scope

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertIds') is not None:
            self.cert_ids = m.get('CertIds')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ResourceScope') is not None:
            self.resource_scope = m.get('ResourceScope')

        return self

