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
        # A list of addresses in the address pool.
        # 
        # This parameter is required.
        self.addr = addr
        # The ID of the address pool. For more information, see [DescribeDnsGtmInstanceAddressPools](https://www.alibabacloud.com/help/en/dns/api-alidns-2015-01-09-describednsgtminstanceaddresspools).
        # 
        # This parameter is required.
        self.addr_pool_id = addr_pool_id
        # The language of the response. Default value: en. Valid values: en, zh, and ja.
        self.lang = lang
        # The load balancing policy. Valid values:
        # 
        # - ALL_RR: Returns all addresses.
        # 
        # - RATIO: Returns addresses by weight.
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
        # The address.
        # 
        # This parameter is required.
        self.addr = addr
        # The source region of the address. This parameter is a JSON string.
        # 
        # - LineCode: The line code of the source region. This parameter is deprecated. Use lineCodes instead.
        # 
        # - lineCodes: A list of line codes for the source regions.
        # 
        # - lineCodeRectifyType: The type of line code rectification. Default value: AUTO. Valid values:
        # 
        #   - NO_NEED: No rectification is required.
        # 
        #   - RECTIFIED: The line code is rectified.
        # 
        #   - AUTO: The line code is automatically rectified.
        self.attribute_info = attribute_info
        # The weight.
        self.lba_weight = lba_weight
        # The mode. Valid values:
        # 
        # - SMART: Smart return
        # 
        # - ONLINE: Always online
        # 
        # - OFFLINE: Always offline
        # 
        # This parameter is required.
        self.mode = mode
        # The remarks.
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

