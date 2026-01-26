# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class GetCloudClusterAllUrlResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: List[main_models.GetCloudClusterAllUrlResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed.
        self.code = code
        # An array object.
        self.data = data
        # The returned message.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values: true and false.
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetCloudClusterAllUrlResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetCloudClusterAllUrlResponseBodyData(DaraModel):
    def __init__(
        self,
        product_code: str = None,
        region: str = None,
        remote_url: main_models.GetCloudClusterAllUrlResponseBodyDataRemoteUrl = None,
    ):
        # The identifier of the cloud service.
        self.product_code = product_code
        # The region ID.
        self.region = region
        # The URLs for remote read and write. The value is a JSON string.
        self.remote_url = remote_url

    def validate(self):
        if self.remote_url:
            self.remote_url.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.region is not None:
            result['Region'] = self.region

        if self.remote_url is not None:
            result['RemoteUrl'] = self.remote_url.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('RemoteUrl') is not None:
            temp_model = main_models.GetCloudClusterAllUrlResponseBodyDataRemoteUrl()
            self.remote_url = temp_model.from_map(m.get('RemoteUrl'))

        return self

class GetCloudClusterAllUrlResponseBodyDataRemoteUrl(DaraModel):
    def __init__(
        self,
        auth_token: bool = None,
        grafana_url: str = None,
        internet_grafana_url: str = None,
        internet_push_gateway_url: str = None,
        internet_remote_read_url: str = None,
        internet_remote_write_url: str = None,
        push_gateway_url: str = None,
        remote_read_url: str = None,
        remote_write_url: str = None,
        token: str = None,
    ):
        # Indicates whether authentication is enabled.
        self.auth_token = auth_token
        # The internal URL for Grafana.
        self.grafana_url = grafana_url
        # The public URL for Grafana.
        self.internet_grafana_url = internet_grafana_url
        # The public URL for Pushgateway.
        self.internet_push_gateway_url = internet_push_gateway_url
        # The public URL for remote read.
        self.internet_remote_read_url = internet_remote_read_url
        # The public URL for remote write.
        self.internet_remote_write_url = internet_remote_write_url
        # The internal URL for Pushgateway.
        self.push_gateway_url = push_gateway_url
        # The internal URL for remote read.
        self.remote_read_url = remote_read_url
        # The internal URL for remote write.
        self.remote_write_url = remote_write_url
        # The token value used for authentication.
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_token is not None:
            result['AuthToken'] = self.auth_token

        if self.grafana_url is not None:
            result['GrafanaUrl'] = self.grafana_url

        if self.internet_grafana_url is not None:
            result['InternetGrafanaUrl'] = self.internet_grafana_url

        if self.internet_push_gateway_url is not None:
            result['InternetPushGatewayUrl'] = self.internet_push_gateway_url

        if self.internet_remote_read_url is not None:
            result['InternetRemoteReadUrl'] = self.internet_remote_read_url

        if self.internet_remote_write_url is not None:
            result['InternetRemoteWriteUrl'] = self.internet_remote_write_url

        if self.push_gateway_url is not None:
            result['PushGatewayUrl'] = self.push_gateway_url

        if self.remote_read_url is not None:
            result['RemoteReadUrl'] = self.remote_read_url

        if self.remote_write_url is not None:
            result['RemoteWriteUrl'] = self.remote_write_url

        if self.token is not None:
            result['Token'] = self.token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthToken') is not None:
            self.auth_token = m.get('AuthToken')

        if m.get('GrafanaUrl') is not None:
            self.grafana_url = m.get('GrafanaUrl')

        if m.get('InternetGrafanaUrl') is not None:
            self.internet_grafana_url = m.get('InternetGrafanaUrl')

        if m.get('InternetPushGatewayUrl') is not None:
            self.internet_push_gateway_url = m.get('InternetPushGatewayUrl')

        if m.get('InternetRemoteReadUrl') is not None:
            self.internet_remote_read_url = m.get('InternetRemoteReadUrl')

        if m.get('InternetRemoteWriteUrl') is not None:
            self.internet_remote_write_url = m.get('InternetRemoteWriteUrl')

        if m.get('PushGatewayUrl') is not None:
            self.push_gateway_url = m.get('PushGatewayUrl')

        if m.get('RemoteReadUrl') is not None:
            self.remote_read_url = m.get('RemoteReadUrl')

        if m.get('RemoteWriteUrl') is not None:
            self.remote_write_url = m.get('RemoteWriteUrl')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        return self

