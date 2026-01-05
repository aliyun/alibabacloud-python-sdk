# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeApplicationsResponseBody(DaraModel):
    def __init__(
        self,
        items: main_models.DescribeApplicationsResponseBodyItems = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        self.items = items
        self.page_number = page_number
        self.page_record_count = page_record_count
        self.request_id = request_id
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.items is not None:
            result['Items'] = self.items.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Items') is not None:
            temp_model = main_models.DescribeApplicationsResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeApplicationsResponseBodyItems(DaraModel):
    def __init__(
        self,
        applications: List[main_models.DescribeApplicationsResponseBodyItemsApplications] = None,
    ):
        self.applications = applications

    def validate(self):
        if self.applications:
            for v1 in self.applications:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Applications'] = []
        if self.applications is not None:
            for k1 in self.applications:
                result['Applications'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.applications = []
        if m.get('Applications') is not None:
            for k1 in m.get('Applications'):
                temp_model = main_models.DescribeApplicationsResponseBodyItemsApplications()
                self.applications.append(temp_model.from_map(k1))

        return self

class DescribeApplicationsResponseBodyItemsApplications(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        application_type: str = None,
        creation_time: str = None,
        dbcluster_id: str = None,
        description: str = None,
        endpoints: main_models.DescribeApplicationsResponseBodyItemsApplicationsEndpoints = None,
        engine_version: str = None,
        expire_time: str = None,
        expired: str = None,
        pay_type: str = None,
        polar_fsinstance_id: str = None,
        region_id: str = None,
        status: str = None,
        zone_id: str = None,
    ):
        self.application_id = application_id
        self.application_type = application_type
        self.creation_time = creation_time
        self.dbcluster_id = dbcluster_id
        self.description = description
        self.endpoints = endpoints
        self.engine_version = engine_version
        self.expire_time = expire_time
        self.expired = expired
        self.pay_type = pay_type
        self.polar_fsinstance_id = polar_fsinstance_id
        self.region_id = region_id
        self.status = status
        self.zone_id = zone_id

    def validate(self):
        if self.endpoints:
            self.endpoints.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.application_type is not None:
            result['ApplicationType'] = self.application_type

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.description is not None:
            result['Description'] = self.description

        if self.endpoints is not None:
            result['Endpoints'] = self.endpoints.to_map()

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.expired is not None:
            result['Expired'] = self.expired

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.polar_fsinstance_id is not None:
            result['PolarFSInstanceId'] = self.polar_fsinstance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Endpoints') is not None:
            temp_model = main_models.DescribeApplicationsResponseBodyItemsApplicationsEndpoints()
            self.endpoints = temp_model.from_map(m.get('Endpoints'))

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('Expired') is not None:
            self.expired = m.get('Expired')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('PolarFSInstanceId') is not None:
            self.polar_fsinstance_id = m.get('PolarFSInstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeApplicationsResponseBodyItemsApplicationsEndpoints(DaraModel):
    def __init__(
        self,
        endpoint: List[main_models.DescribeApplicationsResponseBodyItemsApplicationsEndpointsEndpoint] = None,
    ):
        self.endpoint = endpoint

    def validate(self):
        if self.endpoint:
            for v1 in self.endpoint:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['endpoint'] = []
        if self.endpoint is not None:
            for k1 in self.endpoint:
                result['endpoint'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.endpoint = []
        if m.get('endpoint') is not None:
            for k1 in m.get('endpoint'):
                temp_model = main_models.DescribeApplicationsResponseBodyItemsApplicationsEndpointsEndpoint()
                self.endpoint.append(temp_model.from_map(k1))

        return self

class DescribeApplicationsResponseBodyItemsApplicationsEndpointsEndpoint(DaraModel):
    def __init__(
        self,
        ip: str = None,
        net_type: str = None,
        port: str = None,
    ):
        self.ip = ip
        self.net_type = net_type
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip is not None:
            result['IP'] = self.ip

        if self.net_type is not None:
            result['NetType'] = self.net_type

        if self.port is not None:
            result['Port'] = self.port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IP') is not None:
            self.ip = m.get('IP')

        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        return self

