# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCustomCallTaggingRequest(DaraModel):
    def __init__(
        self,
        custom_number_list: str = None,
        instance_id: str = None,
    ):
        # This parameter is required.
        self.custom_number_list = custom_number_list
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_number_list is not None:
            result['CustomNumberList'] = self.custom_number_list

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomNumberList') is not None:
            self.custom_number_list = m.get('CustomNumberList')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

