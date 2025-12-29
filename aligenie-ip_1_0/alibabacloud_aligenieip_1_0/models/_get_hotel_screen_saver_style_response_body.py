# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aligenieip_1_0 import models as main_models
from darabonba.model import DaraModel

class GetHotelScreenSaverStyleResponseBody(DaraModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        result: List[main_models.GetHotelScreenSaverStyleResponseBodyResult] = None,
        status_code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.status_code is not None:
            result['StatusCode'] = self.status_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.GetHotelScreenSaverStyleResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')

        return self

class GetHotelScreenSaverStyleResponseBodyResult(DaraModel):
    def __init__(
        self,
        cn_name: str = None,
        code: str = None,
        en_name: str = None,
        pic_url: str = None,
    ):
        self.cn_name = cn_name
        self.code = code
        self.en_name = en_name
        self.pic_url = pic_url

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

        if self.en_name is not None:
            result['EnName'] = self.en_name

        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CnName') is not None:
            self.cn_name = m.get('CnName')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('EnName') is not None:
            self.en_name = m.get('EnName')

        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')

        return self

