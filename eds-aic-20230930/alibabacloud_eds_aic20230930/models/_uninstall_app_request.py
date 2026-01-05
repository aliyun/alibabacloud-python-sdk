# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UninstallAppRequest(DaraModel):
    def __init__(
        self,
        app_id_list: List[str] = None,
        instance_group_id_list: List[str] = None,
        instance_id_list: List[str] = None,
    ):
        # The IDs of the apps.
        self.app_id_list = app_id_list
        # The ID of the instance groups. If you specify this parameter, you cannot specify InstanceIdList.
        self.instance_group_id_list = instance_group_id_list
        # The IDs of the cloud phone instances. If you specify this parameter, you cannot specify InstanceGroupIdList.
        self.instance_id_list = instance_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id_list is not None:
            result['AppIdList'] = self.app_id_list

        if self.instance_group_id_list is not None:
            result['InstanceGroupIdList'] = self.instance_group_id_list

        if self.instance_id_list is not None:
            result['InstanceIdList'] = self.instance_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppIdList') is not None:
            self.app_id_list = m.get('AppIdList')

        if m.get('InstanceGroupIdList') is not None:
            self.instance_group_id_list = m.get('InstanceGroupIdList')

        if m.get('InstanceIdList') is not None:
            self.instance_id_list = m.get('InstanceIdList')

        return self

