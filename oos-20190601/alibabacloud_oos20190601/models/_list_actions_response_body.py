# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_oos20190601 import models as main_models
from darabonba.model import DaraModel

class ListActionsResponseBody(DaraModel):
    def __init__(
        self,
        actions: List[main_models.ListActionsResponseBodyActions] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The details of the actions.
        self.actions = actions
        # The number of entries returned per page.
        self.max_results = max_results
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.actions:
            for v1 in self.actions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Actions'] = []
        if self.actions is not None:
            for k1 in self.actions:
                result['Actions'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.actions = []
        if m.get('Actions') is not None:
            for k1 in m.get('Actions'):
                temp_model = main_models.ListActionsResponseBodyActions()
                self.actions.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListActionsResponseBodyActions(DaraModel):
    def __init__(
        self,
        action_type: str = None,
        created_date: str = None,
        description: str = None,
        oosaction_name: str = None,
        popularity: int = None,
        properties: str = None,
        template_version: str = None,
    ):
        # The type of the action.
        # 
        # 1.  Atomic actions
        # 
        #     *   Atomic.API
        #     *   Atomic.Trigger
        #     *   Atomic.Control
        #     *   Atomic.Embedded
        # 
        # 2.  Cloud product actions
        # 
        #     *   Product.ECS
        #     *   Product.RDS
        #     *   Product.VPC
        #     *   Product.FC
        #     *   ...
        self.action_type = action_type
        # The time when the action was created.
        self.created_date = created_date
        # The description of the action.
        self.description = description
        # The name of the action.
        self.oosaction_name = oosaction_name
        # The number of times that the action is used.
        self.popularity = popularity
        # The parameters of the action.
        self.properties = properties
        # The version of the template that corresponds to the action.
        # 
        # >  For atomic actions, this parameter is not returned.
        self.template_version = template_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_type is not None:
            result['ActionType'] = self.action_type

        if self.created_date is not None:
            result['CreatedDate'] = self.created_date

        if self.description is not None:
            result['Description'] = self.description

        if self.oosaction_name is not None:
            result['OOSActionName'] = self.oosaction_name

        if self.popularity is not None:
            result['Popularity'] = self.popularity

        if self.properties is not None:
            result['Properties'] = self.properties

        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')

        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('OOSActionName') is not None:
            self.oosaction_name = m.get('OOSActionName')

        if m.get('Popularity') is not None:
            self.popularity = m.get('Popularity')

        if m.get('Properties') is not None:
            self.properties = m.get('Properties')

        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')

        return self

