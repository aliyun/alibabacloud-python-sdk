# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class Personalizedtxt2imgInferenceJobInfoDTO(DaraModel):
    def __init__(
        self,
        create_user_id: str = None,
        id: str = None,
        job_status: str = None,
        model_id: str = None,
        result_image_url: List[str] = None,
    ):
        self.create_user_id = create_user_id
        self.id = id
        self.job_status = job_status
        self.model_id = model_id
        self.result_image_url = result_image_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_user_id is not None:
            result['createUserId'] = self.create_user_id

        if self.id is not None:
            result['id'] = self.id

        if self.job_status is not None:
            result['jobStatus'] = self.job_status

        if self.model_id is not None:
            result['modelId'] = self.model_id

        if self.result_image_url is not None:
            result['resultImageUrl'] = self.result_image_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createUserId') is not None:
            self.create_user_id = m.get('createUserId')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('jobStatus') is not None:
            self.job_status = m.get('jobStatus')

        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')

        if m.get('resultImageUrl') is not None:
            self.result_image_url = m.get('resultImageUrl')

        return self

