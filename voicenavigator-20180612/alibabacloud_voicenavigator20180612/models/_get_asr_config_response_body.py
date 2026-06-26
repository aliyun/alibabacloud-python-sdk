# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_voicenavigator20180612 import models as main_models
from darabonba.model import DaraModel

class GetAsrConfigResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetAsrConfigResponseBodyData = None,
        error_msg: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code.
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        self.error_msg = error_msg
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
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

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

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
            temp_model = main_models.GetAsrConfigResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetAsrConfigResponseBodyData(DaraModel):
    def __init__(
        self,
        app_key: str = None,
        asr_acoustic_model_id: str = None,
        asr_class_vocabulary_id: str = None,
        asr_customization_id: str = None,
        asr_overrides: str = None,
        asr_vocabulary_id: str = None,
        engine: str = None,
        engine_xufei: str = None,
        nls_service_type: str = None,
    ):
        # The application key.
        self.app_key = app_key
        # The acoustic model ID.
        self.asr_acoustic_model_id = asr_acoustic_model_id
        # The ASR class vocabulary ID.
        self.asr_class_vocabulary_id = asr_class_vocabulary_id
        # The customization ID.
        self.asr_customization_id = asr_customization_id
        self.asr_overrides = asr_overrides
        # The vocabulary ID. You can view the ID on the [ASR Vocabulary Management page](https://aiccs.console.aliyun.com/sentence/vocab?spm=a2c4g.11186623.0.0.7f9bf965IKBpsi).
        self.asr_vocabulary_id = asr_vocabulary_id
        # The speech engine.
        self.engine = engine
        # Parameters for the iFLYTEK engine.
        self.engine_xufei = engine_xufei
        # The NLS service type.
        self.nls_service_type = nls_service_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_key is not None:
            result['AppKey'] = self.app_key

        if self.asr_acoustic_model_id is not None:
            result['AsrAcousticModelId'] = self.asr_acoustic_model_id

        if self.asr_class_vocabulary_id is not None:
            result['AsrClassVocabularyId'] = self.asr_class_vocabulary_id

        if self.asr_customization_id is not None:
            result['AsrCustomizationId'] = self.asr_customization_id

        if self.asr_overrides is not None:
            result['AsrOverrides'] = self.asr_overrides

        if self.asr_vocabulary_id is not None:
            result['AsrVocabularyId'] = self.asr_vocabulary_id

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_xufei is not None:
            result['EngineXufei'] = self.engine_xufei

        if self.nls_service_type is not None:
            result['NlsServiceType'] = self.nls_service_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        if m.get('AsrAcousticModelId') is not None:
            self.asr_acoustic_model_id = m.get('AsrAcousticModelId')

        if m.get('AsrClassVocabularyId') is not None:
            self.asr_class_vocabulary_id = m.get('AsrClassVocabularyId')

        if m.get('AsrCustomizationId') is not None:
            self.asr_customization_id = m.get('AsrCustomizationId')

        if m.get('AsrOverrides') is not None:
            self.asr_overrides = m.get('AsrOverrides')

        if m.get('AsrVocabularyId') is not None:
            self.asr_vocabulary_id = m.get('AsrVocabularyId')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineXufei') is not None:
            self.engine_xufei = m.get('EngineXufei')

        if m.get('NlsServiceType') is not None:
            self.nls_service_type = m.get('NlsServiceType')

        return self

