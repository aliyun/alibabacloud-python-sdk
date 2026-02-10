# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeCommonTargetResultListResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        target_config: main_models.DescribeCommonTargetResultListResponseBodyTargetConfig = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The information about the configuration item.
        self.target_config = target_config

    def validate(self):
        if self.target_config:
            self.target_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.target_config is not None:
            result['TargetConfig'] = self.target_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TargetConfig') is not None:
            temp_model = main_models.DescribeCommonTargetResultListResponseBodyTargetConfig()
            self.target_config = temp_model.from_map(m.get('TargetConfig'))

        return self

class DescribeCommonTargetResultListResponseBodyTargetConfig(DaraModel):
    def __init__(
        self,
        flag: str = None,
        target_default: str = None,
        target_list: List[str] = None,
        target_type: str = None,
        total_count: str = None,
        type: str = None,
    ):
        # The identifier that indicates whether the configuration item is applied to the server. Valid values:
        # 
        # *   **add**: applied
        # *   **del**: not applied
        self.flag = flag
        # The default identifier.
        self.target_default = target_default
        # An array that consists of the IDs of the server groups or the UUIDs of the servers.
        # 
        # >  If **uuid** is returned for the **TargetType** parameter, **UUIDs** of the servers are returned. If **groupId** is returned for the **TargetType** parameter, IDs of the server groups are returned.
        self.target_list = target_list
        # The type of the server to which the configuration item is applied. Valid values:
        # 
        # *   **uuid**: a server
        # *   **groupId**: a server group
        self.target_type = target_type
        # The total number of entries returned.
        self.total_count = total_count
        # The type of the configuration item. Valid values:
        # 
        # *   **webshell_timescan**: webshell detection and removal
        # *   **aliscriptengine**: in-depth detection engine
        # *   **alidetect**: installation scope of local file detection
        # *   **alidetect-scan-enable**: detection scope of local file detection
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.flag is not None:
            result['Flag'] = self.flag

        if self.target_default is not None:
            result['TargetDefault'] = self.target_default

        if self.target_list is not None:
            result['TargetList'] = self.target_list

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Flag') is not None:
            self.flag = m.get('Flag')

        if m.get('TargetDefault') is not None:
            self.target_default = m.get('TargetDefault')

        if m.get('TargetList') is not None:
            self.target_list = m.get('TargetList')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

