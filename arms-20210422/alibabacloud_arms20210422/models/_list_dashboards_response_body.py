# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20210422 import models as main_models
from darabonba.model import DaraModel

class ListDashboardsResponseBody(DaraModel):
    def __init__(
        self,
        dashboard_vos: List[main_models.ListDashboardsResponseBodyDashboardVos] = None,
        request_id: str = None,
    ):
        self.dashboard_vos = dashboard_vos
        self.request_id = request_id

    def validate(self):
        if self.dashboard_vos:
            for v1 in self.dashboard_vos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DashboardVos'] = []
        if self.dashboard_vos is not None:
            for k1 in self.dashboard_vos:
                result['DashboardVos'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dashboard_vos = []
        if m.get('DashboardVos') is not None:
            for k1 in m.get('DashboardVos'):
                temp_model = main_models.ListDashboardsResponseBodyDashboardVos()
                self.dashboard_vos.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListDashboardsResponseBodyDashboardVos(DaraModel):
    def __init__(
        self,
        dashboard_type: str = None,
        exporter: str = None,
        id: str = None,
        is_arms_exporter: bool = None,
        kind: str = None,
        name: str = None,
        need_update: bool = None,
        tags: List[str] = None,
        time: str = None,
        title: str = None,
        type: str = None,
        uid: str = None,
        url: str = None,
        version: str = None,
    ):
        self.dashboard_type = dashboard_type
        self.exporter = exporter
        self.id = id
        self.is_arms_exporter = is_arms_exporter
        self.kind = kind
        self.name = name
        self.need_update = need_update
        self.tags = tags
        self.time = time
        self.title = title
        self.type = type
        self.uid = uid
        self.url = url
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dashboard_type is not None:
            result['DashboardType'] = self.dashboard_type

        if self.exporter is not None:
            result['Exporter'] = self.exporter

        if self.id is not None:
            result['Id'] = self.id

        if self.is_arms_exporter is not None:
            result['IsArmsExporter'] = self.is_arms_exporter

        if self.kind is not None:
            result['Kind'] = self.kind

        if self.name is not None:
            result['Name'] = self.name

        if self.need_update is not None:
            result['NeedUpdate'] = self.need_update

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.time is not None:
            result['Time'] = self.time

        if self.title is not None:
            result['Title'] = self.title

        if self.type is not None:
            result['Type'] = self.type

        if self.uid is not None:
            result['Uid'] = self.uid

        if self.url is not None:
            result['Url'] = self.url

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DashboardType') is not None:
            self.dashboard_type = m.get('DashboardType')

        if m.get('Exporter') is not None:
            self.exporter = m.get('Exporter')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IsArmsExporter') is not None:
            self.is_arms_exporter = m.get('IsArmsExporter')

        if m.get('Kind') is not None:
            self.kind = m.get('Kind')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NeedUpdate') is not None:
            self.need_update = m.get('NeedUpdate')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

