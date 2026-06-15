# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paifeaturestore20230621 import models as main_models
from darabonba.model import DaraModel

class ListLLMConfigsResponseBody(DaraModel):
    def __init__(
        self,
        llmconfigs: List[main_models.ListLLMConfigsResponseBodyLLMConfigs] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # A list of LLM configuration objects.
        # 
        # This parameter is required.
        self.llmconfigs = llmconfigs
        # The maximum number of results returned in this request.
        self.max_results = max_results
        # The token for retrieving the next page of results. If this parameter is not returned, no more results are available. To retrieve the next page, pass this value in the `NextToken` parameter of a subsequent request.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total count.
        self.total_count = total_count

    def validate(self):
        if self.llmconfigs:
            for v1 in self.llmconfigs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LLMConfigs'] = []
        if self.llmconfigs is not None:
            for k1 in self.llmconfigs:
                result['LLMConfigs'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.llmconfigs = []
        if m.get('LLMConfigs') is not None:
            for k1 in m.get('LLMConfigs'):
                temp_model = main_models.ListLLMConfigsResponseBodyLLMConfigs()
                self.llmconfigs.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListLLMConfigsResponseBodyLLMConfigs(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        base_url: str = None,
        batch_size: int = None,
        embedding_dimension: int = None,
        enable_fusion: bool = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        llmconfig_id: str = None,
        max_tokens: int = None,
        model: str = None,
        model_type: str = None,
        name: str = None,
        resource_group_id: str = None,
        rps: int = None,
        workspace_id: str = None,
    ):
        # The API key.
        self.api_key = api_key
        # The base URL for API calls.
        self.base_url = base_url
        # The batch size.
        self.batch_size = batch_size
        # The embedding dimension. If this parameter is empty or set to 0, the system uses the model\\"s default dimension.
        self.embedding_dimension = embedding_dimension
        # Specifies whether to enable the Fusion feature.
        self.enable_fusion = enable_fusion
        # The creation time.
        self.gmt_create_time = gmt_create_time
        # The modification time.
        self.gmt_modified_time = gmt_modified_time
        # The LLM configuration ID.
        self.llmconfig_id = llmconfig_id
        # The maximum number of tokens to process for a single input.
        self.max_tokens = max_tokens
        # The model name.
        self.model = model
        # The model type.
        self.model_type = model_type
        # The name of the LLM configuration.
        self.name = name
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The maximum number of requests per second (RPS).
        self.rps = rps
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['ApiKey'] = self.api_key

        if self.base_url is not None:
            result['BaseUrl'] = self.base_url

        if self.batch_size is not None:
            result['BatchSize'] = self.batch_size

        if self.embedding_dimension is not None:
            result['EmbeddingDimension'] = self.embedding_dimension

        if self.enable_fusion is not None:
            result['EnableFusion'] = self.enable_fusion

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.llmconfig_id is not None:
            result['LLMConfigId'] = self.llmconfig_id

        if self.max_tokens is not None:
            result['MaxTokens'] = self.max_tokens

        if self.model is not None:
            result['Model'] = self.model

        if self.model_type is not None:
            result['ModelType'] = self.model_type

        if self.name is not None:
            result['Name'] = self.name

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.rps is not None:
            result['Rps'] = self.rps

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')

        if m.get('BaseUrl') is not None:
            self.base_url = m.get('BaseUrl')

        if m.get('BatchSize') is not None:
            self.batch_size = m.get('BatchSize')

        if m.get('EmbeddingDimension') is not None:
            self.embedding_dimension = m.get('EmbeddingDimension')

        if m.get('EnableFusion') is not None:
            self.enable_fusion = m.get('EnableFusion')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('LLMConfigId') is not None:
            self.llmconfig_id = m.get('LLMConfigId')

        if m.get('MaxTokens') is not None:
            self.max_tokens = m.get('MaxTokens')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Rps') is not None:
            self.rps = m.get('Rps')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

