# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeCheckWarningMachinesResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        machines: List[main_models.DescribeCheckWarningMachinesResponseBodyMachines] = None,
        page_size: int = None,
        request_id: str = None,
    ):
        # The number of the servers on which the same risk item is detected.
        self.count = count
        # The number of the page to return. Default value: **1**.
        self.current_page = current_page
        # The servers on which the same risk item is detected.
        self.machines = machines
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.machines:
            for v1 in self.machines:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        result['Machines'] = []
        if self.machines is not None:
            for k1 in self.machines:
                result['Machines'].append(k1.to_map() if k1 else None)

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.machines = []
        if m.get('Machines') is not None:
            for k1 in m.get('Machines'):
                temp_model = main_models.DescribeCheckWarningMachinesResponseBodyMachines()
                self.machines.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeCheckWarningMachinesResponseBodyMachines(DaraModel):
    def __init__(
        self,
        bind: bool = None,
        instance_id: str = None,
        instance_name: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        region_id: str = None,
        uuid: str = None,
    ):
        # Indicates whether Security Center is authorized to protect the asset. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.bind = bind
        # The instance ID of the server.
        self.instance_id = instance_id
        # The instance name of the server.
        self.instance_name = instance_name
        # The public IP address of the server.
        self.internet_ip = internet_ip
        # The private IP address of the server.
        self.intranet_ip = intranet_ip
        # The ID of the region in which the server resides.
        self.region_id = region_id
        # The UUID of the server.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bind is not None:
            result['Bind'] = self.bind

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bind') is not None:
            self.bind = m.get('Bind')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

