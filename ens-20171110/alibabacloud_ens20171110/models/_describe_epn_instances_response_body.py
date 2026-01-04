# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeEpnInstancesResponseBody(DaraModel):
    def __init__(
        self,
        epninstances: main_models.DescribeEpnInstancesResponseBodyEPNInstances = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Details of EPN instances.
        self.epninstances = epninstances
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of pages returned.
        self.total_count = total_count

    def validate(self):
        if self.epninstances:
            self.epninstances.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.epninstances is not None:
            result['EPNInstances'] = self.epninstances.to_map()

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
        if m.get('EPNInstances') is not None:
            temp_model = main_models.DescribeEpnInstancesResponseBodyEPNInstances()
            self.epninstances = temp_model.from_map(m.get('EPNInstances'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeEpnInstancesResponseBodyEPNInstances(DaraModel):
    def __init__(
        self,
        epninstance: List[main_models.DescribeEpnInstancesResponseBodyEPNInstancesEPNInstance] = None,
    ):
        self.epninstance = epninstance

    def validate(self):
        if self.epninstance:
            for v1 in self.epninstance:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EPNInstance'] = []
        if self.epninstance is not None:
            for k1 in self.epninstance:
                result['EPNInstance'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.epninstance = []
        if m.get('EPNInstance') is not None:
            for k1 in m.get('EPNInstance'):
                temp_model = main_models.DescribeEpnInstancesResponseBodyEPNInstancesEPNInstance()
                self.epninstance.append(temp_model.from_map(k1))

        return self

class DescribeEpnInstancesResponseBodyEPNInstancesEPNInstance(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        epninstance_id: str = None,
        epninstance_name: str = None,
        epninstance_type: str = None,
        end_time: str = None,
        internet_max_bandwidth_out: int = None,
        modify_time: str = None,
        networking_model: str = None,
        start_time: str = None,
        status: str = None,
    ):
        # The time when the instance was created. The time is displayed in UTC.
        self.creation_time = creation_time
        # The ID of the EPN instance.
        self.epninstance_id = epninstance_id
        # The name of the EPN instance.
        self.epninstance_name = epninstance_name
        # Set the value to EdgeToEdge.
        self.epninstance_type = epninstance_type
        # The end of the time range during which the data was queried. The time is displayed in UTC.
        self.end_time = end_time
        # The inbound bandwidth. Unit: Mbit/s.
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        # The time when the instance was last modified. The time is displayed in UTC.
        self.modify_time = modify_time
        # The networking mode. Valid values:
        # 
        # *   SpeedUp: intelligent acceleration network (Internet)
        # *   Connection: internal network
        # *   SpeedUpAndConnection: intelligent acceleration network and internal network
        self.networking_model = networking_model
        # The beginning of the time range during which the data was queried. The time is displayed in UTC.
        self.start_time = start_time
        # The status of the instance. Valid values:
        # 
        # *   Running
        # *   Excuting
        # *   Stopped
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.epninstance_id is not None:
            result['EPNInstanceId'] = self.epninstance_id

        if self.epninstance_name is not None:
            result['EPNInstanceName'] = self.epninstance_name

        if self.epninstance_type is not None:
            result['EPNInstanceType'] = self.epninstance_type

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.internet_max_bandwidth_out is not None:
            result['InternetMaxBandwidthOut'] = self.internet_max_bandwidth_out

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.networking_model is not None:
            result['NetworkingModel'] = self.networking_model

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('EPNInstanceId') is not None:
            self.epninstance_id = m.get('EPNInstanceId')

        if m.get('EPNInstanceName') is not None:
            self.epninstance_name = m.get('EPNInstanceName')

        if m.get('EPNInstanceType') is not None:
            self.epninstance_type = m.get('EPNInstanceType')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InternetMaxBandwidthOut') is not None:
            self.internet_max_bandwidth_out = m.get('InternetMaxBandwidthOut')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('NetworkingModel') is not None:
            self.networking_model = m.get('NetworkingModel')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

