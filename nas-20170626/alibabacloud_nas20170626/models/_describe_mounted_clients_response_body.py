# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nas20170626 import models as main_models
from darabonba.model import DaraModel

class DescribeMountedClientsResponseBody(DaraModel):
    def __init__(
        self,
        clients: main_models.DescribeMountedClientsResponseBodyClients = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The queried clients.
        self.clients = clients
        # The page number.
        self.page_number = page_number
        # The number of IP addresses returned per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of IP addresses.
        self.total_count = total_count

    def validate(self):
        if self.clients:
            self.clients.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.clients is not None:
            result['Clients'] = self.clients.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Clients') is not None:
            temp_model = main_models.DescribeMountedClientsResponseBodyClients()
            self.clients = temp_model.from_map(m.get('Clients'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeMountedClientsResponseBodyClients(DaraModel):
    def __init__(
        self,
        client: List[main_models.DescribeMountedClientsResponseBodyClientsClient] = None,
    ):
        self.client = client

    def validate(self):
        if self.client:
            for v1 in self.client:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Client'] = []
        if self.client is not None:
            for k1 in self.client:
                result['Client'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.client = []
        if m.get('Client') is not None:
            for k1 in m.get('Client'):
                temp_model = main_models.DescribeMountedClientsResponseBodyClientsClient()
                self.client.append(temp_model.from_map(k1))

        return self

class DescribeMountedClientsResponseBodyClientsClient(DaraModel):
    def __init__(
        self,
        client_ip: str = None,
    ):
        # The IP address of the client.
        self.client_ip = client_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_ip is not None:
            result['ClientIP'] = self.client_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIP') is not None:
            self.client_ip = m.get('ClientIP')

        return self

