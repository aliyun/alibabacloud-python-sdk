# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paistudio20220112 import models as main_models
from darabonba.model import DaraModel

class UpdateQuotaRequest(DaraModel):
    def __init__(
        self,
        cluster_spec: main_models.UpdateQuotaRequestClusterSpec = None,
        description: str = None,
        enable_graceful_upgrade: bool = None,
        graceful_upgrade_config: main_models.UpdateQuotaRequestGracefulUpgradeConfig = None,
        labels: List[main_models.Label] = None,
        propagate_default_gpudriver: bool = None,
        queue_strategy: str = None,
        quota_config: main_models.QuotaConfig = None,
        quota_name: str = None,
    ):
        # The configurations of the compute cluster bound to the quota (RNQ Ray cluster). This parameter is only available for RNQ quotas and will be rejected for common quotas. It can only be modified when no operations are in progress on the quota. Unpassed sub-fields retain the current effective configurations.
        self.cluster_spec = cluster_spec
        # The description of the resource quota.
        self.description = description
        # Specifies whether to execute the current ClusterSpec change as a rolling upgrade (draining and migrating nodes one by one to the new cluster) instead of the default stop-and-rebuild method.
        self.enable_graceful_upgrade = enable_graceful_upgrade
        # The tuning parameters for the migration process. This parameter is only allowed when EnableGracefulUpgrade is set to true.
        self.graceful_upgrade_config = graceful_upgrade_config
        # The list of user-defined labels.
        # This is a full update.
        self.labels = labels
        # Specifies whether to pass the default GPU driver configuration to child quotas.
        self.propagate_default_gpudriver = propagate_default_gpudriver
        # The queuing strategy for tasks on the quota.
        self.queue_strategy = queue_strategy
        # The resource quota configuration.
        self.quota_config = quota_config
        # The name of the resource quota.
        self.quota_name = quota_name

    def validate(self):
        if self.cluster_spec:
            self.cluster_spec.validate()
        if self.graceful_upgrade_config:
            self.graceful_upgrade_config.validate()
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()
        if self.quota_config:
            self.quota_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_spec is not None:
            result['ClusterSpec'] = self.cluster_spec.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.enable_graceful_upgrade is not None:
            result['EnableGracefulUpgrade'] = self.enable_graceful_upgrade

        if self.graceful_upgrade_config is not None:
            result['GracefulUpgradeConfig'] = self.graceful_upgrade_config.to_map()

        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        if self.propagate_default_gpudriver is not None:
            result['PropagateDefaultGPUDriver'] = self.propagate_default_gpudriver

        if self.queue_strategy is not None:
            result['QueueStrategy'] = self.queue_strategy

        if self.quota_config is not None:
            result['QuotaConfig'] = self.quota_config.to_map()

        if self.quota_name is not None:
            result['QuotaName'] = self.quota_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterSpec') is not None:
            temp_model = main_models.UpdateQuotaRequestClusterSpec()
            self.cluster_spec = temp_model.from_map(m.get('ClusterSpec'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnableGracefulUpgrade') is not None:
            self.enable_graceful_upgrade = m.get('EnableGracefulUpgrade')

        if m.get('GracefulUpgradeConfig') is not None:
            temp_model = main_models.UpdateQuotaRequestGracefulUpgradeConfig()
            self.graceful_upgrade_config = temp_model.from_map(m.get('GracefulUpgradeConfig'))

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.Label()
                self.labels.append(temp_model.from_map(k1))

        if m.get('PropagateDefaultGPUDriver') is not None:
            self.propagate_default_gpudriver = m.get('PropagateDefaultGPUDriver')

        if m.get('QueueStrategy') is not None:
            self.queue_strategy = m.get('QueueStrategy')

        if m.get('QuotaConfig') is not None:
            temp_model = main_models.QuotaConfig()
            self.quota_config = temp_model.from_map(m.get('QuotaConfig'))

        if m.get('QuotaName') is not None:
            self.quota_name = m.get('QuotaName')

        return self

class UpdateQuotaRequestGracefulUpgradeConfig(DaraModel):
    def __init__(
        self,
        drain_timeout_seconds: int = None,
        max_unavailable: str = None,
        task_drain_reserve_workers: int = None,
    ):
        # The timeout limit for Ray draining of a single node. After the timeout, the node is still directly scaled down, which does not cause the upgrade to fail.
        self.drain_timeout_seconds = drain_timeout_seconds
        # The migration window width, which is the maximum number of workers in the old cluster that are simultaneously in an unavailable state (draining or drained and pending removal), that is, the number of nodes migrated in parallel.
        self.max_unavailable = max_unavailable
        # The number of workers in the old cluster that are kept in a schedulable state while waiting for the remaining Ray tasks in the old cluster to complete.
        self.task_drain_reserve_workers = task_drain_reserve_workers

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.drain_timeout_seconds is not None:
            result['DrainTimeoutSeconds'] = self.drain_timeout_seconds

        if self.max_unavailable is not None:
            result['MaxUnavailable'] = self.max_unavailable

        if self.task_drain_reserve_workers is not None:
            result['TaskDrainReserveWorkers'] = self.task_drain_reserve_workers

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DrainTimeoutSeconds') is not None:
            self.drain_timeout_seconds = m.get('DrainTimeoutSeconds')

        if m.get('MaxUnavailable') is not None:
            self.max_unavailable = m.get('MaxUnavailable')

        if m.get('TaskDrainReserveWorkers') is not None:
            self.task_drain_reserve_workers = m.get('TaskDrainReserveWorkers')

        return self

class UpdateQuotaRequestClusterSpec(DaraModel):
    def __init__(
        self,
        cluster_type: str = None,
        data_sources: List[str] = None,
        image: str = None,
    ):
        # The cluster type. Currently, only RayCluster is supported.
        self.cluster_type = cluster_type
        # The list of data sources mounted to the cluster. This parameter uses the overall replacement semantics: if it is not passed, the current state is maintained; if an empty array is passed, the list is cleared. Each element is a JSON object string that contains DataSourceId or Uri (one of them is required and they are mutually exclusive) and an optional MountPath.
        self.data_sources = data_sources
        # The container image used by the Ray cluster. If this parameter is explicitly passed, the system switches to this image. If it is left empty and the data sources remain unchanged, and GetQuota returns UpgradeAvailable=true, this update is considered an upgrade to the platform default image. To keep the current image, explicitly pass the current value.
        self.image = image

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type

        if self.data_sources is not None:
            result['DataSources'] = self.data_sources

        if self.image is not None:
            result['Image'] = self.image

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')

        if m.get('DataSources') is not None:
            self.data_sources = m.get('DataSources')

        if m.get('Image') is not None:
            self.image = m.get('Image')

        return self

