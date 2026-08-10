# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_codesec20260401 import models as main_models
from darabonba.model import DaraModel

class DescribeScansResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeScansResponseBodyItems] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.items = items
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.DescribeScansResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class DescribeScansResponseBodyItems(DaraModel):
    def __init__(
        self,
        code_bundle_id: int = None,
        created_at: str = None,
        created_by: str = None,
        engine_snapshot: main_models.DescribeScansResponseBodyItemsEngineSnapshot = None,
        finished_at: str = None,
        id: int = None,
        kind: str = None,
        project_id: int = None,
        scan_metrics: main_models.DescribeScansResponseBodyItemsScanMetrics = None,
        scan_progress: int = None,
        started_at: str = None,
        status: str = None,
        task_name: str = None,
        updated_at: str = None,
        worker_id: str = None,
    ):
        self.code_bundle_id = code_bundle_id
        # 扫描任务创建时间（RFC3339）
        self.created_at = created_at
        self.created_by = created_by
        self.engine_snapshot = engine_snapshot
        # 扫描结束时间（RFC3339）
        self.finished_at = finished_at
        self.id = id
        self.kind = kind
        self.project_id = project_id
        self.scan_metrics = scan_metrics
        self.scan_progress = scan_progress
        # 扫描开始时间（RFC3339）
        self.started_at = started_at
        self.status = status
        self.task_name = task_name
        # 扫描任务更新时间（RFC3339）
        self.updated_at = updated_at
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
            temp_model = main_models.DescribeScansResponseBodyItemsEngineSnapshot()
            self.engine_snapshot = temp_model.from_map(m.get('engineSnapshot'))

        if m.get('finishedAt') is not None:
            self.finished_at = m.get('finishedAt')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('kind') is not None:
            self.kind = m.get('kind')

        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')

        if m.get('scanMetrics') is not None:
            temp_model = main_models.DescribeScansResponseBodyItemsScanMetrics()
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

class DescribeScansResponseBodyItemsScanMetrics(DaraModel):
    def __init__(
        self,
        credit: float = None,
        file_count: int = None,
        lines_of_code: int = None,
        token_total: int = None,
    ):
        self.credit = credit
        self.file_count = file_count
        self.lines_of_code = lines_of_code
        self.token_total = token_total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credit is not None:
            result['credit'] = self.credit

        if self.file_count is not None:
            result['fileCount'] = self.file_count

        if self.lines_of_code is not None:
            result['linesOfCode'] = self.lines_of_code

        if self.token_total is not None:
            result['tokenTotal'] = self.token_total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('credit') is not None:
            self.credit = m.get('credit')

        if m.get('fileCount') is not None:
            self.file_count = m.get('fileCount')

        if m.get('linesOfCode') is not None:
            self.lines_of_code = m.get('linesOfCode')

        if m.get('tokenTotal') is not None:
            self.token_total = m.get('tokenTotal')

        return self

class DescribeScansResponseBodyItemsEngineSnapshot(DaraModel):
    def __init__(
        self,
        sast: bool = None,
        sca: bool = None,
    ):
        self.sast = sast
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

