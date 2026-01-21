# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeUnhealthyHostAvailabilityResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        unhealthy_list: main_models.DescribeUnhealthyHostAvailabilityResponseBodyUnhealthyList = None,
    ):
        # The status code.
        # 
        # >  The status code 200 indicates that the request was successful.
        self.code = code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success
        # The unhealthy instances that are detected by the specified availability monitoring tasks.
        self.unhealthy_list = unhealthy_list

    def validate(self):
        if self.unhealthy_list:
            self.unhealthy_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.unhealthy_list is not None:
            result['UnhealthyList'] = self.unhealthy_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('UnhealthyList') is not None:
            temp_model = main_models.DescribeUnhealthyHostAvailabilityResponseBodyUnhealthyList()
            self.unhealthy_list = temp_model.from_map(m.get('UnhealthyList'))

        return self

class DescribeUnhealthyHostAvailabilityResponseBodyUnhealthyList(DaraModel):
    def __init__(
        self,
        node_task_instance: List[main_models.DescribeUnhealthyHostAvailabilityResponseBodyUnhealthyListNodeTaskInstance] = None,
    ):
        self.node_task_instance = node_task_instance

    def validate(self):
        if self.node_task_instance:
            for v1 in self.node_task_instance:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NodeTaskInstance'] = []
        if self.node_task_instance is not None:
            for k1 in self.node_task_instance:
                result['NodeTaskInstance'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.node_task_instance = []
        if m.get('NodeTaskInstance') is not None:
            for k1 in m.get('NodeTaskInstance'):
                temp_model = main_models.DescribeUnhealthyHostAvailabilityResponseBodyUnhealthyListNodeTaskInstance()
                self.node_task_instance.append(temp_model.from_map(k1))

        return self

class DescribeUnhealthyHostAvailabilityResponseBodyUnhealthyListNodeTaskInstance(DaraModel):
    def __init__(
        self,
        id: int = None,
        instance_list: main_models.DescribeUnhealthyHostAvailabilityResponseBodyUnhealthyListNodeTaskInstanceInstanceList = None,
    ):
        # The ID of the availability monitoring task.
        self.id = id
        self.instance_list = instance_list

    def validate(self):
        if self.instance_list:
            self.instance_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.instance_list is not None:
            result['InstanceList'] = self.instance_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceList') is not None:
            temp_model = main_models.DescribeUnhealthyHostAvailabilityResponseBodyUnhealthyListNodeTaskInstanceInstanceList()
            self.instance_list = temp_model.from_map(m.get('InstanceList'))

        return self

class DescribeUnhealthyHostAvailabilityResponseBodyUnhealthyListNodeTaskInstanceInstanceList(DaraModel):
    def __init__(
        self,
        string: List[str] = None,
    ):
        self.string = string

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.string is not None:
            result['String'] = self.string

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('String') is not None:
            self.string = m.get('String')

        return self

