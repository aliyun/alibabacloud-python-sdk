# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetLoadBalancerRequest(DaraModel):
    def __init__(
        self,
        id: int = None,
        site_id: int = None,
    ):
        # The load balancer ID, which uniquely identifies the load balancer to query. This ID is returned when the load balancer is created. You can also call the [ListLoadBalancers](https://help.aliyun.com/document_detail/2868897.html) operation to obtain all load balancers under a site.
        # 
        # This parameter is required.
        self.id = id
        # The site ID. You can call the [ListSites](~~ListSites~~) operation to obtain the site ID.
        # 
        # This parameter is required.
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        return self

