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
        # A list of SSL connection information.
        self.items = items
        # The request ID.
        self.request_id = request_id
        # Indicates whether automatic rotation of SSL certificates is enabled. Valid values:
        # 
        # - **Enable**: enabled
        # 
        # - **Disable**: disabled
        # 
        # > This parameter is supported only for PolarDB for MySQL.
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
        # The cluster endpoint ID.
        self.dbendpoint_id = dbendpoint_id
        # Indicates whether automatic rotation of SSL certificates is enabled. Valid values:
        # 
        # - **Enable**: enabled
        # 
        # - **Disable**: disabled
        # 
        # > This parameter is supported only when the database engine is compatible with PostgreSQL or Oracle syntax.
        self.sslauto_rotate = sslauto_rotate
        # The SSL connection endpoint.
        self.sslconnection_string = sslconnection_string
        # Indicates whether SSL encryption is enabled. Valid values:
        # 
        # - **Enabled**: enabled.
        # 
        # - **Disabled**: disabled.
        self.sslenabled = sslenabled
        # The certificate validity period. Format: `yyyy-MM-ddTHH:mm:ssZ` (UTC time).
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

