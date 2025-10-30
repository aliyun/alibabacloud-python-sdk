# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateModelServiceShrinkRequest(DaraModel):
    def __init__(
        self,
        ai_nodes_shrink: str = None,
        client_token: str = None,
        dbinstance_id: str = None,
        description: str = None,
        enable_public_connection: bool = None,
        inference_engine: str = None,
        model_name: str = None,
        model_params_shrink: str = None,
        replicas: int = None,
        resource_group_id: str = None,
        security_iplist: str = None,
    ):
        # This parameter is required.
        self.ai_nodes_shrink = ai_nodes_shrink
        self.client_token = client_token
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        self.description = description
        self.enable_public_connection = enable_public_connection
        self.inference_engine = inference_engine
        # This parameter is required.
        self.model_name = model_name
        self.model_params_shrink = model_params_shrink
        self.replicas = replicas
        self.resource_group_id = resource_group_id
        self.security_iplist = security_iplist

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ai_nodes_shrink is not None:
            result['AiNodes'] = self.ai_nodes_shrink

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.description is not None:
            result['Description'] = self.description

        if self.enable_public_connection is not None:
            result['EnablePublicConnection'] = self.enable_public_connection

        if self.inference_engine is not None:
            result['InferenceEngine'] = self.inference_engine

        if self.model_name is not None:
            result['ModelName'] = self.model_name

        if self.model_params_shrink is not None:
            result['ModelParams'] = self.model_params_shrink

        if self.replicas is not None:
            result['Replicas'] = self.replicas

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AiNodes') is not None:
            self.ai_nodes_shrink = m.get('AiNodes')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnablePublicConnection') is not None:
            self.enable_public_connection = m.get('EnablePublicConnection')

        if m.get('InferenceEngine') is not None:
            self.inference_engine = m.get('InferenceEngine')

        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        if m.get('ModelParams') is not None:
            self.model_params_shrink = m.get('ModelParams')

        if m.get('Replicas') is not None:
            self.replicas = m.get('Replicas')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')

        return self

