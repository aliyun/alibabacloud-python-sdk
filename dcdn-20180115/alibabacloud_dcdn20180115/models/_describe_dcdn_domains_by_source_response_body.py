# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dcdn20180115 import models as main_models
from darabonba.model import DaraModel

class DescribeDcdnDomainsBySourceResponseBody(DaraModel):
    def __init__(
        self,
        domain_info: List[main_models.DescribeDcdnDomainsBySourceResponseBodyDomainInfo] = None,
        request_id: str = None,
    ):
        # The information about each origin server and the corresponding domain names.
        # 
        # This parameter is required.
        self.domain_info = domain_info
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.domain_info:
            for v1 in self.domain_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DomainInfo'] = []
        if self.domain_info is not None:
            for k1 in self.domain_info:
                result['DomainInfo'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_info = []
        if m.get('DomainInfo') is not None:
            for k1 in m.get('DomainInfo'):
                temp_model = main_models.DescribeDcdnDomainsBySourceResponseBodyDomainInfo()
                self.domain_info.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDcdnDomainsBySourceResponseBodyDomainInfo(DaraModel):
    def __init__(
        self,
        domain_list: List[main_models.DescribeDcdnDomainsBySourceResponseBodyDomainInfoDomainList] = None,
        source: str = None,
    ):
        # The information about the domain names.
        self.domain_list = domain_list
        # The origin server.
        self.source = source

    def validate(self):
        if self.domain_list:
            for v1 in self.domain_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DomainList'] = []
        if self.domain_list is not None:
            for k1 in self.domain_list:
                result['DomainList'].append(k1.to_map() if k1 else None)

        if self.source is not None:
            result['Source'] = self.source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_list = []
        if m.get('DomainList') is not None:
            for k1 in m.get('DomainList'):
                temp_model = main_models.DescribeDcdnDomainsBySourceResponseBodyDomainInfoDomainList()
                self.domain_list.append(temp_model.from_map(k1))

        if m.get('Source') is not None:
            self.source = m.get('Source')

        return self

class DescribeDcdnDomainsBySourceResponseBodyDomainInfoDomainList(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        domain_cname: str = None,
        domain_name: str = None,
        domain_type: str = None,
        status: str = None,
        update_time: str = None,
    ):
        # The creation time.
        self.create_time = create_time
        # The CNAME record assigned to the domain name.
        self.domain_cname = domain_cname
        # The accelerated domain name.
        self.domain_name = domain_name
        # The workload type of the accelerated domain name. Valid value:
        # 
        # *   **ipa**: layer 4 acceleration
        # *   **dynamic**: layer 7 acceleration
        self.domain_type = domain_type
        # The status of the domain name. Valid value:
        # 
        # *   **applying**: The domain name is under review.
        # *   **configuring**: The domain name is being configured.
        # *   **online**: The domain name is working as expected.
        # *   **stopping**: The domain name is being stopped.
        # *   **offline**: The domain name is disabled.
        # *   **disabling**: The domain name is being removed.
        self.status = status
        # The time when the domain name was updated.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.domain_cname is not None:
            result['DomainCname'] = self.domain_cname

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.domain_type is not None:
            result['DomainType'] = self.domain_type

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DomainCname') is not None:
            self.domain_cname = m.get('DomainCname')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

