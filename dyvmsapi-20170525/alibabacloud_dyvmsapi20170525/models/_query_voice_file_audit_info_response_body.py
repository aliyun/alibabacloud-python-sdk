# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dyvmsapi20170525 import models as main_models
from darabonba.model import DaraModel

class QueryVoiceFileAuditInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.QueryVoiceFileAuditInfoResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code.
        # 
        # The value OK indicates that the request was successful. For more information about other response codes, see [API error codes](https://help.aliyun.com/document_detail/112502.html).
        self.code = code
        # The response parameters.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.QueryVoiceFileAuditInfoResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QueryVoiceFileAuditInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        audit_state: str = None,
        reject_info: str = None,
        voice_code: str = None,
    ):
        # The review state of the voice file. Valid values:
        # 
        # *   **AUDIT_STATE_INIT**: The voice file was under review.
        # *   **AUDIT_STATE_PASS**: The voice file was approved.
        # *   **AUDIT_STATE_NOT_PASS**: The voice file was rejected.
        # *   **AUDIT_STATE_UPLOADING**: The voice file was approved and is being uploaded.
        # *   **AUDIT_STATE_REDOING**: The voice file was being reprocessed.
        # *   **AUDIT_SATE_CANCEL**: The review of the voice file was canceled.
        # *   **AUDIT_PAUSE**: The review of the voice file was suspended.
        # *   **AUDIT_ORDER_FINISHED**: The voice file was approved by the ticket system and was waiting for the review of the Internet service provider (ISP).
        self.audit_state = audit_state
        # The reason why the voice file was rejected.
        self.reject_info = reject_info
        # The code of the voice file.
        self.voice_code = voice_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audit_state is not None:
            result['AuditState'] = self.audit_state

        if self.reject_info is not None:
            result['RejectInfo'] = self.reject_info

        if self.voice_code is not None:
            result['VoiceCode'] = self.voice_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditState') is not None:
            self.audit_state = m.get('AuditState')

        if m.get('RejectInfo') is not None:
            self.reject_info = m.get('RejectInfo')

        if m.get('VoiceCode') is not None:
            self.voice_code = m.get('VoiceCode')

        return self

