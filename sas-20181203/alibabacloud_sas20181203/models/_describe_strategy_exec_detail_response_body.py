# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeStrategyExecDetailResponseBody(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        fail_count: int = None,
        failed_ecs_list: List[main_models.DescribeStrategyExecDetailResponseBodyFailedEcsList] = None,
        in_process_count: int = None,
        percent: str = None,
        request_id: str = None,
        source: str = None,
        start_time: str = None,
        success_count: int = None,
    ):
        # The time when the baseline check ends.
        self.end_time = end_time
        # The number of check items that failed to pass the baseline check. This type of check item is considered risk items.
        self.fail_count = fail_count
        # The servers on which risk items were detected.
        self.failed_ecs_list = failed_ecs_list
        # The number of tasks that are **running **based on the baseline check policy.
        self.in_process_count = in_process_count
        # The execution progress of the baseline check policy.
        self.percent = percent
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The type of the baseline check. Valid values:
        # 
        # *   **Schedule**: automatic check that periodically runs
        # *   **Manual**: intermediate check that is manually performed
        self.source = source
        # The time when the baseline check starts.
        self.start_time = start_time
        # The number of check items that **passed** the baseline check.
        self.success_count = success_count

    def validate(self):
        if self.failed_ecs_list:
            for v1 in self.failed_ecs_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.fail_count is not None:
            result['FailCount'] = self.fail_count

        result['FailedEcsList'] = []
        if self.failed_ecs_list is not None:
            for k1 in self.failed_ecs_list:
                result['FailedEcsList'].append(k1.to_map() if k1 else None)

        if self.in_process_count is not None:
            result['InProcessCount'] = self.in_process_count

        if self.percent is not None:
            result['Percent'] = self.percent

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.source is not None:
            result['Source'] = self.source

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.success_count is not None:
            result['SuccessCount'] = self.success_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('FailCount') is not None:
            self.fail_count = m.get('FailCount')

        self.failed_ecs_list = []
        if m.get('FailedEcsList') is not None:
            for k1 in m.get('FailedEcsList'):
                temp_model = main_models.DescribeStrategyExecDetailResponseBodyFailedEcsList()
                self.failed_ecs_list.append(temp_model.from_map(k1))

        if m.get('InProcessCount') is not None:
            self.in_process_count = m.get('InProcessCount')

        if m.get('Percent') is not None:
            self.percent = m.get('Percent')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')

        return self

class DescribeStrategyExecDetailResponseBodyFailedEcsList(DaraModel):
    def __init__(
        self,
        ip: str = None,
        instance_name: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        reason: str = None,
    ):
        # The IP address of the server on which the baseline check was performed.
        self.ip = ip
        # The name of the instance.
        self.instance_name = instance_name
        # The public IP address.
        self.internet_ip = internet_ip
        # The private IP address.
        self.intranet_ip = intranet_ip
        # The failure cause for the check item.
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip is not None:
            result['IP'] = self.ip

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip

        if self.reason is not None:
            result['Reason'] = self.reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IP') is not None:
            self.ip = m.get('IP')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        return self

