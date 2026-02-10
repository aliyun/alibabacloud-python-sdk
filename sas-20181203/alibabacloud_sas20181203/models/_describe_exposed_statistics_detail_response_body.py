# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeExposedStatisticsDetailResponseBody(DaraModel):
    def __init__(
        self,
        page_info: main_models.DescribeExposedStatisticsDetailResponseBodyPageInfo = None,
        request_id: str = None,
        statistics_details: List[main_models.DescribeExposedStatisticsDetailResponseBodyStatisticsDetails] = None,
    ):
        # The pagination information.
        self.page_info = page_info
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # An array consisting of the gateway assets, ports, system components, or public IP addresses that are exposed on the Internet and are returned.
        self.statistics_details = statistics_details

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.statistics_details:
            for v1 in self.statistics_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['StatisticsDetails'] = []
        if self.statistics_details is not None:
            for k1 in self.statistics_details:
                result['StatisticsDetails'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = main_models.DescribeExposedStatisticsDetailResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.statistics_details = []
        if m.get('StatisticsDetails') is not None:
            for k1 in m.get('StatisticsDetails'):
                temp_model = main_models.DescribeExposedStatisticsDetailResponseBodyStatisticsDetails()
                self.statistics_details.append(temp_model.from_map(k1))

        return self

class DescribeExposedStatisticsDetailResponseBodyStatisticsDetails(DaraModel):
    def __init__(
        self,
        exposed_count: int = None,
        exposure_component: str = None,
        exposure_ip: str = None,
        exposure_port: str = None,
        exposure_type: str = None,
        exposure_type_id: str = None,
        exposure_type_instance_name: str = None,
        forward_port: str = None,
        region_id: str = None,
    ):
        # The total number of system vulnerabilities that are detected on your server and are exposed on the Internet.
        self.exposed_count = exposed_count
        # The system component that is exposed on the Internet.
        self.exposure_component = exposure_component
        # The public IP address that is exposed on the Internet.
        self.exposure_ip = exposure_ip
        # The port that is exposed on the Internet.
        self.exposure_port = exposure_port
        # The resource from which the asset is exposed. Valid values:
        # 
        # *   **INTERNET_IP**: the IP address of the Elastic Compute Service (ECS) instance
        # *   **SLB**: the public IP address of the SLB instance
        # *   **EIP**: the elastic IP address (EIP)
        # *   **DNAT**: the NAT gateway that connects to the Internet by using the DNAT feature
        self.exposure_type = exposure_type
        # The ID of the instance to which the resource belongs. The valid values of this parameter vary based on the value of the ExposureType parameter.
        # 
        # *   If the value of the **ExposureType** parameter is **INTERNET_IP**, the value of this parameter is an empty string.
        # *   If the value of the **ExposureType** parameter is **SLB**, the value of this parameter is the ID of the Internet-facing SLB instance.
        # *   If the value of the **ExposureType** parameter is **EIP**, the value of this parameter is the ID of the EIP.
        # *   If the value of the **ExposureType** parameter is **DNAT**, the value of this parameter is the ID of the NAT gateway.
        self.exposure_type_id = exposure_type_id
        # The name of the gateway asset that is exposed on the Internet.
        self.exposure_type_instance_name = exposure_type_instance_name
        # The listener port that is used to redirect HTTP requests.
        self.forward_port = forward_port
        # The region ID of the asset.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exposed_count is not None:
            result['ExposedCount'] = self.exposed_count

        if self.exposure_component is not None:
            result['ExposureComponent'] = self.exposure_component

        if self.exposure_ip is not None:
            result['ExposureIp'] = self.exposure_ip

        if self.exposure_port is not None:
            result['ExposurePort'] = self.exposure_port

        if self.exposure_type is not None:
            result['ExposureType'] = self.exposure_type

        if self.exposure_type_id is not None:
            result['ExposureTypeId'] = self.exposure_type_id

        if self.exposure_type_instance_name is not None:
            result['ExposureTypeInstanceName'] = self.exposure_type_instance_name

        if self.forward_port is not None:
            result['ForwardPort'] = self.forward_port

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExposedCount') is not None:
            self.exposed_count = m.get('ExposedCount')

        if m.get('ExposureComponent') is not None:
            self.exposure_component = m.get('ExposureComponent')

        if m.get('ExposureIp') is not None:
            self.exposure_ip = m.get('ExposureIp')

        if m.get('ExposurePort') is not None:
            self.exposure_port = m.get('ExposurePort')

        if m.get('ExposureType') is not None:
            self.exposure_type = m.get('ExposureType')

        if m.get('ExposureTypeId') is not None:
            self.exposure_type_id = m.get('ExposureTypeId')

        if m.get('ExposureTypeInstanceName') is not None:
            self.exposure_type_instance_name = m.get('ExposureTypeInstanceName')

        if m.get('ForwardPort') is not None:
            self.forward_port = m.get('ForwardPort')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class DescribeExposedStatisticsDetailResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of entries returned on the current page.
        self.count = count
        # The page number of the returned page.
        self.current_page = current_page
        # The number of entries returned per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

