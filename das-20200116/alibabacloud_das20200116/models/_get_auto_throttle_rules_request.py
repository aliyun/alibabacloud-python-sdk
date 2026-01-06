# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAutoThrottleRulesRequest(DaraModel):
    def __init__(
        self,
        console_context: str = None,
        instance_ids: str = None,
    ):
        # The reserved parameter.
        self.console_context = console_context
        # The database instance IDs.
        # 
        # *   Set this parameter to a JSON array that consists of multiple instance IDs. Separate instance IDs with commas (,). Example: `[\\"Instance ID1\\",\\"Instance ID2\\"]`.
        # 
        # *   By default, if you leave this parameter empty, all database instances for which the automatic SQL throttling feature has been enabled within the current Alibaba Cloud account are returned. The following types of database instances are returned:
        # 
        #     *   Database instances for which the automatic SQL throttling feature is currently enabled.
        #     *   Database instances for which the automatic SQL throttling feature was once enabled but is currently disabled. Released database instances are not included.
        self.instance_ids = instance_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.console_context is not None:
            result['ConsoleContext'] = self.console_context

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleContext') is not None:
            self.console_context = m.get('ConsoleContext')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        return self

