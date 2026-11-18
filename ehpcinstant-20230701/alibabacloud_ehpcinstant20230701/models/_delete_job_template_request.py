# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteJobTemplateRequest(DaraModel):
    def __init__(
        self,
        job_template_id: str = None,
    ):
        # The ID of the job template.
        # 
        # This parameter is required.
        self.job_template_id = job_template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_template_id is not None:
            result['JobTemplateId'] = self.job_template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobTemplateId') is not None:
            self.job_template_id = m.get('JobTemplateId')

        return self

