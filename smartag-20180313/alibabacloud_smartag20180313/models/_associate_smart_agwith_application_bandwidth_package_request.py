# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_smartag20180313 import models as main_models
from darabonba.model import DaraModel

class AssociateSmartAGWithApplicationBandwidthPackageRequest(DaraModel):
    def __init__(
        self,
        application_bandwidth_package_id: str = None,
        associate_configs: List[main_models.AssociateSmartAGWithApplicationBandwidthPackageRequestAssociateConfigs] = None,
        client_token: str = None,
        dry_run: bool = None,
        region_id: str = None,
    ):
        # The instance ID of the bandwidth plan for application acceleration.
        # 
        # This parameter is required.
        self.application_bandwidth_package_id = application_bandwidth_package_id
        # The list of Smart Access Gateway instances to be associated.
        # 
        # This parameter is required.
        self.associate_configs = associate_configs
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must make sure that the value is unique among different requests. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the RequestId of the API request as the client token. The RequestId of each API request may be different.
        self.client_token = client_token
        # Specifies whether to perform a dry run on the association request. The dry run includes permission and instance status checks. Valid values:
        # 
        # - **false** (default): Sends a normal request and associates the bandwidth plan for application acceleration with the Smart Access Gateway instance after the request passes the check.
        # - **true**: Sends a check request and performs only the check without associating the bandwidth plan for application acceleration with the Smart Access Gateway instance. The check items include whether required parameters are specified and whether the request format is valid. If the request fails the check, an error is returned. If the request passes the check, the `DryRunOperation` error code is returned.
        self.dry_run = dry_run
        # The ID of the region to which the bandwidth plan for application acceleration belongs.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query region IDs.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        if self.associate_configs:
            for v1 in self.associate_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_bandwidth_package_id is not None:
            result['ApplicationBandwidthPackageId'] = self.application_bandwidth_package_id

        result['AssociateConfigs'] = []
        if self.associate_configs is not None:
            for k1 in self.associate_configs:
                result['AssociateConfigs'].append(k1.to_map() if k1 else None)

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationBandwidthPackageId') is not None:
            self.application_bandwidth_package_id = m.get('ApplicationBandwidthPackageId')

        self.associate_configs = []
        if m.get('AssociateConfigs') is not None:
            for k1 in m.get('AssociateConfigs'):
                temp_model = main_models.AssociateSmartAGWithApplicationBandwidthPackageRequestAssociateConfigs()
                self.associate_configs.append(temp_model.from_map(k1))

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class AssociateSmartAGWithApplicationBandwidthPackageRequestAssociateConfigs(DaraModel):
    def __init__(
        self,
        bandwidth: int = None,
        smart_agid: str = None,
    ):
        # The peak bandwidth for application acceleration of the Smart Access Gateway instance. Unit: Mbit/s.
        # 
        # > The peak bandwidth for application acceleration of each Smart Access Gateway instance cannot exceed the peak bandwidth of the associated bandwidth plan for application acceleration.
        # 
        # This parameter is required.
        self.bandwidth = bandwidth
        # The Smart Access Gateway instance ID.
        # 
        # This parameter is required.
        self.smart_agid = smart_agid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.smart_agid is not None:
            result['SmartAGId'] = self.smart_agid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('SmartAGId') is not None:
            self.smart_agid = m.get('SmartAGId')

        return self

