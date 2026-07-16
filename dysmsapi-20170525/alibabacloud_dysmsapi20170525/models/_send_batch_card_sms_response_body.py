# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dysmsapi20170525 import models as main_models
from darabonba.model import DaraModel

class SendBatchCardSmsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.SendBatchCardSmsResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The request status code.
        # * If **OK** is returned, the request is successful.
        # * For information about other error codes, see [API error codes](https://help.aliyun.com/document_detail/101346.html).
        self.code = code
        # The returned data.
        self.data = data
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call is successful. Valid values:
        # 
        # - **true**: The call is successful.
        # 
        # - **false**: The call fails.
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
            temp_model = main_models.SendBatchCardSmsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class SendBatchCardSmsResponseBodyData(DaraModel):
    def __init__(
        self,
        biz_card_id: str = None,
        biz_digital_id: str = None,
        biz_sms_id: str = None,
        card_tmp_state: int = None,
        media_mobiles: str = None,
        not_media_mobiles: str = None,
    ):
        # The ID of the card SMS sending task.
        self.biz_card_id = biz_card_id
        # The ID of the digital SMS sending task.
        self.biz_digital_id = biz_digital_id
        # The ID of the text SMS sending task.
        self.biz_sms_id = biz_sms_id
        # The review status of the card SMS template. Valid values:
        # - **0**: Under review.
        # - **1**: Approved.
        # - **2**: Rejected.
        # > For SMS messages that are rejected, you can configure the fallback process by using the **FallbackType** parameter.
        self.card_tmp_state = card_tmp_state
        # The mobile phone numbers that receive the card SMS messages.
        self.media_mobiles = media_mobiles
        # The fallback phone numbers.
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

