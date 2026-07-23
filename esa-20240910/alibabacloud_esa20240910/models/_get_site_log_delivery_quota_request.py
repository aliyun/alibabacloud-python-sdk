# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSiteLogDeliveryQuotaRequest(DaraModel):
    def __init__(
        self,
        business_type: str = None,
        site_id: int = None,
    ):
        # The type of real-time logs. Valid values:
        # - **dcdn_log_access_l1 (default)**: access logs.
        # - **dcdn_log_er**: edge function logs.
        # - **dcdn_log_waf**: security protection logs.
        # - **dcdn_log_ipa**: Layer 4 acceleration logs.
        # 
        # This parameter is required.
        self.business_type = business_type
        # The site ID. You can call the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation to obtain the site ID.
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
        if self.business_type is not None:
            result['BusinessType'] = self.business_type

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        return self

