# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLimitationResponseBody(DaraModel):
    def __init__(
        self,
        max_number_of_alb_server_group: int = None,
        max_number_of_dbinstances: int = None,
        max_number_of_lifecycle_hooks: int = None,
        max_number_of_load_balancers: int = None,
        max_number_of_max_size: int = None,
        max_number_of_min_size: int = None,
        max_number_of_nlb_server_group: int = None,
        max_number_of_notification_configurations: int = None,
        max_number_of_scaling_configurations: int = None,
        max_number_of_scaling_groups: int = None,
        max_number_of_scaling_instances: int = None,
        max_number_of_scaling_rules: int = None,
        max_number_of_scheduled_tasks: int = None,
        max_number_of_vserver_groups: int = None,
        request_id: str = None,
    ):
        # The maximum number of Application Load Balancer (ALB) server groups that can be attached to a scaling group.
        # 
        # >  To view the quota or request a quota increase, go to [Quota Center](https://quotas.console.aliyun.com/products/ess/quotas).
        self.max_number_of_alb_server_group = max_number_of_alb_server_group
        # The maximum number of ApsaraDB RDS instances that can be associated with a scaling group.
        # 
        # >  To view the quota or request a quota increase, go to [Quota Center](https://quotas.console.aliyun.com/products/ess/quotas).
        self.max_number_of_dbinstances = max_number_of_dbinstances
        # The maximum number of lifecycle hooks that can be created in a scaling group.
        self.max_number_of_lifecycle_hooks = max_number_of_lifecycle_hooks
        # The maximum number of Classic Load Balancer (CLB, formerly known as SLB) instances that can be associated with a scaling group.
        # 
        # >  To view the quota or request a quota increase, go to [Quota Center](https://quotas.console.aliyun.com/products/ess/quotas).
        self.max_number_of_load_balancers = max_number_of_load_balancers
        # The maximum number of instances that can be contained in a scaling group.
        # 
        # >  To view the quota or request a quota increase, go to [Quota Center](https://quotas.console.aliyun.com/products/ess/quotas).
        self.max_number_of_max_size = max_number_of_max_size
        # The minimum number of instances that must be contained in a scaling group. The value of `MaxNumberOfMinSize` must be consistent with the value of `MaxNumberOfMaxSize`.
        self.max_number_of_min_size = max_number_of_min_size
        # The maximum number of Network Load Balancer (NLB) server groups that can be attached to a scaling group.
        # 
        # >  To view the quota or request a quota increase, go to [Quota Center](https://quotas.console.aliyun.com/products/ess/quotas).
        self.max_number_of_nlb_server_group = max_number_of_nlb_server_group
        # The maximum number of notification rules that can be created in a scaling group.
        self.max_number_of_notification_configurations = max_number_of_notification_configurations
        # The maximum number of scaling configurations that can be created in a scaling group.
        # 
        # >  To view the quota or request a quota increase, go to [Quota Center](https://quotas.console.aliyun.com/products/ess/quotas).
        self.max_number_of_scaling_configurations = max_number_of_scaling_configurations
        # The maximum number of scaling groups that can be created in a region by using an Alibaba Cloud account.
        # 
        # >  To view the quota or request a quota increase, go to [Quota Center](https://quotas.console.aliyun.com/products/ess/quotas).
        self.max_number_of_scaling_groups = max_number_of_scaling_groups
        # The maximum number of Elastic Compute Service (ECS) instances or elastic container instances that can be automatically scaled in a scaling group at the same time.
        self.max_number_of_scaling_instances = max_number_of_scaling_instances
        # The maximum number of scaling rules that can be created in a scaling group.
        # 
        # >  To view the quota or request a quota increase, go to [Quota Center](https://quotas.console.aliyun.com/products/ess/quotas).
        self.max_number_of_scaling_rules = max_number_of_scaling_rules
        # The maximum number of scheduled tasks that can be created in a region by using an Alibaba Cloud account.
        # 
        # >  To view the quota or request a quota increase, go to [Quota Center](https://quotas.console.aliyun.com/products/ess/quotas).
        self.max_number_of_scheduled_tasks = max_number_of_scheduled_tasks
        # The maximum number of CLB vServer groups that can be attached to a scaling group.
        # 
        # >  To view the quota or request a quota increase, go to [Quota Center](https://quotas.console.aliyun.com/products/ess/quotas).
        self.max_number_of_vserver_groups = max_number_of_vserver_groups
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_number_of_alb_server_group is not None:
            result['MaxNumberOfAlbServerGroup'] = self.max_number_of_alb_server_group

        if self.max_number_of_dbinstances is not None:
            result['MaxNumberOfDBInstances'] = self.max_number_of_dbinstances

        if self.max_number_of_lifecycle_hooks is not None:
            result['MaxNumberOfLifecycleHooks'] = self.max_number_of_lifecycle_hooks

        if self.max_number_of_load_balancers is not None:
            result['MaxNumberOfLoadBalancers'] = self.max_number_of_load_balancers

        if self.max_number_of_max_size is not None:
            result['MaxNumberOfMaxSize'] = self.max_number_of_max_size

        if self.max_number_of_min_size is not None:
            result['MaxNumberOfMinSize'] = self.max_number_of_min_size

        if self.max_number_of_nlb_server_group is not None:
            result['MaxNumberOfNlbServerGroup'] = self.max_number_of_nlb_server_group

        if self.max_number_of_notification_configurations is not None:
            result['MaxNumberOfNotificationConfigurations'] = self.max_number_of_notification_configurations

        if self.max_number_of_scaling_configurations is not None:
            result['MaxNumberOfScalingConfigurations'] = self.max_number_of_scaling_configurations

        if self.max_number_of_scaling_groups is not None:
            result['MaxNumberOfScalingGroups'] = self.max_number_of_scaling_groups

        if self.max_number_of_scaling_instances is not None:
            result['MaxNumberOfScalingInstances'] = self.max_number_of_scaling_instances

        if self.max_number_of_scaling_rules is not None:
            result['MaxNumberOfScalingRules'] = self.max_number_of_scaling_rules

        if self.max_number_of_scheduled_tasks is not None:
            result['MaxNumberOfScheduledTasks'] = self.max_number_of_scheduled_tasks

        if self.max_number_of_vserver_groups is not None:
            result['MaxNumberOfVServerGroups'] = self.max_number_of_vserver_groups

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxNumberOfAlbServerGroup') is not None:
            self.max_number_of_alb_server_group = m.get('MaxNumberOfAlbServerGroup')

        if m.get('MaxNumberOfDBInstances') is not None:
            self.max_number_of_dbinstances = m.get('MaxNumberOfDBInstances')

        if m.get('MaxNumberOfLifecycleHooks') is not None:
            self.max_number_of_lifecycle_hooks = m.get('MaxNumberOfLifecycleHooks')

        if m.get('MaxNumberOfLoadBalancers') is not None:
            self.max_number_of_load_balancers = m.get('MaxNumberOfLoadBalancers')

        if m.get('MaxNumberOfMaxSize') is not None:
            self.max_number_of_max_size = m.get('MaxNumberOfMaxSize')

        if m.get('MaxNumberOfMinSize') is not None:
            self.max_number_of_min_size = m.get('MaxNumberOfMinSize')

        if m.get('MaxNumberOfNlbServerGroup') is not None:
            self.max_number_of_nlb_server_group = m.get('MaxNumberOfNlbServerGroup')

        if m.get('MaxNumberOfNotificationConfigurations') is not None:
            self.max_number_of_notification_configurations = m.get('MaxNumberOfNotificationConfigurations')

        if m.get('MaxNumberOfScalingConfigurations') is not None:
            self.max_number_of_scaling_configurations = m.get('MaxNumberOfScalingConfigurations')

        if m.get('MaxNumberOfScalingGroups') is not None:
            self.max_number_of_scaling_groups = m.get('MaxNumberOfScalingGroups')

        if m.get('MaxNumberOfScalingInstances') is not None:
            self.max_number_of_scaling_instances = m.get('MaxNumberOfScalingInstances')

        if m.get('MaxNumberOfScalingRules') is not None:
            self.max_number_of_scaling_rules = m.get('MaxNumberOfScalingRules')

        if m.get('MaxNumberOfScheduledTasks') is not None:
            self.max_number_of_scheduled_tasks = m.get('MaxNumberOfScheduledTasks')

        if m.get('MaxNumberOfVServerGroups') is not None:
            self.max_number_of_vserver_groups = m.get('MaxNumberOfVServerGroups')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

