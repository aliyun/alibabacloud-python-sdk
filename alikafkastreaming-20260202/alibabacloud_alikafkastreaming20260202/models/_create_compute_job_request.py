# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateComputeJobRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        cu_limit: float = None,
        cu_reserved: float = None,
        draft_sql: str = None,
        instance_id: str = None,
        job_config: str = None,
        job_name: str = None,
        region_id: str = None,
        remark: str = None,
        upgrade_mode: str = None,
        user_id: str = None,
    ):
        self.client_token = client_token
        self.cu_limit = cu_limit
        self.cu_reserved = cu_reserved
        self.draft_sql = draft_sql
        # This parameter is required.
        self.instance_id = instance_id
        self.job_config = job_config
        # This parameter is required.
        self.job_name = job_name
        # This parameter is required.
        self.region_id = region_id
        self.remark = remark
        self.upgrade_mode = upgrade_mode
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.cu_limit is not None:
            result['CuLimit'] = self.cu_limit

        if self.cu_reserved is not None:
            result['CuReserved'] = self.cu_reserved

        if self.draft_sql is not None:
            result['DraftSql'] = self.draft_sql

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.job_config is not None:
            result['JobConfig'] = self.job_config

        if self.job_name is not None:
            result['JobName'] = self.job_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.upgrade_mode is not None:
            result['UpgradeMode'] = self.upgrade_mode

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CuLimit') is not None:
            self.cu_limit = m.get('CuLimit')

        if m.get('CuReserved') is not None:
            self.cu_reserved = m.get('CuReserved')

        if m.get('DraftSql') is not None:
            self.draft_sql = m.get('DraftSql')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('JobConfig') is not None:
            self.job_config = m.get('JobConfig')

        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('UpgradeMode') is not None:
            self.upgrade_mode = m.get('UpgradeMode')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

