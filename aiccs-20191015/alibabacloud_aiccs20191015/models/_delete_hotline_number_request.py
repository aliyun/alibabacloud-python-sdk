# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteHotlineNumberRequest(DaraModel):
    def __init__(
        self,
        hotline_number: str = None,
        instance_id: str = None,
    ):
        # This parameter is required.
        self.hotline_number = hotline_number
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hotline_number is not None:
            result['HotlineNumber'] = self.hotline_number

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotlineNumber') is not None:
            self.hotline_number = m.get('HotlineNumber')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

