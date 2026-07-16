# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_expressconnectrouter20230901 import models as main_models
from darabonba.model import DaraModel

class ModifyExpressConnectRouterInterRegionTransitModeRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        ecr_id: str = None,
        transit_mode_list: List[main_models.ModifyExpressConnectRouterInterRegionTransitModeRequestTransitModeList] = None,
        version: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run.
        # *   **false** (default): performs a dry run and performs the actual request.
        self.dry_run = dry_run
        # The ECR ID.
        # 
        # This parameter is required.
        self.ecr_id = ecr_id
        # The cross-region forwarding modes.
        self.transit_mode_list = transit_mode_list
        self.version = version

    def validate(self):
        if self.transit_mode_list:
            for v1 in self.transit_mode_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id

        result['TransitModeList'] = []
        if self.transit_mode_list is not None:
            for k1 in self.transit_mode_list:
                result['TransitModeList'].append(k1.to_map() if k1 else None)

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')

        self.transit_mode_list = []
        if m.get('TransitModeList') is not None:
            for k1 in m.get('TransitModeList'):
                temp_model = main_models.ModifyExpressConnectRouterInterRegionTransitModeRequestTransitModeList()
                self.transit_mode_list.append(temp_model.from_map(k1))

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class ModifyExpressConnectRouterInterRegionTransitModeRequestTransitModeList(DaraModel):
    def __init__(
        self,
        mode: str = None,
        region_id: str = None,
    ):
        # The cross-domain forwarding mode of the ECR. Valid values:
        # 
        # *   **ECMP**: the load balancing mode.
        # *   **NearBy**: the nearby forwarding mode.
        self.mode = mode
        # The region ID of the ECR.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mode is not None:
            result['Mode'] = self.mode

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

