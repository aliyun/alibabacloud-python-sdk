# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class GetRunningTasksResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.GetRunningTasksResponseBodyResult] = None,
        vendor_request_id: str = None,
        vendor_type: str = None,
    ):
        self.request_id = request_id
        self.result = result
        self.vendor_request_id = vendor_request_id
        self.vendor_type = vendor_type

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['result'].append(k1.to_map() if k1 else None)

        if self.vendor_request_id is not None:
            result['vendorRequestId'] = self.vendor_request_id

        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.result = []
        if m.get('result') is not None:
            for k1 in m.get('result'):
                temp_model = main_models.GetRunningTasksResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('vendorRequestId') is not None:
            self.vendor_request_id = m.get('vendorRequestId')

        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')

        return self

class GetRunningTasksResponseBodyResult(DaraModel):
    def __init__(
        self,
        active_time_gmt: str = None,
        activity_id: str = None,
        actual_actioner_id: str = None,
        create_time_gmt: str = None,
        finish_time_gmt: str = None,
        originator_id: str = None,
        process_instance_id: str = None,
        status: str = None,
        task_id: str = None,
        task_type: str = None,
        title: str = None,
        title_in_english: str = None,
    ):
        self.active_time_gmt = active_time_gmt
        self.activity_id = activity_id
        self.actual_actioner_id = actual_actioner_id
        self.create_time_gmt = create_time_gmt
        self.finish_time_gmt = finish_time_gmt
        self.originator_id = originator_id
        self.process_instance_id = process_instance_id
        self.status = status
        self.task_id = task_id
        self.task_type = task_type
        self.title = title
        self.title_in_english = title_in_english

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active_time_gmt is not None:
            result['ActiveTimeGMT'] = self.active_time_gmt

        if self.activity_id is not None:
            result['ActivityId'] = self.activity_id

        if self.actual_actioner_id is not None:
            result['ActualActionerId'] = self.actual_actioner_id

        if self.create_time_gmt is not None:
            result['CreateTimeGMT'] = self.create_time_gmt

        if self.finish_time_gmt is not None:
            result['FinishTimeGMT'] = self.finish_time_gmt

        if self.originator_id is not None:
            result['OriginatorId'] = self.originator_id

        if self.process_instance_id is not None:
            result['ProcessInstanceId'] = self.process_instance_id

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.title is not None:
            result['Title'] = self.title

        if self.title_in_english is not None:
            result['TitleInEnglish'] = self.title_in_english

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveTimeGMT') is not None:
            self.active_time_gmt = m.get('ActiveTimeGMT')

        if m.get('ActivityId') is not None:
            self.activity_id = m.get('ActivityId')

        if m.get('ActualActionerId') is not None:
            self.actual_actioner_id = m.get('ActualActionerId')

        if m.get('CreateTimeGMT') is not None:
            self.create_time_gmt = m.get('CreateTimeGMT')

        if m.get('FinishTimeGMT') is not None:
            self.finish_time_gmt = m.get('FinishTimeGMT')

        if m.get('OriginatorId') is not None:
            self.originator_id = m.get('OriginatorId')

        if m.get('ProcessInstanceId') is not None:
            self.process_instance_id = m.get('ProcessInstanceId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('TitleInEnglish') is not None:
            self.title_in_english = m.get('TitleInEnglish')

        return self

