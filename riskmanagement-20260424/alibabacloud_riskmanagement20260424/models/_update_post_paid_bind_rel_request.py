# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_riskmanagement20260424 import models as main_models
from darabonba.model import DaraModel

class UpdatePostPaidBindRelRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        sdk_request: main_models.UpdatePostPaidBindRelRequestSdkRequest = None,
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
            temp_model = main_models.UpdatePostPaidBindRelRequestSdkRequest()
            self.sdk_request = temp_model.from_map(m.get('SdkRequest'))

        return self

class UpdatePostPaidBindRelRequestSdkRequest(DaraModel):
    def __init__(
        self,
        auto_bind: int = None,
        auto_bind_version: int = None,
        bind_action: List[main_models.UpdatePostPaidBindRelRequestSdkRequestBindAction] = None,
        update_if_necessary: bool = None,
    ):
        self.auto_bind = auto_bind
        self.auto_bind_version = auto_bind_version
        self.bind_action = bind_action
        self.update_if_necessary = update_if_necessary

    def validate(self):
        if self.bind_action:
            for v1 in self.bind_action:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_bind is not None:
            result['AutoBind'] = self.auto_bind

        if self.auto_bind_version is not None:
            result['AutoBindVersion'] = self.auto_bind_version

        result['BindAction'] = []
        if self.bind_action is not None:
            for k1 in self.bind_action:
                result['BindAction'].append(k1.to_map() if k1 else None)

        if self.update_if_necessary is not None:
            result['UpdateIfNecessary'] = self.update_if_necessary

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoBind') is not None:
            self.auto_bind = m.get('AutoBind')

        if m.get('AutoBindVersion') is not None:
            self.auto_bind_version = m.get('AutoBindVersion')

        self.bind_action = []
        if m.get('BindAction') is not None:
            for k1 in m.get('BindAction'):
                temp_model = main_models.UpdatePostPaidBindRelRequestSdkRequestBindAction()
                self.bind_action.append(temp_model.from_map(k1))

        if m.get('UpdateIfNecessary') is not None:
            self.update_if_necessary = m.get('UpdateIfNecessary')

        return self

class UpdatePostPaidBindRelRequestSdkRequestBindAction(DaraModel):
    def __init__(
        self,
        bind_all: bool = None,
        uuid_list: List[str] = None,
        version: str = None,
    ):
        self.bind_all = bind_all
        self.uuid_list = uuid_list
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bind_all is not None:
            result['BindAll'] = self.bind_all

        if self.uuid_list is not None:
            result['UuidList'] = self.uuid_list

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindAll') is not None:
            self.bind_all = m.get('BindAll')

        if m.get('UuidList') is not None:
            self.uuid_list = m.get('UuidList')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

