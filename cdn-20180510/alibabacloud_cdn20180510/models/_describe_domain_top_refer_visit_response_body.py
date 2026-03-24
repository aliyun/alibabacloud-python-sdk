# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cdn20180510 import models as main_models
from darabonba.model import DaraModel

class DescribeDomainTopReferVisitResponseBody(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        request_id: str = None,
        start_time: str = None,
        top_refer_list: main_models.DescribeDomainTopReferVisitResponseBodyTopReferList = None,
    ):
        # The accelerated domain name.
        self.domain_name = domain_name
        # The ID of the request.
        self.request_id = request_id
        # The beginning of the time range that was queried.
        self.start_time = start_time
        self.top_refer_list = top_refer_list

    def validate(self):
        if self.top_refer_list:
            self.top_refer_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.top_refer_list is not None:
            result['TopReferList'] = self.top_refer_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TopReferList') is not None:
            temp_model = main_models.DescribeDomainTopReferVisitResponseBodyTopReferList()
            self.top_refer_list = temp_model.from_map(m.get('TopReferList'))

        return self

class DescribeDomainTopReferVisitResponseBodyTopReferList(DaraModel):
    def __init__(
        self,
        refer_list: List[main_models.DescribeDomainTopReferVisitResponseBodyTopReferListReferList] = None,
    ):
        self.refer_list = refer_list

    def validate(self):
        if self.refer_list:
            for v1 in self.refer_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ReferList'] = []
        if self.refer_list is not None:
            for k1 in self.refer_list:
                result['ReferList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.refer_list = []
        if m.get('ReferList') is not None:
            for k1 in m.get('ReferList'):
                temp_model = main_models.DescribeDomainTopReferVisitResponseBodyTopReferListReferList()
                self.refer_list.append(temp_model.from_map(k1))

        return self

class DescribeDomainTopReferVisitResponseBodyTopReferListReferList(DaraModel):
    def __init__(
        self,
        flow: str = None,
        flow_proportion: float = None,
        refer_detail: str = None,
        visit_data: str = None,
        visit_proportion: float = None,
    ):
        self.flow = flow
        self.flow_proportion = flow_proportion
        self.refer_detail = refer_detail
        self.visit_data = visit_data
        self.visit_proportion = visit_proportion

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.flow is not None:
            result['Flow'] = self.flow

        if self.flow_proportion is not None:
            result['FlowProportion'] = self.flow_proportion

        if self.refer_detail is not None:
            result['ReferDetail'] = self.refer_detail

        if self.visit_data is not None:
            result['VisitData'] = self.visit_data

        if self.visit_proportion is not None:
            result['VisitProportion'] = self.visit_proportion

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')

        if m.get('FlowProportion') is not None:
            self.flow_proportion = m.get('FlowProportion')

        if m.get('ReferDetail') is not None:
            self.refer_detail = m.get('ReferDetail')

        if m.get('VisitData') is not None:
            self.visit_data = m.get('VisitData')

        if m.get('VisitProportion') is not None:
            self.visit_proportion = m.get('VisitProportion')

        return self

