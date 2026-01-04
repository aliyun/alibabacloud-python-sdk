# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceBootConfigurationResponseBody(DaraModel):
    def __init__(
        self,
        instances: main_models.DescribeInstanceBootConfigurationResponseBodyInstances = None,
        request_id: str = None,
    ):
        # Schema of Response
        self.instances = instances
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.instances:
            self.instances.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instances is not None:
            result['Instances'] = self.instances.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Instances') is not None:
            temp_model = main_models.DescribeInstanceBootConfigurationResponseBodyInstances()
            self.instances = temp_model.from_map(m.get('Instances'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeInstanceBootConfigurationResponseBodyInstances(DaraModel):
    def __init__(
        self,
        boot_set: str = None,
        boot_type: str = None,
        disk_set: str = None,
        instance_id: str = None,
    ):
        # The startup method.
        self.boot_set = boot_set
        # The startup type.
        self.boot_type = boot_type
        # Specifies whether the startup depends on the disk.
        self.disk_set = disk_set
        # The ID of the instance.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.boot_set is not None:
            result['BootSet'] = self.boot_set

        if self.boot_type is not None:
            result['BootType'] = self.boot_type

        if self.disk_set is not None:
            result['DiskSet'] = self.disk_set

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BootSet') is not None:
            self.boot_set = m.get('BootSet')

        if m.get('BootType') is not None:
            self.boot_type = m.get('BootType')

        if m.get('DiskSet') is not None:
            self.disk_set = m.get('DiskSet')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

