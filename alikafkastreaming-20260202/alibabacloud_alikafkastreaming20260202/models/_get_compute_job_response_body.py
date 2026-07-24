# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_alikafkastreaming20260202 import models as main_models
from darabonba.model import DaraModel

class GetComputeJobResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetComputeJobResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetComputeJobResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetComputeJobResponseBodyData(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        cu_limit: float = None,
        cu_reserved: float = None,
        cu_used: float = None,
        debug_mode: int = None,
        deployed_sql: str = None,
        draft_sql: str = None,
        history_infos: str = None,
        instance_id: str = None,
        job_config: str = None,
        job_name: str = None,
        owner: str = None,
        region_id: str = None,
        remark: str = None,
        status: str = None,
        upgrade_mode: str = None,
    ):
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.create_time = create_time
        self.cu_limit = cu_limit
        self.cu_reserved = cu_reserved
        self.cu_used = cu_used
        self.debug_mode = debug_mode
        self.deployed_sql = deployed_sql
        self.draft_sql = draft_sql
        self.history_infos = history_infos
        self.instance_id = instance_id
        self.job_config = job_config
        self.job_name = job_name
        self.owner = owner
        self.region_id = region_id
        self.remark = remark
        self.status = status
        self.upgrade_mode = upgrade_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.cu_limit is not None:
            result['CuLimit'] = self.cu_limit

        if self.cu_reserved is not None:
            result['CuReserved'] = self.cu_reserved

        if self.cu_used is not None:
            result['CuUsed'] = self.cu_used

        if self.debug_mode is not None:
            result['DebugMode'] = self.debug_mode

        if self.deployed_sql is not None:
            result['DeployedSql'] = self.deployed_sql

        if self.draft_sql is not None:
            result['DraftSql'] = self.draft_sql

        if self.history_infos is not None:
            result['HistoryInfos'] = self.history_infos

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.job_config is not None:
            result['JobConfig'] = self.job_config

        if self.job_name is not None:
            result['JobName'] = self.job_name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.status is not None:
            result['Status'] = self.status

        if self.upgrade_mode is not None:
            result['UpgradeMode'] = self.upgrade_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CuLimit') is not None:
            self.cu_limit = m.get('CuLimit')

        if m.get('CuReserved') is not None:
            self.cu_reserved = m.get('CuReserved')

        if m.get('CuUsed') is not None:
            self.cu_used = m.get('CuUsed')

        if m.get('DebugMode') is not None:
            self.debug_mode = m.get('DebugMode')

        if m.get('DeployedSql') is not None:
            self.deployed_sql = m.get('DeployedSql')

        if m.get('DraftSql') is not None:
            self.draft_sql = m.get('DraftSql')

        if m.get('HistoryInfos') is not None:
            self.history_infos = m.get('HistoryInfos')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('JobConfig') is not None:
            self.job_config = m.get('JobConfig')

        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpgradeMode') is not None:
            self.upgrade_mode = m.get('UpgradeMode')

        return self

