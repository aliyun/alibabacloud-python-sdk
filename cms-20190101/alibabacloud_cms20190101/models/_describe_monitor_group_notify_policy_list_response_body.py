# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeMonitorGroupNotifyPolicyListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        notify_policy_list: main_models.DescribeMonitorGroupNotifyPolicyListResponseBodyNotifyPolicyList = None,
        request_id: str = None,
        success: str = None,
        total: int = None,
    ):
        # The status code.
        # 
        # > The status code 200 indicates that the request was successful.
        self.code = code
        # The error message.
        self.message = message
        # The returned policies.
        self.notify_policy_list = notify_policy_list
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.notify_policy_list:
            self.notify_policy_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.notify_policy_list is not None:
            result['NotifyPolicyList'] = self.notify_policy_list.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NotifyPolicyList') is not None:
            temp_model = main_models.DescribeMonitorGroupNotifyPolicyListResponseBodyNotifyPolicyList()
            self.notify_policy_list = temp_model.from_map(m.get('NotifyPolicyList'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeMonitorGroupNotifyPolicyListResponseBodyNotifyPolicyList(DaraModel):
    def __init__(
        self,
        notify_policy: List[main_models.DescribeMonitorGroupNotifyPolicyListResponseBodyNotifyPolicyListNotifyPolicy] = None,
    ):
        self.notify_policy = notify_policy

    def validate(self):
        if self.notify_policy:
            for v1 in self.notify_policy:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NotifyPolicy'] = []
        if self.notify_policy is not None:
            for k1 in self.notify_policy:
                result['NotifyPolicy'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.notify_policy = []
        if m.get('NotifyPolicy') is not None:
            for k1 in m.get('NotifyPolicy'):
                temp_model = main_models.DescribeMonitorGroupNotifyPolicyListResponseBodyNotifyPolicyListNotifyPolicy()
                self.notify_policy.append(temp_model.from_map(k1))

        return self

class DescribeMonitorGroupNotifyPolicyListResponseBodyNotifyPolicyListNotifyPolicy(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        group_id: str = None,
        id: str = None,
        start_time: int = None,
        type: str = None,
    ):
        # The end of the time range to query.
        # 
        # Unit: milliseconds.
        self.end_time = end_time
        # The ID of the application group.
        self.group_id = group_id
        # The policy ID.
        self.id = id
        # The beginning of the time range to query.
        # 
        # Unit: milliseconds.
        self.start_time = start_time
        # The policy type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.id is not None:
            result['Id'] = self.id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

