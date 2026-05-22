# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListWafTemplateRulesShrinkRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        phase: str = None,
        query_args_shrink: str = None,
        site_id: int = None,
    ):
        self.instance_id = instance_id
        # WAF operation phase, used to filter template rules for a specific phase.
        self.phase = phase
        # Query parameters, used to filter template rules based on conditions such as rule type.
        self.query_args_shrink = query_args_shrink
        # Site ID, which can be obtained by calling the [ListSites](https://help.aliyun.com/document_detail/2850189.html) API.
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

        if self.query_args_shrink is not None:
            result['QueryArgs'] = self.query_args_shrink

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Phase') is not None:
            self.phase = m.get('Phase')

        if m.get('QueryArgs') is not None:
            self.query_args_shrink = m.get('QueryArgs')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        return self

