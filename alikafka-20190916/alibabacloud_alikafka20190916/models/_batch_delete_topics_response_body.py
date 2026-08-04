# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alikafka20190916 import models as main_models
from darabonba.model import DaraModel

class BatchDeleteTopicsResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.BatchDeleteTopicsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
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

        if m.get('Data') is not None:
            temp_model = main_models.BatchDeleteTopicsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class BatchDeleteTopicsResponseBodyData(DaraModel):
    def __init__(
        self,
        failed_count: int = None,
        results: main_models.BatchDeleteTopicsResponseBodyDataResults = None,
        success_count: int = None,
        total: int = None,
    ):
        self.failed_count = failed_count
        self.results = results
        self.success_count = success_count
        self.total = total

    def validate(self):
        if self.results:
            self.results.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed_count is not None:
            result['FailedCount'] = self.failed_count

        if self.results is not None:
            result['Results'] = self.results.to_map()

        if self.success_count is not None:
            result['SuccessCount'] = self.success_count

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailedCount') is not None:
            self.failed_count = m.get('FailedCount')

        if m.get('Results') is not None:
            temp_model = main_models.BatchDeleteTopicsResponseBodyDataResults()
            self.results = temp_model.from_map(m.get('Results'))

        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class BatchDeleteTopicsResponseBodyDataResults(DaraModel):
    def __init__(
        self,
        topic_delete_result_item_vo: List[main_models.BatchDeleteTopicsResponseBodyDataResultsTopicDeleteResultItemVO] = None,
    ):
        self.topic_delete_result_item_vo = topic_delete_result_item_vo

    def validate(self):
        if self.topic_delete_result_item_vo:
            for v1 in self.topic_delete_result_item_vo:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TopicDeleteResultItemVO'] = []
        if self.topic_delete_result_item_vo is not None:
            for k1 in self.topic_delete_result_item_vo:
                result['TopicDeleteResultItemVO'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.topic_delete_result_item_vo = []
        if m.get('TopicDeleteResultItemVO') is not None:
            for k1 in m.get('TopicDeleteResultItemVO'):
                temp_model = main_models.BatchDeleteTopicsResponseBodyDataResultsTopicDeleteResultItemVO()
                self.topic_delete_result_item_vo.append(temp_model.from_map(k1))

        return self



class BatchDeleteTopicsResponseBodyDataResultsTopicDeleteResultItemVO(DaraModel):
    def __init__(
        self,
        code: int = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        message: str = None,
        status: str = None,
        success: bool = None,
        topic: str = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.message = message
        self.status = status
        self.success = success
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code

        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message

        if self.message is not None:
            result['Message'] = self.message

        if self.status is not None:
            result['Status'] = self.status

        if self.success is not None:
            result['Success'] = self.success

        if self.topic is not None:
            result['Topic'] = self.topic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        return self

