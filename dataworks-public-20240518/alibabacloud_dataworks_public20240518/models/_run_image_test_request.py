# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RunImageTestRequest(DaraModel):
    def __init__(
        self,
        cu: float = None,
        id: str = None,
        process_id: str = None,
        resource_group_id: str = None,
    ):
        # The test compute unit (CU).
        self.cu = cu
        # The image ID.
        # 
        # This parameter is required.
        self.id = id
        # The image test execution ID, which is used as an idempotence identifier.
        self.process_id = process_id
        # The unique identifier of the general-purpose resource group used to run the test task. Only Serverless resource groups are supported.
        # 
        # This parameter is required.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cu is not None:
            result['Cu'] = self.cu

        if self.id is not None:
            result['Id'] = self.id

        if self.process_id is not None:
            result['ProcessId'] = self.process_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cu') is not None:
            self.cu = m.get('Cu')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ProcessId') is not None:
            self.process_id = m.get('ProcessId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

