# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class UpdateGtmAddressPoolRequest(DaraModel):
    def __init__(
        self,
        addr: List[main_models.UpdateGtmAddressPoolRequestAddr] = None,
        addr_pool_id: str = None,
        lang: str = None,
        min_available_addr_num: int = None,
        name: str = None,
        type: str = None,
    ):
        # This parameter is required.
        self.addr = addr
        # The ID of the address pool that you want to modify.
        # 
        # This parameter is required.
        self.addr_pool_id = addr_pool_id
        # The language used by the user.
        self.lang = lang
        # The minimum number of available addresses in the address pool.
        self.min_available_addr_num = min_available_addr_num
        # The name of the address pool that you want to modify.
        self.name = name
        # The type of the address pool that you want to modify.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.addr:
            for v1 in self.addr:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Addr'] = []
        if self.addr is not None:
            for k1 in self.addr:
                result['Addr'].append(k1.to_map() if k1 else None)

        if self.addr_pool_id is not None:
            result['AddrPoolId'] = self.addr_pool_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.min_available_addr_num is not None:
            result['MinAvailableAddrNum'] = self.min_available_addr_num

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.addr = []
        if m.get('Addr') is not None:
            for k1 in m.get('Addr'):
                temp_model = main_models.UpdateGtmAddressPoolRequestAddr()
                self.addr.append(temp_model.from_map(k1))

        if m.get('AddrPoolId') is not None:
            self.addr_pool_id = m.get('AddrPoolId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('MinAvailableAddrNum') is not None:
            self.min_available_addr_num = m.get('MinAvailableAddrNum')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class UpdateGtmAddressPoolRequestAddr(DaraModel):
    def __init__(
        self,
        lba_weight: int = None,
        mode: str = None,
        value: str = None,
    ):
        # The weight of the address pool that you want to modify.
        self.lba_weight = lba_weight
        # The mode of the address pool that you want to modify.
        # 
        # *   **SMART**: Intelligent return
        # *   **ONLINE**: Always online
        # *   **OFFLINE**: Always offline
        self.mode = mode
        # The addresses in the address pool.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lba_weight is not None:
            result['LbaWeight'] = self.lba_weight

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LbaWeight') is not None:
            self.lba_weight = m.get('LbaWeight')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

