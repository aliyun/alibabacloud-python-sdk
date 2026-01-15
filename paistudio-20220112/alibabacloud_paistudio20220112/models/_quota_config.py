# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paistudio20220112 import models as main_models
from darabonba.model import DaraModel

class QuotaConfig(DaraModel):
    def __init__(
        self,
        acs: main_models.ACS = None,
        cluster_id: str = None,
        control_plane_cluster_id: str = None,
        default_gpudriver: str = None,
        enable_gpushare: bool = None,
        enable_preempt_subquota_workloads: bool = None,
        enable_self_quota_preemption: bool = None,
        enable_sub_quota_preemption: bool = None,
        eni_cache_config: main_models.EniCacheConfig = None,
        oversold_usage_config: main_models.OversoldUsageConfig = None,
        resource_specs: List[main_models.WorkspaceSpecs] = None,
        sandbox_cache_config: main_models.SandboxCacheConfig = None,
        self_quota_preemption_config: main_models.SelfQuotaPreemptionConfig = None,
        sub_quota_preemption_config: main_models.SubQuotaPreemptionConfig = None,
        support_gpudrivers: List[str] = None,
        support_rdma: bool = None,
        use_case: str = None,
        user_vpc: main_models.UserVpc = None,
    ):
        self.acs = acs
        self.cluster_id = cluster_id
        self.control_plane_cluster_id = control_plane_cluster_id
        self.default_gpudriver = default_gpudriver
        self.enable_gpushare = enable_gpushare
        self.enable_preempt_subquota_workloads = enable_preempt_subquota_workloads
        self.enable_self_quota_preemption = enable_self_quota_preemption
        self.enable_sub_quota_preemption = enable_sub_quota_preemption
        self.eni_cache_config = eni_cache_config
        self.oversold_usage_config = oversold_usage_config
        self.resource_specs = resource_specs
        self.sandbox_cache_config = sandbox_cache_config
        self.self_quota_preemption_config = self_quota_preemption_config
        self.sub_quota_preemption_config = sub_quota_preemption_config
        self.support_gpudrivers = support_gpudrivers
        self.support_rdma = support_rdma
        self.use_case = use_case
        self.user_vpc = user_vpc

    def validate(self):
        if self.acs:
            self.acs.validate()
        if self.eni_cache_config:
            self.eni_cache_config.validate()
        if self.oversold_usage_config:
            self.oversold_usage_config.validate()
        if self.resource_specs:
            for v1 in self.resource_specs:
                 if v1:
                    v1.validate()
        if self.sandbox_cache_config:
            self.sandbox_cache_config.validate()
        if self.self_quota_preemption_config:
            self.self_quota_preemption_config.validate()
        if self.sub_quota_preemption_config:
            self.sub_quota_preemption_config.validate()
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

        if self.control_plane_cluster_id is not None:
            result['ControlPlaneClusterId'] = self.control_plane_cluster_id

        if self.default_gpudriver is not None:
            result['DefaultGPUDriver'] = self.default_gpudriver

        if self.enable_gpushare is not None:
            result['EnableGPUShare'] = self.enable_gpushare

        if self.enable_preempt_subquota_workloads is not None:
            result['EnablePreemptSubquotaWorkloads'] = self.enable_preempt_subquota_workloads

        if self.enable_self_quota_preemption is not None:
            result['EnableSelfQuotaPreemption'] = self.enable_self_quota_preemption

        if self.enable_sub_quota_preemption is not None:
            result['EnableSubQuotaPreemption'] = self.enable_sub_quota_preemption

        if self.eni_cache_config is not None:
            result['EniCacheConfig'] = self.eni_cache_config.to_map()

        if self.oversold_usage_config is not None:
            result['OversoldUsageConfig'] = self.oversold_usage_config.to_map()

        result['ResourceSpecs'] = []
        if self.resource_specs is not None:
            for k1 in self.resource_specs:
                result['ResourceSpecs'].append(k1.to_map() if k1 else None)

        if self.sandbox_cache_config is not None:
            result['SandboxCacheConfig'] = self.sandbox_cache_config.to_map()

        if self.self_quota_preemption_config is not None:
            result['SelfQuotaPreemptionConfig'] = self.self_quota_preemption_config.to_map()

        if self.sub_quota_preemption_config is not None:
            result['SubQuotaPreemptionConfig'] = self.sub_quota_preemption_config.to_map()

        if self.support_gpudrivers is not None:
            result['SupportGPUDrivers'] = self.support_gpudrivers

        if self.support_rdma is not None:
            result['SupportRDMA'] = self.support_rdma

        if self.use_case is not None:
            result['UseCase'] = self.use_case

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

        if m.get('ControlPlaneClusterId') is not None:
            self.control_plane_cluster_id = m.get('ControlPlaneClusterId')

        if m.get('DefaultGPUDriver') is not None:
            self.default_gpudriver = m.get('DefaultGPUDriver')

        if m.get('EnableGPUShare') is not None:
            self.enable_gpushare = m.get('EnableGPUShare')

        if m.get('EnablePreemptSubquotaWorkloads') is not None:
            self.enable_preempt_subquota_workloads = m.get('EnablePreemptSubquotaWorkloads')

        if m.get('EnableSelfQuotaPreemption') is not None:
            self.enable_self_quota_preemption = m.get('EnableSelfQuotaPreemption')

        if m.get('EnableSubQuotaPreemption') is not None:
            self.enable_sub_quota_preemption = m.get('EnableSubQuotaPreemption')

        if m.get('EniCacheConfig') is not None:
            temp_model = main_models.EniCacheConfig()
            self.eni_cache_config = temp_model.from_map(m.get('EniCacheConfig'))

        if m.get('OversoldUsageConfig') is not None:
            temp_model = main_models.OversoldUsageConfig()
            self.oversold_usage_config = temp_model.from_map(m.get('OversoldUsageConfig'))

        self.resource_specs = []
        if m.get('ResourceSpecs') is not None:
            for k1 in m.get('ResourceSpecs'):
                temp_model = main_models.WorkspaceSpecs()
                self.resource_specs.append(temp_model.from_map(k1))

        if m.get('SandboxCacheConfig') is not None:
            temp_model = main_models.SandboxCacheConfig()
            self.sandbox_cache_config = temp_model.from_map(m.get('SandboxCacheConfig'))

        if m.get('SelfQuotaPreemptionConfig') is not None:
            temp_model = main_models.SelfQuotaPreemptionConfig()
            self.self_quota_preemption_config = temp_model.from_map(m.get('SelfQuotaPreemptionConfig'))

        if m.get('SubQuotaPreemptionConfig') is not None:
            temp_model = main_models.SubQuotaPreemptionConfig()
            self.sub_quota_preemption_config = temp_model.from_map(m.get('SubQuotaPreemptionConfig'))

        if m.get('SupportGPUDrivers') is not None:
            self.support_gpudrivers = m.get('SupportGPUDrivers')

        if m.get('SupportRDMA') is not None:
            self.support_rdma = m.get('SupportRDMA')

        if m.get('UseCase') is not None:
            self.use_case = m.get('UseCase')

        if m.get('UserVpc') is not None:
            temp_model = main_models.UserVpc()
            self.user_vpc = temp_model.from_map(m.get('UserVpc'))

        return self

