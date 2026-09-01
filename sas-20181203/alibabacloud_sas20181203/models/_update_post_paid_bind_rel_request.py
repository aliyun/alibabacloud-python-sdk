# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class UpdatePostPaidBindRelRequest(DaraModel):
    def __init__(
        self,
        auto_bind: int = None,
        auto_bind_version: int = None,
        bind_action: List[main_models.UpdatePostPaidBindRelRequestBindAction] = None,
        client_token: str = None,
        product_code: str = None,
        update_if_necessary: bool = None,
    ):
        # Specifies whether to enable automatic binding for new assets. Valid values:
        # 
        # - **0**: disabled
        # - **1**: enabled
        self.auto_bind = auto_bind
        # The edition to automatically bind when new assets are added. Valid values:
        # - **1**: Free Edition 
        # - **3**: Enterprise Edition
        # - **5**: Advanced Edition
        # - **6**: Anti-virus Edition    
        # - **7**: Ultimate Edition
        self.auto_bind_version = auto_bind_version
        # The binding action parameter.
        self.bind_action = bind_action
        # The client token that is used to ensure the idempotence of the request. Different requests must use different tokens. The token supports only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        self.product_code = product_code
        # Specifies whether to forcibly upgrade the edition.
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

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

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
                temp_model = main_models.UpdatePostPaidBindRelRequestBindAction()
                self.bind_action.append(temp_model.from_map(k1))

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('UpdateIfNecessary') is not None:
            self.update_if_necessary = m.get('UpdateIfNecessary')

        return self

class UpdatePostPaidBindRelRequestBindAction(DaraModel):
    def __init__(
        self,
        bind_all: bool = None,
        free_type: str = None,
        uuid_list: List[str] = None,
        version: str = None,
    ):
        # Specifies whether to bind all servers. Default value: **false**. Valid values:
        # 
        # - **true**: yes
        # - **false**: no
        self.bind_all = bind_all
        self.free_type = free_type
        # The list of server UUIDs.
        self.uuid_list = uuid_list
        # The protection edition of Security Center to bind. Valid values:  
        # - **1**: Free Edition 
        # - **3**: Enterprise Edition
        # - **5**: Advanced Edition
        # - **6**: Anti-virus Edition    
        # - **7**: Ultimate Edition
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

        if self.free_type is not None:
            result['FreeType'] = self.free_type

        if self.uuid_list is not None:
            result['UuidList'] = self.uuid_list

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindAll') is not None:
            self.bind_all = m.get('BindAll')

        if m.get('FreeType') is not None:
            self.free_type = m.get('FreeType')

        if m.get('UuidList') is not None:
            self.uuid_list = m.get('UuidList')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

