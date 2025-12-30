# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetLiveRecordTemplateRequest(DaraModel):
    def __init__(
        self,
        job_id: str = None,
        template_id: str = None,
    ):
        # The ID of the recording job. You can specify the JobId parameter to retrieve the snapshot of the template used by the job.
        self.job_id = job_id
        # The template ID.
        # 
        # This parameter is required.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

