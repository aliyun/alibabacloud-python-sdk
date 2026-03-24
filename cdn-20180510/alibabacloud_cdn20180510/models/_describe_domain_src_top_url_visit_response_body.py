# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cdn20180510 import models as main_models
from darabonba.model import DaraModel

class DescribeDomainSrcTopUrlVisitResponseBody(DaraModel):
    def __init__(
        self,
        all_url_list: main_models.DescribeDomainSrcTopUrlVisitResponseBodyAllUrlList = None,
        domain_name: str = None,
        request_id: str = None,
        start_time: str = None,
        url_200list: main_models.DescribeDomainSrcTopUrlVisitResponseBodyUrl200List = None,
        url_300list: main_models.DescribeDomainSrcTopUrlVisitResponseBodyUrl300List = None,
        url_400list: main_models.DescribeDomainSrcTopUrlVisitResponseBodyUrl400List = None,
        url_500list: main_models.DescribeDomainSrcTopUrlVisitResponseBodyUrl500List = None,
    ):
        self.all_url_list = all_url_list
        # The accelerated domain name.
        self.domain_name = domain_name
        # The ID of the request.
        self.request_id = request_id
        # The beginning of the time range that was queried.
        self.start_time = start_time
        self.url_200list = url_200list
        self.url_300list = url_300list
        self.url_400list = url_400list
        self.url_500list = url_500list

    def validate(self):
        if self.all_url_list:
            self.all_url_list.validate()
        if self.url_200list:
            self.url_200list.validate()
        if self.url_300list:
            self.url_300list.validate()
        if self.url_400list:
            self.url_400list.validate()
        if self.url_500list:
            self.url_500list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.all_url_list is not None:
            result['AllUrlList'] = self.all_url_list.to_map()

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.url_200list is not None:
            result['Url200List'] = self.url_200list.to_map()

        if self.url_300list is not None:
            result['Url300List'] = self.url_300list.to_map()

        if self.url_400list is not None:
            result['Url400List'] = self.url_400list.to_map()

        if self.url_500list is not None:
            result['Url500List'] = self.url_500list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllUrlList') is not None:
            temp_model = main_models.DescribeDomainSrcTopUrlVisitResponseBodyAllUrlList()
            self.all_url_list = temp_model.from_map(m.get('AllUrlList'))

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Url200List') is not None:
            temp_model = main_models.DescribeDomainSrcTopUrlVisitResponseBodyUrl200List()
            self.url_200list = temp_model.from_map(m.get('Url200List'))

        if m.get('Url300List') is not None:
            temp_model = main_models.DescribeDomainSrcTopUrlVisitResponseBodyUrl300List()
            self.url_300list = temp_model.from_map(m.get('Url300List'))

        if m.get('Url400List') is not None:
            temp_model = main_models.DescribeDomainSrcTopUrlVisitResponseBodyUrl400List()
            self.url_400list = temp_model.from_map(m.get('Url400List'))

        if m.get('Url500List') is not None:
            temp_model = main_models.DescribeDomainSrcTopUrlVisitResponseBodyUrl500List()
            self.url_500list = temp_model.from_map(m.get('Url500List'))

        return self

class DescribeDomainSrcTopUrlVisitResponseBodyUrl500List(DaraModel):
    def __init__(
        self,
        url_list: List[main_models.DescribeDomainSrcTopUrlVisitResponseBodyUrl500ListUrlList] = None,
    ):
        self.url_list = url_list

    def validate(self):
        if self.url_list:
            for v1 in self.url_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['UrlList'] = []
        if self.url_list is not None:
            for k1 in self.url_list:
                result['UrlList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.url_list = []
        if m.get('UrlList') is not None:
            for k1 in m.get('UrlList'):
                temp_model = main_models.DescribeDomainSrcTopUrlVisitResponseBodyUrl500ListUrlList()
                self.url_list.append(temp_model.from_map(k1))

        return self

class DescribeDomainSrcTopUrlVisitResponseBodyUrl500ListUrlList(DaraModel):
    def __init__(
        self,
        flow: str = None,
        flow_proportion: float = None,
        url_detail: str = None,
        visit_data: str = None,
        visit_proportion: float = None,
    ):
        self.flow = flow
        self.flow_proportion = flow_proportion
        self.url_detail = url_detail
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

        if self.url_detail is not None:
            result['UrlDetail'] = self.url_detail

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

        if m.get('UrlDetail') is not None:
            self.url_detail = m.get('UrlDetail')

        if m.get('VisitData') is not None:
            self.visit_data = m.get('VisitData')

        if m.get('VisitProportion') is not None:
            self.visit_proportion = m.get('VisitProportion')

        return self

class DescribeDomainSrcTopUrlVisitResponseBodyUrl400List(DaraModel):
    def __init__(
        self,
        url_list: List[main_models.DescribeDomainSrcTopUrlVisitResponseBodyUrl400ListUrlList] = None,
    ):
        self.url_list = url_list

    def validate(self):
        if self.url_list:
            for v1 in self.url_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['UrlList'] = []
        if self.url_list is not None:
            for k1 in self.url_list:
                result['UrlList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.url_list = []
        if m.get('UrlList') is not None:
            for k1 in m.get('UrlList'):
                temp_model = main_models.DescribeDomainSrcTopUrlVisitResponseBodyUrl400ListUrlList()
                self.url_list.append(temp_model.from_map(k1))

        return self

class DescribeDomainSrcTopUrlVisitResponseBodyUrl400ListUrlList(DaraModel):
    def __init__(
        self,
        flow: str = None,
        flow_proportion: float = None,
        url_detail: str = None,
        visit_data: str = None,
        visit_proportion: float = None,
    ):
        self.flow = flow
        self.flow_proportion = flow_proportion
        self.url_detail = url_detail
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

        if self.url_detail is not None:
            result['UrlDetail'] = self.url_detail

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

        if m.get('UrlDetail') is not None:
            self.url_detail = m.get('UrlDetail')

        if m.get('VisitData') is not None:
            self.visit_data = m.get('VisitData')

        if m.get('VisitProportion') is not None:
            self.visit_proportion = m.get('VisitProportion')

        return self

class DescribeDomainSrcTopUrlVisitResponseBodyUrl300List(DaraModel):
    def __init__(
        self,
        url_list: List[main_models.DescribeDomainSrcTopUrlVisitResponseBodyUrl300ListUrlList] = None,
    ):
        self.url_list = url_list

    def validate(self):
        if self.url_list:
            for v1 in self.url_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['UrlList'] = []
        if self.url_list is not None:
            for k1 in self.url_list:
                result['UrlList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.url_list = []
        if m.get('UrlList') is not None:
            for k1 in m.get('UrlList'):
                temp_model = main_models.DescribeDomainSrcTopUrlVisitResponseBodyUrl300ListUrlList()
                self.url_list.append(temp_model.from_map(k1))

        return self

class DescribeDomainSrcTopUrlVisitResponseBodyUrl300ListUrlList(DaraModel):
    def __init__(
        self,
        flow: str = None,
        flow_proportion: float = None,
        url_detail: str = None,
        visit_data: str = None,
        visit_proportion: float = None,
    ):
        self.flow = flow
        self.flow_proportion = flow_proportion
        self.url_detail = url_detail
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

        if self.url_detail is not None:
            result['UrlDetail'] = self.url_detail

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

        if m.get('UrlDetail') is not None:
            self.url_detail = m.get('UrlDetail')

        if m.get('VisitData') is not None:
            self.visit_data = m.get('VisitData')

        if m.get('VisitProportion') is not None:
            self.visit_proportion = m.get('VisitProportion')

        return self

class DescribeDomainSrcTopUrlVisitResponseBodyUrl200List(DaraModel):
    def __init__(
        self,
        url_list: List[main_models.DescribeDomainSrcTopUrlVisitResponseBodyUrl200ListUrlList] = None,
    ):
        self.url_list = url_list

    def validate(self):
        if self.url_list:
            for v1 in self.url_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['UrlList'] = []
        if self.url_list is not None:
            for k1 in self.url_list:
                result['UrlList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.url_list = []
        if m.get('UrlList') is not None:
            for k1 in m.get('UrlList'):
                temp_model = main_models.DescribeDomainSrcTopUrlVisitResponseBodyUrl200ListUrlList()
                self.url_list.append(temp_model.from_map(k1))

        return self

class DescribeDomainSrcTopUrlVisitResponseBodyUrl200ListUrlList(DaraModel):
    def __init__(
        self,
        flow: str = None,
        flow_proportion: float = None,
        url_detail: str = None,
        visit_data: str = None,
        visit_proportion: float = None,
    ):
        self.flow = flow
        self.flow_proportion = flow_proportion
        self.url_detail = url_detail
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

        if self.url_detail is not None:
            result['UrlDetail'] = self.url_detail

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

        if m.get('UrlDetail') is not None:
            self.url_detail = m.get('UrlDetail')

        if m.get('VisitData') is not None:
            self.visit_data = m.get('VisitData')

        if m.get('VisitProportion') is not None:
            self.visit_proportion = m.get('VisitProportion')

        return self

class DescribeDomainSrcTopUrlVisitResponseBodyAllUrlList(DaraModel):
    def __init__(
        self,
        url_list: List[main_models.DescribeDomainSrcTopUrlVisitResponseBodyAllUrlListUrlList] = None,
    ):
        self.url_list = url_list

    def validate(self):
        if self.url_list:
            for v1 in self.url_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['UrlList'] = []
        if self.url_list is not None:
            for k1 in self.url_list:
                result['UrlList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.url_list = []
        if m.get('UrlList') is not None:
            for k1 in m.get('UrlList'):
                temp_model = main_models.DescribeDomainSrcTopUrlVisitResponseBodyAllUrlListUrlList()
                self.url_list.append(temp_model.from_map(k1))

        return self

class DescribeDomainSrcTopUrlVisitResponseBodyAllUrlListUrlList(DaraModel):
    def __init__(
        self,
        flow: str = None,
        flow_proportion: float = None,
        url_detail: str = None,
        visit_data: str = None,
        visit_proportion: float = None,
    ):
        self.flow = flow
        self.flow_proportion = flow_proportion
        self.url_detail = url_detail
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

        if self.url_detail is not None:
            result['UrlDetail'] = self.url_detail

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

        if m.get('UrlDetail') is not None:
            self.url_detail = m.get('UrlDetail')

        if m.get('VisitData') is not None:
            self.visit_data = m.get('VisitData')

        if m.get('VisitProportion') is not None:
            self.visit_proportion = m.get('VisitProportion')

        return self

