# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RebootInstancesRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        force_reboot: bool = None,
        instance_ids: str = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # Specifies whether to forcibly restart the servers. Valid values:
        # 
        # - true: forcibly restarts the servers. This operation is equivalent to the typical power-off operation. Cache data that is not written to storage devices on the server will be lost.
        # 
        # - false: normally restarts the instance.
        # 
        # Default value: false
        self.force_reboot = force_reboot
        # The IDs of the simple application servers. The value can be a JSON array that consists of up to 100 simple application server IDs. Separate multiple server IDs with commas (,).
        # 
        # This parameter is required.
        self.instance_ids = instance_ids
        # The region ID of the simple application servers. You can call the [ListRegions](https://help.aliyun.com/document_detail/189315.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.force_reboot is not None:
            result['ForceReboot'] = self.force_reboot

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ForceReboot') is not None:
            self.force_reboot = m.get('ForceReboot')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

