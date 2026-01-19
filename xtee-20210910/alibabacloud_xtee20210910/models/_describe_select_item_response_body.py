# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeSelectItemResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_object: main_models.DescribeSelectItemResponseBodyResultObject = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Return object
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_object is not None:
            result['resultObject'] = self.result_object.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('resultObject') is not None:
            temp_model = main_models.DescribeSelectItemResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('resultObject'))

        return self

class DescribeSelectItemResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        monitor_status_list: List[str] = None,
        task_id_list: List[str] = None,
    ):
        # Monitoring status list.
        self.monitor_status_list = monitor_status_list
        # Task ID list.
        self.task_id_list = task_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.monitor_status_list is not None:
            result['monitorStatusList'] = self.monitor_status_list

        if self.task_id_list is not None:
            result['taskIdList'] = self.task_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('monitorStatusList') is not None:
            self.monitor_status_list = m.get('monitorStatusList')

        if m.get('taskIdList') is not None:
            self.task_id_list = m.get('taskIdList')

        return self

