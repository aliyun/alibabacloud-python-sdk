# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateControlPlaneLogRequest(DaraModel):
    def __init__(
        self,
        aliuid: str = None,
        components: List[str] = None,
        log_project: str = None,
        log_ttl: str = None,
    ):
        # The ID of the Alibaba Cloud account.
        self.aliuid = aliuid
        # The control plane components for which you want to enable log collection.
        self.components = components
        # The name of the Simple Log Service Project that you want to use to store the logs of control plane components.
        # 
        # Default value: k8s-log-$Cluster ID.
        self.log_project = log_project
        # The retention period of the log data stored in the Logstore. Valid values: 1 to 3000. Unit: days.
        # 
        # Default value: 30.
        self.log_ttl = log_ttl

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliuid is not None:
            result['aliuid'] = self.aliuid

        if self.components is not None:
            result['components'] = self.components

        if self.log_project is not None:
            result['log_project'] = self.log_project

        if self.log_ttl is not None:
            result['log_ttl'] = self.log_ttl

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aliuid') is not None:
            self.aliuid = m.get('aliuid')

        if m.get('components') is not None:
            self.components = m.get('components')

        if m.get('log_project') is not None:
            self.log_project = m.get('log_project')

        if m.get('log_ttl') is not None:
            self.log_ttl = m.get('log_ttl')

        return self

