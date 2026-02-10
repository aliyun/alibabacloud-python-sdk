# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAgentlessRiskUuidRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        instance_id: str = None,
        instance_name: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        machine_name: str = None,
        page_size: int = None,
        risk: bool = None,
        target_name: str = None,
        target_type: int = None,
    ):
        # The page number.
        self.current_page = current_page
        # The instance ID of the asset.
        self.instance_id = instance_id
        # The instance name of the asset.
        self.instance_name = instance_name
        # The public IP address of the asset that you want to query.
        self.internet_ip = internet_ip
        # The private IP address of the asset that you want to query.
        self.intranet_ip = intranet_ip
        # The name of the instance.
        self.machine_name = machine_name
        # The number of entries per page.
        self.page_size = page_size
        # Specifies whether risks exist. Valid values:
        # 
        # *   **true**: Risks exist.
        # *   **false**: Risks do not exist.
        self.risk = risk
        # The name of the detection object.
        self.target_name = target_name
        # Specifies the type of the object being inspected. Valid values:
        # 
        # *   **1**: Host Snapshot.
        # *   **2**: Host Image.
        # *   **3**: User Snapshot.
        # *   **4**: User Image.
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip

        if self.machine_name is not None:
            result['MachineName'] = self.machine_name

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.risk is not None:
            result['Risk'] = self.risk

        if self.target_name is not None:
            result['TargetName'] = self.target_name

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')

        if m.get('MachineName') is not None:
            self.machine_name = m.get('MachineName')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Risk') is not None:
            self.risk = m.get('Risk')

        if m.get('TargetName') is not None:
            self.target_name = m.get('TargetName')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

