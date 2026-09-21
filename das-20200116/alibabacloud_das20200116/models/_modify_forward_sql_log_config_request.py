# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyForwardSqlLogConfigRequest(DaraModel):
    def __init__(
        self,
        enable: bool = None,
        instance_id: str = None,
        service: str = None,
        source: str = None,
    ):
        # Specifies whether to enable the feature. Valid values:
        # 
        # - **true**: Enable.
        # - **false**: Disable.
        # 
        # This parameter is required.
        self.enable = enable
        # The database instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The service type. Valid values:
        # DAS_OPS: enables TOP KEY delivery.
        # 
        # This parameter is required.
        self.service = service
        # The task source. Valid values:
        # - TOP_KEY: enables TOP KEY delivery.
        # 
        # This parameter is required.
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['Enable'] = self.enable

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.service is not None:
            result['Service'] = self.service

        if self.source is not None:
            result['Source'] = self.source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Service') is not None:
            self.service = m.get('Service')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        return self

