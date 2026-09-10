# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetCronExecTimeRequest(DaraModel):
    def __init__(
        self,
        cron_rule: str = None,
    ):
        # The Cron expression. Replace spaces with plus signs `+` when passing the expression as a query parameter.
        # 
        # This parameter is required.
        self.cron_rule = cron_rule

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cron_rule is not None:
            result['cronRule'] = self.cron_rule

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cronRule') is not None:
            self.cron_rule = m.get('cronRule')

        return self

