# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateOrUpdateSwimmingLaneShrinkRequest(DaraModel):
    def __init__(
        self,
        app_entry_rule_shrink: str = None,
        canary_model: int = None,
        enable: bool = None,
        group_id: int = None,
        lane_id: int = None,
        lane_name: str = None,
        lane_tag: str = None,
        mse_gateway_entry_rule_shrink: str = None,
        namespace_id: str = None,
    ):
        # The route configuration of the gateway.
        # 
        # >  This parameter is required if the gateway entry of the lane group is Java.
        self.app_entry_rule_shrink = app_entry_rule_shrink
        # Full-link Grayscale Mode:
        # 
        # *   0: The request is routed based on the content of the request.
        # *   1: routing based on percentages
        self.canary_model = canary_model
        # Lane Status
        # 
        # *   true: enabled
        # *   false: disabled
        self.enable = enable
        # The ID of the lane group to which the lane belongs.
        self.group_id = group_id
        # The ID of the lane.
        self.lane_id = lane_id
        # The name of the lane.
        self.lane_name = lane_name
        # The tag of the lane.
        self.lane_tag = lane_tag
        # The route configuration of the MSE gateway.
        # 
        # >  If the **EntryAppType** is set to **apig** or **mse-gw**, it is required.
        self.mse_gateway_entry_rule_shrink = mse_gateway_entry_rule_shrink
        # The namespace ID.
        self.namespace_id = namespace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_entry_rule_shrink is not None:
            result['AppEntryRule'] = self.app_entry_rule_shrink

        if self.canary_model is not None:
            result['CanaryModel'] = self.canary_model

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.lane_id is not None:
            result['LaneId'] = self.lane_id

        if self.lane_name is not None:
            result['LaneName'] = self.lane_name

        if self.lane_tag is not None:
            result['LaneTag'] = self.lane_tag

        if self.mse_gateway_entry_rule_shrink is not None:
            result['MseGatewayEntryRule'] = self.mse_gateway_entry_rule_shrink

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppEntryRule') is not None:
            self.app_entry_rule_shrink = m.get('AppEntryRule')

        if m.get('CanaryModel') is not None:
            self.canary_model = m.get('CanaryModel')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('LaneId') is not None:
            self.lane_id = m.get('LaneId')

        if m.get('LaneName') is not None:
            self.lane_name = m.get('LaneName')

        if m.get('LaneTag') is not None:
            self.lane_tag = m.get('LaneTag')

        if m.get('MseGatewayEntryRule') is not None:
            self.mse_gateway_entry_rule_shrink = m.get('MseGatewayEntryRule')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        return self

