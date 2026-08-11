# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteOutboundCallRestrictionRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        restriction_id_list: List[str] = None,
    ):
        # The instance ID.
        self.instance_id = instance_id
        # The list of outbound call restriction IDs.
        self.restriction_id_list = restriction_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.restriction_id_list is not None:
            result['RestrictionIdList'] = self.restriction_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RestrictionIdList') is not None:
            self.restriction_id_list = m.get('RestrictionIdList')

        return self

