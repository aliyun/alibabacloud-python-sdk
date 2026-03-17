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
        # The ID of the bandwidth plan for application acceleration.
        # 
        # This parameter is required.
        self.application_bandwidth_package_id = application_bandwidth_package_id
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not set this parameter, ClientToken is set to the value of RequestId. The value of RequestId for each API request may be different.
        self.client_token = client_token
        # Specifies whether to precheck the request. Check items include permissions and the status of the specified cloud resources. Valid values:
        # 
        # *   **false** (default): sends the request. After the request passes the check, the SAG instance is disassociated from the bandwidth plan for application acceleration.
        # *   **true**: prechecks the request but does not disassociate the SAG instance from the bandwidth plan for application acceleration. If you use this value, the system checks the required parameters and the request syntax. If the request fails the precheck, an error message is returned. If the request passes the precheck, the `DryRunOperation` error code is returned.
        self.dry_run = dry_run
        # The region ID of the bandwidth plan for application acceleration.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the SAG instance.
        self.smart_agid = smart_agid
        # The list of the SAG instance id.
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

