# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dyvmsapi20170525 import models as main_models
from darabonba.model import DaraModel

class SetTransferCalleePoolConfigRequest(DaraModel):
    def __init__(
        self,
        called_route_mode: str = None,
        details: List[main_models.SetTransferCalleePoolConfigRequestDetails] = None,
        owner_id: int = None,
        phone_number: str = None,
        qualification_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The call mode. Valid values:
        # 
        # *   **roundRobin**
        # *   **random**
        # 
        # This parameter is required.
        self.called_route_mode = called_route_mode
        # The information about the phone numbers for transferring the call.
        # 
        # This parameter is required.
        self.details = details
        self.owner_id = owner_id
        # The phone number used for transferring the call.
        # 
        # This parameter is required.
        self.phone_number = phone_number
        # The qualification ID. You can call the [GetHotlineQualificationByOrder](https://help.aliyun.com/document_detail/393548.html) operation to obtain the qualification ID.
        # 
        # This parameter is required.
        self.qualification_id = qualification_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        if self.details:
            for v1 in self.details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.called_route_mode is not None:
            result['CalledRouteMode'] = self.called_route_mode

        result['Details'] = []
        if self.details is not None:
            for k1 in self.details:
                result['Details'].append(k1.to_map() if k1 else None)

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number

        if self.qualification_id is not None:
            result['QualificationId'] = self.qualification_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CalledRouteMode') is not None:
            self.called_route_mode = m.get('CalledRouteMode')

        self.details = []
        if m.get('Details') is not None:
            for k1 in m.get('Details'):
                temp_model = main_models.SetTransferCalleePoolConfigRequestDetails()
                self.details.append(temp_model.from_map(k1))

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        if m.get('QualificationId') is not None:
            self.qualification_id = m.get('QualificationId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

class SetTransferCalleePoolConfigRequestDetails(DaraModel):
    def __init__(
        self,
        called: str = None,
        caller: str = None,
    ):
        # The called number.
        # 
        # This parameter is required.
        self.called = called
        # The calling number.
        self.caller = caller

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.called is not None:
            result['Called'] = self.called

        if self.caller is not None:
            result['Caller'] = self.caller

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Called') is not None:
            self.called = m.get('Called')

        if m.get('Caller') is not None:
            self.caller = m.get('Caller')

        return self

