# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_pairecservice20221213 import models as main_models
from darabonba.model import DaraModel

class ShoppingAssistantResponseBody(DaraModel):
    def __init__(
        self,
        citation: main_models.ShoppingAssistantResponseBodyCitation = None,
        content: str = None,
        conversation_id: str = None,
        error_code: str = None,
        event: str = None,
        request_id: str = None,
        result: main_models.ShoppingAssistantResponseBodyResult = None,
        session_id: str = None,
        stop_reason: str = None,
    ):
        # The citation information.
        self.citation = citation
        # The returned content.
        self.content = content
        # The session ID.
        self.conversation_id = conversation_id
        # The error message.
        self.error_code = error_code
        # The event.
        self.event = event
        # The request ID.
        self.request_id = request_id
        # The result details.
        self.result = result
        # The session ID.
        self.session_id = session_id
        # The stop reason.
        self.stop_reason = stop_reason

    def validate(self):
        if self.citation:
            self.citation.validate()
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.citation is not None:
            result['Citation'] = self.citation.to_map()

        if self.content is not None:
            result['Content'] = self.content

        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.event is not None:
            result['Event'] = self.event

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.stop_reason is not None:
            result['StopReason'] = self.stop_reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Citation') is not None:
            temp_model = main_models.ShoppingAssistantResponseBodyCitation()
            self.citation = temp_model.from_map(m.get('Citation'))

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Event') is not None:
            self.event = m.get('Event')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.ShoppingAssistantResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('StopReason') is not None:
            self.stop_reason = m.get('StopReason')

        return self

class ShoppingAssistantResponseBodyResult(DaraModel):
    def __init__(
        self,
        citation: main_models.ShoppingAssistantResponseBodyResultCitation = None,
        content: str = None,
        error_code: str = None,
        step_info: main_models.ShoppingAssistantResponseBodyResultStepInfo = None,
        stop_reason: str = None,
    ):
        # The citation information.
        self.citation = citation
        # The returned content.
        self.content = content
        # The error message.
        self.error_code = error_code
        # The step information.
        self.step_info = step_info
        # The stop reason.
        self.stop_reason = stop_reason

    def validate(self):
        if self.citation:
            self.citation.validate()
        if self.step_info:
            self.step_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.citation is not None:
            result['Citation'] = self.citation.to_map()

        if self.content is not None:
            result['Content'] = self.content

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.step_info is not None:
            result['StepInfo'] = self.step_info.to_map()

        if self.stop_reason is not None:
            result['StopReason'] = self.stop_reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Citation') is not None:
            temp_model = main_models.ShoppingAssistantResponseBodyResultCitation()
            self.citation = temp_model.from_map(m.get('Citation'))

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('StepInfo') is not None:
            temp_model = main_models.ShoppingAssistantResponseBodyResultStepInfo()
            self.step_info = temp_model.from_map(m.get('StepInfo'))

        if m.get('StopReason') is not None:
            self.stop_reason = m.get('StopReason')

        return self

class ShoppingAssistantResponseBodyResultStepInfo(DaraModel):
    def __init__(
        self,
        step: str = None,
    ):
        # The step.
        self.step = step

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.step is not None:
            result['Step'] = self.step

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Step') is not None:
            self.step = m.get('Step')

        return self

class ShoppingAssistantResponseBodyResultCitation(DaraModel):
    def __init__(
        self,
        item_id: str = None,
        type: str = None,
    ):
        # The ID of the item.
        self.item_id = item_id
        # The reference data type. Fixed value: item.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.item_id is not None:
            result['ItemId'] = self.item_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ShoppingAssistantResponseBodyCitation(DaraModel):
    def __init__(
        self,
        item_id: str = None,
        type: str = None,
    ):
        # The ID of the `item`.
        self.item_id = item_id
        # The reference data type. Fixed value: `item`.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.item_id is not None:
            result['ItemId'] = self.item_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

