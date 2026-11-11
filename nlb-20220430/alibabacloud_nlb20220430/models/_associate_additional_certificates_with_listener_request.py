# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AssociateAdditionalCertificatesWithListenerRequest(DaraModel):
    def __init__(
        self,
        additional_certificate_ids: List[str] = None,
        client_token: str = None,
        dry_run: bool = None,
        listener_id: str = None,
        region_id: str = None,
    ):
        # The list of additional certificates. You can associate up to 15 additional certificates with a listener in a single call.
        # 
        # This parameter is required.
        self.additional_certificate_ids = additional_certificate_ids
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can generate a value for this parameter on your client to ensure that the value is unique across different requests. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** of each API request is unique.
        self.client_token = client_token
        # Specifies whether to only precheck this request. Valid values:
        # - **true**: sends a check request and does not add the additional certificates to the TCPSSL listener. The system checks whether the required parameters are specified, the request format is valid, and the service limits are met. If the request fails the check, the system returns an error. If the request passes the check, the system returns the error code `DryRunOperation`.
        # - **false** (default): sends a standard request. If the request passes the check, the system returns an HTTP 2xx status code and performs the operation.
        self.dry_run = dry_run
        # The ID of the listener. This operation only supports TCPSSL listener IDs.
        # 
        # This parameter is required.
        self.listener_id = listener_id
        # The ID of the region where the Network Load Balancer (NLB) instance is deployed. 
        # 
        # You can invoke the [DescribeRegions](https://help.aliyun.com/document_detail/443657.html) operation to query region IDs.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.additional_certificate_ids is not None:
            result['AdditionalCertificateIds'] = self.additional_certificate_ids

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdditionalCertificateIds') is not None:
            self.additional_certificate_ids = m.get('AdditionalCertificateIds')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

