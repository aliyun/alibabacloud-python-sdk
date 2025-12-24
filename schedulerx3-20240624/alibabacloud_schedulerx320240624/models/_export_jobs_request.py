# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ExportJobsRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        cluster_id: str = None,
        export_job_type: int = None,
        job_ids: List[int] = None,
    ):
        # This parameter is required.
        self.app_name = app_name
        # This parameter is required.
        self.cluster_id = cluster_id
        self.export_job_type = export_job_type
        # -
        self.job_ids = job_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.export_job_type is not None:
            result['ExportJobType'] = self.export_job_type

        if self.job_ids is not None:
            result['JobIds'] = self.job_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ExportJobType') is not None:
            self.export_job_type = m.get('ExportJobType')

        if m.get('JobIds') is not None:
            self.job_ids = m.get('JobIds')

        return self

