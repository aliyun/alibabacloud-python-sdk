# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeLoginBaseConfigsResponseBody(DaraModel):
    def __init__(
        self,
        base_configs: List[main_models.DescribeLoginBaseConfigsResponseBodyBaseConfigs] = None,
        current_page: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The description of the configuration.
        self.base_configs = base_configs
        # The page number of the returned page.
        self.current_page = current_page
        # The number of entries returned per page. Default value: **20**.
        self.page_size = page_size
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.base_configs:
            for v1 in self.base_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BaseConfigs'] = []
        if self.base_configs is not None:
            for k1 in self.base_configs:
                result['BaseConfigs'].append(k1.to_map() if k1 else None)

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.base_configs = []
        if m.get('BaseConfigs') is not None:
            for k1 in m.get('BaseConfigs'):
                temp_model = main_models.DescribeLoginBaseConfigsResponseBodyBaseConfigs()
                self.base_configs.append(temp_model.from_map(k1))

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeLoginBaseConfigsResponseBodyBaseConfigs(DaraModel):
    def __init__(
        self,
        account: str = None,
        end_time: str = None,
        ip: str = None,
        location: str = None,
        remark: str = None,
        start_time: str = None,
        target_list: List[main_models.DescribeLoginBaseConfigsResponseBodyBaseConfigsTargetList] = None,
        total_count: int = None,
        uuid_count: int = None,
    ):
        # The common logon account.
        self.account = account
        # The end time of the common logon time range.
        self.end_time = end_time
        # The common logon IP address.
        self.ip = ip
        # The common logon location.
        self.location = location
        # Corresponding configuration remark information.
        self.remark = remark
        # The start time of the common logon time range.
        self.start_time = start_time
        # The details of the servers to which the configuration is applied.
        self.target_list = target_list
        # The total number of servers.
        self.total_count = total_count
        # The number of servers to which the configuration is applied.
        self.uuid_count = uuid_count

    def validate(self):
        if self.target_list:
            for v1 in self.target_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account is not None:
            result['Account'] = self.account

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.location is not None:
            result['Location'] = self.location

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        result['TargetList'] = []
        if self.target_list is not None:
            for k1 in self.target_list:
                result['TargetList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.uuid_count is not None:
            result['UuidCount'] = self.uuid_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('Location') is not None:
            self.location = m.get('Location')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        self.target_list = []
        if m.get('TargetList') is not None:
            for k1 in m.get('TargetList'):
                temp_model = main_models.DescribeLoginBaseConfigsResponseBodyBaseConfigsTargetList()
                self.target_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('UuidCount') is not None:
            self.uuid_count = m.get('UuidCount')

        return self

class DescribeLoginBaseConfigsResponseBodyBaseConfigsTargetList(DaraModel):
    def __init__(
        self,
        target: str = None,
        target_type: str = None,
    ):
        # The UUID or group ID of the server.
        self.target = target
        # The type of the server to which the configuration is applied. Valid values:
        # 
        # *   **uuid**: a server
        # *   **groupId**: a server group
        # *   **global**: all servers
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.target is not None:
            result['Target'] = self.target

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Target') is not None:
            self.target = m.get('Target')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

