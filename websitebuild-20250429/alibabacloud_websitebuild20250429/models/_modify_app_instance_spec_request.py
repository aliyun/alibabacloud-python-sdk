# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyAppInstanceSpecRequest(DaraModel):
    def __init__(
        self,
        application_type: str = None,
        biz_id: str = None,
        client_token: str = None,
        deploy_area: str = None,
        extend: str = None,
        payment_type: str = None,
        site_version: str = None,
    ):
        self.application_type = application_type
        self.biz_id = biz_id
        self.client_token = client_token
        self.deploy_area = deploy_area
        self.extend = extend
        self.payment_type = payment_type
        self.site_version = site_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_type is not None:
            result['ApplicationType'] = self.application_type

        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.deploy_area is not None:
            result['DeployArea'] = self.deploy_area

        if self.extend is not None:
            result['Extend'] = self.extend

        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type

        if self.site_version is not None:
            result['SiteVersion'] = self.site_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')

        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DeployArea') is not None:
            self.deploy_area = m.get('DeployArea')

        if m.get('Extend') is not None:
            self.extend = m.get('Extend')

        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')

        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')

        return self

