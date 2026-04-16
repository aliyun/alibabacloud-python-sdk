# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aicontent20240611 import models as main_models
from darabonba.model import DaraModel

class RequestLogDTO(DaraModel):
    def __init__(
        self,
        api_key_id: int = None,
        client_id: int = None,
        client_uuid: str = None,
        completion_tokens: int = None,
        delete_tag: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        model_code: str = None,
        model_id: int = None,
        model_name: str = None,
        model_type: str = None,
        prompt_tokens: int = None,
        request_body: str = None,
        request_id: str = None,
        request_time: str = None,
        response_body: str = None,
        response_time_ms: int = None,
        status: str = None,
        status_code: int = None,
        symbol: str = None,
        total_tokens: int = None,
        usage: main_models.UsageInfoDTO = None,
    ):
        self.api_key_id = api_key_id
        self.client_id = client_id
        self.client_uuid = client_uuid
        self.completion_tokens = completion_tokens
        self.delete_tag = delete_tag
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.model_code = model_code
        self.model_id = model_id
        self.model_name = model_name
        self.model_type = model_type
        self.prompt_tokens = prompt_tokens
        self.request_body = request_body
        self.request_id = request_id
        self.request_time = request_time
        self.response_body = response_body
        self.response_time_ms = response_time_ms
        self.status = status
        self.status_code = status_code
        self.symbol = symbol
        self.total_tokens = total_tokens
        self.usage = usage

    def validate(self):
        if self.usage:
            self.usage.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key_id is not None:
            result['apiKeyId'] = self.api_key_id

        if self.client_id is not None:
            result['clientId'] = self.client_id

        if self.client_uuid is not None:
            result['clientUuid'] = self.client_uuid

        if self.completion_tokens is not None:
            result['completionTokens'] = self.completion_tokens

        if self.delete_tag is not None:
            result['deleteTag'] = self.delete_tag

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        if self.model_code is not None:
            result['modelCode'] = self.model_code

        if self.model_id is not None:
            result['modelId'] = self.model_id

        if self.model_name is not None:
            result['modelName'] = self.model_name

        if self.model_type is not None:
            result['modelType'] = self.model_type

        if self.prompt_tokens is not None:
            result['promptTokens'] = self.prompt_tokens

        if self.request_body is not None:
            result['requestBody'] = self.request_body

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.request_time is not None:
            result['requestTime'] = self.request_time

        if self.response_body is not None:
            result['responseBody'] = self.response_body

        if self.response_time_ms is not None:
            result['responseTimeMs'] = self.response_time_ms

        if self.status is not None:
            result['status'] = self.status

        if self.status_code is not None:
            result['statusCode'] = self.status_code

        if self.symbol is not None:
            result['symbol'] = self.symbol

        if self.total_tokens is not None:
            result['totalTokens'] = self.total_tokens

        if self.usage is not None:
            result['usage'] = self.usage.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiKeyId') is not None:
            self.api_key_id = m.get('apiKeyId')

        if m.get('clientId') is not None:
            self.client_id = m.get('clientId')

        if m.get('clientUuid') is not None:
            self.client_uuid = m.get('clientUuid')

        if m.get('completionTokens') is not None:
            self.completion_tokens = m.get('completionTokens')

        if m.get('deleteTag') is not None:
            self.delete_tag = m.get('deleteTag')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('modelCode') is not None:
            self.model_code = m.get('modelCode')

        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')

        if m.get('modelName') is not None:
            self.model_name = m.get('modelName')

        if m.get('modelType') is not None:
            self.model_type = m.get('modelType')

        if m.get('promptTokens') is not None:
            self.prompt_tokens = m.get('promptTokens')

        if m.get('requestBody') is not None:
            self.request_body = m.get('requestBody')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('requestTime') is not None:
            self.request_time = m.get('requestTime')

        if m.get('responseBody') is not None:
            self.response_body = m.get('responseBody')

        if m.get('responseTimeMs') is not None:
            self.response_time_ms = m.get('responseTimeMs')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')

        if m.get('symbol') is not None:
            self.symbol = m.get('symbol')

        if m.get('totalTokens') is not None:
            self.total_tokens = m.get('totalTokens')

        if m.get('usage') is not None:
            temp_model = main_models.UsageInfoDTO()
            self.usage = temp_model.from_map(m.get('usage'))

        return self

