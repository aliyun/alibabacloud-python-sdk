# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class GetDISyncInstanceInfoResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetDISyncInstanceInfoResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status of the real-time synchronization task or data synchronization solution.
        self.data = data
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetDISyncInstanceInfoResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetDISyncInstanceInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        message: str = None,
        name: str = None,
        solution_info: main_models.GetDISyncInstanceInfoResponseBodyDataSolutionInfo = None,
        status: str = None,
    ):
        # The cause of the failure to obtain the status of the real-time synchronization task or data synchronization solution. If the status of the real-time synchronization task or data synchronization solution is obtained, the value null is returned.
        self.message = message
        # *   If the TaskType parameter is set to DI_REALTIME, the Name parameter indicates the name of the real-time synchronization task.
        # *   If the TaskType parameter is set to DI_SOLUTION, the value null is returned.
        self.name = name
        # *   If the TaskType parameter is set to DI_REALTIME, the value null is returned.
        # *   If the TaskType parameter is set to DI_SOLUTION, the SolutionInfo parameter indicates the details of the data synchronization solution.
        self.solution_info = solution_info
        # *   If the TaskType parameter is set to DI_REALTIME, the Status parameter indicates the status of the real-time synchronization task. Valid values: PAUSE, NORUN, RUN, KILLING, and WAIT.
        # *   If the TaskType parameter is set to DI_SOLUTION, the Status parameter indicates the status of the data synchronization solution. Valid values: success and fail.
        self.status = status

    def validate(self):
        if self.solution_info:
            self.solution_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['Message'] = self.message

        if self.name is not None:
            result['Name'] = self.name

        if self.solution_info is not None:
            result['SolutionInfo'] = self.solution_info.to_map()

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SolutionInfo') is not None:
            temp_model = main_models.GetDISyncInstanceInfoResponseBodyDataSolutionInfo()
            self.solution_info = temp_model.from_map(m.get('SolutionInfo'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetDISyncInstanceInfoResponseBodyDataSolutionInfo(DaraModel):
    def __init__(
        self,
        creator_name: str = None,
        id: int = None,
        status: str = None,
        step_detail: List[main_models.GetDISyncInstanceInfoResponseBodyDataSolutionInfoStepDetail] = None,
    ):
        # The creator of the data synchronization solution.
        self.creator_name = creator_name
        # The ID of the data synchronization solution.
        self.id = id
        # The status of the data synchronization solution.
        self.status = status
        # The step details of the data synchronization solution.
        self.step_detail = step_detail

    def validate(self):
        if self.step_detail:
            for v1 in self.step_detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creator_name is not None:
            result['CreatorName'] = self.creator_name

        if self.id is not None:
            result['Id'] = self.id

        if self.status is not None:
            result['Status'] = self.status

        result['StepDetail'] = []
        if self.step_detail is not None:
            for k1 in self.step_detail:
                result['StepDetail'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatorName') is not None:
            self.creator_name = m.get('CreatorName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.step_detail = []
        if m.get('StepDetail') is not None:
            for k1 in m.get('StepDetail'):
                temp_model = main_models.GetDISyncInstanceInfoResponseBodyDataSolutionInfoStepDetail()
                self.step_detail.append(temp_model.from_map(k1))

        return self

class GetDISyncInstanceInfoResponseBodyDataSolutionInfoStepDetail(DaraModel):
    def __init__(
        self,
        info: str = None,
        status: str = None,
        step_id: int = None,
        step_name: str = None,
    ):
        # The information of the data synchronization solution.
        self.info = info
        # The status of the step in the data synchronization solution.
        self.status = status
        # The ID of the step in the data synchronization solution.
        self.step_id = step_id
        # The name of the step in the data synchronization solution.
        self.step_name = step_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.info is not None:
            result['Info'] = self.info

        if self.status is not None:
            result['Status'] = self.status

        if self.step_id is not None:
            result['StepId'] = self.step_id

        if self.step_name is not None:
            result['StepName'] = self.step_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Info') is not None:
            self.info = m.get('Info')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StepId') is not None:
            self.step_id = m.get('StepId')

        if m.get('StepName') is not None:
            self.step_name = m.get('StepName')

        return self

