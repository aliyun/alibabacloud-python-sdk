# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_amqp_open20191212 import models as main_models
from darabonba.model import DaraModel

class ListVirtualHostsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListVirtualHostsResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ListVirtualHostsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListVirtualHostsResponseBodyData(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        virtual_hosts: List[main_models.ListVirtualHostsResponseBodyDataVirtualHosts] = None,
    ):
        # The maximum number of entries returned.
        self.max_results = max_results
        # The token that marks the end of the current returned page. If this parameter is empty, all data is retrieved.
        self.next_token = next_token
        # The vhosts.
        self.virtual_hosts = virtual_hosts

    def validate(self):
        if self.virtual_hosts:
            for v1 in self.virtual_hosts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['VirtualHosts'] = []
        if self.virtual_hosts is not None:
            for k1 in self.virtual_hosts:
                result['VirtualHosts'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.virtual_hosts = []
        if m.get('VirtualHosts') is not None:
            for k1 in m.get('VirtualHosts'):
                temp_model = main_models.ListVirtualHostsResponseBodyDataVirtualHosts()
                self.virtual_hosts.append(temp_model.from_map(k1))

        return self

class ListVirtualHostsResponseBodyDataVirtualHosts(DaraModel):
    def __init__(
        self,
        name: str = None,
    ):
        # The vhost name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

