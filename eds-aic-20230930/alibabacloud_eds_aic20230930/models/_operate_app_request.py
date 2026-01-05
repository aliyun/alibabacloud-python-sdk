# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class OperateAppRequest(DaraModel):
    def __init__(
        self,
        app_id: int = None,
        instance_id_list: List[str] = None,
        operate_type: str = None,
    ):
        # The ID of the app.
        self.app_id = app_id
        # The IDs of the cloud phone instances.
        self.instance_id_list = instance_id_list
        # The type of the operation.
        # 
        # Valid values:
        # 
        # *   stop: closes the app.
        # *   restart: reopens the app.
        # *   start: open the app.
        self.operate_type = operate_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.instance_id_list is not None:
            result['InstanceIdList'] = self.instance_id_list

        if self.operate_type is not None:
            result['OperateType'] = self.operate_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('InstanceIdList') is not None:
            self.instance_id_list = m.get('InstanceIdList')

        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')

        return self

