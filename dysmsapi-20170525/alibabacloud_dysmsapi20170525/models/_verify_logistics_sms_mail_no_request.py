# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class VerifyLogisticsSmsMailNoRequest(DaraModel):
    def __init__(
        self,
        express_company_code: str = None,
        mail_no: str = None,
        owner_id: int = None,
        platform_company_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # This parameter is required.
        self.express_company_code = express_company_code
        # This parameter is required.
        self.mail_no = mail_no
        self.owner_id = owner_id
        self.platform_company_code = platform_company_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.express_company_code is not None:
            result['ExpressCompanyCode'] = self.express_company_code

        if self.mail_no is not None:
            result['MailNo'] = self.mail_no

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.platform_company_code is not None:
            result['PlatformCompanyCode'] = self.platform_company_code

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpressCompanyCode') is not None:
            self.express_company_code = m.get('ExpressCompanyCode')

        if m.get('MailNo') is not None:
            self.mail_no = m.get('MailNo')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PlatformCompanyCode') is not None:
            self.platform_company_code = m.get('PlatformCompanyCode')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

