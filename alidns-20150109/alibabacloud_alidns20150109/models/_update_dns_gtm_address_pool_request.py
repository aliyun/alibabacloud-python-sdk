# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class UpdateDnsGtmAddressPoolRequest(DaraModel):
    def __init__(
        self,
        addr: List[main_models.UpdateDnsGtmAddressPoolRequestAddr] = None,
        addr_pool_id: str = None,
        lang: str = None,
        lba_strategy: str = None,
        name: str = None,
    ):
        # The address pools.
        # 
        # This parameter is required.
        self.addr = addr
        # The ID of the address pool.
        # 
        # This parameter is required.
        self.addr_pool_id = addr_pool_id
        # The language of the values of specific response parameters. Default value: en. Valid values: en, zh, and ja.
        self.lang = lang
        # The load balancing policy of the address pool. Valid values:
        # 
        # *   ALL_RR: returns all addresses.
        # *   RATIO: returns addresses by weight.
        # 
        # This parameter is required.
        self.lba_strategy = lba_strategy
        # The name of the address pool.
        self.name = name

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

        if self.lba_strategy is not None:
            result['LbaStrategy'] = self.lba_strategy

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.addr = []
        if m.get('Addr') is not None:
            for k1 in m.get('Addr'):
                temp_model = main_models.UpdateDnsGtmAddressPoolRequestAddr()
                self.addr.append(temp_model.from_map(k1))

        if m.get('AddrPoolId') is not None:
            self.addr_pool_id = m.get('AddrPoolId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('LbaStrategy') is not None:
            self.lba_strategy = m.get('LbaStrategy')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class UpdateDnsGtmAddressPoolRequestAddr(DaraModel):
    def __init__(
        self,
        addr: str = None,
        attribute_info: str = None,
        lba_weight: int = None,
        mode: str = None,
        remark: str = None,
    ):
        # The address in the address pool.
        # 
        # This parameter is required.
        self.addr = addr
        # The information about the source region of the address. The value of the parameter is a string in the JSON format. Valid values:
        # 
        # *   LineCode: the line code of the source region. This parameter is deprecated. Use lineCodes instead.
        # 
        # *   lineCodes: the line codes of the source region
        # 
        # *   lineCodeRectifyType: the rectification type of the line code. Default value: AUTO. Valid values:
        # 
        #     *   NO_NEED: no need for rectification
        #     *   RECTIFIED: rectified
        #     *   AUTO: automatic rectification
        self.attribute_info = attribute_info
        # The weight of the address.
        self.lba_weight = lba_weight
        # The return mode of the addresses. Valid values:
        # 
        # *   SMART: smart return
        # *   ONLINE: always online
        # *   OFFLINE: always offline
        # 
        # This parameter is required.
        self.mode = mode
        # The description of the address pool.
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addr is not None:
            result['Addr'] = self.addr

        if self.attribute_info is not None:
            result['AttributeInfo'] = self.attribute_info

        if self.lba_weight is not None:
            result['LbaWeight'] = self.lba_weight

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.remark is not None:
            result['Remark'] = self.remark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Addr') is not None:
            self.addr = m.get('Addr')

        if m.get('AttributeInfo') is not None:
            self.attribute_info = m.get('AttributeInfo')

        if m.get('LbaWeight') is not None:
            self.lba_weight = m.get('LbaWeight')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        return self

