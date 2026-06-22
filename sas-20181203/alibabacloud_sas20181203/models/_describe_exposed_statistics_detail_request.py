# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeExposedStatisticsDetailRequest(DaraModel):
    def __init__(
        self,
        criteria: str = None,
        current_page: int = None,
        exposure_ip: str = None,
        instance_id: str = None,
        page_size: int = None,
        resource_directory_account_id: int = None,
        statistics_type: str = None,
        statistics_type_gateway_type: str = None,
        statistics_type_instance_value: str = None,
        uuid: str = None,
    ):
        # The query condition.
        self.criteria = criteria
        # The page number of the current page in a paged query.
        self.current_page = current_page
        # The public IP address that is exposed on the Internet for the asset to query.
        self.exposure_ip = exposure_ip
        # The instance ID of the asset to query.
        self.instance_id = instance_id
        # The maximum number of entries per page in a paged query. Default value: 20. If you leave this parameter empty, 20 entries are returned per page.
        # > Set PageSize to a non-empty value.
        self.page_size = page_size
        # The Alibaba Cloud account ID of the member accounts in the resource folder.
        # > Invoke the [DescribeMonitorAccounts](~~DescribeMonitorAccounts~~) operation to obtain this parameter.
        self.resource_directory_account_id = resource_directory_account_id
        # The type of statistics to query. Valid values:
        # - **exposureType**: gateway assets exposed on the Internet.
        # - **exposurePort**: ports exposed on the Internet.
        # - **exposureComponent**: system components exposed on the Internet.
        # - **exposureIp**: IP addresses exposed on the Internet.
        # 
        # This parameter is required.
        self.statistics_type = statistics_type
        # The Asset Type of the gateway to query. This parameter takes effect only when **StatisticsType** is set to **exposureType**. Valid values:
        # - **SLB**: public IP address of a load balancing SLB instance.
        # - **DNAT**: NAT gateway that uses the DNAT feature to connect to the Internet.
        self.statistics_type_gateway_type = statistics_type_gateway_type
        # The instance ID of the gateway to query. This parameter takes effect only when **StatisticsType** is set to **exposureType**.
        self.statistics_type_instance_value = statistics_type_instance_value
        # The UUID of the server to query.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.criteria is not None:
            result['Criteria'] = self.criteria

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.exposure_ip is not None:
            result['ExposureIp'] = self.exposure_ip

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id

        if self.statistics_type is not None:
            result['StatisticsType'] = self.statistics_type

        if self.statistics_type_gateway_type is not None:
            result['StatisticsTypeGatewayType'] = self.statistics_type_gateway_type

        if self.statistics_type_instance_value is not None:
            result['StatisticsTypeInstanceValue'] = self.statistics_type_instance_value

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Criteria') is not None:
            self.criteria = m.get('Criteria')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('ExposureIp') is not None:
            self.exposure_ip = m.get('ExposureIp')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')

        if m.get('StatisticsType') is not None:
            self.statistics_type = m.get('StatisticsType')

        if m.get('StatisticsTypeGatewayType') is not None:
            self.statistics_type_gateway_type = m.get('StatisticsTypeGatewayType')

        if m.get('StatisticsTypeInstanceValue') is not None:
            self.statistics_type_instance_value = m.get('StatisticsTypeInstanceValue')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

