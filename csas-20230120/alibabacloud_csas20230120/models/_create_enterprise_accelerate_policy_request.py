# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateEnterpriseAcceleratePolicyRequest(DaraModel):
    def __init__(
        self,
        acceleration_type: str = None,
        description: str = None,
        name: str = None,
        priority: str = None,
        show_in_client: int = None,
        upstream_host: str = None,
        upstream_port: int = None,
        upstream_type: str = None,
        user_attribute_group: str = None,
    ):
        self.acceleration_type = acceleration_type
        self.description = description
        self.name = name
        self.priority = priority
        self.show_in_client = show_in_client
        # This parameter is required.
        self.upstream_host = upstream_host
        # This parameter is required.
        self.upstream_port = upstream_port
        # This parameter is required.
        self.upstream_type = upstream_type
        # This parameter is required.
        self.user_attribute_group = user_attribute_group

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acceleration_type is not None:
            result['AccelerationType'] = self.acceleration_type

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.show_in_client is not None:
            result['ShowInClient'] = self.show_in_client

        if self.upstream_host is not None:
            result['UpstreamHost'] = self.upstream_host

        if self.upstream_port is not None:
            result['UpstreamPort'] = self.upstream_port

        if self.upstream_type is not None:
            result['UpstreamType'] = self.upstream_type

        if self.user_attribute_group is not None:
            result['UserAttributeGroup'] = self.user_attribute_group

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccelerationType') is not None:
            self.acceleration_type = m.get('AccelerationType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('ShowInClient') is not None:
            self.show_in_client = m.get('ShowInClient')

        if m.get('UpstreamHost') is not None:
            self.upstream_host = m.get('UpstreamHost')

        if m.get('UpstreamPort') is not None:
            self.upstream_port = m.get('UpstreamPort')

        if m.get('UpstreamType') is not None:
            self.upstream_type = m.get('UpstreamType')

        if m.get('UserAttributeGroup') is not None:
            self.user_attribute_group = m.get('UserAttributeGroup')

        return self

