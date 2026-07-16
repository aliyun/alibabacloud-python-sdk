# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class RunApplicationActionRequest(DaraModel):
    def __init__(
        self,
        action_name: str = None,
        batch_size: int = None,
        cluster_id: str = None,
        component_instance_selector: main_models.ComponentInstanceSelector = None,
        description: str = None,
        execute_strategy: str = None,
        interval: int = None,
        region_id: str = None,
        rolling_execute: bool = None,
    ):
        # The name of the action. Valid values:
        # 
        # - start
        # 
        # - stop
        # 
        # - config
        # 
        # - restart
        # 
        # - refresh_queues
        # 
        # - refresh_labels
        # 
        # This parameter is required.
        self.action_name = action_name
        # The number of applications in each batch.
        self.batch_size = batch_size
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The operation object.
        # 
        # This parameter is required.
        self.component_instance_selector = component_instance_selector
        # The description of the execution.
        self.description = description
        # The execution policy. Valid values:
        # 
        # - FAILED_BLOCK: The system stops the execution if the execution fails.
        # 
        # - FAILED_CONTINUE: The system continues the execution if the execution fails.
        self.execute_strategy = execute_strategy
        # The interval for rolling execution. Unit: seconds.
        self.interval = interval
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Specifies whether to enable rolling execution.
        self.rolling_execute = rolling_execute

    def validate(self):
        if self.component_instance_selector:
            self.component_instance_selector.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_name is not None:
            result['ActionName'] = self.action_name

        if self.batch_size is not None:
            result['BatchSize'] = self.batch_size

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.component_instance_selector is not None:
            result['ComponentInstanceSelector'] = self.component_instance_selector.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.execute_strategy is not None:
            result['ExecuteStrategy'] = self.execute_strategy

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.rolling_execute is not None:
            result['RollingExecute'] = self.rolling_execute

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionName') is not None:
            self.action_name = m.get('ActionName')

        if m.get('BatchSize') is not None:
            self.batch_size = m.get('BatchSize')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ComponentInstanceSelector') is not None:
            temp_model = main_models.ComponentInstanceSelector()
            self.component_instance_selector = temp_model.from_map(m.get('ComponentInstanceSelector'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExecuteStrategy') is not None:
            self.execute_strategy = m.get('ExecuteStrategy')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RollingExecute') is not None:
            self.rolling_execute = m.get('RollingExecute')

        return self

