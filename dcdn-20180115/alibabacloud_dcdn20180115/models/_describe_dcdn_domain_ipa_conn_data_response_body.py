# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dcdn20180115 import models as main_models
from darabonba.model import DaraModel

class DescribeDcdnDomainIpaConnDataResponseBody(DaraModel):
    def __init__(
        self,
        connection_data_per_interval: main_models.DescribeDcdnDomainIpaConnDataResponseBodyConnectionDataPerInterval = None,
        end_time: str = None,
        request_id: str = None,
        start_time: str = None,
    ):
        # The number of user connections at each time interval.
        self.connection_data_per_interval = connection_data_per_interval
        # The end of the time range during which data was queried.
        self.end_time = end_time
        # The request ID.
        self.request_id = request_id
        # The beginning of the time range during which data was queried.
        self.start_time = start_time

    def validate(self):
        if self.connection_data_per_interval:
            self.connection_data_per_interval.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_data_per_interval is not None:
            result['ConnectionDataPerInterval'] = self.connection_data_per_interval.to_map()

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionDataPerInterval') is not None:
            temp_model = main_models.DescribeDcdnDomainIpaConnDataResponseBodyConnectionDataPerInterval()
            self.connection_data_per_interval = temp_model.from_map(m.get('ConnectionDataPerInterval'))

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class DescribeDcdnDomainIpaConnDataResponseBodyConnectionDataPerInterval(DaraModel):
    def __init__(
        self,
        data_module: List[main_models.DescribeDcdnDomainIpaConnDataResponseBodyConnectionDataPerIntervalDataModule] = None,
    ):
        self.data_module = data_module

    def validate(self):
        if self.data_module:
            for v1 in self.data_module:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataModule'] = []
        if self.data_module is not None:
            for k1 in self.data_module:
                result['DataModule'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k1 in m.get('DataModule'):
                temp_model = main_models.DescribeDcdnDomainIpaConnDataResponseBodyConnectionDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k1))

        return self

class DescribeDcdnDomainIpaConnDataResponseBodyConnectionDataPerIntervalDataModule(DaraModel):
    def __init__(
        self,
        connections: int = None,
        domain: str = None,
        time_stamp: str = None,
    ):
        # The number of IPA user connections.
        self.connections = connections
        # The accelerated domain name.
        self.domain = domain
        # The timestamp of the data returned.
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connections is not None:
            result['Connections'] = self.connections

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Connections') is not None:
            self.connections = m.get('Connections')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        return self

