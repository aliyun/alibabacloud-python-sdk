# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class DescribeIpControlsResponseBody(DaraModel):
    def __init__(
        self,
        ip_control_infos: main_models.DescribeIpControlsResponseBodyIpControlInfos = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The information about the ACL. The information is an array that consists of IpControlInfo data. The information does not include specific policies.
        self.ip_control_infos = ip_control_infos
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of returned entries.
        self.total_count = total_count

    def validate(self):
        if self.ip_control_infos:
            self.ip_control_infos.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip_control_infos is not None:
            result['IpControlInfos'] = self.ip_control_infos.to_map()

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
        if m.get('IpControlInfos') is not None:
            temp_model = main_models.DescribeIpControlsResponseBodyIpControlInfos()
            self.ip_control_infos = temp_model.from_map(m.get('IpControlInfos'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeIpControlsResponseBodyIpControlInfos(DaraModel):
    def __init__(
        self,
        ip_control_info: List[main_models.DescribeIpControlsResponseBodyIpControlInfosIpControlInfo] = None,
    ):
        self.ip_control_info = ip_control_info

    def validate(self):
        if self.ip_control_info:
            for v1 in self.ip_control_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['IpControlInfo'] = []
        if self.ip_control_info is not None:
            for k1 in self.ip_control_info:
                result['IpControlInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ip_control_info = []
        if m.get('IpControlInfo') is not None:
            for k1 in m.get('IpControlInfo'):
                temp_model = main_models.DescribeIpControlsResponseBodyIpControlInfosIpControlInfo()
                self.ip_control_info.append(temp_model.from_map(k1))

        return self

class DescribeIpControlsResponseBodyIpControlInfosIpControlInfo(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        ip_control_id: str = None,
        ip_control_name: str = None,
        ip_control_type: str = None,
        modified_time: str = None,
        region_id: str = None,
    ):
        # The time when the ACL was created. The time is displayed in UTC.
        self.create_time = create_time
        # The description of the ACL.
        self.description = description
        # The ID of the ACL.
        self.ip_control_id = ip_control_id
        # The name of the ACL.
        self.ip_control_name = ip_control_name
        # The type of the ACL.
        self.ip_control_type = ip_control_type
        # The time when the ACL was modified. The time is displayed in UTC.
        self.modified_time = modified_time
        # The ID of the region in which the ACL is deployed.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.ip_control_id is not None:
            result['IpControlId'] = self.ip_control_id

        if self.ip_control_name is not None:
            result['IpControlName'] = self.ip_control_name

        if self.ip_control_type is not None:
            result['IpControlType'] = self.ip_control_type

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('IpControlId') is not None:
            self.ip_control_id = m.get('IpControlId')

        if m.get('IpControlName') is not None:
            self.ip_control_name = m.get('IpControlName')

        if m.get('IpControlType') is not None:
            self.ip_control_type = m.get('IpControlType')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

