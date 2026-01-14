# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class ListApplicationMonitorDetectResultResponseBody(DaraModel):
    def __init__(
        self,
        application_monitor_detect_result_list: List[main_models.ListApplicationMonitorDetectResultResponseBodyApplicationMonitorDetectResultList] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Details about the diagnostic result of the origin probing task.
        self.application_monitor_detect_result_list = application_monitor_detect_result_list
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.application_monitor_detect_result_list:
            for v1 in self.application_monitor_detect_result_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ApplicationMonitorDetectResultList'] = []
        if self.application_monitor_detect_result_list is not None:
            for k1 in self.application_monitor_detect_result_list:
                result['ApplicationMonitorDetectResultList'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.application_monitor_detect_result_list = []
        if m.get('ApplicationMonitorDetectResultList') is not None:
            for k1 in m.get('ApplicationMonitorDetectResultList'):
                temp_model = main_models.ListApplicationMonitorDetectResultResponseBodyApplicationMonitorDetectResultList()
                self.application_monitor_detect_result_list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListApplicationMonitorDetectResultResponseBodyApplicationMonitorDetectResultList(DaraModel):
    def __init__(
        self,
        accelerator_id: str = None,
        content: str = None,
        detail: str = None,
        detect_time: str = None,
        diag_status: str = None,
        listener_id: str = None,
        port: str = None,
        protocol: str = None,
        status_code: str = None,
        task_id: str = None,
    ):
        # The ID of the GA instance on which the origin probing task runs.
        self.accelerator_id = accelerator_id
        # The response content returned by the origin probing task.
        self.content = content
        # The description of the diagnostic result. Valid values:
        # 
        # *   **All forward nodes work well.:** The origin server is normal.
        # *   **Endpoint network error.:** The origin server is abnormal. You must check whether the origin server is running as expected.
        # *   **Public network error.:** An Internet error occurred, which is a network error that occurred when the client connected to the acceleration region.
        # *   **Ga internal error.:** An internal error occurred. For example, an exception occurred when GA processed a request.
        # *   **Ga has been deleted.:** The current GA instance is deleted.
        # *   **Ga state is not stable.:** The current GA instance is in an unstable state, such as the Configuring state.
        # *   **Ga has no listener configuration.:** No listener is configured for the current GA instance.
        # *   **Missing endpoint configuration.:** No endpoint is configured.
        # *   **Missing acceleration region configuration.:** No acceleration region is configured.
        # *   **Missing endpointgroup configuration.:** No endpoint group is configured.
        self.detail = detail
        # The time when the diagnosis of the origin probing task ends.
        self.detect_time = detect_time
        # The diagnostic result of the origin probing task. Valid values:
        # 
        # *   **success:** The origin probing task succeeded.
        # *   **failed:** The origin probing task failed.
        self.diag_status = diag_status
        # The ID of the listener on which the origin probing task runs.
        self.listener_id = listener_id
        # The listener port.
        self.port = port
        # The network transmission protocol that is used by the listener. Valid values:
        # 
        # *   **tcp:** TCP.
        # *   **udp:** UDP.
        # *   **http:** HTTP.
        # *   **https:** HTTPS.
        # 
        # >  UDP listeners do not support probing.
        self.protocol = protocol
        # The error code returned by the origin probing task.
        self.status_code = status_code
        # The origin probing task ID.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id

        if self.content is not None:
            result['Content'] = self.content

        if self.detail is not None:
            result['Detail'] = self.detail

        if self.detect_time is not None:
            result['DetectTime'] = self.detect_time

        if self.diag_status is not None:
            result['DiagStatus'] = self.diag_status

        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id

        if self.port is not None:
            result['Port'] = self.port

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.status_code is not None:
            result['StatusCode'] = self.status_code

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Detail') is not None:
            self.detail = m.get('Detail')

        if m.get('DetectTime') is not None:
            self.detect_time = m.get('DetectTime')

        if m.get('DiagStatus') is not None:
            self.diag_status = m.get('DiagStatus')

        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

