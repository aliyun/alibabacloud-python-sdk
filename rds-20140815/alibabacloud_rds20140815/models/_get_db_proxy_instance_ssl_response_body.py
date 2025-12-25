# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class GetDbProxyInstanceSslResponseBody(DaraModel):
    def __init__(
        self,
        db_proxy_cert_list_items: main_models.GetDbProxyInstanceSslResponseBodyDbProxyCertListItems = None,
        request_id: str = None,
    ):
        # An array that consists of SSL encryption settings.
        self.db_proxy_cert_list_items = db_proxy_cert_list_items
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.db_proxy_cert_list_items:
            self.db_proxy_cert_list_items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_proxy_cert_list_items is not None:
            result['DbProxyCertListItems'] = self.db_proxy_cert_list_items.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbProxyCertListItems') is not None:
            temp_model = main_models.GetDbProxyInstanceSslResponseBodyDbProxyCertListItems()
            self.db_proxy_cert_list_items = temp_model.from_map(m.get('DbProxyCertListItems'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetDbProxyInstanceSslResponseBodyDbProxyCertListItems(DaraModel):
    def __init__(
        self,
        db_proxy_cert_list_items: List[main_models.GetDbProxyInstanceSslResponseBodyDbProxyCertListItemsDbProxyCertListItems] = None,
    ):
        self.db_proxy_cert_list_items = db_proxy_cert_list_items

    def validate(self):
        if self.db_proxy_cert_list_items:
            for v1 in self.db_proxy_cert_list_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DbProxyCertListItems'] = []
        if self.db_proxy_cert_list_items is not None:
            for k1 in self.db_proxy_cert_list_items:
                result['DbProxyCertListItems'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.db_proxy_cert_list_items = []
        if m.get('DbProxyCertListItems') is not None:
            for k1 in m.get('DbProxyCertListItems'):
                temp_model = main_models.GetDbProxyInstanceSslResponseBodyDbProxyCertListItemsDbProxyCertListItems()
                self.db_proxy_cert_list_items.append(temp_model.from_map(k1))

        return self

class GetDbProxyInstanceSslResponseBodyDbProxyCertListItemsDbProxyCertListItems(DaraModel):
    def __init__(
        self,
        cert_common_name: str = None,
        db_instance_name: str = None,
        endpoint_name: str = None,
        endpoint_type: str = None,
        ssl_expired_time: str = None,
    ):
        # The dedicated proxy endpoint for which SSL encryption is enabled.
        self.cert_common_name = cert_common_name
        # The instance ID.
        self.db_instance_name = db_instance_name
        # The ID of the dedicated proxy endpoint.
        self.endpoint_name = endpoint_name
        # The default identifier of the dedicated proxy endpoint. The value is fixed as **RWSplit**.
        self.endpoint_type = endpoint_type
        # The time at which the certificate expires.
        self.ssl_expired_time = ssl_expired_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_common_name is not None:
            result['CertCommonName'] = self.cert_common_name

        if self.db_instance_name is not None:
            result['DbInstanceName'] = self.db_instance_name

        if self.endpoint_name is not None:
            result['EndpointName'] = self.endpoint_name

        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type

        if self.ssl_expired_time is not None:
            result['SslExpiredTime'] = self.ssl_expired_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertCommonName') is not None:
            self.cert_common_name = m.get('CertCommonName')

        if m.get('DbInstanceName') is not None:
            self.db_instance_name = m.get('DbInstanceName')

        if m.get('EndpointName') is not None:
            self.endpoint_name = m.get('EndpointName')

        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')

        if m.get('SslExpiredTime') is not None:
            self.ssl_expired_time = m.get('SslExpiredTime')

        return self

