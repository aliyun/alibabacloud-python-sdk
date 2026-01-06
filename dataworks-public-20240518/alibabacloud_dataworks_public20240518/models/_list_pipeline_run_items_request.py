# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPipelineRunItemsRequest(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        pipeline_run_id: str = None,
        project_id: int = None,
    ):
        # The page number, for pagination.
        self.page_number = page_number
        # The requested page number, used for pagination.
        self.page_size = page_size
        # The workflow task ID. To obtain the ID, see [ListPipelineRuns](https://help.aliyun.com/document_detail/438042.html).
        # 
        # This parameter is required.
        self.pipeline_run_id = pipeline_run_id
        # The ID of the DataWorks workspace. You can obtain the workspace ID from the workspace configuration page in the DataWorks console.
        # 
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.pipeline_run_id is not None:
            result['PipelineRunId'] = self.pipeline_run_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PipelineRunId') is not None:
            self.pipeline_run_id = m.get('PipelineRunId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

