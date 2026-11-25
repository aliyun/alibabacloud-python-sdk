# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rdsai20250507 import models as main_models
from darabonba.model import DaraModel

class GetContextDatabaseUsageResponseBody(DaraModel):
    def __init__(
        self,
        dimension: str = None,
        end_time: str = None,
        items: List[main_models.GetContextDatabaseUsageResponseBodyItems] = None,
        request_id: str = None,
        start_time: str = None,
        workspace_id: str = None,
    ):
        # The query dimension. Valid values:
        # - `Workspace`: A single workspace.
        # - `Account`: All workspaces under the caller account.
        self.dimension = dimension
        # The end time of the query range passed in the request, exclusive.
        self.end_time = end_time
        # The usage list. It returns all seven metering items in a fixed order. If an item has no data within the query range, its usage is 0.
        self.items = items
        # The ID of the API request. You can use the ID to troubleshoot issues.
        self.request_id = request_id
        # The start time of the query range passed in the request, inclusive.
        self.start_time = start_time
        # The ID of the queried workspace. This field has a value only when `Dimension` is set to `Workspace`. It is empty for the account dimension.
        self.workspace_id = workspace_id

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dimension is not None:
            result['Dimension'] = self.dimension

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.GetContextDatabaseUsageResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class GetContextDatabaseUsageResponseBodyItems(DaraModel):
    def __init__(
        self,
        item: str = None,
        quantity: int = None,
        unit: str = None,
    ):
        # The metering item.
        self.item = item
        # The usage of the item within the query range. The unit is specified by `Unit`. The number of calls, tokens, and context evolutions are accumulated over the range. Storage is calculated by averaging the occupancy snapshots of each workspace within the range and rounding to the nearest integer byte. For the account dimension, the average values of all workspaces are summed.
        self.quantity = quantity
        # The metering unit. Valid values:
        # - `Count`: The number of calls.
        # - `Token`: The number of tokens.
        # - `MicroCredit`: One millionth of a credit.
        # - `Byte`: Bytes.
        self.unit = unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.item is not None:
            result['Item'] = self.item

        if self.quantity is not None:
            result['Quantity'] = self.quantity

        if self.unit is not None:
            result['Unit'] = self.unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Item') is not None:
            self.item = m.get('Item')

        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        return self

