# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_green20220302 import models as main_models
from darabonba.model import DaraModel

class TextModerationResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.TextModerationResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code.
        self.code = code
        # The moderation result data.
        self.data = data
        # The response message for the request.
        self.message = message
        # The request ID.
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
            temp_model = main_models.TextModerationResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class TextModerationResponseBodyData(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        data_id: str = None,
        descriptions: str = None,
        device_id: str = None,
        ext: main_models.TextModerationResponseBodyDataExt = None,
        labels: str = None,
        manual_task_id: str = None,
        reason: str = None,
    ):
        # The \\`accountId\\` specified in the request.
        self.account_id = account_id
        # The data ID of the moderated object.
        # 
        # > If you specify the dataId parameter in the request, its value is returned in this parameter.
        self.data_id = data_id
        # The description of the label.
        self.descriptions = descriptions
        # The \\`deviceId\\` specified in the request.
        self.device_id = device_id
        # Auxiliary reference information for the text.
        self.ext = ext
        # The moderation labels. If multiple labels are returned, they are separated by commas (,). Valid values: ad: advertisement profanity: profanity contraband: contraband sexual_content: sexual content violence: violent and terrorist content nonsense: meaningless content spam: spam negative_content: undesirable content cyberbullying: cyberbullying C_customized: A match in a custom library
        self.labels = labels
        # The ID of the manual review task.
        self.manual_task_id = manual_task_id
        # A JSON string that contains the reason for the moderation result. The string includes the following fields:
        # 
        # 1. riskTips: The sub-labels.
        # 
        # 2. riskWords: The detected risk words.
        # 
        # 3. adNums: The detected ad-related numbers.
        # 
        # 4. customizedWords: The detected custom words.
        # 
        # 5. customizedLibs: The names of the custom libraries that contain a match.
        # 
        # 6. riskLevel: The risk level, which is recommended by the system. Valid values:
        # 
        # - high: high risk
        # 
        # - medium: medium risk
        # 
        # - low: low risk
        self.reason = reason

    def validate(self):
        if self.ext:
            self.ext.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['accountId'] = self.account_id

        if self.data_id is not None:
            result['dataId'] = self.data_id

        if self.descriptions is not None:
            result['descriptions'] = self.descriptions

        if self.device_id is not None:
            result['deviceId'] = self.device_id

        if self.ext is not None:
            result['ext'] = self.ext.to_map()

        if self.labels is not None:
            result['labels'] = self.labels

        if self.manual_task_id is not None:
            result['manualTaskId'] = self.manual_task_id

        if self.reason is not None:
            result['reason'] = self.reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')

        if m.get('dataId') is not None:
            self.data_id = m.get('dataId')

        if m.get('descriptions') is not None:
            self.descriptions = m.get('descriptions')

        if m.get('deviceId') is not None:
            self.device_id = m.get('deviceId')

        if m.get('ext') is not None:
            temp_model = main_models.TextModerationResponseBodyDataExt()
            self.ext = temp_model.from_map(m.get('ext'))

        if m.get('labels') is not None:
            self.labels = m.get('labels')

        if m.get('manualTaskId') is not None:
            self.manual_task_id = m.get('manualTaskId')

        if m.get('reason') is not None:
            self.reason = m.get('reason')

        return self

class TextModerationResponseBodyDataExt(DaraModel):
    def __init__(
        self,
        llm_content: main_models.TextModerationResponseBodyDataExtLlmContent = None,
    ):
        # The output from the Large Language Model (LLM).
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
            result['llmContent'] = self.llm_content.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('llmContent') is not None:
            temp_model = main_models.TextModerationResponseBodyDataExtLlmContent()
            self.llm_content = temp_model.from_map(m.get('llmContent'))

        return self

class TextModerationResponseBodyDataExtLlmContent(DaraModel):
    def __init__(
        self,
        output_text: str = None,
    ):
        # The output content.
        self.output_text = output_text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.output_text is not None:
            result['outputText'] = self.output_text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('outputText') is not None:
            self.output_text = m.get('outputText')

        return self

