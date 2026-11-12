# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DissociateSmartAGFromApplicationBandwidthPackageRequest(DaraModel):
    def __init__(
        self,
        application_bandwidth_package_id: str = None,
        client_token: str = None,
        dry_run: bool = None,
        region_id: str = None,
        smart_agid: str = None,
        smart_agid_list: List[str] = None,
    ):
        # The instance ID of the bandwidth plan for application acceleration.
        # 
        # This parameter is required.
        self.application_bandwidth_package_id = application_bandwidth_package_id
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, and you must make sure that the value is unique among different requests. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the RequestId of the API request as the client token. The RequestId of each API request may be different.
        self.client_token = client_token
        # Specifies whether to perform a dry run on the disassociation request. The dry run includes checks on permissions and instance status. Valid values:
        # 
        # - **false** (default): Sends a normal request. If the request passes the check, the bandwidth plan for application acceleration is disassociated from the Smart Access Gateway instance.
        # - **true**: Sends a dry run request. Only the check is performed, and the bandwidth plan for application acceleration is not disassociated from the Smart Access Gateway instance. Check items include whether required parameters are specified and the request format. If the check fails, the corresponding error is returned. If the check passes, the `DryRunOperation` error code is returned.
        self.dry_run = dry_run
        # The region ID of the bandwidth plan for application acceleration.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query region IDs.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The instance ID of the Smart Access Gateway.
        self.smart_agid = smart_agid
        # The list of Smart Access Gateway instance IDs.
        # 
        # You can enter up to 100 Smart Access Gateway instance IDs at a time.
        self.smart_agid_list = smart_agid_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_bandwidth_package_id is not None:
            result['ApplicationBandwidthPackageId'] = self.application_bandwidth_package_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.smart_agid is not None:
            result['SmartAGId'] = self.smart_agid

        if self.smart_agid_list is not None:
            result['SmartAGIdList'] = self.smart_agid_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationBandwidthPackageId') is not None:
            self.application_bandwidth_package_id = m.get('ApplicationBandwidthPackageId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SmartAGId') is not None:
            self.smart_agid = m.get('SmartAGId')

        if m.get('SmartAGIdList') is not None:
            self.smart_agid_list = m.get('SmartAGIdList')

        return self

