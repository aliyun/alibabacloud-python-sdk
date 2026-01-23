# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetRepoBuildRecordRequest(DaraModel):
    def __init__(
        self,
        build_record_id: str = None,
        instance_id: str = None,
    ):
        # The ID of the image building record.
        # 
        # This parameter is required.
        self.build_record_id = build_record_id
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.build_record_id is not None:
            result['BuildRecordId'] = self.build_record_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuildRecordId') is not None:
            self.build_record_id = m.get('BuildRecordId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

