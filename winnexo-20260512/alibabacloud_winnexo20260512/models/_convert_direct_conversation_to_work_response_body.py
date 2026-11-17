# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConvertDirectConversationToWorkResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        conversion_id: str = None,
        converted_rounds: int = None,
        history_scope: str = None,
        message: str = None,
        request_id: str = None,
        retryable: bool = None,
        source_epoch: int = None,
        source_session_id: str = None,
        status: str = None,
        target_session_id: str = None,
        through_sequence: int = None,
        work_mode: str = None,
    ):
        # The response status code.
        self.code = code
        # The session conversion record ID.
        self.conversion_id = conversion_id
        # The number of converted conversation turns.
        self.converted_rounds = converted_rounds
        # The scope of the converted historical messages.
        self.history_scope = history_scope
        # The response message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Specifies whether retries are supported.
        self.retryable = retryable
        # The source session version identifier.
        self.source_epoch = source_epoch
        # The source session ID.
        self.source_session_id = source_session_id
        # The conversion status.
        self.status = status
        # The target work session ID.
        self.target_session_id = target_session_id
        # The cutoff message sequence number for the conversion.
        self.through_sequence = through_sequence
        # The work session mode.
        self.work_mode = work_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.conversion_id is not None:
            result['conversionId'] = self.conversion_id

        if self.converted_rounds is not None:
            result['convertedRounds'] = self.converted_rounds

        if self.history_scope is not None:
            result['historyScope'] = self.history_scope

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.retryable is not None:
            result['retryable'] = self.retryable

        if self.source_epoch is not None:
            result['sourceEpoch'] = self.source_epoch

        if self.source_session_id is not None:
            result['sourceSessionId'] = self.source_session_id

        if self.status is not None:
            result['status'] = self.status

        if self.target_session_id is not None:
            result['targetSessionId'] = self.target_session_id

        if self.through_sequence is not None:
            result['throughSequence'] = self.through_sequence

        if self.work_mode is not None:
            result['workMode'] = self.work_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('conversionId') is not None:
            self.conversion_id = m.get('conversionId')

        if m.get('convertedRounds') is not None:
            self.converted_rounds = m.get('convertedRounds')

        if m.get('historyScope') is not None:
            self.history_scope = m.get('historyScope')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('retryable') is not None:
            self.retryable = m.get('retryable')

        if m.get('sourceEpoch') is not None:
            self.source_epoch = m.get('sourceEpoch')

        if m.get('sourceSessionId') is not None:
            self.source_session_id = m.get('sourceSessionId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('targetSessionId') is not None:
            self.target_session_id = m.get('targetSessionId')

        if m.get('throughSequence') is not None:
            self.through_sequence = m.get('throughSequence')

        if m.get('workMode') is not None:
            self.work_mode = m.get('workMode')

        return self

