# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDBResourceManagementModeResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        resource_management_mode: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The resource management mode. Valid values:
        # 
        # *   resourceGroup: resource group management.
        # *   resourceQueue: resource queue management.
        self.resource_management_mode = resource_management_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_management_mode is not None:
            result['ResourceManagementMode'] = self.resource_management_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceManagementMode') is not None:
            self.resource_management_mode = m.get('ResourceManagementMode')

        return self

