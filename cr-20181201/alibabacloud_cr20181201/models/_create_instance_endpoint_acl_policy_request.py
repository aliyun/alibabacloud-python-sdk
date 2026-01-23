# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateInstanceEndpointAclPolicyRequest(DaraModel):
    def __init__(
        self,
        comment: str = None,
        endpoint_type: str = None,
        entry: str = None,
        instance_id: str = None,
        module_name: str = None,
    ):
        # The description.
        self.comment = comment
        # The type of the endpoint. Set the value to Internet.
        # 
        # This parameter is required.
        self.endpoint_type = endpoint_type
        # The CIDR block that is accessible.
        # 
        # This parameter is required.
        self.entry = entry
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the module that you want to access. Valid values:
        # 
        # *   `Registry`: the image repository.
        # *   `Chart`: a Helm chart.
        self.module_name = module_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type

        if self.entry is not None:
            result['Entry'] = self.entry

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.module_name is not None:
            result['ModuleName'] = self.module_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')

        if m.get('Entry') is not None:
            self.entry = m.get('Entry')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')

        return self

