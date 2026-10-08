# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetServiceListPageRequest(DaraModel):
    def __init__(
        self,
        namespace: str = None,
        origin: str = None,
        page: int = None,
        region: str = None,
        search_type: str = None,
        search_value: str = None,
        service_type: str = None,
        side: str = None,
        size: int = None,
    ):
        # The namespace.
        self.namespace = namespace
        # The source of the data. Valid values:
        # 
        # *   `agent`: Use this value if you use the service query feature of the latest version to pass the query result.
        # *   `registry`: Use this value if you use the service query feature of the earlier version to pass the query result.
        self.origin = origin
        # The number of the page to return. Pages start from Page 0.
        self.page = page
        # The ID of the region.
        self.region = region
        # The type of the service. Valid values:
        # 
        # *   `app`: searches by application.
        # *   `service`: searches by service.
        # *   `providerIp`: searches by IP address.
        self.search_type = search_type
        # The keyword used for the search.
        # 
        # *   Set this parameter to the ID of the application if you set the searchType parameter to app.``
        # *   Set this parameter to the name of the service if you set the serachType parameter to service.``
        # *   Set this parameter to the IP address of the application if you set the searchType parameter to providerIp.
        self.search_value = search_value
        # The type of the service. Valid values:
        # 
        # *   `dubbo`
        # *   `springCloud`
        # *   `hsf`
        # *   `istio`
        self.service_type = service_type
        # Specifies the provider side or the consumer side. Valid values:
        # 
        # *   provider
        # *   consumer
        self.side = side
        # The number of entries to return on each page.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.namespace is not None:
            result['namespace'] = self.namespace

        if self.origin is not None:
            result['origin'] = self.origin

        if self.page is not None:
            result['page'] = self.page

        if self.region is not None:
            result['region'] = self.region

        if self.search_type is not None:
            result['searchType'] = self.search_type

        if self.search_value is not None:
            result['searchValue'] = self.search_value

        if self.service_type is not None:
            result['serviceType'] = self.service_type

        if self.side is not None:
            result['side'] = self.side

        if self.size is not None:
            result['size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        if m.get('origin') is not None:
            self.origin = m.get('origin')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('searchType') is not None:
            self.search_type = m.get('searchType')

        if m.get('searchValue') is not None:
            self.search_value = m.get('searchValue')

        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')

        if m.get('side') is not None:
            self.side = m.get('side')

        if m.get('size') is not None:
            self.size = m.get('size')

        return self

