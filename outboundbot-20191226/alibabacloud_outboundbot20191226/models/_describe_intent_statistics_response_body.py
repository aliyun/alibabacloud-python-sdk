# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_outboundbot20191226 import models as main_models
from darabonba.model import DaraModel

class DescribeIntentStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        global_intent_num: int = None,
        global_intents: List[main_models.DescribeIntentStatisticsResponseBodyGlobalIntents] = None,
        group_id: str = None,
        http_status_code: int = None,
        instance_id: str = None,
        intents_after_no_answer: List[main_models.DescribeIntentStatisticsResponseBodyIntentsAfterNoAnswer] = None,
        message: str = None,
        process_intent_num: int = None,
        process_intents: List[main_models.DescribeIntentStatisticsResponseBodyProcessIntents] = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.global_intent_num = global_intent_num
        self.global_intents = global_intents
        self.group_id = group_id
        self.http_status_code = http_status_code
        self.instance_id = instance_id
        self.intents_after_no_answer = intents_after_no_answer
        self.message = message
        self.process_intent_num = process_intent_num
        self.process_intents = process_intents
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.global_intents:
            for v1 in self.global_intents:
                 if v1:
                    v1.validate()
        if self.intents_after_no_answer:
            for v1 in self.intents_after_no_answer:
                 if v1:
                    v1.validate()
        if self.process_intents:
            for v1 in self.process_intents:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.global_intent_num is not None:
            result['GlobalIntentNum'] = self.global_intent_num

        result['GlobalIntents'] = []
        if self.global_intents is not None:
            for k1 in self.global_intents:
                result['GlobalIntents'].append(k1.to_map() if k1 else None)

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        result['IntentsAfterNoAnswer'] = []
        if self.intents_after_no_answer is not None:
            for k1 in self.intents_after_no_answer:
                result['IntentsAfterNoAnswer'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.process_intent_num is not None:
            result['ProcessIntentNum'] = self.process_intent_num

        result['ProcessIntents'] = []
        if self.process_intents is not None:
            for k1 in self.process_intents:
                result['ProcessIntents'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('GlobalIntentNum') is not None:
            self.global_intent_num = m.get('GlobalIntentNum')

        self.global_intents = []
        if m.get('GlobalIntents') is not None:
            for k1 in m.get('GlobalIntents'):
                temp_model = main_models.DescribeIntentStatisticsResponseBodyGlobalIntents()
                self.global_intents.append(temp_model.from_map(k1))

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        self.intents_after_no_answer = []
        if m.get('IntentsAfterNoAnswer') is not None:
            for k1 in m.get('IntentsAfterNoAnswer'):
                temp_model = main_models.DescribeIntentStatisticsResponseBodyIntentsAfterNoAnswer()
                self.intents_after_no_answer.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('ProcessIntentNum') is not None:
            self.process_intent_num = m.get('ProcessIntentNum')

        self.process_intents = []
        if m.get('ProcessIntents') is not None:
            for k1 in m.get('ProcessIntents'):
                temp_model = main_models.DescribeIntentStatisticsResponseBodyProcessIntents()
                self.process_intents.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeIntentStatisticsResponseBodyProcessIntents(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        hit_after_no_answer: int = None,
        hit_num: int = None,
        instance_id: str = None,
        intent_id: str = None,
        intent_name: str = None,
        rate_display: str = None,
        type: str = None,
    ):
        self.group_id = group_id
        self.hit_after_no_answer = hit_after_no_answer
        self.hit_num = hit_num
        self.instance_id = instance_id
        self.intent_id = intent_id
        self.intent_name = intent_name
        self.rate_display = rate_display
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.hit_after_no_answer is not None:
            result['HitAfterNoAnswer'] = self.hit_after_no_answer

        if self.hit_num is not None:
            result['HitNum'] = self.hit_num

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.intent_id is not None:
            result['IntentId'] = self.intent_id

        if self.intent_name is not None:
            result['IntentName'] = self.intent_name

        if self.rate_display is not None:
            result['RateDisplay'] = self.rate_display

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('HitAfterNoAnswer') is not None:
            self.hit_after_no_answer = m.get('HitAfterNoAnswer')

        if m.get('HitNum') is not None:
            self.hit_num = m.get('HitNum')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')

        if m.get('IntentName') is not None:
            self.intent_name = m.get('IntentName')

        if m.get('RateDisplay') is not None:
            self.rate_display = m.get('RateDisplay')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeIntentStatisticsResponseBodyIntentsAfterNoAnswer(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        hit_after_no_answer: int = None,
        instance_id: str = None,
        intent_id: str = None,
        intent_name: str = None,
    ):
        self.group_id = group_id
        self.hit_after_no_answer = hit_after_no_answer
        self.instance_id = instance_id
        self.intent_id = intent_id
        self.intent_name = intent_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.hit_after_no_answer is not None:
            result['HitAfterNoAnswer'] = self.hit_after_no_answer

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.intent_id is not None:
            result['IntentId'] = self.intent_id

        if self.intent_name is not None:
            result['IntentName'] = self.intent_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('HitAfterNoAnswer') is not None:
            self.hit_after_no_answer = m.get('HitAfterNoAnswer')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')

        if m.get('IntentName') is not None:
            self.intent_name = m.get('IntentName')

        return self

class DescribeIntentStatisticsResponseBodyGlobalIntents(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        hit_after_no_answer: int = None,
        hit_num: int = None,
        instance_id: str = None,
        intent_id: str = None,
        intent_name: str = None,
        type: str = None,
    ):
        self.group_id = group_id
        self.hit_after_no_answer = hit_after_no_answer
        self.hit_num = hit_num
        self.instance_id = instance_id
        self.intent_id = intent_id
        self.intent_name = intent_name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.hit_after_no_answer is not None:
            result['HitAfterNoAnswer'] = self.hit_after_no_answer

        if self.hit_num is not None:
            result['HitNum'] = self.hit_num

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.intent_id is not None:
            result['IntentId'] = self.intent_id

        if self.intent_name is not None:
            result['IntentName'] = self.intent_name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('HitAfterNoAnswer') is not None:
            self.hit_after_no_answer = m.get('HitAfterNoAnswer')

        if m.get('HitNum') is not None:
            self.hit_num = m.get('HitNum')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')

        if m.get('IntentName') is not None:
            self.intent_name = m.get('IntentName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

