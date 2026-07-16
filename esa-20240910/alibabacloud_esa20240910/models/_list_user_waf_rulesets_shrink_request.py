# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListUserWafRulesetsShrinkRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
        phase: str = None,
        query_args_shrink: str = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The page number to return.
        self.page_number = page_number
        # The number of entries to return on each page.
        self.page_size = page_size
        # Specifies the execution phase of the WAF rule.
        # 
        # - `http_whitelist`: whitelist rule
        # 
        # - `http_custom`: custom rule
        # 
        # - `http_managed`: managed rule
        # 
        # - `http_anti_scan`: anti-scan rule
        # 
        # - `http_ratelimit`: rate limit rule
        # 
        # - `ip_access_rule`: IP access rule
        # 
        # - `http_bot`: advanced mode bot
        # 
        # - `http_security_level_rule`: security rule
        self.phase = phase
        # Parameters for filtering and sorting the results.
        self.query_args_shrink = query_args_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.phase is not None:
            result['Phase'] = self.phase

        if self.query_args_shrink is not None:
            result['QueryArgs'] = self.query_args_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Phase') is not None:
            self.phase = m.get('Phase')

        if m.get('QueryArgs') is not None:
            self.query_args_shrink = m.get('QueryArgs')

        return self

