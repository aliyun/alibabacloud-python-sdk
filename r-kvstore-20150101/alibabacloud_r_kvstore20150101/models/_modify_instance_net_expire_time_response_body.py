# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_r_kvstore20150101 import models as main_models
from darabonba.model import DaraModel

class ModifyInstanceNetExpireTimeResponseBody(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        net_info_items: main_models.ModifyInstanceNetExpireTimeResponseBodyNetInfoItems = None,
        request_id: str = None,
    ):
        # The ID of the instance.
        self.instance_id = instance_id
        # Details about the extension period for which the classic network endpoint of the instance is retained.
        self.net_info_items = net_info_items
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.net_info_items:
            self.net_info_items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.net_info_items is not None:
            result['NetInfoItems'] = self.net_info_items.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NetInfoItems') is not None:
            temp_model = main_models.ModifyInstanceNetExpireTimeResponseBodyNetInfoItems()
            self.net_info_items = temp_model.from_map(m.get('NetInfoItems'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ModifyInstanceNetExpireTimeResponseBodyNetInfoItems(DaraModel):
    def __init__(
        self,
        net_info_item: List[main_models.ModifyInstanceNetExpireTimeResponseBodyNetInfoItemsNetInfoItem] = None,
    ):
        self.net_info_item = net_info_item

    def validate(self):
        if self.net_info_item:
            for v1 in self.net_info_item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NetInfoItem'] = []
        if self.net_info_item is not None:
            for k1 in self.net_info_item:
                result['NetInfoItem'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.net_info_item = []
        if m.get('NetInfoItem') is not None:
            for k1 in m.get('NetInfoItem'):
                temp_model = main_models.ModifyInstanceNetExpireTimeResponseBodyNetInfoItemsNetInfoItem()
                self.net_info_item.append(temp_model.from_map(k1))

        return self

class ModifyInstanceNetExpireTimeResponseBodyNetInfoItemsNetInfoItem(DaraModel):
    def __init__(
        self,
        connection_string: str = None,
        dbinstance_net_type: str = None,
        expired_time: str = None,
        ipaddress: str = None,
        port: str = None,
    ):
        # The endpoint of the classic network.
        self.connection_string = connection_string
        # The network type of the instance. The returned value is **Classic**.
        self.dbinstance_net_type = dbinstance_net_type
        # The expiration time of the classic network endpoint.
        self.expired_time = expired_time
        # The IP address of the instance in the classic network.
        self.ipaddress = ipaddress
        # The port number that is used to connect to the instance.
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string

        if self.dbinstance_net_type is not None:
            result['DBInstanceNetType'] = self.dbinstance_net_type

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.ipaddress is not None:
            result['IPAddress'] = self.ipaddress

        if self.port is not None:
            result['Port'] = self.port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('DBInstanceNetType') is not None:
            self.dbinstance_net_type = m.get('DBInstanceNetType')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('IPAddress') is not None:
            self.ipaddress = m.get('IPAddress')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        return self

