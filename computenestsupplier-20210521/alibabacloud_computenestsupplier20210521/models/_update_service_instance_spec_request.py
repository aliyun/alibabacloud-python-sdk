# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class UpdateServiceInstanceSpecRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        enable_user_prometheus: bool = None,
        operation_name: str = None,
        parameters: Dict[str, Any] = None,
        predefined_parameters_name: str = None,
        service_instance_id: str = None,
    ):
        # A unique identifier that you provide to ensure the idempotence of the request. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # Specifies whether to enable Prometheus on the client. Valid values:
        # 
        # - true: Enables Prometheus.
        # 
        # - false: Disables Prometheus.
        self.enable_user_prometheus = enable_user_prometheus
        # The name of the upgrade or downgrade action.
        self.operation_name = operation_name
        # The configuration parameters of the service instance.
        self.parameters = parameters
        # The package name.
        self.predefined_parameters_name = predefined_parameters_name
        # The ID of the service instance.
        self.service_instance_id = service_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.enable_user_prometheus is not None:
            result['EnableUserPrometheus'] = self.enable_user_prometheus

        if self.operation_name is not None:
            result['OperationName'] = self.operation_name

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.predefined_parameters_name is not None:
            result['PredefinedParametersName'] = self.predefined_parameters_name

        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('EnableUserPrometheus') is not None:
            self.enable_user_prometheus = m.get('EnableUserPrometheus')

        if m.get('OperationName') is not None:
            self.operation_name = m.get('OperationName')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('PredefinedParametersName') is not None:
            self.predefined_parameters_name = m.get('PredefinedParametersName')

        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')

        return self

