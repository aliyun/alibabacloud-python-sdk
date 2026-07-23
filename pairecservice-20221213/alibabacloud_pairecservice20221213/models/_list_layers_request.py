# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListLayersRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        laboratory_id: str = None,
    ):
        # The instance ID. You can obtain this ID by calling the ListInstances API.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The laboratory ID. You can obtain this ID by calling the ListLaboratories API.
        # 
        # This parameter is required.
        self.laboratory_id = laboratory_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.laboratory_id is not None:
            result['LaboratoryId'] = self.laboratory_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LaboratoryId') is not None:
            self.laboratory_id = m.get('LaboratoryId')

        return self

