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
        # The ID of the smart tagging job. You can obtain this ID from the response to the [SubmitSmarttagJob](https://help.aliyun.com/document_detail/478786.html) call.
        # 
        # This parameter is required.
        self.job_id = job_id
        # Additional request parameters, formatted as a JSON string. For example: `{"labelResultType":"auto"}`. The `labelResultType` parameter supports the following values:
        # 
        # - `auto`: machine-generated tagging results
        # 
        # - `hmi`: human-in-the-loop tagging results
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

