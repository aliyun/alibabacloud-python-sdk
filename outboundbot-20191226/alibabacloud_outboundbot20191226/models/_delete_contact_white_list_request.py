# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteContactWhiteListRequest(DaraModel):
    def __init__(
        self,
        contact_white_list_id: str = None,
        instance_id: str = None,
        operator: str = None,
    ):
        # This parameter is required.
        self.contact_white_list_id = contact_white_list_id
        # This parameter is required.
        self.instance_id = instance_id
        self.operator = operator

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_white_list_id is not None:
            result['ContactWhiteListId'] = self.contact_white_list_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.operator is not None:
            result['Operator'] = self.operator

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactWhiteListId') is not None:
            self.contact_white_list_id = m.get('ContactWhiteListId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        return self

