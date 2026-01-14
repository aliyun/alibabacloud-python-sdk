# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class UpdateCustomRoutingEndpointGroupDestinationsRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        destination_configurations: List[main_models.UpdateCustomRoutingEndpointGroupDestinationsRequestDestinationConfigurations] = None,
        dry_run: bool = None,
        endpoint_group_id: str = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must ensure that it is unique among all requests. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the value of **RequestId** as the value of **ClientToken**. The value of **RequestId** for each API request may be different.
        self.client_token = client_token
        # The mapping configurations of endpoint group.
        # 
        # You must specify the backend service port range and protocol of the endpoint group. The specified information is used to map the port range of the associated listener.
        # 
        # You can specify at most 20 mapping configurations, which include port ranges and protocol types.
        # 
        # This parameter is required.
        self.destination_configurations = destination_configurations
        # Specifies whether to perform a dry run. Valid values:
        # 
        # *   **true**: performs a dry run. The system checks the required parameters, request syntax, and limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false**: performs a dry run and sends the request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The ID of the endpoint group.
        # 
        # This parameter is required.
        self.endpoint_group_id = endpoint_group_id
        # The ID of the region where the GA instance is deployed. Set the value to **cn-hangzhou**.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        if self.destination_configurations:
            for v1 in self.destination_configurations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        result['DestinationConfigurations'] = []
        if self.destination_configurations is not None:
            for k1 in self.destination_configurations:
                result['DestinationConfigurations'].append(k1.to_map() if k1 else None)

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        self.destination_configurations = []
        if m.get('DestinationConfigurations') is not None:
            for k1 in m.get('DestinationConfigurations'):
                temp_model = main_models.UpdateCustomRoutingEndpointGroupDestinationsRequestDestinationConfigurations()
                self.destination_configurations.append(temp_model.from_map(k1))

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class UpdateCustomRoutingEndpointGroupDestinationsRequestDestinationConfigurations(DaraModel):
    def __init__(
        self,
        destination_id: str = None,
        from_port: int = None,
        protocols: List[str] = None,
        to_port: int = None,
    ):
        # The ID of the mapping configuration of the endpoint group.
        # 
        # This parameter is required.
        self.destination_id = destination_id
        # The start port of the backend service port range of the endpoint group.
        # 
        # Valid values: **1** to **65499**. The **FromPort** value must be smaller than or equal to the **ToPort** value.
        # 
        # You can specify up to 20 start ports in each request.
        self.from_port = from_port
        # The backend service protocol of the endpoint group. Valid values:
        # 
        # *   **tcp**: TCP
        # *   **udp**: UDP
        # *   **tcp,udp**: TCP and UDP
        # 
        # You can specify up to four backend service protocols in each configuration.
        self.protocols = protocols
        # The end port of the backend service port range of the endpoint group.
        # 
        # Valid values: **1** to **65499**. The **FromPort** value must be smaller than or equal to the **ToPort** value.
        # 
        # You can specify up to 20 end ports in each request.
        self.to_port = to_port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.destination_id is not None:
            result['DestinationId'] = self.destination_id

        if self.from_port is not None:
            result['FromPort'] = self.from_port

        if self.protocols is not None:
            result['Protocols'] = self.protocols

        if self.to_port is not None:
            result['ToPort'] = self.to_port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationId') is not None:
            self.destination_id = m.get('DestinationId')

        if m.get('FromPort') is not None:
            self.from_port = m.get('FromPort')

        if m.get('Protocols') is not None:
            self.protocols = m.get('Protocols')

        if m.get('ToPort') is not None:
            self.to_port = m.get('ToPort')

        return self

