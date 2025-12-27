# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeDesktopMetadataResponseBody(DaraModel):
    def __init__(
        self,
        desktops: List[main_models.DescribeDesktopMetadataResponseBodyDesktops] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.desktops = desktops
        self.next_token = next_token
        self.request_id = request_id

    def validate(self):
        if self.desktops:
            for v1 in self.desktops:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Desktops'] = []
        if self.desktops is not None:
            for k1 in self.desktops:
                result['Desktops'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.desktops = []
        if m.get('Desktops') is not None:
            for k1 in m.get('Desktops'):
                temp_model = main_models.DescribeDesktopMetadataResponseBodyDesktops()
                self.desktops.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDesktopMetadataResponseBodyDesktops(DaraModel):
    def __init__(
        self,
        charge_type: str = None,
        creation_time: str = None,
        desktop_group_id: str = None,
        desktop_id: str = None,
        desktop_name: str = None,
        desktop_status: str = None,
        desktop_type: str = None,
        expired_time: str = None,
        image_id: str = None,
        local_name: str = None,
        management_flags: List[str] = None,
        member_eni_ip: str = None,
        office_site_id: str = None,
        platform: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_group_name: str = None,
        start_time: str = None,
    ):
        self.charge_type = charge_type
        self.creation_time = creation_time
        self.desktop_group_id = desktop_group_id
        self.desktop_id = desktop_id
        self.desktop_name = desktop_name
        self.desktop_status = desktop_status
        self.desktop_type = desktop_type
        self.expired_time = expired_time
        self.image_id = image_id
        self.local_name = local_name
        self.management_flags = management_flags
        self.member_eni_ip = member_eni_ip
        self.office_site_id = office_site_id
        self.platform = platform
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.resource_group_name = resource_group_name
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id

        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name

        if self.desktop_status is not None:
            result['DesktopStatus'] = self.desktop_status

        if self.desktop_type is not None:
            result['DesktopType'] = self.desktop_type

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.local_name is not None:
            result['LocalName'] = self.local_name

        if self.management_flags is not None:
            result['ManagementFlags'] = self.management_flags

        if self.member_eni_ip is not None:
            result['MemberEniIp'] = self.member_eni_ip

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')

        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')

        if m.get('DesktopStatus') is not None:
            self.desktop_status = m.get('DesktopStatus')

        if m.get('DesktopType') is not None:
            self.desktop_type = m.get('DesktopType')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')

        if m.get('ManagementFlags') is not None:
            self.management_flags = m.get('ManagementFlags')

        if m.get('MemberEniIp') is not None:
            self.member_eni_ip = m.get('MemberEniIp')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

