# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DisassociateAdditionalCertificatesWithListenerRequest(DaraModel):
    def __init__(
        self,
        additional_certificate_ids: List[str] = None,
        client_token: str = None,
        dry_run: bool = None,
        listener_id: str = None,
        region_id: str = None,
    ):
        # The additional certificates. You can disassociate up to 15 additional certificates in each call.
        # 
        # This parameter is required.
        self.additional_certificate_ids = additional_certificate_ids
        # The client token used to ensure the idempotence of the request.
        # 
        # You can use the client to generate this value. Ensure that the value is unique among all requests. Only ASCII characters are allowed.
        # 
        # >  If you do not specify this parameter, the value of **RequestId** is used.**** **RequestId** is different for each request.
        self.client_token = client_token
        # Specifies whether to perform a dry run. Valid values:
        # 
        # *   **true**: Validates the request without performing the operation. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the validation, the corresponding error message is returned. If the request passes the validation, the `DryRunOperation` error code is returned.
        # *   **false** (default): validates the request and performs the operation. If the request passes the validation, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The listener ID. Only TCP/SSL listener IDs are supported.
        # 
        # This parameter is required.
        self.listener_id = listener_id
        # The region ID of the NLB instance.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/443657.html) operation to query the most recent region list.
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

