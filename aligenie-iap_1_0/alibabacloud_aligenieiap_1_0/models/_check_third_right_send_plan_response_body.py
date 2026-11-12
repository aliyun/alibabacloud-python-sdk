# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_aligenieiap_1_0 import models as main_models
from darabonba.model import DaraModel

class CheckThirdRightSendPlanResponseBody(DaraModel):
    def __init__(
        self,
        ret_code: int = None,
        ret_msg: str = None,
        ret_value: main_models.CheckThirdRightSendPlanResponseBodyRetValue = None,
    ):
        # Return code
        self.ret_code = ret_code
        # Error message
        self.ret_msg = ret_msg
        # Result of invoking the API
        self.ret_value = ret_value

    def validate(self):
        if self.ret_value:
            self.ret_value.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ret_code is not None:
            result['RetCode'] = self.ret_code

        if self.ret_msg is not None:
            result['RetMsg'] = self.ret_msg

        if self.ret_value is not None:
            result['RetValue'] = self.ret_value.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RetCode') is not None:
            self.ret_code = m.get('RetCode')

        if m.get('RetMsg') is not None:
            self.ret_msg = m.get('RetMsg')

        if m.get('RetValue') is not None:
            temp_model = main_models.CheckThirdRightSendPlanResponseBodyRetValue()
            self.ret_value = temp_model.from_map(m.get('RetValue'))

        return self

class CheckThirdRightSendPlanResponseBodyRetValue(DaraModel):
    def __init__(
        self,
        activate_date: str = None,
        card_type: int = None,
        channel_code: str = None,
        channel_name: str = None,
        extend_info: Dict[str, Any] = None,
        request_id: str = None,
        rights_expired_date: str = None,
    ):
        # Activation time
        self.activate_date = activate_date
        # Card type
        self.card_type = card_type
        # Channel code
        self.channel_code = channel_code
        # Channel Name
        self.channel_name = channel_name
        # Extension field
        self.extend_info = extend_info
        # Request ID
        self.request_id = request_id
        # Rights expiration time
        self.rights_expired_date = rights_expired_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activate_date is not None:
            result['ActivateDate'] = self.activate_date

        if self.card_type is not None:
            result['CardType'] = self.card_type

        if self.channel_code is not None:
            result['ChannelCode'] = self.channel_code

        if self.channel_name is not None:
            result['ChannelName'] = self.channel_name

        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.rights_expired_date is not None:
            result['RightsExpiredDate'] = self.rights_expired_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivateDate') is not None:
            self.activate_date = m.get('ActivateDate')

        if m.get('CardType') is not None:
            self.card_type = m.get('CardType')

        if m.get('ChannelCode') is not None:
            self.channel_code = m.get('ChannelCode')

        if m.get('ChannelName') is not None:
            self.channel_name = m.get('ChannelName')

        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RightsExpiredDate') is not None:
            self.rights_expired_date = m.get('RightsExpiredDate')

        return self

