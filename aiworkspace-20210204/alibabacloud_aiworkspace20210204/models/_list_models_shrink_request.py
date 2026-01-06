# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListModelsShrinkRequest(DaraModel):
    def __init__(
        self,
        collections: str = None,
        conditions_shrink: str = None,
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
        tag_shrink: str = None,
        task: str = None,
        workspace_id: str = None,
    ):
        # The collection where the model is located. You can specify multiple collections and separate them with commas (,).
        self.collections = collections
        self.conditions_shrink = conditions_shrink
        # The domain. Only models in the domain are returned. Valid values: nlp (Natural Language Processing) and cv (Computer Vision).
        self.domain = domain
        # The label. Models whose label key or label value contains a specific label are filtered.
        self.label = label
        # The model name used to filter the returned models.
        self.model_name = model_name
        # The model type.
        self.model_type = model_type
        # The order in which the entries are sorted by the specific field on the returned page. Default value: ASC.
        # 
        # *   ASC
        # *   DESC
        self.order = order
        # The model source used to filter the models that belong to a community or organization, such as ModelScope and Hugging Face.
        self.origin = origin
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The provider. If you configure this parameter, only the models exposed by the provider are returned. If you leave this parameter empty, only models owned by the user are returned.
        self.provider = provider
        # The query condition. For example, if you set the value to nlp, all models that match ModelName, Domain, Task, LabelKey, and LabelValue are returned.
        self.query = query
        # The field used to sort the results. The GmtCreateTime field is used for sorting.
        self.sort_by = sort_by
        # The tags of the model.
        self.tag_shrink = tag_shrink
        # The task used to filter the models that belong to the task type. Example: text-classification.
        self.task = task
        # The workspace ID. Only models in this workspace are queried. You can call [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html) to obtain the workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.collections is not None:
            result['Collections'] = self.collections

        if self.conditions_shrink is not None:
            result['Conditions'] = self.conditions_shrink

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

        if self.tag_shrink is not None:
            result['Tag'] = self.tag_shrink

        if self.task is not None:
            result['Task'] = self.task

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Collections') is not None:
            self.collections = m.get('Collections')

        if m.get('Conditions') is not None:
            self.conditions_shrink = m.get('Conditions')

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

        if m.get('Tag') is not None:
            self.tag_shrink = m.get('Tag')

        if m.get('Task') is not None:
            self.task = m.get('Task')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

