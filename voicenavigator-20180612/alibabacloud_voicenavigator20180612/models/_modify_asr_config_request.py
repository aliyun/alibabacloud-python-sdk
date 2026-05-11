# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyAsrConfigRequest(DaraModel):
    def __init__(
        self,
        app_key: str = None,
        asr_acoustic_model_id: str = None,
        asr_class_vocabulary_id: str = None,
        asr_customization_id: str = None,
        asr_overrides: str = None,
        asr_vocabulary_id: str = None,
        config_level: int = None,
        engine: str = None,
        entry_id: str = None,
        nls_service_type: str = None,
    ):
        self.app_key = app_key
        self.asr_acoustic_model_id = asr_acoustic_model_id
        self.asr_class_vocabulary_id = asr_class_vocabulary_id
        self.asr_customization_id = asr_customization_id
        self.asr_overrides = asr_overrides
        self.asr_vocabulary_id = asr_vocabulary_id
        self.config_level = config_level
        self.engine = engine
        self.entry_id = entry_id
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

        if self.config_level is not None:
            result['ConfigLevel'] = self.config_level

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.entry_id is not None:
            result['EntryId'] = self.entry_id

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

        if m.get('ConfigLevel') is not None:
            self.config_level = m.get('ConfigLevel')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EntryId') is not None:
            self.entry_id = m.get('EntryId')

        if m.get('NlsServiceType') is not None:
            self.nls_service_type = m.get('NlsServiceType')

        return self

