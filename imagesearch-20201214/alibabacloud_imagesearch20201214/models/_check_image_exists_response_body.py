# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_imagesearch20201214 import models as main_models
from darabonba.model import DaraModel

class CheckImageExistsResponseBody(DaraModel):
    def __init__(
        self,
        auctions: main_models.CheckImageExistsResponseBodyAuctions = None,
        code: int = None,
        exists: bool = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.auctions = auctions
        self.code = code
        self.exists = exists
        self.msg = msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.auctions:
            self.auctions.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auctions is not None:
            result['Auctions'] = self.auctions.to_map()

        if self.code is not None:
            result['Code'] = self.code

        if self.exists is not None:
            result['Exists'] = self.exists

        if self.msg is not None:
            result['Msg'] = self.msg

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Auctions') is not None:
            temp_model = main_models.CheckImageExistsResponseBodyAuctions()
            self.auctions = temp_model.from_map(m.get('Auctions'))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Exists') is not None:
            self.exists = m.get('Exists')

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class CheckImageExistsResponseBodyAuctions(DaraModel):
    def __init__(
        self,
        category_id: int = None,
        custom_content: str = None,
        int_attr: int = None,
        int_attr_2: int = None,
        int_attr_3: int = None,
        int_attr_4: int = None,
        pic_name: str = None,
        product_id: str = None,
        str_attr: str = None,
        str_attr_2: str = None,
        str_attr_3: str = None,
        str_attr_4: str = None,
    ):
        self.category_id = category_id
        self.custom_content = custom_content
        self.int_attr = int_attr
        self.int_attr_2 = int_attr_2
        self.int_attr_3 = int_attr_3
        self.int_attr_4 = int_attr_4
        self.pic_name = pic_name
        self.product_id = product_id
        self.str_attr = str_attr
        self.str_attr_2 = str_attr_2
        self.str_attr_3 = str_attr_3
        self.str_attr_4 = str_attr_4

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.custom_content is not None:
            result['CustomContent'] = self.custom_content

        if self.int_attr is not None:
            result['IntAttr'] = self.int_attr

        if self.int_attr_2 is not None:
            result['IntAttr2'] = self.int_attr_2

        if self.int_attr_3 is not None:
            result['IntAttr3'] = self.int_attr_3

        if self.int_attr_4 is not None:
            result['IntAttr4'] = self.int_attr_4

        if self.pic_name is not None:
            result['PicName'] = self.pic_name

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.str_attr is not None:
            result['StrAttr'] = self.str_attr

        if self.str_attr_2 is not None:
            result['StrAttr2'] = self.str_attr_2

        if self.str_attr_3 is not None:
            result['StrAttr3'] = self.str_attr_3

        if self.str_attr_4 is not None:
            result['StrAttr4'] = self.str_attr_4

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('CustomContent') is not None:
            self.custom_content = m.get('CustomContent')

        if m.get('IntAttr') is not None:
            self.int_attr = m.get('IntAttr')

        if m.get('IntAttr2') is not None:
            self.int_attr_2 = m.get('IntAttr2')

        if m.get('IntAttr3') is not None:
            self.int_attr_3 = m.get('IntAttr3')

        if m.get('IntAttr4') is not None:
            self.int_attr_4 = m.get('IntAttr4')

        if m.get('PicName') is not None:
            self.pic_name = m.get('PicName')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('StrAttr') is not None:
            self.str_attr = m.get('StrAttr')

        if m.get('StrAttr2') is not None:
            self.str_attr_2 = m.get('StrAttr2')

        if m.get('StrAttr3') is not None:
            self.str_attr_3 = m.get('StrAttr3')

        if m.get('StrAttr4') is not None:
            self.str_attr_4 = m.get('StrAttr4')

        return self

