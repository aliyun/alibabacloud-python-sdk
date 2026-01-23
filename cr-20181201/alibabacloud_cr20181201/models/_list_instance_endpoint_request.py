# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListInstanceEndpointRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        module_name: str = None,
        summary: bool = None,
    ):
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the module that you want to access. Valid values:
        # 
        # *   `Registry`: image repositories.
        # *   `Chart`: Helm charts.
        self.module_name = module_name
        # Specify whether to return endpoints in simple mode. If yes, no access control information about the endpoint is returned.
        self.summary = summary

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.module_name is not None:
            result['ModuleName'] = self.module_name

        if self.summary is not None:
            result['Summary'] = self.summary

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        return self

