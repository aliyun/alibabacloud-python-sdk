# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aligenieip_1_0 import models as main_models
from darabonba.model import DaraModel

class GetHotelHomeBackImageAndModesResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: main_models.GetHotelHomeBackImageAndModesResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.GetHotelHomeBackImageAndModesResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class GetHotelHomeBackImageAndModesResponseBodyResult(DaraModel):
    def __init__(
        self,
        background_image: str = None,
        hotel_name: str = None,
        mode_list: List[main_models.GetHotelHomeBackImageAndModesResponseBodyResultModeList] = None,
    ):
        self.background_image = background_image
        self.hotel_name = hotel_name
        self.mode_list = mode_list

    def validate(self):
        if self.mode_list:
            for v1 in self.mode_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.background_image is not None:
            result['BackgroundImage'] = self.background_image

        if self.hotel_name is not None:
            result['HotelName'] = self.hotel_name

        result['ModeList'] = []
        if self.mode_list is not None:
            for k1 in self.mode_list:
                result['ModeList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackgroundImage') is not None:
            self.background_image = m.get('BackgroundImage')

        if m.get('HotelName') is not None:
            self.hotel_name = m.get('HotelName')

        self.mode_list = []
        if m.get('ModeList') is not None:
            for k1 in m.get('ModeList'):
                temp_model = main_models.GetHotelHomeBackImageAndModesResponseBodyResultModeList()
                self.mode_list.append(temp_model.from_map(k1))

        return self

class GetHotelHomeBackImageAndModesResponseBodyResultModeList(DaraModel):
    def __init__(
        self,
        cn_name: str = None,
        code: str = None,
        icon: str = None,
    ):
        self.cn_name = cn_name
        self.code = code
        self.icon = icon

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cn_name is not None:
            result['CnName'] = self.cn_name

        if self.code is not None:
            result['Code'] = self.code

        if self.icon is not None:
            result['Icon'] = self.icon

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CnName') is not None:
            self.cn_name = m.get('CnName')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Icon') is not None:
            self.icon = m.get('Icon')

        return self

