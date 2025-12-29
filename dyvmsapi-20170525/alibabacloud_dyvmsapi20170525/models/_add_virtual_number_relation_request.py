# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddVirtualNumberRelationRequest(DaraModel):
    def __init__(
        self,
        corp_name_list: str = None,
        number_list: str = None,
        owner_id: int = None,
        phone_num: str = None,
        prod_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        route_type: int = None,
    ):
        # The company names. Separate multiple company names with commas (,).
        self.corp_name_list = corp_name_list
        # The real numbers. Separate multiple real numbers with commas (,).
        # 
        # This parameter is required.
        self.number_list = number_list
        self.owner_id = owner_id
        # The virtual number.
        # 
        # This parameter is required.
        self.phone_num = phone_num
        # The service name. Default value: **dyvms**.
        self.prod_code = prod_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The route type. Valid values:
        # 
        # *   **0**: number location first.
        # *   **1**: random.
        # 
        # This parameter is required.
        self.route_type = route_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.corp_name_list is not None:
            result['CorpNameList'] = self.corp_name_list

        if self.number_list is not None:
            result['NumberList'] = self.number_list

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.phone_num is not None:
            result['PhoneNum'] = self.phone_num

        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.route_type is not None:
            result['RouteType'] = self.route_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpNameList') is not None:
            self.corp_name_list = m.get('CorpNameList')

        if m.get('NumberList') is not None:
            self.number_list = m.get('NumberList')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PhoneNum') is not None:
            self.phone_num = m.get('PhoneNum')

        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RouteType') is not None:
            self.route_type = m.get('RouteType')

        return self

