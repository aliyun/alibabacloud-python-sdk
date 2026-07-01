# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dysmsapi20170525 import models as main_models
from darabonba.model import DaraModel

class GetCardSmsLinkResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetCardSmsLinkResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 请求状态码。取值：
        # - OK：代表请求成功。
        # - 其他错误码，请参见[错误码列表](https://help.aliyun.com/document_detail/101346.html)。
        self.code = code
        # 返回数据。
        self.data = data
        # 请求ID。
        self.request_id = request_id
        # 接口调用是否成功。取值：
        # 
        # - **true**：调用成功。
        # - **false**：调用失败。
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetCardSmsLinkResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetCardSmsLinkResponseBodyData(DaraModel):
    def __init__(
        self,
        card_phone_numbers: str = None,
        card_sign_names: str = None,
        card_sms_links: str = None,
        card_tmp_state: int = None,
        not_media_mobiles: str = None,
    ):
        # 支持卡片短信的手机号码。
        self.card_phone_numbers = card_phone_numbers
        # 用于申请卡片短信短链的短信签名，在发送时签名、接收号码、卡片短信短链要一一对应。
        self.card_sign_names = card_sign_names
        # 卡片短信短链。
        self.card_sms_links = card_sms_links
        # 卡片短信模板审核状态。取值：
        # - **0**：审核中。
        # - **1**：审核通过。
        # - **2**：审核不通过。
        # 
        # > 未审核通过的短信走回落流程。
        self.card_tmp_state = card_tmp_state
        # 不支持卡片短信的手机号。
        self.not_media_mobiles = not_media_mobiles

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.card_phone_numbers is not None:
            result['CardPhoneNumbers'] = self.card_phone_numbers

        if self.card_sign_names is not None:
            result['CardSignNames'] = self.card_sign_names

        if self.card_sms_links is not None:
            result['CardSmsLinks'] = self.card_sms_links

        if self.card_tmp_state is not None:
            result['CardTmpState'] = self.card_tmp_state

        if self.not_media_mobiles is not None:
            result['NotMediaMobiles'] = self.not_media_mobiles

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CardPhoneNumbers') is not None:
            self.card_phone_numbers = m.get('CardPhoneNumbers')

        if m.get('CardSignNames') is not None:
            self.card_sign_names = m.get('CardSignNames')

        if m.get('CardSmsLinks') is not None:
            self.card_sms_links = m.get('CardSmsLinks')

        if m.get('CardTmpState') is not None:
            self.card_tmp_state = m.get('CardTmpState')

        if m.get('NotMediaMobiles') is not None:
            self.not_media_mobiles = m.get('NotMediaMobiles')

        return self

