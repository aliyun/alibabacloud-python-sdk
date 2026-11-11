# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetListenerAttributeRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        listener_id: str = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can generate the parameter value from your client to ensure that it is unique among different requests. The ClientToken parameter supports only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** of each API request is different.
        self.client_token = client_token
        # Specifies whether to only precheck the request. Valid values:
        # - **true**: sends a check request and does not query the listener details. Check items include whether required parameters are specified, the request format, and service limits. If the check fails, the corresponding error is returned. If the check succeeds, the error code `DryRunOperation` is returned.
        # - **false** (default): sends a normal request. After the check succeeds, the HTTP 2xx status code is returned and the operation is directly performed.
        self.dry_run = dry_run
        # The listener ID.
        # 
        # This parameter is required.
        self.listener_id = listener_id
        # The region ID of the Network Load Balancer (NLB) instance. 
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
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

