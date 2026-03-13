# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pai20240521 import models as main_models
from darabonba.model import DaraModel

class QuotaConfig(DaraModel):
    def __init__(
        self,
        acs: main_models.ACS = None,
        cluster_id: str = None,
        default_gpudriver: str = None,
        enable_preempt_subquota_workloads: bool = None,
        resource_specs: List[main_models.WorkspaceSpecs] = None,
        support_gpudrivers: List[str] = None,
        support_rdma: bool = None,
        user_vpc: main_models.UserVpc = None,
    ):
        self.acs = acs
        self.cluster_id = cluster_id
        self.default_gpudriver = default_gpudriver
        self.enable_preempt_subquota_workloads = enable_preempt_subquota_workloads
        self.resource_specs = resource_specs
        self.support_gpudrivers = support_gpudrivers
        self.support_rdma = support_rdma
        self.user_vpc = user_vpc

    def validate(self):
        if self.acs:
            self.acs.validate()
        if self.resource_specs:
            for v1 in self.resource_specs:
                 if v1:
                    v1.validate()
        if self.user_vpc:
            self.user_vpc.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acs is not None:
            result['ACS'] = self.acs.to_map()

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.default_gpudriver is not None:
            result['DefaultGPUDriver'] = self.default_gpudriver

        if self.enable_preempt_subquota_workloads is not None:
            result['EnablePreemptSubquotaWorkloads'] = self.enable_preempt_subquota_workloads

        result['ResourceSpecs'] = []
        if self.resource_specs is not None:
            for k1 in self.resource_specs:
                result['ResourceSpecs'].append(k1.to_map() if k1 else None)

        if self.support_gpudrivers is not None:
            result['SupportGPUDrivers'] = self.support_gpudrivers

        if self.support_rdma is not None:
            result['SupportRDMA'] = self.support_rdma

        if self.user_vpc is not None:
            result['UserVpc'] = self.user_vpc.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ACS') is not None:
            temp_model = main_models.ACS()
            self.acs = temp_model.from_map(m.get('ACS'))

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('DefaultGPUDriver') is not None:
            self.default_gpudriver = m.get('DefaultGPUDriver')

        if m.get('EnablePreemptSubquotaWorkloads') is not None:
            self.enable_preempt_subquota_workloads = m.get('EnablePreemptSubquotaWorkloads')

        self.resource_specs = []
        if m.get('ResourceSpecs') is not None:
            for k1 in m.get('ResourceSpecs'):
                temp_model = main_models.WorkspaceSpecs()
                self.resource_specs.append(temp_model.from_map(k1))

        if m.get('SupportGPUDrivers') is not None:
            self.support_gpudrivers = m.get('SupportGPUDrivers')

        if m.get('SupportRDMA') is not None:
            self.support_rdma = m.get('SupportRDMA')

        if m.get('UserVpc') is not None:
            temp_model = main_models.UserVpc()
            self.user_vpc = temp_model.from_map(m.get('UserVpc'))

        return self

