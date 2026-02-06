# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class SubmitDynamicImageJobResponseBody(DaraModel):
    def __init__(
        self,
        dynamic_image_job: main_models.SubmitDynamicImageJobResponseBodyDynamicImageJob = None,
        request_id: str = None,
    ):
        # The information about the animated image job.
        self.dynamic_image_job = dynamic_image_job
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.dynamic_image_job:
            self.dynamic_image_job.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dynamic_image_job is not None:
            result['DynamicImageJob'] = self.dynamic_image_job.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DynamicImageJob') is not None:
            temp_model = main_models.SubmitDynamicImageJobResponseBodyDynamicImageJob()
            self.dynamic_image_job = temp_model.from_map(m.get('DynamicImageJob'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class SubmitDynamicImageJobResponseBodyDynamicImageJob(DaraModel):
    def __init__(
        self,
        job_id: str = None,
    ):
        # The ID of the animated image job.
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_id is not None:
            result['JobId'] = self.job_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        return self

