# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAppPublishStatusRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        deploy_order_id: int = None,
        website_domain: str = None,
    ):
        self.biz_id = biz_id
        self.deploy_order_id = deploy_order_id
        self.website_domain = website_domain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.deploy_order_id is not None:
            result['DeployOrderId'] = self.deploy_order_id

        if self.website_domain is not None:
            result['WebsiteDomain'] = self.website_domain

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('DeployOrderId') is not None:
            self.deploy_order_id = m.get('DeployOrderId')

        if m.get('WebsiteDomain') is not None:
            self.website_domain = m.get('WebsiteDomain')

        return self

