# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListWafUsageOfRulesRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        phase: str = None,
        site_id: int = None,
    ):
        # The WAF instance ID.
        # 
        # If this parameter is left empty, the API returns an empty result. We recommend that you always specify this parameter.
        self.instance_id = instance_id
        # The phase in which the WAF rule runs. This parameter is required.
        # 
        # Common values: http_custom, http_ratelimit, http_anti_scan, http_bot, http_managed, http_whitelist, and http_threat_intelligence.
        # 
        # > Note: This parameter is required on the server side. If this parameter is not specified, the API returns InvalidParameter (400).
        self.phase = phase
        # The site ID. You can call the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation to obtain the site ID.
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.phase is not None:
            result['Phase'] = self.phase

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Phase') is not None:
            self.phase = m.get('Phase')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        return self

