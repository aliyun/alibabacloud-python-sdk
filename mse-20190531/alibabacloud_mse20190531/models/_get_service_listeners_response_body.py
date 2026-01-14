# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class GetServiceListenersResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.GetServiceListenersResponseBodyData] = None,
        error_code: str = None,
        http_code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The returned data.
        self.data = data
        # The error code returned if the request failed.
        self.error_code = error_code
        # The HTTP status code returned.
        self.http_code = http_code
        # The message returned.
        # 
        # *   If the request is successful, a success message is returned.
        # *   If the request fails, an error message is returned.
        self.message = message
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   `true`: The request was successful.
        # *   `false`: The request failed.
        self.success = success
        # The number of listeners that are queried.
        self.total_count = total_count

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
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.http_code is not None:
            result['HttpCode'] = self.http_code

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetServiceListenersResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class GetServiceListenersResponseBodyData(DaraModel):
    def __init__(
        self,
        addr: str = None,
        agent: str = None,
        app: str = None,
        cluster: str = None,
        ip: str = None,
        namespace_id: str = None,
        port: str = None,
        service_name: str = None,
    ):
        # The IP address of the listener.
        self.addr = addr
        # The listener client version.
        self.agent = agent
        # The application name of the listener.
        self.app = app
        # The name of the cluster to which the monitored service belongs.
        self.cluster = cluster
        # The IP address of the monitored service.
        self.ip = ip
        # The ID of the namespace.
        self.namespace_id = namespace_id
        # The port number of the monitored service.
        self.port = port
        # The name of the monitored service.
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addr is not None:
            result['Addr'] = self.addr

        if self.agent is not None:
            result['Agent'] = self.agent

        if self.app is not None:
            result['App'] = self.app

        if self.cluster is not None:
            result['Cluster'] = self.cluster

        if self.ip is not None:
            result['IP'] = self.ip

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.port is not None:
            result['Port'] = self.port

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Addr') is not None:
            self.addr = m.get('Addr')

        if m.get('Agent') is not None:
            self.agent = m.get('Agent')

        if m.get('App') is not None:
            self.app = m.get('App')

        if m.get('Cluster') is not None:
            self.cluster = m.get('Cluster')

        if m.get('IP') is not None:
            self.ip = m.get('IP')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        return self

