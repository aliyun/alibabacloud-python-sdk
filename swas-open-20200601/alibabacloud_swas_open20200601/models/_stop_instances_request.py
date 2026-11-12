# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StopInstancesRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        force_stop: bool = None,
        instance_ids: str = None,
        region_id: str = None,
    ):
        # Ensures the idempotence of the request. You can generate the parameter value on your client and ensure that the value is unique across different requests. The ClientToken parameter supports only ASCII characters and can be up to 64 characters in length. For more information, see [Ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # Specifies whether to forcibly stop the instance.
        # 
        # - **true**: forcibly stops the instance.
        # 
        # - **false** (default): normally stops the instance.
        self.force_stop = force_stop
        # The instance IDs of the simple application servers. The value can be a JSON array that consists of up to 100 instance IDs. Separate multiple instance IDs with commas (,).
        # 
        # This parameter is required.
        self.instance_ids = instance_ids
        # The region ID of the simple application server instance. You can call the [ListRegions](https://help.aliyun.com/document_detail/189315.html) operation to query the supported Alibaba Cloud regions.
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

        if self.force_stop is not None:
            result['ForceStop'] = self.force_stop

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ForceStop') is not None:
            self.force_stop = m.get('ForceStop')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

