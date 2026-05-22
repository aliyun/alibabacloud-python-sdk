# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeProjectMessagesRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        page_index: int = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.page_index = page_index

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_index is not None:
            result['PageIndex'] = self.page_index

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')

        return self

