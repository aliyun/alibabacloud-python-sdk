# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class GetDigitalWatermarkExtractResultResponseBody(DaraModel):
    def __init__(
        self,
        ai_extract_result_list: List[main_models.GetDigitalWatermarkExtractResultResponseBodyAiExtractResultList] = None,
        request_id: str = None,
    ):
        # The details of the watermark extraction job.
        self.ai_extract_result_list = ai_extract_result_list
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.ai_extract_result_list:
            for v1 in self.ai_extract_result_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AiExtractResultList'] = []
        if self.ai_extract_result_list is not None:
            for k1 in self.ai_extract_result_list:
                result['AiExtractResultList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ai_extract_result_list = []
        if m.get('AiExtractResultList') is not None:
            for k1 in m.get('AiExtractResultList'):
                temp_model = main_models.GetDigitalWatermarkExtractResultResponseBodyAiExtractResultList()
                self.ai_extract_result_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetDigitalWatermarkExtractResultResponseBodyAiExtractResultList(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        error_message: str = None,
        job_id: str = None,
        modify_time: str = None,
        status: str = None,
        water_mark_text: str = None,
    ):
        # The time when the watermark extraction job was created.
        self.create_time = create_time
        # The error message.
        self.error_message = error_message
        # The ID of the watermark extraction job.
        self.job_id = job_id
        # The time when the watermark extraction job was last updated.
        self.modify_time = modify_time
        # The status of the watermark extraction job. Valid values:
        # 
        # *   **Success**
        # *   **Failed**
        # *   **Processing**
        self.status = status
        # The extracted watermark content.
        self.water_mark_text = water_mark_text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.status is not None:
            result['Status'] = self.status

        if self.water_mark_text is not None:
            result['WaterMarkText'] = self.water_mark_text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('WaterMarkText') is not None:
            self.water_mark_text = m.get('WaterMarkText')

        return self

