# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dianjin20240628 import models as main_models
from darabonba.model import DaraModel

class RealTimeDialogResponseBody(DaraModel):
    def __init__(
        self,
        choices: List[main_models.RealTimeDialogResponseBodyChoices] = None,
        created: str = None,
        id: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.choices = choices
        self.created = created
        self.id = id
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.choices:
            for v1 in self.choices:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['choices'] = []
        if self.choices is not None:
            for k1 in self.choices:
                result['choices'].append(k1.to_map() if k1 else None)

        if self.created is not None:
            result['created'] = self.created

        if self.id is not None:
            result['id'] = self.id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.choices = []
        if m.get('choices') is not None:
            for k1 in m.get('choices'):
                temp_model = main_models.RealTimeDialogResponseBodyChoices()
                self.choices.append(temp_model.from_map(k1))

        if m.get('created') is not None:
            self.created = m.get('created')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class RealTimeDialogResponseBodyChoices(DaraModel):
    def __init__(
        self,
        delta: main_models.RealTimeDialogResponseBodyChoicesDelta = None,
        finish_reason: str = None,
        index: int = None,
        message: main_models.RealTimeDialogResponseBodyChoicesMessage = None,
    ):
        self.delta = delta
        self.finish_reason = finish_reason
        self.index = index
        self.message = message

    def validate(self):
        if self.delta:
            self.delta.validate()
        if self.message:
            self.message.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delta is not None:
            result['delta'] = self.delta.to_map()

        if self.finish_reason is not None:
            result['finishReason'] = self.finish_reason

        if self.index is not None:
            result['index'] = self.index

        if self.message is not None:
            result['message'] = self.message.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('delta') is not None:
            temp_model = main_models.RealTimeDialogResponseBodyChoicesDelta()
            self.delta = temp_model.from_map(m.get('delta'))

        if m.get('finishReason') is not None:
            self.finish_reason = m.get('finishReason')

        if m.get('index') is not None:
            self.index = m.get('index')

        if m.get('message') is not None:
            temp_model = main_models.RealTimeDialogResponseBodyChoicesMessage()
            self.message = temp_model.from_map(m.get('message'))

        return self

class RealTimeDialogResponseBodyChoicesMessage(DaraModel):
    def __init__(
        self,
        analysis_process: str = None,
        call_time: str = None,
        hang_up_dialog: bool = None,
        intention_code: str = None,
        intention_name: str = None,
        intention_script: str = None,
        interrupt: bool = None,
        recommend_intention: str = None,
        recommend_script: str = None,
        self_directed_script: str = None,
        self_directed_script_full_content: str = None,
        skip_current_recognize: bool = None,
    ):
        self.analysis_process = analysis_process
        # time
        self.call_time = call_time
        self.hang_up_dialog = hang_up_dialog
        self.intention_code = intention_code
        self.intention_name = intention_name
        self.intention_script = intention_script
        self.interrupt = interrupt
        self.recommend_intention = recommend_intention
        self.recommend_script = recommend_script
        self.self_directed_script = self_directed_script
        self.self_directed_script_full_content = self_directed_script_full_content
        self.skip_current_recognize = skip_current_recognize

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.analysis_process is not None:
            result['analysisProcess'] = self.analysis_process

        if self.call_time is not None:
            result['callTime'] = self.call_time

        if self.hang_up_dialog is not None:
            result['hangUpDialog'] = self.hang_up_dialog

        if self.intention_code is not None:
            result['intentionCode'] = self.intention_code

        if self.intention_name is not None:
            result['intentionName'] = self.intention_name

        if self.intention_script is not None:
            result['intentionScript'] = self.intention_script

        if self.interrupt is not None:
            result['interrupt'] = self.interrupt

        if self.recommend_intention is not None:
            result['recommendIntention'] = self.recommend_intention

        if self.recommend_script is not None:
            result['recommendScript'] = self.recommend_script

        if self.self_directed_script is not None:
            result['selfDirectedScript'] = self.self_directed_script

        if self.self_directed_script_full_content is not None:
            result['selfDirectedScriptFullContent'] = self.self_directed_script_full_content

        if self.skip_current_recognize is not None:
            result['skipCurrentRecognize'] = self.skip_current_recognize

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('analysisProcess') is not None:
            self.analysis_process = m.get('analysisProcess')

        if m.get('callTime') is not None:
            self.call_time = m.get('callTime')

        if m.get('hangUpDialog') is not None:
            self.hang_up_dialog = m.get('hangUpDialog')

        if m.get('intentionCode') is not None:
            self.intention_code = m.get('intentionCode')

        if m.get('intentionName') is not None:
            self.intention_name = m.get('intentionName')

        if m.get('intentionScript') is not None:
            self.intention_script = m.get('intentionScript')

        if m.get('interrupt') is not None:
            self.interrupt = m.get('interrupt')

        if m.get('recommendIntention') is not None:
            self.recommend_intention = m.get('recommendIntention')

        if m.get('recommendScript') is not None:
            self.recommend_script = m.get('recommendScript')

        if m.get('selfDirectedScript') is not None:
            self.self_directed_script = m.get('selfDirectedScript')

        if m.get('selfDirectedScriptFullContent') is not None:
            self.self_directed_script_full_content = m.get('selfDirectedScriptFullContent')

        if m.get('skipCurrentRecognize') is not None:
            self.skip_current_recognize = m.get('skipCurrentRecognize')

        return self

class RealTimeDialogResponseBodyChoicesDelta(DaraModel):
    def __init__(
        self,
        analysis_process: str = None,
        call_time: str = None,
        hang_up_dialog: bool = None,
        intention_code: str = None,
        intention_name: str = None,
        intention_script: str = None,
        interrupt: bool = None,
        recommend_intention: str = None,
        recommend_script: str = None,
        self_directed_script: str = None,
        self_directed_script_full_content: str = None,
        skip_current_recognize: bool = None,
    ):
        self.analysis_process = analysis_process
        # time
        self.call_time = call_time
        self.hang_up_dialog = hang_up_dialog
        self.intention_code = intention_code
        self.intention_name = intention_name
        self.intention_script = intention_script
        self.interrupt = interrupt
        self.recommend_intention = recommend_intention
        self.recommend_script = recommend_script
        self.self_directed_script = self_directed_script
        self.self_directed_script_full_content = self_directed_script_full_content
        self.skip_current_recognize = skip_current_recognize

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.analysis_process is not None:
            result['analysisProcess'] = self.analysis_process

        if self.call_time is not None:
            result['callTime'] = self.call_time

        if self.hang_up_dialog is not None:
            result['hangUpDialog'] = self.hang_up_dialog

        if self.intention_code is not None:
            result['intentionCode'] = self.intention_code

        if self.intention_name is not None:
            result['intentionName'] = self.intention_name

        if self.intention_script is not None:
            result['intentionScript'] = self.intention_script

        if self.interrupt is not None:
            result['interrupt'] = self.interrupt

        if self.recommend_intention is not None:
            result['recommendIntention'] = self.recommend_intention

        if self.recommend_script is not None:
            result['recommendScript'] = self.recommend_script

        if self.self_directed_script is not None:
            result['selfDirectedScript'] = self.self_directed_script

        if self.self_directed_script_full_content is not None:
            result['selfDirectedScriptFullContent'] = self.self_directed_script_full_content

        if self.skip_current_recognize is not None:
            result['skipCurrentRecognize'] = self.skip_current_recognize

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('analysisProcess') is not None:
            self.analysis_process = m.get('analysisProcess')

        if m.get('callTime') is not None:
            self.call_time = m.get('callTime')

        if m.get('hangUpDialog') is not None:
            self.hang_up_dialog = m.get('hangUpDialog')

        if m.get('intentionCode') is not None:
            self.intention_code = m.get('intentionCode')

        if m.get('intentionName') is not None:
            self.intention_name = m.get('intentionName')

        if m.get('intentionScript') is not None:
            self.intention_script = m.get('intentionScript')

        if m.get('interrupt') is not None:
            self.interrupt = m.get('interrupt')

        if m.get('recommendIntention') is not None:
            self.recommend_intention = m.get('recommendIntention')

        if m.get('recommendScript') is not None:
            self.recommend_script = m.get('recommendScript')

        if m.get('selfDirectedScript') is not None:
            self.self_directed_script = m.get('selfDirectedScript')

        if m.get('selfDirectedScriptFullContent') is not None:
            self.self_directed_script_full_content = m.get('selfDirectedScriptFullContent')

        if m.get('skipCurrentRecognize') is not None:
            self.skip_current_recognize = m.get('skipCurrentRecognize')

        return self

