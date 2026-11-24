# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartComputeJobRequest(DaraModel):
    def __init__(
        self,
        cu_limit: float = None,
        cu_reserved: float = None,
        draft_sql: str = None,
        instance_id: str = None,
        job_name: str = None,
        recovery_mode: str = None,
        region_id: str = None,
    ):
        # The CU limit for the job. Integers and decimals are supported.
        self.cu_limit = cu_limit
        # The number of reserved CUs for the job. Integers and decimals are supported.
        # 
        # > The number of reserved CUs cannot exceed the CU limit.
        self.cu_reserved = cu_reserved
        # **The Flink SQL draft, which must be a self-contained and complete DDL and DML statement.**
        self.draft_sql = draft_sql
        # **The compute instance ID.**
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # **The name of the compute job.**
        # 
        # This parameter is required.
        self.job_name = job_name
        # **The recovery mode, such as savepoint or stateless.**
        self.recovery_mode = recovery_mode
        # **The region ID.**
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cu_limit is not None:
            result['CuLimit'] = self.cu_limit

        if self.cu_reserved is not None:
            result['CuReserved'] = self.cu_reserved

        if self.draft_sql is not None:
            result['DraftSql'] = self.draft_sql

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.job_name is not None:
            result['JobName'] = self.job_name

        if self.recovery_mode is not None:
            result['RecoveryMode'] = self.recovery_mode

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CuLimit') is not None:
            self.cu_limit = m.get('CuLimit')

        if m.get('CuReserved') is not None:
            self.cu_reserved = m.get('CuReserved')

        if m.get('DraftSql') is not None:
            self.draft_sql = m.get('DraftSql')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        if m.get('RecoveryMode') is not None:
            self.recovery_mode = m.get('RecoveryMode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

