# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSiteResponseBody(DaraModel):
    def __init__(
        self,
        name_server_list: str = None,
        request_id: str = None,
        site_id: int = None,
        verify_code: str = None,
    ):
        # The list of name servers assigned to the site, separated by commas (,). This field has a value when the access type of the site is NS. You need to change the DNS servers of the site to these name servers. Then you can verify the site ownership and activate the site.
        self.name_server_list = name_server_list
        # The request ID.
        self.request_id = request_id
        # The site ID.
        self.site_id = site_id
        # The verification code of the site. When the access type of the site is CNAME, you need to add a TXT record with the record name **_esaauth.[site name]** and the record value set to the **verification code** on the DNS server of the site. Then you can verify the site ownership and activate the site.
        self.verify_code = verify_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name_server_list is not None:
            result['NameServerList'] = self.name_server_list

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.verify_code is not None:
            result['VerifyCode'] = self.verify_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NameServerList') is not None:
            self.name_server_list = m.get('NameServerList')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('VerifyCode') is not None:
            self.verify_code = m.get('VerifyCode')

        return self

