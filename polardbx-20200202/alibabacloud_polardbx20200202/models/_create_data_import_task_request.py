# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDataImportTaskRequest(DaraModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        dst_db: str = None,
        dst_password: str = None,
        dst_res_id: str = None,
        dst_user_name: str = None,
        region_id: str = None,
        slink_task_id: str = None,
        src_db: str = None,
        src_password: str = None,
        src_res_id: str = None,
        src_user_name: str = None,
    ):
        self.dbinstance_name = dbinstance_name
        self.dst_db = dst_db
        self.dst_password = dst_password
        self.dst_res_id = dst_res_id
        self.dst_user_name = dst_user_name
        # This parameter is required.
        self.region_id = region_id
        # This parameter is required.
        self.slink_task_id = slink_task_id
        self.src_db = src_db
        self.src_password = src_password
        self.src_res_id = src_res_id
        self.src_user_name = src_user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.dst_db is not None:
            result['DstDb'] = self.dst_db

        if self.dst_password is not None:
            result['DstPassword'] = self.dst_password

        if self.dst_res_id is not None:
            result['DstResId'] = self.dst_res_id

        if self.dst_user_name is not None:
            result['DstUserName'] = self.dst_user_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.slink_task_id is not None:
            result['SlinkTaskId'] = self.slink_task_id

        if self.src_db is not None:
            result['SrcDb'] = self.src_db

        if self.src_password is not None:
            result['SrcPassword'] = self.src_password

        if self.src_res_id is not None:
            result['SrcResId'] = self.src_res_id

        if self.src_user_name is not None:
            result['SrcUserName'] = self.src_user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('DstDb') is not None:
            self.dst_db = m.get('DstDb')

        if m.get('DstPassword') is not None:
            self.dst_password = m.get('DstPassword')

        if m.get('DstResId') is not None:
            self.dst_res_id = m.get('DstResId')

        if m.get('DstUserName') is not None:
            self.dst_user_name = m.get('DstUserName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SlinkTaskId') is not None:
            self.slink_task_id = m.get('SlinkTaskId')

        if m.get('SrcDb') is not None:
            self.src_db = m.get('SrcDb')

        if m.get('SrcPassword') is not None:
            self.src_password = m.get('SrcPassword')

        if m.get('SrcResId') is not None:
            self.src_res_id = m.get('SrcResId')

        if m.get('SrcUserName') is not None:
            self.src_user_name = m.get('SrcUserName')

        return self

