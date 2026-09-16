# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyAIDBClusterModelResponseBody(DaraModel):
    def __init__(
        self,
        dry_run: bool = None,
        model_type: str = None,
        request_id: str = None,
        target_model_name: str = None,
        target_oss_path: str = None,
        task_id: int = None,
        total_batches: int = None,
        total_msds: int = None,
        warnings: List[str] = None,
    ):
        # Indicates whether the request is a dry run.
        self.dry_run = dry_run
        # The model type of the instance.
        self.model_type = model_type
        # Id of the request
        self.request_id = request_id
        # The resolved target model name.
        self.target_model_name = target_model_name
        # The resolved target OSS path.
        self.target_oss_path = target_oss_path
        # The ID of the asynchronous task. This parameter is empty when DryRun is set to true.
        self.task_id = task_id
        # The number of change batches.
        self.total_batches = total_batches
        # The number of affected model service instances.
        self.total_msds = total_msds
        # The change warnings returned by the upstream service. The caller must display these warnings.
        self.warnings = warnings

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.model_type is not None:
            result['ModelType'] = self.model_type

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.target_model_name is not None:
            result['TargetModelName'] = self.target_model_name

        if self.target_oss_path is not None:
            result['TargetOssPath'] = self.target_oss_path

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.total_batches is not None:
            result['TotalBatches'] = self.total_batches

        if self.total_msds is not None:
            result['TotalMsds'] = self.total_msds

        if self.warnings is not None:
            result['Warnings'] = self.warnings

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TargetModelName') is not None:
            self.target_model_name = m.get('TargetModelName')

        if m.get('TargetOssPath') is not None:
            self.target_oss_path = m.get('TargetOssPath')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TotalBatches') is not None:
            self.total_batches = m.get('TotalBatches')

        if m.get('TotalMsds') is not None:
            self.total_msds = m.get('TotalMsds')

        if m.get('Warnings') is not None:
            self.warnings = m.get('Warnings')

        return self

