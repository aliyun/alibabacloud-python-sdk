# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateBaselineShrinkRequest(DaraModel):
    def __init__(
        self,
        alert_enabled: bool = None,
        alert_margin_threshold: int = None,
        alert_settings_shrink: str = None,
        baseline_id: int = None,
        baseline_name: str = None,
        baseline_type: str = None,
        enabled: bool = None,
        node_ids: str = None,
        overtime_settings_shrink: str = None,
        owner: str = None,
        priority: int = None,
        project_id: int = None,
        remove_node_ids: str = None,
    ):
        # Specifies whether to enable the alerting feature. Valid values: true and false.
        self.alert_enabled = alert_enabled
        # The alert margin threshold of the baseline. Unit: minutes.
        self.alert_margin_threshold = alert_margin_threshold
        # The alert settings of the baseline.
        self.alert_settings_shrink = alert_settings_shrink
        # The baseline ID. You can call the [ListBaselines](https://help.aliyun.com/document_detail/2261507.html) operation to query the ID.
        # 
        # This parameter is required.
        self.baseline_id = baseline_id
        # The name of the baseline.
        self.baseline_name = baseline_name
        # The type of the baseline. Valid values: DAILY and HOURLY.
        self.baseline_type = baseline_type
        # Specifies whether to enable the baseline. Valid values: true and false.
        self.enabled = enabled
        # The ancestor nodes of nodes in the baseline. Separate the ancestor nodes with commas (,). If a large number of ancestor nodes exist, we recommend that you create a zero load node and configure the zero load node as the descendant node of nodes in the baseline to facilitate node management.
        self.node_ids = node_ids
        # The settings of the committed completion time of the baseline.
        self.overtime_settings_shrink = overtime_settings_shrink
        # The ID of the Alibaba Cloud account used by the baseline owner.
        self.owner = owner
        # The priority of the baseline. Valid values: {1,3,5,7,8}.
        self.priority = priority
        # The workspace ID. You can call the [ListBaselines](https://help.aliyun.com/document_detail/2261507.html) operation to query the ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The ID of the node that you want to disassociate from the baseline. You can specify multiple node IDs. Separate multiple node IDs with commas (,).
        self.remove_node_ids = remove_node_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_enabled is not None:
            result['AlertEnabled'] = self.alert_enabled

        if self.alert_margin_threshold is not None:
            result['AlertMarginThreshold'] = self.alert_margin_threshold

        if self.alert_settings_shrink is not None:
            result['AlertSettings'] = self.alert_settings_shrink

        if self.baseline_id is not None:
            result['BaselineId'] = self.baseline_id

        if self.baseline_name is not None:
            result['BaselineName'] = self.baseline_name

        if self.baseline_type is not None:
            result['BaselineType'] = self.baseline_type

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.node_ids is not None:
            result['NodeIds'] = self.node_ids

        if self.overtime_settings_shrink is not None:
            result['OvertimeSettings'] = self.overtime_settings_shrink

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.remove_node_ids is not None:
            result['RemoveNodeIds'] = self.remove_node_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertEnabled') is not None:
            self.alert_enabled = m.get('AlertEnabled')

        if m.get('AlertMarginThreshold') is not None:
            self.alert_margin_threshold = m.get('AlertMarginThreshold')

        if m.get('AlertSettings') is not None:
            self.alert_settings_shrink = m.get('AlertSettings')

        if m.get('BaselineId') is not None:
            self.baseline_id = m.get('BaselineId')

        if m.get('BaselineName') is not None:
            self.baseline_name = m.get('BaselineName')

        if m.get('BaselineType') is not None:
            self.baseline_type = m.get('BaselineType')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('NodeIds') is not None:
            self.node_ids = m.get('NodeIds')

        if m.get('OvertimeSettings') is not None:
            self.overtime_settings_shrink = m.get('OvertimeSettings')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RemoveNodeIds') is not None:
            self.remove_node_ids = m.get('RemoveNodeIds')

        return self

