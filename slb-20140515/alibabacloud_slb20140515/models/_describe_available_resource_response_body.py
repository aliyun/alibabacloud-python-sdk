# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_slb20140515 import models as main_models
from darabonba.model import DaraModel

class DescribeAvailableResourceResponseBody(DaraModel):
    def __init__(
        self,
        available_resources: main_models.DescribeAvailableResourceResponseBodyAvailableResources = None,
        request_id: str = None,
    ):
        # The zones and the supported resources.
        self.available_resources = available_resources
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.available_resources:
            self.available_resources.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_resources is not None:
            result['AvailableResources'] = self.available_resources.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableResources') is not None:
            temp_model = main_models.DescribeAvailableResourceResponseBodyAvailableResources()
            self.available_resources = temp_model.from_map(m.get('AvailableResources'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeAvailableResourceResponseBodyAvailableResources(DaraModel):
    def __init__(
        self,
        available_resource: List[main_models.DescribeAvailableResourceResponseBodyAvailableResourcesAvailableResource] = None,
    ):
        self.available_resource = available_resource

    def validate(self):
        if self.available_resource:
            for v1 in self.available_resource:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AvailableResource'] = []
        if self.available_resource is not None:
            for k1 in self.available_resource:
                result['AvailableResource'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.available_resource = []
        if m.get('AvailableResource') is not None:
            for k1 in m.get('AvailableResource'):
                temp_model = main_models.DescribeAvailableResourceResponseBodyAvailableResourcesAvailableResource()
                self.available_resource.append(temp_model.from_map(k1))

        return self

class DescribeAvailableResourceResponseBodyAvailableResourcesAvailableResource(DaraModel):
    def __init__(
        self,
        master_zone_id: str = None,
        slave_zone_id: str = None,
        support_resources: main_models.DescribeAvailableResourceResponseBodyAvailableResourcesAvailableResourceSupportResources = None,
    ):
        # The primary zone.
        self.master_zone_id = master_zone_id
        # The secondary zone.
        self.slave_zone_id = slave_zone_id
        # The supported resources.
        self.support_resources = support_resources

    def validate(self):
        if self.support_resources:
            self.support_resources.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.master_zone_id is not None:
            result['MasterZoneId'] = self.master_zone_id

        if self.slave_zone_id is not None:
            result['SlaveZoneId'] = self.slave_zone_id

        if self.support_resources is not None:
            result['SupportResources'] = self.support_resources.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MasterZoneId') is not None:
            self.master_zone_id = m.get('MasterZoneId')

        if m.get('SlaveZoneId') is not None:
            self.slave_zone_id = m.get('SlaveZoneId')

        if m.get('SupportResources') is not None:
            temp_model = main_models.DescribeAvailableResourceResponseBodyAvailableResourcesAvailableResourceSupportResources()
            self.support_resources = temp_model.from_map(m.get('SupportResources'))

        return self

class DescribeAvailableResourceResponseBodyAvailableResourcesAvailableResourceSupportResources(DaraModel):
    def __init__(
        self,
        support_resource: List[main_models.DescribeAvailableResourceResponseBodyAvailableResourcesAvailableResourceSupportResourcesSupportResource] = None,
    ):
        self.support_resource = support_resource

    def validate(self):
        if self.support_resource:
            for v1 in self.support_resource:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SupportResource'] = []
        if self.support_resource is not None:
            for k1 in self.support_resource:
                result['SupportResource'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.support_resource = []
        if m.get('SupportResource') is not None:
            for k1 in m.get('SupportResource'):
                temp_model = main_models.DescribeAvailableResourceResponseBodyAvailableResourcesAvailableResourceSupportResourcesSupportResource()
                self.support_resource.append(temp_model.from_map(k1))

        return self

class DescribeAvailableResourceResponseBodyAvailableResourcesAvailableResourceSupportResourcesSupportResource(DaraModel):
    def __init__(
        self,
        address_ipversion: str = None,
        address_type: str = None,
    ):
        # The type of the IP address.
        # 
        # Valid values: **ipv4 and ipv6**.
        self.address_ipversion = address_ipversion
        # The network type.
        # 
        # Valid values: **vpc, classic-internet, and classic-intranet**.
        self.address_type = address_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address_ipversion is not None:
            result['AddressIPVersion'] = self.address_ipversion

        if self.address_type is not None:
            result['AddressType'] = self.address_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressIPVersion') is not None:
            self.address_ipversion = m.get('AddressIPVersion')

        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')

        return self

