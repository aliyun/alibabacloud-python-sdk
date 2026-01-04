# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateUploadAuthRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        purpose: str = None,
        type: str = None,
    ):
        # IDaaS EIAM的实例id
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # 文件用途
        self.purpose = purpose
        # 文件类型，目前只支持image,最大1M
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.purpose is not None:
            result['Purpose'] = self.purpose

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Purpose') is not None:
            self.purpose = m.get('Purpose')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

