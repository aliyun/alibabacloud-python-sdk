# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Personalizedtxt2imgQueryInferenceJobInfoRequest(DaraModel):
    def __init__(
        self,
        inference_job_id: str = None,
    ):
        # This parameter is required.
        self.inference_job_id = inference_job_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.inference_job_id is not None:
            result['inferenceJobId'] = self.inference_job_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('inferenceJobId') is not None:
            self.inference_job_id = m.get('inferenceJobId')

        return self

