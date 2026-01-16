# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class MigrationJob(DaraModel):
    def __init__(
        self,
        current_state: str = None,
        disable_source_cluster_auth: bool = None,
        disable_target_cluster_auth: bool = None,
        end_time: int = None,
        migration_job_id: str = None,
        phase: str = None,
        source_cluster: main_models.MigrationJobSourceCluster = None,
        start_time: int = None,
        status_result: List[main_models.MigrationJobStatusResult] = None,
        target_cluster: main_models.MigrationJobTargetCluster = None,
        update_time: int = None,
    ):
        self.current_state = current_state
        self.disable_source_cluster_auth = disable_source_cluster_auth
        self.disable_target_cluster_auth = disable_target_cluster_auth
        self.end_time = end_time
        self.migration_job_id = migration_job_id
        self.phase = phase
        self.source_cluster = source_cluster
        self.start_time = start_time
        self.status_result = status_result
        self.target_cluster = target_cluster
        self.update_time = update_time

    def validate(self):
        if self.source_cluster:
            self.source_cluster.validate()
        if self.status_result:
            for v1 in self.status_result:
                 if v1:
                    v1.validate()
        if self.target_cluster:
            self.target_cluster.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_state is not None:
            result['currentState'] = self.current_state

        if self.disable_source_cluster_auth is not None:
            result['disableSourceClusterAuth'] = self.disable_source_cluster_auth

        if self.disable_target_cluster_auth is not None:
            result['disableTargetClusterAuth'] = self.disable_target_cluster_auth

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.migration_job_id is not None:
            result['migrationJobId'] = self.migration_job_id

        if self.phase is not None:
            result['phase'] = self.phase

        if self.source_cluster is not None:
            result['sourceCluster'] = self.source_cluster.to_map()

        if self.start_time is not None:
            result['startTime'] = self.start_time

        result['statusResult'] = []
        if self.status_result is not None:
            for k1 in self.status_result:
                result['statusResult'].append(k1.to_map() if k1 else None)

        if self.target_cluster is not None:
            result['targetCluster'] = self.target_cluster.to_map()

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currentState') is not None:
            self.current_state = m.get('currentState')

        if m.get('disableSourceClusterAuth') is not None:
            self.disable_source_cluster_auth = m.get('disableSourceClusterAuth')

        if m.get('disableTargetClusterAuth') is not None:
            self.disable_target_cluster_auth = m.get('disableTargetClusterAuth')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('migrationJobId') is not None:
            self.migration_job_id = m.get('migrationJobId')

        if m.get('phase') is not None:
            self.phase = m.get('phase')

        if m.get('sourceCluster') is not None:
            temp_model = main_models.MigrationJobSourceCluster()
            self.source_cluster = temp_model.from_map(m.get('sourceCluster'))

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        self.status_result = []
        if m.get('statusResult') is not None:
            for k1 in m.get('statusResult'):
                temp_model = main_models.MigrationJobStatusResult()
                self.status_result.append(temp_model.from_map(k1))

        if m.get('targetCluster') is not None:
            temp_model = main_models.MigrationJobTargetCluster()
            self.target_cluster = temp_model.from_map(m.get('targetCluster'))

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        return self

class MigrationJobTargetCluster(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        type: str = None,
    ):
        self.instance_id = instance_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class MigrationJobStatusResult(DaraModel):
    def __init__(
        self,
        code: str = None,
        success: bool = None,
    ):
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class MigrationJobSourceCluster(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        type: str = None,
    ):
        self.instance_id = instance_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

