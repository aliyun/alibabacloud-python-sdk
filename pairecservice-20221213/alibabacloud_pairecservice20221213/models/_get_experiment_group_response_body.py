# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetExperimentGroupResponseBody(DaraModel):
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
        holding_buckets: str = None,
        laboratory_id: str = None,
        layer_id: str = None,
        name: str = None,
        need_aa: bool = None,
        owner: str = None,
        random_flow: int = None,
        request_id: str = None,
        reserved_buckets: str = None,
        scene_id: str = None,
        status: str = None,
    ):
        self.config = config
        self.crowd_id = crowd_id
        self.crowd_target_type = crowd_target_type
        self.debug_crowd_id = debug_crowd_id
        self.debug_users = debug_users
        self.description = description
        self.distribution_time_duration = distribution_time_duration
        self.distribution_type = distribution_type
        self.filter = filter
        self.holding_buckets = holding_buckets
        self.laboratory_id = laboratory_id
        self.layer_id = layer_id
        self.name = name
        self.need_aa = need_aa
        self.owner = owner
        self.random_flow = random_flow
        # Id of the request
        self.request_id = request_id
        self.reserved_buckets = reserved_buckets
        self.scene_id = scene_id
        self.status = status

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

        if self.holding_buckets is not None:
            result['HoldingBuckets'] = self.holding_buckets

        if self.laboratory_id is not None:
            result['LaboratoryId'] = self.laboratory_id

        if self.layer_id is not None:
            result['LayerId'] = self.layer_id

        if self.name is not None:
            result['Name'] = self.name

        if self.need_aa is not None:
            result['NeedAA'] = self.need_aa

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.random_flow is not None:
            result['RandomFlow'] = self.random_flow

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.reserved_buckets is not None:
            result['ReservedBuckets'] = self.reserved_buckets

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        if self.status is not None:
            result['Status'] = self.status

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

        if m.get('HoldingBuckets') is not None:
            self.holding_buckets = m.get('HoldingBuckets')

        if m.get('LaboratoryId') is not None:
            self.laboratory_id = m.get('LaboratoryId')

        if m.get('LayerId') is not None:
            self.layer_id = m.get('LayerId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NeedAA') is not None:
            self.need_aa = m.get('NeedAA')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('RandomFlow') is not None:
            self.random_flow = m.get('RandomFlow')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ReservedBuckets') is not None:
            self.reserved_buckets = m.get('ReservedBuckets')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

