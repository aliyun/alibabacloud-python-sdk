# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class GetK8sAppPrecheckResultResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetK8sAppPrecheckResultResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The HTTP status code that is returned.
        self.code = code
        # The data that is returned.
        self.data = data
        # The additional information that is returned.
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
            temp_model = main_models.GetK8sAppPrecheckResultResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetK8sAppPrecheckResultResponseBodyData(DaraModel):
    def __init__(
        self,
        job_results: List[main_models.GetK8sAppPrecheckResultResponseBodyDataJobResults] = None,
        reason: str = None,
        status: str = None,
    ):
        # The precheck result for the application change.
        self.job_results = job_results
        # The reason why the application failed the precheck. This parameter is left empty when the application passed the precheck.
        self.reason = reason
        # The precheck state for the application change. Valid values:
        # 
        # - checking: The application is being prechecked.
        # 
        # - pass: The application passed the precheck.
        # 
        # - failed: The application failed the precheck.
        self.status = status

    def validate(self):
        if self.job_results:
            for v1 in self.job_results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['JobResults'] = []
        if self.job_results is not None:
            for k1 in self.job_results:
                result['JobResults'].append(k1.to_map() if k1 else None)

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.job_results = []
        if m.get('JobResults') is not None:
            for k1 in m.get('JobResults'):
                temp_model = main_models.GetK8sAppPrecheckResultResponseBodyDataJobResults()
                self.job_results.append(temp_model.from_map(k1))

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetK8sAppPrecheckResultResponseBodyDataJobResults(DaraModel):
    def __init__(
        self,
        interrupted: bool = None,
        name: str = None,
        pass_: bool = None,
        reason: str = None,
    ):
        # Specifies whether the precheck of the item was interrupted:
        # 
        # - true: The precheck of the item was interrupted.
        # 
        # - false: The precheck of the item was not interrupted.
        self.interrupted = interrupted
        # The name of the precheck item.
        self.name = name
        # Indicates whether the precheck item passed the precheck:
        # 
        # - true: The precheck item passed the precheck.
        # 
        # - false: The precheck item failed the precheck.
        self.pass_ = pass_
        # The reason why the precheck item failed the precheck or the precheck of the item was interrupted. This parameter is left empty when the application passed the precheck.
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.interrupted is not None:
            result['Interrupted'] = self.interrupted

        if self.name is not None:
            result['Name'] = self.name

        if self.pass_ is not None:
            result['Pass'] = self.pass_

        if self.reason is not None:
            result['Reason'] = self.reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Interrupted') is not None:
            self.interrupted = m.get('Interrupted')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Pass') is not None:
            self.pass_ = m.get('Pass')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        return self

