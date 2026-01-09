# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResetHotlineNumberShrinkRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        enable_inbound: bool = None,
        enable_inbound_evaluation: bool = None,
        enable_outbound: bool = None,
        enable_outbound_evaluation: bool = None,
        evaluation_level: int = None,
        hotline_number: str = None,
        inbound_flow_id: int = None,
        instance_id: str = None,
        outbound_all_depart: bool = None,
        outbound_range_list_shrink: str = None,
    ):
        # This parameter is required.
        self.description = description
        # This parameter is required.
        self.enable_inbound = enable_inbound
        # This parameter is required.
        self.enable_inbound_evaluation = enable_inbound_evaluation
        # This parameter is required.
        self.enable_outbound = enable_outbound
        # This parameter is required.
        self.enable_outbound_evaluation = enable_outbound_evaluation
        self.evaluation_level = evaluation_level
        # This parameter is required.
        self.hotline_number = hotline_number
        self.inbound_flow_id = inbound_flow_id
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.outbound_all_depart = outbound_all_depart
        self.outbound_range_list_shrink = outbound_range_list_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.enable_inbound is not None:
            result['EnableInbound'] = self.enable_inbound

        if self.enable_inbound_evaluation is not None:
            result['EnableInboundEvaluation'] = self.enable_inbound_evaluation

        if self.enable_outbound is not None:
            result['EnableOutbound'] = self.enable_outbound

        if self.enable_outbound_evaluation is not None:
            result['EnableOutboundEvaluation'] = self.enable_outbound_evaluation

        if self.evaluation_level is not None:
            result['EvaluationLevel'] = self.evaluation_level

        if self.hotline_number is not None:
            result['HotlineNumber'] = self.hotline_number

        if self.inbound_flow_id is not None:
            result['InboundFlowId'] = self.inbound_flow_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.outbound_all_depart is not None:
            result['OutboundAllDepart'] = self.outbound_all_depart

        if self.outbound_range_list_shrink is not None:
            result['OutboundRangeList'] = self.outbound_range_list_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnableInbound') is not None:
            self.enable_inbound = m.get('EnableInbound')

        if m.get('EnableInboundEvaluation') is not None:
            self.enable_inbound_evaluation = m.get('EnableInboundEvaluation')

        if m.get('EnableOutbound') is not None:
            self.enable_outbound = m.get('EnableOutbound')

        if m.get('EnableOutboundEvaluation') is not None:
            self.enable_outbound_evaluation = m.get('EnableOutboundEvaluation')

        if m.get('EvaluationLevel') is not None:
            self.evaluation_level = m.get('EvaluationLevel')

        if m.get('HotlineNumber') is not None:
            self.hotline_number = m.get('HotlineNumber')

        if m.get('InboundFlowId') is not None:
            self.inbound_flow_id = m.get('InboundFlowId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OutboundAllDepart') is not None:
            self.outbound_all_depart = m.get('OutboundAllDepart')

        if m.get('OutboundRangeList') is not None:
            self.outbound_range_list_shrink = m.get('OutboundRangeList')

        return self

