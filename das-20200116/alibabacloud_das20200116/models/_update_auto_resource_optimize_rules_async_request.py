# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAutoResourceOptimizeRulesAsyncRequest(DaraModel):
    def __init__(
        self,
        console_context: str = None,
        instance_ids: str = None,
        result_id: str = None,
        table_fragmentation_ratio: float = None,
        table_space_size: float = None,
    ):
        # The reserved parameter.
        self.console_context = console_context
        # The database instance IDs.
        # 
        # >  Set this parameter to a JSON array that consists of multiple instance IDs. Separate instance IDs with commas (,). Example: `[\\"Instance ID1\\", \\"Instance ID2\\"]`.
        # 
        # This parameter is required.
        self.instance_ids = instance_ids
        # The ID of the asynchronous request.
        # 
        # >  Asynchronous calls do not immediately return the complete results. To obtain the complete results, you must use the value of **ResultId** returned in the response to re-initiate the call until the value of **isFinish** is **true**.**** In this case, you must call this operation at least twice.
        self.result_id = result_id
        # The fragmentation rate that triggers automatic fragment recycling of a single physical table. Valid values: **0.10** to **0.99**.
        # 
        # This parameter is required.
        self.table_fragmentation_ratio = table_fragmentation_ratio
        # The minimum storage usage that triggers automatic fragment recycling of a single physical table. Valid values: **5** to **100**. Unit: GB.
        # 
        # This parameter is required.
        self.table_space_size = table_space_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.console_context is not None:
            result['ConsoleContext'] = self.console_context

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.result_id is not None:
            result['ResultId'] = self.result_id

        if self.table_fragmentation_ratio is not None:
            result['TableFragmentationRatio'] = self.table_fragmentation_ratio

        if self.table_space_size is not None:
            result['TableSpaceSize'] = self.table_space_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleContext') is not None:
            self.console_context = m.get('ConsoleContext')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('ResultId') is not None:
            self.result_id = m.get('ResultId')

        if m.get('TableFragmentationRatio') is not None:
            self.table_fragmentation_ratio = m.get('TableFragmentationRatio')

        if m.get('TableSpaceSize') is not None:
            self.table_space_size = m.get('TableSpaceSize')

        return self

