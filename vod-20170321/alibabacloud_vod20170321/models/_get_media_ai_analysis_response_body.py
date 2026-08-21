# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class GetMediaAiAnalysisResponseBody(DaraModel):
    def __init__(
        self,
        ai_analysis_result_list: main_models.GetMediaAiAnalysisResponseBodyAiAnalysisResultList = None,
        request_id: str = None,
    ):
        self.ai_analysis_result_list = ai_analysis_result_list
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.ai_analysis_result_list:
            self.ai_analysis_result_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ai_analysis_result_list is not None:
            result['AiAnalysisResultList'] = self.ai_analysis_result_list.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AiAnalysisResultList') is not None:
            temp_model = main_models.GetMediaAiAnalysisResponseBodyAiAnalysisResultList()
            self.ai_analysis_result_list = temp_model.from_map(m.get('AiAnalysisResultList'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetMediaAiAnalysisResponseBodyAiAnalysisResultList(DaraModel):
    def __init__(
        self,
        ai_analysis_result: List[main_models.GetMediaAiAnalysisResponseBodyAiAnalysisResultListAiAnalysisResult] = None,
    ):
        self.ai_analysis_result = ai_analysis_result

    def validate(self):
        if self.ai_analysis_result:
            for v1 in self.ai_analysis_result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AiAnalysisResult'] = []
        if self.ai_analysis_result is not None:
            for k1 in self.ai_analysis_result:
                result['AiAnalysisResult'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ai_analysis_result = []
        if m.get('AiAnalysisResult') is not None:
            for k1 in m.get('AiAnalysisResult'):
                temp_model = main_models.GetMediaAiAnalysisResponseBodyAiAnalysisResultListAiAnalysisResult()
                self.ai_analysis_result.append(temp_model.from_map(k1))

        return self

class GetMediaAiAnalysisResponseBodyAiAnalysisResultListAiAnalysisResult(DaraModel):
    def __init__(
        self,
        content: str = None,
        extra: str = None,
        result_type: str = None,
        summary: str = None,
        title: str = None,
    ):
        self.content = content
        self.extra = extra
        self.result_type = result_type
        self.summary = summary
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.extra is not None:
            result['Extra'] = self.extra

        if self.result_type is not None:
            result['ResultType'] = self.result_type

        if self.summary is not None:
            result['Summary'] = self.summary

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Extra') is not None:
            self.extra = m.get('Extra')

        if m.get('ResultType') is not None:
            self.result_type = m.get('ResultType')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

