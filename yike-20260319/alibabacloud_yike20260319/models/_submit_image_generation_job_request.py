# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitImageGenerationJobRequest(DaraModel):
    def __init__(
        self,
        aspect_ratio: str = None,
        client_token: str = None,
        input: str = None,
        job_parameters: str = None,
        job_type: str = None,
        model: str = None,
        n: str = None,
        resolution: str = None,
        scene: str = None,
        user_data: str = None,
    ):
        self.aspect_ratio = aspect_ratio
        self.client_token = client_token
        self.input = input
        self.job_parameters = job_parameters
        self.job_type = job_type
        self.model = model
        self.n = n
        self.resolution = resolution
        self.scene = scene
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aspect_ratio is not None:
            result['AspectRatio'] = self.aspect_ratio

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.input is not None:
            result['Input'] = self.input

        if self.job_parameters is not None:
            result['JobParameters'] = self.job_parameters

        if self.job_type is not None:
            result['JobType'] = self.job_type

        if self.model is not None:
            result['Model'] = self.model

        if self.n is not None:
            result['N'] = self.n

        if self.resolution is not None:
            result['Resolution'] = self.resolution

        if self.scene is not None:
            result['Scene'] = self.scene

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AspectRatio') is not None:
            self.aspect_ratio = m.get('AspectRatio')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Input') is not None:
            self.input = m.get('Input')

        if m.get('JobParameters') is not None:
            self.job_parameters = m.get('JobParameters')

        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('N') is not None:
            self.n = m.get('N')

        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')

        if m.get('Scene') is not None:
            self.scene = m.get('Scene')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

