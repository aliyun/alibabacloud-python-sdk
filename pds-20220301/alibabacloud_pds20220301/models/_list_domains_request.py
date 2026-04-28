# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDomainsRequest(DaraModel):
    def __init__(
        self,
        limit: int = None,
        marker: str = None,
        parent_domain_id: str = None,
        service_code: str = None,
    ):
        # The maximum number of results to return. Valid values: 1 to 100. Default value: 50.
        self.limit = limit
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of marker.
        self.marker = marker
        # The ID of the parent domain.
        self.parent_domain_id = parent_domain_id
        self.service_code = service_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.limit is not None:
            result['limit'] = self.limit

        if self.marker is not None:
            result['marker'] = self.marker

        if self.parent_domain_id is not None:
            result['parent_domain_id'] = self.parent_domain_id

        if self.service_code is not None:
            result['service_code'] = self.service_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')

        if m.get('marker') is not None:
            self.marker = m.get('marker')

        if m.get('parent_domain_id') is not None:
            self.parent_domain_id = m.get('parent_domain_id')

        if m.get('service_code') is not None:
            self.service_code = m.get('service_code')

        return self

