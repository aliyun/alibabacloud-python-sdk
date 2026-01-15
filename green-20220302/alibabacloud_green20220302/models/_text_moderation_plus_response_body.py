# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_green20220302 import models as main_models
from darabonba.model import DaraModel

class TextModerationPlusResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.TextModerationPlusResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The returned HTTP status code. The status code 200 indicates that the request was successful.
        self.code = code
        # The moderation results.
        self.data = data
        # The message that is returned in response to the request.
        self.message = message
        # Id of the request
        self.request_id = request_id

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

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.TextModerationPlusResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class TextModerationPlusResponseBodyData(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        advice: List[main_models.TextModerationPlusResponseBodyDataAdvice] = None,
        attack_level: str = None,
        attack_result: List[main_models.TextModerationPlusResponseBodyDataAttackResult] = None,
        data_id: str = None,
        detected_language: str = None,
        ext: main_models.TextModerationPlusResponseBodyDataExt = None,
        manual_task_id: str = None,
        result: List[main_models.TextModerationPlusResponseBodyDataResult] = None,
        risk_level: str = None,
        score: float = None,
        sensitive_level: str = None,
        sensitive_result: List[main_models.TextModerationPlusResponseBodyDataSensitiveResult] = None,
        translated_content: str = None,
    ):
        self.account_id = account_id
        # The suggestion.
        self.advice = advice
        # The level of prompt attack
        self.attack_level = attack_level
        # The result of prompt attack detect
        self.attack_result = attack_result
        # The id of data
        self.data_id = data_id
        self.detected_language = detected_language
        self.ext = ext
        self.manual_task_id = manual_task_id
        # The results.
        self.result = result
        # Risk Level
        self.risk_level = risk_level
        # The score.
        self.score = score
        # The level of sensitivity data
        self.sensitive_level = sensitive_level
        # The result of sensitivity data detect
        self.sensitive_result = sensitive_result
        self.translated_content = translated_content

    def validate(self):
        if self.advice:
            for v1 in self.advice:
                 if v1:
                    v1.validate()
        if self.attack_result:
            for v1 in self.attack_result:
                 if v1:
                    v1.validate()
        if self.ext:
            self.ext.validate()
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()
        if self.sensitive_result:
            for v1 in self.sensitive_result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        result['Advice'] = []
        if self.advice is not None:
            for k1 in self.advice:
                result['Advice'].append(k1.to_map() if k1 else None)

        if self.attack_level is not None:
            result['AttackLevel'] = self.attack_level

        result['AttackResult'] = []
        if self.attack_result is not None:
            for k1 in self.attack_result:
                result['AttackResult'].append(k1.to_map() if k1 else None)

        if self.data_id is not None:
            result['DataId'] = self.data_id

        if self.detected_language is not None:
            result['DetectedLanguage'] = self.detected_language

        if self.ext is not None:
            result['Ext'] = self.ext.to_map()

        if self.manual_task_id is not None:
            result['ManualTaskId'] = self.manual_task_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.score is not None:
            result['Score'] = self.score

        if self.sensitive_level is not None:
            result['SensitiveLevel'] = self.sensitive_level

        result['SensitiveResult'] = []
        if self.sensitive_result is not None:
            for k1 in self.sensitive_result:
                result['SensitiveResult'].append(k1.to_map() if k1 else None)

        if self.translated_content is not None:
            result['TranslatedContent'] = self.translated_content

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        self.advice = []
        if m.get('Advice') is not None:
            for k1 in m.get('Advice'):
                temp_model = main_models.TextModerationPlusResponseBodyDataAdvice()
                self.advice.append(temp_model.from_map(k1))

        if m.get('AttackLevel') is not None:
            self.attack_level = m.get('AttackLevel')

        self.attack_result = []
        if m.get('AttackResult') is not None:
            for k1 in m.get('AttackResult'):
                temp_model = main_models.TextModerationPlusResponseBodyDataAttackResult()
                self.attack_result.append(temp_model.from_map(k1))

        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')

        if m.get('DetectedLanguage') is not None:
            self.detected_language = m.get('DetectedLanguage')

        if m.get('Ext') is not None:
            temp_model = main_models.TextModerationPlusResponseBodyDataExt()
            self.ext = temp_model.from_map(m.get('Ext'))

        if m.get('ManualTaskId') is not None:
            self.manual_task_id = m.get('ManualTaskId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.TextModerationPlusResponseBodyDataResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('SensitiveLevel') is not None:
            self.sensitive_level = m.get('SensitiveLevel')

        self.sensitive_result = []
        if m.get('SensitiveResult') is not None:
            for k1 in m.get('SensitiveResult'):
                temp_model = main_models.TextModerationPlusResponseBodyDataSensitiveResult()
                self.sensitive_result.append(temp_model.from_map(k1))

        if m.get('TranslatedContent') is not None:
            self.translated_content = m.get('TranslatedContent')

        return self

class TextModerationPlusResponseBodyDataSensitiveResult(DaraModel):
    def __init__(
        self,
        description: str = None,
        label: str = None,
        sensitive_data: List[str] = None,
        sensitive_level: str = None,
    ):
        # Description
        self.description = description
        # The label
        self.label = label
        # The sensitive data.
        self.sensitive_data = sensitive_data
        # The level of sensitivity data
        self.sensitive_level = sensitive_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.label is not None:
            result['Label'] = self.label

        if self.sensitive_data is not None:
            result['SensitiveData'] = self.sensitive_data

        if self.sensitive_level is not None:
            result['SensitiveLevel'] = self.sensitive_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('SensitiveData') is not None:
            self.sensitive_data = m.get('SensitiveData')

        if m.get('SensitiveLevel') is not None:
            self.sensitive_level = m.get('SensitiveLevel')

        return self

class TextModerationPlusResponseBodyDataResult(DaraModel):
    def __init__(
        self,
        confidence: float = None,
        customized_hit: List[main_models.TextModerationPlusResponseBodyDataResultCustomizedHit] = None,
        description: str = None,
        label: str = None,
        risk_positions: List[main_models.TextModerationPlusResponseBodyDataResultRiskPositions] = None,
        risk_words: str = None,
    ):
        # The score of the confidence level. Valid values: 0 to 100. The value is accurate to two decimal places.
        self.confidence = confidence
        # The custom term hit by the moderated content.
        self.customized_hit = customized_hit
        # The description of the label.
        self.description = description
        # The label.
        self.label = label
        self.risk_positions = risk_positions
        # The term hit by the moderated content.
        self.risk_words = risk_words

    def validate(self):
        if self.customized_hit:
            for v1 in self.customized_hit:
                 if v1:
                    v1.validate()
        if self.risk_positions:
            for v1 in self.risk_positions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.confidence is not None:
            result['Confidence'] = self.confidence

        result['CustomizedHit'] = []
        if self.customized_hit is not None:
            for k1 in self.customized_hit:
                result['CustomizedHit'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['Description'] = self.description

        if self.label is not None:
            result['Label'] = self.label

        result['RiskPositions'] = []
        if self.risk_positions is not None:
            for k1 in self.risk_positions:
                result['RiskPositions'].append(k1.to_map() if k1 else None)

        if self.risk_words is not None:
            result['RiskWords'] = self.risk_words

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')

        self.customized_hit = []
        if m.get('CustomizedHit') is not None:
            for k1 in m.get('CustomizedHit'):
                temp_model = main_models.TextModerationPlusResponseBodyDataResultCustomizedHit()
                self.customized_hit.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        self.risk_positions = []
        if m.get('RiskPositions') is not None:
            for k1 in m.get('RiskPositions'):
                temp_model = main_models.TextModerationPlusResponseBodyDataResultRiskPositions()
                self.risk_positions.append(temp_model.from_map(k1))

        if m.get('RiskWords') is not None:
            self.risk_words = m.get('RiskWords')

        return self

class TextModerationPlusResponseBodyDataResultRiskPositions(DaraModel):
    def __init__(
        self,
        end_pos: int = None,
        risk_word: str = None,
        start_pos: int = None,
    ):
        self.end_pos = end_pos
        self.risk_word = risk_word
        self.start_pos = start_pos

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_pos is not None:
            result['EndPos'] = self.end_pos

        if self.risk_word is not None:
            result['RiskWord'] = self.risk_word

        if self.start_pos is not None:
            result['StartPos'] = self.start_pos

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndPos') is not None:
            self.end_pos = m.get('EndPos')

        if m.get('RiskWord') is not None:
            self.risk_word = m.get('RiskWord')

        if m.get('StartPos') is not None:
            self.start_pos = m.get('StartPos')

        return self

class TextModerationPlusResponseBodyDataResultCustomizedHit(DaraModel):
    def __init__(
        self,
        key_words: str = None,
        lib_name: str = None,
    ):
        # The terms that are hit. Multiple terms are separated by commas (,).
        self.key_words = key_words
        # The library name.
        self.lib_name = lib_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key_words is not None:
            result['KeyWords'] = self.key_words

        if self.lib_name is not None:
            result['LibName'] = self.lib_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyWords') is not None:
            self.key_words = m.get('KeyWords')

        if m.get('LibName') is not None:
            self.lib_name = m.get('LibName')

        return self

class TextModerationPlusResponseBodyDataExt(DaraModel):
    def __init__(
        self,
        llm_content: main_models.TextModerationPlusResponseBodyDataExtLlmContent = None,
    ):
        self.llm_content = llm_content

    def validate(self):
        if self.llm_content:
            self.llm_content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.llm_content is not None:
            result['LlmContent'] = self.llm_content.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LlmContent') is not None:
            temp_model = main_models.TextModerationPlusResponseBodyDataExtLlmContent()
            self.llm_content = temp_model.from_map(m.get('LlmContent'))

        return self

class TextModerationPlusResponseBodyDataExtLlmContent(DaraModel):
    def __init__(
        self,
        output_text: str = None,
    ):
        self.output_text = output_text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.output_text is not None:
            result['OutputText'] = self.output_text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutputText') is not None:
            self.output_text = m.get('OutputText')

        return self

class TextModerationPlusResponseBodyDataAttackResult(DaraModel):
    def __init__(
        self,
        attack_level: str = None,
        confidence: float = None,
        description: str = None,
        label: str = None,
    ):
        # The level of prompt attack
        self.attack_level = attack_level
        # The confidence
        self.confidence = confidence
        # Description
        self.description = description
        # The label
        self.label = label

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attack_level is not None:
            result['AttackLevel'] = self.attack_level

        if self.confidence is not None:
            result['Confidence'] = self.confidence

        if self.description is not None:
            result['Description'] = self.description

        if self.label is not None:
            result['Label'] = self.label

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttackLevel') is not None:
            self.attack_level = m.get('AttackLevel')

        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        return self

class TextModerationPlusResponseBodyDataAdvice(DaraModel):
    def __init__(
        self,
        answer: str = None,
        hit_label: str = None,
        hit_lib_name: str = None,
    ):
        # The answer.
        self.answer = answer
        # Hit Label
        self.hit_label = hit_label
        # Hit Library Name
        self.hit_lib_name = hit_lib_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.answer is not None:
            result['Answer'] = self.answer

        if self.hit_label is not None:
            result['HitLabel'] = self.hit_label

        if self.hit_lib_name is not None:
            result['HitLibName'] = self.hit_lib_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Answer') is not None:
            self.answer = m.get('Answer')

        if m.get('HitLabel') is not None:
            self.hit_label = m.get('HitLabel')

        if m.get('HitLibName') is not None:
            self.hit_lib_name = m.get('HitLibName')

        return self

