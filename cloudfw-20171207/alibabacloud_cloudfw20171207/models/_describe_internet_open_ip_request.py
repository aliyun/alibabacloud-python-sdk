# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeInternetOpenIpRequest(DaraModel):
    def __init__(
        self,
        assets_instance_id: str = None,
        assets_instance_name: str = None,
        assets_type: str = None,
        current_page: str = None,
        end_time: str = None,
        lang: str = None,
        page_size: str = None,
        port: str = None,
        public_ip: str = None,
        region_no: str = None,
        risk_level: str = None,
        service_name: str = None,
        start_time: str = None,
    ):
        # The instance ID.
        self.assets_instance_id = assets_instance_id
        # The instance name.
        self.assets_instance_name = assets_instance_name
        # The asset type of the instance.
        self.assets_type = assets_type
        # The page number.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The end of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        self.end_time = end_time
        # The language of the content within the response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # The number of entries per page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The port number.
        self.port = port
        # The public IP address of the instance.
        self.public_ip = public_ip
        # The region ID of the instance.
        self.region_no = region_no
        # The risk level. If you leave this parameter empty, all risk levels are queried. Valid values:
        # 
        # *   **3**: high risk
        # *   **2**: medium risk
        # *   **1**: low risk
        # *   **0**: no risk
        self.risk_level = risk_level
        # The application.
        self.service_name = service_name
        # The beginning of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assets_instance_id is not None:
            result['AssetsInstanceId'] = self.assets_instance_id

        if self.assets_instance_name is not None:
            result['AssetsInstanceName'] = self.assets_instance_name

        if self.assets_type is not None:
            result['AssetsType'] = self.assets_type

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.port is not None:
            result['Port'] = self.port

        if self.public_ip is not None:
            result['PublicIp'] = self.public_ip

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetsInstanceId') is not None:
            self.assets_instance_id = m.get('AssetsInstanceId')

        if m.get('AssetsInstanceName') is not None:
            self.assets_instance_name = m.get('AssetsInstanceName')

        if m.get('AssetsType') is not None:
            self.assets_type = m.get('AssetsType')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('PublicIp') is not None:
            self.public_ip = m.get('PublicIp')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

