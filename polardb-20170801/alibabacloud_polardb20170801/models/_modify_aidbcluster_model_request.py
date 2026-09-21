# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyAIDBClusterModelRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        display_model_name: str = None,
        dry_run: bool = None,
        model_name: str = None,
        region_id: str = None,
        restart_mode: str = None,
        worker_batch_size: int = None,
    ):
        # The ID of the PolarDB AI 3.0 logical instance.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The new client-facing invocation name. If this parameter is not specified, the existing invocation name is retained.
        self.display_model_name = display_model_name
        # Specifies whether to only preview the change without actually performing it.
        self.dry_run = dry_run
        # The name of the target model. Select a value from the ModelName values returned by the DescribeAvailableModels operation.
        # 
        # This parameter is required.
        self.model_name = model_name
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The restart mode for workers. Valid values:
        # - inPlace
        # - recreate
        self.restart_mode = restart_mode
        # The maximum number of workers to restart per batch within a single MSD. Valid values: 1 to 30. This parameter takes effect only when RestartMode is set to inPlace.
        self.worker_batch_size = worker_batch_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.display_model_name is not None:
            result['DisplayModelName'] = self.display_model_name

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.model_name is not None:
            result['ModelName'] = self.model_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.restart_mode is not None:
            result['RestartMode'] = self.restart_mode

        if self.worker_batch_size is not None:
            result['WorkerBatchSize'] = self.worker_batch_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DisplayModelName') is not None:
            self.display_model_name = m.get('DisplayModelName')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RestartMode') is not None:
            self.restart_mode = m.get('RestartMode')

        if m.get('WorkerBatchSize') is not None:
            self.worker_batch_size = m.get('WorkerBatchSize')

        return self

