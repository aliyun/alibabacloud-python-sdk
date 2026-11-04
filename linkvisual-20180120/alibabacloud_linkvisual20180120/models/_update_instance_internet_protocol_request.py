# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateInstanceInternetProtocolRequest(DaraModel):
    def __init__(
        self,
        iot_instance_id: str = None,
        ip_version: str = None,
    ):
        # The instance ID. You can view the **ID** of the current instance on the **Instance overview** page in the IoT Platform console.
        # 
        # >Notice: 
        # - If an ID value is available, you must specify it. Otherwise, the call fails.
        # - If the <props="intl"><ph>**Instance overview** page or </ph>ID value is not available, you do not need to specify it.
        # 
        # 
        # 
        # For more information about instances, see [Instance overview](https://help.aliyun.com/document_detail/356505.html).
        # 
        # This parameter is required.
        self.iot_instance_id = iot_instance_id
        # The IP protocol version. Valid values:
        # - IPv4 (default)
        # - IPv6
        # 
        # > If the IP protocol version is set to IPv6, streaming media-related addresses are changed to IPv4/IPv6 dual-stack addresses. Make sure that your devices and applications are configured for IPv6. Otherwise, exceptions such as playback screen loading failures may occur.
        # 
        # This parameter is required.
        self.ip_version = ip_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id

        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')

        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        return self

