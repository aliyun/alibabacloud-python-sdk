# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ImportKMSSecretsForHostShrinkRequest(DaraModel):
    def __init__(
        self,
        host_id: int = None,
        instance_id: str = None,
        region_id: str = None,
        secrets_shrink: str = None,
    ):
        # The ID of the host to import the KMS secrets to.
        # 
        # > Only ECS hosts can import KMS secrets. You can call the [ListHosts](https://help.aliyun.com/document_detail/200665.html) operation to obtain this parameter.
        # 
        # This parameter is required.
        self.host_id = host_id
        # The ID of the Bastionhost instance.
        # 
        # > You can call the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to obtain this parameter.
        self.instance_id = instance_id
        # The region ID of the Bastionhost instance.
        # 
        # > For more information about region IDs and names, see [Regions and availability zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id
        # The KMS secrets to import.
        self.secrets_shrink = secrets_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.host_id is not None:
            result['HostId'] = self.host_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.secrets_shrink is not None:
            result['Secrets'] = self.secrets_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Secrets') is not None:
            self.secrets_shrink = m.get('Secrets')

        return self

