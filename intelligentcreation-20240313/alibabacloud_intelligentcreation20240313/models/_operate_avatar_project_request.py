# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OperateAvatarProjectRequest(DaraModel):
    def __init__(
        self,
        operate_type: str = None,
        project_id: str = None,
        res_channel_number: int = None,
        res_type: str = None,
    ):
        self.operate_type = operate_type
        self.project_id = project_id
        self.res_channel_number = res_channel_number
        self.res_type = res_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.operate_type is not None:
            result['operateType'] = self.operate_type

        if self.project_id is not None:
            result['projectId'] = self.project_id

        if self.res_channel_number is not None:
            result['resChannelNumber'] = self.res_channel_number

        if self.res_type is not None:
            result['resType'] = self.res_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('operateType') is not None:
            self.operate_type = m.get('operateType')

        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')

        if m.get('resChannelNumber') is not None:
            self.res_channel_number = m.get('resChannelNumber')

        if m.get('resType') is not None:
            self.res_type = m.get('resType')

        return self

