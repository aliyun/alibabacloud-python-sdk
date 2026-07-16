# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aisearchengine20260417 import models as main_models
from darabonba.model import DaraModel

class QaChatResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.QaChatResponseBodyData = None,
        event: str = None,
        id: str = None,
    ):
        # Protocol data
        self.data = data
        # Event type description:
        # 
        # 1. Lifecycle
        #    - start / finish
        #    - Marks the beginning and end of a message
        # 
        # 2. Text content
        #    - text-start / text-delta / text-end
        #    - Markdown text streaming output
        # 
        # 3. Inline media
        #    - data-image-info / data-video-info
        #    - Media cards in text-image/text-video mixed content
        # 
        # 4. Source references
        #    - data-reference
        #    - Unified source list (web / document / image / video)
        # 
        # 5. Inline references
        #    - data-document-ref
        #    - Perplexity-style inline document references
        # 
        # 6. Template video
        #    - data-template-video
        #    - Video cards output by AV template agent
        # 
        # 7. Template analysis
        #    - data-video-info / data-template-info / data-template-video-content
        #    - Analysis result data from AV template agent
        #    - Table-type templates such as "Speech Transcription", "Video Outline", and "Video-to-Script" are delivered at once via data-template-video-content
        # 
        # 8. Streaming JSON
        #    - json-start / json-delta / json-end
        #    - Incremental delta-only JSON streaming protocol
        #    - Used for structured JSON template analysis output such as "Action Expression"
        self.event = event
        # Request ID, same as requestId
        self.id = id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.event is not None:
            result['event'] = self.event

        if self.id is not None:
            result['id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.QaChatResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('event') is not None:
            self.event = m.get('event')

        if m.get('id') is not None:
            self.id = m.get('id')

        return self

class QaChatResponseBodyData(DaraModel):
    def __init__(
        self,
        data: str = None,
        delta: str = None,
        error_code: str = None,
        error_text: str = None,
        finish_reason: str = None,
        id: str = None,
        request_id: str = None,
        retryable: bool = None,
        type: str = None,
    ):
        # Structured response data
        self.data = data
        # Incremental text output
        self.delta = delta
        # See error code list
        self.error_code = error_code
        # See error code list
        self.error_text = error_text
        # Completion reason. When the value is stop, it indicates output is complete; on error, the output is the error reason.
        self.finish_reason = finish_reason
        # Unique identifier. For multi-segment text, different segments use different ids, while the id remains consistent within a text segment
        self.id = id
        # Request ID
        self.request_id = request_id
        # Whether the error is retryable, defaults to true
        self.retryable = retryable
        # Same as event
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data

        if self.delta is not None:
            result['delta'] = self.delta

        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.error_text is not None:
            result['errorText'] = self.error_text

        if self.finish_reason is not None:
            result['finishReason'] = self.finish_reason

        if self.id is not None:
            result['id'] = self.id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.retryable is not None:
            result['retryable'] = self.retryable

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')

        if m.get('delta') is not None:
            self.delta = m.get('delta')

        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorText') is not None:
            self.error_text = m.get('errorText')

        if m.get('finishReason') is not None:
            self.finish_reason = m.get('finishReason')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('retryable') is not None:
            self.retryable = m.get('retryable')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

