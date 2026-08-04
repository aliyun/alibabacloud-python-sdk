# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aligeniessp_1_0 import models as main_models
from darabonba.model import DaraModel

class ScanCodeBindRequest(DaraModel):
    def __init__(
        self,
        bind_req: main_models.ScanCodeBindRequestBindReq = None,
        user_info: main_models.ScanCodeBindRequestUserInfo = None,
    ):
        # Input parameters for QR code scanning binding
        # 
        # This parameter is required.
        self.bind_req = bind_req
        # User identity information
        # 
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.bind_req:
            self.bind_req.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bind_req is not None:
            result['BindReq'] = self.bind_req.to_map()

        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindReq') is not None:
            temp_model = main_models.ScanCodeBindRequestBindReq()
            self.bind_req = temp_model.from_map(m.get('BindReq'))

        if m.get('UserInfo') is not None:
            temp_model = main_models.ScanCodeBindRequestUserInfo()
            self.user_info = temp_model.from_map(m.get('UserInfo'))

        return self

class ScanCodeBindRequestUserInfo(DaraModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # Value corresponding to the encoding type. Enter the Project ID of the project to which the product belongs. You can view this in the Tmall Genie AI Platform console.
        # 
        # This parameter is required.
        self.encode_key = encode_key
        # Encoding type. Enter PROJECT_ID here.
        # 
        # This parameter is required.
        self.encode_type = encode_type
        # User Identifier. Enter the value of userOpenId or userUnionId.
        # 
        # This parameter is required.
        self.id = id
        # Device ID type:  
        # OPEN_ID: Default Device ID identifier.  
        # UNION_ID: Organization-dimension Device ID identifier. You must request an organization in advance on the Open Platform.
        # 
        # This parameter is required.
        self.id_type = id_type
        # Organization ID. Required if IdType is UNION_ID.
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key

        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type

        if self.id is not None:
            result['Id'] = self.id

        if self.id_type is not None:
            result['IdType'] = self.id_type

        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')

        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')

        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')

        return self

class ScanCodeBindRequestBindReq(DaraModel):
    def __init__(
        self,
        client_id: str = None,
        code: str = None,
        ext_info: str = None,
    ):
        # Product client ID
        # 
        # This parameter is required.
        self.client_id = client_id
        # authCode
        # 
        # This parameter is required.
        self.code = code
        # Extension parameter
        self.ext_info = ext_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.code is not None:
            result['Code'] = self.code

        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')

        return self

