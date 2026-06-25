# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiworkspace20210204 import models as main_models
from darabonba.model import DaraModel

class ListModelsRequest(DaraModel):
    def __init__(
        self,
        collections: str = None,
        conditions: List[main_models.ListModelsRequestConditions] = None,
        domain: str = None,
        label: str = None,
        model_name: str = None,
        model_type: str = None,
        order: str = None,
        origin: str = None,
        page_number: int = None,
        page_size: int = None,
        provider: str = None,
        query: str = None,
        sort_by: str = None,
        tag: List[main_models.ListModelsRequestTag] = None,
        task: str = None,
        workspace_id: str = None,
    ):
        # The collections to which the model belongs. You can specify multiple collections. Separate them with commas (,).
        self.collections = collections
        # The conditions.
        self.conditions = conditions
        # The domain. This parameter is used to filter the model list by domain. Examples: nlp (natural language processing) and cv (computer vision).
        self.domain = domain
        # The label string. This parameter is used to filter the list. Models are returned if their label keys or values contain the specified string.
        self.label = label
        # The model name. This parameter is used to filter the model list.
        self.model_name = model_name
        # The model type.
        self.model_type = model_type
        # The order in which to sort the results of a paged query. The default value is ASC.
        # 
        # - ASC: ascending order.
        # 
        # - DESC: descending order.
        self.order = order
        # The model source. This parameter is used to filter the model list by community or organization. Examples: ModelScope and HuggingFace.
        self.origin = origin
        # The page number of the model list. The value starts from 1. The default value is 1.
        self.page_number = page_number
        # The number of models to display on each page in a paged query. The default value is 10.
        self.page_size = page_size
        # The provider. If you specify a provider, only the public models from that provider are returned. If you leave this parameter empty, your own models are returned.
        self.provider = provider
        # The query condition. This parameter performs a fuzzy match on ModelName, Domain, Task, LabelKey, and LabelValue. For example, if you enter nlp, models that match in any of these fields are returned.
        self.query = query
        # The field to use for sorting in a paged query. Currently, only the GmtCreateTime field is supported.
        self.sort_by = sort_by
        # The list of tags.
        self.tag = tag
        # The task. This parameter is used to filter the model list by task type. Example: text-classification.
        self.task = task
        # The workspace ID. The returned list contains only the models in the specified workspace. For more information about how to obtain a workspace ID, see [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html).
        self.workspace_id = workspace_id

    def validate(self):
        if self.conditions:
            for v1 in self.conditions:
                 if v1:
                    v1.validate()
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.collections is not None:
            result['Collections'] = self.collections

        result['Conditions'] = []
        if self.conditions is not None:
            for k1 in self.conditions:
                result['Conditions'].append(k1.to_map() if k1 else None)

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.label is not None:
            result['Label'] = self.label

        if self.model_name is not None:
            result['ModelName'] = self.model_name

        if self.model_type is not None:
            result['ModelType'] = self.model_type

        if self.order is not None:
            result['Order'] = self.order

        if self.origin is not None:
            result['Origin'] = self.origin

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.provider is not None:
            result['Provider'] = self.provider

        if self.query is not None:
            result['Query'] = self.query

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.task is not None:
            result['Task'] = self.task

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Collections') is not None:
            self.collections = m.get('Collections')

        self.conditions = []
        if m.get('Conditions') is not None:
            for k1 in m.get('Conditions'):
                temp_model = main_models.ListModelsRequestConditions()
                self.conditions.append(temp_model.from_map(k1))

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('Origin') is not None:
            self.origin = m.get('Origin')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Provider') is not None:
            self.provider = m.get('Provider')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.ListModelsRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('Task') is not None:
            self.task = m.get('Task')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class ListModelsRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value of the tag.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListModelsRequestConditions(DaraModel):
    def __init__(
        self,
        column: str = None,
        operator: str = None,
        value: str = None,
    ):
        # The parameter name. Example: ParameterSize.
        self.column = column
        # The operator. Example: LessThan.
        self.operator = operator
        # The value. Example: 3000.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column is not None:
            result['Column'] = self.column

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Column') is not None:
            self.column = m.get('Column')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

