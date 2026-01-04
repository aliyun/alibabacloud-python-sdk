# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceSpecResponseBody(DaraModel):
    def __init__(
        self,
        bandwidth_limit: int = None,
        code: int = None,
        data_disk_max_size: int = None,
        data_disk_min_size: int = None,
        instance_specs: main_models.DescribeInstanceSpecResponseBodyInstanceSpecs = None,
        request_id: str = None,
        system_disk_max_size: int = None,
    ):
        # The bandwidth limit for a single instance. Unit: Mbit/s.
        self.bandwidth_limit = bandwidth_limit
        # The returned service code. A value of 0 indicates that the operation was successful.
        self.code = code
        # The maximum capacity of a data disk. Unit: GB.
        self.data_disk_max_size = data_disk_max_size
        # The minimum capacity of a data disk. Unit: GB.
        self.data_disk_min_size = data_disk_min_size
        # The information about instance specifications.
        self.instance_specs = instance_specs
        # The request ID.
        self.request_id = request_id
        # The maximum capacity of the system disk. Unit: GiB.
        self.system_disk_max_size = system_disk_max_size

    def validate(self):
        if self.instance_specs:
            self.instance_specs.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth_limit is not None:
            result['BandwidthLimit'] = self.bandwidth_limit

        if self.code is not None:
            result['Code'] = self.code

        if self.data_disk_max_size is not None:
            result['DataDiskMaxSize'] = self.data_disk_max_size

        if self.data_disk_min_size is not None:
            result['DataDiskMinSize'] = self.data_disk_min_size

        if self.instance_specs is not None:
            result['InstanceSpecs'] = self.instance_specs.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.system_disk_max_size is not None:
            result['SystemDiskMaxSize'] = self.system_disk_max_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandwidthLimit') is not None:
            self.bandwidth_limit = m.get('BandwidthLimit')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('DataDiskMaxSize') is not None:
            self.data_disk_max_size = m.get('DataDiskMaxSize')

        if m.get('DataDiskMinSize') is not None:
            self.data_disk_min_size = m.get('DataDiskMinSize')

        if m.get('InstanceSpecs') is not None:
            temp_model = main_models.DescribeInstanceSpecResponseBodyInstanceSpecs()
            self.instance_specs = temp_model.from_map(m.get('InstanceSpecs'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SystemDiskMaxSize') is not None:
            self.system_disk_max_size = m.get('SystemDiskMaxSize')

        return self

class DescribeInstanceSpecResponseBodyInstanceSpecs(DaraModel):
    def __init__(
        self,
        instance_spec: List[main_models.DescribeInstanceSpecResponseBodyInstanceSpecsInstanceSpec] = None,
    ):
        self.instance_spec = instance_spec

    def validate(self):
        if self.instance_spec:
            for v1 in self.instance_spec:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceSpec'] = []
        if self.instance_spec is not None:
            for k1 in self.instance_spec:
                result['InstanceSpec'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_spec = []
        if m.get('InstanceSpec') is not None:
            for k1 in m.get('InstanceSpec'):
                temp_model = main_models.DescribeInstanceSpecResponseBodyInstanceSpecsInstanceSpec()
                self.instance_spec.append(temp_model.from_map(k1))

        return self

class DescribeInstanceSpecResponseBodyInstanceSpecsInstanceSpec(DaraModel):
    def __init__(
        self,
        core: str = None,
        display_name: str = None,
        instance_type: str = None,
        memory: str = None,
    ):
        # The number of CPU cores.
        self.core = core
        # The display name of the instance type.
        self.display_name = display_name
        # The type of the instance.
        self.instance_type = instance_type
        # The memory size. Unit: MB.
        self.memory = memory

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.core is not None:
            result['Core'] = self.core

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.memory is not None:
            result['Memory'] = self.memory

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Core') is not None:
            self.core = m.get('Core')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        return self

