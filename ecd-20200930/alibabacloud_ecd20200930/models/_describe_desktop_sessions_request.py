# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeDesktopSessionsRequest(DaraModel):
    def __init__(
        self,
        check_os_session: bool = None,
        desktop_id: List[str] = None,
        desktop_name: str = None,
        end_time: str = None,
        end_user_id: str = None,
        end_user_id_filter: str = None,
        fill_hardware_info: bool = None,
        language: str = None,
        office_site_id: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        session_status: str = None,
        start_time: str = None,
        sub_pay_type: str = None,
    ):
        # Specifies whether to turn on the switch to check session status of cloud computers.
        self.check_os_session = check_os_session
        # The IDs of the cloud computers. You can specify the IDs of 1 to 100 cloud computers.
        self.desktop_id = desktop_id
        # The name of the cloud computer.
        self.desktop_name = desktop_name
        # The end of the time range to query.
        self.end_time = end_time
        # The ID of the end user.
        self.end_user_id = end_user_id
        # The user ID. This parameter functions the same as the `EndUserId` parameter. You only need to include one of them in your request.
        self.end_user_id_filter = end_user_id_filter
        self.fill_hardware_info = fill_hardware_info
        self.language = language
        # The office network ID.
        self.office_site_id = office_site_id
        # The page number.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The region ID. You can call the [DescribeRegions](~~DescribeRegions~~) operation to query the regions supported by Elastic Desktop Service (EDS).
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        # The state of the session.
        # 
        # Valid values:
        # 
        # *   Connected
        # *   Disconnected
        self.session_status = session_status
        # The start of the time range to query.
        self.start_time = start_time
        # The billing method of cloud computers.
        # 
        # Valid values:
        # 
        # *   duration: hourly plan (available for users in the whitelist)
        # *   postPaid: pay-as-you-go
        # *   monthPackage: monthly subscription (the 120-hour/250-hour computing plan)
        # *   prePaid: monthly subscription (the Unlimited computing plan)
        self.sub_pay_type = sub_pay_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_os_session is not None:
            result['CheckOsSession'] = self.check_os_session

        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.end_user_id_filter is not None:
            result['EndUserIdFilter'] = self.end_user_id_filter

        if self.fill_hardware_info is not None:
            result['FillHardwareInfo'] = self.fill_hardware_info

        if self.language is not None:
            result['Language'] = self.language

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.session_status is not None:
            result['SessionStatus'] = self.session_status

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.sub_pay_type is not None:
            result['SubPayType'] = self.sub_pay_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckOsSession') is not None:
            self.check_os_session = m.get('CheckOsSession')

        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('EndUserIdFilter') is not None:
            self.end_user_id_filter = m.get('EndUserIdFilter')

        if m.get('FillHardwareInfo') is not None:
            self.fill_hardware_info = m.get('FillHardwareInfo')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SessionStatus') is not None:
            self.session_status = m.get('SessionStatus')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('SubPayType') is not None:
            self.sub_pay_type = m.get('SubPayType')

        return self

