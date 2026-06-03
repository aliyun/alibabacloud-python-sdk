# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CopyVerifySchemeRequest(DaraModel):
    def __init__(
        self,
        cm_api_code: int = None,
        cm_new_flag: bool = None,
        ct_api_code: int = None,
        ct_new_flag: bool = None,
        cu_api_code: int = None,
        cu_new_flag: bool = None,
        email: str = None,
        model_scene_code: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # native：1，web：5
        self.cm_api_code = cm_api_code
        # true，将在移动侧创建新的AppId，false将直接从模版方案中复制已经创建的移动AppId信息
        self.cm_new_flag = cm_new_flag
        # native：3，web：8
        self.ct_api_code = ct_api_code
        # true，将在电信侧创建新的AppId，false将直接从模版方案中复制已经创建的电信AppId信息
        self.ct_new_flag = ct_new_flag
        # native：9，web：10
        self.cu_api_code = cu_api_code
        # true，将在联通侧创建新的AppId，false将直接从模版方案中复制已经创建的联通AppId信息
        self.cu_new_flag = cu_new_flag
        self.email = email
        # This parameter is required.
        self.model_scene_code = model_scene_code
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cm_api_code is not None:
            result['CmApiCode'] = self.cm_api_code

        if self.cm_new_flag is not None:
            result['CmNewFlag'] = self.cm_new_flag

        if self.ct_api_code is not None:
            result['CtApiCode'] = self.ct_api_code

        if self.ct_new_flag is not None:
            result['CtNewFlag'] = self.ct_new_flag

        if self.cu_api_code is not None:
            result['CuApiCode'] = self.cu_api_code

        if self.cu_new_flag is not None:
            result['CuNewFlag'] = self.cu_new_flag

        if self.email is not None:
            result['Email'] = self.email

        if self.model_scene_code is not None:
            result['ModelSceneCode'] = self.model_scene_code

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CmApiCode') is not None:
            self.cm_api_code = m.get('CmApiCode')

        if m.get('CmNewFlag') is not None:
            self.cm_new_flag = m.get('CmNewFlag')

        if m.get('CtApiCode') is not None:
            self.ct_api_code = m.get('CtApiCode')

        if m.get('CtNewFlag') is not None:
            self.ct_new_flag = m.get('CtNewFlag')

        if m.get('CuApiCode') is not None:
            self.cu_api_code = m.get('CuApiCode')

        if m.get('CuNewFlag') is not None:
            self.cu_new_flag = m.get('CuNewFlag')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('ModelSceneCode') is not None:
            self.model_scene_code = m.get('ModelSceneCode')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

