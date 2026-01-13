# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_pairecservice20221213 import models as main_models
from darabonba.model import DaraModel

class QueryTrafficControlTargetItemReportDetailResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        traffic_control_target_item_report_detail: main_models.QueryTrafficControlTargetItemReportDetailResponseBodyTrafficControlTargetItemReportDetail = None,
    ):
        self.request_id = request_id
        self.traffic_control_target_item_report_detail = traffic_control_target_item_report_detail

    def validate(self):
        if self.traffic_control_target_item_report_detail:
            self.traffic_control_target_item_report_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.traffic_control_target_item_report_detail is not None:
            result['TrafficControlTargetItemReportDetail'] = self.traffic_control_target_item_report_detail.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TrafficControlTargetItemReportDetail') is not None:
            temp_model = main_models.QueryTrafficControlTargetItemReportDetailResponseBodyTrafficControlTargetItemReportDetail()
            self.traffic_control_target_item_report_detail = temp_model.from_map(m.get('TrafficControlTargetItemReportDetail'))

        return self

class QueryTrafficControlTargetItemReportDetailResponseBodyTrafficControlTargetItemReportDetail(DaraModel):
    def __init__(
        self,
        item_control_tail_report_details: List[main_models.QueryTrafficControlTargetItemReportDetailResponseBodyTrafficControlTargetItemReportDetailItemControlTailReportDetails] = None,
        item_control_top_report_details: List[main_models.QueryTrafficControlTargetItemReportDetailResponseBodyTrafficControlTargetItemReportDetailItemControlTopReportDetails] = None,
    ):
        self.item_control_tail_report_details = item_control_tail_report_details
        self.item_control_top_report_details = item_control_top_report_details

    def validate(self):
        if self.item_control_tail_report_details:
            for v1 in self.item_control_tail_report_details:
                 if v1:
                    v1.validate()
        if self.item_control_top_report_details:
            for v1 in self.item_control_top_report_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ItemControlTailReportDetails'] = []
        if self.item_control_tail_report_details is not None:
            for k1 in self.item_control_tail_report_details:
                result['ItemControlTailReportDetails'].append(k1.to_map() if k1 else None)

        result['ItemControlTopReportDetails'] = []
        if self.item_control_top_report_details is not None:
            for k1 in self.item_control_top_report_details:
                result['ItemControlTopReportDetails'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.item_control_tail_report_details = []
        if m.get('ItemControlTailReportDetails') is not None:
            for k1 in m.get('ItemControlTailReportDetails'):
                temp_model = main_models.QueryTrafficControlTargetItemReportDetailResponseBodyTrafficControlTargetItemReportDetailItemControlTailReportDetails()
                self.item_control_tail_report_details.append(temp_model.from_map(k1))

        self.item_control_top_report_details = []
        if m.get('ItemControlTopReportDetails') is not None:
            for k1 in m.get('ItemControlTopReportDetails'):
                temp_model = main_models.QueryTrafficControlTargetItemReportDetailResponseBodyTrafficControlTargetItemReportDetailItemControlTopReportDetails()
                self.item_control_top_report_details.append(temp_model.from_map(k1))

        return self

class QueryTrafficControlTargetItemReportDetailResponseBodyTrafficControlTargetItemReportDetailItemControlTopReportDetails(DaraModel):
    def __init__(
        self,
        features: Dict[str, Any] = None,
        item_id: str = None,
        target_progress: str = None,
        target_traffic: int = None,
    ):
        self.features = features
        self.item_id = item_id
        self.target_progress = target_progress
        self.target_traffic = target_traffic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.features is not None:
            result['Features'] = self.features

        if self.item_id is not None:
            result['ItemId'] = self.item_id

        if self.target_progress is not None:
            result['TargetProgress'] = self.target_progress

        if self.target_traffic is not None:
            result['TargetTraffic'] = self.target_traffic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Features') is not None:
            self.features = m.get('Features')

        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')

        if m.get('TargetProgress') is not None:
            self.target_progress = m.get('TargetProgress')

        if m.get('TargetTraffic') is not None:
            self.target_traffic = m.get('TargetTraffic')

        return self

class QueryTrafficControlTargetItemReportDetailResponseBodyTrafficControlTargetItemReportDetailItemControlTailReportDetails(DaraModel):
    def __init__(
        self,
        features: Dict[str, Any] = None,
        item_id: str = None,
        target_progress: str = None,
        target_traffic: int = None,
    ):
        self.features = features
        self.item_id = item_id
        self.target_progress = target_progress
        self.target_traffic = target_traffic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.features is not None:
            result['Features'] = self.features

        if self.item_id is not None:
            result['ItemId'] = self.item_id

        if self.target_progress is not None:
            result['TargetProgress'] = self.target_progress

        if self.target_traffic is not None:
            result['TargetTraffic'] = self.target_traffic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Features') is not None:
            self.features = m.get('Features')

        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')

        if m.get('TargetProgress') is not None:
            self.target_progress = m.get('TargetProgress')

        if m.get('TargetTraffic') is not None:
            self.target_traffic = m.get('TargetTraffic')

        return self

