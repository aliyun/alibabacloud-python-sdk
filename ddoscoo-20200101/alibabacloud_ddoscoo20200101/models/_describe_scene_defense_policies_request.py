# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSceneDefensePoliciesRequest(DaraModel):
    def __init__(
        self,
        resource_group_id: str = None,
        status: str = None,
        template: str = None,
    ):
        # The ID of the resource group to which the instance belongs in Resource Management.
        # 
        # If you do not configure this parameter, the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id
        # The status of the policy. Valid values:
        # 
        # *   **0**: disabled
        # *   **1**: pending enabling
        # *   **2**: enabled
        # *   **3**: expired
        self.status = status
        # The type of the template that is used to create the policy. Valid values:
        # 
        # *   **promotion**: the Important Activity template
        # *   **bypass**: the Forward All template
        self.template = template

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.status is not None:
            result['Status'] = self.status

        if self.template is not None:
            result['Template'] = self.template

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        return self

