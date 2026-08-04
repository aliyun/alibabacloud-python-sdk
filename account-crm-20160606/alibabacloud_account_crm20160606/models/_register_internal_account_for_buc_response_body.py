# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_account_crm20160606 import models as main_models
from darabonba.model import DaraModel

class RegisterInternalAccountForBucResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.RegisterInternalAccountForBucResponseBodyData = None,
        localized_message: str = None,
        message: str = None,
        msg: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.localized_message = localized_message
        self.message = message
        self.msg = msg
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.localized_message is not None:
            result['LocalizedMessage'] = self.localized_message

        if self.message is not None:
            result['Message'] = self.message

        if self.msg is not None:
            result['Msg'] = self.msg

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.RegisterInternalAccountForBucResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('LocalizedMessage') is not None:
            self.localized_message = m.get('LocalizedMessage')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class RegisterInternalAccountForBucResponseBodyData(DaraModel):
    def __init__(
        self,
        account_status: str = None,
        account_structure: str = None,
        extend_info: str = None,
        havana_id: str = None,
        last_login_time: str = None,
        owner_bid: str = None,
        parent_pk: str = None,
        partner_pk: str = None,
        pk: str = None,
        site: str = None,
    ):
        self.account_status = account_status
        self.account_structure = account_structure
        self.extend_info = extend_info
        self.havana_id = havana_id
        self.last_login_time = last_login_time
        self.owner_bid = owner_bid
        self.parent_pk = parent_pk
        self.partner_pk = partner_pk
        self.pk = pk
        self.site = site

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_status is not None:
            result['AccountStatus'] = self.account_status

        if self.account_structure is not None:
            result['AccountStructure'] = self.account_structure

        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info

        if self.havana_id is not None:
            result['HavanaId'] = self.havana_id

        if self.last_login_time is not None:
            result['LastLoginTime'] = self.last_login_time

        if self.owner_bid is not None:
            result['OwnerBid'] = self.owner_bid

        if self.parent_pk is not None:
            result['ParentPk'] = self.parent_pk

        if self.partner_pk is not None:
            result['PartnerPk'] = self.partner_pk

        if self.pk is not None:
            result['Pk'] = self.pk

        if self.site is not None:
            result['Site'] = self.site

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountStatus') is not None:
            self.account_status = m.get('AccountStatus')

        if m.get('AccountStructure') is not None:
            self.account_structure = m.get('AccountStructure')

        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')

        if m.get('HavanaId') is not None:
            self.havana_id = m.get('HavanaId')

        if m.get('LastLoginTime') is not None:
            self.last_login_time = m.get('LastLoginTime')

        if m.get('OwnerBid') is not None:
            self.owner_bid = m.get('OwnerBid')

        if m.get('ParentPk') is not None:
            self.parent_pk = m.get('ParentPk')

        if m.get('PartnerPk') is not None:
            self.partner_pk = m.get('PartnerPk')

        if m.get('Pk') is not None:
            self.pk = m.get('Pk')

        if m.get('Site') is not None:
            self.site = m.get('Site')

        return self

