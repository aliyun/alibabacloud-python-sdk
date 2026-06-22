# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDomainCountResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        root_domains_count: int = None,
        sub_domains_count: int = None,
        total_domains_count: int = None,
    ):
        # The ID of the request. Alibaba Cloud generates a unique identifier for each request. You can use the ID to troubleshoot issues.
        self.request_id = request_id
        # The number of root domains in the assets.
        self.root_domains_count = root_domains_count
        # The number of subdomains in the assets.
        self.sub_domains_count = sub_domains_count
        # The total number of domain name assets returned.
        self.total_domains_count = total_domains_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.root_domains_count is not None:
            result['RootDomainsCount'] = self.root_domains_count

        if self.sub_domains_count is not None:
            result['SubDomainsCount'] = self.sub_domains_count

        if self.total_domains_count is not None:
            result['TotalDomainsCount'] = self.total_domains_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RootDomainsCount') is not None:
            self.root_domains_count = m.get('RootDomainsCount')

        if m.get('SubDomainsCount') is not None:
            self.sub_domains_count = m.get('SubDomainsCount')

        if m.get('TotalDomainsCount') is not None:
            self.total_domains_count = m.get('TotalDomainsCount')

        return self

