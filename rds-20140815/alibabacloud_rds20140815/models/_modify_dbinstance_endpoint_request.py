# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class ModifyDBInstanceEndpointRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dbinstance_endpoint_description: str = None,
        dbinstance_endpoint_id: str = None,
        dbinstance_id: str = None,
        node_items: List[main_models.ModifyDBInstanceEndpointRequestNodeItems] = None,
        resource_owner_id: int = None,
    ):
        self.client_token = client_token
        self.dbinstance_endpoint_description = dbinstance_endpoint_description
        # This parameter is required.
        self.dbinstance_endpoint_id = dbinstance_endpoint_id
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        self.node_items = node_items
        self.resource_owner_id = resource_owner_id

    def validate(self):
        if self.node_items:
            for v1 in self.node_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dbinstance_endpoint_description is not None:
            result['DBInstanceEndpointDescription'] = self.dbinstance_endpoint_description

        if self.dbinstance_endpoint_id is not None:
            result['DBInstanceEndpointId'] = self.dbinstance_endpoint_id

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        result['NodeItems'] = []
        if self.node_items is not None:
            for k1 in self.node_items:
                result['NodeItems'].append(k1.to_map() if k1 else None)

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DBInstanceEndpointDescription') is not None:
            self.dbinstance_endpoint_description = m.get('DBInstanceEndpointDescription')

        if m.get('DBInstanceEndpointId') is not None:
            self.dbinstance_endpoint_id = m.get('DBInstanceEndpointId')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        self.node_items = []
        if m.get('NodeItems') is not None:
            for k1 in m.get('NodeItems'):
                temp_model = main_models.ModifyDBInstanceEndpointRequestNodeItems()
                self.node_items.append(temp_model.from_map(k1))

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

class ModifyDBInstanceEndpointRequestNodeItems(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        node_id: str = None,
        weight: int = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.node_id = node_id
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

