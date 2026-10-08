# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class StartK8sAppPrecheckResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.StartK8sAppPrecheckResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The HTTP status code.
        self.code = code
        # The returned data.
        self.data = data
        # The returned message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.StartK8sAppPrecheckResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class StartK8sAppPrecheckResponseBodyData(DaraModel):
    def __init__(
        self,
        jobs: List[str] = None,
    ):
        # The jobs and the details about the jobs.
        self.jobs = jobs

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.jobs is not None:
            result['Jobs'] = self.jobs

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Jobs') is not None:
            self.jobs = m.get('Jobs')

        return self

