# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_codesec20260401 import models as main_models
from darabonba.model import DaraModel

class CreateScanResponseBody(DaraModel):
    def __init__(
        self,
        code_bundle_id: int = None,
        created_at: str = None,
        created_by: str = None,
        engine_snapshot: main_models.CreateScanResponseBodyEngineSnapshot = None,
        finished_at: str = None,
        id: int = None,
        kind: str = None,
        project_id: int = None,
        request_id: str = None,
        scan_metrics: main_models.CreateScanResponseBodyScanMetrics = None,
        scan_progress: int = None,
        started_at: str = None,
        status: str = None,
        task_name: str = None,
        updated_at: str = None,
        worker_id: str = None,
    ):
        # The code package ID.
        self.code_bundle_id = code_bundle_id
        # The creation time.
        self.created_at = created_at
        # The user ID of the task creator.
        self.created_by = created_by
        # The supported types.
        self.engine_snapshot = engine_snapshot
        # The scan end time.
        self.finished_at = finished_at
        # The task ID.
        self.id = id
        # The type. Valid values:
        # * full: full data
        # * incremental: incremental
        self.kind = kind
        # The project ID.
        self.project_id = project_id
        # The request ID.
        self.request_id = request_id
        # The scan information.
        self.scan_metrics = scan_metrics
        # The task progress.
        self.scan_progress = scan_progress
        # The start time.
        self.started_at = started_at
        # The status. Valid values:
        # * running: Running.
        # * completed: Completed.
        # * failed: Failed.
        # * canceling: Being canceled.
        # * canceled: Canceled.
        self.status = status
        # The task name.
        self.task_name = task_name
        # The update time.
        self.updated_at = updated_at
        # Deprecated.
        self.worker_id = worker_id

    def validate(self):
        if self.engine_snapshot:
            self.engine_snapshot.validate()
        if self.scan_metrics:
            self.scan_metrics.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code_bundle_id is not None:
            result['codeBundleId'] = self.code_bundle_id

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.created_by is not None:
            result['createdBy'] = self.created_by

        if self.engine_snapshot is not None:
            result['engineSnapshot'] = self.engine_snapshot.to_map()

        if self.finished_at is not None:
            result['finishedAt'] = self.finished_at

        if self.id is not None:
            result['id'] = self.id

        if self.kind is not None:
            result['kind'] = self.kind

        if self.project_id is not None:
            result['projectId'] = self.project_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.scan_metrics is not None:
            result['scanMetrics'] = self.scan_metrics.to_map()

        if self.scan_progress is not None:
            result['scanProgress'] = self.scan_progress

        if self.started_at is not None:
            result['startedAt'] = self.started_at

        if self.status is not None:
            result['status'] = self.status

        if self.task_name is not None:
            result['taskName'] = self.task_name

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        if self.worker_id is not None:
            result['workerId'] = self.worker_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('codeBundleId') is not None:
            self.code_bundle_id = m.get('codeBundleId')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('createdBy') is not None:
            self.created_by = m.get('createdBy')

        if m.get('engineSnapshot') is not None:
            temp_model = main_models.CreateScanResponseBodyEngineSnapshot()
            self.engine_snapshot = temp_model.from_map(m.get('engineSnapshot'))

        if m.get('finishedAt') is not None:
            self.finished_at = m.get('finishedAt')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('kind') is not None:
            self.kind = m.get('kind')

        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('scanMetrics') is not None:
            temp_model = main_models.CreateScanResponseBodyScanMetrics()
            self.scan_metrics = temp_model.from_map(m.get('scanMetrics'))

        if m.get('scanProgress') is not None:
            self.scan_progress = m.get('scanProgress')

        if m.get('startedAt') is not None:
            self.started_at = m.get('startedAt')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('taskName') is not None:
            self.task_name = m.get('taskName')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('workerId') is not None:
            self.worker_id = m.get('workerId')

        return self

class CreateScanResponseBodyScanMetrics(DaraModel):
    def __init__(
        self,
        file_count: int = None,
        lines_of_code: int = None,
        token_total: int = None,
    ):
        # The number of files.
        self.file_count = file_count
        # The number of lines of code.
        self.lines_of_code = lines_of_code
        # Deprecated.
        self.token_total = token_total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_count is not None:
            result['fileCount'] = self.file_count

        if self.lines_of_code is not None:
            result['linesOfCode'] = self.lines_of_code

        if self.token_total is not None:
            result['tokenTotal'] = self.token_total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileCount') is not None:
            self.file_count = m.get('fileCount')

        if m.get('linesOfCode') is not None:
            self.lines_of_code = m.get('linesOfCode')

        if m.get('tokenTotal') is not None:
            self.token_total = m.get('tokenTotal')

        return self

class CreateScanResponseBodyEngineSnapshot(DaraModel):
    def __init__(
        self,
        sast: bool = None,
        sca: bool = None,
    ):
        # Indicates whether SAST is supported.
        self.sast = sast
        # Indicates whether SCA is supported.
        self.sca = sca

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.sast is not None:
            result['sast'] = self.sast

        if self.sca is not None:
            result['sca'] = self.sca

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sast') is not None:
            self.sast = m.get('sast')

        if m.get('sca') is not None:
            self.sca = m.get('sca')

        return self

