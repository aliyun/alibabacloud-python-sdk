# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDcvDelegationResponseBody(DaraModel):
    def __init__(
        self,
        delegation_domain: str = None,
        request_id: str = None,
        site_id: int = None,
        site_name: str = None,
    ):
        # The DCV managed domain name.
        self.delegation_domain = delegation_domain
        # Id of the request
        self.request_id = request_id
        # The site ID.
        self.site_id = site_id
        # The site name.
        self.site_name = site_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delegation_domain is not None:
            result['DelegationDomain'] = self.delegation_domain

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.site_name is not None:
            result['SiteName'] = self.site_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DelegationDomain') is not None:
            self.delegation_domain = m.get('DelegationDomain')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('SiteName') is not None:
            self.site_name = m.get('SiteName')

        return self

