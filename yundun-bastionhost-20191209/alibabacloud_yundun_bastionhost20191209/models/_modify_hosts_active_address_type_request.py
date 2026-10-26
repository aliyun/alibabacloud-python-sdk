# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyHostsActiveAddressTypeRequest(DaraModel):
    def __init__(
        self,
        active_address_type: str = None,
        host_ids: str = None,
        instance_id: str = None,
        project_id: int = None,
        region_id: str = None,
    ):
        # The new endpoint type of the host. Valid values:
        # 
        # - **Public**: Internet
        # - **Private**: private network
        # 
        # This parameter is required.
        self.active_address_type = active_address_type
        # The IDs of the hosts whose endpoint types you want to modify. The value is a character string in JSON format. You can specify up to 100 host IDs.
        # You can invoke the [ListHosts](https://help.aliyun.com/document_detail/200665.html) operation to obtain the value of this parameter.
        # 
        # This parameter is required.
        self.host_ids = host_ids
        # The instance ID of the Bastionhost instance to which the host whose endpoint type you want to modify belongs.
        # 
        # > You can invoke the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to obtain the value of this parameter.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The project ID.
        self.project_id = project_id
        # The area ID of the Bastionhost instance to which the host whose endpoint type you want to modify belongs.
        # 
        # > For more information about the mapping between area IDs and area names, see [Regions and active zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active_address_type is not None:
            result['ActiveAddressType'] = self.active_address_type

        if self.host_ids is not None:
            result['HostIds'] = self.host_ids

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveAddressType') is not None:
            self.active_address_type = m.get('ActiveAddressType')

        if m.get('HostIds') is not None:
            self.host_ids = m.get('HostIds')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

