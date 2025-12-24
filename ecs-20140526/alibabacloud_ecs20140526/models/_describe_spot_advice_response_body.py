# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeSpotAdviceResponseBody(DaraModel):
    def __init__(
        self,
        available_spot_zones: main_models.DescribeSpotAdviceResponseBodyAvailableSpotZones = None,
        region_id: str = None,
        request_id: str = None,
    ):
        # Details about spot instances in the zones of the specified region.
        # 
        # >  The return values are sorted based on the historical percentages of average spot instance prices relative to pay-as-you-go instance prices for instance types.
        self.available_spot_zones = available_spot_zones
        # The region ID.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.available_spot_zones:
            self.available_spot_zones.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_spot_zones is not None:
            result['AvailableSpotZones'] = self.available_spot_zones.to_map()

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableSpotZones') is not None:
            temp_model = main_models.DescribeSpotAdviceResponseBodyAvailableSpotZones()
            self.available_spot_zones = temp_model.from_map(m.get('AvailableSpotZones'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeSpotAdviceResponseBodyAvailableSpotZones(DaraModel):
    def __init__(
        self,
        available_spot_zone: List[main_models.DescribeSpotAdviceResponseBodyAvailableSpotZonesAvailableSpotZone] = None,
    ):
        self.available_spot_zone = available_spot_zone

    def validate(self):
        if self.available_spot_zone:
            for v1 in self.available_spot_zone:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AvailableSpotZone'] = []
        if self.available_spot_zone is not None:
            for k1 in self.available_spot_zone:
                result['AvailableSpotZone'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.available_spot_zone = []
        if m.get('AvailableSpotZone') is not None:
            for k1 in m.get('AvailableSpotZone'):
                temp_model = main_models.DescribeSpotAdviceResponseBodyAvailableSpotZonesAvailableSpotZone()
                self.available_spot_zone.append(temp_model.from_map(k1))

        return self

class DescribeSpotAdviceResponseBodyAvailableSpotZonesAvailableSpotZone(DaraModel):
    def __init__(
        self,
        available_spot_resources: main_models.DescribeSpotAdviceResponseBodyAvailableSpotZonesAvailableSpotZoneAvailableSpotResources = None,
        zone_id: str = None,
    ):
        # Details about spot instances in the previous 30 days, including the release rate of spot instances and percentages of average spot instance prices relative to pay-as-you-go instance prices.
        self.available_spot_resources = available_spot_resources
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        if self.available_spot_resources:
            self.available_spot_resources.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_spot_resources is not None:
            result['AvailableSpotResources'] = self.available_spot_resources.to_map()

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableSpotResources') is not None:
            temp_model = main_models.DescribeSpotAdviceResponseBodyAvailableSpotZonesAvailableSpotZoneAvailableSpotResources()
            self.available_spot_resources = temp_model.from_map(m.get('AvailableSpotResources'))

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeSpotAdviceResponseBodyAvailableSpotZonesAvailableSpotZoneAvailableSpotResources(DaraModel):
    def __init__(
        self,
        available_spot_resource: List[main_models.DescribeSpotAdviceResponseBodyAvailableSpotZonesAvailableSpotZoneAvailableSpotResourcesAvailableSpotResource] = None,
    ):
        self.available_spot_resource = available_spot_resource

    def validate(self):
        if self.available_spot_resource:
            for v1 in self.available_spot_resource:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AvailableSpotResource'] = []
        if self.available_spot_resource is not None:
            for k1 in self.available_spot_resource:
                result['AvailableSpotResource'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.available_spot_resource = []
        if m.get('AvailableSpotResource') is not None:
            for k1 in m.get('AvailableSpotResource'):
                temp_model = main_models.DescribeSpotAdviceResponseBodyAvailableSpotZonesAvailableSpotZoneAvailableSpotResourcesAvailableSpotResource()
                self.available_spot_resource.append(temp_model.from_map(k1))

        return self

class DescribeSpotAdviceResponseBodyAvailableSpotZonesAvailableSpotZoneAvailableSpotResourcesAvailableSpotResource(DaraModel):
    def __init__(
        self,
        average_spot_discount: int = None,
        instance_type: str = None,
        interrupt_rate_desc: str = None,
        interruption_rate: float = None,
    ):
        # The percentage of the average spot instance price relative to the pay-as-you-go instance price in the previous 30 days. Unit: %. Valid values: 1 to 100.
        # 
        # You can calculate the average spot instance price based on the return value. For example, if the pay-as-you-go instance price is 1 and the return value of this parameter is 20, the average spot instance price in the previous 30 days is 0.2.
        self.average_spot_discount = average_spot_discount
        # The instance type.
        self.instance_type = instance_type
        # The release rate range of spot instances in the previous 30 days, which corresponds to the `InterruptionRate` value. Valid values:
        # 
        # *   0-3%
        # *   3-5%
        # *   5-10%
        # *   10-100%
        self.interrupt_rate_desc = interrupt_rate_desc
        # The average release rate of spot instances in the previous 30 days. Unit: %.
        self.interruption_rate = interruption_rate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.average_spot_discount is not None:
            result['AverageSpotDiscount'] = self.average_spot_discount

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.interrupt_rate_desc is not None:
            result['InterruptRateDesc'] = self.interrupt_rate_desc

        if self.interruption_rate is not None:
            result['InterruptionRate'] = self.interruption_rate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AverageSpotDiscount') is not None:
            self.average_spot_discount = m.get('AverageSpotDiscount')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('InterruptRateDesc') is not None:
            self.interrupt_rate_desc = m.get('InterruptRateDesc')

        if m.get('InterruptionRate') is not None:
            self.interruption_rate = m.get('InterruptionRate')

        return self

