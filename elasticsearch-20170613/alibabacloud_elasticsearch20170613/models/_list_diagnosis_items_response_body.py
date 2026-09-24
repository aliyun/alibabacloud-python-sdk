# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class ListDiagnosisItemsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.ListDiagnosisItemsResponseBodyResult] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The returned results.
        self.result = result

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListDiagnosisItemsResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        return self

class ListDiagnosisItemsResponseBodyResult(DaraModel):
    def __init__(
        self,
        billable: bool = None,
        category: str = None,
        description: str = None,
        es_api_required: bool = None,
        key: str = None,
        level: str = None,
        name: str = None,
        sort_order: int = None,
        supported_modes: List[str] = None,
    ):
        # Indicates whether billable tokens are consumed. The value is true when level is ADVANCED.
        self.billable = billable
        # The category code. You can use this value to group diagnostic items by category.
        self.category = category
        # The diagnostic item description.
        self.description = description
        # Indicates whether the cluster API is accessed.
        self.es_api_required = es_api_required
        # The diagnostic item identifier.
        self.key = key
        # The diagnostic item level. Valid values:
        # 
        # - BASIC: basic inspection item (free).
        # - ADVANCED: advanced inspection item (consumes billable tokens).
        self.level = level
        # The diagnostic item name.
        self.name = name
        # The sort order number for display.
        self.sort_order = sort_order
        # The supported execution modes. Basic items support RULE and AGENT. Advanced items support only AGENT.
        self.supported_modes = supported_modes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.billable is not None:
            result['billable'] = self.billable

        if self.category is not None:
            result['category'] = self.category

        if self.description is not None:
            result['description'] = self.description

        if self.es_api_required is not None:
            result['esApiRequired'] = self.es_api_required

        if self.key is not None:
            result['key'] = self.key

        if self.level is not None:
            result['level'] = self.level

        if self.name is not None:
            result['name'] = self.name

        if self.sort_order is not None:
            result['sortOrder'] = self.sort_order

        if self.supported_modes is not None:
            result['supportedModes'] = self.supported_modes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billable') is not None:
            self.billable = m.get('billable')

        if m.get('category') is not None:
            self.category = m.get('category')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('esApiRequired') is not None:
            self.es_api_required = m.get('esApiRequired')

        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('level') is not None:
            self.level = m.get('level')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('sortOrder') is not None:
            self.sort_order = m.get('sortOrder')

        if m.get('supportedModes') is not None:
            self.supported_modes = m.get('supportedModes')

        return self

