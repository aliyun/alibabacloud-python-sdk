# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateExperimentGroupRequest(DaraModel):
    def __init__(
        self,
        config: str = None,
        crowd_id: str = None,
        crowd_target_type: str = None,
        debug_crowd_id: str = None,
        debug_users: str = None,
        description: str = None,
        distribution_time_duration: int = None,
        distribution_type: str = None,
        filter: str = None,
        instance_id: str = None,
        layer_id: str = None,
        name: str = None,
        need_aa: bool = None,
        random_flow: int = None,
        reservced_buckets: str = None,
    ):
        # The configuration of the experiment group.
        self.config = config
        # The ID of the crowd for crowd targeting. You can obtain this ID by calling the ListCrowds API.
        self.crowd_id = crowd_id
        # The type of crowd targeting for the experiment group. Valid values:
        # 
        # - All: all traffic
        # 
        # - Filter: traffic that matches the filter condition
        # 
        # - CrowdId: traffic from the specified crowd ID
        # 
        # - Random: a random percentage of traffic
        self.crowd_target_type = crowd_target_type
        # The ID of the debug crowd. You can obtain this ID by calling the ListCrowds API.
        self.debug_crowd_id = debug_crowd_id
        # A comma-separated list of UIDs for debug users. The UIDs can belong to Alibaba Cloud main accounts or sub-accounts.
        self.debug_users = debug_users
        # The description of the experiment group.
        # 
        # This parameter is required.
        self.description = description
        # The time duration for traffic distribution.
        self.distribution_time_duration = distribution_time_duration
        # The distribution type. ● UserId: Distributes traffic by user ID. ● TimeDuration: Distributes traffic by time duration.
        self.distribution_type = distribution_type
        # The filter condition for crowd targeting.
        self.filter = filter
        # The ID of the instance. You can obtain this ID by calling the ListInstances API.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the layer. You can obtain this ID by calling the ListLayers API.
        # 
        # This parameter is required.
        self.layer_id = layer_id
        # The name of the experiment group.
        # 
        # This parameter is required.
        self.name = name
        # Specifies whether an AA experiment group is required.
        self.need_aa = need_aa
        # If CrowdTargetType is set to Random, this parameter specifies the percentage of traffic (from 0 to 100) to route to the experiment group.
        self.random_flow = random_flow
        # The reserved buckets.
        self.reservced_buckets = reservced_buckets

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.crowd_id is not None:
            result['CrowdId'] = self.crowd_id

        if self.crowd_target_type is not None:
            result['CrowdTargetType'] = self.crowd_target_type

        if self.debug_crowd_id is not None:
            result['DebugCrowdId'] = self.debug_crowd_id

        if self.debug_users is not None:
            result['DebugUsers'] = self.debug_users

        if self.description is not None:
            result['Description'] = self.description

        if self.distribution_time_duration is not None:
            result['DistributionTimeDuration'] = self.distribution_time_duration

        if self.distribution_type is not None:
            result['DistributionType'] = self.distribution_type

        if self.filter is not None:
            result['Filter'] = self.filter

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.layer_id is not None:
            result['LayerId'] = self.layer_id

        if self.name is not None:
            result['Name'] = self.name

        if self.need_aa is not None:
            result['NeedAA'] = self.need_aa

        if self.random_flow is not None:
            result['RandomFlow'] = self.random_flow

        if self.reservced_buckets is not None:
            result['ReservcedBuckets'] = self.reservced_buckets

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('CrowdId') is not None:
            self.crowd_id = m.get('CrowdId')

        if m.get('CrowdTargetType') is not None:
            self.crowd_target_type = m.get('CrowdTargetType')

        if m.get('DebugCrowdId') is not None:
            self.debug_crowd_id = m.get('DebugCrowdId')

        if m.get('DebugUsers') is not None:
            self.debug_users = m.get('DebugUsers')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DistributionTimeDuration') is not None:
            self.distribution_time_duration = m.get('DistributionTimeDuration')

        if m.get('DistributionType') is not None:
            self.distribution_type = m.get('DistributionType')

        if m.get('Filter') is not None:
            self.filter = m.get('Filter')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LayerId') is not None:
            self.layer_id = m.get('LayerId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NeedAA') is not None:
            self.need_aa = m.get('NeedAA')

        if m.get('RandomFlow') is not None:
            self.random_flow = m.get('RandomFlow')

        if m.get('ReservcedBuckets') is not None:
            self.reservced_buckets = m.get('ReservcedBuckets')

        return self

