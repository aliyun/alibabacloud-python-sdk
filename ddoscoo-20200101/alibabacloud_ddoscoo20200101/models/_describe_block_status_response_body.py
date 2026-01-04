# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeBlockStatusResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        status_list: List[main_models.DescribeBlockStatusResponseBodyStatusList] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # An array that consists of details of the Diversion from Origin Server configurations of the instance.
        self.status_list = status_list

    def validate(self):
        if self.status_list:
            for v1 in self.status_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['StatusList'] = []
        if self.status_list is not None:
            for k1 in self.status_list:
                result['StatusList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.status_list = []
        if m.get('StatusList') is not None:
            for k1 in m.get('StatusList'):
                temp_model = main_models.DescribeBlockStatusResponseBodyStatusList()
                self.status_list.append(temp_model.from_map(k1))

        return self

class DescribeBlockStatusResponseBodyStatusList(DaraModel):
    def __init__(
        self,
        block_status_list: List[main_models.DescribeBlockStatusResponseBodyStatusListBlockStatusList] = None,
        ip: str = None,
    ):
        # An array that consists of details of the Diversion from Origin Server configuration.
        self.block_status_list = block_status_list
        # The IP address of the instance.
        self.ip = ip

    def validate(self):
        if self.block_status_list:
            for v1 in self.block_status_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BlockStatusList'] = []
        if self.block_status_list is not None:
            for k1 in self.block_status_list:
                result['BlockStatusList'].append(k1.to_map() if k1 else None)

        if self.ip is not None:
            result['Ip'] = self.ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.block_status_list = []
        if m.get('BlockStatusList') is not None:
            for k1 in m.get('BlockStatusList'):
                temp_model = main_models.DescribeBlockStatusResponseBodyStatusListBlockStatusList()
                self.block_status_list.append(temp_model.from_map(k1))

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        return self

class DescribeBlockStatusResponseBodyStatusListBlockStatusList(DaraModel):
    def __init__(
        self,
        block_status: str = None,
        end_time: int = None,
        line: str = None,
        start_time: int = None,
    ):
        # The blocking status of the network traffic. Valid values:
        # 
        # *   **areablock**: Network traffic is blocked.
        # *   **normal**: Network traffic is not blocked.
        self.block_status = block_status
        # The end time of the blocking. This value is a UNIX timestamp. Unit: seconds.
        self.end_time = end_time
        # The Internet service provider (ISP) line from which the traffic is blocked. Valid values:
        # 
        # *   **ct**: China Telecom (International)
        # *   **cut**: China Unicom (International)
        self.line = line
        # The start time of the blocking. This value is a UNIX timestamp. Unit: seconds.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.block_status is not None:
            result['BlockStatus'] = self.block_status

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.line is not None:
            result['Line'] = self.line

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockStatus') is not None:
            self.block_status = m.get('BlockStatus')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Line') is not None:
            self.line = m.get('Line')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

