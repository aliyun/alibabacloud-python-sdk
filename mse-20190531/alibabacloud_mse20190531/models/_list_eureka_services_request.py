# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListEurekaServicesRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        cluster_id: str = None,
        page_num: int = None,
        page_size: int = None,
        region_id: str = None,
        request_pars: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.accept_language = accept_language
        # The ID of the instance.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The number of the page to return.
        # 
        # This parameter is required.
        self.page_num = page_num
        # The number of entries to return on each page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The region ID.
        self.region_id = region_id
        # The extended request parameters in the JSON format.
        self.request_pars = request_pars

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')

        return self

