# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryNacosGrayConfigRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        data_id: str = None,
        gray_name: str = None,
        group: str = None,
        instance_id: str = None,
        namespace_id: str = None,
        region_id: str = None,
        request_pars: str = None,
    ):
        self.accept_language = accept_language
        # This parameter is required.
        self.data_id = data_id
        self.gray_name = gray_name
        self.group = group
        # This parameter is required.
        self.instance_id = instance_id
        self.namespace_id = namespace_id
        self.region_id = region_id
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

        if self.data_id is not None:
            result['DataId'] = self.data_id

        if self.gray_name is not None:
            result['GrayName'] = self.gray_name

        if self.group is not None:
            result['Group'] = self.group

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')

        if m.get('GrayName') is not None:
            self.gray_name = m.get('GrayName')

        if m.get('Group') is not None:
            self.group = m.get('Group')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')

        return self

