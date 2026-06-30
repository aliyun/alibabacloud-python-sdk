# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_realtranslationagent20260622 import models as main_models
from darabonba.model import DaraModel

class UploadTranslationFileResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.UploadTranslationFileResponseBodyData = None,
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
            temp_model = main_models.UploadTranslationFileResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class UploadTranslationFileResponseBodyData(DaraModel):
    def __init__(
        self,
        credit_breakdown: str = None,
        credits_available: bool = None,
        detected_lang: str = None,
        estimated_cost_credits: float = None,
        estimated_time: int = None,
        fonts: Dict[str, List[str]] = None,
        page_count: int = None,
        sensitive_detected: bool = None,
        sensitive_tags: List[str] = None,
        task_id: str = None,
        word_count: int = None,
    ):
        self.credit_breakdown = credit_breakdown
        self.credits_available = credits_available
        self.detected_lang = detected_lang
        self.estimated_cost_credits = estimated_cost_credits
        self.estimated_time = estimated_time
        self.fonts = fonts
        self.page_count = page_count
        self.sensitive_detected = sensitive_detected
        self.sensitive_tags = sensitive_tags
        self.task_id = task_id
        self.word_count = word_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credit_breakdown is not None:
            result['CreditBreakdown'] = self.credit_breakdown

        if self.credits_available is not None:
            result['CreditsAvailable'] = self.credits_available

        if self.detected_lang is not None:
            result['DetectedLang'] = self.detected_lang

        if self.estimated_cost_credits is not None:
            result['EstimatedCostCredits'] = self.estimated_cost_credits

        if self.estimated_time is not None:
            result['EstimatedTime'] = self.estimated_time

        if self.fonts is not None:
            result['Fonts'] = self.fonts

        if self.page_count is not None:
            result['PageCount'] = self.page_count

        if self.sensitive_detected is not None:
            result['SensitiveDetected'] = self.sensitive_detected

        if self.sensitive_tags is not None:
            result['SensitiveTags'] = self.sensitive_tags

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.word_count is not None:
            result['WordCount'] = self.word_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreditBreakdown') is not None:
            self.credit_breakdown = m.get('CreditBreakdown')

        if m.get('CreditsAvailable') is not None:
            self.credits_available = m.get('CreditsAvailable')

        if m.get('DetectedLang') is not None:
            self.detected_lang = m.get('DetectedLang')

        if m.get('EstimatedCostCredits') is not None:
            self.estimated_cost_credits = m.get('EstimatedCostCredits')

        if m.get('EstimatedTime') is not None:
            self.estimated_time = m.get('EstimatedTime')

        if m.get('Fonts') is not None:
            self.fonts = m.get('Fonts')

        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')

        if m.get('SensitiveDetected') is not None:
            self.sensitive_detected = m.get('SensitiveDetected')

        if m.get('SensitiveTags') is not None:
            self.sensitive_tags = m.get('SensitiveTags')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('WordCount') is not None:
            self.word_count = m.get('WordCount')

        return self

