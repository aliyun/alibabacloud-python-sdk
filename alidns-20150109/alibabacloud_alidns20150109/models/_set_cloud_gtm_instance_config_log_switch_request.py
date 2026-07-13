# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetCloudGtmInstanceConfigLogSwitchRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        config_id: str = None,
        instance_id: str = None,
        status: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. Generate a unique value for this parameter. The client token can contain only ASCII characters and cannot exceed 64 characters in length.
        # 
        # > If you do not specify this parameter, the system automatically uses the RequestId of the API request as the ClientToken. The RequestId of each API request may be different.
        self.client_token = client_token
        # The ID of the instance configuration. A and AAAA records can be configured for the same connected domain name and GTM instance. In this case, the GTM instance has two instance configurations. ConfigId uniquely identifies an instance configuration. To find the ConfigId for a domain name instance, call the [ListCloudGtmInstanceConfigs](https://help.aliyun.com/document_detail/2797349.html) operation.
        # 
        # This parameter is required.
        self.config_id = config_id
        # The ID of the Global Traffic Manager (GTM) 3.0 instance.
        self.instance_id = instance_id
        # The status of the network traffic analysis feature:
        # 
        # - enable
        # 
        # - disable
        # 
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

