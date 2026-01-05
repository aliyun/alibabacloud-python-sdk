# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateApplicationShrinkRequest(DaraModel):
    def __init__(
        self,
        application_type: str = None,
        architecture: str = None,
        auto_create_polar_fs: bool = None,
        auto_renew: bool = None,
        auto_use_coupon: bool = None,
        components_shrink: str = None,
        dbcluster_id: str = None,
        description: str = None,
        dry_run: bool = None,
        endpoints_shrink: str = None,
        pay_type: str = None,
        period: str = None,
        polar_fsinstance_id: str = None,
        promotion_code: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        used_time: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # This parameter is required.
        self.application_type = application_type
        # This parameter is required.
        self.architecture = architecture
        self.auto_create_polar_fs = auto_create_polar_fs
        self.auto_renew = auto_renew
        self.auto_use_coupon = auto_use_coupon
        self.components_shrink = components_shrink
        self.dbcluster_id = dbcluster_id
        self.description = description
        self.dry_run = dry_run
        self.endpoints_shrink = endpoints_shrink
        self.pay_type = pay_type
        self.period = period
        self.polar_fsinstance_id = polar_fsinstance_id
        self.promotion_code = promotion_code
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.used_time = used_time
        self.v_switch_id = v_switch_id
        self.vpc_id = vpc_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_type is not None:
            result['ApplicationType'] = self.application_type

        if self.architecture is not None:
            result['Architecture'] = self.architecture

        if self.auto_create_polar_fs is not None:
            result['AutoCreatePolarFs'] = self.auto_create_polar_fs

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.auto_use_coupon is not None:
            result['AutoUseCoupon'] = self.auto_use_coupon

        if self.components_shrink is not None:
            result['Components'] = self.components_shrink

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.description is not None:
            result['Description'] = self.description

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.endpoints_shrink is not None:
            result['Endpoints'] = self.endpoints_shrink

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.period is not None:
            result['Period'] = self.period

        if self.polar_fsinstance_id is not None:
            result['PolarFSInstanceId'] = self.polar_fsinstance_id

        if self.promotion_code is not None:
            result['PromotionCode'] = self.promotion_code

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.used_time is not None:
            result['UsedTime'] = self.used_time

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')

        if m.get('Architecture') is not None:
            self.architecture = m.get('Architecture')

        if m.get('AutoCreatePolarFs') is not None:
            self.auto_create_polar_fs = m.get('AutoCreatePolarFs')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('AutoUseCoupon') is not None:
            self.auto_use_coupon = m.get('AutoUseCoupon')

        if m.get('Components') is not None:
            self.components_shrink = m.get('Components')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('Endpoints') is not None:
            self.endpoints_shrink = m.get('Endpoints')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PolarFSInstanceId') is not None:
            self.polar_fsinstance_id = m.get('PolarFSInstanceId')

        if m.get('PromotionCode') is not None:
            self.promotion_code = m.get('PromotionCode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

