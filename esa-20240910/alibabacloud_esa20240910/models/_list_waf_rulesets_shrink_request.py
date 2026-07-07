# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListWafRulesetsShrinkRequest(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        phase: str = None,
        query_args_shrink: str = None,
        site_id: int = None,
        site_version: int = None,
    ):
        # The page number. Specifies the current page number for paging queries.
        self.page_number = page_number
        # The page size. Specifies the number of records per page for paging queries.
        self.page_size = page_size
        # The WAF rule execution phase. Valid values:
        # - http_whitelist: whitelist rules
        # - http_custom: custom rules
        # - http_managed: managed rules
        # - http_anti_scan: scan protection rules
        # - http_ratelimit: frequency control rules
        # - ip_access_rule: IP access rules
        # - http_bot: advanced mode bots
        # - http_security_level_rule: security rules
        self.phase = phase
        # The query parameters, passed in JSON format, including various filter conditions.
        self.query_args_shrink = query_args_shrink
        # The site ID. You can call the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation to obtain the site ID.
        self.site_id = site_id
        # The version number of the site configuration. For sites with configuration version management enabled, you can use this parameter to specify the site version for which the configuration takes effect. Default value: 0.
        self.site_version = site_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.phase is not None:
            result['Phase'] = self.phase

        if self.query_args_shrink is not None:
            result['QueryArgs'] = self.query_args_shrink

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.site_version is not None:
            result['SiteVersion'] = self.site_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Phase') is not None:
            self.phase = m.get('Phase')

        if m.get('QueryArgs') is not None:
            self.query_args_shrink = m.get('QueryArgs')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')

        return self

