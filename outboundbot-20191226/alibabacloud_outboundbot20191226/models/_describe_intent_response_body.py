# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_outboundbot20191226 import models as main_models
from darabonba.model import DaraModel

class DescribeIntentResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        intent: main_models.DescribeIntentResponseBodyIntent = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.intent = intent
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.intent:
            self.intent.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.intent is not None:
            result['Intent'] = self.intent.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Intent') is not None:
            temp_model = main_models.DescribeIntentResponseBodyIntent()
            self.intent = temp_model.from_map(m.get('Intent'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeIntentResponseBodyIntent(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        intent_description: str = None,
        intent_id: str = None,
        intent_name: str = None,
        keywords: str = None,
        script_id: str = None,
        update_time: int = None,
        utterances: str = None,
    ):
        self.create_time = create_time
        self.intent_description = intent_description
        self.intent_id = intent_id
        self.intent_name = intent_name
        self.keywords = keywords
        self.script_id = script_id
        self.update_time = update_time
        self.utterances = utterances

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.intent_description is not None:
            result['IntentDescription'] = self.intent_description

        if self.intent_id is not None:
            result['IntentId'] = self.intent_id

        if self.intent_name is not None:
            result['IntentName'] = self.intent_name

        if self.keywords is not None:
            result['Keywords'] = self.keywords

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.utterances is not None:
            result['Utterances'] = self.utterances

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('IntentDescription') is not None:
            self.intent_description = m.get('IntentDescription')

        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')

        if m.get('IntentName') is not None:
            self.intent_name = m.get('IntentName')

        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('Utterances') is not None:
            self.utterances = m.get('Utterances')

        return self

