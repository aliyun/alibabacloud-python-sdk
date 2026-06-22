# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class DRPlanConfigurationDetail(DaraModel):
    def __init__(
        self,
        application_configs: List[main_models.ApplicationConfig] = None,
        applications: List[main_models.Application] = None,
        bootstrap_scripts: List[main_models.Script] = None,
        cluster_name: str = None,
        cluster_type: str = None,
        deletion_protection: bool = None,
        deploy_mode: str = None,
        description: str = None,
        log_collect_strategy: str = None,
        managed_scaling_policy: main_models.DRPlanConfigurationDetailManagedScalingPolicy = None,
        meta_store_type: str = None,
        node_attributes: main_models.NodeAttributes = None,
        node_groups: List[main_models.NodeGroupConfig] = None,
        payment_type: str = None,
        region_id: str = None,
        release_version: str = None,
        resource_group_id: str = None,
        scaling_policies: List[main_models.ScalingPolicy] = None,
        scaling_time_zone: str = None,
        security_mode: str = None,
        subscription_config: main_models.SubscriptionConfig = None,
        tags: List[main_models.Tag] = None,
    ):
        self.application_configs = application_configs
        self.applications = applications
        self.bootstrap_scripts = bootstrap_scripts
        self.cluster_name = cluster_name
        # This parameter is required.
        self.cluster_type = cluster_type
        self.deletion_protection = deletion_protection
        # This parameter is required.
        self.deploy_mode = deploy_mode
        self.description = description
        # This parameter is required.
        self.log_collect_strategy = log_collect_strategy
        self.managed_scaling_policy = managed_scaling_policy
        # This parameter is required.
        self.meta_store_type = meta_store_type
        # This parameter is required.
        self.node_attributes = node_attributes
        self.node_groups = node_groups
        # This parameter is required.
        self.payment_type = payment_type
        # This parameter is required.
        self.region_id = region_id
        # This parameter is required.
        self.release_version = release_version
        self.resource_group_id = resource_group_id
        self.scaling_policies = scaling_policies
        self.scaling_time_zone = scaling_time_zone
        # This parameter is required.
        self.security_mode = security_mode
        self.subscription_config = subscription_config
        self.tags = tags

    def validate(self):
        if self.application_configs:
            for v1 in self.application_configs:
                 if v1:
                    v1.validate()
        if self.applications:
            for v1 in self.applications:
                 if v1:
                    v1.validate()
        if self.bootstrap_scripts:
            for v1 in self.bootstrap_scripts:
                 if v1:
                    v1.validate()
        if self.managed_scaling_policy:
            self.managed_scaling_policy.validate()
        if self.node_attributes:
            self.node_attributes.validate()
        if self.node_groups:
            for v1 in self.node_groups:
                 if v1:
                    v1.validate()
        if self.scaling_policies:
            for v1 in self.scaling_policies:
                 if v1:
                    v1.validate()
        if self.subscription_config:
            self.subscription_config.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ApplicationConfigs'] = []
        if self.application_configs is not None:
            for k1 in self.application_configs:
                result['ApplicationConfigs'].append(k1.to_map() if k1 else None)

        result['Applications'] = []
        if self.applications is not None:
            for k1 in self.applications:
                result['Applications'].append(k1.to_map() if k1 else None)

        result['BootstrapScripts'] = []
        if self.bootstrap_scripts is not None:
            for k1 in self.bootstrap_scripts:
                result['BootstrapScripts'].append(k1.to_map() if k1 else None)

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type

        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection

        if self.deploy_mode is not None:
            result['DeployMode'] = self.deploy_mode

        if self.description is not None:
            result['Description'] = self.description

        if self.log_collect_strategy is not None:
            result['LogCollectStrategy'] = self.log_collect_strategy

        if self.managed_scaling_policy is not None:
            result['ManagedScalingPolicy'] = self.managed_scaling_policy.to_map()

        if self.meta_store_type is not None:
            result['MetaStoreType'] = self.meta_store_type

        if self.node_attributes is not None:
            result['NodeAttributes'] = self.node_attributes.to_map()

        result['NodeGroups'] = []
        if self.node_groups is not None:
            for k1 in self.node_groups:
                result['NodeGroups'].append(k1.to_map() if k1 else None)

        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.release_version is not None:
            result['ReleaseVersion'] = self.release_version

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['ScalingPolicies'] = []
        if self.scaling_policies is not None:
            for k1 in self.scaling_policies:
                result['ScalingPolicies'].append(k1.to_map() if k1 else None)

        if self.scaling_time_zone is not None:
            result['ScalingTimeZone'] = self.scaling_time_zone

        if self.security_mode is not None:
            result['SecurityMode'] = self.security_mode

        if self.subscription_config is not None:
            result['SubscriptionConfig'] = self.subscription_config.to_map()

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.application_configs = []
        if m.get('ApplicationConfigs') is not None:
            for k1 in m.get('ApplicationConfigs'):
                temp_model = main_models.ApplicationConfig()
                self.application_configs.append(temp_model.from_map(k1))

        self.applications = []
        if m.get('Applications') is not None:
            for k1 in m.get('Applications'):
                temp_model = main_models.Application()
                self.applications.append(temp_model.from_map(k1))

        self.bootstrap_scripts = []
        if m.get('BootstrapScripts') is not None:
            for k1 in m.get('BootstrapScripts'):
                temp_model = main_models.Script()
                self.bootstrap_scripts.append(temp_model.from_map(k1))

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')

        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')

        if m.get('DeployMode') is not None:
            self.deploy_mode = m.get('DeployMode')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('LogCollectStrategy') is not None:
            self.log_collect_strategy = m.get('LogCollectStrategy')

        if m.get('ManagedScalingPolicy') is not None:
            temp_model = main_models.DRPlanConfigurationDetailManagedScalingPolicy()
            self.managed_scaling_policy = temp_model.from_map(m.get('ManagedScalingPolicy'))

        if m.get('MetaStoreType') is not None:
            self.meta_store_type = m.get('MetaStoreType')

        if m.get('NodeAttributes') is not None:
            temp_model = main_models.NodeAttributes()
            self.node_attributes = temp_model.from_map(m.get('NodeAttributes'))

        self.node_groups = []
        if m.get('NodeGroups') is not None:
            for k1 in m.get('NodeGroups'):
                temp_model = main_models.NodeGroupConfig()
                self.node_groups.append(temp_model.from_map(k1))

        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReleaseVersion') is not None:
            self.release_version = m.get('ReleaseVersion')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.scaling_policies = []
        if m.get('ScalingPolicies') is not None:
            for k1 in m.get('ScalingPolicies'):
                temp_model = main_models.ScalingPolicy()
                self.scaling_policies.append(temp_model.from_map(k1))

        if m.get('ScalingTimeZone') is not None:
            self.scaling_time_zone = m.get('ScalingTimeZone')

        if m.get('SecurityMode') is not None:
            self.security_mode = m.get('SecurityMode')

        if m.get('SubscriptionConfig') is not None:
            temp_model = main_models.SubscriptionConfig()
            self.subscription_config = temp_model.from_map(m.get('SubscriptionConfig'))

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.Tag()
                self.tags.append(temp_model.from_map(k1))

        return self

class DRPlanConfigurationDetailManagedScalingPolicy(DaraModel):
    def __init__(
        self,
        constraints: main_models.ManagedScalingConstraints = None,
    ):
        self.constraints = constraints

    def validate(self):
        if self.constraints:
            self.constraints.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.constraints is not None:
            result['Constraints'] = self.constraints.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Constraints') is not None:
            temp_model = main_models.ManagedScalingConstraints()
            self.constraints = temp_model.from_map(m.get('Constraints'))

        return self

