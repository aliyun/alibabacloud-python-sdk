# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryVideoCognitionJobShrinkRequest(DaraModel):
    def __init__(
        self,
        include_results_shrink: str = None,
        job_id: str = None,
        params: str = None,
    ):
        # Specifies whether to include the full algorithm results in the response.
        self.include_results_shrink = include_results_shrink
        # The ID of the task to query. It is returned when you call the [SubmitSmarttagJob](https://help.aliyun.com/document_detail/478786.html) operation.
        # 
        # This parameter is required.
        self.job_id = job_id
        # Additional request parameters, provided as a JSON string.
        self.params = params

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.include_results_shrink is not None:
            result['IncludeResults'] = self.include_results_shrink

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.params is not None:
            result['Params'] = self.params

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IncludeResults') is not None:
            self.include_results_shrink = m.get('IncludeResults')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        return self

