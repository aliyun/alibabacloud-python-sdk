# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sandbox20260820 import models as main_models
from darabonba.model import DaraModel

class ListCustomDomainsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        custom_domains: List[main_models.CustomDomainResp] = None,
        has_more: bool = None,
        max_results: int = None,
        message: str = None,
        next_offset: int = None,
        next_token: str = None,
        request_id: str = None,
        total: int = None,
    ):
        # The response code. The value is 200 if the request is successful.
        self.code = code
        # The custom domain names.
        self.custom_domains = custom_domains
        # Indicates whether a next page is available.
        self.has_more = has_more
        # The maximum number of records to return per page.
        self.max_results = max_results
        # The response message.
        self.message = message
        # The offset for the next page.
        self.next_offset = next_offset
        # The pagination token for the next page. This parameter is empty if no more results are available.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of records.
        self.total = total

    def validate(self):
        if self.custom_domains:
            for v1 in self.custom_domains:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.custom_domains is not None:
            result['customDomains'] = []
            for k1 in self.custom_domains:
                result['customDomains'].append(k1.to_map() if k1 else None)

        if self.has_more is not None:
            result['hasMore'] = self.has_more

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.message is not None:
            result['message'] = self.message

        if self.next_offset is not None:
            result['nextOffset'] = self.next_offset

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('customDomains') is not None:
            self.custom_domains = []
            for k1 in m.get('customDomains'):
                temp_model = main_models.CustomDomainResp()
                self.custom_domains.append(temp_model.from_map(k1))

        if m.get('hasMore') is not None:
            self.has_more = m.get('hasMore')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('nextOffset') is not None:
            self.next_offset = m.get('nextOffset')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

