# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dysmsapi20170525 import models as main_models
from darabonba.model import DaraModel

class SendCardSmsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.SendCardSmsResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 请求状态码。
        # * 返回OK代表请求成功。
        # * 其他错误码，请参见[错误码列表](https://help.aliyun.com/document_detail/101346.html)。
        self.code = code
        # 返回数据。
        self.data = data
        # 请求ID。
        self.request_id = request_id
        # 调用接口是否成功。取值：
        # 
        # - **true**：调用成功。
        # 
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
            temp_model = main_models.SendCardSmsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class SendCardSmsResponseBodyData(DaraModel):
    def __init__(
        self,
        biz_card_id: str = None,
        biz_digital_id: str = None,
        biz_sms_id: str = None,
        card_tmp_state: int = None,
        media_mobiles: str = None,
        not_media_mobiles: str = None,
    ):
        # 卡片短信发送ID。
        self.biz_card_id = biz_card_id
        # 数字短信发送ID。
        self.biz_digital_id = biz_digital_id
        # 文本短信发送ID。
        self.biz_sms_id = biz_sms_id
        # 卡片短信模板审核状态。取值：
        # - **0**：审核中。
        # - **1**：审核通过。
        # - **2**：审核不通过。
        # >  审核不通过的短信可通过**FallbackType**字段设置回落流程。
        self.card_tmp_state = card_tmp_state
        # 接收卡片短信的手机号。
        self.media_mobiles = media_mobiles
        # 回落的手机号。
        self.not_media_mobiles = not_media_mobiles

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_card_id is not None:
            result['BizCardId'] = self.biz_card_id

        if self.biz_digital_id is not None:
            result['BizDigitalId'] = self.biz_digital_id

        if self.biz_sms_id is not None:
            result['BizSmsId'] = self.biz_sms_id

        if self.card_tmp_state is not None:
            result['CardTmpState'] = self.card_tmp_state

        if self.media_mobiles is not None:
            result['MediaMobiles'] = self.media_mobiles

        if self.not_media_mobiles is not None:
            result['NotMediaMobiles'] = self.not_media_mobiles

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCardId') is not None:
            self.biz_card_id = m.get('BizCardId')

        if m.get('BizDigitalId') is not None:
            self.biz_digital_id = m.get('BizDigitalId')

        if m.get('BizSmsId') is not None:
            self.biz_sms_id = m.get('BizSmsId')

        if m.get('CardTmpState') is not None:
            self.card_tmp_state = m.get('CardTmpState')

        if m.get('MediaMobiles') is not None:
            self.media_mobiles = m.get('MediaMobiles')

        if m.get('NotMediaMobiles') is not None:
            self.not_media_mobiles = m.get('NotMediaMobiles')

        return self

