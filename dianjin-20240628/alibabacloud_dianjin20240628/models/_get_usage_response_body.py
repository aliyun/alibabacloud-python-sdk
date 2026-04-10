# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dianjin20240628 import models as main_models
from darabonba.model import DaraModel

class GetUsageResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetUsageResponseBodyData = None,
        message: str = None,
        retry_able: bool = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.retry_able = retry_able
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
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.retry_able is not None:
            result['retryAble'] = self.retry_able

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetUsageResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('retryAble') is not None:
            self.retry_able = m.get('retryAble')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class GetUsageResponseBodyData(DaraModel):
    def __init__(
        self,
        entitlements: List[main_models.GetUsageResponseBodyDataEntitlements] = None,
        model_stats: List[main_models.GetUsageResponseBodyDataModelStats] = None,
        summary: main_models.GetUsageResponseBodyDataSummary = None,
    ):
        self.entitlements = entitlements
        self.model_stats = model_stats
        self.summary = summary

    def validate(self):
        if self.entitlements:
            for v1 in self.entitlements:
                 if v1:
                    v1.validate()
        if self.model_stats:
            for v1 in self.model_stats:
                 if v1:
                    v1.validate()
        if self.summary:
            self.summary.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['entitlements'] = []
        if self.entitlements is not None:
            for k1 in self.entitlements:
                result['entitlements'].append(k1.to_map() if k1 else None)

        result['modelStats'] = []
        if self.model_stats is not None:
            for k1 in self.model_stats:
                result['modelStats'].append(k1.to_map() if k1 else None)

        if self.summary is not None:
            result['summary'] = self.summary.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.entitlements = []
        if m.get('entitlements') is not None:
            for k1 in m.get('entitlements'):
                temp_model = main_models.GetUsageResponseBodyDataEntitlements()
                self.entitlements.append(temp_model.from_map(k1))

        self.model_stats = []
        if m.get('modelStats') is not None:
            for k1 in m.get('modelStats'):
                temp_model = main_models.GetUsageResponseBodyDataModelStats()
                self.model_stats.append(temp_model.from_map(k1))

        if m.get('summary') is not None:
            temp_model = main_models.GetUsageResponseBodyDataSummary()
            self.summary = temp_model.from_map(m.get('summary'))

        return self

class GetUsageResponseBodyDataSummary(DaraModel):
    def __init__(
        self,
        total_input_usage: int = None,
        total_output_usage: int = None,
        total_requests: int = None,
        total_usage: int = None,
    ):
        self.total_input_usage = total_input_usage
        self.total_output_usage = total_output_usage
        self.total_requests = total_requests
        self.total_usage = total_usage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.total_input_usage is not None:
            result['totalInputUsage'] = self.total_input_usage

        if self.total_output_usage is not None:
            result['totalOutputUsage'] = self.total_output_usage

        if self.total_requests is not None:
            result['totalRequests'] = self.total_requests

        if self.total_usage is not None:
            result['totalUsage'] = self.total_usage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('totalInputUsage') is not None:
            self.total_input_usage = m.get('totalInputUsage')

        if m.get('totalOutputUsage') is not None:
            self.total_output_usage = m.get('totalOutputUsage')

        if m.get('totalRequests') is not None:
            self.total_requests = m.get('totalRequests')

        if m.get('totalUsage') is not None:
            self.total_usage = m.get('totalUsage')

        return self

class GetUsageResponseBodyDataModelStats(DaraModel):
    def __init__(
        self,
        input_usage: int = None,
        model: str = None,
        output_usage: int = None,
        requests: int = None,
        total_usage: int = None,
    ):
        self.input_usage = input_usage
        self.model = model
        self.output_usage = output_usage
        self.requests = requests
        self.total_usage = total_usage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_usage is not None:
            result['inputUsage'] = self.input_usage

        if self.model is not None:
            result['model'] = self.model

        if self.output_usage is not None:
            result['outputUsage'] = self.output_usage

        if self.requests is not None:
            result['requests'] = self.requests

        if self.total_usage is not None:
            result['totalUsage'] = self.total_usage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('inputUsage') is not None:
            self.input_usage = m.get('inputUsage')

        if m.get('model') is not None:
            self.model = m.get('model')

        if m.get('outputUsage') is not None:
            self.output_usage = m.get('outputUsage')

        if m.get('requests') is not None:
            self.requests = m.get('requests')

        if m.get('totalUsage') is not None:
            self.total_usage = m.get('totalUsage')

        return self

class GetUsageResponseBodyDataEntitlements(DaraModel):
    def __init__(
        self,
        allowed_models: List[str] = None,
        binding_id: int = None,
        effective_at: str = None,
        expire_at: str = None,
        quota_initial: int = None,
        quota_remaining: int = None,
        quota_used: int = None,
        status: str = None,
        template_id: int = None,
        template_name: str = None,
    ):
        self.allowed_models = allowed_models
        self.binding_id = binding_id
        self.effective_at = effective_at
        self.expire_at = expire_at
        self.quota_initial = quota_initial
        self.quota_remaining = quota_remaining
        self.quota_used = quota_used
        self.status = status
        self.template_id = template_id
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allowed_models is not None:
            result['allowedModels'] = self.allowed_models

        if self.binding_id is not None:
            result['bindingId'] = self.binding_id

        if self.effective_at is not None:
            result['effectiveAt'] = self.effective_at

        if self.expire_at is not None:
            result['expireAt'] = self.expire_at

        if self.quota_initial is not None:
            result['quotaInitial'] = self.quota_initial

        if self.quota_remaining is not None:
            result['quotaRemaining'] = self.quota_remaining

        if self.quota_used is not None:
            result['quotaUsed'] = self.quota_used

        if self.status is not None:
            result['status'] = self.status

        if self.template_id is not None:
            result['templateId'] = self.template_id

        if self.template_name is not None:
            result['templateName'] = self.template_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allowedModels') is not None:
            self.allowed_models = m.get('allowedModels')

        if m.get('bindingId') is not None:
            self.binding_id = m.get('bindingId')

        if m.get('effectiveAt') is not None:
            self.effective_at = m.get('effectiveAt')

        if m.get('expireAt') is not None:
            self.expire_at = m.get('expireAt')

        if m.get('quotaInitial') is not None:
            self.quota_initial = m.get('quotaInitial')

        if m.get('quotaRemaining') is not None:
            self.quota_remaining = m.get('quotaRemaining')

        if m.get('quotaUsed') is not None:
            self.quota_used = m.get('quotaUsed')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')

        if m.get('templateName') is not None:
            self.template_name = m.get('templateName')

        return self

