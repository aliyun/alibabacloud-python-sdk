# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribePortRangeListEntriesResponseBody(DaraModel):
    def __init__(
        self,
        entries: List[main_models.DescribePortRangeListEntriesResponseBodyEntries] = None,
        request_id: str = None,
    ):
        # Port list entries.
        self.entries = entries
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.entries:
            for v1 in self.entries:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Entries'] = []
        if self.entries is not None:
            for k1 in self.entries:
                result['Entries'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.entries = []
        if m.get('Entries') is not None:
            for k1 in m.get('Entries'):
                temp_model = main_models.DescribePortRangeListEntriesResponseBodyEntries()
                self.entries.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribePortRangeListEntriesResponseBodyEntries(DaraModel):
    def __init__(
        self,
        description: str = None,
        port_range: str = None,
    ):
        # The description of the port range.
        self.description = description
        # The port range.
        self.port_range = port_range

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.port_range is not None:
            result['PortRange'] = self.port_range

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('PortRange') is not None:
            self.port_range = m.get('PortRange')

        return self

