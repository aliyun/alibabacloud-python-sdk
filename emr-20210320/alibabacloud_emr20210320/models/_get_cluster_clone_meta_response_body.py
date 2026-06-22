# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class GetClusterCloneMetaResponseBody(DaraModel):
    def __init__(
        self,
        cluster_clone_meta: main_models.GetClusterCloneMetaResponseBodyClusterCloneMeta = None,
        request_id: str = None,
    ):
        # The clone metadata of the cluster.
        self.cluster_clone_meta = cluster_clone_meta
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.cluster_clone_meta:
            self.cluster_clone_meta.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_clone_meta is not None:
            result['ClusterCloneMeta'] = self.cluster_clone_meta.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterCloneMeta') is not None:
            temp_model = main_models.GetClusterCloneMetaResponseBodyClusterCloneMeta()
            self.cluster_clone_meta = temp_model.from_map(m.get('ClusterCloneMeta'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetClusterCloneMetaResponseBodyClusterCloneMeta(DaraModel):
    def __init__(
        self,
        application_configs: List[main_models.ApplicationConfig] = None,
        applications: List[main_models.Application] = None,
        bootstrap_scripts: List[main_models.Script] = None,
        cluster_id: str = None,
        cluster_name: str = None,
        cluster_state: str = None,
        cluster_type: str = None,
        collation_time_zone: main_models.CollationTimeZone = None,
        deletion_protection: bool = None,
        deploy_mode: str = None,
        emr_default_role: str = None,
        exist_clone_config: bool = None,
        node_attributes: main_models.NodeAttributes = None,
        node_groups: List[main_models.NodeGroup] = None,
        payment_type: str = None,
        region_id: str = None,
        release_version: str = None,
        resource_group_id: str = None,
        scaling_policies: List[main_models.GetClusterCloneMetaResponseBodyClusterCloneMetaScalingPolicies] = None,
        security_mode: str = None,
        subscription_config: main_models.SubscriptionConfig = None,
        tags: List[main_models.Tag] = None,
    ):
        # The modified application configuration items.
        self.application_configs = application_configs
        # The cluster applications.
        self.applications = applications
        # An array of bootstrap scripts. The number of array elements N can be from 1 to 10.
        self.bootstrap_scripts = bootstrap_scripts
        # The cluster ID.
        self.cluster_id = cluster_id
        # The cluster name.
        self.cluster_name = cluster_name
        # The state of the cluster. Valid values:
        # 
        # - STARTING: The cluster is starting.
        # 
        # - START_FAILED: The cluster failed to start.
        # 
        # - BOOTSTRAPPING: The cluster is performing bootstrap actions.
        # 
        # - RUNNING: The cluster is running.
        # 
        # - TERMINATING: The cluster is being terminated.
        # 
        # - TERMINATED: The cluster is terminated.
        # 
        # - TERMINATED_WITH_ERRORS: The cluster is terminated due to an exception.
        # 
        # - TERMINATE_FAILED: The cluster failed to be terminated.
        self.cluster_state = cluster_state
        # The type of the cluster. Valid values:
        # 
        # - DATALAKE: data lake.
        # 
        # - OLAP: data analytics.
        # 
        # - DATAFLOW: real-time data stream.
        # 
        # - DATASERVING: data service.
        # 
        # - CUSTOM: custom cluster.
        # 
        # - HADOOP: Hadoop.
        self.cluster_type = cluster_type
        self.collation_time_zone = collation_time_zone
        # Indicates whether deletion protection is enabled for the cluster. Valid values:
        # 
        # - true: Deletion protection is enabled.
        # 
        # - false: Deletion protection is disabled.
        # 
        # Default value: false.
        self.deletion_protection = deletion_protection
        # The deployment mode of applications in the cluster. Valid values:
        # 
        # - NORMAL: standard deployment.
        # 
        # - HA: high-availability deployment.
        self.deploy_mode = deploy_mode
        # The EMR server role.
        self.emr_default_role = emr_default_role
        # Indicates whether the application configurations can be passed in when you clone a HADOOP cluster. Valid values:
        # 
        # - False: Not supported.
        # 
        # - True: Supported.
        self.exist_clone_config = exist_clone_config
        # The node attributes.
        self.node_attributes = node_attributes
        # An array of node group configurations. The number of array elements N can be from 1 to 100.
        self.node_groups = node_groups
        # The billing method. Valid values:
        # 
        # - PayAsYouGo: pay-as-you-go.
        # 
        # - Subscription: subscription.
        self.payment_type = payment_type
        # The region ID.
        self.region_id = region_id
        # The EMR release.
        self.release_version = release_version
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The Auto Scaling policies for each node group in the cluster.
        self.scaling_policies = scaling_policies
        # The Kerberos security mode of the cluster. Valid values:
        # 
        # - NORMAL: The Kerberos mode is disabled.
        # 
        # - KERBEROS: The Kerberos mode is enabled.
        self.security_mode = security_mode
        # The subscription configuration.
        self.subscription_config = subscription_config
        # The list of cluster tags.
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
        if self.collation_time_zone:
            self.collation_time_zone.validate()
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

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.cluster_state is not None:
            result['ClusterState'] = self.cluster_state

        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type

        if self.collation_time_zone is not None:
            result['CollationTimeZone'] = self.collation_time_zone.to_map()

        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection

        if self.deploy_mode is not None:
            result['DeployMode'] = self.deploy_mode

        if self.emr_default_role is not None:
            result['EmrDefaultRole'] = self.emr_default_role

        if self.exist_clone_config is not None:
            result['ExistCloneConfig'] = self.exist_clone_config

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

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('ClusterState') is not None:
            self.cluster_state = m.get('ClusterState')

        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')

        if m.get('CollationTimeZone') is not None:
            temp_model = main_models.CollationTimeZone()
            self.collation_time_zone = temp_model.from_map(m.get('CollationTimeZone'))

        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')

        if m.get('DeployMode') is not None:
            self.deploy_mode = m.get('DeployMode')

        if m.get('EmrDefaultRole') is not None:
            self.emr_default_role = m.get('EmrDefaultRole')

        if m.get('ExistCloneConfig') is not None:
            self.exist_clone_config = m.get('ExistCloneConfig')

        if m.get('NodeAttributes') is not None:
            temp_model = main_models.NodeAttributes()
            self.node_attributes = temp_model.from_map(m.get('NodeAttributes'))

        self.node_groups = []
        if m.get('NodeGroups') is not None:
            for k1 in m.get('NodeGroups'):
                temp_model = main_models.NodeGroup()
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
                temp_model = main_models.GetClusterCloneMetaResponseBodyClusterCloneMetaScalingPolicies()
                self.scaling_policies.append(temp_model.from_map(k1))

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

class GetClusterCloneMetaResponseBodyClusterCloneMetaScalingPolicies(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        constraints: main_models.GetClusterCloneMetaResponseBodyClusterCloneMetaScalingPoliciesConstraints = None,
        node_group_id: str = None,
        node_group_name: str = None,
        scaling_policy_id: str = None,
        scaling_policy_type: str = None,
        scaling_rules: List[main_models.GetClusterCloneMetaResponseBodyClusterCloneMetaScalingPoliciesScalingRules] = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # The constraints on the maximum and minimum number of nodes in the node group.
        self.constraints = constraints
        # The node group ID.
        self.node_group_id = node_group_id
        # The node group name.
        self.node_group_name = node_group_name
        # The scaling policy ID.
        self.scaling_policy_id = scaling_policy_id
        # The type of the elastic policy.
        self.scaling_policy_type = scaling_policy_type
        # The list of scaling rules.
        self.scaling_rules = scaling_rules

    def validate(self):
        if self.constraints:
            self.constraints.validate()
        if self.scaling_rules:
            for v1 in self.scaling_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.constraints is not None:
            result['Constraints'] = self.constraints.to_map()

        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id

        if self.node_group_name is not None:
            result['NodeGroupName'] = self.node_group_name

        if self.scaling_policy_id is not None:
            result['ScalingPolicyId'] = self.scaling_policy_id

        if self.scaling_policy_type is not None:
            result['ScalingPolicyType'] = self.scaling_policy_type

        result['ScalingRules'] = []
        if self.scaling_rules is not None:
            for k1 in self.scaling_rules:
                result['ScalingRules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Constraints') is not None:
            temp_model = main_models.GetClusterCloneMetaResponseBodyClusterCloneMetaScalingPoliciesConstraints()
            self.constraints = temp_model.from_map(m.get('Constraints'))

        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')

        if m.get('NodeGroupName') is not None:
            self.node_group_name = m.get('NodeGroupName')

        if m.get('ScalingPolicyId') is not None:
            self.scaling_policy_id = m.get('ScalingPolicyId')

        if m.get('ScalingPolicyType') is not None:
            self.scaling_policy_type = m.get('ScalingPolicyType')

        self.scaling_rules = []
        if m.get('ScalingRules') is not None:
            for k1 in m.get('ScalingRules'):
                temp_model = main_models.GetClusterCloneMetaResponseBodyClusterCloneMetaScalingPoliciesScalingRules()
                self.scaling_rules.append(temp_model.from_map(k1))

        return self

class GetClusterCloneMetaResponseBodyClusterCloneMetaScalingPoliciesScalingRules(DaraModel):
    def __init__(
        self,
        activity_type: str = None,
        adjustment_value: int = None,
        metrics_trigger: main_models.MetricsTrigger = None,
        rule_name: str = None,
        time_trigger: main_models.TimeTrigger = None,
        trigger_type: str = None,
    ):
        # The type of the scaling activity. This parameter is required. Valid values:
        # 
        # - SCALE_OUT: scale-out.
        # 
        # - SCALE_IN: scale-in.
        self.activity_type = activity_type
        # The adjustment value. This parameter is required. It must be a positive integer. It specifies the number of instances to add or remove.
        self.adjustment_value = adjustment_value
        # The description of the metric-based scaling rule.
        self.metrics_trigger = metrics_trigger
        # The name of the scaling rule.
        self.rule_name = rule_name
        # The description of the time-based scaling rule.
        self.time_trigger = time_trigger
        # The type of the scaling rule. This parameter is required. Valid values:
        # 
        # - TIME_TRIGGER: time-based scaling.
        # 
        # - METRICS_TRIGGER: metric-based scaling.
        self.trigger_type = trigger_type

    def validate(self):
        if self.metrics_trigger:
            self.metrics_trigger.validate()
        if self.time_trigger:
            self.time_trigger.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activity_type is not None:
            result['ActivityType'] = self.activity_type

        if self.adjustment_value is not None:
            result['AdjustmentValue'] = self.adjustment_value

        if self.metrics_trigger is not None:
            result['MetricsTrigger'] = self.metrics_trigger.to_map()

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.time_trigger is not None:
            result['TimeTrigger'] = self.time_trigger.to_map()

        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityType') is not None:
            self.activity_type = m.get('ActivityType')

        if m.get('AdjustmentValue') is not None:
            self.adjustment_value = m.get('AdjustmentValue')

        if m.get('MetricsTrigger') is not None:
            temp_model = main_models.MetricsTrigger()
            self.metrics_trigger = temp_model.from_map(m.get('MetricsTrigger'))

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('TimeTrigger') is not None:
            temp_model = main_models.TimeTrigger()
            self.time_trigger = temp_model.from_map(m.get('TimeTrigger'))

        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')

        return self

class GetClusterCloneMetaResponseBodyClusterCloneMetaScalingPoliciesConstraints(DaraModel):
    def __init__(
        self,
        max_capacity: int = None,
        max_on_demand_capacity: int = None,
        min_capacity: int = None,
    ):
        # The maximum number of nodes in the node group. Default value: 2000.
        self.max_capacity = max_capacity
        # The maximum number of pay-as-you-go instances.
        self.max_on_demand_capacity = max_on_demand_capacity
        # The minimum number of nodes in the node group. Default value: 0.
        self.min_capacity = min_capacity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_capacity is not None:
            result['MaxCapacity'] = self.max_capacity

        if self.max_on_demand_capacity is not None:
            result['MaxOnDemandCapacity'] = self.max_on_demand_capacity

        if self.min_capacity is not None:
            result['MinCapacity'] = self.min_capacity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxCapacity') is not None:
            self.max_capacity = m.get('MaxCapacity')

        if m.get('MaxOnDemandCapacity') is not None:
            self.max_on_demand_capacity = m.get('MaxOnDemandCapacity')

        if m.get('MinCapacity') is not None:
            self.min_capacity = m.get('MinCapacity')

        return self

