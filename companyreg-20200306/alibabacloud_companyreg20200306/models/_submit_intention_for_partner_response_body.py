# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitIntentionForPartnerResponseBody(DaraModel):
    def __init__(
        self,
        error_msg: str = None,
        ext_info: str = None,
        intention_biz_id: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_msg = error_msg
        self.ext_info = ext_info
        self.intention_biz_id = intention_biz_id
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info

        if self.intention_biz_id is not None:
            result['IntentionBizId'] = self.intention_biz_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')

        if m.get('IntentionBizId') is not None:
            self.intention_biz_id = m.get('IntentionBizId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

