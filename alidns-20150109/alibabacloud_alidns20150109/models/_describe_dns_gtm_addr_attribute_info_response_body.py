# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribeDnsGtmAddrAttributeInfoResponseBody(DaraModel):
    def __init__(
        self,
        addr: main_models.DescribeDnsGtmAddrAttributeInfoResponseBodyAddr = None,
        request_id: str = None,
    ):
        # The address in the address pool.
        self.addr = addr
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.addr:
            self.addr.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addr is not None:
            result['Addr'] = self.addr.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Addr') is not None:
            temp_model = main_models.DescribeDnsGtmAddrAttributeInfoResponseBodyAddr()
            self.addr = temp_model.from_map(m.get('Addr'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDnsGtmAddrAttributeInfoResponseBodyAddr(DaraModel):
    def __init__(
        self,
        addr: List[main_models.DescribeDnsGtmAddrAttributeInfoResponseBodyAddrAddr] = None,
    ):
        self.addr = addr

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.addr = []
        if m.get('Addr') is not None:
            for k1 in m.get('Addr'):
                temp_model = main_models.DescribeDnsGtmAddrAttributeInfoResponseBodyAddrAddr()
                self.addr.append(temp_model.from_map(k1))

        return self

class DescribeDnsGtmAddrAttributeInfoResponseBodyAddrAddr(DaraModel):
    def __init__(
        self,
        addr: str = None,
        attribute_info: main_models.DescribeDnsGtmAddrAttributeInfoResponseBodyAddrAddrAttributeInfo = None,
    ):
        # The address in the address pool.
        self.addr = addr
        # The information about the source region of the address.
        self.attribute_info = attribute_info

    def validate(self):
        if self.attribute_info:
            self.attribute_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addr is not None:
            result['Addr'] = self.addr

        if self.attribute_info is not None:
            result['AttributeInfo'] = self.attribute_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Addr') is not None:
            self.addr = m.get('Addr')

        if m.get('AttributeInfo') is not None:
            temp_model = main_models.DescribeDnsGtmAddrAttributeInfoResponseBodyAddrAddrAttributeInfo()
            self.attribute_info = temp_model.from_map(m.get('AttributeInfo'))

        return self

class DescribeDnsGtmAddrAttributeInfoResponseBodyAddrAddrAttributeInfo(DaraModel):
    def __init__(
        self,
        father_code: str = None,
        group_code: str = None,
        group_name: str = None,
        line_code: str = None,
        line_name: str = None,
    ):
        # The parent line code of the source region.
        self.father_code = father_code
        # The code of the source region group.
        self.group_code = group_code
        # The name of the source region group.
        self.group_name = group_name
        # The line code of the source region.
        self.line_code = line_code
        # The line name of the source region.
        self.line_name = line_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.father_code is not None:
            result['FatherCode'] = self.father_code

        if self.group_code is not None:
            result['GroupCode'] = self.group_code

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.line_code is not None:
            result['LineCode'] = self.line_code

        if self.line_name is not None:
            result['LineName'] = self.line_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FatherCode') is not None:
            self.father_code = m.get('FatherCode')

        if m.get('GroupCode') is not None:
            self.group_code = m.get('GroupCode')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('LineCode') is not None:
            self.line_code = m.get('LineCode')

        if m.get('LineName') is not None:
            self.line_name = m.get('LineName')

        return self

