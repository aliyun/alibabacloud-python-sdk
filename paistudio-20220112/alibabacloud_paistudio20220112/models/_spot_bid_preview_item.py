# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SpotBidPreviewItem(DaraModel):
    def __init__(
        self,
        active: bool = None,
        allow_cross_hpn_zone: bool = None,
        cluster_id: str = None,
        gc_level: str = None,
        instance_type: str = None,
        job_name: str = None,
        max_discount: float = None,
        message: str = None,
        name: str = None,
        phase: str = None,
        replicas: int = None,
    ):
        # Indicates whether the spot bid is active. If set to `false`, the bid is paused.
        self.active = active
        # Determines whether instances can be deployed across different High-Performance Network (HPN) zones. Defaults to `false`.
        self.allow_cross_hpn_zone = allow_cross_hpn_zone
        # The ID of the cluster where resources are provisioned.
        self.cluster_id = cluster_id
        # The GC level for the spot instance.
        self.gc_level = gc_level
        # The type of compute instance.
        self.instance_type = instance_type
        # The name of the associated job.
        self.job_name = job_name
        # The maximum discount percentage from the on-demand price.
        self.max_discount = max_discount
        # A message that provides additional details about the current phase.
        self.message = message
        # The name of the spot bid preview.
        self.name = name
        # The current phase of the spot bid preview. Valid values are `Pending`, `Active`, and `Failed`.
        self.phase = phase
        # The number of instance replicas.
        self.replicas = replicas

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active is not None:
            result['active'] = self.active

        if self.allow_cross_hpn_zone is not None:
            result['allowCrossHpnZone'] = self.allow_cross_hpn_zone

        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id

        if self.gc_level is not None:
            result['gcLevel'] = self.gc_level

        if self.instance_type is not None:
            result['instanceType'] = self.instance_type

        if self.job_name is not None:
            result['jobName'] = self.job_name

        if self.max_discount is not None:
            result['maxDiscount'] = self.max_discount

        if self.message is not None:
            result['message'] = self.message

        if self.name is not None:
            result['name'] = self.name

        if self.phase is not None:
            result['phase'] = self.phase

        if self.replicas is not None:
            result['replicas'] = self.replicas

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')

        if m.get('allowCrossHpnZone') is not None:
            self.allow_cross_hpn_zone = m.get('allowCrossHpnZone')

        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')

        if m.get('gcLevel') is not None:
            self.gc_level = m.get('gcLevel')

        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')

        if m.get('jobName') is not None:
            self.job_name = m.get('jobName')

        if m.get('maxDiscount') is not None:
            self.max_discount = m.get('maxDiscount')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('phase') is not None:
            self.phase = m.get('phase')

        if m.get('replicas') is not None:
            self.replicas = m.get('replicas')

        return self

