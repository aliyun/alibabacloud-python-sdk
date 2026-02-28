# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListCallSummariesRequest(DaraModel):
    def __init__(
        self,
        contact_id_list: List[str] = None,
        instance_id: str = None,
    ):
        self.contact_id_list = contact_id_list
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_id_list is not None:
            result['ContactIdList'] = self.contact_id_list

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactIdList') is not None:
            self.contact_id_list = m.get('ContactIdList')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

