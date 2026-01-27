# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class ListUserApplicationsResponseBody(DaraModel):
    def __init__(
        self,
        applications: List[main_models.ListUserApplicationsResponseBodyApplications] = None,
        request_id: str = None,
        total_num: int = None,
    ):
        self.applications = applications
        # Id of the request
        self.request_id = request_id
        self.total_num = total_num

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_num is not None:
            result['TotalNum'] = self.total_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.applications = []
        if m.get('Applications') is not None:
            for k1 in m.get('Applications'):
                temp_model = main_models.ListUserApplicationsResponseBodyApplications()
                self.applications.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        return self

class ListUserApplicationsResponseBodyApplications(DaraModel):
    def __init__(
        self,
        action: str = None,
        address_groups: List[main_models.AddressGroup] = None,
        addresses: List[str] = None,
        application_id: str = None,
        config_mode: str = None,
        name: str = None,
        port_ranges: List[main_models.ListUserApplicationsResponseBodyApplicationsPortRanges] = None,
        protocol: str = None,
    ):
        self.action = action
        self.address_groups = address_groups
        self.addresses = addresses
        self.application_id = application_id
        self.config_mode = config_mode
        self.name = name
        self.port_ranges = port_ranges
        self.protocol = protocol

    def validate(self):
        if self.address_groups:
            for v1 in self.address_groups:
                 if v1:
                    v1.validate()
        if self.port_ranges:
            for v1 in self.port_ranges:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        result['AddressGroups'] = []
        if self.address_groups is not None:
            for k1 in self.address_groups:
                result['AddressGroups'].append(k1.to_map() if k1 else None)

        if self.addresses is not None:
            result['Addresses'] = self.addresses

        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.config_mode is not None:
            result['ConfigMode'] = self.config_mode

        if self.name is not None:
            result['Name'] = self.name

        result['PortRanges'] = []
        if self.port_ranges is not None:
            for k1 in self.port_ranges:
                result['PortRanges'].append(k1.to_map() if k1 else None)

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        self.address_groups = []
        if m.get('AddressGroups') is not None:
            for k1 in m.get('AddressGroups'):
                temp_model = main_models.AddressGroup()
                self.address_groups.append(temp_model.from_map(k1))

        if m.get('Addresses') is not None:
            self.addresses = m.get('Addresses')

        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ConfigMode') is not None:
            self.config_mode = m.get('ConfigMode')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.port_ranges = []
        if m.get('PortRanges') is not None:
            for k1 in m.get('PortRanges'):
                temp_model = main_models.ListUserApplicationsResponseBodyApplicationsPortRanges()
                self.port_ranges.append(temp_model.from_map(k1))

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        return self

class ListUserApplicationsResponseBodyApplicationsPortRanges(DaraModel):
    def __init__(
        self,
        begin: str = None,
        end: str = None,
    ):
        self.begin = begin
        self.end = end

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin is not None:
            result['Begin'] = self.begin

        if self.end is not None:
            result['End'] = self.end

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')

        if m.get('End') is not None:
            self.end = m.get('End')

        return self

