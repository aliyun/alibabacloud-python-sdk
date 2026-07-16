# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class CreateCustomRoutingEndpointGroupDestinationsRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        destination_configurations: List[main_models.CreateCustomRoutingEndpointGroupDestinationsRequestDestinationConfigurations] = None,
        dry_run: bool = None,
        endpoint_group_id: str = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** may be different for each API request.
        self.client_token = client_token
        # The mapping configurations of the endpoint group.
        # 
        # Specify the service port ranges and protocol types of the backend services for the endpoint group. The specified information is mapped to the associated listener port ranges.
        # 
        # You can specify up to 20 port ranges and protocol types in a single invoke of this operation.
        # 
        # This parameter is required.
        self.destination_configurations = destination_configurations
        # Specifies whether to perform a dry run. Valid values:
        # - **true**: performs a dry run. The system checks the required parameters, request syntax, and business limitations without actually creating the mapping configurations create an endpoint group. If the request fails the dry run, the corresponding error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # - **false** (default): performs a dry run and sends the request. If the request passes the dry run, an HTTP 2xx status code is returned and the mapping configurations create an endpoint group are created.
        self.dry_run = dry_run
        # The endpoint group ID.
        # 
        # This parameter is required.
        self.endpoint_group_id = endpoint_group_id
        # The region ID of the Alibaba Cloud Global Accelerator (GA) instance. Set the value to **ap-southeast-1**.
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
                temp_model = main_models.CreateCustomRoutingEndpointGroupDestinationsRequestDestinationConfigurations()
                self.destination_configurations.append(temp_model.from_map(k1))

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class CreateCustomRoutingEndpointGroupDestinationsRequestDestinationConfigurations(DaraModel):
    def __init__(
        self,
        from_port: int = None,
        protocols: List[str] = None,
        to_port: int = None,
    ):
        # The start port of the backend service port range for the endpoint group.
        # 
        # Valid values: **1** to **65499**. The value of **FromPort** must be less than or equal to the value of **ToPort**.
        # 
        # You can specify up to 20 start ports in a single request.
        # 
        # This parameter is required.
        self.from_port = from_port
        # The protocol types of the backend services for the endpoint group. Valid values:
        # 
        # - **TCP**: TCP protocol.
        # 
        # - **UDP**: UDP protocol.
        # 
        # - **TCP,UDP**: TCP and UDP protocols.
        # 
        # The Terms of Service apply to the selected protocols.
        # 
        # This parameter is required.
        self.protocols = protocols
        # The end port of the backend service port range for the endpoint group.
        # 
        # Valid values: **1** to **65499**. The value of **FromPort** must be less than or equal to the value of **ToPort**.
        # 
        # You can specify up to 20 end ports in a single request.
        # 
        # This parameter is required.
        self.to_port = to_port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_port is not None:
            result['FromPort'] = self.from_port

        if self.protocols is not None:
            result['Protocols'] = self.protocols

        if self.to_port is not None:
            result['ToPort'] = self.to_port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromPort') is not None:
            self.from_port = m.get('FromPort')

        if m.get('Protocols') is not None:
            self.protocols = m.get('Protocols')

        if m.get('ToPort') is not None:
            self.to_port = m.get('ToPort')

        return self

