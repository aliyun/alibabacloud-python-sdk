# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeDBClusterSSLResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeDBClusterSSLResponseBodyItems] = None,
        request_id: str = None,
        sslauto_rotate: str = None,
    ):
        # The list of SSL connections.
        self.items = items
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether automatic rotation of SSL certificates is enabled. Valid values:
        # 
        # *   **Enable**: The feature is enabled.
        # *   **Disable**: The feature is disabled.
        # 
        # > This parameter is valid only for a PolarDB for MySQL cluster.
        self.sslauto_rotate = sslauto_rotate

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sslauto_rotate is not None:
            result['SSLAutoRotate'] = self.sslauto_rotate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeDBClusterSSLResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SSLAutoRotate') is not None:
            self.sslauto_rotate = m.get('SSLAutoRotate')

        return self

class DescribeDBClusterSSLResponseBodyItems(DaraModel):
    def __init__(
        self,
        dbendpoint_id: str = None,
        sslauto_rotate: str = None,
        sslconnection_string: str = None,
        sslenabled: str = None,
        sslexpire_time: str = None,
    ):
        # The ID of the endpoint.
        self.dbendpoint_id = dbendpoint_id
        self.sslauto_rotate = sslauto_rotate
        # The SSL connection string.
        self.sslconnection_string = sslconnection_string
        # Indicates whether SSL encryption is enabled. Valid values:
        # 
        # *   **Enabled**: SSL is enabled.
        # *   **Disable**: SSL is disabled.
        self.sslenabled = sslenabled
        # The time when the server certificate expires. The time is in the `yyyy-MM-ddTHH:mm:ssZ` format. The time is displayed in UTC.
        self.sslexpire_time = sslexpire_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbendpoint_id is not None:
            result['DBEndpointId'] = self.dbendpoint_id

        if self.sslauto_rotate is not None:
            result['SSLAutoRotate'] = self.sslauto_rotate

        if self.sslconnection_string is not None:
            result['SSLConnectionString'] = self.sslconnection_string

        if self.sslenabled is not None:
            result['SSLEnabled'] = self.sslenabled

        if self.sslexpire_time is not None:
            result['SSLExpireTime'] = self.sslexpire_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBEndpointId') is not None:
            self.dbendpoint_id = m.get('DBEndpointId')

        if m.get('SSLAutoRotate') is not None:
            self.sslauto_rotate = m.get('SSLAutoRotate')

        if m.get('SSLConnectionString') is not None:
            self.sslconnection_string = m.get('SSLConnectionString')

        if m.get('SSLEnabled') is not None:
            self.sslenabled = m.get('SSLEnabled')

        if m.get('SSLExpireTime') is not None:
            self.sslexpire_time = m.get('SSLExpireTime')

        return self

