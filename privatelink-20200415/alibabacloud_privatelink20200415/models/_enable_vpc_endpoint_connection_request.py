# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EnableVpcEndpointConnectionRequest(DaraModel):
    def __init__(
        self,
        bandwidth: int = None,
        client_token: str = None,
        dry_run: bool = None,
        endpoint_id: str = None,
        region_id: str = None,
        service_id: str = None,
        traffic_control_mode: str = None,
    ):
        # The bandwidth of the endpoint connection. Unit: Mbit/s.
        # 
        # > The valid values vary depending on the service resource type:
        # > - NLB: 100 to 50000.
        # > - ALB: 100 to 25000.
        # > - CLB: 100 to 10240. Default value: 3072.
        # > - GWLB: 100 to 25000.
        self.bandwidth = bandwidth
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must ensure that it is unique among different requests. **ClientToken** can contain only ASCII characters.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # - **true**: performs only a dry run. The system checks the request for potential issues, including missing required parameters, the request format, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # 
        # - **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, an HTTP 2xx status code is returned and the connection request is accepted.
        self.dry_run = dry_run
        # The endpoint ID.
        # 
        # This parameter is required.
        self.endpoint_id = endpoint_id
        # The region ID of the endpoint connection to be accepted.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/120468.html) operation to query the region IDs.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The endpoint service ID.
        # 
        # This parameter is required.
        self.service_id = service_id
        # - Scalability: automatic scaling. In this mode, the connection bandwidth configured for the endpoint connection does not take effect.
        # 
        # - BandwidthLimit: supports setting a bandwidth upper limit for the endpoint connection. The bandwidth upper limit is the value of Bandwidth.
        #  
        # >- When the service resource is NLB, TrafficControlMode is set to Scalability by default. You can set it to BandwidthLimit and modify the value of Bandwidth to provide a bandwidth upper limit.
        # >- When the service resource is CLB, TrafficControlMode can only be set to BandwidthLimit, which indicates that the service provider provides default bandwidth throttling for each endpoint.
        # > - When the service resource is GWLB, TrafficControlMode can only be set to Scalability.
        self.traffic_control_mode = traffic_control_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.traffic_control_mode is not None:
            result['TrafficControlMode'] = self.traffic_control_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('TrafficControlMode') is not None:
            self.traffic_control_mode = m.get('TrafficControlMode')

        return self

