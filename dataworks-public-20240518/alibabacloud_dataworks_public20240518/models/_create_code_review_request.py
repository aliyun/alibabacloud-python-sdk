# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCodeReviewRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        pipeline_run_id: str = None,
        project_id: int = None,
        reviewers: str = None,
    ):
        # The description of the code review. The maximum length is 1,024 characters.
        self.description = description
        # The ID of a single release pipeline.
        # 
        # This parameter is required.
        self.pipeline_run_id = pipeline_run_id
        # The workspace ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # Specifies the reviewers. Separate multiple accounts with commas (,). At least one reviewer is required, and the maximum length is 512 characters after deduplication.
        # 
        # This parameter is required.
        self.reviewers = reviewers

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.pipeline_run_id is not None:
            result['PipelineRunId'] = self.pipeline_run_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.reviewers is not None:
            result['Reviewers'] = self.reviewers

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('PipelineRunId') is not None:
            self.pipeline_run_id = m.get('PipelineRunId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Reviewers') is not None:
            self.reviewers = m.get('Reviewers')

        return self

