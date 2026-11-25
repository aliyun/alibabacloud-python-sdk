# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class IdpSyncConfig(DaraModel):
    def __init__(
        self,
        auto_sync_enabled: bool = None,
        idp_department_infos: List[main_models.IdpSyncConfigIdpDepartmentInfos] = None,
        schedule_sync_interval_second: int = None,
        user_sync_enabled: bool = None,
    ):
        self.auto_sync_enabled = auto_sync_enabled
        self.idp_department_infos = idp_department_infos
        self.schedule_sync_interval_second = schedule_sync_interval_second
        self.user_sync_enabled = user_sync_enabled

    def validate(self):
        if self.idp_department_infos:
            for v1 in self.idp_department_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_sync_enabled is not None:
            result['AutoSyncEnabled'] = self.auto_sync_enabled

        result['IdpDepartmentInfos'] = []
        if self.idp_department_infos is not None:
            for k1 in self.idp_department_infos:
                result['IdpDepartmentInfos'].append(k1.to_map() if k1 else None)

        if self.schedule_sync_interval_second is not None:
            result['ScheduleSyncIntervalSecond'] = self.schedule_sync_interval_second

        if self.user_sync_enabled is not None:
            result['UserSyncEnabled'] = self.user_sync_enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoSyncEnabled') is not None:
            self.auto_sync_enabled = m.get('AutoSyncEnabled')

        self.idp_department_infos = []
        if m.get('IdpDepartmentInfos') is not None:
            for k1 in m.get('IdpDepartmentInfos'):
                temp_model = main_models.IdpSyncConfigIdpDepartmentInfos()
                self.idp_department_infos.append(temp_model.from_map(k1))

        if m.get('ScheduleSyncIntervalSecond') is not None:
            self.schedule_sync_interval_second = m.get('ScheduleSyncIntervalSecond')

        if m.get('UserSyncEnabled') is not None:
            self.user_sync_enabled = m.get('UserSyncEnabled')

        return self

class IdpSyncConfigIdpDepartmentInfos(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

