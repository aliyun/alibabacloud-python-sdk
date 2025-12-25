# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetProxyResponseBody(DaraModel):
    def __init__(
        self,
        creator_id: int = None,
        creator_name: str = None,
        error_code: str = None,
        error_message: str = None,
        https_port: int = None,
        instance_id: int = None,
        private_enable: bool = None,
        private_host: str = None,
        protocol_port: int = None,
        protocol_type: str = None,
        proxy_id: int = None,
        public_enable: bool = None,
        public_host: str = None,
        region_id: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The ID of the user who enabled the secure access proxy feature.
        self.creator_id = creator_id
        # The nickname of the user who enabled the secure access proxy feature.
        self.creator_name = creator_name
        # The error code returned if the request failed.
        self.error_code = error_code
        # The error message returned if the request failed.
        self.error_message = error_message
        # The port number used by the HTTPS protocol.
        self.https_port = https_port
        # The ID of the instance.
        self.instance_id = instance_id
        # Indicates whether the internal endpoint was enabled. Default value: **true**.
        self.private_enable = private_enable
        # The internal endpoint.
        self.private_host = private_host
        # The port number used by the protocol.
        self.protocol_port = protocol_port
        # The protocol type of the database. Example: MYSQL.
        self.protocol_type = protocol_type
        # The ID of the secure access proxy.
        self.proxy_id = proxy_id
        # Indicates whether the public endpoint was enabled. Valid values:
        # 
        # *   **true**: The public endpoint was enabled.
        # *   **false**: The public endpoint was disabled.
        self.public_enable = public_enable
        # The public endpoint. A public endpoint is returned no matter whether the public endpoint is enabled or disabled.
        # 
        # > 
        # 
        # *   If the value of the PublicEnable parameter is **true**, a valid public endpoint that can be resolved by using Alibaba Cloud DNS is returned.
        # 
        # *   If the value of the PublicEnable parameter is **false**, an invalid public endpoint that cannot be resolved by using Alibaba Cloud DNS is returned.
        self.public_host = public_host
        # The ID of the region in which the instance resides.
        self.region_id = region_id
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id

        if self.creator_name is not None:
            result['CreatorName'] = self.creator_name

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.https_port is not None:
            result['HttpsPort'] = self.https_port

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.private_enable is not None:
            result['PrivateEnable'] = self.private_enable

        if self.private_host is not None:
            result['PrivateHost'] = self.private_host

        if self.protocol_port is not None:
            result['ProtocolPort'] = self.protocol_port

        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type

        if self.proxy_id is not None:
            result['ProxyId'] = self.proxy_id

        if self.public_enable is not None:
            result['PublicEnable'] = self.public_enable

        if self.public_host is not None:
            result['PublicHost'] = self.public_host

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')

        if m.get('CreatorName') is not None:
            self.creator_name = m.get('CreatorName')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('HttpsPort') is not None:
            self.https_port = m.get('HttpsPort')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PrivateEnable') is not None:
            self.private_enable = m.get('PrivateEnable')

        if m.get('PrivateHost') is not None:
            self.private_host = m.get('PrivateHost')

        if m.get('ProtocolPort') is not None:
            self.protocol_port = m.get('ProtocolPort')

        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')

        if m.get('ProxyId') is not None:
            self.proxy_id = m.get('ProxyId')

        if m.get('PublicEnable') is not None:
            self.public_enable = m.get('PublicEnable')

        if m.get('PublicHost') is not None:
            self.public_host = m.get('PublicHost')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

