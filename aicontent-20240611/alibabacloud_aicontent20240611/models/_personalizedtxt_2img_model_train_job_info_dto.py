# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aicontent20240611 import models as main_models
from darabonba.model import DaraModel

class Personalizedtxt2imgModelTrainJobInfoDTO(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        create_user_id: str = None,
        image_url: List[str] = None,
        inference_job_list: List[main_models.Personalizedtxt2imgInferenceJobInfoDTO] = None,
        job_status: str = None,
        name: str = None,
        object_type: str = None,
        id: str = None,
    ):
        self.create_time = create_time
        self.create_user_id = create_user_id
        self.image_url = image_url
        self.inference_job_list = inference_job_list
        self.job_status = job_status
        self.name = name
        self.object_type = object_type
        self.id = id

    def validate(self):
        if self.inference_job_list:
            for v1 in self.inference_job_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        result['InferenceJobList'] = []
        if self.inference_job_list is not None:
            for k1 in self.inference_job_list:
                result['InferenceJobList'].append(k1.to_map() if k1 else None)

        if self.job_status is not None:
            result['JobStatus'] = self.job_status

        if self.name is not None:
            result['Name'] = self.name

        if self.object_type is not None:
            result['ObjectType'] = self.object_type

        if self.id is not None:
            result['id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        self.inference_job_list = []
        if m.get('InferenceJobList') is not None:
            for k1 in m.get('InferenceJobList'):
                temp_model = main_models.Personalizedtxt2imgInferenceJobInfoDTO()
                self.inference_job_list.append(temp_model.from_map(k1))

        if m.get('JobStatus') is not None:
            self.job_status = m.get('JobStatus')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')

        if m.get('id') is not None:
            self.id = m.get('id')

        return self

