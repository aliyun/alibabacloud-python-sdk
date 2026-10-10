# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExportDoNotCallNumbersRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        scope: str = None,
        search_pattern: str = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The application scope. Valid values: SYSTEM and INSTANCE. SYSTEM indicates system-level do-not-call, and INSTANCE indicates customer-defined do-not-call. SYSTEM is associated with the Alibaba Cloud account to which the instance belongs, and INSTANCE is associated only with the current instance. This parameter is optional. Default value: INSTANCE.
        self.scope = scope
        # Specifies the keyword to perform a fuzzy match based on the phone number or remark. This parameter is optional. Default value: empty. An empty value indicates that no filtering is applied.
        self.search_pattern = search_pattern

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.search_pattern is not None:
            result['SearchPattern'] = self.search_pattern

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('SearchPattern') is not None:
            self.search_pattern = m.get('SearchPattern')

        return self

