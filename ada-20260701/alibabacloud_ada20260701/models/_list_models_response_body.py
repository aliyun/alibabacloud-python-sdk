# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ada20260701 import models as main_models
from darabonba.model import DaraModel

class ListModelsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        models: List[main_models.ListModelsResponseBodyModels] = None,
        next_token: str = None,
        request_id: str = None,
        total: int = None,
    ):
        # The maximum number of results used for the current pagination. If pagination is not used, this value is the total number of results. This value is not the actual number of entries returned on the current page.
        self.max_results = max_results
        # The array of model structures. For nested fields, refer to the supplementary description of response parameters.
        self.models = models
        # The token for the next page. An empty value indicates that no more pages exist.
        self.next_token = next_token
        # The ID of the request. You can use the ID to troubleshoot issues.
        self.request_id = request_id
        # The total number of models that meet the filter conditions.
        self.total = total

    def validate(self):
        if self.models:
            for v1 in self.models:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        result['Models'] = []
        if self.models is not None:
            for k1 in self.models:
                result['Models'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        self.models = []
        if m.get('Models') is not None:
            for k1 in m.get('Models'):
                temp_model = main_models.ListModelsResponseBodyModels()
                self.models.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListModelsResponseBodyModels(DaraModel):
    def __init__(
        self,
        capabilities: main_models.ListModelsResponseBodyModelsCapabilities = None,
        context_window: int = None,
        created: int = None,
        credits_coefficient: str = None,
        display_name: str = None,
        id: str = None,
        max_context_window: int = None,
        object: str = None,
        owned_by: str = None,
        supports_thinking: int = None,
        thinking_level: str = None,
        thinking_levels: List[str] = None,
        thinking_mode: int = None,
    ):
        # The model capabilities structure.
        self.capabilities = capabilities
        # The deprecated compatibility field. This field is not returned. Do not rely on this field for integration.
        self.context_window = context_window
        # The time when the model was created. The value is a UNIX timestamp in seconds.
        self.created = created
        # The credits coefficient of the model. The value is returned as a decimal string. This parameter is not returned if it is not configured.
        self.credits_coefficient = credits_coefficient
        # The display name of the model. Do not pass this value as the model identifier.
        self.display_name = display_name
        # The model identifier. Used as Params.modelId for SetAgentSessionModel. Use the actual returned value.
        self.id = id
        # The deprecated compatibility field. This field is not returned. Do not rely on this field for integration.
        self.max_context_window = max_context_window
        # The object type. The value is fixed to model.
        self.object = object
        # The identifier of the model provider.
        self.owned_by = owned_by
        # The deprecated compatibility field. This field is not returned. Use ThinkingLevels instead.
        self.supports_thinking = supports_thinking
        # The default thinking level in the model catalog. This value does not represent the current value of the session. Query the current value by using GetAgentSessionModel.
        self.thinking_level = thinking_level
        # The thinking levels supported by the model. An empty array does not indicate that all levels are supported. The target session still requires validation.
        self.thinking_levels = thinking_levels
        # The deprecated compatibility field. This field is not returned. Use ThinkingLevel instead.
        self.thinking_mode = thinking_mode

    def validate(self):
        if self.capabilities:
            self.capabilities.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.capabilities is not None:
            result['Capabilities'] = self.capabilities.to_map()

        if self.context_window is not None:
            result['ContextWindow'] = self.context_window

        if self.created is not None:
            result['Created'] = self.created

        if self.credits_coefficient is not None:
            result['CreditsCoefficient'] = self.credits_coefficient

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.id is not None:
            result['Id'] = self.id

        if self.max_context_window is not None:
            result['MaxContextWindow'] = self.max_context_window

        if self.object is not None:
            result['Object'] = self.object

        if self.owned_by is not None:
            result['OwnedBy'] = self.owned_by

        if self.supports_thinking is not None:
            result['SupportsThinking'] = self.supports_thinking

        if self.thinking_level is not None:
            result['ThinkingLevel'] = self.thinking_level

        if self.thinking_levels is not None:
            result['ThinkingLevels'] = self.thinking_levels

        if self.thinking_mode is not None:
            result['ThinkingMode'] = self.thinking_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capabilities') is not None:
            temp_model = main_models.ListModelsResponseBodyModelsCapabilities()
            self.capabilities = temp_model.from_map(m.get('Capabilities'))

        if m.get('ContextWindow') is not None:
            self.context_window = m.get('ContextWindow')

        if m.get('Created') is not None:
            self.created = m.get('Created')

        if m.get('CreditsCoefficient') is not None:
            self.credits_coefficient = m.get('CreditsCoefficient')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MaxContextWindow') is not None:
            self.max_context_window = m.get('MaxContextWindow')

        if m.get('Object') is not None:
            self.object = m.get('Object')

        if m.get('OwnedBy') is not None:
            self.owned_by = m.get('OwnedBy')

        if m.get('SupportsThinking') is not None:
            self.supports_thinking = m.get('SupportsThinking')

        if m.get('ThinkingLevel') is not None:
            self.thinking_level = m.get('ThinkingLevel')

        if m.get('ThinkingLevels') is not None:
            self.thinking_levels = m.get('ThinkingLevels')

        if m.get('ThinkingMode') is not None:
            self.thinking_mode = m.get('ThinkingMode')

        return self

class ListModelsResponseBodyModelsCapabilities(DaraModel):
    def __init__(
        self,
        input_modalities: List[str] = None,
    ):
        # The supported input modalities. For text sessions, select a model that includes text.
        self.input_modalities = input_modalities

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_modalities is not None:
            result['InputModalities'] = self.input_modalities

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputModalities') is not None:
            self.input_modalities = m.get('InputModalities')

        return self

