# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sfmmultimodalapp20250909 import models as main_models
from darabonba.model import DaraModel

class ListDomainResponseBody(DaraModel):
    def __init__(
        self,
        domain_info_list: List[main_models.ListDomainResponseBodyDomainInfoList] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.domain_info_list = domain_info_list
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.domain_info_list:
            for v1 in self.domain_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DomainInfoList'] = []
        if self.domain_info_list is not None:
            for k1 in self.domain_info_list:
                result['DomainInfoList'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_info_list = []
        if m.get('DomainInfoList') is not None:
            for k1 in m.get('DomainInfoList'):
                temp_model = main_models.ListDomainResponseBodyDomainInfoList()
                self.domain_info_list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListDomainResponseBodyDomainInfoList(DaraModel):
    def __init__(
        self,
        domain_code: str = None,
        domain_name: str = None,
        tool_count: int = None,
        tool_list: List[main_models.ListDomainResponseBodyDomainInfoListToolList] = None,
    ):
        self.domain_code = domain_code
        self.domain_name = domain_name
        self.tool_count = tool_count
        self.tool_list = tool_list

    def validate(self):
        if self.tool_list:
            for v1 in self.tool_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_code is not None:
            result['DomainCode'] = self.domain_code

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.tool_count is not None:
            result['ToolCount'] = self.tool_count

        result['ToolList'] = []
        if self.tool_list is not None:
            for k1 in self.tool_list:
                result['ToolList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainCode') is not None:
            self.domain_code = m.get('DomainCode')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('ToolCount') is not None:
            self.tool_count = m.get('ToolCount')

        self.tool_list = []
        if m.get('ToolList') is not None:
            for k1 in m.get('ToolList'):
                temp_model = main_models.ListDomainResponseBodyDomainInfoListToolList()
                self.tool_list.append(temp_model.from_map(k1))

        return self

class ListDomainResponseBodyDomainInfoListToolList(DaraModel):
    def __init__(
        self,
        tool_code: str = None,
        tool_name: str = None,
    ):
        self.tool_code = tool_code
        self.tool_name = tool_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tool_code is not None:
            result['ToolCode'] = self.tool_code

        if self.tool_name is not None:
            result['ToolName'] = self.tool_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ToolCode') is not None:
            self.tool_code = m.get('ToolCode')

        if m.get('ToolName') is not None:
            self.tool_name = m.get('ToolName')

        return self

