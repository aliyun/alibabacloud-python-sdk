# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sandbox20260820 import models as main_models
from darabonba.model import DaraModel

class PublicWarmPool(DaraModel):
    def __init__(
        self,
        capacity_observed_time: str = None,
        capacity_policy: main_models.WarmPoolCapacityPolicy = None,
        current_error: str = None,
        deleting: bool = None,
        preparing: int = None,
        ready: int = None,
        releasing: int = None,
        source_unavailable: bool = None,
        target_capacity: int = None,
        team_id: str = None,
        template_id: str = None,
    ):
        # The most recent observation time of the capacity status.
        self.capacity_observed_time = capacity_observed_time
        # The capacity policy of the warm pool, which includes the base target capacity and optional scheduled rules.
        self.capacity_policy = capacity_policy
        # The masked text of the current background error. This value is null if no error occurs.
        self.current_error = current_error
        # Indicates whether the warm pool is being deleted.
        self.deleting = deleting
        # The number of sandboxes that are currently being prepared.
        self.preparing = preparing
        # The number of sandboxes that are currently ready.
        self.ready = ready
        # The number of sandboxes that are currently being released.
        self.releasing = releasing
        # Indicates whether the source of the associated template is unavailable.
        self.source_unavailable = source_unavailable
        # The current target capacity.
        self.target_capacity = target_capacity
        # The team ID.
        self.team_id = team_id
        # The template ID, which specifies the template associated with the warm pool.
        self.template_id = template_id

    def validate(self):
        if self.capacity_policy:
            self.capacity_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.capacity_observed_time is not None:
            result['capacityObservedTime'] = self.capacity_observed_time

        if self.capacity_policy is not None:
            result['capacityPolicy'] = self.capacity_policy.to_map()

        if self.current_error is not None:
            result['currentError'] = self.current_error

        if self.deleting is not None:
            result['deleting'] = self.deleting

        if self.preparing is not None:
            result['preparing'] = self.preparing

        if self.ready is not None:
            result['ready'] = self.ready

        if self.releasing is not None:
            result['releasing'] = self.releasing

        if self.source_unavailable is not None:
            result['sourceUnavailable'] = self.source_unavailable

        if self.target_capacity is not None:
            result['targetCapacity'] = self.target_capacity

        if self.team_id is not None:
            result['teamID'] = self.team_id

        if self.template_id is not None:
            result['templateID'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('capacityObservedTime') is not None:
            self.capacity_observed_time = m.get('capacityObservedTime')

        if m.get('capacityPolicy') is not None:
            temp_model = main_models.WarmPoolCapacityPolicy()
            self.capacity_policy = temp_model.from_map(m.get('capacityPolicy'))

        if m.get('currentError') is not None:
            self.current_error = m.get('currentError')

        if m.get('deleting') is not None:
            self.deleting = m.get('deleting')

        if m.get('preparing') is not None:
            self.preparing = m.get('preparing')

        if m.get('ready') is not None:
            self.ready = m.get('ready')

        if m.get('releasing') is not None:
            self.releasing = m.get('releasing')

        if m.get('sourceUnavailable') is not None:
            self.source_unavailable = m.get('sourceUnavailable')

        if m.get('targetCapacity') is not None:
            self.target_capacity = m.get('targetCapacity')

        if m.get('teamID') is not None:
            self.team_id = m.get('teamID')

        if m.get('templateID') is not None:
            self.template_id = m.get('templateID')

        return self

