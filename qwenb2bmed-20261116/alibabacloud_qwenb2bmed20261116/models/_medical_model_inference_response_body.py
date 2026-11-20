# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_qwenb2bmed20261116 import models as main_models
from darabonba.model import DaraModel

class MedicalModelInferenceResponseBody(DaraModel):
    def __init__(
        self,
        audio_frames: List[main_models.MedicalModelInferenceResponseBodyAudioFrames] = None,
        communication: main_models.MedicalModelInferenceResponseBodyCommunication = None,
        data: main_models.MedicalModelInferenceResponseBodyData = None,
        error: main_models.MedicalModelInferenceResponseBodyError = None,
        error_code: Any = None,
        error_msg: str = None,
        request_id: str = None,
    ):
        # The optional list of audio frames in the response. This can be empty or omitted when no audio is present.
        self.audio_frames = audio_frames
        # The information used to associate response frames with the original business request and session.
        self.communication = communication
        # The business data returned in this response, including messages and optional extended information.
        self.data = data
        # The error details returned when a business call fails.
        self.error = error
        # The business status code.
        self.error_code = error_code
        # The business status description.
        self.error_msg = error_msg
        # The optional business request correlation ID. For the POP request ID, see x-acs-request-id.
        self.request_id = request_id

    def validate(self):
        if self.audio_frames:
            for v1 in self.audio_frames:
                 if v1:
                    v1.validate()
        if self.communication:
            self.communication.validate()
        if self.data:
            self.data.validate()
        if self.error:
            self.error.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['audioFrames'] = []
        if self.audio_frames is not None:
            for k1 in self.audio_frames:
                result['audioFrames'].append(k1.to_map() if k1 else None)

        if self.communication is not None:
            result['communication'] = self.communication.to_map()

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.error is not None:
            result['error'] = self.error.to_map()

        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.audio_frames = []
        if m.get('audioFrames') is not None:
            for k1 in m.get('audioFrames'):
                temp_model = main_models.MedicalModelInferenceResponseBodyAudioFrames()
                self.audio_frames.append(temp_model.from_map(k1))

        if m.get('communication') is not None:
            temp_model = main_models.MedicalModelInferenceResponseBodyCommunication()
            self.communication = temp_model.from_map(m.get('communication'))

        if m.get('data') is not None:
            temp_model = main_models.MedicalModelInferenceResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('error') is not None:
            temp_model = main_models.MedicalModelInferenceResponseBodyError()
            self.error = temp_model.from_map(m.get('error'))

        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class MedicalModelInferenceResponseBodyError(DaraModel):
    def __init__(
        self,
        code: Any = None,
        message: str = None,
        request_id: str = None,
    ):
        # The business error code used by the client to identify the failure type.
        self.code = code
        # The descriptive text of the business error.
        self.message = message
        # The business request correlation ID of the failed call, used for troubleshooting.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class MedicalModelInferenceResponseBodyData(DaraModel):
    def __init__(
        self,
        debug: Any = None,
        extra_info: main_models.MedicalModelInferenceResponseBodyDataExtraInfo = None,
        messages: List[main_models.MedicalModelInferenceResponseBodyDataMessages] = None,
    ):
        # The optional debug information included in the business response.
        self.debug = debug
        # The extended business information, which may include inputResources.
        self.extra_info = extra_info
        # The list of messages returned in this business response or the current streaming response frame.
        self.messages = messages

    def validate(self):
        if self.extra_info:
            self.extra_info.validate()
        if self.messages:
            for v1 in self.messages:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.debug is not None:
            result['debug'] = self.debug

        if self.extra_info is not None:
            result['extraInfo'] = self.extra_info.to_map()

        result['messages'] = []
        if self.messages is not None:
            for k1 in self.messages:
                result['messages'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('debug') is not None:
            self.debug = m.get('debug')

        if m.get('extraInfo') is not None:
            temp_model = main_models.MedicalModelInferenceResponseBodyDataExtraInfo()
            self.extra_info = temp_model.from_map(m.get('extraInfo'))

        self.messages = []
        if m.get('messages') is not None:
            for k1 in m.get('messages'):
                temp_model = main_models.MedicalModelInferenceResponseBodyDataMessages()
                self.messages.append(temp_model.from_map(k1))

        return self

class MedicalModelInferenceResponseBodyDataMessages(DaraModel):
    def __init__(
        self,
        content: Any = None,
        meta_data: main_models.MedicalModelInferenceResponseBodyDataMessagesMetaData = None,
        mime_type: str = None,
        status: str = None,
    ):
        # The text or content corresponding to the message type.
        self.content = content
        # The extended metadata associated with this message.
        self.meta_data = meta_data
        # The type of the message.
        self.mime_type = mime_type
        # The status of the business message.
        self.status = status

    def validate(self):
        if self.meta_data:
            self.meta_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.meta_data is not None:
            result['metaData'] = self.meta_data.to_map()

        if self.mime_type is not None:
            result['mimeType'] = self.mime_type

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('metaData') is not None:
            temp_model = main_models.MedicalModelInferenceResponseBodyDataMessagesMetaData()
            self.meta_data = temp_model.from_map(m.get('metaData'))

        if m.get('mimeType') is not None:
            self.mime_type = m.get('mimeType')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

class MedicalModelInferenceResponseBodyDataMessagesMetaData(DaraModel):
    def __init__(
        self,
        bar_title: str = None,
        content: Any = None,
        multi_load: List[main_models.MedicalModelInferenceResponseBodyDataMessagesMetaDataMultiLoad] = None,
        source_seq: str = None,
        type: str = None,
    ):
        # The title of the status bar.
        self.bar_title = bar_title
        # The content of the metadata.
        self.content = content
        # The list of structured content associated with the body, such as image-text cards, returned by message type.
        self.multi_load = multi_load
        # The source identifier.
        self.source_seq = source_seq
        # The type of the metadata.
        self.type = type

    def validate(self):
        if self.multi_load:
            for v1 in self.multi_load:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bar_title is not None:
            result['barTitle'] = self.bar_title

        if self.content is not None:
            result['content'] = self.content

        result['multiLoad'] = []
        if self.multi_load is not None:
            for k1 in self.multi_load:
                result['multiLoad'].append(k1.to_map() if k1 else None)

        if self.source_seq is not None:
            result['sourceSeq'] = self.source_seq

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('barTitle') is not None:
            self.bar_title = m.get('barTitle')

        if m.get('content') is not None:
            self.content = m.get('content')

        self.multi_load = []
        if m.get('multiLoad') is not None:
            for k1 in m.get('multiLoad'):
                temp_model = main_models.MedicalModelInferenceResponseBodyDataMessagesMetaDataMultiLoad()
                self.multi_load.append(temp_model.from_map(k1))

        if m.get('sourceSeq') is not None:
            self.source_seq = m.get('sourceSeq')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class MedicalModelInferenceResponseBodyDataMessagesMetaDataMultiLoad(DaraModel):
    def __init__(
        self,
        content: Any = None,
        source_seq: str = None,
        type: str = None,
    ):
        # The content of the card.
        self.content = content
        # The reference identifier of the card.
        self.source_seq = source_seq
        # The type of the card.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.source_seq is not None:
            result['sourceSeq'] = self.source_seq

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('sourceSeq') is not None:
            self.source_seq = m.get('sourceSeq')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class MedicalModelInferenceResponseBodyDataExtraInfo(DaraModel):
    def __init__(
        self,
        input_resources: List[main_models.MedicalModelInferenceResponseBodyDataExtraInfoInputResources] = None,
    ):
        # The transfer results of the input resources for this round.
        self.input_resources = input_resources

    def validate(self):
        if self.input_resources:
            for v1 in self.input_resources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['inputResources'] = []
        if self.input_resources is not None:
            for k1 in self.input_resources:
                result['inputResources'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.input_resources = []
        if m.get('inputResources') is not None:
            for k1 in m.get('inputResources'):
                temp_model = main_models.MedicalModelInferenceResponseBodyDataExtraInfoInputResources()
                self.input_resources.append(temp_model.from_map(k1))

        return self

class MedicalModelInferenceResponseBodyDataExtraInfoInputResources(DaraModel):
    def __init__(
        self,
        content_index: int = None,
        file_name: str = None,
        resource_id: str = None,
        type: str = None,
        url: str = None,
    ):
        # The index of the original content block.
        self.content_index = content_index
        # The name of the resource file.
        self.file_name = file_name
        # The ID of the transferred resource.
        self.resource_id = resource_id
        # The type of the input resource.
        self.type = type
        # The URL of the transferred resource.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_index is not None:
            result['contentIndex'] = self.content_index

        if self.file_name is not None:
            result['fileName'] = self.file_name

        if self.resource_id is not None:
            result['resourceId'] = self.resource_id

        if self.type is not None:
            result['type'] = self.type

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contentIndex') is not None:
            self.content_index = m.get('contentIndex')

        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')

        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

class MedicalModelInferenceResponseBodyCommunication(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        response_id: int = None,
        session_id: str = None,
    ):
        # The business request ID. This is the same as the business request ID when present.
        self.request_id = request_id
        # The ID of the business response frame.
        self.response_id = response_id
        # The ID of the customer session.
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.response_id is not None:
            result['responseId'] = self.response_id

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('responseId') is not None:
            self.response_id = m.get('responseId')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        return self

class MedicalModelInferenceResponseBodyAudioFrames(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        last: bool = None,
        message: str = None,
        request_id: str = None,
        type: str = None,
    ):
        # The error code.
        self.code = code
        # The encoded audio data.
        self.data = data
        # Indicates whether this is the last audio frame.
        self.last = last
        # The error description.
        self.message = message
        # The request correlation ID.
        self.request_id = request_id
        # The type of the audio or error frame.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data

        if self.last is not None:
            result['last'] = self.last

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            self.data = m.get('data')

        if m.get('last') is not None:
            self.last = m.get('last')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

