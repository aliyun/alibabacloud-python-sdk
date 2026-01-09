# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiccs20191015 import models as main_models
from darabonba.model import DaraModel

class ResetHotlineNumberRequest(DaraModel):
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
        outbound_range_list: List[main_models.ResetHotlineNumberRequestOutboundRangeList] = None,
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
        self.outbound_range_list = outbound_range_list

    def validate(self):
        if self.outbound_range_list:
            for v1 in self.outbound_range_list:
                 if v1:
                    v1.validate()

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

        result['OutboundRangeList'] = []
        if self.outbound_range_list is not None:
            for k1 in self.outbound_range_list:
                result['OutboundRangeList'].append(k1.to_map() if k1 else None)

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

        self.outbound_range_list = []
        if m.get('OutboundRangeList') is not None:
            for k1 in m.get('OutboundRangeList'):
                temp_model = main_models.ResetHotlineNumberRequestOutboundRangeList()
                self.outbound_range_list.append(temp_model.from_map(k1))

        return self

class ResetHotlineNumberRequestOutboundRangeList(DaraModel):
    def __init__(
        self,
        department_id: int = None,
        group_id_list: List[int] = None,
    ):
        self.department_id = department_id
        self.group_id_list = group_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.department_id is not None:
            result['DepartmentId'] = self.department_id

        if self.group_id_list is not None:
            result['GroupIdList'] = self.group_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')

        if m.get('GroupIdList') is not None:
            self.group_id_list = m.get('GroupIdList')

        return self

