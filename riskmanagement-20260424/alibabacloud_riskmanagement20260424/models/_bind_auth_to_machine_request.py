# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_riskmanagement20260424 import models as main_models
from darabonba.model import DaraModel

class BindAuthToMachineRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        sdk_request: main_models.BindAuthToMachineRequestSdkRequest = None,
    ):
        self.region_id = region_id
        self.sdk_request = sdk_request

    def validate(self):
        if self.sdk_request:
            self.sdk_request.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.sdk_request is not None:
            result['SdkRequest'] = self.sdk_request.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SdkRequest') is not None:
            temp_model = main_models.BindAuthToMachineRequestSdkRequest()
            self.sdk_request = temp_model.from_map(m.get('SdkRequest'))

        return self



class BindAuthToMachineRequestSdkRequest(DaraModel):
    def __init__(
        self,
        auth_version: int = None,
        auto_bind: int = None,
        bind: List[str] = None,
        bind_all: bool = None,
        criteria: str = None,
        is_pre_bind: int = None,
        logical_exp: str = None,
        ntm_version: int = None,
        pre_bind_order_id: int = None,
        un_bind: List[str] = None,
    ):
        self.auth_version = auth_version
        self.auto_bind = auto_bind
        self.bind = bind
        self.bind_all = bind_all
        self.criteria = criteria
        self.is_pre_bind = is_pre_bind
        self.logical_exp = logical_exp
        self.ntm_version = ntm_version
        self.pre_bind_order_id = pre_bind_order_id
        self.un_bind = un_bind

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_version is not None:
            result['AuthVersion'] = self.auth_version

        if self.auto_bind is not None:
            result['AutoBind'] = self.auto_bind

        if self.bind is not None:
            result['Bind'] = self.bind

        if self.bind_all is not None:
            result['BindAll'] = self.bind_all

        if self.criteria is not None:
            result['Criteria'] = self.criteria

        if self.is_pre_bind is not None:
            result['IsPreBind'] = self.is_pre_bind

        if self.logical_exp is not None:
            result['LogicalExp'] = self.logical_exp

        if self.ntm_version is not None:
            result['NtmVersion'] = self.ntm_version

        if self.pre_bind_order_id is not None:
            result['PreBindOrderId'] = self.pre_bind_order_id

        if self.un_bind is not None:
            result['UnBind'] = self.un_bind

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthVersion') is not None:
            self.auth_version = m.get('AuthVersion')

        if m.get('AutoBind') is not None:
            self.auto_bind = m.get('AutoBind')

        if m.get('Bind') is not None:
            self.bind = m.get('Bind')

        if m.get('BindAll') is not None:
            self.bind_all = m.get('BindAll')

        if m.get('Criteria') is not None:
            self.criteria = m.get('Criteria')

        if m.get('IsPreBind') is not None:
            self.is_pre_bind = m.get('IsPreBind')

        if m.get('LogicalExp') is not None:
            self.logical_exp = m.get('LogicalExp')

        if m.get('NtmVersion') is not None:
            self.ntm_version = m.get('NtmVersion')

        if m.get('PreBindOrderId') is not None:
            self.pre_bind_order_id = m.get('PreBindOrderId')

        if m.get('UnBind') is not None:
            self.un_bind = m.get('UnBind')

        return self

