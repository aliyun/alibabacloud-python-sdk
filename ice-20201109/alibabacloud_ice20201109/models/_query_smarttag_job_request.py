# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QuerySmarttagJobRequest(DaraModel):
    def __init__(
        self,
        job_id: str = None,
        params: str = None,
    ):
        # The ID of the smart tagging job that you want to query. You can obtain the job ID from the response parameters of the SubmitSmarttagJob operation.
        # 
        # This parameter is required.
        self.job_id = job_id
        # The extra parameters that you want to query in the request. The value is a JSON string. Example: {"labelResultType":"auto"}. The value of labelResultType is of the STRING type. Valid values:
        # 
        # *   auto: machine tagging
        # *   hmi: tagging by human and machine
        self.params = params

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.params is not None:
            result['Params'] = self.params

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        return self

