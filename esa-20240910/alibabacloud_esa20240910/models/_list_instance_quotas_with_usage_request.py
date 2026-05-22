# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListInstanceQuotasWithUsageRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        quota_names: str = None,
        site_id: int = None,
    ):
        # The plan ID, which can be obtained by calling the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation.
        self.instance_id = instance_id
        # The quota names in the plan. Separate the quota names with commas (,). You can query up to 10 quota names at a time. Valid values:
        # 
        # *   **customHttpCert**: the custom certificates.
        # *   **transition_rule**: the transform rules.
        # *   **waiting_room**: the waiting rooms.
        # *   **https|rule_quota**: the SSL/TLS rules.
        # *   **cache_rules|rule_quota**: the cache rules.
        # *   **configuration_rules|rule_quota**: the configuration rules.
        # *   **redirect_rules|rule_quota**: the redirect rules.
        # *   **compression_rules|rule_quota**: the compression rules.
        # *   **origin_rules|rule_quota**: the origin rules.
        # 
        # This parameter is required.
        self.quota_names = quota_names
        # The website ID, which can be obtained by calling the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation.
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

        if self.quota_names is not None:
            result['QuotaNames'] = self.quota_names

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('QuotaNames') is not None:
            self.quota_names = m.get('QuotaNames')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        return self

