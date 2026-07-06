# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteInstanceEndpointAclPolicyShrinkRequest(DaraModel):
    def __init__(
        self,
        endpoint_type: str = None,
        entries_shrink: str = None,
        entry: str = None,
        instance_id: str = None,
        module_name: str = None,
    ):
        # The endpoint type. Only Internet is supported.
        # 
        # This parameter is required.
        self.endpoint_type = endpoint_type
        self.entries_shrink = entries_shrink
        # The IP CIDR block.
        self.entry = entry
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The module for which the access policy is set. Valid values:
        # 
        # - `Registry`: access to the image repository
        # 
        # - `Chart`: access to Helm Chart
        self.module_name = module_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type

        if self.entries_shrink is not None:
            result['Entries'] = self.entries_shrink

        if self.entry is not None:
            result['Entry'] = self.entry

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.module_name is not None:
            result['ModuleName'] = self.module_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')

        if m.get('Entries') is not None:
            self.entries_shrink = m.get('Entries')

        if m.get('Entry') is not None:
            self.entry = m.get('Entry')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')

        return self

