# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_hitsdb20200615 import models as main_models
from darabonba.model import DaraModel

class ListLdpsComputeGroupsResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        group_list: List[main_models.ListLdpsComputeGroupsResponseBodyGroupList] = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.group_list = group_list
        self.request_id = request_id

    def validate(self):
        if self.group_list:
            for v1 in self.group_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        result['GroupList'] = []
        if self.group_list is not None:
            for k1 in self.group_list:
                result['GroupList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        self.group_list = []
        if m.get('GroupList') is not None:
            for k1 in m.get('GroupList'):
                temp_model = main_models.ListLdpsComputeGroupsResponseBodyGroupList()
                self.group_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListLdpsComputeGroupsResponseBodyGroupList(DaraModel):
    def __init__(
        self,
        exception_info: str = None,
        group_name: str = None,
        is_default: bool = None,
        properties: Dict[str, Any] = None,
        state: str = None,
        web_ui: str = None,
    ):
        self.exception_info = exception_info
        self.group_name = group_name
        self.is_default = is_default
        self.properties = properties
        self.state = state
        self.web_ui = web_ui

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exception_info is not None:
            result['ExceptionInfo'] = self.exception_info

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.properties is not None:
            result['Properties'] = self.properties

        if self.state is not None:
            result['State'] = self.state

        if self.web_ui is not None:
            result['WebUI'] = self.web_ui

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExceptionInfo') is not None:
            self.exception_info = m.get('ExceptionInfo')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('Properties') is not None:
            self.properties = m.get('Properties')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('WebUI') is not None:
            self.web_ui = m.get('WebUI')

        return self

